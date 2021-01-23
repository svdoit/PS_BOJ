word = list(map(str, input()))
alphabet = [-1]*26

for i in range(len(word)):
    index = ord(word[i])-ord('a')
    if alphabet[index] != -1:
        continue
    else:
        alphabet[index] = i

for i in range(26):
    print(alphabet[i], end=' ')
