for i in range(1, 101):
    if i % 3 and i % 5 == 0:
        print("FIZZBUZZ")
    if i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print (i)

