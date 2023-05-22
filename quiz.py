import random
import json

def record_score(users,username,score):
    users[username]["prev_score"]= score

    if score > users[username]["high_score"]:
        users[username]["high_score"] = score

    with open('users.json', 'w') as f:
        json.dump(users, f , indent=4 )


def quiz(users,username):
    print("previous score: ", users[username]["prev_score"],"           highscore: ", users[username]["high_score"])
    with open('questions.json','r') as f:
        questions = json.loads(f.read())

    random.shuffle(questions)

    score = 0   
    i=questions
    count = 0
    while count <= 9:
        print(f"\n{i[count]['question']} \n [1] {i[count]['options'][0]}\n [2] {i[count]['options'][1]}\n [3] {i[count]['options'][2]}\n [4] {i[count]['options'][3]}\n")

        user_answer = int(input("Enter the number of your answer: "))
        if i[count]['options'][int(user_answer)-1] == i[count]['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        count += 1

    print(f"final score: {score}") 
    record_score(users,username,score)
