number_of_days = int(input())

for locations in range(number_of_days):
    expected_yield = float(input())
    days = int(input())
    current_yield = 0
    for days_in_locations in range(days):
        yield_per_day = float(input())
        current_yield += yield_per_day
    average_yield = current_yield / days
    if average_yield >= expected_yield:
        print(f"Good job! Average gold per day: {average_yield:.2f}.")
    else:
        diff = expected_yield - average_yield
        print(f"You need {diff:.2f} gold.")
