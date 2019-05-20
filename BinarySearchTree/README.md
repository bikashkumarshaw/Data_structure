# Data_structure

### Binary search tree:
#### Prepares a binary tree for given inputs and gives search options.

### How to use:
#### insert:

```
>>> from bst import BST
>>> k = BST()
>>> k.insert(12)
>>> k.insert(34)
>>> k.insert(13)
>>> k.insert(12)
>>> k.insert(90)
>>> k.insert(36)
>>> k.insert(8798)                             
>>> k.PrintTree()
12
13
34
36
90
8798
>>> 
```

#### Search:
```
>>> k.search(13)
True
>>> k.search(76)
False
>>> 
```

#### delete:
```
>>> k.delete(13)
>>> k.PrintTree()
12
34
36
90
8798
>>> k.delete(12)    
>>> k.PrintTree()
34
36
90
8798
>>> 
```
