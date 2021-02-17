number_one = int(input())
number_two = int(input())
magic_number = int(input())
one = 0
two = 0
count = 0
flag = False

for one in range(number_one, number_two + 1):
    for two in range(number_one, number_two + 1):
        count += 1
        if one + two == magic_number:
            print(f"Combination N:{count} ({one} + {two} = {magic_number})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{count} combinations - neither equals {magic_number}")
