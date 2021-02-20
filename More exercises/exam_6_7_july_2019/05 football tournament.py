football_team = input()
played_games = int(input())
w = 0
d = 0
l = 0

for i in range(played_games):
    result = input()

    if result == "W":
        w += 1
    elif result == "D":
        d += 1
    elif result == "L":
        l += 1
if played_games == 0:
    print(f"{football_team} hasn't played any games during this season. ")
else:
    total_points = w * 3 + d
    percent = w / played_games * 100
    print(f"{football_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {percent:.2f}%")
