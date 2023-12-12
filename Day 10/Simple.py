def is_prime(number):
    # Your code here
    for i in (2, number):
        if number % i != 0:
            return True
    return False

# Test the function
print(is_prime(7))   # Should print True
print(is_prime(12))  # Should print False
print(is_prime(19))  # Should print True



        

