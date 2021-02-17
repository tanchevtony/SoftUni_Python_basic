price_baggage_over_20 = float(input())
kg_baggage = float(input())
days = int(input())
baggage_qty = int(input())

price = 0

if kg_baggage < 10:
    price = price_baggage_over_20 * 0.20
elif 10 <= kg_baggage <= 20:
    price = price_baggage_over_20 * 0.50
elif kg_baggage > 20:
    price = price_baggage_over_20

if days < 7:
    price *= 1.40
elif 7 <= days <= 30:
    price *= 1.15
else:
    price *= 1.10

total_price = price * baggage_qty

print(f"The total price of bags is: {total_price:.2f} lv.")
