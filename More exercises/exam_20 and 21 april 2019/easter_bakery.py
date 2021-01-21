flour_price_per_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs_qty = int(input())
yeast_qty = int(input())

sugar_price = flour_price_per_kg * 0.75
eggs_price = flour_price_per_kg * 1.1
yeast_price = sugar_price * 0.2
sum_flour = flour_price_per_kg * kg_flour
sum_sugar = sugar_price * kg_sugar
sum_eggs = eggs_price * eggs_qty
sum_yeast = yeast_price * yeast_qty
total_sum = sum_eggs + sum_flour + sum_sugar + sum_yeast

print(f"{total_sum:.2f}")