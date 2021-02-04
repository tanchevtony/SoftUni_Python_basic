one_lv_coin = int(input())
two_lv_coin = int(input())
five_lv_bill = int(input())
amount = int(input())

for a in range(0, one_lv_coin + 1):
    for b in range(0, two_lv_coin + 1):
        for c in range(0, five_lv_bill + 1):
            if a * 1 + b * 2 + c * 5 == amount:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {amount} lv.")