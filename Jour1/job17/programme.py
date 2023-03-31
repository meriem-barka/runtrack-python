
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FrizzBuzz")
    elif i % 3 == 0:
        print("Frizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)