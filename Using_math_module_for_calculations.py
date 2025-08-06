import math

# Step 1: Get user input
value = float(input("\nEnter a number to perform math calculations: "))

# Step 2: Use math module functions
if value < 0:
    print("Square root and logarithm are not defined for negative numbers.")
else:
    square_root = math.sqrt(value)
    natural_log = math.log(value)  # log base e
    sine_value = math.sin(value)   # value in radians

    # Step 3: Display results
    print(f"\nResults using math module:")
    print(f"Square Root of {value}: {square_root}")
    print(f"Natural Logarithm of {value}: {natural_log}")
    print(f"Sine of {value} radians: {sine_value}")