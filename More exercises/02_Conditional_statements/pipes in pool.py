volume = int(input())  # obem
p1 = int(input())  # debit parva traba
p2 = int(input())  # debit vtora traba
hours = float(input())  # chasovete v koito rabotnikat otsastwa

first_pipe = p1 * hours
second_pipe = p2 * hours

sum_pipes_volume = first_pipe + second_pipe

if sum_pipes_volume <= volume:
    pool_percent = (sum_pipes_volume / volume) * 100
    first_pipe_percent = (first_pipe / sum_pipes_volume) * 100
    second_pipe_percent = (second_pipe / sum_pipes_volume) * 100
    print(f"The pool is {pool_percent:.2f}% full. Pipe 1: {first_pipe_percent:.2f}%. Pipe 2: {second_pipe_percent:.2f}%")
else:
    overflow = sum_pipes_volume - volume
    print(f"For {hours:.2f} hours the pool overflows with {overflow:.2f} liters.")
