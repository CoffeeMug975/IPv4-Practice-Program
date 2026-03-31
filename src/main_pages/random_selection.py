# Author: Daniel Asefa
# Purpose: 3/30/2026

import random
from src.utils.data_formatter import format_json_data

def not_type_c_question(question_list: list, question_not_c: int) -> str:
    match question_not_c:
        case 1:
            print(f"For a CIDR of {question_list[0]} provide the following:\n")
            entered_ipv4_class = input(f"IPv4 Class: ")
            entered_subnet_mask = input(f"Subnet Mask: ")
            entered_block_size = input(f"Block Size: ")
            entered_num_of_subnets = input(f"Number of Subnets: ")
            entered_num_of_hosts = input(f"Number of Hosts: ")

            # Execute method to compare inputted data to answers
            # check_answers()
        case 2:
            print("Subnet Mask Question")
        case __:
            print("Error: invalid question type of {question_not_c}")
    return

# 5 varieties of CheckAnswer() is not a good thing
# Has to be a better way. Look into later

def type_c_question(question_list: list, question_c: int) -> str:
    print(f"Question List: {question_list}")
    print(f"Question Type: {question_c}")
    return "something"


def is_id_c(selection_id: int) -> bool:
    if selection_id >= 24:
        return True
    else:
        return False

def random_selection():
    input("Inside random option")

    cidr_list = format_json_data()              # Generate list from JSON data 
    selection_id = int(random.randint(1,24))    # Random number from 1 to 24 referencing id of JSON data
    question_c = random.randint(1,3)            # Question can give user one of 3 variables (CIDR / SubnetMask / Hosts)
    question_not_c = random.randint(1,2)        # Question can give user one of 2 variables (CIDR / SubnetMask)

    # print(f"Selection ID: {selection_id}\tType: {type(selection_id)}")      # This line is for testing - DELETE LATER

    # Get question data for given selection id and store it in a list
    #   question_list[0] = CIDR
    #   question_list[1] = IPv4 Class
    #   question_list[2] = Subnet Mask
    #   question_list[3] = Block Size
    #   question_list[4] = Number of subnets
    #   question_list[5] = Number of Hosts
    for cidr in cidr_list:
        if selection_id == cidr.getId():
            # print(cidr)                                                     # This line is for testing - DELETE LATER
            global question_list
            question_list =[cidr.getCidr()]
            question_list.append(cidr.getIpClass())
            question_list.append(cidr.getSubnetMask())
            question_list.append(cidr.getBlockSize())
            question_list.append(cidr.getNumberOfSubnets())
            question_list.append(cidr.getHosts())

    print(f"Question List outside: {question_list}")                        # This line is for testing - DELETE LATER

    if is_id_c(selection_id):
        print("Option 1")
        type_c_question(question_list, question_c)
        return
    
    if not is_id_c(selection_id):
        print("Option 1")
        not_type_c_question(question_list, question_not_c)
        return

    input ("Press enter to exit random test env.")

    # print (selection_id)

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

