movie_name = input()
total_tickets = 0
students_tickets = 0
standard_tickets = 0
kids_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())
    sold_tickets = 0

    ticket_type = input()
    while ticket_type != "End":
        sold_tickets += 1
        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "student":
            students_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        if sold_tickets == free_seats:
            break
        ticket_type = input()
    total_tickets += sold_tickets
    print(f"{movie_name} - {sold_tickets / free_seats * 100:.2f}% full.")
    movie_name = input()

percent_student = students_tickets / total_tickets * 100
percent_standard = standard_tickets / total_tickets * 100
percent_kids = kids_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")
