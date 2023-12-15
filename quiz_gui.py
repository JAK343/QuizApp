from tkinter import *
from tkinter import messagebox as mb
import json


class Quiz:

    # Init method. Question number count at 0
    def __init__(self):
        self.q_number = 0
        self.display_title()
        self.display_question()
        self.chosen_answer = IntVar()
        self.opts= self.radio_buttons()
        self.display_options()
        self.button()
        self.seconds = 15
        self.timer_running = False
        # self.displayTimer()
        self.update_timer()
        self.finalQuestionCount=len(question)
        self.correct=0

    def display_title(self):
        title = Label(root, text="General knowledge quiz", width=55, fg="white", background="blue", font=("ariel", 20))
        title.place(x=5, y=5)
        bonus_point_message = Label(root, text="Answer within 5 seconds to score a bonus point!", fg="white", background="blue")
        bonus_point_message.place(x=300, y=100)

    def display_question(self):
        q_number = Label(root, text=question[self.q_number], width=60, bg="blue", fg="white", font=('ariel' , 16, 'bold'), anchor='w' )
        q_number.place(x=300, y=60)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(root, text="", variable=self.chosen_answer,
            value = len(q_list) + 1, font = ("ariel", 14, "bold"))

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

    # def displayTimer(self):
        # self.timer_label = Label(root, text="15", width=30)
        # self.timer_label.place(x = 700, y = 300)
        
    def update_timer(self):
        self.timer_running = True
        if self.timer_running and self.seconds > 0:
            self.seconds -= 1
            seconds = self.seconds % 60
            time = f"{seconds}"
            # self.timer_label.configure(text=time)
            root.after(1000, self.update_timer)
            """     if int(time) > 10:
                self.timer_label.configure(text=time, bg="green")
            elif int(time) < 10 and int(time) > 5:
                self.timer_label.configure(text=time, bg="orange")
            else:
                self.timer_label.configure(text=time, bg="red") """


    def button(self):
        
        next_button = Button(root, text="Next", command=self.next_btn, width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)

    # Game logic
    
    def check_answer(self, q_number):
        if self.chosen_answer.get() == answer[q_number]:
            return True
        
    def next_btn(self):
        if self.check_answer(self.q_number):
            self.correct += 1
            if self.seconds >= 10:
                self.correct += 1

        self.q_number += 1

        if self.q_number == self.finalQuestionCount:
            self.displayResult()
            root.destroy()
        else:
            self.seconds = 15
            self.display_question()
            self.display_options() 
            
    def displayResult(self):
        scoreboard = int(self.correct)
        
        if scoreboard / self.finalQuestionCount * 100 > 75:
            message = f"You scored {scoreboard} out of {self.finalQuestionCount * 2}. Wow! Very impressive!"
        elif scoreboard / self.finalQuestionCount * 100 > 50:
            message = f"You scored {scoreboard} out of {self.finalQuestionCount * 2}. Pretty good. Still some room for improvement"
        elif scoreboard / self.finalQuestionCount * 100 > 25:
            message = f"You scored {scoreboard} out of {self.finalQuestionCount * 2}. You got some right, but not the best score ever..."
        else:
            message = f"You scored {scoreboard} out of {self.finalQuestionCount * 2}. Better luck next time..."

        mb.showinfo("Result", f"{message}")

# Create root window

root = Tk()
# Root window 
root.configure(background="blue")
root.title("General knowledge quiz")
root.geometry('1000x500')

# Setting up json import
with open('questions.json') as f:
    data = json.load(f)

question = (data['Question'])
answer = (data['Answer'])
options = (data['Options'])

# Exceute tkinter
quiz = Quiz()
root.mainloop()