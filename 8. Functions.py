def hello_func():
    print('Hello Function!')


hello_func()

print()


def hello_func_2():
    return 'Hello Function!'


print(hello_func_2())

print()


def hello_func_3(greeting, name='You'):
    return f'{greeting}, {name}!'


print(hello_func_3('Hi'))
print(hello_func_3('Hi', 'Jude'))

print()


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)
student_info(*courses, **info)
