# a = 5
# while True:
#     if a > 10:
#         break
#     print("a = " + str(a))
#     a += 1

line = input()
text =[]
while line != "Stop":
    text.append(line)
    line = input()
print(text)