from tkinter import *
from tkinter.ttk import *
import random

def low():
  entry.delete(0, END)

  length = var1.get()

  lower = "abcdefghijklmnopqrtsuvwxyz"
  upper = "ABCDEFGHIJKLMNOPQRTSUVWXYZabcdefghijklmnopqrtsuvwxyz"
  digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
  password = ""

  if var.get() == 1:
    for i in range(0, length):
      password = password + random.choice(lower)
    return password

  elif var.get() == 0:
    for i in range(0, length):
      password = password + random.choice(upper)
    return password

  elif var.get() == 3:
    for i in range(0, length):
      password = password + random.choice(digits)
    return password

  else:
    print("Please choose an option")

def generate():
  password_1 = low()
  entry.insert(10, password_1)

root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")

password = Label(root, text = "Password")
password.grid(row = 0)

entry = Entry(root)
entry.grid(row = 0, column = 1)

length = Label(root, text = "Length")
length.grid(row = 1)

generate_button = Button(root,text = "Generate", command = generate)
generate_button.grid(row = 0, column = 2)

low_strength = Radiobutton(root, text = "Low", variable = var, value = 1)
low_strength.grid(row = 1, column = 2, sticky = "E")

middle_strength = Radiobutton(root, text = "Middle", variable = var,value = 0)
middle_strength.grid(row = 1,column = 3, sticky = "E")

strong_strength = Radiobutton(root, text = "Strong", variable = var, value = 3)
strong_strength.grid(row = 1, column = 4, sticky = "E")

combo = Combobox(root, textvariable = var1)


combo["values"] = (8,9,10,11,12,13,14,15,16,
                   17,18,19,20,21,22,23,24,25,26
                   ,27,28,29,30,31,32,"Length")

combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column = 1, row = 1)

root.mainloop()
