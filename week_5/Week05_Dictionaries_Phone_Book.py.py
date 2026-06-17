phone_book = {}  # empty dictionary
while True:
    name = input('please enter your name: ')
    if name == 'stop':
        break
    phone = input('please enter your phone number: ')
    if phone == 'stop':
        break
    phone_book[name] = phone  # store it properly

print(phone_book)
# print all
for name, phone in phone_book.items():
    print(name, ":", phone)


