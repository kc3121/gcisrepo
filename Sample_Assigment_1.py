'''Functions implemented to check whether a number is even or odd
and find it's  square and cube'''

def even(Num1):
    if Num1%2==0:
        print(Num1, " is Even number")
        '''To check even Number 
        If the number is divisible by 2, the it's an even number'''
    else:
        print(Num1, "is not an even number")

def odd(Num1):
    if Num1%2!=0: #If number not divisible by 2, then it's an odd number
        print(Num1, " is an odd number")
    else:
        print(Num1, "is not an Odd number")

def square(Num1):
    print("Square =", Num1**2) #To find the square

def cube(Num1):
    print("Cube = ", Num1**3) #To find the cube
    
def main():
    Num1=int(input("Enter a no = "))
    even(Num1)
    odd(Num1)
    square(Num1)
    cube(Num1)
main() #Call the main function
