N = int(input())

group_word = 0

for i in range(N):
    word = input()
    exist = 0
    
    for index in range(len(word)-1):
        if word[index] != word[index+1]: #알파벳이 달라지는 시점
            check_rest = word[index+1:] #그 인덱스부터 끝까지 체크
            
            if check_rest.count(word[index]) > 0: #지금 알파벳이 앞으로도 또 나오는가?
                exist += 1
                
    if exist == 0:
            group_word += 1

print(group_word)
