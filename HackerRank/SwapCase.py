def swap_case(s):
    newS = ''
    for aLetter in s:
        if aLetter.isupper():
            newS += aLetter.lower()
        elif aLetter.islower():
            newS += aLetter.upper()
        else:
            newS += aLetter
            
    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
