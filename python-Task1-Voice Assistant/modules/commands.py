from modules.speech import speak, take_command
from utils.datetime_utils import get_time, get_date

from modules.browser import (
    search_google,
    open_google,
    open_youtube,
    search_youtube,
    play_music,
)

from modules.applications import (
    open_notepad,
    open_calculator,
    open_paint,
    open_word,
    open_excel,
    open_powerpoint,
    open_vscode,
    open_chrome,
)

from modules.system import (
    get_battery_percentage,
    take_screenshot,
)

from modules import volume
from modules import brightness


def process_command(command):

    command = command.lower()

    # Greeting
    if any(word in command for word in ["hello", "hi", "hey"]):
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        speak(f"The current time is {get_time()}")

    # Date
    elif "date" in command:
        speak(f"Today's date is {get_date()}")

    # Open Google
    elif "open google" in command:
        speak("Opening Google")
        open_google()

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        open_youtube()

    # Google Search
    elif command.startswith("search "):
        query = command.replace("search", "", 1).strip()

        if query:
            speak(f"Searching Google for {query}")
            search_google(query)
        else:
            speak("Please tell me what to search.")

    # YouTube Search
    elif command.startswith("youtube "):
        query = command.replace("youtube", "", 1).strip()

        if query:
            speak(f"Searching YouTube for {query}")
            search_youtube(query)
        else:
            speak("Please tell me what to search on YouTube.")

    # Play Music
    elif command.startswith("play "):
        song = command.replace("play", "", 1).strip()

        if song:
            speak(f"Playing {song}")
            play_music(song)
        else:
            speak("Please tell me which song to play.")

    # Applications
    elif "open notepad" in command:
        speak("Opening Notepad")
        open_notepad()

    elif "open calculator" in command:
        speak("Opening Calculator")
        open_calculator()

    elif "open paint" in command:
        speak("Opening Paint")
        open_paint()

    elif "open word" in command:
        speak("Opening Microsoft Word")
        open_word()

    elif "open excel" in command:
        speak("Opening Microsoft Excel")
        open_excel()

    elif "open powerpoint" in command:
        speak("Opening Microsoft PowerPoint")
        open_powerpoint()

    elif "open vs code" in command or "open visual studio code" in command:
        speak("Opening Visual Studio Code")
        open_vscode()

    elif "open chrome" in command:
        speak("Opening Google Chrome")
        open_chrome()

    # Battery Percentage
    elif "battery" in command:
        battery = get_battery_percentage()
        speak(battery)

    # Screenshot
    elif "screenshot" in command or "capture screen" in command:
        speak("Taking screenshot")
        message = take_screenshot()
        speak(message)

    # ---------------- Volume ----------------

    elif "increase volume" in command:
        volume.increase()
        speak("Volume increased")

    elif "decrease volume" in command:
        volume.decrease()
        speak("Volume decreased")

    elif "mute volume" in command or command == "mute":
        volume.mute()
        speak("Volume muted")

    elif "unmute volume" in command:
        volume.unmute()
        speak("Volume unmuted")



        # ---------------- Brightness ----------------

    elif "increase brightness" in command:
        brightness.increase()
        speak("Brightness increased")

    elif "decrease brightness" in command:
        brightness.decrease()
        speak("Brightness decreased")

    elif "current brightness" in command:
        level = brightness.get_brightness()
        speak(f"Current brightness is {level} percent")

    elif "set brightness to" in command:
        try:
            percent = int(
                command.replace("set brightness to", "")
                .replace("percent", "")
                .strip()
            )
            brightness.set_brightness(percent)
            speak(f"Brightness set to {percent} percent")
        except:
            speak("Invalid brightness percentage")

    # Exit
    elif any(word in command for word in ["exit", "bye", "stop", "end", "quit"]):
        speak("Goodbye! Have a nice day.")
        return True

    else:
        speak("Sorry, I don't know that command.")

    return False
