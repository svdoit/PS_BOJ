A, B, C = map(int, input().split())
break_even_point = 0

if B >= C:
    break_even_point = -1
else:
    break_even_point = A//(C-B) + 1
    
print(break_even_point)

# /와 //의 차이 중요
