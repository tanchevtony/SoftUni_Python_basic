number = int(input())
counter = 1
all_printed = False
for row in range(1, number + 1):
    for column in range(1, row + 1):

        if counter > number:
            all_printed = True
            break
        print(f"{counter}", end=" ")
        counter += 1
    if all_printed:
        break
    print()