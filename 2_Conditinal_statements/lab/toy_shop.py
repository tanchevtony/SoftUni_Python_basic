"""
Магазин за детски играчки

Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да 
изпълни. С парите, които ще спечели, иска да отиде на екскурзия. Да се напише 
програма, която пресмята печалбата от поръчката.
Цени на играчките:
•	Пъзел - 2.60 лв.
•	Говореща кукла - 3 лв.
•	Плюшено мече - 4.10 лв.
•	Миньон - 8.20 лв.
•	Камионче - 2 лв.
Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от
 общата цена. От спечелените пари Петя трябва да даде 10% за наема на магазина. 
 Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

Вход
От конзолата се четат 6 реда:
1.	Цена на екскурзията - реално число;
2.	Брой пъзели - цяло число;
3.	Брой говорещи кукли - цяло число;
4.	Брой плюшени мечета - цяло число;
5.	Брой миньони - цяло число;
6.	Брой камиончета - цяло число.

Изход
На конзолата се отпечатва:
•	Ако парите са достатъчни се отпечатва:
o	"Yes! {оставащите пари} lv left."
•	Ако парите НЕ са достатъчни се отпечатва:
o	"Not enough money! {недостигащите пари} lv needed."
Резултатът трябва да се форматира до втория знак след десетичната запетая.

"""

trip_price = float(input())
puzzle_qty = int(input())
dolls_qty = int(input())
bears_qty = int(input())
minion_qty = int(input())
lorry_qty = int(input())

sum_toys = (puzzle_qty * 2.60) + (dolls_qty * 3) + (bears_qty * 4.10) + (minion_qty * 8.20) + (lorry_qty * 2)
count_toys = puzzle_qty + dolls_qty + bears_qty + minion_qty + lorry_qty
discount = 0

if count_toys >= 50:
    discount = sum_toys * 0.25
total = sum_toys - discount
rent = total * 0.10
profit = total - rent

if profit >= trip_price:
    left_money = profit - trip_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    left_money = abs(profit - trip_price)
    print(f"Not enough money! {left_money:.2f} lv needed.")