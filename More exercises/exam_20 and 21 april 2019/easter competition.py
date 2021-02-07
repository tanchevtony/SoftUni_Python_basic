import sys
number_of_bake = int(input())


top_baker_name = ''
max_points = -sys.maxsize

for i in range(1, number_of_bake + 1):
    name = input()
    sum_grades = 0

    while name != "Stop":
        points = int(input())
        max_points += points
        name = input()
