import math

hours_needed = int(input())
days = int(input())
number_of_employee_overtime = int(input())

working_hours = 8 * (days * 0.90)
overtime = number_of_employee_overtime * (2 * days)
total_time = math.floor(working_hours + overtime)
time_needed = abs(hours_needed - total_time)

if total_time >= hours_needed:
    print(f"Yes!{time_needed} hours left.")
else:
    print(f"Not enough time!{time_needed} hours needed.")

