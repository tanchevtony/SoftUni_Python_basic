square_meters = float(input())

area = square_meters * 7.61
discount = 0.18 * area
final_price = area - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")