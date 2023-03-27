def Perimeter(a,b):
    return 2 * (a + b)

def Area(a,b):
    return (a * b)

a = int(input("\n"))
b = int(input("\n"))

ar = Area(a,b)
per = Perimeter(a,b)

print(ar)
print(per)