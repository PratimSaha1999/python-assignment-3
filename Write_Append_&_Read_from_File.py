# Step 1: Take input from user to write to the file
user_input = input("\nEnter some text to write into 'output.txt': ")

# Step 2: Write to output.txt
with open("output.txt", "w") as f:
    f.write(user_input + "\n")

# Step 3: Append additional data to the same file
additional_data = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(additional_data + "\n")

# Step 4: Read and display the final content of the file
print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())