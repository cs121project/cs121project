import os
import time
import json
import random
from loginmenu import *
from rockpaperscissor import *

os.system('cls')

def SleepTime():
    time.sleep(3)
    os.system('cls')

def start():
    print("Welcome; I'm here to give you information about Sustainable Development Goals.")
    print('I will be your E-Book or Dictionary. I will also be your consultant.')

    print("\nNow, how may I help you?")
    print('[1] I was hoping you could give me the list of Sustainable Development Goals and give a brief definition.')
    print('[2] Go to Log In/Register Option and Challenge yourself with Quiz.')
    print('You can see if you improve your knowledge about the SDG, there will be a comparison once you finish the quiz.')
    print('[3] Rock/Paper/Scissor')
    print('If you win, you will get some fact/s and if you lose, you need to answer a question.')
    print('[0] Exit')

    choiceStart = int(input("\nWhat do you want to do?: "))
    if choiceStart == 1:
        SleepTime()
        SDGs()
    elif choiceStart == 2:
        SleepTime()
        LoginRegister()
    elif choiceStart == 3:
        SleepTime()
        play_game()
    elif choiceStart == 0:
        print("\nGoodbye!")
        time.sleep(3)
        exit()
    else:
        print("\nPlease choose between the given choices.")
        SleepTime()
        start()

def SDGs():
    SleepTime()
    SDGNumTitle = ["[SDG 1] No Poverty","[SDG 2] Zero Hunger","[SDG 3] Good Health and Well-being",
    "[SDG 4] Quality Education","[SDG 5] Gender Equality","[SDG 6] Clean Water and Sanitation",
    "[SDG 7] Affordable and Clean Energy","[SDG 8] Decent Work and Economic Growth",
    "[SDG 9] Industry, Innovation and Infrastructure","[SDG 10] Reduced Inequalities",
    "[SDG 11] Sustainable Cities and Communities","[SDG 12] Responsible Consumption and Production",
    "[SDG 13] Climate Action","[SDG 14] Life Below Water","[SDG 15] Life On Land",
    "[SDG 16] Peace, Justice and Strong Institutions","[SDG 17] Partnerships for the Goals"]

    for i in SDGNumTitle:
        print(i)
    
    choiceSDGs = int(input("\nWhat SDG do you want me to define for you (1-17)?: SDG "))

    if choiceSDGs == 1:
        NoPoverty.printTitleDes()
    elif choiceSDGs == 2:
        ZeroHunger.printTitleDes()
    elif choiceSDGs == 3:
        GoodHealthAndWellBeing.printTitleDes()
    elif choiceSDGs == 4:
        QualityEducation.printTitleDes()
    elif choiceSDGs == 5:
        GenderEquality.printTitleDes()
    elif choiceSDGs == 6:
        CleanWaterAndSanitation.printTitleDes()
    elif choiceSDGs == 7:
        AffordableAndCleanEnergy.printTitleDes()
    elif choiceSDGs == 8:
        DecentWorkAndEconomicGrowth.printTitleDes()
    elif choiceSDGs == 9:
        IndustryInnovationAndInfrastructure.printTitleDes()
    elif choiceSDGs == 10:
        ReducedInequalities.printTitleDes()
    elif choiceSDGs == 11:
        SustainableCitiesAndCommunities.printTitleDes()
    elif choiceSDGs == 12:
        ResponsibleConsumptionAndProduction.printTitleDes()
    elif choiceSDGs == 13:
        ClimateAction.printTitleDes()
    elif choiceSDGs == 14:
        LifeBelowWater.printTitleDes()
    elif choiceSDGs == 15:
        LifeOnLand.printTitleDes()
    elif choiceSDGs == 16:
        PeaceJusticeAndStrongInstitutions.printTitleDes()
    elif choiceSDGs == 17:
        PartnershipsForTheGoals.printTitleDes()
    else:
        print("\nPlease choose between the given choices.")
        time.sleep(3)
        os.system('cls')
        SDGs()

try:
    with open('sdgs.json', 'r') as f:
        sdgs = json.load(f)
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Error decoding JSON.")

class SDG:
    def __init__(self, number):
        self.number = number
    
    def printTitleDes(self):
        os.system('cls')
        print(f"Title: {sdgs[str(self.number)]['title']}\nDescription: {sdgs['1']['description']}\n")
            
        while True:
            FunctionsYesOrNo = input("Would you like to return, main menu or exit? [Return/Menu/Exit]: ").lower()
            if FunctionsYesOrNo == "return":
                os.system('cls')
                SDGs()
            elif FunctionsYesOrNo == "menu":
                os.system('cls')
                start()
            elif FunctionsYesOrNo == "exit":
                exit()
            else:
                print("\nPlease choose only from the option.\n")
                continue

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

start() # Where everything starts