def d(n):
    result = n
    for i in list(str(n)):
        result += int(i)
    return result

dn_list = []
for i in range(1,10001):
    num = d(i)
    if num <= 10000:
        dn_list.append(num)
    if i not in dn_list:
        print(i)
