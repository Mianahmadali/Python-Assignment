#How would you use an if statement to determine the maximum value from three variables without using the max() function?
var1 = 4
var2 = 9
var3 = 7
if var1 > var2 and var1 > var3:
    print("Variable 1 vas  maximum value")
elif var2 > var3 and var2 > var1 :
    print("Variable 2 has maximum value")
else:
    print("variable 3 has maximum value")



# Initialize the variables
var1 = 4
var2 = 9
var3 = 7

# Assume var1 is the maximum initially
if var1 >= var2 and var1 >= var3:
    max_value = var1
elif var2 >= var1 and var2 >= var3:
    max_value = var2
else:
    max_value = var3

# Output the maximum value
print("The maximum value is:", max_value)