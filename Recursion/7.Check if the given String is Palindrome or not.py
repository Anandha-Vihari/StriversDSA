def palindrome(s):
    rev=s[::-1]
    return True if s==rev else False

print(palindrome("abccba"))