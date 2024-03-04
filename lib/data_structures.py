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

def get_names(spicy_foods):
    names =[food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food["heat_level"]>5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name= food["name"]
        cuisine =food["cuisine"]
        heat_level="🌶" * food["heat_level"]

        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat_level / len(spicy_foods)
    return round(average)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
