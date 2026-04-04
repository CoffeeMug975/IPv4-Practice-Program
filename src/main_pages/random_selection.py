# Author: Daniel Asefa
# Purpose: 3/30/2026

import random
from src.utils.data_formatter import format_json_data

# 5 varieties of CheckAnswer() is not a good thing. Has to be a better way. Look into later
# Create one universal CheckAnswer()
# Is this much case match good? Look into a better way
# Have this page loop until user enters "back"

def check_answers(question_type: str, question_data_dict: dict, entered_data_dict: dict) -> str:
    # check_answer() takes 3 arguments
        # question_type         This determines the answer response
            #    Can make this a string + ensure that string is validated for security (is this needed?)
            # 1. nc_cidr    = This indicates it is a question that gives CIDR, is a class A/B, and asks for all data except hosts   Done 
            # 2. nc_subnet  = This indicates it is a question that gives Subnet, is a class A/B, and asks for all data except hosts Done
            # 3. yc_cidr    = This indicates it is a question that gives CIDR, is a class C, and asks for all other data            Done
            # 4. yc_subnet  = This indicates it is a question that gives Subnet, is a class C, and asks for all other data          d
            # 5. yc_hosts   = This indicates it is a question that gives hosts, is a class C, and asks for all other data           d

        # question_data_dict    This is the static answer data compared entered data is compared to
        # entered_data_dict     This is the user data that was entered
    print("do it")
    return "string"

def not_type_c_question(question_data_dict: dict, question_not_c: int):    
    # Match entered data to question
    print(f"Question Data: {question_data_dict}")
    match question_not_c:
        case 1:
            question_type = str("nc_cidr")
            print(f"For a CIDR of {question_data_dict["cidr"]} provide the following:\n")
            entered_data_dict = {
                "ipv4_class": input(f"IPv4 Class\t\t: "),
                "subnet_mask": input(f"Subnet Mask\t\t: "),
                "block_size": input(f"Block Size\t\t: "),
                "num_of_subnets": input(f"Number of Subnets\t: ")
            }
            # Execute method to compare inputted data to answers
            check_answers()
        case 2:
            question_type = str("nc_subnet")
            print(f"For a Subnet Mask of {question_data_dict["subnet_mask"]} provide the following:\n")
            entered_data_dict = {
                "ipv4_class": input(f"IPv4 Class\t\t: "),
                "cidr": input(f"CIDR\t\t\t\t: "),
                "block_size": input(f"Block Size\t\t: "),
                "num_of_subnets": input(f"Number of Subnets\t: ")
            }
            # Execute method to compare inputted data to answers
            check_answers()
        case __:
            print("Error: invalid question type of {question_not_c}")
    return


def type_c_question(question_data_dict: dict, question_c: int):
    # Match entered data to question
    print(f"Question Data: {question_data_dict}")
    match question_c:
        case 1:
            question_type = str("yc_cidr")
            print(f"For a CIDR of {question_data_dict["cidr"]} provide the following:\n")
            entered_data_dict = {
                "ipv4_class": input(f"IPv4 Class\t\t: "),
                "subnet_mask": input(f"Subnet Mask\t\t: "),
                "block_size": input(f"Block Size\t\t: "),
                "num_of_subnets": input(f"Number of Subnets\t: "),
                "num_of_hosts": input(f"Number of Hosts\t\t: ")
            }
            # Execute method to compare inputted data to answers
            check_answers()
        case 2:
            question_type = str("yc_subnet")
            print(f"For a Subnet Mask of {question_data_dict["subnet_mask"]} provide the following:\n")
            entered_data_dict = {
                "ipv4_class": input(f"IPv4 Class\t\t: "),
                "cidr": input(f"CIDR\t\t\t\t: "),
                "block_size": input(f"Block Size\t\t: "),
                "num_of_subnets": input(f"Number of Subnets\t: "),
                "num_of_hosts": input(f"Number of Hosts\t\t: ")
            }
            # Execute method to compare inputted data to answers
            check_answers()
        case 3:
            question_type = str("yc_hosts")
            print(f"For a number of hosts of {question_data_dict["hosts"]} provide the following:\n")
            entered_data_dict = {
                "ipv4_class": input(f"IPv4 Class\t\t: "),
                "cidr": input(f"CIDR\t\t\t\t: "),
                "subnet_mask": input(f"Subnet Mask\t\t: "),
                "block_size": input(f"Block Size\t\t: "),
                "num_of_subnets": input(f"Number of Subnets\t: "),
                "num_of_hosts": input(f"Number of Hosts\t\t: ")
            }
            # Execute method to compare inputted data to answers
            check_answers()
        case __:
            print("Error: invalid question type of {question_not_c}")

    return


def is_id_c(selection_id: int) -> bool:
    if selection_id >= 24:
        return True
    else:
        return False

def random_selection():
    global entered_data_dict
    global question_data_dict

    # Empty dictionary for new question (for now)
    entered_data_dict = {}
    question_data_dict = {}
    
    cidr_list = format_json_data()              # Generate list from JSON data 
    selection_id = int(random.randint(1,24))    # Random number from 1 to 24 referencing id of JSON data
    question_c = random.randint(1,3)            # Question can give user one of 3 variables (CIDR / SubnetMask / Hosts)
    question_not_c = random.randint(1,2)        # Question can give user one of 2 variables (CIDR / SubnetMask)

    # Get question data for given selection id and store it in a list
    for cidr in cidr_list:
        if selection_id == cidr.getId():
            question_data_dict = {
                "cidr": cidr.getCidr(),
                "ipv4_class": cidr.getIpClass(),
                "subnet_mask": cidr.getSubnetMask(),
                "block_size": cidr.getBlockSize(),
                "num_of_subnets": cidr.getNumberOfSubnets(),
                "hosts": cidr.getHosts()
            }


    if is_id_c(selection_id):
        type_c_question(question_data_dict, question_c)
    
    if not is_id_c(selection_id):
        not_type_c_question(question_data_dict, question_not_c)

    input ("Press enter to exit random test env.")