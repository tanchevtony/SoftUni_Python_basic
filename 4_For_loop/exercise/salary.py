"""
Заплата

Шеф на компания забелязва че все повече служители прекарват  
време в сайтове, които ги разсейват.  
За да предотврати това, той въвежда изненадващи проверки на 
отворените табове на браузъра на служителите си. Според сайта 
се налагат различни глоби:
•	"Facebook" -> 150 лв.
•	"Instagram" -> 100 лв.
•	"Reddit" -> 50 лв.
От конзолата се четат два реда:
•	Брой отворени табове в браузъра n - цяло число в интервала 
[1...10]
•	Заплата - число в интервала [700...1500]
След това n – на брой пъти се чете име на уебсайт – текст
Ако по време на проверката заплатата стане по-малка или равна
на 0 лева, на конзолата се изписва 
"You have lost your salary." и програмата приключва. 
В противен случай след проверката на конзолата се изписва 
остатъкът от заплатата.
"""

open_tabs = int(input())
salary = int(input())

rest_salary = 0

for tab in range(open_tabs):
    open_tab = input()

    if open_tab == "Facebook":
        rest_salary = 150
    elif open_tab == "Instagram":
        rest_salary = 100
    elif open_tab == "Reddit":
        rest_salary = 50
    else:
        rest_salary = 0

    salary -= rest_salary

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)