needed_money - float(input())
cash = float(input())

needed_money = float(input())
money_in_hand = float(input())

spending_days_counter = 0
spending_too_many_days = False
total_days = 0
while money_in_hand < needed_money:
    action = input()
    sum = float(input())
    total_days += 1
    if action == "spend":
        money_in_hand -= sum
        if money_in_hand < 0:
            money_in_hand = 0
        spending_days_counter += 1
        if spending_days_counter == 5:
            spending_too_many_days = True
            break
    else:
        money_in_hand += sum
        spending_days_counter = 0
if spending_too_many_days:
    print("You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")