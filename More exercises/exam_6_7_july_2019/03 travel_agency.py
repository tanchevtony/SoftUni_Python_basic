destination = input()
pack_type = input()
vip = input()
days = int(input())

price = 0
if days > 7:
    days -= 1

if days < 1:
    print("Days must be positive number!")
elif not (destination in ("Bansko", "Borovets") and pack_type in ("noEquipment", "withEquipment")) and not (
        destination in ("Varna", "Burgas") and pack_type in ("noBreakfast", "withBreakfast")):
    print("Invalid input!")
else:
    if destination == "Bansko" or destination == "Borovets":
        if pack_type == "noEquipment":
            price = 80 * days
            if vip == "yes":
                price *= 0.95
        elif pack_type == "withEquipment":
            price = 100 * days
            if vip == "yes":
                price *= 0.90
    elif destination == "Varna" or destination == "Burgas":
        if pack_type == "noBreakfast":
            price = 100 * days
            if vip == "yes":
                price *= 0.93
        elif pack_type == "withBreakfast":
            price = 130 * days
            if vip == "yes":
                price *= 0.88
    print(f"The price is {price:.2f}lv! Have a nice time!")
