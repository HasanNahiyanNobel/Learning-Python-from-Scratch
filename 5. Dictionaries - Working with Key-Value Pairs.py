student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

print()

print(student['name'])
print(student.get('name'))
print(student.get('phone'))  # None
print(student.get('phone', 'Not Found'))  # Not Found

print()

student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))

print()

student['name'] = 'Jane'
print(student.get('name'))

print()

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)

print()

del student['age']
print(student)

print()

phone = student.pop('phone')
print(student)
print(phone)

print()

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

print()

for key, value in student.items():
    print(key, value)