import string
sentence = input("Enter a sentence: ")

digits = 0
lower = 0
upper = 0
punctuations = 0

for x in sentence:
    if x.isdigit():
        digits += 1
    elif x.islower():
        lower += 1
    elif x.isupper():
        upper += 1
    elif x in string.punctuation:
        punctuations += 1


print('{:>15s} {:>5d}'.format("Upper case", upper))    # {s} means format string
print('{:>15s} {:>5d}'.format("Lower case ", lower))   # {d} format digit
print('{:>15s} {:>5d}'.format("Digits", digits))
print('{:>15s} {:>5d}'.format("Punctuation", punctuations))
