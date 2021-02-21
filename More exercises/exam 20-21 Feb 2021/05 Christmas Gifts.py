person_age = input()

number_of_adults = 0
number_of_kids = 0

while person_age != "Christmas":
    person_age = int(person_age)

    if person_age <= 16:
        number_of_kids += 1
    else:
        number_of_adults += 1
    person_age = input()

money_for_toys = number_of_kids * 5
money_for_sweaters = number_of_adults * 15

print(f"Number of adults: {number_of_adults}")
print(f"Number of kids: {number_of_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
