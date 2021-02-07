year_tax = int(input())

sneakers = year_tax * 0.60
tracksuit = sneakers * 0.80
basketball = tracksuit * 1/4
accessories = basketball * 1/5

total = year_tax + sneakers + tracksuit + basketball + accessories
print(f"{total:.2f}")