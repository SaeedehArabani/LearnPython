#fibbonachi seq
# 0, 1, 1, 2, 3, 5, 8, ...

f1 = 1
f2 = 1
n = int(input("enter the number of fibonachi Seq\n"))

if(n == 1):
    print(f1)
    exit(0)

elif(n == 2):
    print(f1)
    print(f2)
    exit(0)

else:
    print(f1)
    print(f2)
    i = 3
    while(i <= n):
        f3 = f1 + f2
        print("{} \t".format(f3))
        f1 = f2
        f2 = f3
        i += 1