import tkinter as tk

def calc():
    num1 = float(entry1.get())
    op = entry2.get()
    num2 = float(entry3.get())

    if op == "/":
        result = num1 / num2
    elif op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    else:
        result = "Invalid operator"

    result_label.config(text=str(result))


window = tk.Tk()
window.title("Calculator")
window.geometry("300x200")

tk.Label(window, text="num1").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="operator (+ - * /)").pack()
entry2 = tk.Entry(window)
entry2.pack()

tk.Label(window, text="num2").pack()
entry3 = tk.Entry(window)
entry3.pack()

tk.Button(window, text="Calculate", command=calc).pack()

result_label = tk.Label(window, text="=")
result_label.pack()

def clear():
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")

tk.Button(window, text="clear", command=clear).pack()


clear()
window.mainloop()