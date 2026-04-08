# Author: Daniel Asefa
# Date: 4/07/2026
# Purpose:
    # - Take question data, question type, ask user question, and store response

from src.utils.check_answers import check_answers


def type_c_question(question_data_dict: dict, question_c: int):
    # Match entered data to question data
    # print(f"Question Data: {question_data_dict}")       # For testing, delete later 
    match question_c:
        case 1:
            question_type = str("yc_cidr")
            print(f"\nFor a CIDR of {question_data_dict["cidr"]} provide the following:\n")
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
            print(f"\nFor a Subnet Mask of {question_data_dict["subnet_mask"]} provide the following:\n")
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
            print(f"\nFor a Number of Hosts of {question_data_dict["num_of_hosts"]} provide the following:\n")
            entered_data_dict = {
                "ipv4_class": input(f"IPv4 Class\t\t: "),
                "cidr": input(f"CIDR\t\t\t: "),
                "subnet_mask": input(f"Subnet Mask\t\t: "),
                "block_size": input(f"Block Size\t\t: "),
                "num_of_subnets": input(f"Number of Subnets\t: "),
                "num_of_hosts": input(f"Number of Hosts\t\t: ")
            }
            # Execute method to compare inputted data to answers
            check_answers(question_type, question_data_dict, entered_data_dict)
        case __:
            print("Error: invalid question type of {question_c}")   # Should be impossible to get here
    return