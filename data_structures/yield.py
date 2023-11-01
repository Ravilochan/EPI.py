def normal_function(n):
    if n == 0:
        return "zero"


def funky_function(n):
    if n == 0:
        return "zero"
    yield n


print(list("hello"), type("hello"))
print("Funky Function =>")
print(type(funky_function(0)))
print(list(funky_function(0)))
print(next(funky_function(10)))
# print(next(funky_function(0)))  # error


print("Normal Function =>")
print(type(normal_function(0)))
print(list(normal_function(0)))
# print(next(normal_function(10)))  # error

"""
The `list()` function in Python is used to convert an iterable (e.g., a generator, list, tuple, etc.) into a list.
When you pass a generator to `list()`, it iterates over the generator to collect all its yielded values and convert them into a list.
In the `funky_function`, when `n` is equal to 0, the function returns the string "zero,". However, the presence of a `yield` statement in the function causes Python to treat it as a generator function. In Python, when a function contains a `yield` statement, it becomes a generator function, and calling the function doesn't execute its code immediately.
Instead, it returns a generator object.

Calling the function with `funky_function(0)` doesn't execute the function's code at this point;
it only creates a generator object. The generator code is only executed when you iterate over it (e.g., using a `for` loop, `list()`, or `next()`).
So, when you use `list(funky_function(0))`, Python tries to iterate over the generator returned by `funky_function(0)`.
However, as mentioned in your code, when `n` is 0, the generator doesn't yield any values; it simply returns "zero".
Therefore, the generator is empty, and `list()` collects no values from it, resulting in an empty list.

In summary, `list()` attempts to iterate over the generator created by `funky_function(0)`, which doesn't yield any values when `n` is 0, and that's why we get an empty list.
The "zero" string is returned by the function, but it's not part of the generator's yielded values.
"""
