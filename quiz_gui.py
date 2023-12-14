from tkinter import * 

# Create root window
root = Tk()
# Root window title and dimension
root.title("General knowledge quiz")
root.geometry('1000x500')

# Add label to root window
lbl = Label(root, text= "Welcome to the quiz!")
lbl.grid()

# Exceute tkinter
root.mainloop()