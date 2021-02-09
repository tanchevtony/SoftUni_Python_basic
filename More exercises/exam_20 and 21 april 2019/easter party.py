number_of_guests = int(input())
cuvert_price_per_person = float(input())
budget = float(input())

price_per_person = 0

if not 10 > number_of_guests and number_of_guests <= 15:
    price_per_person = cuvert_price_per_person - (price_per_person * 0.15)
elif 15 < number_of_guests and not number_of_guests > 20:
    price_per_person = cuvert_price_per_person - (price_per_person * 0.20)

print(f"{price_per_person}")
