type_of_gas = input(str())
liters = float(input())

type1 = 'diesel'
type2 = 'gasoline'
type3 = 'gas'

if type_of_gas == 'Diesel':
    if liters >= 25:
        print(f'You have enough {type1}.')
    else:
        print(f'Fill your tank with {type1}!')

elif type_of_gas == 'Gasoline':
    if liters >= 25:
        print(f'You have enough {type2}.')
    else:
        print(f'Fill your tank with {type2}!')

elif type_of_gas == 'Gas':
    if liters >= 25:
        print(f'You have enough {type3}.')
    else:
        print(f'Fill your tank with {type3}!')
else:
    print('Invalid fuel!')