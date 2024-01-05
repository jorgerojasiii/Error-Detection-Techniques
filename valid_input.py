def valid_input(msg):
    if msg == 'vrc':
        while True:
            binary_input = input('Enter a binary number: ')
            
            if binary_input.isdigit() and all(digit in '01' for digit in binary_input):
                return binary_input
            else:
                print("Invalid input. Please enter a valid binary number.")
    elif msg == 'lrc':
        while True:
            binary_input = input('Enter binary blocks separated by spaces: ')
            blocks = binary_input.split()

            # Check if all blocks are valid binary numbers
            if all((block.isdigit() and all(digit in '01' for digit in block)) for block in blocks):
                return blocks
            else:
                print('Invalid input. Make sure each block is a binary number.')