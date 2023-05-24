def mutate_string(string, position, character):
    aList = list(string)
    aList[position] = character
    newString = ''.join(aList)
    return newString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
