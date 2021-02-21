first = input()
second = input()
third = input()
count = 0
for first_letter in range(ord(first), ord(second) + 1):
    for second_letter in range(ord(first), ord(second) + 1):
        for third_letter in range(ord(first), ord(second) + 1):
            if not chr(first_letter) == third and not chr(second_letter) == third and not chr(third_letter) == third:
                print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
                count += 1
print(f"{count}")