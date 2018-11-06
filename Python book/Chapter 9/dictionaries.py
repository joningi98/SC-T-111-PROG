student = {'name': 'John', 'age': '25', 'courses': ['Math', 'CompSci']}

# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

for key, value in student.items():
    print(key, '=', value)

post2 = dict(message='SS cotopaxi', language='english')

print(student['name'])

print(post2['message'])

my_set = {1, 2, 5, 4, 8, 7, 8, 8, 8, 9}

print(*my_set)

data = [x for x in range(5)]

temp = [x for x in range(7) if x in data and x%2==0]

print(temp)