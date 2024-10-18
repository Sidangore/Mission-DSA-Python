import collections
from collections import deque

s = deque()
s.append(10)
s.append(20)
s.append(30)
s.pop()
s.pop()
s.pop()
if s:
    s.pop()
print(s)
if s:
    print(s[-1])