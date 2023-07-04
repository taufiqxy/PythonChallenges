cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    # intial fibonacci
    arr = [0,1]
    
    # get fibonacci list
    for i in range(n-2):
        arr.append(arr[i]+arr[i+1])
    
    # return list
    return(arr[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
