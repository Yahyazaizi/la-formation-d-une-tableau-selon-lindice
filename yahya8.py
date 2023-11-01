#def a (non,salaire=3000):
  #  print("le non de salarir",non,"et le salier",salaire,"dh")
#m=int(input("le nomber se salarier" ))
#for i in range(m+1)  :
  #  n=input("svp done le non de salarir:")
  #  b=int(input("svp done le salaire de chake salarer:"))
 # print(a(n,b))

def st(t,a,b):
    t1=[]
    for i in range(len(t)):
        if  ( i>=a and i<b ):
            t1.append(t[i])
    return t1
t=[]
a=int(input("a:"))
b=int(input("b:"))
n=int(input("le nomber"))
for i in range (0,10):
    v=int(input("10 entier:"))
    t.append(v)
    if n<a and n>b:
        print("erour")
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
        n = int(input("le nomber"))
        for i in range(0, 10):
            f = int(input("10 entier:"))
            t.append(f)

            print(st(t, a, b))

    elif choix=="2":
         print("stop")
    break















