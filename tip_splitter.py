# This programm splits a bill between giben amount of people and
# tells you how much each should pay based on how many per cents
# you are willing to give as a tip.

bill = float(input('Tell me your bill: '))
desired_percentage = int(input('How many per cents would you want to tip? '))
people = int(input('How many people split the bill? '))

percentage = (bill / 100) * desired_percentage
tip = (bill + percentage) / people
formatted_tip = "{:.2f}".format(tip) # leaves two decimal places
print(formatted_tip)
