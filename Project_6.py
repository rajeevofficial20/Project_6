

print("basic calculator")
a = float(input("enter your first number : "))
operator = input("enter the operator (+, -, *, /,**,//,%) : ")
b = float(input("enter your second number : "))

if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    if b == 0:      
        print("Division by zero is not allowed")
elif operator == '**':
    print(a ** b) 
elif operator == '//':
    if b == 0:
        print("Division by zero is not allowed") 
    else:
        print(a // b)        
elif operator == '%':
    if b == 0:
        print("Division by zero is not allowed")                
    else:
        print(a % b)
else:
    print("Please enter a valid operator")
