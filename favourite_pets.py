# Was created on 1.07.2021
# From a book called Изучаем Python, Эрик Матиз. 
# It creates a dictionary with info about people and their pets.
# Then it prints out stored info.

pets = {
    'cat': {
        'name': 'oksana',
        'f_toy': 'mouse',
        'f_food': 'tuna',
        },
    'dog': {
        'name': 'viktor',
        'f_toy': 'stick',
        'f_food': 'meat',
        },
    }

for pet_name, pet_info in pets.items():
    print(f"I have a {pet_name.upper()}")
    name = pet_info['name']
    priorities = f"{pet_info['f_toy']} and {pet_info['f_food']}"
    print(f"{pet_name.title()} is named as {name.title()}. ",
    f"{name.title()} will choose {priorities} over me anytime.")
