sum = float(input())
sum = int(sum * 100)
coins_counter = 0

coins_counter += sum // 200
sum %= 200
coins_counter += sum // 100
sum %= 100
coins_counter += sum // 50
sum %= 50
coins_counter += sum // 20
sum %= 20
coins_counter += sum // 10
sum %= 10
coins_counter += sum // 5
sum %= 5
coins_counter += sum // 2
sum %= 2
if sum == 1:
    coins_counter += 1
print(coins_counter)


# със while цъкъл

change = float(input())
change = int(change * 100)
coins = 0

while change != 0:
    if change >= 200:
        change -= 200
        coins += 1
        continue
    elif change >= 100:
        change -= 100
        coins += 1
        continue
    elif change >= 50:
        change -= 50
        coins += 1
        continue
    elif change >= 20:
        change -= 20
        coins += 1
        continue
    elif change >= 10:
        change -= 10
        coins += 1
        continue
    elif change >= 5:
        change -= 5
        coins += 1
        continue
    elif change >= 2:
        change -= 2
        coins += 1
        continue
    elif change >= 1:
        change -= 1
        coins += 1
        if change % 2 < 0.01:
            break
        continue

print(f'{coins}')