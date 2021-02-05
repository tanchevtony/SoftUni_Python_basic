budget = float(input())  # float
petrol_needed = float(input())  # float
day_of_the_week = input()  # float

petrol_price = 2.10  # fixed
gid_price = 100  # fixed

sum_petrol = petrol_needed * petrol_price
total = sum_petrol + gid_price
end_price = 0

if day_of_the_week == "Saturday":  # Saturday = 10% discount from end price
    end_price = total - (total * (10 / 100))
elif day_of_the_week == "Sunday":  # Sunday = 20% discount from end price
    end_price = total - (total * (20 / 100))
if budget >= end_price:
    money_left = budget - end_price
    print(f"Safari time! Money left: {money_left:.2f} lv.")
else:
    money_needed = abs(budget - end_price)
    print(f"Not enough money! Money needed: {money_needed:.2f} lv.")