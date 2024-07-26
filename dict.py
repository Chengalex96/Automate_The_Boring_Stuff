myCat = {'size': 'fat', 'color': 'gray', 'noise': 'loud'}

# Key value pairs and mutable

print(myCat['size'])

# Dictionaries use curly brackets, the order does not matter

print(myCat.keys())
print(myCat.values())
print(myCat.items()) # Both values

for k, v in myCat.items():
    print(k, v)

print(myCat.get('size', 0)) # returns default if it doesn't exist

print(myCat.setdefault('star', 'Xt'))

# import pprint: to make it looks nicer when printing