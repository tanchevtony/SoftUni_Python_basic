c_counter = 0
o_counter = 0
n_counter = 0
is_c_found = False
is_o_found = False
is_n_found = False
word = ""

command = input()

while command != "End":
    if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
        if command == "c":
            if c_counter >= 1:
                word += command
            else:
                c_counter += 1
                is_c_found = True
        elif command == "o":
            if o_counter >= 1:
                word += command
            else:
                o_counter += 1
                is_o_found = True
        elif command == "n":
            if n_counter >= 1:
                word += command
            else:
                n_counter += 1
                is_n_found = True
        else:
            word += command
        if is_c_found and is_o_found and is_n_found:
            print(f"{word}", end=" ")
            c_counter = 0
            o_counter = 0
            n_counter = 0
            is_c_found = False
            is_o_found = False
            is_n_found = False
            word = ""

    command = input()
