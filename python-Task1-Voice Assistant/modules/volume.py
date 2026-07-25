import pyautogui


def increase():
    pyautogui.press("volumeup")


def decrease():
    pyautogui.press("volumedown")


def mute():
    pyautogui.press("volumemute")


def unmute():
    pyautogui.press("volumemute")  # Toggle mute
