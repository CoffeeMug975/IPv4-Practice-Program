# Author: Daniel Asefa
# Date: 3-27-2026
# Purpose: Take JSON data and display IPv4 table selection to the main menu, and add a way to return to the main menu after displaying the table

from src.utils.data_formatter import format_json_data



# Function for displaying table
def display_ipv4_table():
    title = str("IPv4 NETWORKING TABLE")
    line = str("-----------------------------------------------------------------------------------") # Line length is 83
    table_length = int(len(line))

    print(f"\n{line}\n{title:^{table_length}}\n{line}\n"
    "CIDR\tIpv4 Class\tSubnetMask         Block Size\t # of Subnets\t     Hosts\n"
    f"{line}")

    cidr_list = format_json_data()
    
    for cidr in cidr_list:
        print(cidr.showData())
    
    print(f"{line}")

    input("\nPress Enter to continue to main menu")
