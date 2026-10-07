# Modular Calculator Mini-Program

 # Uses separate functions for each arithmetic operation
 # ---- FUNCTION DEFINITIONS ----
 
def add_numbers(num1, num2):
    # Take two numbers and return their sum
     total = num1 + num2
     return total
     
def subtract_numbers(num1, num2):
     # Take two numbers and return their difference
     difference = num1 - num2
     return difference
     
def multiply_numbers(num1, num2):
     # Take two numbers and return their product
     product = num1 * num2
     return product
     
def divide_numbers(num1, num2):
     # Check for division by zero before calculating
     if num2 == 0:
         return "Cannot divide by zero."
     quotient = num1 / num2
     return quotient
     
     
print("=== Modular Calculator ===")
 # Get input from user
 
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
 # Show operation menu
 
print("\nChoose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
choice = input("\nEnter choice: ")
 
 # Call matching function and store result
 
if choice == "1":
     result = add_numbers(first_num, second_num)
elif choice == "2":
     result = subtract_numbers(first_num, second_num)
elif choice == "3":
     result = multiply_numbers(first_num, second_num)
elif choice == "4":
     result = divide_numbers(first_num, second_num)
else:
     result = "Invalid choice. Please run the program again."
     
 # Display final output
print(f"\nResult: {result}")