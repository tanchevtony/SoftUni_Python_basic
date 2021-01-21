
import math
number_of_days = int(input())
food_in_kg = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog_food = number_of_days * dog_food_per_day
cat_food = number_of_days * cat_food_per_day
turtle_food = (number_of_days * turtle_food_per_day) / 1000

sum_food = dog_food + cat_food + turtle_food

difference = abs(food_in_kg - sum_food)

if sum_food <= food_in_kg:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")