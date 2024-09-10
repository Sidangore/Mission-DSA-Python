# List [Basics] 


## Slicing in Python
For example, let us have a list,
```python
l = [10, 20, 30, 40, 50]
print(l[0:5:2]) # [10, 30, 50]
print(l[::-1]) # [50, 40, 30, 20, 10] Reverses the List

l2 = l[:] # This copies the l to l2 
```
The above code will print the elements 10, 30, 50
***
list[start:stop:increment] => Returns a List

**Note**: Stop is exclusive

Tuple and String in Python are immutable.


