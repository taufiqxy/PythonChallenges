def count_substring(string, sub_string):
    totalFound = 0
    for i in range(0, len(string)):
        if string.find(sub_string, i, (len(sub_string)+i)) != -1:
            totalFound += 1
    return totalFound

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
