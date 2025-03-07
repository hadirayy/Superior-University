def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def dynamic_calculator():
    print("Welcome to the Dynamic Calculator!")
    print("Available operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exponentiate (^)")
    print("6. Modulus (%)")
    
    while True:
        operation = input("\nEnter operation (+, -, *, /, ^, %, or 'exit' to quit): ").strip()
        
        if operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if operation in ('+', '-', '*', '/', '^', '%'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if operation == '+':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif operation == '-':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif operation == '*':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif operation == '/':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif operation == '^':
                    print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
                elif operation == '%':
                    print(f"{num1} % {num2} = {modulus(num1, num2)}")
                
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    dynamic_calculator()
