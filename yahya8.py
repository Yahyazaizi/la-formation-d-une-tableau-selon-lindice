def st(t,a,b):

    return t[a:b]

t=[]
a = int(input("a:"))
b = int(input("b:"))
while  a > b or a > 10 or b > 10 or b < 0:
       print("svp done la valeure de a et b")
       a=int(input("a:"))
       b=int(input("b:"))





for i in range (0,10):
    v=int(input("10 entier:"))
    t.append(v)

print(st(t,a,b))
while True:
    print("menu")
    print("1.novel liste")
    print("2.stop")
    choix=input("selection une option")
    if choix=="1":
        t = []
        a = int(input("a:"))
        b = int(input("b:"))
        while a > b or a > 10 or b > 10 or b < 0:
            print("svp done la valeure de a et b")
            a = int(input("a:"))
            b = int(input("b:"))
        for i in range(0, 10):
            f = int(input("10 entier:"))
            t.append(f)

        print(st(t, a, b))

    elif choix=="2":
         print("stop")
    break
