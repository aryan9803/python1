
import os

# Get numbers from environment variables
num1 = float(os.getenv("NUM1", 0))
num2 = float(os.getenv("NUM2", 0))

# Add the numbers
sum_result = num1 + num2

# Print the result
print(f"The sum of {num1} and {num2} is {sum_result}")
