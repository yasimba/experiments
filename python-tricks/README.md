# Table of Contents
1. [Loops](#loops)
2. [Slicing](#slicing)
3. [Zipping](#zipping)
4. [Strings](#strings)



## Loops


```python
#print from 1 to n-1
for i in range(1,10):
  print(i)
>1
>2
>3
>4
>5
>6
>7
>8
>9

#print list in reverse
for i in reversed(range(10)):
  print(i)
>9
>8
>7
>6
>5
>4
>3
>2
>1
```


## Slicing

```python
#https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```

## Zipping

```python
#https://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html
a = [1, 2, 3]
b = ['a', 'b', 'c']
z = zip(a, b)
z
[(1, 'a'), (2, 'b'), (3, 'c')]
zip(*z)
[(1, 2, 3), ('a', 'b', 'c')]
```


## Strings
```python
#isalnum --> Checks whether string consists of alphanumeric characters

str = "this2009";  # No space in this string
print str.isalnum()
> True
str = "this is string example....wow!!!";
print str.isalnum()
> False

#Reverse a string:
s = 'abcd'
s[::-1]
print(s )
> dcba


#Comparing strings
>>> "ab" < "ac"
True
>>> min("ab","ac")
'ab'
```


## Counters
```python
from collections import Counter
t = 'ABC'
y = Counter(t)
print(y)
>>> Counter({'A':1,'B':1,'C':1})
```

### Stacks

```
append: Appends object at the end.

x = [1, 2, 3]
x.append([4, 5])
print (x)
gives you: [1, 2, 3, [4, 5]]

extend: Extends list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print (x)
gives you: [1, 2, 3, 4, 5]
https://stackoverflow.com/questions/252703/difference-between-append-vs-extend-list-methods-in-python
```
