A, B = input().split()

A = A[2:] + A[1:2] + A[:1]
B = B[2:] + B[1:2] + B[:1]

int_A = int(A)
int_B = int(B)

if int_A >= int_B:
    print(A)
else:
    print(B)
