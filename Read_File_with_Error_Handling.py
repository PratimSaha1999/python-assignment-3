# Step 1: Try opening and reading the file
try:
    with open("sample.txt", "r") as file:
        print("Contents of 'sample.txt':")
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")