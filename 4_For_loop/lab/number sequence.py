"""
Редица цели числа
Напишете програма, която чете n на брой цели числа. 
Принтирайте най-голямото и най-малкото число сред въведените.

Примерен вход и изход
----------------------------
вход	изход		           
5       Max number: 304             
10      Min number: 0 
20
304
0
50			
-----------------------------
вход     изход
6        Max number: 1000
250      Min number: 0
5
2
0
100
1000	
-----------------------------
"""
import sys
n = int(input())

smallest = sys.maxsize
biggest = -sys.maxsize

for i in range(0, n):
    number = int(input())
    if smallest > number:
        smallest = number
    if number > biggest:
        biggest = number

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")

# ver2
# import sys

# n = int(input())

# smallest = sys.maxsize
# biggest = -sys.maxsize

# for i in range(0, n):
#     num = int(input())
#     if smallest > num:
#         smallest = num
#     elif num > biggest:
#         biggest = num

# print(f"Max number: {biggest}\nMin number: {smallest}")