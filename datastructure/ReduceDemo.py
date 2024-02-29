from functools import reduce

#to calculate the sum of all the elements in the list.
scores = [75, 65, 80, 95, 50]

total = 0

for score in scores:
    total += score

print(total)

#using reduce() function.
def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)