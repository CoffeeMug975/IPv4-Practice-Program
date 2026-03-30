# Author: Daniel Asefa
# Date: 3-27-2026
# Purpose: Take JSON data and display IPv4 table selection to the main menu, and add a way to return to the main menu after displaying the table

from src.misc.dataFormatter import displayJsonData


# Function for displaying table
def displayIPv4Table():
    title = str("IPv4 NETWORKING TABLE")
    line = str("-----------------------------------------------------------------------------------") # Line length is 83
    tableLength = int(len(line))

    print(f"\n{line}\n{title:^{tableLength}}\n{line}\n"
    "CIDR\tIpv4 Class\tSubnetMask         Block Size\t # of Subnets\t     Hosts\n"
    f"{line}")

    cidrList = displayJsonData()
    
    for cidr in cidrList:
        print(cidr.showData())
    
    print(f"{line}")

    input("\nPress Enter to continue to main menu")
