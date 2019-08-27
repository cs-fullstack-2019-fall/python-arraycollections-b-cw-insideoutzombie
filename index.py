### Problem 1:
# Create a function with the variable below. After you create the variable do the instructions below that.
# ```
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# ```
# a) Print the 3rd element of the numberList.
#
# b) Print the size of the array
#
# c) Delete the second element.
#
# d) Print the 3rd element.
def problem1():
    anotherVar()

def anotherVar():
    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem2[2])
    print(len(arrayForProblem2))
    arrayForProblem2.pop()
    print(arrayForProblem2)
    print(arrayForProblem2[2])

### Problem 2:
##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = ""
    while(userInput != 'q'):
        userInput = input("Try again ")

### Problem 4:
# Create an array of 5 numbers.Using a loop, print the elements
#  in the array reverse order.Do not use a function
for i in range(6,1):
    print(i, end=', ')




### Problem 5:
# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def problem5():
    hardCode()

def hardCode():
    arrayForProblem5 = []
    userInput1 = int(input("Number here "))

# def problem3():
#     variableBelow()
#
# def variableBelow():
#     listNames = ["John", "Paul", "George", "Pete"]
#     print(listNames[3])
#     listNames[3]="Ringo"
#     print(listNames)
#     listNames.append("Yoko")
#     print(listNames)

def main():
    # problem1()
    # problem2()
    problem5()

main()
