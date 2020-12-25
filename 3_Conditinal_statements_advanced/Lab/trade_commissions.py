"""
12.	Търговски комисионни	
Фирма дава следните комисионни на търговците си според града, в който 
работят и обема на продажбите:

Град	0 ≤ s ≤ 500	    500 < s ≤ 1000	    1 000 < s ≤ 10000	s > 10000
Sofia	  5%	            7%	                    8%	            12%
Varna	  4.5%	            7.5%	                10%	            13%
Plovdiv	  5.5%	            8%	                    12%	            14.5%

Напишете конзолна програма, която чете име на град (текст) и обем на 
продажби (реално число), въведени от потребителя, и изчислява и извежда 
размера на търговската комисионна според горната таблица. Резултатът да се 
изведе форматиран до 2 цифри след десетичната точка. При невалиден град 
или обем на продажбите (отрицателно число) да се отпечата "error". 

"""

city = input().lower()
number = float(input())

commission = 0

if city == "sofia":
    if number >= 0 and number <= 500:
        commission = 5
    elif number > 500 and number <= 1000:
        commission = 7
    elif number > 1000 and number <= 10000:
        commission = 8
    elif number > 10000:
        commission = 12
if city == 'varna':
    if number >= 0 and number <= 500:
        commission = 4.5
    elif number > 500 and number <= 1000:
        commission = 7.5
    elif number > 1000 and number <= 10000:
        commission = 10
    elif number > 10000:
        commission = 13
if city == 'plovdiv':
    if number >= 0 and number <= 500:
        commission = 5.5
    elif number > 500 and number <= 1000:
        commission = 8
    elif number > 1000 and number <= 10000:
        commission = 12
    elif number > 10000:
        commission = 14.5
if commission > 0:
    total = number * commission / 100
    print(f"{total:.2f}")
else:
    print('error')
