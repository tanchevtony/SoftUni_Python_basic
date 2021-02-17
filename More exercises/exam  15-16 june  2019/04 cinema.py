capacity = int(input())

cinema_income = 0
current_seats = 0

people_in = input()
while people_in != "Movie time!":
    people_in = int(people_in)
    current_seats += people_in
    if capacity < current_seats:
        print("The cinema is full.")
        break

    if people_in % 3 == 0:
        cinema_income += people_in * 5 - 5
    else:
        cinema_income += people_in * 5

    people_in = input()

if people_in == "Movie time!":
    seats_left = capacity - current_seats
    print(f"There are {seats_left} seats left in the cinema.")
print(f"Cinema income - {cinema_income} lv.")