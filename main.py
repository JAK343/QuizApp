import math
from string import ascii_lowercase
import time

Questions = {"In what year did WW1 begin?": ["1914", "1917", "1920", "1923"],
             "How many wives did Henry VIII have?": ["6", "3", "0", "7"],
             "In what year did the Berlin Wall fall?":  ["1989", "1976", "1995", "1970"],
             "What is the capital city of Egypt?":  ["Cairo", "Kampala", "Rome", "Nairobi"],
             "What is the largest country in the world by area?": ["Russia", "China", "USA", "Canada"],
             "How many countries are there in Africa?": ["54", "25", "72", "95"],
             "Which country has won the Men's FIFA World Cup the most times?":  ["Brazil", "France", "Italy", "Argentina"],
             "How often are the Summer Olympic Games held?":  ["Every 4 years", "Every 2 years", "Every 6 years", "Every 8 years"],
             "At which track is the British F1 Grand Prix currently held?": ["Silverstone", "Brands Hatch", "Bedford Autodrome", "Anglesey Circuit"],

             }
numberOfQuestions = 0
scoreboard = 0
finalQuestionCount = 0


def personalDetails():
    username = (input("Hello. What's your name?\n"))
    print(f"Hello {username}! Welcome to the quiz!")

def playQuiz(scoreboard, numberOfQuestions, finalQuestionCount):
    numberOfQuestions = int(input(("How many questions would you like in your quiz?\n")))
    for question, answers in Questions.items():
        correct_answer = answers[0]
        labeled_answers = dict(zip(ascii_lowercase, sorted(answers)))
        if numberOfQuestions == finalQuestionCount:
            break
        print(f"{question}")
        for label, response in labeled_answers.items():
            print(f"{label}: {response}")

        timer = True
        t1 = time.time()
        answer_index = input("Please choose a, b, c, or d...\n")
        t2 = time.time()
        t = math.floor(t2 - t1)
         
        if t >= 10:
            print("You ran out of time! Next question...")
            timer = False                    
        if timer == True:
            answer = labeled_answers[answer_index]
            if answer == correct_answer:
                print("Correct! Well done!")
                scoreboard += 1
            else:
                print("Nope, that's not right...")
            timer = False
        finalQuestionCount += 1

    print(f"Your final score is {scoreboard} out of {finalQuestionCount}")
    if scoreboard / finalQuestionCount * 100 > 75:
        print(f"Wow! Very impressive!")
    elif scoreboard / finalQuestionCount * 100 > 50:
        print(f"Pretty good. Still some room for improvement")
    elif scoreboard / finalQuestionCount * 100 > 25:
        print(f"You got some right, but not the best score ever")
    else:
        print(f"Better luck next time...")

personalDetails()
playQuiz(scoreboard, numberOfQuestions, finalQuestionCount)
