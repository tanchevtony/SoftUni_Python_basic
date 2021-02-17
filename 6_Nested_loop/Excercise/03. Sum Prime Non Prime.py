command = input()
prime_numbers = 0
nonprime_numbers = 0

while command != "stop":
    command = int(command)
    is_prime = False
    if command < 0:
        print(f"Number is negative.")
    else:
        for i in range(2, command):
            if command % i == 0:
                is_prime = True
                break
        if not is_prime:
            prime_numbers += command
        else:
            nonprime_numbers += command

    command = input()
print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {nonprime_numbers}")
