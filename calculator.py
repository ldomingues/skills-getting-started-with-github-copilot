#function to add two numbers
def add(a, b):
    return a + b
#function to subtract two numbers
def subtract(a, b):
    return a - b
#function to multiply two numbers
def multiply(a, b):
    return a * b
#function to divide two numbers
def divide(a, b):   
    if b == 0:
        return "Error! Division by zero."
    return a / b
#run the function to add two numbers
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))