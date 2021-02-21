cat_numbers = int(input())
small_cats = 0
middle_cats = 0
big_cats = 0
total_food_eaten = 0
for i in range(cat_numbers):
    food_eaten = float(input())

    if 100 <= food_eaten < 200:
        small_cats += 1
        total_food_eaten += food_eaten
    elif 200 <= food_eaten < 300:
        middle_cats += 1
        total_food_eaten += food_eaten
    elif 300 <= food_eaten < 400:
        big_cats += 1
        total_food_eaten += food_eaten
price_per_food = (total_food_eaten / 1000) * 12.45

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {middle_cats} cats.")
print(f"Group 3: {big_cats} cats.")
print(f"Price for food per day: {price_per_food:.2f} lv.")


