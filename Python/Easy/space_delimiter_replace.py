# replace any spaces in a string with - using splits and joins

def split_and_join(line):
    line = line.split(' ')
    result = '-'.join(line)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)