spam = 42

def breakfast():
    spam = 'eggs'
    print('Spam in local is ' + spam)
# if no assignment in function, it is global
# or define globnal variable (global spam)

breakfast()
print('Spam in global is ' + str(spam))