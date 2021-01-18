def seq(X):
    count = 0
    
    if X < 100:
        return X
    else:
        for i in range(100, X+1):
            nums = list(map(int, str(i)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
                count += 1
        return (99+count)

N = int(input())
result = seq(N)
print(result)
    
