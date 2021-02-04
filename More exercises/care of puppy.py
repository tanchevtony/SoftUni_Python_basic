food_qty = int(input())
food_qty *= 1000
leftover = 0
command = input()
while command != "Adopted":

    leftover += float(command)
    command = input()

total_ate = abs(leftover - food_qty)
if food_qty >= leftover:
    print(f"Food is enough! Leftovers: {total_ate:.0f} grams.")
else:
    print(f"Food is not enough. You need {total_ate:.0f} grams more.")

