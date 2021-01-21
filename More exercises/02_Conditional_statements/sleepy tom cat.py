days_off = int(input())

norm_play = 30000
work = 63
off_work = 127
days_in_year = 365

working_days = days_in_year - days_off
time = working_days * work + days_off * off_work

if time > norm_play:
    hours = ((time) - norm_play) // 60
    minutes = ((time) - norm_play) % 60

    print("Tom will run away")
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    hours = (norm_play - (time)) // 60
    minutes = (norm_play - (time)) % 60
    print("Tom sleeps well")
    print(f'{hours} hours and {minutes} minutes less for play')
