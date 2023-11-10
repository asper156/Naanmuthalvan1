Certainly! Here's a simple Python implementation of a recursive function to calculate the factorial of a given number:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

You can use this function by passing a number as an argument, for example:

```python
result = factorial(5)
print(result)
```

This will output `120`, which is the factorial of 5.
