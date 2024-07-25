spam = ['cat', 'dog', 'cat']
print(spam.index('cat'))
spam.remove('cat')
print(spam)

# index, append to the end, insert(1, 'chicken), remove (first instance)
# Lists are modified in-place
# spam.sort() - ints or strings by alphabetical, can use reverse=True
# Cannot mix ints and strings
# Sorts with ASCII-betical order, pass key = str.lower