budget = float(input())

products = 0
total_price = 0

while True:
    product = input()
    if product == "Stop":
        print(f"You bought {products} products for {total_price:.2f} leva.")
        break
    product_price = float(input())
    products += 1
    if products % 3 == 0:
        product_price /= 2
    if product_price > budget:
        print("You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        break
    budget -= product_price
    total_price += product_price
