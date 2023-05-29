def print_rangoli(size):
    # your code goes here
    size = int(size)
    let = [chr(97+i) for i in range(0, size)]
    
    # top part
    for i in range(0, size):
        pattern = let[size-i-1]
        for j in range(0, i):
            pattern = let[size-i-1+j+1] + '-' + pattern + '-' + let[size-i-1+j+1]
        print(pattern.center((size*2-1)+((size*2-1)-1), '-'))
    
    # bottom part
    for i in range(0, size-1):
        pattern = let[i+1]
        for j in range(0, size-i-2):
            pattern = let[i+1+j+1] + '-' + pattern + '-' + let[i+1+j+1]
        print(pattern.center((size*2-1)+((size*2-1)-1), '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
