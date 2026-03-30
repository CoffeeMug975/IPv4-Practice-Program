# Author: Daniel Asefa
# Date: 3-27-2026
# Purpose: main function

from src.mainPages.ipv4TableSelection import displayIPv4Table
from src.mainPages.randomSelection import randomSelection
from src.mainPages.challengeSelection import challengeSelection
from src.mainPages.helpSelection import helpMenu

def mainMenu():
    global selection
    selection = input("\n\n\t\tWelcome to IPv4 Practice Application\n\nPlease choose from the following options:\n"
        "\t table       - View networking information table from /8 to /32\n"
        "\t random      - Questions are randomly selected \n"
        "\t challenge   - Timed mode with high scores\n"
        "\t help        - Click here to understand rules\n"
        "\t exit        - Exit application\n\n" \
        "\t: ")
    return selection


def main():
    running = bool(True)

    while running:
        mainMenu()
        match selection:
            case "table":
                displayIPv4Table()
            case "random":
                randomSelection()
            case "challenge":
                challengeSelection()
            case "help":
                helpMenu()
            case "exit":
                if selection == "exit":
                    running = False
            case __:
                print("Error: Invalid Input")

if __name__ == "__main__":
    main()
