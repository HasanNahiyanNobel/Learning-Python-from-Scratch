courses = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Philosophy', 'Social Studies']

print(courses)
print(len(courses))  # Prints the length of the list
print(courses[0])  # Prints the first item in the list
print(courses[-1])  # Prints the last item in the list

print()

print(courses[0:2])  # Prints the first two items in the list
print(courses[:2])  # Prints the first two items in the list, just like strings

print()

courses.append('Art')  # Adds an item to the end of the list
print(courses)

print()

courses.insert(0, 'Chemistry')  # Adds an item to the beginning of the list

print()

"""
Important Notes
"""
courses.insert(0, courses2)  # Adds a list to the beginning of the list
print(courses)
courses.append(courses2)  # Adds a list to the end of the list
print(courses)
courses.extend(courses2)  # Adds a list to the end of the list
print(courses)

print()

courses.remove('Math')  # Removes an item from the list
print(courses)
courses.pop()  # Removes the last item from the list
print(courses)

print()

courses.reverse()  # Reverses the order of the list
print(courses)

print()

courses.remove(['Philosophy', 'Social Studies'])  # Removes the first list from the list
courses.remove(['Philosophy', 'Social Studies'])  # Removes the second list from the list
print(courses)

print()

courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

print()

"""
Important Notes
"""
sorted_courses = sorted(courses)  # Returns a sorted list, and doesn't change the original list
print(courses)
print(sorted_courses)

print()

"""
Important Notes
"""
print('Art' in courses)  # Returns True if the item is in the list, and False if it isn't
print('Biology' in courses)  # Returns True if the item is in the list, and False if it isn't

print()

for index, course in enumerate(courses, start=1):  # `start=1` starts the index at 1 instead of 0
    print(index, course)

print()

course_str = ' - '.join(courses)  # Joins the items in the list with the string
print(course_str)

print()

new_list = course_str.split(' - ')  # Splits the string into a list
print(new_list)

print()

courses1 = ['History', 'Math', 'Physics', 'CompSci']
courses2 = courses1  # This doesn't create a copy of the list, but rather a reference to the original list

print(courses1)
courses1[0] = 'Zoology'
print(courses1)
print(courses2)

print()

"""
Important Notes
"""
tuple1 = ('History', 'Math', 'Physics', 'CompSci')
tuple2 = tuple1  # This doesn't create a copy of the tuple, but rather a reference to the original tuple

# tuple1[0] = 'Zoology'  # This will throw an error, because tuples are immutable

print(tuple1)
print(tuple2)

print()

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}  # Sets don't allow duplicates
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print('Math' in cs_courses)  # Returns True if the item is in the set, and False if it isn't
print(cs_courses.intersection(art_courses))  # Returns the it-b ems that are in both sets
print(cs_courses.difference(art_courses))  # Returns the items that are in the first set, but not the second set
print(cs_courses.union(art_courses))  # Returns the items that are in either set
