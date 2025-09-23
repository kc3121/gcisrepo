''' To implement functions to add, subtract, multiply and two numbers and act as calculator'''

def add(num1,num2):
    '''To add two numbers
    using + operator'''
    print("Addition =",num1+num2) #Using + operator
def subtract(num1,num2):
    '''To subtract two numbers
    using - operator'''
    print("Subtraction =", num1-num2) #Using - operator
def multiply(num1,num2):
    '''To multiply two numbers
    using * operator'''
    print("Multiplication =", num1*num2) #Using * operator
def divide(num1,num2):
    '''To divide two numbers
    using / operator'''
    print("Division =", num1/num2) #Using / operator

def main():
    num1=int(input("Enter num 1 ="))
    num2=int(input("Enter num 2 ="))
    add(num1,num2)
    subtract(num1,num2)
    multiply(num1,num2)
    divide(num1,num2)
main()
    