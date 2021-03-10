# Python Quickref

- snake_case (unless dealing with legacy code)

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
a > b

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

```python
s = "hello"
s[0] # h

for char in "hello":
  print(char)

"ll" in "hello" # True

f'2 cubed is {2**3}' # Interpolation

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

## Tuples

- Ordered and immutable

```python
my_tuple = (1,2,3)
my_tuple = tuple([1,2,3])
my_tuple[0]
```

## Lists

```python
my_list = [-1,0,1,2,3]
my_list = list({-1,0,1,2,3})
my_list[0]  # -1
my_list[-1] #  3

my_list.append(4)
my_list.pop() #default is -1
my_list.insert(0, -10)

# In-place ops:
my_list.sort(key = abs, reverse = True)
my_list.sort(key = lambda x: abs(x))
my_list.reverse()
```

## Sets

- Unordered, no duplicates

```python
my_set = {'a','b','c'}
my_set = set(['a','b','c'])
my_set.add('d')
my_set.remove('d')

'd' in my_set # False
my_set.remove('d')  # exception
my_set.discard('d') # no exception
```

## Dictionaries / Maps

```python
my_dict = {'a': 'aaaaa', 'b': 'bbbbb', 'c': 'ccccc'}
my_dict['a'] # `aaaaa`
my_dict['a'] = 'AAAAA'
my_dict.pop('a') # `AAAAA`
for key in my_dict: print(key, my_dict[key])
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

## Object
```python
class Vehicle:
  def __init__(self, wheels, doors):
    self.wheels = wheels
    self.doors = doors
```

## Further reading

- https://www.w3schools.com/python/default.asp
