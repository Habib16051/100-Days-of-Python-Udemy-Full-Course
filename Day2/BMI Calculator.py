# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#
# The BMI is a measure of some weight taking into account their height. e.g. If a tall person and a short person
# both weigh the same amount, the short person is usually more overweight.
#
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#
# https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv
#
# Warning you should convert the result to a whole number.

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

x = float(weight)
y = float(height)

z = (x / (y * y))
print("Your BMI is :", int(z))
