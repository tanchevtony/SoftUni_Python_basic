movie_name = input()  # John Wick, Star Wars or Jumanji
movie_pack = input()  # Drink, Popcorn or Menu
number_of_tickets = int(input())

price = 0

if movie_name == "John Wick":
    if movie_pack == "Drink":
        price = 12 * number_of_tickets
    elif movie_pack == "Popcorn":
        price = 15 * number_of_tickets
    elif movie_pack == "Menu":
        price = 19 * number_of_tickets
elif movie_name == "Star Wars":
    if movie_pack == "Drink":
        price = 18 * number_of_tickets
    elif movie_pack == "Popcorn":
        price = 25 * number_of_tickets
    elif movie_pack == "Menu":
        price = 30 * number_of_tickets
    if number_of_tickets >= 4:
        price *= 0.70
elif movie_name == "Jumanji":
    if movie_pack == "Drink":
        price = 9 * number_of_tickets
    elif movie_pack == "Popcorn":
        price = 11 * number_of_tickets
    elif movie_pack == "Menu":
        price = 14 * number_of_tickets
    if number_of_tickets == 2:
        price *= 0.85
print(f"Your bill is {price:.2f} leva.")