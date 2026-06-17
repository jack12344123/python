import tkinter as tk
from unittest import result

window = tk.Tk()
window.title("celsius window")
window.geometry("400x1200")

tk.Label(window, text="tep").pack()
name_entry = tk.Entry(window)
name_entry.pack()
def celsius():

    celsius = float(name_entry.get())
    fahrenheit = (celsius * 9 / 5) + 32
    result_label.config(text="fahrenheit = " + str(fahrenheit) + "F")
tk.Button(window, text="Calculate", command=celsius).pack()
result_label = tk.Label(window, text="")
result_label.pack()
def clear():
    name_entry.delete(0, "end")


tk.Button(window, text="clear", command=clear).pack()



clear()
window.mainloop()


