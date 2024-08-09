# datatypes

# IMMUTABLE Datatypes > int, str, float, complex, tuple, set

x = 234
g = "heiren"
n = """
the quick brown fox
jumps over 
the lazy dog.
"""
k = 25.534
b = 134+8j

e = (3,"342", 6e68)
w = {789,"laen",327+4j}


print(x,type(x)) # 234 <class 'int'>

print(g,type(g)) # heiren <class 'str'>

print(n,type(n)) # the quick brown fox
                 # jumps over 
                 # the lazy dog.
                 #  <class 'str'>

print(k,type(k)) # 25.534 <class 'float'>

print(b,type(b)) # (134+8j) <class 'complex'>

print(e,type(e)) # (3, '342', 6e+68) <class 'tuple'>

print(w,type(w)) # {'laen', (327+4j), 789} <class 'set'>


# MUTABLE Datatypes > list , dict , byte arrray

j = [1,454,883,"abcde", 324.443]

print(j,type(j)) # [1, 454, 883, 'abcde', 324.443] <class 'list'>

z = {
    "name" : "rosi329",
    "city" : "isb",
    "os" : "linux"
}


print(z,type(z)) # {'name': 'rosi329', 'city': 'isb', 'os': 'linux'} <class 'dict'>

#  h = bytearray type 
