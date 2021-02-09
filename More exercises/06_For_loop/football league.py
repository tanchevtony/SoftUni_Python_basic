stadium_capacity = int(input())
fens_number = int(input())

a = 0
b = 0
v = 0
g = 0

for i in range(1, fens_number + 1):
    sector = input()

    if sector == "A":
        a +=1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1

percent_a = a / fens_number * 100
percent_b = b / fens_number * 100
percent_v = v / fens_number * 100
percent_g = g / fens_number * 100
percent_average = fens_number / stadium_capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_average:.2f}%")