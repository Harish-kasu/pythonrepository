op = input(" enter an operator +,-,*,/):")
a = int(input("enter the first number:"))

b = int(input("enter the second number:"))

if op == "+":
    print(f"The sum is:", a + b)

elif op == "-":
    print("the difference is :", a-b)

elif op == "*":
    print("the product is:", a * b)

elif op == "/":
    print(" the quotient is :",a/b)

else :
    print(f" the operator {op} is not supported")
    
