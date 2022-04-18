# Instructions
# You are going to write a program which will select a random name from
# a list of names. The person selected will have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and puts
# them inside a List called names. For this to work, you must enter
# all the names as name followed by comma then space. e.g. name, name, name
#
# Example I
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
random_choice = random.randint(0, len(names) - 1)

person_will_pay = names[random_choice]

print(f"{person_will_pay} is going to buy the meal today!")
