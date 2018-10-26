in_str = input("Enter a string: ")

def palindrome(in_str):
    new_word = in_str.replace("'", '').replace('!', '').replace(' ', '').replace(',', '').lower()
    new_word = new_word.lower()
    if new_word == new_word[::-1]:
        return True
    else:
        return False

if palindrome(in_str):
    print('"' + in_str + '"', "is a palindrome.")
else:
    print('"' + in_str + '"', "is not a palindrome.")