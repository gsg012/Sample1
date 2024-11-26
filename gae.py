# Addition of 10 numbers

total = 0

print("Enter 10 numbers:")

for i in range(1, 11):
    number = float(input(f"Enter number {i}: "))
    total += number

print(f"The sum of the 10 numbers is: {total}")

---------------------------------------------------------------------------

# Factorial of given number
num = int(input("Enter a number to find its factorial: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}.")

---------------------------------------------------------------------------

# Average of 5 numbers
total = 0

print("Enter 5 numbers:")

for i in range(1, 6):
    number = float(input(f"Enter number {i}: "))
    total += number

average = total / 5

print(f"The average of the 5 numbers is: {average}")

---------------------------------------------------------------------------


# Maximum of 10 numbers
numbers = []
print("Enter 10 numbers:")

for i in range(1, 11):
    number = float(input(f"Enter number {i}: "))
    numbers.append(number)

maximum = max(numbers)

print(f"The maximum of the 10 numbers is: {maximum}")

