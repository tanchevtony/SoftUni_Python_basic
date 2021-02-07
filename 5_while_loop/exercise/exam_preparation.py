# number_of_fails = int(input())
#
# fails = 0
# sum_grade = 0
# problems_count = 0
# last_problem = ""
#
# while name != "Enough":
#     pass
#     if grade <= 4:
#         fails += 1
#
#     else:
#         problems_count += 1
#         sum_grade += grade
#         last_problem = name
#     name = input()
#     grade = float(input)


# a = 5
# while True:
#     if a > 10:
#         break
#     print(f"a = {a}")
#     a += 1

# new problem while loop

# name = input()
#
# while name != "Stop":
#     print(name)
#     name = input()
#

# new problem whule loop

# username = input()
# password = input()
#
# data = input()
#
# while data != password:
#     data = input()
# print(f"Welcome {username}")

# new problem whule loop

# new problem

# number = int(input())
# count = 1
# while count <= number:
#     print(count)
#     count = 2 * count + 1

player_one_eggs = int(input())
player_two_eggs = int(input())

command = input()
while command != "End of battle":
    if command == "one":
        player_two_eggs -= 1
        if player_two_eggs <= 0:
            print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
            break
    elif command == "two":
        player_one_eggs -= 1
        if player_one_eggs <= 0:
            print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
            break
    command = input()

if command == "End of battle":
    print(f"Player one has {player_one_eggs} eggs left.")
    print(f"Player two has {player_two_eggs} eggs left.")
