# def rectangle_area(x, y):
#     """ the area is base * height """
#     z = x * y
#     print(f"The area is {z}")
#
#
# rectangle_area(5, 6)

def format_name(first_name, last_name):
    # code goes here
    string = ""
    if first_name != "" and last_name != "":
        string = f"Name: {last_name}, {first_name}"
    elif first_name == "" and last_name == "":
        string = ""
    else:
        string = f"Name: {first_name}{last_name}"
    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
