"""
Най-голямо число
Напишете програма, която до получаване на командата 
"Stop", чете цели числа, въведени от потребителя,  
намира най-голямото измежду тях и го принтира. 
Въвежда се по едно число на ред. 
"""
import sys

command = input()

max_number = -sys.maxsize

while command != "Stop":
    number = int(command)
    if number > max_number:
        max_number = number
    command = input()
if max_number != -sys.maxsize: 
    print(max_number)
    
