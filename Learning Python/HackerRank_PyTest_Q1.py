s = 'aWESOME is cODING'
t = s.split(" ")
print(t)

i = 0
j = 2

t[i], t[j] = t[j], t[i]
result = " ".join(t)
print(result)

name='cODING is aWESOME'
print(name.swapcase())