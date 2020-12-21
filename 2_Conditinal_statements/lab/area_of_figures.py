""" 
6.	Лица на фигури
Да се напише програма, в която потребителят въвежда вида и размерите
 на геометрична фигура и пресмята лицето й. Фигурите са четири вида: 
 квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник 
 (triangle). На първия ред на входа се чете вида на фигурата (square, rectangle, circle или triangle):
•	Ако фигурата е квадрат, на следващия ред се чете едно число - дължина на страната му;
•	Ако фигурата е правоъгълник, на следващите два реда четат две числа - дължините на страните му;
•	Ако фигурата е кръг, на следващия ред чете едно число - радиусът на кръга;
•	Ако фигурата е триъгълник, на следващите два реда четат две числа - 
дължината на страната му и дължината на височината към нея. 
Резултатът да се закръгли до 3 цифри след десетичната точка. 

"""
import math

figure = input()

if figure == "rectangle":
    num_one = float(input())
    num_two = float(input())
    print(f"{num_one * num_two:.3f}")
elif figure == "circle":
    num = float(input())
    print(f"{math.pi * num * num:.3f}")
elif figure == "triangle":
    num_one = float(input())
    num_two = float(input())
    print(f"{(num_one * num_two) / 2:.3f}")
elif figure == "square":
    num = float(input())
    print(f"{num * num:.3f}")
    