import tkinter as tk

window = tk.Tk()
window.title("My first window")
window.geometry("400x1200")

tk.Label(window, text="Item name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Item price").pack()
price_entry = tk.Entry(window)
price_entry.pack()

dicshar = {}

def addItem():
    name = name_entry.get()
    price = float(price_entry.get())  # convert to number
    dicshar[name] = price

    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def calculatePrice():
    total = 0
    for item in dicshar:
        total += dicshar[item]
    return total

def displayPrice():
    total = calculatePrice()
    result_label.config(text="Total: $" + str(total))

# Buttons
tk.Button(window, text="Add Item", command=addItem).pack()
tk.Button(window, text="Calculate Total", command=displayPrice).pack()

# Output label
result_label = tk.Label(window, text="Total: $0")
result_label.pack()


window.mainloop()