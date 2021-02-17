poor_grades = int(input())

last_problem = ""
fails = 0
solved_problems = 0
grades = 0
flag = False
name = input()
while name != "Enough":
    grade = int(input())

    if grade <= 4:
        fails += 1
    solved_problems += 1
    last_problem = name
    grades += grade
    if fails == poor_grades:
        flag = True
        break

    name = input()

average_score = grades / solved_problems
if flag:
    print(f"You need a break, {fails} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")






















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

