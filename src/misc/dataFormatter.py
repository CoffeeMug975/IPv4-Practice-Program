# Author: Daniel Asefa
# Date: 3-30-2026
# Purpose: Take JSON data format it into a list and return it

import json
import os
from src.misc.CidrDataClass import CidrData


# Get JSON data, convert to a list and close JSON 
def formatJsonData():
    # Path for json file location
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))     # base_dir = ../../../
    data_path = os.path.join(base_dir, "data", "data.json")                                     # data_path = base_dir/data/data.json

    # load the JSON data
    with open(data_path, 'r') as f:
        json_data = json.load(f)
    f.close()
    
    cidrList = [CidrData(entry) for entry in json_data]

    return cidrList