#a tuple is an immutable list.
#Defining a tuple
rgb = ('red', 'green', 'blue')

print(rgb[0])
print(rgb[1])
print(rgb[2])

#can assign a new tuple to a variable that references a tuple.
colors = ('red', 'green', 'blue')
print(colors)

colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)
#to sort list of tuples

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]


# define a sort key
def sort_key(company):
    return company[2]



# sort the companies by revenue
companies.sort(key=sort_key, reverse=True)

# show the sorted companies
print(companies)