import math
# Function to check
# Log base 2
def Log2(x):
    return (math.log10(x) / math.log10(2))

# Function to check
# if x is power of 2
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

print(isPowerOfTwo(int(input())))
