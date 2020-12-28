"""
Операции между числа

Напишете програма, която чете две цели числа (N1 и N2) и оператор, 
с който да се извърши дадена математическа операция. Възможните 
операции са: Събиране(+), Изваждане(-), Умножение(*),  Деление(/) 
и Модулно деление(%). При събиране, изваждане и умножение на конзолата
трябва да се отпечатат резултата и дали той е четен или нечетен. 
При обикновеното деление – резултата. При модулното деление – остатъка.
Трябва да се има предвид, че делителят може да е равен на 0 (нула),
а на нула не се дели. В този случай трябва да се отпечата специално съобщениe.

Вход
От конзолата се прочитат 3 реда, въведени от потребителя:
•	N1 – цяло число;
•	N2 – цяло число;
•	Оператор – един символ измежду: "+", "-", "*", "/", "%".

Изход
Да се отпечата на конзолата един ред:
•	Ако операцията е събиране, изваждане или умножение:
o	 "{N1} {оператор} {N2} = {резултат} – {even/odd}"
•	Ако операцията е деление:
o	"{N1} / {N2} = {резултат}" – резултат, форматиран до втория знак след
десетичната запетая
•	Ако операцията е модулно деление: 
o	"{N1} % {N2} = {остатък}"
•	В случай на деление с 0 (нула): 
o	"Cannot divide {N1} by zero"

"""
num_one = int(input())
num_two = int(input())
operator = input()

total = 0

if operator == "+":
    total = num_two + num_one
    if total % 2 == 0:
        print(f"{num_one} + {num_two} = {total} - even")
    else:
        print(f"{num_one} + {num_two} = {total} - odd")
elif operator == "-":
    total = num_one - num_two
    if total % 2 == 0:
        print(f"{num_one} - {num_two} = {total} - even")
    else:
        print(f"{num_one} - {num_two} = {total} - odd")
elif operator  == "*":
    total = num_one * num_two
    if total % 2 == 0:
        print(f"{num_one} * {num_two} = {total} - even")
    else:
        print(f"{num_one} * {num_two} = {total} - odd")
elif operator == "/":
    if num_two != 0:
        print(f"{num_one} / {num_two} = {(num_one / num_two):.2f}")
    else:
        print(f"Cannot divide {num_one} by zero")
elif operator == "%":
    if (num_two != 0):
        print(f"{num_one} % {num_two} = {num_one % num_two}")
    else:
        print(f"Cannot divide {num_one} by zero")
    
