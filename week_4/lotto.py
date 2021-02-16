from random import *

i = randint(1, 45)

lotto = set([])
while len(lotto) != 6:
    lotto.add(randint(1, 45))

print(lotto)
