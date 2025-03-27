def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Welcome to the Factorial Calculation Program!")

while True:
    user_input = input("Enter a positive integer to calculate its factorial, or 'exit' to quit: ").strip()
    
    if user_input.lower() == 'exit':
        print("Thank you for using the Factorial Calculation Program! Goodbye.")
        break
    
    try:
        num = int(user_input)
        if num < 0:
            print("Factorial is not defined for negative numbers. Please enter a positive integer.")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer or type 'exit' to quit.")
