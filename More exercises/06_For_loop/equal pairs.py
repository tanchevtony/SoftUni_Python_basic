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

# another solution

pairs = int(input())

sum_numbers = 0
first_pair = 0
Difference = 0
Max_Difference = 0

for i in range(1, 2 * pairs + 1):
    num = int(input())
    sum_numbers += num
    if i % 2 == 0 and i != 2:
        Difference = abs(sum_numbers - first_pair)
        if Difference > Max_Difference:
            Max_Difference = Difference
        first_pair = sum_numbers
        sum_numbers = 0
    elif i == 2:
        first_pair = sum_numbers
        sum_numbers = 0

if Max_Difference == 0:
    print(f'Yes, value={first_pair}')
else:
    print(f'No, maxdiff={Max_Difference}')