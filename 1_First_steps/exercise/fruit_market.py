"""
Пазар за плодове
Мария решава да мине на диета и отива до  близкия пазар, за да купи 
ягоди, банани, портокали и малини. Да се напише програма, която пресмята 
колко пари са  ѝ необходими за да плати сметката, като знаете, че:
•	цената на  малините е на половина по-ниска от тази на ягодите;
•	цената на портокалите е с 40% по-ниска от цената на малините;
•	цената на бананите е с 80% по-ниска от цената на малините.

Вход
От конзолата се четат 5 реда:
1.	Цена на ягодите в лева – реално число;
2.	Количество на бананите в килограми – реално число;
3.	Количество на портокалите в килограми – реално число;
4.	Количество на малините в килограми – реално число;
5.	Количество на ягодите в килограми – реално число.

Изход
Да се отпечата на конзолата едно число:
•	парите, които са необходими на Мария.

"""
strawberry_price = float(input())
qty_banana_kg = float(input())
qty_portocal_kg = float(input())
qty_raspberry_kg = float(input())
qty_strawberry_kg = float(input())

raspberry_price = strawberry_price / 2
portocal_price = raspberry_price - (raspberry_price * 0.40)
banana_price = raspberry_price - (raspberry_price * 0.80)

sum_raspberry = qty_raspberry_kg * raspberry_price
sum_portocal = qty_portocal_kg * portocal_price
sum_banana = qty_banana_kg * banana_price
sum_strawberry = strawberry_price * qty_strawberry_kg

total_sum = sum_raspberry + sum_portocal + sum_banana + sum_strawberry

print(total_sum)
