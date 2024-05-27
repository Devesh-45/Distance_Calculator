print("\tDISTANCE CALCULATOR")
while True:
    x1,y1=list(map(int,input("\nEnter point 1's co-ordinates: ").split(",")))
    x2,y2=list(map(int,input("Enter point 2's co-ordinates: ").split(",")))
    Dist=(((x2-x1)**2)+((y2-y1)**2))**0.5
    print("\nDistance between 2 points=",round(Dist,3))
    print("                          ======")
    a=input("\nDo you want to continue or exit? (yes/no)")
    if a =="no":
        break