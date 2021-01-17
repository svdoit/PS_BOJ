N = int(input())
score = list(map(int, input().split()))
new_score_sum = 0
average = 0

max_score = max(score)

for i in score:
    change_score = i / max_score * 100
    new_score_sum += change_score

average = new_score_sum / N

print(average)
