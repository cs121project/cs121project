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
    while True:
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        if username in users and users[username]['password'] == password:
            print('Login successful!')
            cls()
            quiz(users,username)

        else:
            print('Incorrect username or password. Please try again.')

        lmchoice = input("\nWant to try again? [Yes/No]: ").lower()

        if lmchoice == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif lmchoice == "no":
            break
        else:
            print("\nPlease choose only from the given choice.")
            continue

def add_account(users):
    username = input('Enter a new username: ')
    password = input('Enter a new password: ')

    if username in users:
        print('Username already exists. Please choose a different username.')
        return

    users[username] = {'password': password, 'prev_score': 0 , 'high_score' : 0}
    save_users(users)
    print('New account added successfully!')