"""
Най-малко число
Напишете програма, която до получаване на командата 
"Stop", чете цели числа, въведени от потребителя, 
намира най-малкото измежду тях и го принтира. Въвежда 
се по едно число на ред. 
"""
import sys

command = input()

min_number = sys.maxsize

while command != "Stop":
    number = int(command)
    if number < min_number:
        min_number = number
    command = input()
if min_number != sys.maxsize: 
    print(min_number)