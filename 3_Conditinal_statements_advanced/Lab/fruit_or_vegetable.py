"""
Плод или зеленчук
Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
•	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
•	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
•	Всички останали са "unknown".
Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт.

Примерен вход и изход
вход	изход		вход	изход		вход	изход		    вход	изход
banana	fruit		apple	fruit		tomato	vegetable		water	unknown
"""
name = input()

if name == "banana" or  name == "apple" or name == "kiwi" or name == "cherry" or name == "lemon"  or name == "grapes":
    print("fruit")
elif name == "tomato" or name == "cucumber" or name ==  "pepper" or name == "carrot":
    print("vegetable")
else:
    print("unknown")