
import os

# Get numbers from environment variables
num1 = float(os.getenv("NUM1", 0))
num3 = float(os.getenv("NUM2", 0))

# Add the numbers
sum_result = num1 + num3

# Print the result
print(f"The sum of {num1} and {num3} is {sum_result}")
