# Author: Daniel Asefa
# Purpose: 3/30/2026

import random
from src.utils.data_formatter import format_json_data

def random_selection():
    input("Inside random option")

    # Generate list from JSON data 
    cidr_List = format_json_data()

    # Select a random number from 1 to 24
    random_selection_id = random.randint(1,24)
    random_question_id = random.randint(1,3)
    # 1 = CIDR
    # 2 = Subnet Mask
    # 3 = Hosts

    print (random_selection_id)
    # Need a method to randomly select a line of the JSON data: example.py
    # Example:  Selected Line: 24;C;255.255.255.0;256;1;254

    # Need a method to randomly select 1 unique attribute of the JSON (this one is used in the question wording)
    # Example: Unique Selected Attribute: CIDR /24
    # 
    # Excepted Unique Selected Attributes:
    #               - CIDR
    #               - SubnetMask
    #               - Hosts 

    # Need a method that asks a series of questions based on the unique selected attribute
    # Example: For a "CIDR" of "/24" what is:
    #               - IPv4 Class
    #               - Subnet Mask
    #               - BlockSize  
    #               - #OfSubnets
    #               - Hosts(Only ask for hosts if CIDR >= 24 )


    input ("Press enter to exit random test env.")