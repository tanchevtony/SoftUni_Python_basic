term_of_the_contract = input()
type_of_the_contract = input()
mobile_internet = input()
number_of_months = int(input())

price_term = 0

if term_of_the_contract == "one":
    if type_of_the_contract == "Small":
        price_term = 9.98
    elif term_of_the_contract == "Middle":
        price_term = 18.99
    elif term_of_the_contract == "Large":
        price_term = 25.98
    elif term_of_the_contract == "ExtraLarge":
        price_term = 35.99
elif term_of_the_contract == "two":
    if type_of_the_contract == "Small":
        price_term = 8.58
    elif type_of_the_contract == "Middle":
        price_term = 17.09
    elif type_of_the_contract == "Large":
        price_term = 23.59
    elif type_of_the_contract == "ExtraLarge":
        price_term = 31.79

if mobile_internet == "yes":
    if price_term <= 10:
        price_term += 5.50
    elif price_term <= 30:
        price_term += 4.35
    elif price_term > 30:
        price_term += 3.85

if term_of_the_contract == 'two':
    price_term = price_term - price_term * 3.75 / 100

final_price = price_term * number_of_months
print(f"{final_price:.2f} lv.")