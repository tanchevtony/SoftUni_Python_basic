number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegeterian = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50
total_menu = (number_fish_menu * fish_menu) + (number_chicken_menu * chicken_menu) + \
             (number_vegeterian * vegetarian_menu)
discount = total_menu * 0.20
total_sum = total_menu + discount + 2.50
print(f"Total: {total_sum:.2f}")