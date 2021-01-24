T = int(input())

for i in range(T):
    R, S = input().split()

    for j in range(len(S)):
        print(S[j]*int(R), end='') #end='' 옆으로 붙임
    print() #줄넘김
