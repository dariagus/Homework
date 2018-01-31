def is_palindrome(x):
    x = x.lower()
    x = x.replace(' ', '')
    if x == x[::-1]:
        return True
    else:
        return False

