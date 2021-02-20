
voucher = int(input())
ticket = 0
other = 0
price = 0

purchase = input()
while purchase != "End":
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
    elif len(purchase) <= 8:
        price = ord(purchase[0])

    if voucher - price >= 0:
        voucher -= price
        if len(purchase) > 8:
            ticket += 1
        elif len(purchase) <= 8:
            other += 1
    else:
        break
    purchase = input()
print(f"{ticket}")
print(f"{other}")
