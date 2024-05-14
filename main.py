n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
oper = input("Enter operation: ")
if oper == "+":
    print(n1+n2)
elif oper == "-":
    print(n1-n2)
elif oper == "*":
    print(n1*n2)
elif oper == "/":
    print(n1/n2)
else:
    print("Invalid operation")
