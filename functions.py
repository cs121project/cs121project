import os
import time
import json
import random

with open('sdgs.json', 'r') as f:
    sdgs = json.load(f)

class SDG:
    def __init__(self, title, description):
        self.title
        self.description
    
    def printTitleDes(self):
        print(f"Title: {sdgs['1']['title']}\nDescription: {sdgs['1']['description']}")