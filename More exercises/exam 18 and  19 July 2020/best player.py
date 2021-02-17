best_player = ""
max_scores = 0
hat_trick = 0
player_name = input()
while player_name != "END":

    score = int(input())
    if player_name == "END":
        break
    if score > max_scores:
        best_player = player_name
        max_scores = score
        if score >= 3:
            hat_trick = score
            if max_scores >= 10:
                break
    player_name = input()
print(f"{best_player} is the best player!")
if hat_trick != 0:
    print(f"He has scored {max_scores} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_scores} goals.")
