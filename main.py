import math
from string import ascii_lowercase
import time
import random
from gamefunctions import *

numberOfQuestions = 0
scoreboard = 0
finalQuestionCount = 0
play_round = True

personalDetails()
while play_round == True:
    playQuiz(scoreboard, numberOfQuestions, finalQuestionCount)
    time.sleep(2)
    user_choice = input("Would you like to play again? Please type yes or no\n").lower()
    user_choice = user_choice.strip()

    while user_choice != "yes" and user_choice != "no":
        user_choice = input("Please type yes or no\n").lower()
        user_choice = user_choice.strip()
    if user_choice == "no":
        play_round == False
        print("No worries. We hope you enjoyed the quiz!")
        break
    
