# player_one_eggs = int(input())
# player_two_eggs = int(input())
#
# command = input()
# while command != "End of battle":
#     if command == "one":
#         player_two_eggs -= 1
#         if player_two_eggs <= 0:
#             print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
#             break
#     elif command == "two":
#         player_one_eggs -= 1
#         if player_one_eggs <= 0:
#             print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
#             break
#     command = input()
#
# if command == "End of battle":
#     print(f"Player one has {player_one_eggs} eggs left.")
#     print(f"Player two has {player_two_eggs} eggs left.")

book = input()
count = 0
is_book_found = False
command = input()
while command != "No More Books":

    count += 1
    if command == book:
        is_book_found = True
        break

    command = input()
if is_book_found:
    print(f"You have checked {count} books and found it.")