import math
price_one_tennis_racquet = float(input())
tennis_racquet_qty = int(input())
sneakers_pairs = int(input())

racquet_price = tennis_racquet_qty * price_one_tennis_racquet
sneakers_one_pair = price_one_tennis_racquet / 6
sneakers_pairs_price = sneakers_one_pair * sneakers_pairs
price_equipment = (racquet_price + sneakers_pairs_price) * 0.2
total = racquet_price + sneakers_pairs_price + price_equipment
price_djokovic = math.floor(total / 8)
sponsor = math.ceil(total * 7 / 8)

print(f"Price to be paid by Djokovic {price_djokovic}")
print(f"Price to be paid by sponsors {sponsor}")
