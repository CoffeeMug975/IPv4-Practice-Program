# Author: Daniel Asefa
# Date: 3/30/2026
# Purpose:
    # - Any reference to "c" is about if the given question is in IPv4 Class C or not
    # - Generate a random question, and random question type
    # - Depending of if IP address is of type C route to "type_c_question.py" or "not_type_c_question.py" 
    # - Method loops until user enters "back"

import random
from src.utils.data_formatter import format_json_data
from src.utils.not_type_c_question import not_type_c_question
from src.utils.type_c_question import type_c_question


def random_selection():
    # Set main variables for this function
    global entered_data_dict
    global question_data_dict
    cidr_list = format_json_data()                  # Generate list from JSON data 


    repeat_question = bool(True)
    while repeat_question:
        # Empty dictionary for new question
        entered_data_dict = {}
        question_data_dict = {}
        
        selection_id = int(random.randint(1,24))    # Random number from 1 to 24 referencing id of JSON data
        question_c = random.randint(1,3)            # Question can give user one of 3 variables (CIDR / SubnetMask / Hosts)
        question_not_c = random.randint(1,2)        # Question can give user one of 2 variables (CIDR / SubnetMask)

        # Get question data for given selection id and store it in a list
        for cidr in cidr_list:
            if selection_id == cidr.getId():
                question_data_dict = {
                    "cidr": str(cidr.getCidr()),
                    "ipv4_class": cidr.getIpClass(),
                    "subnet_mask": str(cidr.getSubnetMask()),
                    "block_size": str(cidr.getBlockSize()),
                    "num_of_subnets": str(cidr.getNumberOfSubnets()),
                    "num_of_hosts": str(cidr.getHosts())
                }


        id_value = int(question_data_dict['cidr'])
        if id_value >= 24:
            type_c_question(question_data_dict, question_c)
        else:
            not_type_c_question(question_data_dict, question_not_c)


        repeat_question_decision = input (f"-------------------------\nPress enter for new question OR enter \"back\" to go to main menu\n: ")
        if repeat_question_decision == "back":
            repeat_question = False