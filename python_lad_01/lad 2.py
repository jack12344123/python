shopping_list = []
item = ''
while item != 'done':
    item = input("Enter a item: ")
    shopping_list.append(item)
print("shopping_list", shopping_list[0 : 1])
print("shopping_list", shopping_list[-2])
del shopping_list[-2]
print("shopping_list", shopping_list)