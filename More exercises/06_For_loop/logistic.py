load_numbers = int(input())

price_van = 200
price_truck = 175
price_train = 120

count = 0

van = 0
truck = 0
train = 0

for i in range(1, load_numbers + 1):
    load_tons = int(input())
    count += load_tons

    if load_tons <= 3:
        van += load_tons
    elif 4 <= load_tons <= 11:
        truck += load_tons
    else:
        train += load_tons

average_price = (van * price_van + truck * price_truck + train * price_train) / count
van_percent = van / count * 100
truck_percent = truck / count * 100
train_percent = train / count * 100

print(f"{average_price:.2f}")
print(f"{van_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")