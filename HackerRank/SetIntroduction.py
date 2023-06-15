def average(array):
    # your code goes here
    setHeight = set(array)
    
    return sum(setHeight)/len(setHeight)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
