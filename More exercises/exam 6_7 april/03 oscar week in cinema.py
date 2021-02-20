movie_name = input()
type_of_hall = input()
tickets_numbers = int(input())
price = 0
if movie_name == "A Star Is Born":
    if type_of_hall == "normal":
        price = 7.50 * tickets_numbers
    elif type_of_hall == "luxury":
        price = 10.50 * tickets_numbers
    elif type_of_hall == "ultra luxury":
        price = 13.50 * tickets_numbers
elif movie_name == "Bohemian Rhapsody":
    if type_of_hall == "normal":
        price = 7.35 * tickets_numbers
    elif type_of_hall == "luxury":
        price = 9.45 * tickets_numbers
    elif type_of_hall == "ultra luxury":
        price = 12.75 * tickets_numbers
elif movie_name == "Green Book":
    if type_of_hall == "normal":
        price = 8.15 * tickets_numbers
    elif type_of_hall == "luxury":
        price = 10.25 * tickets_numbers
    elif type_of_hall == "ultra luxury":
        price = 13.25 * tickets_numbers
elif movie_name == "The Favourite":
    if type_of_hall == "normal":
        price = 8.75 * tickets_numbers
    elif type_of_hall == "luxury":
        price = 11.55 * tickets_numbers
    elif type_of_hall == "ultra luxury":
        price = 13.95 * tickets_numbers
print(f"{movie_name} -> {price:.2f} lv.")