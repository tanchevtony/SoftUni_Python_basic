import math
series_name = input()
time_per_episode = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4
left_time = break_time - rest_time - lunch_time
difference = math.ceil(abs(time_per_episode - left_time))

if left_time >= time_per_episode:
    print(f"You have enough time to watch {series_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {difference} more minutes.")
