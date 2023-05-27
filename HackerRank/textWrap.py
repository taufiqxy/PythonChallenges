import textwrap
import math

def wrap(string, max_width):
    wrappedStr = ''
    totalLine = math.ceil(len(string) / max_width)
    
    for i in range(0, totalLine):
        wrappedStr += string[i*max_width:(max_width * (i+1))] + '\n'
    
    return wrappedStr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
