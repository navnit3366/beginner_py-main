# This takes a year as input and checks if it is a leap year or not.

year = int(input("Which year do you want to check? "))

if year % 4 > 0:
    print(f'{year} is not a leap year.')
elif year % 4 == 0 and year % 100 > 0: 
    print(f'{year} is a leap year!')
elif year % 4 == 0 and year % 100 == 0:
    if year % 400 > 0:
        print(f'{year} is not a leap year!')
    else:
        print(f'{year} is leap year.')
