"""Name: Kaavya Chandraprakash
   UID: 419003208"""

def triangle_validator(side_1,side_2,side_3): #Function header with parameters

    """This function checks whether a triangle can be formed from given 3 sides
    (If the sum of any two sides is greater than the 3rd side, then a triangle can be formed)"""

    if side_1+side_2>side_3 and side_1+side_3>side_2 and side_2+side_3>side_1: #Checks the conditions for a triangle to be formed
        return "True" #Uses return statement
    elif side_1+side_2>side_3 and side_1+side_3>side_2 and side_2+side_3>side_1:
        return "False"  #Uses return statement
    else:
        return "False"
    
def main():
    """This function inputs 3 sides from the user and calls the triangle_validator """
    #Asking the users to input the sides of a triangle
    side_1=int(input("Enter side 1 = "))
    side_2=int(input("Enter side 2 = "))
    side_3=int(input("Enter side 3 = "))
    Ans=triangle_validator(side_1,side_2,side_3) #Call function
    print(Ans)

main() # Calling main function