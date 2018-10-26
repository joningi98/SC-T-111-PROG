import unicodedata

sentence = input("Enter a sentence:")

digits =  0
upper_case = 0
lower_case = 0

for c in sentence:
    if c.isdigit():
        digits = digits + 1
    elif(c.islower()):
        lower_case = lower_case + 1
    elif (c.isupper()):
        upper_case = upper_case + 1
    else:
        pass

punct_property_count = sum('P' in unicodedata.category(c) for c in sentence)

print('%15s  %5s' % ("Upper case", upper_case))
print('%15s  %5s' % ("Lower case", lower_case))
print('%15s  %5s' % ("Digits", digits))
print('%15s  %5s' % ("Punctuation", punct_property_count))
