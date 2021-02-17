country = input()
gym_equipment = input()

difficulty = 0
performance = 0

if country == "Russia":
    if gym_equipment == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif gym_equipment == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif gym_equipment == "rope":
        difficulty = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if gym_equipment == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif gym_equipment == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif gym_equipment == "rope":
        difficulty = 9.500
        performance = 9.400
elif country == "Italy":
    if gym_equipment == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif gym_equipment == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif gym_equipment == "rope":
        difficulty = 9.700
        performance = 9.150
total = difficulty + performance
difference = 20 - total
percent = difference / 20 * 100

print(f"The team of {country} get {total:.3f} on {gym_equipment}.")
print(f"{percent:.2f}%")
