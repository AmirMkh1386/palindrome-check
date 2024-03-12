def is_palindrome(word):
    return word == word[::-1]

word = input("Enter number:")

if is_palindrome(word):
    print("it is a palindrome")
else:
    print("It is not palindrome")