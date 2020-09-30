import random
listA = ['a', 'b', 'c', 'd']
print(random.choice(listA))
print(random.choice(listA))
print(random.choice(listA))
print(random.choice(listA))

p = random.sample(listA, 2)
print(p)
print(listA)
