age = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())

sum_toys = 0
sum_money = 0
years = 0
for i in range(1, age + 1):
    if i %2 == 0:
        sum_money += 10 + (sum_toys - 1) * 10
        years += 1
    else:
        sum_toys += 1

total_sum = (sum_money - years) + (sum_toys * single_toy_price)
sum = total_sum - washing_machine_price
if total_sum >= washing_machine_price:
        print(f"Yes! {sum:.2f}")
else:
        print(f"No! {abs(sum):.2f}")