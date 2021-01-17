price_for_kg_vegetable = float(input())
price_for_kg_fruits = float(input())
total_kg_for_vegetable = int(input())
total_kg_for_fruits = int(input())

sum_vegetable = price_for_kg_vegetable * total_kg_for_vegetable
sum_fruits = price_for_kg_fruits * total_kg_for_fruits
total_sum_euro = (sum_vegetable + sum_fruits) / 1.94
print(f"{total_sum_euro:.2f}")
