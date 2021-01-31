"""
Годзила срещу Конг

Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
дали предвидените средства са достатъчни за снимането на филма. 
За снимките  ще бъдат нужни определен брой статисти, 
облекло за всеки един статист и декор.
Известно е, че:
•	Декорът за филма е на стойност 10% от бюджета. 
•	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

Вход
От конзолата се четат 3 реда:
Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

Изход
На конзолата трябва да се отпечатат два реда:
•	Ако  парите за декора и дрехите са повече от бюджета:
o	"Not enough money!"
o	"Wingard needs {парите недостигащи за филма} leva more."
•	Ако парите за декора и дрехите са по малко или равни на бюджета:
o	"Action!" 
o	"Wingard starts filming with {останалите пари} leva left."
Резултатът трябва да е форматиран до втория знак след десетичната запетая.

"""

# movie budget
budget = float(input())
# number of walking gentleman
people = int(input())
# cloth price per 1 walking gentleman
cloth_per_person = float(input())
# decor = 10% from budget / cloth_price / discount
decor = budget * 0.10
cloth_price = cloth_per_person * people
# discount = cloth_price * 0.10

if people > 150:
    cloth_price *= 0.90
    # cloth_money = cloth_price - discount
total_money = decor + cloth_price

if budget >= total_money:
    print(f"Action!\nWingard starts filming with {abs(budget - total_money):.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {abs(total_money - budget):.2f} leva more.")
