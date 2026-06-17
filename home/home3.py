from datetime import date
year = int(input("enter birth_date year: "))
today = date.today()
while year > today.year:
    print("this year is too young")
    year = int(input("Enter birth year again: "))
month = int(input("enter birth_date  month: "))
day = int(input("enter birth_date  day: "))
from datetime import date
birth_date = date(year, month, day)
print(birth_date)
from datetime import timedelta
hundred_days = timedelta(days=100)
future_date = birth_date + hundred_days
print(future_date)
thirty_days = timedelta(days=-30)
past_date = birth_date - thirty_days
print(past_date)
today = date.today()
date = date(year, month, day)v
age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
if age < 18:
    print("You are too young")
else:
    print("You are 18 or older")
    




