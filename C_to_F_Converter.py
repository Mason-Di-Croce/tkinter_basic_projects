import tkinter as tk
from tkinter import ttk

def convert():
    output_string.set(str(float(entry.get()) * 1.8 + 32) + "F")


# Window
window = tk.Tk()
window.title("Celcius to Farenheit")
window.geometry("500x250")

# Title
title_label = ttk.Label(master = window, text = "Celcius to Farenheit", font = "Calibri 24 bold")
title_label.pack()

# Input
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font = "Calibri 24", textvariable = output_string)
output_label.pack(pady = 3)

# Run
window.mainloop()