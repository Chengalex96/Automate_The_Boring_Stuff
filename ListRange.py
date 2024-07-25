print(list(range(0,100,2)))

fruits = ['Apple', 'Banana', 'Pears', 'Pineapples']
for i in range(len(fruits)):
    print('Index ' + str(i) + ' in fruits is ' + fruits[i])

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
size, color, disposition = 'skinny', 'black', 'quiet'
a = 'AAA'
b = 'BBB'
a, b = b, a
spam = 42
spam += 1
print(spam)

print(cat[1:]+cat[:-1])

print(cat*2)

# Indexes start at 0, not 1
# Negative index to refer to last items
# Slice (:), goes up to but not including the last item
# len() works the same as lists with multiplication, and concatenation
# Can covert a value into a list using list()