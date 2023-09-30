import math
a = input("what you want to perform\n"
          "for addition -> +\n"
          "for subtraction -> - \n"
          "for multiplication -> * \n"
          "for division -> /\n"
          "for square root -> sqrt \n"
          "for power ->pow \n"
          "enter below \n")
if a == "+":
    ad = int(input("how many digit you want to add : "))
    summ = []
    for i in range(ad):
        summ.append(float(input("enter the number : ")))
        d = sum(summ)
    print("the sum is", d)
elif a == "-":
    a1 = float(input("enter first no : "))
    a2 = float(input("enter first no : "))
    print("the difference is ", a1-a2)
elif a == "*":
    a1 = float(input("enter first no : "))
    a2 = float(input("enter first no : "))
    print("the product is ", a1*a2)
elif a == "/":
    a1 = float(input("enter first no : "))
    a2 = float(input("enter first no : "))
    if a2 == 0:
        print("not defined")
    else:
        print("the division is ", a1/a2)
elif a == "pow":
    a1 = float(input("enter number : "))
    a2 = float(input("enter power : "))
    print("result is", math.pow(a1, a2))

elif a == "sqrt":
    a1 = float(input("enter no whose square root you wanna calculate"))
    print(math.sqrt(a1))
else:
    print("Invalid symbol")
