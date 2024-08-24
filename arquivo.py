import pandas as pd


countries = pd.read_csv('countries.csv')
print(countries.head())

print(countries['Country (en)'][0])

if countries['Country (en)'][1] == 'Russia':
    print('The second country is Russia')
elif countries['Country (en)'][1] == 'Canada':
    print('The second country is Canada')
elif countries['Country (en)'][1] == 'USA':
    print('The second country is USA')
else:
    print('The country is not on the list')


op = countries['Country (en)'][2]

match op:

    case 'Brazil':
        print('The second country is Brazil')
    case 'Portugal':
        print('The second country is Portugal')
    case 'Morocco':
        print('The second country is Morocco')
    case 'Italy':
        print('The second country is Italy')
    case 'Germany':
        print('The second country is Germany')
    case 'Argentina':
        print('The second country is Argentina')
    case _:
        print('O país não está na lista destacada.')


 

