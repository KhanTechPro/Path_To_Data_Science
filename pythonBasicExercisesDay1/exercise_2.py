## Exercise 2: Print the Sum of a Current Number and a Previous number

previousNumber = 0

for i in range(1, 11) :
    x_sum = previousNumber + i
    print("Current number", i, "Previous number", previousNumber, "Sum: ", x_sum)

    previousNumber = i

