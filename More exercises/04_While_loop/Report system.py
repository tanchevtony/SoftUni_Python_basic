expected_money = int(input())

collected_money = 0
counter = 0  # counter for card or cash
card_count = 0
card_count_people = 0
cash_count = 0
cash_count_people = 0

command = input()

while command != "End":
    transaction = int(command)
    counter += 1

    if counter % 2 == 0:  # second payment card
        if transaction >= 10:
            collected_money += transaction
            card_count += transaction
            card_count_people += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:  # first payment cash
        if transaction <= 100:
            collected_money += transaction
            cash_count += transaction
            cash_count_people += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    if collected_money >= expected_money:
        break

    command = input()
if command == "End":
    print("Failed to collect required money for charity.")
else:
    average_card = card_count / card_count_people
    average_cash = cash_count / cash_count_people
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
