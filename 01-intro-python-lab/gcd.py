
def gcd(a: int, b: int ) -> int:
    if b == 0: # recursion bottom
        return a
    return gcd(b, a % b) # recursion step

if __name__ == "__main__":
    a = int(input("A = "))
    b = int(input("B = "))
    print(gcd(a, b))