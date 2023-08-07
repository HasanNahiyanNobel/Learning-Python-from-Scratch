print('imported module_for_lecture_9.py')

test = 'test string'


def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
