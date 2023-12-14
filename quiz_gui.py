from tkinter import *
from tkinter import messagebox as mb
import json


class Quiz:

    # Method to set question count to 0 and initialise all methods
    def __init__(self):
        self.q_number = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts= self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question)
        self.correct=0

    def display_title(self):
        title = Label(root, text="General knowledge quiz", width=50, bg="blue", fg="white", font=("ariel", 20) )
        title.place(x=0, y=2)

    def display_question(self):
        q_number = Label(root, text=question[self.q_number], width=60, font=('ariel' , 16, 'bold'), anchor='w' )
        q_number.place(x=70, y=100)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(root, text="", variable=self.opt_selected,
            value = len(q_list) + 1, font = ("ariel", 14))

            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
        return q_list
    
    
    def display_options(self):
        val=0
        self.opt_selected.set(0)

        for option in options[self.q_number]:
            self.opts[val]['text']=option
            val+=1

    def buttons(self):
        next_button = Button(root, text="Next", command=self.next_btn, width=10, bg="red", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)
        quit_button= Button(root, text="Quit", command=root.destroy, width=5, bg="red", fg="white", font=("ariel", 16, "bold"))
        quit_button.place(x=700, y=50)

    def displayResult(self):
        wrong_count = self.data_size - self.correct
        correct = f"You got {self.correct} correct"
        wrong = f"You got {wrong_count} wrong"

        score = int(self.correct / self.data_size * 100)
        result = f"You scored {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_answer(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True
        
    def next_btn(self):
        if self.check_answer(self.q_number):
            self.correct += 1

        self.q_number += 1

        if self.q_number == self.data_size:
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