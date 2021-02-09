movie_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input())

ticket_price_per_day = number_of_tickets * ticket_price
total_time_income = number_of_days * ticket_price_per_day
cinema_percent_price = total_time_income * (cinema_percent / 100)

movie_profit = total_time_income - cinema_percent_price
print(f"The profit from the movie {movie_name} is {movie_profit:.2f} lv.")