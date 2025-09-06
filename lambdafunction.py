from functools import reduce

nums = [1,3,4,6,7]
k = lambda y:y*y*y
s = k(4)

m= tuple(map(lambda y: y**2, nums))

f = tuple(filter(lambda y: y%2==0, nums))

r = reduce(lambda x,y: x*y , nums)

print(s)
print(m)
print(f)
print(r)


