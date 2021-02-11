number_of_clients = int(input())

total = 0
for i in range(number_of_clients):
    product = input()
    current_sells = 0
    current_sum = 0
    while product != "Finish":
        current_sells += 1
        if product == "basket":
            current_sum += 1.50
        elif product == "wreath":
            current_sum += 3.80
        elif product == "chocolate bunny":
            current_sum += 7
        product = input()
    if current_sells % 2 == 0:
        current_sum *= 0.80

    print(f"You purchased {current_sells} items for {current_sum:.2f} leva.")
    total += current_sum
average = total / number_of_clients
print(f"Average bill per client is: {average:.2f} leva.")

