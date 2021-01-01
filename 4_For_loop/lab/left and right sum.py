""" 
Лява и дясна сума

Да се напише програма, която чете 2*n-на брой цели числа, 
подадени от потребителя, и проверява дали сумата на първите 
n числа (лява сума) е равна на сумата на вторите n числа 
(дясна сума). При равенство печата " Yes, sum = " + сумата; 
иначе печата " No, diff = " + разликата. Разликата се изчислява 
като положително число (по абсолютна стойност).
"""
n = int(input())

left_sum = 0
right_sum = 0

for i in range (n):
    num = int(input())
    left_sum += num

for k in range(n):
    num = int(input())
    right_sum += num

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")





# n = int(input())

# left_sum = 0
# right_sum = 0

# for num in range(0, n*2):
#     cur_num = int(input())
#     if left_sum == right_sum:
#         left_sum += cur_num
#     elif num >= n:
#         right_sum += cur_num

# if left_sum == right_sum:
#     print(f"'Yes, sum = {right_sum}")
# else:
#    print(f"No, diff = {abs(left_sum - right_sum)}")