def is_palindrome(a):
    s = str(a)

    if s == s[::-1]:
        return True
    return False

a = int(input("Enter the value of a: "))
print(is_palindrome(a))