data = float(input())

if data >= 26 and data <= 35:
    print("Hot")
elif data >= 20.1 and data <= 25.9:
    print("Warm")
elif data >= 15 and data <= 20:
    print("Mild")
elif data >= 12 and data <= 14.9:
    print("Cool")
elif data >= 5 and data <= 11.9:
    print("Cold")
else:
    print("unknown")