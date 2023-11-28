x=int(input("Enter number "))
y=int(input("Enter number "))
operate= (x+y,x-y,x*y,x/y)
print(operate)



First_number= float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
Second_number = float(input("Enter the second number: "))

displayResult=(First_number, operator,Second_number) 
    
result = None

if operator == '+':
        result = First_number + Second_number
elif operator == '-':
        result = First_number - Second_number
elif operator == '*':
        result = First_number * Second_number
elif operator == '/':
    if  Second_number != 0:
            result = First_number / Second_number
    else:
        print("Error: Division by zero is not allowed.")
        
print(f"{First_number} {operator} {Second_number} = {result}")

main=()
   
print("Calculator Program")


First_number, operator,  = ()

   
displayResult(First_number, operator, Second_number)

if _name_ == "_main_":
  main()
