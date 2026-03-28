# Author: Daniel Asefa
# 
# 1.    
# 2.    
# 2.    

from src.ipv4TableSelection import displayIPv4Table


# Inefficient to hard code all this.
# Create a loop that pulls from the json and formats it 

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
                print("random option selected")
            case "challenge":
                print("challenge option selected")
            case "help":
                print("help option selected")
            case "exit":
                if selection == "exit":
                    running = False
            case __:
                print("Error: Invalid Input")

if __name__ == "__main__":
    main()
