"""
Баланс по сметка

Напишете програма, която пресмята колко общо пари
има в сметката, след като направите определен брой
вноски. На всеки ред ще получавате сумата, която
трябва да внесете в сметката до получаване на команда
“NoMoreMoney”. При всяка получена сума на конзолата
трябва да се извежда "Increase: " + сумата (форматирана
до втория знак след десетичната запетая) и тя да се прибавя
в сметката. Ако получите число по-малко от 0 на конзолата
трябва да се изведе "Invalid operation!" и програмата да
приключи. Когато програмата приключи трябва да се принтира
"Total: " + общата сума в сметката закръглена до втория
знак след десетичната запетая.
"""
command = input()

total_sum = 0

while command != "NoMoreMoney":
    money = float(command)
    if money <= 0:
        print("Invalid operation!")
        break
    else:
        total_sum += money
        print(f"Increase: {money:.2f}")
    command = input()
print(f"Total: {total_sum:.2f}")