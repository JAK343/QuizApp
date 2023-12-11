username = (input("Hello. What's your name?\n"))
print(f"Hello {username}! Welcome to the quiz!")

numberOfQuestions = 0
scoreboard = 0

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

for question, answers in Questions.items():
    correct_answer = answers[0]
    sorted_answers = sorted(answers)

    for label, response in enumerate(sorted_answers):
        print(f"{label}: {response}")
    answer_index = int(input(f"{question}\nPlease choose 0, 1, 2, or 3\n"))
    answer = sorted_answers[answer_index]

    if answer == correct_answer:
        print("Correct! Well done!")
        scoreboard += 1
    else:
        print("Nope, that's not right...")
    numberOfQuestions += 1
print(f"So, your final score is...{scoreboard}")
