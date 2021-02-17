import math

word = input()
biggest_sum = 0
powerful_word = ''

while word != "End of words":
    current_sum = 0

    for letter in word:
        current_sum += ord(letter)
    if word[0].lower() in "aeiouy":
        current_sum *= len(word)
    else:
        current_sum = math.floor(current_sum / len(word))
    if current_sum > biggest_sum:
        biggest_sum = current_sum
        powerful_word = word

    word = input()

if word == "End of words":
    print(f'The most powerful word is {powerful_word} - {biggest_sum}')


#  вариант 2 на същата задача

command = input()
max_sum = 0
max_word = ""
while command != "End of words":
    current_sum = sum([ord(i) for i in command])
    if command[0].lower() in "aeiouy":
        current_sum *= len(command)
    else:
        current_sum /= len(command)
    if current_sum > max_sum:
        max_sum = current_sum
        max_word = command
    command = input()
print(f"The most powerful word is {max_word} - {max_sum}")

# #  вариант 3 на същата задача

command = input()
most_powerful_word = ''
max_power = 0
while command != 'End of words':
    current_word = command
    current_power = 0
    for letter in current_word:
        current_power += ord(letter)
    must_be_multiplied = False
    if current_word[0] == 'a' or current_word[0] == "A":  #current_word[0].lower()=='a'
        must_be_multiplied = True
    if current_word[0] == 'e' or current_word[0] == "E":  #current_word[0].lower()=='a'
        must_be_multiplied = True
    if current_word[0] == 'i' or current_word[0] == "I":  #current_word[0].lower()=='a'
        must_be_multiplied = True
    if current_word[0] == 'o' or current_word[0] == "O":  #current_word[0].lower()=='a'
        must_be_multiplied = True
    if current_word[0] == 'u' or current_word[0] == "U":  #current_word[0].lower()=='a'
        must_be_multiplied = True
    if current_word[0] == 'y' or current_word[0] == "Y":  #current_word[0].lower()=='a'
        must_be_multiplied = True
    if must_be_multiplied:
        current_power *= len(current_word)
    else:
        current_power = int(current_power / len(current_word))
    if current_power > max_power:
        max_power = current_power
        most_powerful_word = current_word
    command = input()
print(f"The most powerful word is {most_powerful_word} - {max_power}")