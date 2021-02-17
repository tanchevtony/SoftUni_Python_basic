n = int(input())
l = int(input())

alphabet = "abcdefghijklmnopqrstuwxyz"
for symbol_1 in range(1, n):
    for symbol_2 in range(1, n):
        for symbol_3_index in range(l):
            symbol_3 = alphabet[symbol_3_index]
            for symbol_4_index in range(l):
                symbol_4 = alphabet[symbol_4_index]
                for symbol_5 in range(1, n + 1):
                    if symbol_5 > symbol_1 and symbol_5 > symbol_2:
                        print(f"{symbol_1}{symbol_2}{symbol_3}{symbol_4}{symbol_5}", end=" ")

#  решение на задачата с ascii

n = int(input())
l = int(input())
for first in range(1, n + 1):
    for second in range(1, n + 1):
        for third in range(97, 97 + l):
            for fourth in range(97, 97 + l):
                for fifth in range(1, n + 1):
                    if fifth > first and fifth > second:
                        print(f'{first}{second}{chr(third)}{chr(fourth)}{fifth}', end=" ")