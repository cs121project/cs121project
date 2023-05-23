import json
import os
import time
from quiz import*
import getpass

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_users():
    with open('users.json') as f:
        users = json.load(f)
    return users

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f , indent=4 )

def login(users):
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username in users and users[username]['password'] == password:
        print('Login successful!')
        cls()
        quiz(users,username)

    else:
        print('Incorrect username or password. Please try again.')

def add_account(users):
    username = input('Enter a new username: ')
    password = input('Enter a new password: ')

    if username in users:
        print('Username already exists. Please choose a different username.')
        return

    users[username] = {'password': password, 'prev_score': 0 , 'high_score' : 0}
    save_users(users)
    print('New account added successfully!')

def LoginRegister():
    users = load_users()

    choice = input("What do you want to do?\n[1] Login \n[2] Register\n[3] Cancel\nENTER YOUR CHOICE:")

    if choice == '1':
        login(users)
        QuizChoice = input("\nWhat do you want to do? [Menu/Return]").lower()
        if QuizChoice == "menu":
            pass
        elif QuizChoice == "return":
            pass
        else:
            pass
    elif choice == '2':
        add_account(users)
    elif choice == '3':
        return
    else:
        print("Enter a Valid choice.")
        time.sleep(5)
        cls()
        return LoginRegister()