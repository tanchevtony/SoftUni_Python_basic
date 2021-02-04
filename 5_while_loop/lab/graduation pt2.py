"""
7.	Завършване – част 2
Напишете програма, която изчислява средната оценка на 
ученик от цялото му обучение. На първия ред ще получите 
името на ученика, а на всеки следващ ред - неговите 
годишни оценки. Ученикът преминава в следващия клас, 
ако годишната му оценка е по-голяма или равна на 4.00. 
Ако ученикът бъде скъсан повече от един път, то той бива 
изключен и програмата приключва, като се отпечатва името 
на ученика и в кой клас е изключен.
 При успешно завършване на 12-ти клас да се отпечата : 
"{име на ученика} graduated. Average grade: {средната 
оценка от цялото обучение}"
В случай, че ученикът е изключен от училище, да се 
отпечата:
"{име на ученика} has been excluded at {класа, в който 
е бил изключен} grade"
Стойността трябва да бъде форматирана до втория знак 
след десетичната запетая.
"""
name = input()

current_class = 0   # class reached
fails = 0   # how many fails
grade = 0   # grade sum

while current_class < 12:
    current_grade = float(input())
    if current_grade < 4:
        fails += 1
        if fails == 2:
            break
    grade += current_grade
    current_class += 1
if fails:
    print(f"{name } has been excluded at {current_class} grade")
else:
    average_grade = grade / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
