def Addition(a , b):
    print(f"sum of {a} and {b} is: {a+b}")


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
        break
    print("enter number:")
    a= int(input("enter first value:"))
    b= int(input("enter second value:"))

    if(ch==1):
        Addition(a , b)

    
    else:
        print("Invalid input")

       