n = int(input())

num_1 = 0
num_2 = 0
sum_1 = 0
sum_2 = 0
max_sum = 0

for i in range(0, n):

    if i % 2 == 0:
        first_n = int(input())
        second_n = int(input())
        sum_2 = first_n + second_n
    else:
        first_n = int(input())
        second_n = int(input())
        sum_1 = first_n + second_n
if i > 0:
    if sum_1 != sum_2:
        max_sum = abs(sum_1 - sum_2)
if max_sum == 0:
    print(f"Yes, value={sum_2}")
else:
    print(f"No, maxdiff={max_sum}")