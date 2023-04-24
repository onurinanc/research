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
