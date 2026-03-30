# Author: Daniel Asefa
# Date: 3-30-2026
# Purpose: Class for raw JSON data


class CidrData:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.cidr = data["cidr"]
        self.ipClass = data["ipClass"]
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
    
    def getIpClass(self):
        return self.ipClass

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
        return (f"{self.id}\t {self.cidr}\t {self.ipClass}\t {self.subnetMask}\t {self.blockSize}\t {self.numberOfSubnets}\t {self.hosts}")

    def showData(self):
        return (f"{self.cidr:>3}\t {self.ipClass}\t\t {self.subnetMask:<15}\t {self.blockSize:>3}\t {str(self.numberOfSubnets):>5}\t\t {self.hosts:>10,}")
