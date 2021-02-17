player_one = input()
player_two = input()

points_player_one = 0
points_player_two = 0

input_value = input()

while input_value != "End of game":
    card_player_one = int(input_value)
    card_player_two = int(input())

    if card_player_one > card_player_two:
        points_player_one += card_player_one - card_player_two
    elif card_player_two > card_player_one:
        points_player_two += card_player_two - card_player_one
    else:
        print("Number wars!")
        card_player_one = int(input())
        card_player_two = int(input())

        if card_player_one > card_player_two:
            print(f"{player_one} is winner with {points_player_one} points")

        elif card_player_two > card_player_one:
            print(f"{player_two} is winner with {points_player_two} points")
        break

    input_value = input()
if input_value == "End of game":
    print(f"{player_one} has {points_player_one} points")
    print(f"{player_two} has {points_player_two} points")

# 100/100