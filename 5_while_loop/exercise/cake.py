side_a = int(input())
side_b = int(input())
pieces = side_a * side_b
count = 0
flag = False
taken = input()
while taken != "STOP":
    taken = int(taken)
    count += taken
    if pieces <= count:
        flag = True
        break
    taken = input()
diff = abs(pieces - count)
if flag:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")

100/100
