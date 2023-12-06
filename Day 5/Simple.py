def factorial(number):
    result = 1
    for i in range(1, (number+1)):
        result *= i # result = restult * i
    
    return result

number = int(input("enter your number: \t"))

result = factorial(number)

print("Factorial for given number: " + str(result))