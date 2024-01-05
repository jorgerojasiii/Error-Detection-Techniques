from valid_input import valid_input
from functools import reduce
from operator import xor

def longitudinal_redundancy_check():
    print('LONGITUDINAL REDUNDANCY CHECK')
    data = valid_input('lrc')
    result = reduce(xor, (int(binary, 2) for binary in data))

    # Convert the result back to binary
    lrc = bin(result)[2:].zfill(len(data[0]))
    data_ = ''.join(data[::-1])
    print(f'Parity Block is {lrc}')
    print(f'Transmitted data: \033[4m{lrc}\033[0m{data_}')


longitudinal_redundancy_check()  