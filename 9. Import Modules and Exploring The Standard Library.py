from module_for_lecture_9 import find_index, test
import sys
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print()

print(sys.path)

print()

random_course = random.choice(courses)
print(random_course)
