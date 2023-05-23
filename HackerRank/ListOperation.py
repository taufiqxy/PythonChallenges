# this challenge is about list operation

if __name__ == '__main__':
    N = int(input())
    
    aList = []
    
    for _ in range(N):
        instruction = input().split(' ')
        if instruction[0] == 'insert':
            aList.insert(int(instruction[1]), int(instruction[2]))
        elif instruction[0] == 'print':
            print(aList)
        elif instruction[0] == 'remove':
            aList.remove(int(instruction[1]))
        elif instruction[0] == 'append':
            aList.append(int(instruction[1]))
        elif instruction[0] == 'sort':
            aList.sort()
        elif instruction[0] == 'pop':
            aList.pop()
        elif instruction[0] == 'reverse':
            aList.reverse()
        else:
            print('command not found')
