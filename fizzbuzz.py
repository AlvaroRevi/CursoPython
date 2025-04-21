# FizzBuzz Game Solver

# Loop through numbers from 1 to 100 (inclusive)
for number in range(1, 101):
    # Check if divisible by both 3 and 5
    # This check needs to come first because numbers divisible by both
    # are also divisible by 3 and 5 individually.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Check if divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # Check if divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # If none of the above, print the number itself
    else:
        print(number) 