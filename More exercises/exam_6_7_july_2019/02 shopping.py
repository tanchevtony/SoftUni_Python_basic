budget = float(input())
number_of_gpu = int(input())
number_of_cpu = int(input())
number_of_ram = int(input())

gpu_price = 250 * number_of_gpu
cpu_price = gpu_price * 0.35 * number_of_cpu
ram_price = gpu_price * 0.10 * number_of_ram

total = gpu_price + cpu_price + ram_price


if number_of_gpu > number_of_cpu:
    total *= 0.85
if budget >= total:
    diff = budget - total
    print(f"You have {diff:.2f} leva left!")
else:
    diff = abs(total - budget)
    print(f"Not enough money! You need {diff:.2f} leva more!")

# 100/100

