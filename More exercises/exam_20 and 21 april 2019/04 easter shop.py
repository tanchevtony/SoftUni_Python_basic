current_eggs = int(input())

sold_eggs = 0

command = input()
while command != "Close":
    if command == "Fill":
        eggs_to_fill = int(input())
        current_eggs += eggs_to_fill
    if command == "Buy":
        eggs_to_buy = int(input())
        if eggs_to_buy <= current_eggs:
            current_eggs -= eggs_to_buy
            sold_eggs += eggs_to_buy
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {current_eggs}.")
            break
    command = input()
if command == "Close":
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")