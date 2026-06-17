def add_item():
    item_name = item_name_entry.get()
    item_price = item_price_entry.get()

    if item_name == "" or item_price == "":
        output_label.config(text="Please enter both item name and price.")
        return

    try:
        item_price = float(item_price)
    except:
        output_label.config(text="Price must be a number.")
        return
