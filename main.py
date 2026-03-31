# Author: Daniel Asefa
# Date: 3-27-2026
# Purpose: main function

from src.main_pages.ipv4_table_selection import display_ipv4_table
from src.main_pages.random_selection import random_selection
from src.main_pages.challenge_selection import challenge_selection
from src.main_pages.help_selection import help_menu


def main_menu():
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

        selection = main_menu()
        match selection:
            case "table":
                display_ipv4_table()
            case "random":
                random_selection()
            case "challenge":
                challenge_selection()
            case "help":
                help_menu()
            case "exit":
                if selection == "exit":
                    running = False
            case __:
                print("Error: Invalid Input")

if __name__ == "__main__":
    main()
