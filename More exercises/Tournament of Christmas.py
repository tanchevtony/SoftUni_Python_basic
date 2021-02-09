number_of_tournament_days = int(input())

total_raised_money = 0

for i in range(1, number_of_tournament_days + 1):

    sport = input()
    while sport != "Finish":
        result = input()

        if result == "win":
            total_raised_money += 20
        elif result == "lose":

        sport = input()


