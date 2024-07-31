#Raise your own exceptions

# raise Exception('This is the error message')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be 1 character')
    
    if (width < 2) or (height <2):
        raise Exception(' Width and Height must be greater than 2')


    print(symbol * width)

    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol*width)

boxPrint( '*', 15, 15)
boxPrint( 'X', 5, 15)

import traceback

try:
    raise Exception('Err message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info as written in error_log.txt')

# Traffic light
market2 = {'ns': 'green', 'ew': 'red'}

def switchLights(interesection):
    for key in interesection.keys():
        if interesection[key] == 'green':
            interesection[key] = 'yellow'
        elif interesection[key] == 'yellow':
            interesection[key] = 'red'
        elif interesection[key] == 'red':
            interesection[key] = 'green'
    assert 'red' in interesection.values(), 'Neither Light is red!' + str(interesection)

    # Assertion are for programmer errors

print(market2)
switchLights(market2)    
print(market2)


