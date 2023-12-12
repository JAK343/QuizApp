import math
from string import ascii_lowercase
import time
import random
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
    numberOfQuestions = int(input(("How many questions would you like in your quiz? You can select up to 9 questions\n")))
    while numberOfQuestions > len(Questions):
        numberOfQuestions = int(input("Please choose between 1 and 9 questions...\n"))
    print(f"Ok then, {numberOfQuestions} questions coming up...")
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
        t1 = time.time()
        answer_index = input("Please choose a, b, c, or d...\n")
        t2 = time.time()
        t = math.floor(t2 - t1)
         
        if t >= 15:
            print("You ran out of time! Next question...")
            timer = False                    
        if timer == True:
            answer = labeled_answers[answer_index]
            if answer == correct_answer:
                print("Correct! Well done!")
                scoreboard += 1
                if t < 5:
                    print("And you scored a bonus point for your quick answer! Nice!")
                    scoreboard += 1
            else:
                print("Nope, that's not right...")
            timer = False
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