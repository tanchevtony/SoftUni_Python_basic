number_of_groups = int(input())

total_people = 0
musala = 0
montblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for i in range(1, number_of_groups + 1):
    number_of_people = int(input())

    if number_of_people <= 5:
        musala += number_of_people
    elif 6 <= number_of_people <= 12:
        montblan += number_of_people
    elif 13 <= number_of_people <= 25:
        kilimandjaro += number_of_people
    elif 26 <= number_of_people <= 40:
        k2 += number_of_people
    elif number_of_people >= 41:
        everest += number_of_people

total_people = musala + montblan + kilimandjaro + k2 + everest
musala_percent = (musala / total_people) * 100
montblan_percent = montblan / total_people * 100
kilimandjaro_percent = kilimandjaro / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100
print(f"{musala_percent:.2f}%")
print(f"{montblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")