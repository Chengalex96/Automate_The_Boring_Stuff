spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # Goes abck to the start of the loop
    print('spam is ' + str(spam))
