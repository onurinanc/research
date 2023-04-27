from bls12_381_field_elements import FQ, FQ2

curve_order = 52435875175126190479447740508185965837690552500527637822603658699938581184513

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        if not Point.validate(self):
            raise Exception(f"Provided coordinates {self} don't form a point on that curve")

    def validate(self):
        return True

    def __neg__(self):
        return Point(self.x, -self.y)
        
    def __add__(self, other):
        # add edge case for self = other
        # add edge case for result = identity
        inv_temp = other.x - self.x
        slope = (other.y - self.y) * inv_temp.inv()
        x3 = slope * slope - self.x - other.x
        y3 = slope * (self.x - x3) - self.y
        return Point(x3, y3)

    def double(self):
        inv_temp = self.y + self.y
        slope = (self.x * self.x + self.x * self.x + self.x * self.x) * inv_temp.inv()
        x3 = slope * slope - self.x - self.x
        y3 = slope * (self.x - x3) - self.y
        return Point(x3, y3)

class PointG2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        if not PointG2.validate(self):
            raise Exception(f"Provided coordinates {self} don't form a point on that curve")

    def validate(self):
        return True

    def __neg__(self):
        return PointG2(self.x, -self.y)
        
    def __add__(self, other):
        # add edge case for self = other
        # add edge case for result = identity
        inv_temp = other.x - self.x
        slope = (other.y - self.y) * inv_temp.invFQ2()
        x3 = slope * slope - self.x - other.x
        y3 = slope * (self.x - x3) - self.y
        return PointG2(x3, y3)

    def double(self):
        inv_temp = self.y + self.y
        slope = (self.x * self.x + self.x * self.x + self.x * self.x) * inv_temp.inv()
        x3 = slope * slope - self.x - self.x
        y3 = slope * (self.x - x3) - self.y
        return PointG2(x3, y3)

G1_GENERATOR = Point(FQ(3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507), FQ(1339506544944476473020471379941921221584933875938349620426543736416511423956333506472724655353366534992391756441569))
G2_GENERATOR = Point(FQ2(FQ(352701069587466618187139116011060144890029952792775240219908644239793785735715026873347600343865175952761926303160), FQ(3059144344244213709971259814753781636986470325476647558659373206291635324768958432433509563104347017837885763365758)), FQ2(FQ(1985150602287291935568054521177171638300868978215655730859378665066344726373823718423869104263333984641494340347905), FQ(927553665492332455747201965776037880757740193453592970025027978793976877002675564980949289727957565575433344219582)))

a = G1_GENERATOR * G1_GENERATOR
print(a)

b = G1_GENERATOR.double()
print(b)
#print(b.x)
#print(b.y)
print(a.x)
print(a.y)
print(b.x)
print(b.y)
#assert(a == b)

c = G2_GENERATOR + G2_GENERATOR
d = G2_GENERATOR.double()

#print(c)
#print(d)

#print(c.x)

#assert(c == d)