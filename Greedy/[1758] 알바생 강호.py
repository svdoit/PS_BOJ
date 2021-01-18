import sys

N = int(sys.stdin.readline().strip())
ppl = []

for i in range(N):
    ppl.append(int(sys.stdin.readline().strip()))

ppl.sort(reverse=True)
result = 0

for i in range(N):
    final_tip = ppl[i] - ((i+1) - 1)
    if final_tip > 0 :
        result += final_tip

print(result)
    
