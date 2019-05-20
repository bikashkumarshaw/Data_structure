# Data_structure

### List:

#### This is a duplication of Lists in python with its basic implementation.

### How to use:

#### append:
```
>>> from list import List
>>> k = List()
>>> for val in range(3, 27, 2):
... 	k.append(val)
... 
>>> print k
[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
```

#### delete:
```
>>> k.delete(9)
()
>>> print k
[3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 25]
```
#### insert:
```
>>> k.insert(12, 0)
>>> print k
[12, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 25]
```
#### pop:
```
>>> k.pop(0)
12
>>> print k
[3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 25]
```
#### PrintTree:
```
>>> k.PrintTree()
3
5
7
11
13
15
17
19
21
23
25
>>>
```
