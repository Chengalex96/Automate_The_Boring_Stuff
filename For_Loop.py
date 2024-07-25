count = 100
sum = 0

for i in range(0, count + 1, 7):
    sum = sum + i
    if(i % 10 == 0):
        print('Count is at ' + str(i))
print(sum)

print(i)