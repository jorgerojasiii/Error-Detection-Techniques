from valid_input import valid_input

def vertical_redundancy_checking():
    print('VERTICAL REDUNDANCY CHECK')
    data = valid_input('vrc')
    data = str(data)
    count_of_1s = data.count('1')
    while True:
        even_or_odd = input('Even or Odd, type e or o: ')
        if even_or_odd.lower() in ['e', 'o']:
            break
        else:
            even_or_odd = input('Even or Odd, type e or o: ')

    if even_or_odd in ['o', 'O']:
        if count_of_1s % 2 == 0:
            parity_bit = 1
        else:
            parity_bit = 0
    elif even_or_odd in ['e', 'E']:
        if count_of_1s % 2 == 0:
            parity_bit = 0
        else:
            parity_bit = 1
    print(f'Parity Bit is {parity_bit}')
    print(f'Transmitted Data: \033[4m{parity_bit}\033[0m{data}')
