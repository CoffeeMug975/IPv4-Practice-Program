# Author: Daniel Asefa
# Date: 4/07/2026
# Purpose:
    # - Take question data, entered data & question type(nc_cidr / nc_subnet / yc_cidr / yc_subnet / yc_hosts)
    # - Display question and entered data for user to compare
    # - Compare entered vs question and check for errors

# Improvements 
    # - Create 1 field that they all can use
    # - Remove old testing lines

def check_answers(question_type: str, question_data_dict: dict, entered_data_dict: dict):
    # print(f"\n-----------\nQuestion Type: {question_type}\n")           # For testing, delete later
    # print(f"Question Data Dict: {question_data_dict}\n")                # For testing, delete later
    # print(f"Entered Data Dict: {entered_data_dict}\n-----------\n")     # For testing, delete later

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
            print(f"\n\n\t\t\tActual Values\t\tEntered Values\n"
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

            # Set up fields for question type
            fields = {
                "IPv4 Class": "ipv4_class",
                "CIDR": "cidr",
                "Block Size": "block_size",
                "Number of Subnets": "num_of_subnets"
            }

            # Display actual vs entered for user to compare
            print(f"\n\n\t\t\tActual Values\t\tEntered Values\n"
            f"IPv4 Class\t\t: {question_data_dict['ipv4_class']}\t\t\t: {entered_data_dict['ipv4_class']}\n"
            f"CIDR\t\t\t: {question_data_dict['cidr']}\t\t\t: {entered_data_dict['cidr']}\n"
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

        case "yc_cidr":

            # Set up fields for question type
            fields = {
                "IPv4 Class": "ipv4_class",
                "Subnet Mask": "subnet_mask",
                "Block Size": "block_size",
                "Number of Subnets": "num_of_subnets",
                "Number of Hosts": "num_of_hosts"
            }

            # Display actual vs entered for user to compare
            print(f"\n\n\t\t\tActual Values\t\tEntered Values\n"
            f"IPv4 Class\t\t: {question_data_dict['ipv4_class']}\t\t\t: {entered_data_dict['ipv4_class']}\n"
            f"Subnet Mask\t\t: {question_data_dict['subnet_mask']}\t: {entered_data_dict['subnet_mask']}\n"
            f"Block Size\t\t: {question_data_dict['block_size']}\t\t\t: {entered_data_dict['block_size']}\n"
            f"Number of Subnets\t: {question_data_dict['num_of_subnets']}\t\t\t: {entered_data_dict['num_of_subnets']}\n"
            f"Number of Hosts\t\t: {question_data_dict['num_of_hosts']}\t\t\t: {entered_data_dict['num_of_hosts']}\n"
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
                        
        case "yc_subnet":

            # Set up fields for question type
            fields = {
                "IPv4 Class": "ipv4_class",
                "CIDR": "cidr",
                "Block Size": "block_size",
                "Number of Subnets": "num_of_subnets",
                "Number of Hosts": "num_of_hosts"
            }

            # Display actual vs entered for user to compare
            print(f"\n\n\t\t\tActual Values\t\tEntered Values\n"
            f"IPv4 Class\t\t: {question_data_dict['ipv4_class']}\t\t\t: {entered_data_dict['ipv4_class']}\n"
            f"CIDR\t\t\t: {question_data_dict['cidr']}\t\t\t: {entered_data_dict['cidr']}\n"
            f"Block Size\t\t: {question_data_dict['block_size']}\t\t\t: {entered_data_dict['block_size']}\n"
            f"Number of Subnets\t: {question_data_dict['num_of_subnets']}\t\t\t: {entered_data_dict['num_of_subnets']}\n"
            f"Number of Hosts\t\t: {question_data_dict['num_of_hosts']}\t\t\t: {entered_data_dict['num_of_hosts']}\n"
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

        case "yc_hosts":

            # Set up fields for question type
            fields = {
                "IPv4 Class": "ipv4_class",
                "CIDR": "cidr",
                "Subnet Mask": "subnet_mask",
                "Block Size": "block_size",
                "Number of Subnets": "num_of_subnets",
                "Number of Hosts": "num_of_hosts"
            }

            # Display actual vs entered for user to compare
            print(f"\n\n\t\t\tActual Values\t\tEntered Values\n"
            f"IPv4 Class\t\t: {question_data_dict['ipv4_class']}\t\t\t: {entered_data_dict['ipv4_class']}\n"
            f"CIDR\t\t\t: {question_data_dict['cidr']}\t\t\t: {entered_data_dict['cidr']}\n"
            f"Subnet Mask\t\t: {question_data_dict['subnet_mask']}\t: {entered_data_dict['subnet_mask']}\n"            
            f"Block Size\t\t: {question_data_dict['block_size']}\t\t\t: {entered_data_dict['block_size']}\n"
            f"Number of Subnets\t: {question_data_dict['num_of_subnets']}\t\t\t: {entered_data_dict['num_of_subnets']}\n"
            f"Number of Hosts\t\t: {question_data_dict['num_of_hosts']}\t\t\t: {entered_data_dict['num_of_hosts']}\n"
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
