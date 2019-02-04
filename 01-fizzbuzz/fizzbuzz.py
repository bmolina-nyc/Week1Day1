
def fizzbuzz(n):
    for el in range(0, n):
        if el % 3 == 0 and el % 5 == 0:
            print("FizzBuzz")
        elif el % 3 == 0 and el % 5 != 0:
            print("Fizz")
        elif el % 3 != 0 and el % 5 == 0:
            print("Buzz")
        else:
            print(el)
        

print(fizzbuzz(20))