import tkinter as tk
from tkinter import ttk
import random

our_rand = random.randint(1,10)
def compare():
    if int(entry.get()) == our_rand:
        output_string.set("You guessed correctly!")
    elif int(entry.get()) < our_rand:
        output_string.set("Too cold!")
    else:
        output_string.set("Too hot!")

# Window
window = tk.Tk()
window.title("Guess the Number")
window.geometry("700x400")

# tkinter variables
int_var = tk.IntVar()

# Widgets
label = ttk.Label(window, text = "Hello, please try to guess a random number between 1-10, and I'll tell you if you're hot, cold or correct.", font = "Calibri, 10 bold")
label.pack()

entry = ttk.Entry(window, textvariable = int_var)
entry.pack()

button = ttk.Button(window, text = "Compare", command = compare)
button.pack()

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font = "Calibri 24", textvariable = output_string)
output_label.pack(pady = 3)

# Run
window.mainloop()