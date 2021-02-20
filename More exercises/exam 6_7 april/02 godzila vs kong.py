budget = float(input())
walking_gentleman = int(input())
price_per_walking_gentleman = float(input())


decor = budget * 0.10
cloths_walking_gentleman = walking_gentleman * price_per_walking_gentleman
if walking_gentleman > 150:
    cloths_walking_gentleman *= 0.90

total = decor + cloths_walking_gentleman
money_diff = abs(budget - total)

if budget >= total:
    print("Action!")
    print(f"Wingard starts filming with {money_diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {money_diff:.2f} leva more.")
