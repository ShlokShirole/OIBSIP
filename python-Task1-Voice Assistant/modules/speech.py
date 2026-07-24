import asyncio
import edge_tts
import pygame
import os
import tempfile
import speech_recognition as sr

VOICE = "en-US-GuyNeural"

pygame.mixer.init()


def speak(text):
    print(f"Assistant: {text}")

    async def _speak():
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_path = temp_file.name
        temp_file.close()

        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(temp_path)

        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove(temp_path)

    asyncio.run(_speak())


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source)

            print("Recognizing...")

            command = recognizer.recognize_google(audio)

            print(f"You: {command}")

            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

        except Exception as e:
            print(e)
            speak("Something went wrong.")
            return ""
