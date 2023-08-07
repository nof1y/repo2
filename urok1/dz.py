def isPalindrom(s1):

    s2 = s1[::-1]

    if s1 == s2:
        return True
    else:
        return False


print(isPalindrom(input()))
