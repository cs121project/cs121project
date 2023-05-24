import random
import json

def record_score(users,username,score):
    users[username]["prev_score"]= score

    if score > users[username]["high_score"]:
        users[username]["high_score"] = score

    try:
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
        print("Score recorded successfully.")
    except IOError:
        print("Error: Failed to write score to file.")

def quiz(users, username):
    print("Your Previous Score:", users[username]["prev_score"],"\nYour High Score:", users[username]["high_score"])
    with open('questions.json', 'r') as f:
        questions = json.loads(f.read())

    random.shuffle(questions)

    score = 0
    i = questions
    count = 0
    while count <= 9:
        print(f"\n{i[count]['question']} \n [1] {i[count]['options'][0]}\n [2] {i[count]['options'][1]}\n [3] {i[count]['options'][2]}\n [4] {i[count]['options'][3]}\n")

        try:
            user_answer = int(input("Enter the number of your answer: "))

            if user_answer > 4:
                print("Invalid input. This will be considered as wrong.")
                continue
            elif user_answer < 1:
                print("Invalid input. This will be considered as wrong.")
                continue

            if i[count]['options'][user_answer - 1] == i[count]['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
            count += 1

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nFinal score: {score}")

    if score > users[username]["prev_score"]:
        print("\nCongrats! You beat your previous score.")
    elif score < users[username]["prev_score"]:
        print("\nNice try, but your previous score was higher.")
    else:
        print("\nNothing changed. Your current score is the same as your previous score.")

    record_score(users, username, score)