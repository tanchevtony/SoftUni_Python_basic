result_first = input()
result_second = input()
result_third = input()

win = 0
lost = 0
even = 0

if ord(result_first[0]) > ord(result_first[2]):
    win += 1
elif ord(result_first[0]) < ord(result_first[2]):
    lost += 1
else:
    even += 1

if ord(result_second[0]) > ord(result_second[2]):
    win += 1
elif ord(result_second[0]) < ord(result_second[2]):
    lost += 1
else:
    even += 1

if ord(result_third[0]) > ord(result_third[2]):
    win += 1
elif ord(result_third[0]) < ord(result_third[2]):
    lost += 1
else:
    even += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {even}")