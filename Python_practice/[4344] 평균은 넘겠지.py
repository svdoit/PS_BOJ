C = int(input())

for i in range(C):
    case = list(map(int, input().split(" ")))
    avg = sum(case[1:])/case[0]
    
    count = 0
    
    for score in case[1:]:
        if score > avg:
            count += 1
    print("%.3f%%" %round((count / case[0] * 100),3))
    
