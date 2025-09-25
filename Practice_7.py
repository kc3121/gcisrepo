'''Two functions implemented

 to find list of even and odd nos'''
def even(n):
    
    for i in range (0,n+1,2):
        print("Even = ", i, end '')
def odd(n):
    for j in range(1,n+1,2):
        print("Odd = ", j, end ='')

def main():
    n=int(input("Enter a no = "))
    A=even(n)
    B=odd(n)

main()
    
    