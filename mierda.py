from random import choice, sample

my_list = ["PC1", "PC2", "PC3", "PC4", "PC5", "OC6", "PC7", "PC8", "PC9", "PC10"]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

from platform import platform
 
print(platform())
print(platform(1))
print(platform(0, 1))


from platform import machine
 
print(machine())

from platform import processor
 
print(processor())

from platform import system
 
print(system())

from platform import version
 
print(version())


from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

import math
p=result = math.e
pp=math.exp(1)
print(p)
print(pp)