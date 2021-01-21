import math
x = int(input()) # area square meters
y = float(input())  # grapes per square meter
z = int(input())  # needed litres
workers_qty = int(input())


total_grapes = x * y
wine = 0.4 * total_grapes / 2.5
rest_wine = 0
wine_per_worker = 0

if wine >= z:
    rest_wine = wine - z
    wine_per_worker = rest_wine / workers_qty
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(rest_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
else:
    rest_wine = z - wine
    print(f"It will be a tough winter! More {math.floor(rest_wine)} liters wine needed.")