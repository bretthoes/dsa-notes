"""
Fundamental operations:
"""
# AND
# both bits have to be 1 for the result to be 1 (else 0)
n = 1 & 1

# OR
# if either is 1, the result is 1
n = 1 | 0

# XOR
# if exactly one is 1, the result is 1
n = 0 ^ 1

# NOT (negation)
n = ~n

# Bit Shifting
# (left)
# when we shift left by one, we multiple by 2
# 001 << 1 -> 010
# 010 << 1 -> 100
# 100 << 1 -> 000
# (right)
# when we shift right by one, we divide by 2
# but when we shift right, we round down if we have an odd number
# 100 >> 1 -> 010
# 010 >> 1 -> 001
# 001 >> 1 -> 000
n = 1 
n = n << 1
n = n >> 1

# sample problem
# Counting Bits:
def countBits(n):
    count = 0
    while n > 0:
        count += 1
        n = n >> 1 # same as n // 2
    return count

# 23 = 10111
print(countBits(23))

# check even/odd
def is_odd(x: int) -> bool:
    return bool(x & 1)

# Swap two integers without a temporary variable
# Uses XOR’s reversibility:
a = 12
b = 4
a = a ^ b
b = a ^ b
a = a ^ b


def is_power_of_two(x: int) -> bool:
    return x > 0 and (x & (x - 1)) == 0
