juniors = int(input())
seniors = int(input())
type_terrain = input()  # trail, cross-country, downhill, road

total_participants = juniors + seniors
tax_juniors = 0
tax_seniors = 0

if type_terrain == "trail":
    tax_juniors = 5.50
    tax_seniors = 7
elif type_terrain == "cross-country":
    tax_juniors = 8
    tax_seniors = 9.50
    if total_participants >= 50:
        tax_juniors *= 0.75
        tax_seniors *= 0.75
elif type_terrain == "downhill":
    tax_juniors = 12.25
    tax_seniors = 13.75
elif type_terrain == "road":
    tax_juniors = 20
    tax_seniors = 21.50

total = juniors * tax_juniors + seniors * tax_seniors
costs = total - total * 0.95
total_sum = total - costs
print(f"{total_sum:.2f}")