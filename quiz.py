import random
import json

def quiz(users,username):
    print("previous score: ", users[username]["score"])
    with open('questions.json','r') as f:
        questions = json.loads(f.read())

    random.shuffle(questions)

    score = 0   
    for i in questions:
        
        print(f"\n{i['question']} \n {i['options']}\n")
        user_answer = int(input("Enter the number of your answer: "))
        if i['options'][int(user_answer)-1] == i['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    print(f"final score: {score}") 
    users[username]["score"]= score
