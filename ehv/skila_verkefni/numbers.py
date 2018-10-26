sentence = input("Enter a sentence: ")
digits = 0
l = 0

for c in sentence:
    if c.isdigit():
        digits += 1
    else:
        pass

lower_case = 0
upper_case = 0

for c in sentence:
      if(c.islower()):
            lower_case += 1
      elif(c.isupper()):
            upper_case += 1

#fann ekki betri leið til þess að finna Punctuation 

import re 
import unicodedata

punct_property_count = sum('P' in unicodedata.category(c) for c in sentence)

print("{:>5s} {:15d}".format("Lower case", lower_case))
print("{:>5s} {:15d}".format("Upper case", upper_case))
print("{:>5s} {:15d}".format("Digits", digits))
print("{:5s} {:15d}".format("Punctuation", (punct_property_count)))     
 

