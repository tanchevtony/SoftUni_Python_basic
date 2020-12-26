"""
В една кинозала столовете са наредени в правоъгълна форма в r реда 
и c колони. Има три вида прожекции с билети на различни цени:
•	Premiere – премиерна прожекция, на цена 12.00 лева;
•	Normal – стандартна прожекция, на цена 7.50 лева;
•	Discount – прожекция за деца, ученици и студенти на намалена 
цена от 5.00 лева.
Напишете програма, която чете тип прожекция (текст), 
брой редове и брой колони в залата (цели числа), въведени от 
потребителя, и изчислява общите приходи от билети при пълна зала. 
Резултатът да се отпечата във формат 2 знака след десетичната точка.  

"""
screening_type = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if screening_type == "Premiere":
    income = cinema_capacity * 12.00
elif screening_type == "Normal":
    income = cinema_capacity * 7.50
elif screening_type == "Discount":
    income = cinema_capacity * 5.00

print(f"{income:.2f} leva")
