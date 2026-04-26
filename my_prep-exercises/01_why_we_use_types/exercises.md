
## Exercise 1

### Question

What does `double("22")` do?


### Answer

`double("22")` returns `"2222"`.

### Explanation

In Python, multiplying a string by an integer repeats the string.
So `"22" * 2` becomes `"2222"`.

---

## Exercise 2

### Question

What is the bug in this code?

```python
def double(number):
    return number * 3
```

### Answer

The function name is `double`, but it multiplies the number by 3.

### Explanation

The name `double` suggests that the function should multiply the number by 2.
However, the implementation multiplies by 3.

To fix this, we can either:

* Change the logic:

```python
def double(number):
    return number * 2
```

* Or rename the function:

```python
def triple(number):
    return number * 3
```

---

## My Thoughts

Type annotations help make code clearer and safer.
They allow developers to understand what type of data a function expects and returns.

Without types, functions can behave in unexpected ways, like working with strings instead of numbers, which can lead to bugs.

However, types cannot catch logical errors, such as using `* 3` instead of `* 2`.
