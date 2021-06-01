import sys


# for i in range(ord("a"), ord("z") + 1):
#     print(chr(i))
#
# n = int(input())
# min_num = sys.maxsize
# for i in range(1, n + 1):
#     current_num = int(input())
#     if current_num < min_num:
#         min_num = current_num
# print(min_num)
# lst = []
# num = int(input('How many numbers: '))
# for n in range(num):
#     numbers = int(input('Enter number: '))
#     lst.append(numbers)
# print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

# string = "Data analysis with python"
# result = string.split(" ")
# print(result)
#
# def f(a, L=[]):
#     L.append(a)
#     return L
# f(1)
# f(2)
# print(f(3))

def print_seconds(hours, minutes, seconds):
    print(f"{hours},{minutes},{seconds}")


print_seconds(1, 2, 3)
