field_prime = 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559787

try:
    foo = long
except:
    long = int

class FQ():
    def __init__(self, n):
        if isinstance(n, self.__class__):
            self.n = n
        else:
            self.n = n % field_prime
        assert isinstance(self.n, (int, long))

    def __add__(self, other):
        num = other.n if isinstance(other, FQ) else other
        return FQ((self.n + num) % field_prime)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        num = other.n if isinstance(other, FQ) else other
        return FQ((self.n - num) % field_prime)

    def __rsub__(self, other):
        num = other.n if isinstance(other, FQ) else other
        return FQ((num - self.n) % field_prime)

    def __mul__(self, other):
        num = other.n if isinstance(other, FQ) else other
        return FQ((num * self.n) % field_prime)

    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        num = other.n if isinstance(other, FQ) else other
        assert isinstance(num, (int, long))
        return FQ(self.n * inv(num, field_prime) % field_prime)

    def __rdiv__(self, other):
        num = other.n if isinstance(other, FQ) else other
        assert isinstance(num, (int, long))
        return FQ(inv(self.n, field_prime) * num % field_prime)

    def __truediv__(self, other):
        return self.__div__(other)

    def __rtruediv__(self, other):
        return self.__rdiv__(other)

    def __eq__(self, other):
        if isinstance(other, FQ):
            return self.n == other.n
        else:
            return self.n == other
    
    def __neq__(self, other):
        return not self == other

    def __neg__(self):
        return FQ(-self.n)

    def __repr__(self):
        return repr(self.n)

    def mul_nonres(self):
        return FQ(self.n)

class FQ2():
    def __init__(self, u0, u1):
        assert(isinstance(u0, FQ))
        assert(isinstance(u1, FQ))
        self.c0 = u0
        self.c1 = u1

    def __add__(self, other):
        assert(isinstance(other, FQ2))
        return FQ2(other.c0 + self.c0, other.c1 + self.c1)

    def __radd__(self, other):
        assert(isinstance(other, FQ2))
        return self + other

    def __sub__(self, other):
        assert(isinstance(other, FQ2))
        return FQ2(self.c0 - other.c0, self.c1 - other.c1)

    def __rsub__(self, other):
        assert(isinstance(other, FQ2))
        return FQ2(other.c0 - self.c0, other.c1 - self.c1)

    def __mul__(self, other):
        assert(isinstance(other, FQ2))
        return FQ2(self.c0 * other.c0 - self.c1 * other.c1, self.c1 * other.c0 + self.c0 * other.c1)
        
    def __rmul__(self, other):
        assert(isinstance(other, FQ2))
        return self * other

    def mul_nonres(self):
        return FQ2(self.c0 - self.c1, self.c0 + self.c1)

    def invFQ2(self):
        factor = inv(self.c1.n * self.c1.n + self.c0.n + self.c0.n, field_prime)
        return FQ2(self.c0 * factor, (-self.c1) * factor)

    def __eq__(self, other):
            assert(isinstance(other, FQ2))
            return self.c0 == other.c0 and self.c1 == other.c1
        
    def __neq__(self, other):
        assert(isinstance(other, FQ2))
        return not self == other

    def __neg__(self):
        return FQ2(-self.c0, -self.c1)

    def __repr__(self):
        return "(" + self.c0.__str__() + "," + self.c1.__str__() + ")"

class FQ6():
    def __init__(self, u0, u1, u2):
        assert(isinstance(u0, FQ2))
        assert(isinstance(u1, FQ2))
        assert(isinstance(u2, FQ2))
        self.c0 = u0
        self.c1 = u1
        self.c2 = u2

    def __add__(self):
        print("not impl yet!")


# Extended Euclidean Algorithm to find an inverse of a field element
def inv(a, n):
    if a == 0:
        return 0
    lm, hm = 1, 0
    low, high = a % n, n
    while low > 1:
        r = high//low
        nm, new = hm-lm*r, high-low*r
        lm, low, hm, high = nm, new, lm, low
    return lm % n

a = FQ(1)
b = FQ(1)

c = FQ2(a, b)
d = FQ2(a, b)

res = c.invFQ2()
print(c == d)
print(c != d)
print(c == -d)
print(res)
print(res.c0)
print(res.c1)

total = res.c0 + res.c1
print(total)

