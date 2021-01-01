"""
Елемент, равен на сумата на останалите
Да се напише програма, която чете n-на брой цели числа, 
въведени от потребителя, и проверява дали сред тях съществува 
число, което е равно на сумата на всички останали. 
Ако има такъв елемент, печата
 "Yes"
"Sum = "  + неговата стойност ,
иначе печата "No"
"Diff = " + разликата между най-големия елемент и сумата 
 на останалите (по абсолютна стойност). 
"""

import sys

n = int(input())

sum_numbers = 0
max_number = -sys.maxsize

for i in range(0,n):
    num = int(input())
    sum_numbers += num

    if num > max_number:
        max_number = num
sum_numbers -= max_number

if sum_numbers == max_number:
    print(f'Yes\nSum = {sum_numbers}')
else:
    print(f'No\nDiff = {abs(max_number - sum_numbers)}')