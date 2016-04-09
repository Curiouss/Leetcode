def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    length = len(s)
    i = 0
    j = length - 1
    counter1 = 0
    counter2 = 0
    if s == "":
        return True
    while i + 1 < length and j > 0:
        if s[i].isalpha() == 0:
            i += 1
            counter1 += 1
        if s[j].isalpha() == 0:
            j -= 1
            counter1 += 1
        if s[i].isalpha() == 1 and s[j].isalpha() == 1:
            if s[i].upper() == s[j].upper():
                i += 1
                j -= 1
            else:
                return False
        if counter1 == counter2:
            i += 1
            j -= 1
            counter1 = counter2
    return True
