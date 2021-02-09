actor_name = input()
rating = float(input())
judges = int(input())

total_points = 0 + rating

for i in range(1, judges + 1):
    judge_name = input()
    given_points = float(input())
    total_points += len(judge_name) * given_points / 2
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = abs(1250.5 - total_points)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
