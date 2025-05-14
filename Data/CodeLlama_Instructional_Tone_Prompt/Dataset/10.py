def make_palindrome(string):
    # find the longest postfix of supplied string that is a palindrome
    postfix = ""
    for i in range(len(string)):
        if string[:len(string) - i] == string[len(string) - i:][::-1]:
            postfix = string[:len(string) - i]
            break
    # append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + postfix[::-1]
