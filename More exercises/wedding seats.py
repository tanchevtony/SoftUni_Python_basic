last_sector = input()
number_of_rows_in_first_sector = int(input())
odd_row_places = int(input())
last_sector_ord = ord(last_sector)
counter = 0
for each_sector in range(65, last_sector_ord + 1):
    if each_sector > 65:
        number_of_rows_in_first_sector += 1
    for each_row in range(1, number_of_rows_in_first_sector + 1):
        if each_row % 2 == 0:
            seats = odd_row_places + 2
        else:
            seats = odd_row_places
        for each_place in range(97, 97 + seats):
            counter += 1
            print(f'{chr(each_sector)}{each_row}{chr(each_place)}')
print(counter)