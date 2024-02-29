numbers = [1, 3, 2, 7, 9, 4]
print(numbers)
numbers.append(100)
print(numbers)
#list containing another list
coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)

#insert() method adds a new element at any position in the list.
numbers.insert(2, 101)
print(numbers)
#del statement allows you to remove an element from a list by specifying the position of the element.
del numbers[0]

last = numbers.pop()#removes the last element and returns the new list.

print(last)

#iteration for list
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)

#indexing
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'Osaka'

if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")