import random
import json
import os
import time

def load_json(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in file '{file_path}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading '{file_path}': {str(e)}")

rules = load_json('rpsrules.json')
questions = load_json('rpsquestions.json')
fun_facts = load_json('rpsfunfacts.json')


def play_round():
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    while True:
        user_choice = input('Choose rock (1), paper (2), or scissors (3): ')
        if user_choice not in choices:
            print('Invalid choice!')
        else:
            user_choice = choices[user_choice]
            break

   
    if user_choice == 'rock':
        print('You chose rock:')
        print('    _______')
        print('---\'   ____)')
        print('      (_____)')
        print('      (_____)')
        print('      (____)')
        print('---.__(___)')
    elif user_choice == 'paper':
        print('You chose paper:')
        print('     _______')
        print('---\'    ____)____')
        print('           ______)')
        print('          _______)')
        print('         _______)')
        print('---.__________)')
    elif user_choice == 'scissors':
        print('You chose scissors:')
        print('    _______')
        print('---\'   ____)____')
        print('          ______)')
        print('       __________)')
        print('      (____)')
        print('---.__(___)')

    computer_choice = random.choice(list(rules.keys()))
 
    if computer_choice == 'rock':
        print('Computer chose rock:')
        print('    _______')
        print('---\'   ____)')
        print('      (_____)')
        print('      (_____)')
        print('      (____)')
        print('---.__(___)')
    elif computer_choice == 'paper':
        print('Computer chose paper:')
        print('     _______')
        print('---\'    ____)____')
        print('           ______)')
        print('          _______)')
        print('         _______)')
        print('---.__________)')
    elif computer_choice == 'scissors':
        print('Computer chose scissors:')
        print('    _______')
        print('---\'   ____)____')
        print('          ______)')
        print('       __________)')
        print('      (____)')
        print('---.__(___)')

    if rules[user_choice] == computer_choice:
        print(f'\nYou win!\nHere is a fun fact: {fun_facts[str(random.randint(1, 80))]}')
    elif rules[computer_choice] == user_choice:
        question = questions[str(random.randint(1, 80))]
        print('\nYou lose!\nHere is a question:')
        print(question['question'])
        
        for key, value in question['choices'].items():
            print(f"{key.upper()}: {value}")
        user_answer = input('\nAnswer: ').upper()
        if user_answer == question['answer'].lower():
            print('Correct!')
        else:
            print('Incorrect!')
    else:
        print('It\'s a tie!')