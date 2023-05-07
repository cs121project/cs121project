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
        #quiz(username) di pa tapos

    else:
        print('Incorrect username or password. Please try again.')

def add_account(users):
    username = input('Enter a new username: ')
    password = input('Enter a new password: ')

    if username in users:
        print('Username already exists. Please choose a different username.')
        return

    users[username] = {'password': password, 'score': 0}
    save_users(users)
    print('New account added successfully!')

def main():
    users = load_users()

    choice = input("What do you want to do:\n[1] login\n[2] register\n[3] cancel\nENTER YOUR CHOICE:")

    if choice == '1':
        login(users)
    elif choice == '2':
        add_account(users)
    elif choice == '3':
        return
    else:
        print("Enter a Valid choice")
        time.sleep(5)
        cls()
        return main()

main()