number_of_guests = int(input())
cuvert_price_per_person = float(input())
budget = float(input())

price_per_person = 0

if number_of_guests >= 10 and number_of_guests <= 15:
    price_per_person = cuvert_price_per_person - (price_per_person * 0.15)
elif number_of_guests > 15 and number_of_guests <= 20:
    price_per_person = cuvert_price_per_person - (price_per_person * 0.20)

print(f"{price_per_person}")
