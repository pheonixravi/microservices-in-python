s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)
#To span a string multiple lines, you use triple-quotes “””…””” or ”’…”’. 
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

print(help_message)

#formatting string
name = 'John'
message = f'Hi {name}'
print(message)

greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)
#Accessing string elements
str = "Python String"
print(str[0]) 
print(str[1])

#Slicing strings(Slicing allows you to get a substring from a string.)
str = "Python String"
print(str[0:2])#returns a substring that includes the character from the index 0 (included) to 2 (excluded)

#Python strings are immutable.
str = "Python String"
str[0] = 'Java String'