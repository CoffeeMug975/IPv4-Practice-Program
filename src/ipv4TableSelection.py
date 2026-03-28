import json
import os
import pprint

# Author: Daniel Asefa

# Lets think about this
# displayIPv4Table() should call getJsonData()
# Then come up with a fancy line to print each line






def displayIPv4Table():
    print("\n IPv4 NETWORKING TABLE\n"
    "CIDR\tSubnetMask\tBlock Size\t # of Hosts\t Hosts\n"
    )

    # Path for json file location
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "data.json")


    # load the JSON data
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    # Print data

    pprint.pprint(data)




    input("\nPress any button to continue to main menu")
