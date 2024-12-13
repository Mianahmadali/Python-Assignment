#Print the sum of even and odd numbers separately up to a given number.
def sum_even_odd_numbers(n):
    sum_even = 0
    sum_odd = 0
    
    for i in range(1, n + 1):
        if i % 2 == 0:  # Even number
            sum_even += i
        else:  # Odd number
            sum_odd += i
    
    return sum_even, sum_odd

# Input: A number 'n'
n = int(input("Enter a number: "))
even_sum, odd_sum = sum_even_odd_numbers(n)

print(f"Sum of even numbers up to {n}: {even_sum}")
print(f"Sum of odd numbers up to {n}: {odd_sum}")
