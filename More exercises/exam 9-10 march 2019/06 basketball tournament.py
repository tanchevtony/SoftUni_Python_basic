tournament_name = input()

desi_team_wins = 0
desi_team_lose = 0
count = 0

while tournament_name != "End of tournaments":
    games_number = int(input())
    count += games_number
    for i in range(1, games_number + 1):
        points_desi_team = int(input())
        points_b_team = int(input())

        difference = abs(points_desi_team - points_b_team)

        if points_desi_team > points_b_team:
            desi_team_wins += 1
            print(f"Game {i} of tournament {tournament_name}: win with {difference} points.")
        else:
            desi_team_lose += 1
            print(f"Game {i} of tournament {tournament_name}: lost with {difference} points.")

    tournament_name = input()
average_wins = desi_team_wins / count * 100
average_lose = desi_team_lose / count * 100
print(f"{average_wins:.2f}% matches win")
print(f"{average_lose:.2f}% matches lost")

100/100
