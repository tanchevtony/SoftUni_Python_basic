number = int(input())

for i in range(1000, 10000):
    string_i = str(i)
    if string_i[1] != str(0) and string_i[2] != str(0) and string_i[3] != str(0):
        sum_first_two = int(string_i[0]) + int(string_i[1])
        sum_second_two = int(string_i[2]) + int(string_i[3])
        if sum_first_two == sum_second_two:
            if number % sum_first_two == 0:
                print(f'{string_i}', end=" ")