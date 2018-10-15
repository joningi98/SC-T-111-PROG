with open("words.txt", "r") as rf:
    for line in rf:
        replace = line.replace('. ', '\n')
        stripped = replace.strip()
        print(stripped, end=" ")
    with open("sentences.txt", "w") as w:
        stripped = replace.strip()
        w.write(stripped)

with open("words.txt", 'r+') as f:
    text = f.read()
    text = wr.sub('foobar', 'bar', text)
    f.seek(0)
    f.write(text)
    f.truncate()

# ‘r’ – Read mode which is used when the file is only being read
# ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
# ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
# ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file

file = open("words.txt", "r")
print(file.read())

file = open("words.txt", "r")
print(file.readline(3))           # Third line in file



with open(“hello.text”, “r”) as f:
data = f.readlines()

for line in data:
words = line.split()
print words
