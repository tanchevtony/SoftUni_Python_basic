needed_money = float(input())
club_income = 0
cocktail_name = input()
while cocktail_name != "Party!":
    number_of_cocktails = int(input())
    current_order = number_of_cocktails * len(cocktail_name)

    if not current_order % 2 == 0:
        current_order *= 0.75

    club_income += current_order
    if club_income >= needed_money:
        break
    cocktail_name = input()
difference = abs(needed_money - club_income)
if club_income >= needed_money:
    print("Target acquired.")
else:
    print(f"We need {difference:.2f} leva more.")
print(f"Club income - {club_income:.2f} leva.")
