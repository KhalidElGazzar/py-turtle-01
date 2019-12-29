"""
The rules
Before you start coding, let's make sure the basic idea of Fizz Buzz is clear. You count up through a series of numbers (0, 1, 2, 3, 4, 5 ... ) and for each number:

If the number is evenly divisible by 3, you say "Fizz"
If the number is evenly divisible by 5, you say "Buzz"
If the number is evenly divisible by both 3 and 5, you say "FizzBuzz"
"""


for i in range(20):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)