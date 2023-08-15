def isPalindrom(string):

    expandedstring = string[::-1]

    if string == expandedstring:
        return True
    else:
        return False


print(isPalindrom(input()))
