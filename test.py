"""class Test:
    a = []
    def Set_a(self, x, y, z):
        self.a.append(x)
        self.a.append(y)
        self.a.append(z)

variables = [1, 2, 3]
a = Test()
eval("a.Set_a(variables[0], variables[1], variables[2])")
print(a.a)"""
def Test(a):
    print(a)

b = 1
eval("Test(b)")
