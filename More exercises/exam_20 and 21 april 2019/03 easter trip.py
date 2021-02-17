destination = input()
from_to = input()
days = int(input())

price = 0

if destination == "France":
    if from_to == "21-23":
        price = 30
    elif from_to == "24-27":
        price = 35
    elif from_to == "28-31":
        price = 40
elif destination == "Italy":
    if from_to == "21-23":
        price = 28
    elif from_to == "24-27":
        price = 32
    elif from_to == "28-31":
        price = 39
elif destination == "Germany":
    if from_to == "21-23":
        price = 32
    elif from_to == "24-27":
        price = 37
    elif from_to == "28-31":
        price = 43

print(f"Easter trip to {destination} : {price * days:.2f} leva.")