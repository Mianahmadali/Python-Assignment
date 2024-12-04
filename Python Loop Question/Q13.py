#Use nested loops to print a pyramid pattern of *.any
# Number of rows for the pyramid
rows = 10

# Outer loop for each row
for i in range(rows):
    # Print spaces for the left side of the pyramid
    for j in range(rows - i - 1):
        print(" ", end="")  # Print space without a newline

    # Print asterisks for the pyramid
    for k in range(2 * i + 1):
        print("*", end="")  # Print asterisk without a newline

    # Move to the next line after each row
    print()