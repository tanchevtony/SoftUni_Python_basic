import sys
import math

number_of_bake = int(input())

sugar_qty = 0
flour_qty = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for i in range(1, number_of_bake + 1):
    sugar = int(input())
    flour = int(input())
    sugar_qty += sugar
    flour_qty += flour

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour
pak_of_sugar = math.ceil(sugar_qty / 950)
pack_of_flour = math.ceil(flour_qty / 750)

print(f"Sugar: {pak_of_sugar}")
print(f"Flour: {pack_of_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
