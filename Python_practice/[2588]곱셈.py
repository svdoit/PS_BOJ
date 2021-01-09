num1 = int(input())
num2 = int(input())

out1 = num1 * ((num2%100)%10)
out2 = num1 * ((num2%100)//10)
out3 = num1 * ((num2//100))
result = num1*num2

print(out1, out2, out3, result, sep='\n')
