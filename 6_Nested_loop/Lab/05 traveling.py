destination = input()
while destination != "End":
    budget = float(input())
    money = 0

    while money < budget:
        current_money = float(input())
        money += current_money
    print(f"Going to {destination}!")
    destination = input()



