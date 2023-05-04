import os
import time
from functions import *

os.system('cls')

def start():
    print("Welcome; I'm here to give you information about Sustainable Development Goals.")
    print('I will be your E-Book or Dictionary. I will also be your consultant.')

    print("\nNow, how may I help you?")
    print('[1] I was hoping you could give me the list of Sustainable Development Goals and give a brief definition.')
    print('You can view the Consultant Support in each section of SDGs.')
    print('[0] Exit')

    choiceStart = int(input("\nWhat do you want to do?: "))
    if choiceStart == 1:
        SDGs()
    elif choiceStart == 0:
        print("\nGoodbye!")
        time.sleep(3)
        exit()
    else:
        print("\nPlease choose between the given choices.")
        time.sleep(3)
        os.system('cls')
        start()

def SDGs():
    time.sleep(3)
    os.system('cls')
    
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
        NoPoverty()
    elif choiceSDGs == 2:
        ZeroHunger()
    elif choiceSDGs == 3:
        GoodHealthAndWellBeing()
    elif choiceSDGs == 4:
        QualityEducation()
    elif choiceSDGs == 5:
        GenderEquality()
    elif choiceSDGs == 6:
        CleanWaterAndSanitation()
    elif choiceSDGs == 7:
        AffordableAndCleanEnergy()
    elif choiceSDGs == 8:
        DecentWorkAndEconomicGrowth()
    elif choiceSDGs == 9:
        IndustryInnovationAndInfrastructure()
    elif choiceSDGs == 10:
        ReducedInequalities()
    elif choiceSDGs == 11:
        SustainableCitiesAndCommunities()
    elif choiceSDGs == 12:
        ResponsibleConsumptionAndProduction()
    elif choiceSDGs == 13:
        ClimateAction()
    elif choiceSDGs == 14:
        LifeBelowWater()
    elif choiceSDGs == 15:
        LifeOnLand()
    elif choiceSDGs == 16:
        PeaceJusticeAndStrongInstitutions()
    elif choiceSDGs == 17:
        PartnershipsForTheGoals()
    else:
        print("\nPlease choose between the given choices.")
        time.sleep(3)
        os.system('cls')
        SDGs()

start()