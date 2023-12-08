def is_prime(i):
    j = i
    while j > 1:
        if ((i % j) == 0) and (i != j):    
            return False
        j -= 1    
    return True

def find_prime_numbers(number): # number = 5

    result = []                 # result = []

    for i in range(2, number+1): # range = [1, 2, 3, 4, 5]
        if is_prime(i):
            result.append(i)

    return result

result = find_prime_numbers(20)

print(result)
print(sum(result))

        



    

