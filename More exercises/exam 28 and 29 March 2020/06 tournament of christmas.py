days = int(input())
total_win = 0
total_lose = 0
total_money = 0

for i in range(days):
    sport = input()
    win_games = 0
    lose_games = 0
    current_win_money = 0

    while sport != "Finish":
        result = input()

        if result == "win":
            current_win_money += 20
            win_games += 1
        elif result == "lose":
            lose_games += 1
        sport = input()
    total_win += win_games
    total_lose += lose_games
    if win_games > lose_games:
        current_win_money *= 1.10
    total_money += current_win_money
if total_win > total_lose:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")