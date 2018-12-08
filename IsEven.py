class IsEven:
    """return True if 'n' is a prime number, False otherwise"""
    import time
    import math

    def isprimev1(self,n):
        """version:1,return True if 'n' is a prime number, False otherwise"""
        if n == 1:
            return False
        for d in range(2, n):
            if n % d == 0:
                return False
        return True

    def isprimev2(self,n):
        """version:2,return True if 'n' is a prime number, False otherwise"""
        if n == 1:
            return False
        import math
        max_divisor = math.floor(math.sqrt(n))
        for d in range(2, 1+max_divisor):
            if n % d == 0:
                return False
        return True

    def isprimev3(self,n):
        """version:3,return True if 'n' is a prime number, False otherwise"""
        if n == 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        import math
        max_divisor = math.floor(math.sqrt(n))
        for d in range(3, 1+max_divisor, 2):
            if n % d == 0:
                return False
        return True

"""============time function====================="""
e=IsEven()
import time
t0 = time.time()
for n in range(1, 10000):
    e.isprimev1(n)
t1 = time.time()
print("time required for v1:", t1-t0)

t2 = time.time()
for n in range(1, 10000):
    e.isprimev2(n)
t3 = time.time()
print("time required for v2:", t3-t2)
t4 = time.time()
for n in range(1, 10000):
    e.isprimev3(n)
t5 = time.time()
print("time required for v3:", t5-t4)