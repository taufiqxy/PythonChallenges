def print_formatted(number):
    # your code goes here
    maxBinLen = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        print(str(i).rjust(maxBinLen, ' ')+ ' ' +str(oct(i)[2:]).rjust(maxBinLen, ' ')+ ' ' +str(hex(i)[2:]).upper().rjust(maxBinLen, ' ')+ ' ' +str(bin(i)[2:]).rjust(maxBinLen, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
