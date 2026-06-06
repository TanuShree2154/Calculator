def Addition(a , b):
    print(f"sum of {a} and {b} is: {a+b}")
def division(a,b):
    if (a==0 or b==0):
       print("Division by zero is not possible")
    else:
        print(f"Divison of {a} by {b} is:{a/b}")
      
    

def Subtraction(a, b):
    print(f"Difference of {a} and {b} is: {a-b}")

def Multiplication(a,b):
    print(f"Product of {a} and {b} is: {a*b}")

print("""choose option to perfrom operation:
      1. addition 
      2. substraction 
      3. multiply 
      4. division 
      5. power
      6. modulo 
      7. floor division
      8. exit
      """)

while(True):
    
    ch = int(input("enter your choice:"))
    if(ch==8):
        print("Exit.")
        break
    print("enter number:")
    a= int(input("enter first value:"))
    b= int(input("enter second value:"))

    if(ch==1):
        Addition(a , b)
    elif(ch==4):
        division(a,b)
        
    
    elif(ch==2):
     Subtraction(a, b)

    elif(ch==3):
        Multiplication(a,b)    

    
    else:
     print("Invalid input")





       