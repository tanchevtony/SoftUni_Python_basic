desired_high = int(input())

fails = 0
total_jumps = 0
current_jumps = 0
current_high = 0
reduced_high = desired_high - 30
flag = False
for i in range(reduced_high, desired_high + 1, 5):
    for j in range(1, 3 + 1):
        total_jumps += 1
        current_high = i
        jumped_high = int(input())

        if jumped_high > i:
            current_jumps += 1
            fails = 0
            break
        else:
            fails += 1

        if fails == 3:
            print(f"Tihomir failed at {i}cm after {total_jumps} jumps.")
            flag = True
            # break # също може дасе прекрати цялата програма с exit()

    if flag:
        break
if not flag:
    print(f"Tihomir succeeded, he jumped over {current_high}cm after {current_jumps} jumps.")
