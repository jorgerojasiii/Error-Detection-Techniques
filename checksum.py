from valid_input import valid_input
def checksum():
    print('CHECKSUM')
    data = valid_input('checksum')
    binary_sum = bin(sum(int(binary, 2) for binary in data))[2:]
    while True:
        left, right = binary_sum[:len(binary_sum) - len(data[0])], binary_sum[-len(data[0]):]
        binary_sum = bin(int(left, 2) + int(right, 2))[2:].zfill(len(data[0]))
        if len(binary_sum) == len(data[0]):
            break
    data_ = ''.join(data)
    print(f'Parity Block is {binary_sum}')
    print(f'Transmitted data: \033[4m{binary_sum}\033[0m{data_}')
checksum()