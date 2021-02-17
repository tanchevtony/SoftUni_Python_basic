budget = float(input())

total_sum = 0
wage = 0
action = False
actor_name = input()
while actor_name != "ACTION":

    actor_name_length = len(actor_name)
    if actor_name_length > 15:
        wage = budget * 0.20
    else:
        wage = float(input())
    budget -= wage
    if budget <= 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        action = True
        break

    actor_name = input()

if not action:
    print(f"We are left with {budget:.2f} leva.")
