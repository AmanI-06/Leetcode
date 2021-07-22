from collections import Counter
a="abcd"
b="abcde"
print(Counter(b))
print(Counter(a))
print((Counter(b) - Counter(a)).popitem())