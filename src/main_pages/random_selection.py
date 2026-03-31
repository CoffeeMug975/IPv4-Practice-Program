# Author: Daniel Asefa
# Purpose: 3/30/2026

import random
from src.utils.data_formatter import format_json_data

# 5 varieties of CheckAnswer() is not a good thing. Has to be a better way. Look into later
# Create one universal CheckAnswer()
# Is this much case match good? Look into a better way
# Have this page loop until user enters "back"

def not_type_c_question(question_list: list, question_not_c: int) -> str:
    match question_not_c:
        case 1:
            print(f"For a CIDR of {question_list[0]} provide the following:\n")
            entered_ipv4_class = input(f"IPv4 Class: ")
            entered_subnet_mask = input(f"Subnet Mask: ")
            entered_block_size = input(f"Block Size: ")
            entered_num_of_subnets = input(f"Number of Subnets: ")

            # Execute method to compare inputted data to answers
            # check_answers()
        case 2:
            print(f"For a Subnet Mask of {question_list[1]} provide the following:\n")
            entered_ipv4_class = input(f"IPv4 Class: ")
            entered_cidr = input(f"CIDR: ")
            entered_block_size = input(f"Block Size: ")
            entered_num_of_subnets = input(f"Number of Subnets: ")

            # Execute method to compare inputted data to answers
            # check_answers()
        case __:
            print("Error: invalid question type of {question_not_c}")
    return


def type_c_question(question_list: list, question_c: int) -> str:
    print(f"Question List: {question_list}")
    print(f"Question Type: {question_c}")
    match question_c:
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
            print(f"For a Subnet Mask of {question_list[1]} provide the following:\n")
            entered_ipv4_class = input(f"IPv4 Class: ")
            entered_cidr = input(f"CIDR: ")
            entered_block_size = input(f"Block Size: ")
            entered_num_of_subnets = input(f"Number of Subnets: ")
            entered_num_of_hosts = input(f"Number of Hosts: ")

            # Execute method to compare inputted data to answers
            # check_answers()
        case 3:
            print(f"For a number of hosts of {question_list[2]} provide the following:\n")
            entered_ipv4_class = input(f"IPv4 Class: ")
            entered_cidr = input(f"CIDR: ")
            entered_subnet_mask = input(f"Subnet Mask: ")
            entered_block_size = input(f"Block Size: ")
            entered_num_of_subnets = input(f"Number of Subnets: ")
            entered_num_of_hosts = input(f"Number of Hosts: ")

            # Execute method to compare inputted data to answers
            # check_answers()
        case __:
            print("Error: invalid question type of {question_not_c}")

    return "something"


def is_id_c(selection_id: int) -> bool:
    if selection_id >= 24:
        return True
    else:
        return False

def random_selection():
    cidr_list = format_json_data()              # Generate list from JSON data 
    selection_id = int(random.randint(1,24))    # Random number from 1 to 24 referencing id of JSON data
    question_c = random.randint(1,3)            # Question can give user one of 3 variables (CIDR / SubnetMask / Hosts)
    question_not_c = random.randint(1,2)        # Question can give user one of 2 variables (CIDR / SubnetMask)

    # Get question data for given selection id and store it in a list
    for cidr in cidr_list:
        if selection_id == cidr.getId():
            global question_list
            question_list = [cidr.getCidr()]                    # question_list[0] = CIDR
            question_list.append(cidr.getIpClass())             # question_list[1] = IPv4 Class
            question_list.append(cidr.getSubnetMask())          # question_list[2] = Subnet Mask
            question_list.append(cidr.getBlockSize())           # question_list[3] = Block Size
            question_list.append(cidr.getNumberOfSubnets())     # question_list[4] = Number of subnets
            question_list.append(cidr.getHosts())               # question_list[5] = Number of Hosts

    if is_id_c(selection_id):
        type_c_question(question_list, question_c)
        return
    
    if not is_id_c(selection_id):
        not_type_c_question(question_list, question_not_c)
        return

    input ("Press enter to exit random test env.")