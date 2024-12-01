#Print all prime number between 1 and 50.
# Loop through numbers from 2 to 50
for num in range(2, 51):
    is_prime = True 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False  
            break
    if is_prime:
        print(num)
