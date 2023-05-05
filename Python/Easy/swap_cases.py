# create a function to swap the case of every character in a string entered

def swap_case(s):
    new_case = []
    for char in s:
        if char.isupper() == True:
            new_case.append(char.lower())
        elif char.islower() == True:
            new_case.append((char.upper()))
        else:
            new_case.append(char)
    result = ''.join(new_case) 
    return result

if __name__ == '__main__':
    s = input("Enter a string to change the case of: ")
    result = swap_case(s)
    print(result)