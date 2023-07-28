# A simple message
message = 'Hello World!'

print(message[0:5])  # The first number is inclusive, but the second one is exclusive
print(message[:5])  # If you leave the first number blank, it will start from the beginning
print(message[6:])  # If you leave the second number blank, it will go to the end

print(message.count('l'))  # Counts the number of times the character appears in the string

print(message.replace('World', 'Universe'))  # Replaces the first argument with the second argument

print(f'{message} Welcome to Python!')  # f-strings are used to format strings
