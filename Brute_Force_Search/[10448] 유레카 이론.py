T = [n*(n+1)//2 for n in range(1, 45)]
eur = [0]*1001

K = int(input())
Klist = []
for _ in range(K) :
    Klist.append(int(input()))

for t1 in T :
    for t2 in T :
        for t3 in T :
            if (t1 + t2 + t3) <= 1000 :
                eur[t1 + t2 + t3] = 1

for _ in range(K) :
    print(eur[Klist[_]])
                

