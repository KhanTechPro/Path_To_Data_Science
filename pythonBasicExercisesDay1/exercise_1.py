## Exercise 1: Calculate the multiplication and sum of two numbers

print("Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = int(num1) * int(num2)

if sum <= 1000 :
    print(sum)
else:
    sum = int(num1) + int(num2)
    print(sum)