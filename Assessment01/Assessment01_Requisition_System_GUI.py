import tkinter as tk
counter = 0
items = []
def add_item():
    item_name = item_name_entry.get()
    item_price = item_price_entry.get()
    if item_name == "" or item_price == "":
        output_label.config(text=" enter name and price.")
        return
    try:
        price = float(item_price)
    except ValueError:
        output_label.config(text="Price must be a number.")
        return

    items.append((item_name, price))
    items_listbox.insert(tk.END, f"{item_name} - ${price}")

    output_label.config(text="Item added.")
def calculate_total():
    total = 0
    for item in items:
        total += item[1]

    total_label.config(text="Total: $" + str(total))
    return total
def check_approval():
    global counter

    staff_name = staff_name_entry.get()
    staff_id = staff_id_entry.get()
    date = date_entry.get()

    if staff_name == "" or staff_id == "" or date == "":
        output_label.config(text="Please fill in Staff Name, Staff ID, and Date.")
        return

    if len(items) == 0:
        output_label.config(text="Please add one item.")
        return

    requisition_id = counter + 10000
    counter += 1
    total = calculate_total()
    status = "Pending"
    approval_ref = "NA"

    if total < 500:
        status = "Approved"
        last_three = str(requisition_id)[-3:]
        approval_ref = staff_id + last_three

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Printing requisitions:\n")
    result_text.insert(tk.END, "Date: " + date + "\n")
    result_text.insert(tk.END, "Requisition ID: " + str(requisition_id) + "\n")
    result_text.insert(tk.END, "Staff ID: " + staff_id + "\n")
    result_text.insert(tk.END, "Staff Name: " + staff_name + "\n")
    result_text.insert(tk.END, "Total: $" + str(total) + "\n")
    result_text.insert(tk.END, "Status: " + status + "\n")
    result_text.insert(tk.END, "Approval Reference Number: " + approval_ref)

    output_label.config(text="Approval successfully.")


window = tk.Tk()
window.title("Requisition System")
window.geometry("500x650")


tk.Label(window, text="Staff Name").pack()
staff_name_entry = tk.Entry(window, width=40)
staff_name_entry.pack()

tk.Label(window, text="Staff ID").pack()
staff_id_entry = tk.Entry(window, width=40)
staff_id_entry.pack()

tk.Label(window, text="Date").pack()
date_entry = tk.Entry(window, width=40)
date_entry.pack()

tk.Label(window, text="Item Name").pack()
item_name_entry = tk.Entry(window, width=40)
item_name_entry.pack()

tk.Label(window, text="Item Price").pack()
item_price_entry = tk.Entry(window, width=40)
item_price_entry.pack()

tk.Button(window, text="Add Item", command=add_item).pack(pady=5)
tk.Button(window, text="Calculate Total", command=calculate_total).pack(pady=5)
tk.Button(window, text="Check Approval", command=check_approval).pack(pady=5)

tk.Label(window, text="Items Added").pack()
items_listbox = tk.Listbox(window, width=50, height=8)
items_listbox.pack()

total_label = tk.Label(window, text="Total: $0")
total_label.pack(pady=10)

output_label = tk.Label(window, text="", fg="red")
output_label.pack()

result_text = tk.Text(window, width=50, height=12)
result_text.pack(pady=10)

window.mainloop()







