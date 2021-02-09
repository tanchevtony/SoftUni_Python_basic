counter = int(input())
sum_count = 0
for i in range(1, counter + 1):
    number = int(input())
    sum_count += number
average = sum_count / counter
print(f"{average:.2f}")