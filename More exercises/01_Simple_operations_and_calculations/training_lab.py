import math

l = float(input()) * 100
w = float(input()) * 100

length = 120
width = 70
row = math.trunc(l / length)
column = math.trunc((w - 100) / width)

total = (row * column) - 3
print(total)