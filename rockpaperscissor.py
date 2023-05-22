import random
import json
import os

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
        print(f'You win! Here is a fun fact: {fun_facts[str(random.randint(1, 80))]}')
    elif rules[computer_choice] == user_choice:
        question = questions[str(random.randint(1, 80))]
        print('You lose! Here is a question:')
        print(question['question'])
        
        for key, value in question['choices'].items():
            print(f"{key.upper()}: {value}")
        user_answer = input('Answer: ').upper()
        if user_answer == question['answer'].lower():
            print('Correct!')
        else:
            print('Incorrect!')
    else:
        print('It\'s a tie!')

def play_game():
    while True:
        print("Welcome to Rock-Paper-Scissors game!")
        print("\nWhat would you like to do/know?: ")
        print("1. Play\n2. How to play\n3. About\n4. Exit")
        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            num_rounds = int(input('\nHow many rounds do you want to play?: '))
            print()
            for i in range(num_rounds):
                print(f'Round {i+1}:')
                play_round()
                input("\nPress any key to continue...")
                os.system('cls')

        elif choice == '2':
            print("How to play:\n"
                  "1. Choose either rock, paper, or scissors by entering the corresponding number.\n"
                  "2. Rock beats scissors, scissors beats paper, and paper beats rock.\n"
                  "3. You will earn a point if you win a round, and lose a point if you lose a round.\n"
                  "4. At the end of the game, your total score will be displayed.\n")

        elif choice == '3':
            print("About:\n"
                  "The Sustainable Development Goals (SDGs) are a set of 17 interconnected goals that aim to address "
                  "global challenges such as poverty, hunger, education, gender equality, clean water, energy, "
                  "economic growth, sustainable cities, climate action, and more. By working towards these goals, "
                  "we can create a better future for all, leaving no one behind.\n")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.\n")