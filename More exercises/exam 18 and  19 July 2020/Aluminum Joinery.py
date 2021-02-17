joinery_qty = int(input())
type_of_joinery = input()
delivery = input()

price = 0

if type_of_joinery == "90X130":
    price = 110 * joinery_qty
    if joinery_qty >= 60:
        price *= 0.92
    elif joinery_qty >= 30:
        price *= 0.95
elif type_of_joinery == "100X150":
    price = 140 * joinery_qty
    if joinery_qty >= 80:
        price *= 0.90
    elif joinery_qty >= 40:
        price *= 0.94
elif type_of_joinery == "130X180":
    price = 190 * joinery_qty
    if joinery_qty >= 50:
        price *= 0.88
    elif joinery_qty >= 20:
        price *= 0.93
elif type_of_joinery == "200X300":
    price = 250 * joinery_qty
    if joinery_qty >= 50:
        price *= 0.86
    elif joinery_qty >= 25:
        price *= 0.91

if delivery == "With delivery":
    price += 60
if joinery_qty > 99:
    price *= 0.96

if joinery_qty <= 10:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")

