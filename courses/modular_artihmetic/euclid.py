

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def gcd_manual(a, b):
    """Compute the greatest common divisor of a and b using manual steps."""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find integers x and y such that ax + by = gcd(a, b)."""
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

a = 66528
b = 52920

gcd_val = gcd_manual(a, b)
gcd_extended, x, y = extended_gcd(a, b)

print(f"GCD of {a} and {b} is: {gcd_val}")
# print(f"Extended GCD: {gcd_extended}, x: {x}, y: {y}")
# print(f"Verification: {a} * {x} + {b} * {y} = {gcd_extended}")





