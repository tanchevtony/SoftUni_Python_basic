kilometers = int(input())
part_of_the_day = input()

price = 0
if kilometers < 20:
    type_of_transport = "taxi"
    if part_of_the_day == "day":
        price = 0.7 + kilometers * 0.79
    elif part_of_the_day == "night":
        price = 0.7 + kilometers * 0.9
elif 20 <= kilometers < 100:
    price = 0.09 * kilometers
else:
    price = 0.06 * kilometers
print(f"{price:.2f}")
