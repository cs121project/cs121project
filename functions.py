import os
import time
import json
import random

with open('sdgs.json', 'r') as f:
    sdgs = json.load(f)

class SDG:
    def __init__(self, number):
        self.number = number
    
    def printTitleDes(self):
        print(f"Title: {sdgs[str(self.number)]['title']}\nDescription: {sdgs['1']['description']}")

NoPoverty = SDG(1)

NoPoverty.printTitleDes()

# print(f"Title: {sdgs['1']['title']}\nDescription: {sdgs['1']['description']}")