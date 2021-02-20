import math
number_of_people = int(input())
enter_tax = float(input())
lounge = float(input())
umbrella = float(input())

total = number_of_people * enter_tax
lounge_count = math.ceil(number_of_people * 0.75) * lounge
umbrella_count = math.ceil(number_of_people * 0.50) * umbrella
total_sum = total + lounge_count + umbrella_count

print(f"{total_sum:.2f} lv.")