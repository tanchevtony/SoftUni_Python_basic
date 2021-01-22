import math
magnolia_qty = int(input())
hyacinth_qty = int(input())
roses_qty = int(input())
cactus_qty = int(input())
gift_price = float(input())

magnolia = 3.25
hyacinth = 4
roses = 3.50
cactus = 8

sum_flowers = magnolia_qty * magnolia + hyacinth_qty * hyacinth + roses_qty * roses + cactus_qty * cactus
total = sum_flowers * 0.95
diff = abs(total - gift_price)
if total >= gift_price:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")