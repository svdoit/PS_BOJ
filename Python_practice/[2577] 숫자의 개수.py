A = int(input())
B = int(input())
C = int(input())

num_list = list(str(A*B*C))

for i in range(10):
    num_count = num_list.count(str(i))
    print(num_count)


