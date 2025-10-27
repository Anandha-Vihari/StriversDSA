def is_palindrome(n):
    rev=0
    dup=n
    while n>0:
        ld=n%10
        rev=(rev*10)+ld
        n=n//10
    if rev==dup:
        return "Palindrome"
    else:
        return "Not a Palidrome"
print(is_palindrome(11113631))