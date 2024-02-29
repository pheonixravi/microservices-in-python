price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

tax_amount = int(price) * int(tax) / 100    #type conversion
print(f'The tax amount is ${tax_amount}')