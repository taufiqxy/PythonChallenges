def split_and_join(line):
    # write your code here
    splitedLine = line.split(" ")
    rejoinLine = "-".join(splitedLine)
    return rejoinLine

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
