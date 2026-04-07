# Author: Daniel Asefa
# Purpose: 3/30/2026

# reference to "c" is about if the given question is in IPv4 Class C or not
import random
from src.utils.data_formatter import format_json_data

# Is this much case match good? Look into a better way

# Turn this into a callable .py file
def check_answers(question_type: str, question_data_dict: dict, entered_data_dict: dict):
    # check_answer() takes 3 arguments
        # question_type         This determines the answer response
            # (nc_cidr / nc_subnet / yc_cidr / yc_subnet / yc_hosts)
            # 1. nc_cidr    = Question that gives CIDR, is class A/B, and asks for all data except hosts 
            # 2. nc_subnet  = Question that gives Subnet, is class A/B, and asks for all data except hosts
            # 3. yc_cidr    = Question that gives CIDR, is a class C, and asks for all other data
            # 4. yc_subnet  = Question that gives Subnet, is a class C, and asks for all other data
            # 5. yc_hosts   = Question that gives hosts, is a class C, and asks for all other data

        # question_data_dict    This is the static answer data compared entered data is compared to
        # entered_data_dict     This is the user data that was entered
    print(f"\n-----------\nQuestion Type: {question_type}\n")
    print(f"Question Data Dict: {question_data_dict}\n")
    print(f"Entered Data Dict: {entered_data_dict}\n-----------\n")

    # I guess more case matches for each question type? Or is there a better way to do this?
    match question_type:
        case "nc_cidr":

            # Set up fields for this question type
            fields = {
                "IPv4 Class": "ipv4_class",
                "Subnet Mask": "subnet_mask",
                "Block Size": "block_size",
                "Number of Subnets": "num_of_subnets"
            }

            # Display actual vs entered for user to compare
            print(f"\t\t\tActual Values\t\tEntered Values\n"
            f"IPv4 Class\t\t: {question_data_dict['ipv4_class']}\t\t\t: {entered_data_dict['ipv4_class']}\n"
            f"Subnet Mask\t\t: {question_data_dict['subnet_mask']}\t\t: {entered_data_dict['subnet_mask']}\n"
            f"Block Size\t\t: {question_data_dict['block_size']}\t\t\t: {entered_data_dict['block_size']}\n"
            f"Number of Subnets\t: {question_data_dict['num_of_subnets']}\t\t\t: {entered_data_dict['num_of_subnets']}\n"
            "")
            

            # Check for errors & print if any
            errors = []

            for label, key in fields.items():
                if question_data_dict[key] != entered_data_dict[key]:
                    errors.append(label)

            if errors:
                print(f"Errors: " + ", ".join(errors))
            else:
                print("All correct, great job!!")

        case "nc_subnet":
            return("This is a nc_subnet question")
            # Compare entered data to question data and print results

        case "yc_cidr":
            print("This is a yc_cidr question")
            
            
        case "yc_subnet":
            print("This is a yc_subnet question")
        case "yc_hosts":
            print("This is a yc_hosts question")
    return "End string"

# Turn this into a callable .py file
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
            check_answers(question_type, question_data_dict, entered_data_dict)
        case 2:
            question_type = str("nc_subnet")
            print(f"For a Subnet Mask of {question_data_dict["subnet_mask"]} provide the following:\n")
            entered_data_dict = {
                "ipv4_class": input(f"IPv4 Class\t\t: "),
                "cidr": input(f"CIDR\t\t\t: "),
                "block_size": input(f"Block Size\t\t: "),
                "num_of_subnets": input(f"Number of Subnets\t: ")
            }
            # Execute method to compare inputted data to answers
            check_answers(question_type, question_data_dict, entered_data_dict)
        case __:
            print("Error: invalid question type of {question_not_c}")
    return

# Turn this into a callable .py file
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
            check_answers(question_type, question_data_dict, entered_data_dict)
        case 2:
            question_type = str("yc_subnet")
            print(f"For a Subnet Mask of {question_data_dict["subnet_mask"]} provide the following:\n")
            entered_data_dict = {
                "ipv4_class": input(f"IPv4 Class\t\t: "),
                "cidr": input(f"CIDR\t\t\t: "),
                "block_size": input(f"Block Size\t\t: "),
                "num_of_subnets": input(f"Number of Subnets\t: "),
                "num_of_hosts": input(f"Number of Hosts\t\t: ")
            }
            # Execute method to compare inputted data to answers
            check_answers(question_type, question_data_dict, entered_data_dict)
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
            check_answers(question_type, question_data_dict, entered_data_dict)
        case __:
            print("Error: invalid question type of {question_not_c}")
    return


def is_id_c(id_value: int) -> bool:
    if id_value >= 24:
        return True
    else:
        return False

# This is the main method of this page
def random_selection():
    global entered_data_dict
    global question_data_dict
    cidr_list = format_json_data()              # Generate list from JSON data 

    repeat_question = bool(True)

    while repeat_question:
        # Empty dictionary for new question (for now)
        entered_data_dict = {}
        question_data_dict = {}
        
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


        id_value = question_data_dict['cidr']
        if is_id_c(id_value):
            type_c_question(question_data_dict, question_c)
        
        if not is_id_c(id_value):
            not_type_c_question(question_data_dict, question_not_c)

        # repeat_question_decision = input (f"Enter \"new\"for an new question or \"back\" to go back to main menu\n: ")
        repeat_question_decision = input (f"-------------------------\nPress enter for new question OR enter \"back\" to go to main menu\n: ")
        if repeat_question_decision == "back":
            repeat_question = False