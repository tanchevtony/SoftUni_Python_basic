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

# another version has not been tested

money_for_vacation = float(input())
money = float(input())

days = 0
spend_days = 0

while money < money_for_vacation:

    spend_or_save = input()
    money_spend_saved = float(input())
    days += 1

    if spend_or_save == "spend":
        spend_days += 1
        money -= money_spend_saved
        if money < 0:
            money = 0

    elif spend_or_save == "save":
        money += money_spend_saved
        spend_days = 0

    if spend_days == 5:
        print(f"You can\'t save the money.")
        print(f"{days}")
        break

    elif money >= money_for_vacation and spend_days < 5:
        print(f"You saved the money for {days} days.")