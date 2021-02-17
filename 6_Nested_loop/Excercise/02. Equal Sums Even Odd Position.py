first_number = int(input())
second_number = int(input())
for current_number in range(first_number, second_number + 1):
    odd_digits = 0
    even_digits = 0
    for index, value in enumerate(str(current_number)):
        if index % 2 == 0:
            odd_digits += int(value)
        else:
            even_digits += int(value)
    if odd_digits == even_digits:
        print(f"{current_number}", end=" ")