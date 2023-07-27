# This program takes height and weight as an input. 
# It calculates the body mass index then and prints the result.

height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

result = weight / (height * height)
result = int(result)

if result < 18:
    print(f'You BMI is {result}. You are underweight')
elif result < 25:
    print(f'You BMI is {result}. It is a sign of normal weight')
elif result <30:
    print(f'You BMI is {result}. You are slightly overweight')
elif result < 35:
    print(f'You BMI is {result}. It is obese')
elif result > 35:
    print(f'You BMI is {result}. It is critical obese')
