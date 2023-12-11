from string import ascii_lowercase
import gamefunctions

numberOfQuestions = 0
scoreboard = 0

def personalDetails():
    username = (input("Hello. What's your name?\n"))
    print(f"Hello {username}! Welcome to the quiz!")


def finalScoreboard(scoreboard, numberOfQuestions):
    print(f"Your final score is {scoreboard} out of {numberOfQuestions}")
    if scoreboard / numberOfQuestions * 100 > 75:
        print(f"Wow! Very impressive!")
    elif scoreboard / numberOfQuestions * 100 > 50:
        print(f"Pretty good. Still some room for improvement")
    elif scoreboard / numberOfQuestions * 100 > 25:
        print(f"You got some right, but not the best score ever")
    else:
        print(f"Better luck next time...")

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

# Correct answer is set by index and answers are sorted. All answers are displayed and user asked
# to enter number for answer. Message returned. Scoreboard updated and presented at end of game

personalDetails()

for question, answers in Questions.items():
    correct_answer = answers[0]
    labeled_answers = dict(zip(ascii_lowercase, sorted(answers)))
    print(f"{question}")
    for label, response in labeled_answers.items():
        print(f"{label}: {response}")
    answer_index = input("Please choose a, b, c, or d...\n")
    answer = labeled_answers[answer_index]

    if answer == correct_answer:
        print("Correct! Well done!")
        scoreboard += 1
    else:
        print("Nope, that's not right...")
    numberOfQuestions += 1

finalScoreboard(scoreboard, numberOfQuestions)