# Python Quickref

- snake_case (unless dealing with legacy code)
- zero-based indexing

```python
a = 1               # int
b = 1.5             # float
c = d = "hello"     # string
t, f  = True, False # bool
```

## Operators

```python
a % b # Modulus
a ** b # Exponent
a // b # Floor division

# Assignment
a += 2
a *= 2

# Comparison ("same contents?")
a == b
a != b
a > b and b >=  c

# Identity ("same object/pointer?")
a is b
a is not b

# Logic
a and b
a or b
not a

# Membership
a in b
a not in b
```

## Casting

```python
a = str(1)
b = int('2')
c = float('3.5')
```

## Strings

- Strings are immutable arrays
- Use a list of strings and `join` to mimic a stringbuilder

```python
s = "hello"
s[0] # h

for char in "hello":
  print(char)

"ll" in "hello" # True

f'2 cubed is {2**3}' # Interpolation

'a'*10 # 'aaaaaaaaaa'

# Methods:
s = "this is a string"
ss = "is"
s.startswith(ss), s.endswith(ss)
s.count(ss)
s.index(ss), s.rindex(ss) # exception
s.find(ss), s.rfind(ss)  # no exception

s.isalpha() # alphabet
s.isdigit() # digits 0-9
s.isalnum() # alphanumeric
s.islower(), s.isupper()

s.lower(), s.upper()
s.replace("string", "blah")
s.lstrip(), s.strip(), s.rstrip() # trim whitespace
"{}, {}!".format("Hello", "World")

s.ljust(i), s.center(i), s.rjust(i) # i = len of returned str

words = "hello there".split() # ['hello', 'there']
chars = list("abc") # ['a', 'b', 'c']
", ".join(chars)    # "1, 2, 3"
```

## Control Flow

```python
if x > 0: foo()
elif not x > 5: bar()
else: foobar()

y = 'foo' if z > 0 else 'bar'
```

## Loops

```python
# All print 0,1,2,3,4:
for i in range(5): print(i)
for s in '01234': print(s)
for e in [0,1,2,3,4]: print(e)

j = 0
while j < 5: print(i)

break    # Exit the loop
continue # Exit the current iteration
```

## Built in Functions

```python
print("{} said hello to {}!".format("Bob", "Alice"))
abs(-0.5)
len() # list, strings, etc
round(1.2345, 2) # 1.23
chr(ord('a')) # char to unicode
```

### Iterables

```python
sorted([3,1,2])
all([True, True])
any([True, True])
filter(lambda x: x > 1, [1,2,3])
map(abs, [-1,2,3])
min|max([1,2,3])
sum([1,2,3])
reversed([1,2,3])
zip([1,2,3],[4,5,6])
iter([0,1,2,3,4]) # See Loops section
```

## Lists

- Use an array internally
- Can be also be used for:
  - stacks - append() and pop()
  - queues - append() and pop(0)
    - pop(0) is O(n) --> use collections.deque instead

```python
my_list = [-1,0,1,2,3]
my_list = list({-1,0,1,2,3})
my_list[0]  # -1
my_list[-1] #  3

[1,2,3] == [1,2,3] # True
[3,2,1] == [1,2,3] # False
list1 + list2 #combine 2 lists

my_list.append(4)
my_list.pop() #defaults to the last element (-1)
my_list.insert(0, -10)

# In-place ops:
my_list.sort(key = abs, reverse = True)
my_list.sort(key = lambda x: abs(x))
my_list.reverse()
```

## Sets

- Use a Hash table internally
- Unordered, no duplicates

```python
my_set = {'a','b','c'}
my_set = set(['a','b','c'])
my_set.add('d')
my_set.remove('d')  # exception
my_set.discard('d') # no exception

'd' in my_set # False

{1,2,3} == {1,2,3}   # True
{1,2,3} == {3,2,2,1} # True
```

## Dictionaries / Maps

- Use a Hash table internally

```python
my_dict = {'a': 'aaaaa', 'b': 'bbbbb', 'c': 'ccccc'}
my_dict['a'] # `aaaaa`
my_dict['a'] = 'AAAAA'
my_dict.pop('a') # `AAAAA`
for key in my_dict: print(key, my_dict[key])
```

## Tuples

- Ordered and immutable

```python
my_tuple = (1,2,3)
my_tuple = tuple([1,2,3])
my_tuple[0]
```

## collections — Container datatypes

```python
# dict/map subclass where elements are keys and counts are the values
from collections import Counter
c = Counter(iterable_or_dict) # strings are iterables too

c(element) # returns count or 0 if element DNE
c(element) = 5 # set count
del c(element) # delete element from c

for element in c:
  count = c[element])

c.elements() #iterator, keys are repeated according to their counts
c.most_common(optional_int)
c.update(optional_iterable_or_map) #update c with param's values

# Common patterns (copied from docs):
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts
```

https://docs.python.org/3/library/collections.html#collections.deque

```python
from collections import deque
rotate()
```

## Slicing

Slicing lists does not generate copies of the objects in the list; it just copies the references to them.

```python
my_list = list("abcde")
my_list[ start_index : stop_index_exlusive : step]

# All these mean the same thing:
my_list[ 0 : len(my_list) : 1 ] # Defaults
my_list[::]
my_list[:]
my_list[]
my_list

# Examples
my_list[::2] # Every second element
"abc"[::-1] # Reverse a string
arr[n:] + arr[:n] # shift/roll/rotate a list
```

## Enumerate

```python
for index,val in enumerate(['a','b','c']): print(index,val)

for index,val in enumerate('abc'): print(index,val)
```

## List Comprehensions

```python
newlist = [expression for item in iterable if condition == True]
newlist = [s.upper() for s in ['a','b','c'] if s <= 'b' ]
```

## itertools

```python
from itertools import *
p = permutations([1, 2])
# (1, 2) (2, 1)

c = combinations([1, 2, 3], 2)
# (1, 2) (1, 3) (2, 3)

list_of_lists = [['a', 'b'], ['-'], ['y', 'z']]
products = product(*list_of_lists)
mp = map(lambda i: "".join(i), products)
# a-y a-z b-y b-z
```

## Packing and Unpacking

```python
x, y = y, z # swap values

# tuple unpacking
(x, y, z) = 1, 2, 3
x, y, z = (1, 2, 3)
x, y, z = 1, 2, 3

# iterable unpacking (NB: not safe with sets)
x, y, z = '123'
x, y, z = [1, 2, 3]
x, y, z = range(3)

# Star/* operator aka unpacking operator
*x, = 1, 2 # note the comma, which makes it a tuple; aka x = [1, 2]
x, *y, z = [1,2,3,4,5] # aka x=1  y=[2,3,4]  z=5

my_list0 = [1,2,3,4,5]
my_list1 = [0,*my_list0,6]
```

print unpacking via star operator `*`:

```python
arr = [1, 2, 3, 4, 5]
print(' '.join(map(str,arr)))
print (*arr)
# '1 2 3 4 5' printed by both
```

## Exceptions

```python
if a > b:
  raise Exception("uh oh")

try:
  do_something()
except ArithmeticError:
  print("Caught a arithmetic error")
except:
  print("Caught a misc error")
else:
  print("Executed iff nothing went wrong")
finally:
  print("This will always execute")
```

## Objects

```python
class Vehicle:
  def __init__(self, wheels, doors):
    self.wheels = wheels
    self.doors = doors

  def my_class_method(self):
    pass
```

## Script shebang

https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3-shebang

```python
#!/usr/bin/env python3
import stuff

def my_func():
  print("hello")
```

## File IO

```python
with open('data.txt','w') as f:
  for i in range(10):
    f.write(f'{i}\n')

with open('data.txt') as f:
  lines = f.readlines()
for line in lines:
  print(line)
```

## Is python call by reference or call by value?

- Immutables like strings and tuples are call by value
- Mutables like collections are call by reference

## Further reading

- https://www.w3schools.com/python/default.asp
- https://www.programiz.com/python-programming/inheritance
- https://www.geeksforgeeks.org/inheritance-in-python/
- https://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html
- https://github.com/justmarkham/python-reference/blob/master/reference.py
