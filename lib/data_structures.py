# def get_names(spicy_foods):
#     names = []
#     for food in spicy_foods:
#         names.append(food["name"])
#         return names
#     pass
def get_names(spicy_foods):
    
    return [food['name'] for food in spicy_foods]
    pass

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]




def get_spiciest_foods(spicy_foods):
    # return [food['name'] for food in spicy_foods if ['heat_level'] > 5 ]
    spiciest_foods = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest_foods.append(food.copy())
    return spiciest_foods
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
      heat_level = "🌶" * food["heat_level"]  # Create string with heat level emojis
      print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
      if food["cuisine"] == cuisine:
       return food.copy()  
    return None
    pass

def print_spiciest_foods(spicy_foods):
    hot_foods = get_spiciest_foods(spicy_foods)  
    for food in hot_foods:
      heat_level = "🌶" * food["heat_level"]  
      print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    pass

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
      total_heat += food["heat_level"]
    average_heat = total_heat // len(spicy_foods) 
    return average_heat
    pass

def create_spicy_food(spicy_foods, spicy_food):
      new_spicy_foods = spicy_foods.copy()  
      new_spicy_foods.append(spicy_food.copy())  
      return new_spicy_foods
    
