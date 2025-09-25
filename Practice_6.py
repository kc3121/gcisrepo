'''This functions checks whether triangle
 can be formed from the given 3 sides'''

def triangle_validator(A,B,C):
    '''Given 3 sides and checks
      whether sum of any two sides is greater than the 3rd side'''
    if A+B>C and A+C>B and B+C>A: #Checks the condition for a triangle to form
        return "True" #Returns True if condition is met
    else:
        return "False" #Returns False if condition is not met
def main():
    '''This function inputs 3 sides of the triangle 
    and calls the triangle_validator function and stores the return value in a variable named Ans'''
    A=int(input("Enter side 1 = "))
    B=int(input("Enter side 2 = "))
    C=int(input("Enter side 3 = "))
    Ans=triangle_validator(A,B,C) #Calling triangle_validator function
    print(Ans)
main()