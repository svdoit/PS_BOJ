N, X = map(int, input().split())
numArr = list(map(int, input().split()))

for i in range(N):   
    if numArr[i] < X :
        print(numArr[i], end=" ")

