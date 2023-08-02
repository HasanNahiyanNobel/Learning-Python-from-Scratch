language = 'Python'

if language == 'Python':
    print('Conditional was True')

print()

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

print()

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

print()

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

print()

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(id(a))
print(id(b))
print(a == b)
