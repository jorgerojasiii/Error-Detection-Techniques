from valid_input import valid_input

def cyclic_redundancy_check():
    """
    wag tularan, gawang tamad
    """
    print('CYCLIC REDUNDANCY CHECK')
    dividend = valid_input('crc1')
    divisor = valid_input('crc2')
    tdivisor = divisor
    ans = ''
    dividend = [str(num) for num in dividend]
    dividend_zeroes = [str(0) for num in range(len(divisor)-1)]
    dividend.extend(dividend_zeroes)
    xor = ''.join(dividend[:len(divisor)])
    del dividend[:len(divisor)]
    ans += str(xor[0])
    while len(dividend) > 0:        
        y=int(xor,2) ^ int(divisor,2)
        xor = bin(y)[2:].zfill(len(xor))[1:]
        ans += str(xor[0])
        if str(xor[0]) == '0':
            divisor = ''.join(['0' for num in range(len(tdivisor))])
        else:
            divisor = tdivisor
        xor = str(xor) + str(dividend[0])
        del dividend[0]
    if str(xor[0]) == '0':
        divisor = ''.join(['0' for num in range(len(tdivisor))])
    else:
        divisor = tdivisor
    y=int(xor,2) ^ int(divisor,2)
    xor = bin(y)[2:].zfill(len(xor))[1:]
    print(f'Quotient: {ans}, Remainder: {xor}')
    

cyclic_redundancy_check()
