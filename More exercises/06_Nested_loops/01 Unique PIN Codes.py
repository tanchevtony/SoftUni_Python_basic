first_number_limit = int(input())
second_number_limit = int(input())
third_number_limit = int(input())

for first in range(1, first_number_limit + 1):
    if first % 2 == 0:
        for second in range(2, second_number_limit + 1):
            if second == 2 or second == 3 or second == 5 or second == 7:
                for third in range(1, third_number_limit + 1):
                    if third % 2 == 0:
                        print(f"{first} {second} {third}")
                     