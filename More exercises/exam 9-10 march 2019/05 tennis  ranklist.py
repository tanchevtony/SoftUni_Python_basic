tournaments = int(input())
points = int(input())

earned_points = 0
wins = 0

for i in range(tournaments):
    stage = input()

    if stage == "W":
        earned_points += 2000
        wins += 1
    elif stage == "F":
        earned_points += 1200
    elif stage == "SF":
        earned_points += 720

total_points = points + earned_points
average_points = int(earned_points / tournaments)
percent_wins = wins / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_wins:.2f}%")


100/100

