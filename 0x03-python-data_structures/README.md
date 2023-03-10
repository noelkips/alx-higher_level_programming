** 0x03-python-data_structures**

The project tasks in this repository covers the following concepts:<br>
> Why Python programming is awesome
> What are lists and how to use them
> What are the differences and similarities between strings and lists
> What are the most common methods of lists and how to use them
> How to use lists as stacks and queues
> What are list comprehensions and how to use them
> What are tuples and how to use them
> When to use tuples versus lists
> What is a sequence
> What is tuple packing
> What is sequence unpacking
> What is the del statement and how to use it


Tasks
**Task 0** Write a function that prints all integers of a list.

> Prototype: def print_list_integer(my_list=[]):
> Format: one integer per line. See example
> You are not allowed to import any module
> You can assume that the list only contains integers
> You are not allowed to cast integers into strings
> You have to use str.format() to print integers

**Task 1** Write a function that retrieves an element from a list like in C.

> Prototype: def element_at(my_list, idx):
> If idx is negative, the function should return None
> If idx is out of range (> of number of element in my_list), the function should return None
> You are not allowed to import any module
> You are not allowed to use try/except

**Task 2**
Write a function that replaces an element of a list at a specific position (like in C).

**Task 3**
Write a function that prints all integers of a list, in reverse order.

**Task 4**
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).


**Task 5**
Write a function that removes all characters c and C from a string.


**Task 6**
Write a function that prints a matrix of integers.

**Task 7**
Write a function that adds 2 tuples.

**Task 8**
Write a function that returns a tuple with the length of a string and its first character.

**Task 9**
Write a function that finds the biggest integer of a list.

**Task 10**
Write a function that finds all multiples of 2 in a list.

**Task 11**
Write a function that deletes the item at a specific position in a list.

**Task 12**
Complete the source code in order to switch value of a and b

**Task 13**
Technical interview preparation:

**Task 14**
CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.


Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.
<br>
All your files will be interpreted/compiled on Ubuntu 14.04 LTS


Create a C function that prints some basic info about Python lists.

Prototype: void print_python_list_info(PyObject *p);
Python version: 3.4
Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
OS: Ubuntu 14.04 LTS
Start by reading:
listobject.h
object.h
Common Object Structures
List Objects
