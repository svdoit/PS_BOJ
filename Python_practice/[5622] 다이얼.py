dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
call = input()
time = 0

for alphabet in call:
    for d in dial:
        if alphabet in d:
            time += dial.index(d) + 3

print(time)
