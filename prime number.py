#For checking whether a number is prime number or not:
number = int(input("Enter the number to check if it's a prime number or not: "))

if number <= 1:
    print("Please enter a number greater than 1, since negative numbers, 0, and 1 are not prime numbers.")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")