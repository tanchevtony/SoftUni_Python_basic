inherited_money = float(input())
back_to = int(input())

years = 18

for i in range(1800, back_to + 1):
    if i % 2 != 0:
        inherited_money -= 12000 + (years * 50)
        years += 1
    else:
        inherited_money -= 12000
        years += 1
if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
