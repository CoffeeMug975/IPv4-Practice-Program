# Author: Daniel Asefa
# Date: 3-27-2026
# Purpose: take JSON data and display it in a table

import json
import os

class CidrData:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.cidr = data["cidr"]
        self.subnetMask = data["subnetMask"]
        self.blockSize = data["blockSize"]
        self.numberOfSubnets = data["numberOfSubnets"]
        self.hosts = data["hosts"]

    # No need for setter, this is hard coded data that never changes

    # getters
    def getId(self):
        return self.id
    
    def getCidr(self):
        return self.cidr

    def getSubnetMask(self):
        return self.subnetMask
    
    def getBlockSize(self):
        return self.blockSize
    
    def getNumberOfSubnets(self):
        return self.numberOfSubnets
    
    def getHosts(self):
        return self.hosts
    
    # Str method
    def __str__(self):
        return (f"{self.id}\t {self.cidr}\t\t {self.subnetMask}\t {self.blockSize}\t {self.numberOfSubnets}\t {self.hosts}")

    def showData(self):
        return (f"{self.cidr:>3}\t {self.subnetMask:<15}\t {self.blockSize:>3}\t {str(self.numberOfSubnets):>5}\t\t {self.hosts:>10,}")



def displayJsonData():
    # Path for json file location
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "data.json")

    # load the JSON data
    with open(data_path, 'r') as f:
        json_data = json.load(f)
    
    cidrList = [CidrData(entry) for entry in json_data]

    for cidr in cidrList:
        print(cidr.showData())

    f.close()



def displayIPv4Table():
    title = str("IPv4 NETWORKING TABLE")
    line = "--------------------------------------------------------------------"
    print(f"\n{line}\n{title:^68}\n{line}\n"
    "CIDR\tSubnetMask         Block Size\t # of Subnets\t     Hosts\n"
    f"{line}")

    displayJsonData()
    
    print(f"{line}")

    input("\nPress any button to continue to main menu")
