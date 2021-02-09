budget = float(input())
series = int(input())


total = 0

for i in range(1, series + 1):
    series_name = input()
    price = float(input())

    if series_name == "Thrones":
        total += price * 0.50
    elif series_name == "Lucifer":
        total += price * 0.60
    elif series_name == "Protector":
        total += price * 0.70
    elif series_name == "TotalDrama":
        total += price * 0.80
    elif series_name == "Area":
        total += price * 0.90
    else:
        total += price
diff = abs(budget - total)
if budget >= total:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")