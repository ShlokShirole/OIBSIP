import psutil
import pyautogui
import os
from datetime import datetime


def get_battery_percentage():
    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is not available."

    percent = battery.percent

    if battery.power_plugged:
        return f"Battery is {percent} percent and charging."

    return f"Battery is {percent} percent."


def take_screenshot():
    folder = "Screenshots"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")
    filepath = os.path.join(folder, filename)

    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)

    return f"Screenshot saved successfully in the {folder} folder."
