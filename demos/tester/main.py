#!/usr/bin/env python3
try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None
import logging
import os
import subprocess
from logging import getLogger

import pyudev
import serial
import time

BAUD = 115200
DEFAULT_TIMEOUT = 30
IMAGE_WRITE_TIMEOUT = 120
ESP_IMAGE = "ESP32_GENERIC_C3-20250809-v1.26.0.bin"
BUZZER_PIN = 22

logger = getLogger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(logging.StreamHandler())


esp_files = os.listdir("esp_files")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = None


if GPIO is not None:
    pwm = GPIO.PWM(BUZZER_PIN, 440)  # Default frequency


def buzzer(frequency=440, duration=1, repeats=1, interval=0.2, duty_cycle=50):
    if pwm is None:
        logger.warning("RPi.GPIO not available, skipping buzzer test.")
        return
    for _ in range(repeats):
        pwm.start(duty_cycle)
        pwm.ChangeFrequency(frequency)
        try:
            time.sleep(duration)
        finally:
            pwm.stop()
        time.sleep(interval)


def play_intro_melody():
    # Melody: list of (frequency, duration, duty_cycle)
    melody = [
        (523, 0.2, 50),  # C5
        (587, 0.2, 50),  # D5
        (659, 0.2, 50),  # E5
        (698, 0.2, 50),  # F5
        (784, 0.3, 50),  # G5
    ]
    for note in melody:
        freq, dur, duty = note
        buzzer(frequency=freq, duration=dur, duty_cycle=duty, repeats=1, interval=0.05)


def run_demo(port: str):
    ser = serial.Serial(port, BAUD, timeout=1)
    ser.write(b"\x03")  # Ctrl-C to stop any running program
    time.sleep(0.1)
    ser.write(b"\x05")
    time.sleep(0.05)
    with open("test.py", "r") as f:
        for line in f:
            ser.write(line.encode().replace(b"\n", b"\r\n"))
            time.sleep(0.01)
    ser.write(b"\x04")
    time.sleep(0.1)
    response = ser.read_all().decode()
    ser.close()
    return response


def flash_demo(port: str):
    output = subprocess.check_output(["esptool.py", "-p", port, "erase_flash"], timeout=DEFAULT_TIMEOUT)
    if b"Chip erase completed successfully" not in output and b"Flash memory erased successfully" not in output:
        raise RuntimeError("Flash erase failed. Output: " + output.decode())
    output = subprocess.check_output(
        ["esptool.py",  "-p", port, "--baud", "460800", "write_flash", "0", ESP_IMAGE],
        timeout=IMAGE_WRITE_TIMEOUT,
    )
    if b"Hash of data verified" not in output:
        raise RuntimeError("Flash write failed. Output: " + output.decode())
    return True


def esp_files_touch():
    output = subprocess.check_output(["mpremote", "fs", "ls"], timeout=DEFAULT_TIMEOUT).decode()
    if "ls :" not in output:
        raise RuntimeError("Failed to list files on device")
    for file in esp_files:
        if file not in output:
            subprocess.check_output(["mpremote", "fs", "cp", f"esp_files/{file}", ":"], timeout=DEFAULT_TIMEOUT)


def search_devices():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='tty')
    is_running = False
    for device in iter(monitor.poll, None):
        if device.action == 'add' and not is_running:
            logger.info(f"USB Device detected: {device}")
            buzzer(1500, 0.5)
            is_running = True
            response = ""
            try:
                esp_files_touch()
            except Exception as e:
                logger.warning(f"Error syncing files: {e}")
            try:
                response = run_demo(device.device_node)
            except Exception as e:
                logger.warning(f"Error running demo: {e}")
            if "hello world" in response:
                logger.info("Demo ran successfully!")
                buzzer(2000, 0.5, 2, 0.5)
            else:
                logger.warning("Demo did not run as expected.")
                buzzer(100, 3)
                try:
                    flash_demo(device.device_node)
                except Exception as e:
                    logger.warning(f"Error flashing demo: {e}")
                    buzzer(100, 3)
                else:
                    logger.info("Flashing successful.")
                    buzzer(2200, 0.5, 3, 0.5)
            time.sleep(0.1)
        elif device.action == 'remove':
            logger.info(f"USB Device disconnected: {device}")
            is_running = False


if __name__ == '__main__':
    logger.info("Initializing USB monitor...")
    play_intro_melody()
    search_devices()
