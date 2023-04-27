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
        return FQ(self.n * num.inv())

    def __rdiv__(self, other):
        num = other.n if isinstance(other, FQ) else other
        assert isinstance(num, (int, long))
        return FQ(self.inv() * num % field_prime)

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

    def inv(self):
        if self.n == 0:
            return 0
        lm, hm = 1, 0
        low, high = self.n % field_prime, field_prime
        while low > 1:
            r = high//low
            nm, new = hm-lm*r, high-low*r
            lm, low, hm, high = nm, new, lm, low
        return lm % field_prime

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

    def inv(self):
        inverse_temp = self.c1 * self.c1 + self.c0 + self.c0
        factor = inverse_temp.inv()
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

    def __add__(self, other):
        assert(isinstance(other, FQ6))
        return FQ6(self.c0 + other.c0, self.c1 + other.c1, self.c2 + other.c2)

    def __radd__(self, other):
        assert(isinstance(other, FQ6))
        return self + other

    def __sub__(self, other):
        assert(isinstance(other, FQ6))
        return FQ6(self.c0 - other.c0, self.c1 - other.c1, self.c2 - other.c2)
    
    def __rsub__(self, other):
        assert(isinstance(other, FQ6))
        return FQ6(other.c0 - self.c0, other.c1 - self.c1, other.c2 - self.c2)

    def __mul__(self, other):
        assert(isinstance(other, FQ6))
        t0 = self.c0 * other.c0
        t1 = self.c0 * other.c1 + self.c1 * other.c0
        t2 = self.c0 * other.c2 + self.c1 * other.c1 + self.c2 * other.c0
        t3 = self.c1 * other.c2 + self.c2 * other.c1
        t3 = t3.mul_nonres()
        t4 = self.c2 * other.c2
        t4 = t4.mul_nonres()
        return FQ6(t0 + t3, t1 + t4, t2)

    def __rmul__(self, other):
        assert(isinstance(other, FQ6))
        return self * other

    def mul_nonres(self):
        return FQ6(self.c2.mul_nonres(), self.c0, self.c1)

    def inv(self):
        mul_nonres1 = self.c1 * self.c2
        mul_nonres2 = self.c2 * self.c2
        t0 = self.c0 * self.c1 - mul_nonres1.mul_nonres()
        t1 = mul_nonres2.mul_nonres() - self.c0 * self.c1
        t2 = self.c1 * self.c1 - self.c0 * self.c2
        mul_nonres3 = self.c2 * t1
        mul_nonres4 = self.c1 * t2
        inverse_temp = self.c0 * t0 + mul_nonres3 + mul_nonres4
        factor = inverse_temp.inv()
        return FQ6(t0 * factor, t1 * factor, t2 * factor)

    def __eq__(self, other):
            assert(isinstance(other, FQ6))
            return self.c0 == other.c0 and self.c1 == other.c1 and self.c2 == self.c2
        
    def __neq__(self, other):
        assert(isinstance(other, FQ6))
        return not self == other

    def __neg__(self):
        return FQ6(-self.c0, -self.c1, -self.c2)

    def __repr__(self):
        return "(" + self.c0.__str__() + "," + self.c1.__str__() + "," + self.c2.__str__() + ")"

class FQ12():
    def __init__(self, u0, u1):
        assert(isinstance(u0, FQ6))
        assert(isinstance(u1, FQ6))
        self.c0 = u0
        self.c1 = u1
    
    def __add__(self, other):
        assert(isinstance(other, FQ12))
        return FQ12(self.c0 + other.c0, self.c1 + other.c1)

    def __radd__(self, other):
        assert(isinstance(other, FQ12))
        return self + other

    def __sub__(self, other):
        assert(isinstance(other, FQ12))
        return FQ12(self.c0 - other.c0, self.c1 - other.c1)

    def __rsub__(self, other):
        assert(isinstance(other, FQ12))
        return FQ12(other.c0 - self.c0, other.c1 - self.c1)

    def __mul__(self, other):
        assert(isinstance(other, FQ12))
        mul_nonres1 = self.c1 * other.c1
        return FQ12(self.c0 * other.c0 + mul_nonres1.mul_nonres(), self.c1 * other.c0 + self.c0 * other.c1)

    def __rmul__(self, other):
        assert(isinstance(other, FQ12))
        return self * other


    def mul_nonres(self):
        print("No need for FQ12!")

    def inv(self):
        mul_nonres1 = self.c1 * self.c1
        inverse_temp = self.c0 * self.c0 - mul_nonres1.mul_nonres()
        factor = inverse_temp.inv()
        return FQ12(self.c0 * factor, -self.c1 * factor)

    def __eq__(self, other):
            assert(isinstance(other, FQ12))
            return self.c0 == other.c0 and self.c1 == other.c1
        
    def __neq__(self, other):
        assert(isinstance(other, FQ12))
        return not self == other

    def __neg__(self):
        return FQ12(-self.c0, -self.c1)

    def __repr__(self):
        return "(" + self.c0.__str__() + "," + self.c1.__str__() + ")"


a = FQ(1)
b = FQ(1)
c = FQ(3)
d = FQ(4)
e = FQ(2)
f = FQ(8)

u = FQ2(a, b)
v = FQ2(c, d)
t = FQ2(e, f)

x = FQ6(u, v, t)
y = FQ6(t, v, u)

res = x * y
res1 = y * x
print(res)
print(res.c0)
print(res.c1)
print(res.c2)
print(res1)
print(res1.c0)
print(res1.c1)
print(res1.c2)

res2 = x + y
print(res2)

res3 = x - y
print(res3)

res4 = x.inv()
print(res4)

res5 = y.mul_nonres()
print(res5)
print("#################")

zz = FQ12(x, y)
zy = FQ12(x, -y)

result = zz * zy
print(result)

result1 = zz + zy
print(result1)

result2 = zz - zy
print(result2)

result3 = zz.inv()
print(result3)
