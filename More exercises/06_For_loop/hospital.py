days = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, days + 1):
    current_patients = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1

    if current_patients > doctors:
        treated_patients += doctors
        untreated_patients += current_patients - doctors
    else:
        treated_patients += current_patients

print(f"Treated patients: {treated_patients}.\nUntreated patients: {untreated_patients}.")
