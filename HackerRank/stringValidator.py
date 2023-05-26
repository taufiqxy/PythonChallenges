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
# Alternative 2, more safer
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

#########################################################
# Alternative 3, the simple one (using built function)
#########################################################

if __name__ == '__main__':
    s = input()
    
    condition1 = any(aLetter.isalnum() for aLetter in s)
    condition2 = any(aLetter.isalpha() for aLetter in s)
    condition3 = any(aLetter.isdigit() for aLetter in s)
    condition4 = any(aLetter.islower() for aLetter in s)
    condition5 = any(aLetter.isupper() for aLetter in s)
    
    print(condition1)
    print(condition2)
    print(condition3)
    print(condition4)
    print(condition5)

#########################################################
# Alternative 4, another alternative
#########################################################

if __name__ == '__main__':
    s = input()
    
    condition1 = False
    condition2 = False
    condition3 = False
    condition4 = False
    condition5 = False
    
    for aLetter in s:
        if aLetter.isalnum():
            condition1 = True
        if aLetter.isalpha():
            condition2 = True
        if aLetter.isdigit():
            condition3 = True
        if aLetter.islower():
            condition4 = True
        if aLetter.isupper():
            condition5 = True
    
    print(condition1)
    print(condition2)
    print(condition3)
    print(condition4)
    print(condition5)
