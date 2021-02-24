import math
def is_prime(n):
    divisor = 2
    while divisor < int(math.sqrt(n)):
        if n % divisor == 0:
            return False
        divisor += 1
    return True

def is_prime_for(n):
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

if __name__ == "__main__":
    print("Hello from Python!")
    n = int(input("Input a number: "))
    print(f"Number {n} is prime: {is_prime_for(n)}")
