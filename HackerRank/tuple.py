# this code only work for pypy 3

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_tupple = tuple(integer_list)
    hashed = hash(integer_tupple)
    print(hashed)
