conversion = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for a in conversion:
    word = word.replace(a, '*')

print(len(word))
