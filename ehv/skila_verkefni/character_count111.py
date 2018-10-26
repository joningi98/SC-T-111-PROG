sentence = input("Enter a sentence:")

print(len(sentence))


#count number og spaces
print("count of number of spaces in sentance is {}".format(sentence.count(' ')))

#count numbers

print(sentence.count)

#String 10 spaces wide including the object, right justified (>).
#print('{:>10s} is {:<10d} years old.' format('Bill', 25))
print("{} is {} years old".format("Bill",25))
#Bill is 25 years old.
print("{:>10s} is {:<10d} years old".format("Bill",25))
#Bill is 25 years old.

for i in range(5):
    print("{:10d} --> {:4d}".format(i,i**2))

