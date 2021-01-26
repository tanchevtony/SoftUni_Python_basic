season = input()
kilometers_per_month = float(input())

salary = 0

if season == "Spring" or season == "Autumn" and kilometers_per_month <= 5000:
    salary = kilometers_per_month * 0.75 * 4
elif season == "Spring" or season == "Autumn" and 5000 < kilometers_per_month <= 10000:
    salary = kilometers_per_month * 0.95 * 4
elif 10000 < kilometers_per_month <= 20000:
    salary = kilometers_per_month * 1.45 * 4
total_sum = salary * 0.90

print(f"{total_sum:.2f}")
