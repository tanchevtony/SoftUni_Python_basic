money_available = float(input())
command = input()
purchase_count = 0
while command != "mall.Enter":
    command = input()
command = input()
while command != 'mall.Exit':

    for symbol in command:
        if 'A' <= symbol <= 'Z':
            price = ord(symbol) * 0.5
            if money_available <= price:
                continue
            money_available -= price
            purchase_count += 1
        elif 'a' <= symbol <= 'z':
            price = ord(symbol) * 0.3
            if money_available <= price:
                continue
            money_available -= price
            purchase_count += 1
        elif symbol == '%':
            if money_available >= 0:
                money_available *= 0.5
                purchase_count += 1
        elif symbol == '*':
            money_available += 10
        else:
            if money_available >= ord(symbol):
                money_available -= ord(symbol)
                purchase_count += 1
    command = input()
if purchase_count == 0:
    print(f'No purchases. Money left: {money_available:.2f} lv.')
else:
    print(f'{purchase_count} purchases. Money left: {money_available:.2f} lv.')
