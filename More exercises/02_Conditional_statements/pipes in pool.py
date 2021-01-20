volume = int(input())  #  obem
p1 = int(input())  # debit parva traba
p2 = int(input()) # debit vtora traba
hours = float(input())  # chasovete v koito rabotnikat otsastwa

first_pipe = p1 * hours
second_pipe = p2 * hours

sum_pipes_volume = first_pipe + second_pipe

if sum_pipes_volume <= volume:
    pool_percent = (sum_pipes_volume / volume) * 100
    first_pipe_percent = (first_pipe / sum_pipes_volume) * 100
    second_pipe_percent = (second_pipe / sum_pipes_volume) * 100
