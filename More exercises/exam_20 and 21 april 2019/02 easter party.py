number_of_guests = int(input())
cuvert_price_per_person = float(input())
budget = float(input())

price_per_person = 0

if 10 <= number_of_guests <= 15:
    price_per_person = cuvert_price_per_person * 0.85
elif 15 < number_of_guests <= 20:
    price_per_person = cuvert_price_per_person * 0.80
elif number_of_guests > 20:
    price_per_person = cuvert_price_per_person * 0.75
else:
    price_per_person = cuvert_price_per_person

cake = budget * 0.10
total_sum = number_of_guests * price_per_person + cake
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")