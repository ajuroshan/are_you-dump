import tkinter as tk
from tkinter import messagebox

import random


def update_label():
    messagebox.showinfo("YOU ARE DUMP", "I KNEW IT")

# def update_label():
#     label = tk.Label(root, text="I KNEW IT")


def move_button():
    button.place(x=random.randint(1, 350), y=random.randint(1, 350))


root = tk.Tk()
root.geometry("400x400")
label = tk.Label(root, text="ARE YOU DUMP")
label2 = tk.Label(root, text="ARE YOU DUMP")

button = tk.Button(root, text="NO", command=move_button)
button2 = tk.Button(root, text="YES", command=update_label)
label.pack()
button.pack()
button2.pack()
root.mainloop()
