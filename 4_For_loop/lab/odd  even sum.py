"""
Четна / нечетна сума
Да се напише програма, която чете n-на брой цели числа, 
подадени от потребителя, и проверява дали сумата от числата 
на четни позиции е равна на сумата на числата на нечетни позиции. 
При равенство да се отпечатат два реда: "Yes" и на нов ред 
"Sum = " + сумата; иначе да се отпечата 
"No" и на нов ред "Diff = " + разликата. 
Разликата се изчислява по абсолютна стойност. 

"""
n = int(input())

even_num = 0
odd_num = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        even_num += num
    else:
        odd_num += num

if even_num == odd_num:
    print(f"Yes\nSum = {even_num}")
else:
    diff = abs(even_num - odd_num)
    print(f"No\nDiff = {diff}")
