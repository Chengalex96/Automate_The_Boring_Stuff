def div42by(divideBy):
    try:
      return 42 / divideBy
    except ZeroDivisionError:
       print("Divide by 0")

# use to avoid divide by 0's error

print(div42by(2))
print(div42by(42))
print(div42by(0))