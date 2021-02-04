choose_type = input()  # Espresso, Cappuccino, Tea
sugar = input()  # without, Normal, Extra
number_of_drinks = int(input())

price = 0

if choose_type == "Espresso":
    if sugar == "Without":
        price = number_of_drinks * 0.90
        price *= 0.65
    elif sugar == "Normal":
        price = number_of_drinks * 1
    elif sugar == "Extra":
        price = number_of_drinks * 1.20

elif choose_type == "Cappuccino":
    if sugar == "Without":
        price = number_of_drinks * 1
        price *= 0.65
    elif sugar == "Normal":
        price = number_of_drinks * 1.20
    elif sugar == "Extra":
        price = number_of_drinks * 1.60

elif choose_type == "Tea":
    if sugar == "Without":
        price = number_of_drinks * 0.50
        price *= 0.65
    elif sugar == "Normal":
        price = number_of_drinks * 0.60
    elif sugar == "Extra":
        price = number_of_drinks * 0.70

if choose_type == "Espresso" and number_of_drinks >= 5:
    price *= 0.75
if price > 15:
    price *= 0.80
print(f"You bought {number_of_drinks} cups of {choose_type} for {price:.2f} lv.")


