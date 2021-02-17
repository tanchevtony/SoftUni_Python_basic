control_in_minutes = int(input())
control_in_seconds = int(input())
route_length = float(input())
seconds_per_100 = int(input())

sum_seconds = control_in_minutes * 60 + control_in_seconds
time_late = route_length / 120
total_time_late = time_late * 2.5
marins_time = (route_length / 100) * seconds_per_100 - total_time_late
difference = abs(marins_time - sum_seconds)
if sum_seconds >= marins_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {marins_time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")