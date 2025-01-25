T = 1,2,3,4,5,6,7,8,9 # tuple

a, b, *rest = T # first 2 elements
*rest, c, d = T # last 2 elements

print(a, b)
print(rest)

