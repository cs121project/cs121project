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
ZeroHunger = SDG(2)
GoodHealthAndWellBeing = SDG(3)
QualityEducation = SDG(4)
GenderEquality = SDG(5)
CleanWaterAndSanitation = SDG(6)
AffordableAndCleanEnergy = SDG(7)
DecentWorkAndEconomicGrowth= SDG(8)
IndustryInnovationAndInfrastructure= SDG(9)
ReducedInequalities = SDG(10)
SustainableCitiesAndCommunities = SDG(11)
ResponsibleConsumptionAndProduction = SDG(12)
ClimateAction = SDG(13)
LifeBelowWater = SDG(14)
LifeOnLand= SDG(15)
PeaceJusticeAndStrongInstitutions = SDG(16)
PartnershipsForTheGoals = SDG(17)