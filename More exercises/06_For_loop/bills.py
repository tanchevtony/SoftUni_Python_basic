months_numbers = int(input())

electricity_count = 0
water_count = 0
internet_count = 0
other_count = 0

for i in range(1, months_numbers + 1):
    electricity = float(input())
    electricity_count += electricity
    water_count += 20
    internet_count += 15
    total_other_count = electricity_count + water_count + internet_count
    other_count = total_other_count * 1.20
average = (electricity_count + water_count + internet_count + other_count) / months_numbers

print(f"Electricity: {electricity_count:.2f} lv")
print(f"Water: {water_count:.2f} lv")
print(f"Internet: {internet_count:.2f} lv")
print(f"Other: {other_count:.2f} lv")
print(f"Average: {average:.2f} lv")
