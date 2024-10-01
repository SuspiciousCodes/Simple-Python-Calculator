# Simple Python Calculator
# Author: @SuspiciousCodes on Github.
# Date: 01/10/2024
# Version : v1.0.0

operator = input("Enter an operator (+ - * /): ")
print(" ")

num1 =  float(input("Enter the 1st number: "))

num2 =  float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(" ")
    print (f"Your answer is: {round(result, 2)}") 
    
elif operator == "-":
    result = num1 - num2
    print(" ")
    print (f"Your answer is: {round(result, 2)}")    
    
elif operator == "*":
    result = num1 * num2
    print(" ")
    print (f"Your answer is: {round(result, 2)}")    
    
elif operator == "/":
    result = num1 / num2
    print(" ")
    print (f"Your answer is: {round(result, 2)}")
        
else:
    print(f"'{operator}' is not a valid operator!")

    
