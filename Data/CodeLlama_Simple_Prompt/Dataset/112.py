def reverse_delete(s, c):
    # delete all characters in s that are equal to any character in c
    for char in c:
        s = s.replace(char, "")
    # check if the result string is palindrome
    return (s, s == s[::-1])
