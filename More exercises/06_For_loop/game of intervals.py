turn = int(input())

result = 0
zero_to_9 = 0
ten_to_19 = 0
twenty_to_29 = 0
thirty_to_39 = 0
forty_to_50 = 0
invalid_numbers = 0

for i in range(1, turn + 1):
    number = int(input())
    if 0 <= number <= 9:
        result += number * 0.20
        zero_to_9 += 1
    elif 10 <= number <= 19:
        result += number * 0.30
        ten_to_19 += 1
    elif 20 <= number <= 29:
        result += number * 0.40
        twenty_to_29 += 1
    elif 30 <= number <= 39:
        result += 50
        thirty_to_39 += 1
    elif 40 <= number <= 50:
        result += 100
        forty_to_50 += 1
    else:
        result /= 2
        invalid_numbers += 1

zero_to_9_percent = zero_to_9 / turn * 100
ten_to_19_percent = ten_to_19 / turn * 100
twenty_to_29_percent = twenty_to_29 / turn * 100
thirty_to_39_percent = thirty_to_39 / turn * 100
forty_to_50_percent = forty_to_50 / turn * 100
invalid_numbers_percent = invalid_numbers / turn * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {zero_to_9_percent:.2f}%")
print(f"From 10 to 19: {ten_to_19_percent:.2f}%")
print(f"From 20 to 29: {twenty_to_29_percent:.2f}%")
print(f"From 30 to 39: {thirty_to_39_percent:.2f}%")
print(f"From 40 to 50: {forty_to_50_percent:.2f}%")
print(f"Invalid numbers: {invalid_numbers_percent:.2f}%")