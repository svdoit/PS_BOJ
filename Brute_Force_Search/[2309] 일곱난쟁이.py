heights = []

for i in range(9):
    heights.append(int(input()))

sum_heights = sum(heights)
first = 0
second = 0

for i in range(9):
    for j in range(i+1, 9):
        if (sum_heights - (heights[i]+heights[j])) == 100:
            first = heights[i]
            second = heights[j]

heights.remove(first)
heights.remove(second)
heights.sort()

for i in heights:
    print(i)
