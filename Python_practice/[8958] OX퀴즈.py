N = int(input())

for i in range(N):
    OX_case = list(input())
    
    count = 0
    score = 0
    
    for j in OX_case:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)

            
