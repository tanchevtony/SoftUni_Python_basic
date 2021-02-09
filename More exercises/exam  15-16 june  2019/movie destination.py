movie_budget = float(input())
destination = input()  # Dubai, Sofia or London
season = input()  # Summer or Winter
number_of_days = int(input())

price = 0

if destination == "Dubai":
    if season == "Winter":
        price = 45000 * number_of_days
    elif season == "Summer":
        price = 40000 * number_of_days
elif destination == "Sofia":
    if season == "Winter":
        price = 17000 * number_of_days
    elif season == "Summer":
        price = 12500 * number_of_days
elif destination == "London":
    if season == "Winter":
        price = 24000 * number_of_days
    elif season == "Summer":
        price = 20250 * number_of_days

if destination == "Dubai":
    price *= 0.70
elif destination == "Sofia":
    price *= 1.25
diff = abs(movie_budget - price)

if movie_budget >= price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")