import math
average_speed = float(input())
fuel = float(input())

total_distance = 384400 * 2
time_go_back = math.ceil(total_distance / average_speed)
total_time = time_go_back + 3
needed_fuel = (fuel * total_distance) / 100
print(f"{total_time}\n{int(needed_fuel)}")
