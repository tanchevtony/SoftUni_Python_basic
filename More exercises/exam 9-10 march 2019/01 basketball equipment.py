year_tax = int(input())
tennis_racquets = int(input())
sneaker_pairs = int(input())
sneakers = year_tax / 6

tracksuit = sneaker_pairs * 0.80
basketball = tracksuit * 1/4
accessories = basketball * 1/5

total = year_tax + sneakers + tracksuit + basketball + accessories
price_djokovic = total / 8
sponsor = total * 7/8

print(f"Price to be paid by Djokovic {price_djokovic}")
print(f"Price to be paid by sponsors {sponsor}")
