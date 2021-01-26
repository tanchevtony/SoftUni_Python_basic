days = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, days + 1):
    patients = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1


print(f"Treated Patients: {treated_patients}.\nUntreated patients: {untreated_patients}.")


