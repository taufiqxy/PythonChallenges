def minion_game(string):
    # your code goes here
    # uppercase string
    string = string.upper()
    
    # vowel characters
    vowels = {'A', 'I', 'U', 'E', 'O'}
    
    stuartScore = 0
    kevinScore = 0
    for i in range (0, len(string)):
        if not string[i] in vowels:
            stuartScore += len(string)-i
        if string[i] in vowels:
            kevinScore += len(string)-i
    
    if stuartScore > kevinScore:
        print('Stuart ' + str(stuartScore))
    elif kevinScore > stuartScore:
        print('Kevin ' + str(kevinScore))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
