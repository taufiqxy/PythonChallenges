#########################################################
# Alternative 1, less safer
#########################################################
if __name__ == '__main__':
    s = input()
    
    statements = ['aLetter.isalnum()', 'aLetter.isalpha()',
                  'aLetter.isdigit()', 'aLetter.islower()',
                  'aLetter.isupper()',
                 ]
    
    for aStatement in statements:
        condition = True
        for aLetter in s:
            if eval(aStatement):
                condition = False
                print('True')
                break
        if condition:
            print('False')

#########################################################
# Alternative 2 more safer
#########################################################

if __name__ == '__main__':
    s = input()
    
    # condition function
    def statement1(aLetter):
        return aLetter.isalnum()
    def statement2(aLetter):
        return aLetter.isalpha()
    def statement3(aLetter):
        return aLetter.isdigit()
    def statement4(aLetter):
        return aLetter.islower()
    def statement5(aLetter):
        return aLetter.isupper()
    
    statements = [statement1, statement2, statement3, statement4, statement5]
    
    for aStatement in statements:
        condition = True
        for aLetter in s:
            if aStatement(aLetter):
                condition = False
                print('True')
                break
        if condition:
            print('False')
