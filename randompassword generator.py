

bcp=40


import random
a = random.randint(0, bcp)
b = random.randint(0, bcp)
c = random.randint(0, bcp)
d = random.randint(0, bcp)
e = random.randint(0, bcp)
f = random.randint(0, bcp)
g = random.randint(0, bcp)
h = random.randint(0, bcp)
ab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", "","","","","","","9","8","7","6","5","4","3","2","1"]
ps=(ab[a]+ab[b]+ab[c]+ab[d]+ab[e]+ab[f]+ab[g]+ab[h])
print("your random password is:",ps)

