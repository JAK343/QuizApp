from tkinter import *
from tkinter import messagebox as mb
import json


class Quiz:

    # Method to set question count to 0 and initialise all methods
    def __init__(self):
        self.q_number = 0
        self.display_title()
        self.display_question()
        self.chosen_answer = IntVar()
        self.opts= self.radio_buttons()
        self.display_options()
        self.buttons()
        self.finalQuestionCount=len(question)
        self.correct=0

    def display_title(self):
        title = Label(root, text="General knowledge quiz", width=55, fg="black", font=("ariel", 20))
        title.place(x=5, y=5)

    def display_question(self):
        q_number = Label(root, text=question[self.q_number], width=60, font=('ariel' , 16, 'bold'), anchor='w' )
        q_number.place(x=300, y=100)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(root, text="", variable=self.chosen_answer,
            value = len(q_list) + 1, font = ("ariel", 14))

            q_list.append(radio_btn)
            radio_btn.place(x = 300, y = y_pos)
            y_pos += 40
        return q_list
    
    
    def display_options(self):
        val=0
        self.chosen_answer.set(0)

        for option in options[self.q_number]:
            self.opts[val]['text']=option
            val+=1

    def buttons(self):
        next_button = Button(root, text="Next", command=self.next_btn, width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)

    def displayResult(self):
        scoreboard = int(self.correct)
        
        if scoreboard / self.finalQuestionCount * 100 > 75:
            message = f"You scored {scoreboard} out of {self.finalQuestionCount}. Wow! Very impressive!"
        elif scoreboard / self.finalQuestionCount * 100 > 50:
            message = f"You scored {scoreboard} out of {self.finalQuestionCount}. Pretty good. Still some room for improvement"
        elif scoreboard / self.finalQuestionCount * 100 > 25:
            message = f"You scored {scoreboard} out of {self.finalQuestionCount}. You got some right, but not the best score ever..."
        else:
            message = f"You scored {scoreboard} out of {self.finalQuestionCount}. Better luck next time..."

        mb.showinfo("Result", f"{message}")

    def check_answer(self, q_number):
        if self.chosen_answer.get() == answer[q_number]:
            return True
        
    def next_btn(self):
        if self.check_answer(self.q_number):
            self.correct += 1

        self.q_number += 1

        if self.q_number == self.finalQuestionCount:
            self.displayResult()
            root.destroy()
        else:
            self.display_question()
            self.display_options() 


# Create root window

root = Tk()
# Root window 
root.title("General knowledge quiz")
root.geometry('1000x500')

# Setting up json import
with open('questions.json') as f:
    data = json.load(f)

question = (data['Question'])
answer = (data['Answer'])
options = (data['Options'])


quiz = Quiz()
# Exceute tkinter
root.mainloop()