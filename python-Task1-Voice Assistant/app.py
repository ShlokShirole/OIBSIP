from modules.speech import speak, take_command
from modules.commands import process_command
from config.settings import ASSISTANT_NAME


def main():
    speak(f"Hello! I am {ASSISTANT_NAME}, your Voice Assistant.")

    while True:
        command = take_command()

        if command:
            should_exit = process_command(command)

            if should_exit:
                break


if __name__ == "__main__":
    main()
