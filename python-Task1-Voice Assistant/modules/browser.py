import webbrowser
import pywhatkit


def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")


def search_youtube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


def play_music(song):
    pywhatkit.playonyt(song)            
