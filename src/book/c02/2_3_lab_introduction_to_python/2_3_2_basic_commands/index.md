---
layout: default
title: "index"
---

[< 2.3.1 Getting Started](../2_3_1_getting_started/index.html) | [2.3.3 Introduction To Numerical Python >](../2_3_3_introduction_to_numerical_python/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 2.3.2 Basic Commands_

In this lab, we will introduce some simple `Python` commands.

For more resources about `Python` in general, readers may want to consult the tutorial at `docs.python.org/3/tutorial/`. Like most programming languages, `Python` uses _functions_ to perform operations.

To run a function called `fun`, we type `fun(input1, input2)`, where the inputs (or _arguments_) `input1` and `input2` tell `Python` how to run the function.

A function can have any number of inputs.

For example, the `print()` function outputs a text representation of all of its arguments to the console.

```python
In [1]: print('fit a model with', 11, 'variables')
fit a model with 11 variables
```

The following command will provide information about the `print()` function.

```python
In [2]: print?
```

Adding two integers in `Python` is pretty intuitive.

```python
In [3]: 3 + 5
Out[3]: 8
```

In `Python`, textual data is handled using _strings_.

For instance, `"hello"` and `'hello'` are strings.

We can concatenate them using the addition `+` symbol.

```python
In [4]: "hello" + " " + "world"
Out[4]: 'hello world'
```

A string is actually a type of _sequence_: this is a generic term for an ordered list.

The three most important types of sequences are lists, tuples, and strings.

We introduce lists now.

The following command instructs `Python` to join together the numbers 3, 4, and 5, and to save them as a _list_ named `x`.

When we type `x`, it gives us back the list.

```python
In [5]: x = [3, 4, 5]
        x
Out[5]: [3, 4, 5]
```

Note that we used the brackets `[]` to construct this list.

We will often want to add two sets of numbers together.

It is reasonable to try the following code, though it will not produce the desired results.

```python
In [6]: y = [4, 9, 7]
        x + y
Out[6]: [3, 4, 5, 4, 9, 7]
```

The result may appear slightly counterintuitive: why did `Python` not add the entries of the lists element-by-element?

In `Python`, lists hold _arbitrary_ objects, and are added using _concatenation_.

In fact, concatenation is the behavior that we saw earlier when we entered `"hello" + " " + "world"`.

This example reflects the fact that `Python` is a general-purpose programming language.

Much of `Python`’s data-specific functionality comes from other packages, notably `numpy` and `pandas`.

In the next section, we will introduce the `numpy` package.

See `docs.scipy.org/doc/numpy/user/quickstart.html` for more information about `numpy`.

---

## Sub-Chapters


[< 2.3.1 Getting Started](../2_3_1_getting_started/index.html) | [2.3.3 Introduction To Numerical Python >](../2_3_3_introduction_to_numerical_python/index.html)
