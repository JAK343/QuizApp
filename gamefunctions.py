import math
from string import ascii_lowercase
import time
import random
import sys
from questions import *

def personalDetails():
    username = (input("Hello. What's your name?\n"))
    print(f"Hello {username}! Welcome to the quiz!")
    time.sleep(2)
    print(f"You will have 15 seconds to answer each question.")
    time.sleep(2)
    print(f"You will also get a bonus point if you can answer in under 5 seconds")
    time.sleep(2)

def playQuiz(scoreboard, numberOfQuestions, finalQuestionCount):
    numberOfQuestions = None

    while numberOfQuestions is None:
        try:
            numberOfQuestions = int(input(f"How many questions would you like in your quiz? You can choose between 1 and {len(Questions)}\n"))
        except ValueError:
            print(f"Please print a valid number")
        else:
            if numberOfQuestions > len(Questions):
                print(f"Please enter between 1 and {len(Questions)}")
                numberOfQuestions = None

    print(f"Okay then, {numberOfQuestions} questions coming up...")
    time.sleep(2)
    print(f"Good luck...")
    time.sleep(2)

    num_questions_in_quiz = min(numberOfQuestions, len(Questions))
    quiz_questions = random.sample(list(Questions.items()), k=num_questions_in_quiz)

    for num, (question, answers) in enumerate(quiz_questions, start=1):
        correct_answer = answers[0]
        labeled_answers = dict(zip(ascii_lowercase, random.sample(answers, k=len(answers))))
        if numberOfQuestions == finalQuestionCount:
            break
        print(f"{question}")
        for label, response in labeled_answers.items():
            print(f"{label}: {response}")

        timer = True
        valid_answer = True
        t1 = time.time()
        answer_index = input("Please choose a, b, c, or d...\n").lower()
        answer_index = answer_index.strip()
        if answer_index != "a" and answer_index != "b" and answer_index != "c" and answer_index != "d":
            print("Sorry, you didn't enter a, b, c, or d. No points there...")
            valid_answer = False
        t2 = time.time()
        t = math.floor(t2 - t1)
         
        if t >= 15:
            print("You ran out of time! Next question...")
            timer = False                    
        if timer == True and valid_answer == True:
            answer = labeled_answers[answer_index]
            if answer == correct_answer:
                print("Correct! Well done!")
                scoreboard += 1
                if t < 5:
                    print("And you scored a bonus point for your quick answer! Nice!")
                    scoreboard += 1
            else:
                print("Nope, that's not right...")
                print(f"The correct answer was {correct_answer}")
            timer = False
        time.sleep(2)
        finalQuestionCount += 1

    print(f"That's the end of the quiz...")
    time.sleep(2)
    print(f"Your final score is {scoreboard} out of a possible {finalQuestionCount * 2}")
    time.sleep(2)

    if scoreboard / (finalQuestionCount * 2) * 100 > 75:
        print(f"Wow! Very impressive!")
    elif scoreboard / (finalQuestionCount * 2) * 100 > 50:
        print(f"Pretty good. Still some room for improvement")
    elif scoreboard / (finalQuestionCount * 2) * 100 > 25:
        print(f"You got some right, but not the best score ever...")
    else:
        print(f"Better luck next time...")