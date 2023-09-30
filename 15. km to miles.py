a=input("what you want to change M for miles and KM for kilo meters \n"
        "PLEASE NOTE CAPS LOCK SHOULD BE ON ->")
if a== "M":
    v = int(input("Enter the value in Miles :"))
    print(v,"MILES in kilometer is ", v * 1.6 ,"KM")
elif a== "KM":
    v = int(input("Enter the value in KILOMETER :"))
    print(v,"KM in miles is ", v * 0.6,"MILES")
else:
    print("ENTER M OR KM ")

