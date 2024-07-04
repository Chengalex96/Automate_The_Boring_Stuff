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

