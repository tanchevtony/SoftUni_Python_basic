team = input()  # "Argentina", "Brazil", "Croatia", "Denmark"
souvenir = input()  # "flags", "caps", "posters", "stickers"
sold_souvenirs = int(input())

price = 0

if team == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price = 5.10
    elif souvenir == "stickers":
        price = 1.25
elif team == "Brazil":
    if souvenir == "flags":
        price = 4.20
    elif souvenir == "caps":
        price = 8.50
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.20
elif team == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.90
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.10
elif team == "Denmark":
    if souvenir == "flags":
        price = 3.10
    elif souvenir == "caps":
        price = 6.50
    elif souvenir == "posters":
        price = 4.80
    elif souvenir == "stickers":
        price = 0.90
total_sum = price * sold_souvenirs
if not team == "Argentina" and not team == "Brazil" and not team == "Croatia" and not team == "Denmark":
    print("Invalid country!")
elif not souvenir == "flags" and not souvenir == "caps" and not souvenir == "posters" and not souvenir == "stickers":
    print("Invalid stock!")
else:
    print(f"Pepi bought {sold_souvenirs} {souvenir} of {team} for {total_sum:.2f} lv.")
