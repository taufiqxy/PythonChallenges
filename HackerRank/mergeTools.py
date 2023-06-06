def merge_the_tools(string, k):
    # your code goes here
    l = len(string)
    n = int(l/k)
    for i in range (0, n):
        block = string[k*i:k*i+k]
        tempList = []
        for c in block:
            if not c in tempList:
                tempList.append(c)
        
        block = ''.join(tempList)
        print(block)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
