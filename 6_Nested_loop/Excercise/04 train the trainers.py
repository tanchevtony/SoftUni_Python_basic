judges = int(input())
total_grade = 0
count = 0
command = input()
while command != "Finish":
    current_grade = 0
    for i in range(judges):
        grade = float(input())
        current_grade += grade
    current_grade /= judges
    print(f"{command} - {current_grade:.2f}.")
    total_grade += current_grade
    count += 1
    command = input()
final_assessment = total_grade / count
print(f"Student's final assessment is {final_assessment:.2f}.")

