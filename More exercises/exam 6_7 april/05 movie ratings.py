
movie_numbers = int(input())
max_rating = 0
max_movie_name = ""
min_rating = 0
min_movie_name = ""
total_rating = 0
for i in range(movie_numbers):
    current_movie_name = input()
    current_movie_rating = float(input())
    total_rating += current_movie_rating
    if current_movie_rating > max_rating:
        max_movie_name = current_movie_name
        max_rating = current_movie_rating
    elif min_rating == 0 or current_movie_rating < min_rating:
        min_movie_name = current_movie_name
        min_rating = current_movie_rating
average_rating = total_rating / movie_numbers
print(f"{max_movie_name} is with highest rating: {max_rating:.1f}")
print(f"{min_movie_name} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

