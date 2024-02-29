def is_PrimeNumber(number):
    if number<=1:
        return False
    for i in range(2,(number/2)+1):
        if number%i == 0:
            return False
    return True
    

number=17
print(number,"is a prime number",is_PrimeNumber(number))
