## Exercise 5: Check if the first and last numbers of a list are the same

def first_last_same(numberList):
    print("Given list:", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 10]
print("The result is: ", first_last_same(numbers_x))
