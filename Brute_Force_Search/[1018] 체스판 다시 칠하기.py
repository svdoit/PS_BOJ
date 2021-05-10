N, M = map(int, input().split())
test = []
for _ in range(N):
    test.append(input())

min_list = []

for i in range(N-7):
    for j in range(M-7):
        cnt_w = cnt_b = 0
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if test[a][b] != 'W': cnt_w += 1
                    if test[a][b] != 'B': cnt_b += 1
                else:
                    if test[a][b] != 'B': cnt_w += 1
                    if test[a][b] != 'W': cnt_b += 1
        
        min_list.append(cnt_w)
        min_list.append(cnt_b)        

print(min(min_list))
