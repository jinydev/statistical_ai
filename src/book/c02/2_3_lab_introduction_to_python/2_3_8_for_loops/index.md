---
layout: default
title: "index"
---

# _2.3.8 For Loops_

A `for` loop is a standard tool in many languages that repeatedly evaluates some chunk of code while varying different values inside the code. For example, suppose we loop over elements of a list and compute their sum.

```python
In [96]: total = 0
         for value in [3, 2, 19]:
             total += value
         print('Total is: {0}'.format(total))
Total is: 24
```

The indented code beneath the line with the `for` statement is run for each value in the sequence specified in the `for` statement. The loop ends either when the cell ends or when code is indented at the same level as the original `for` statement. We see that the final line above which prints the total is executed only once after the for loop has terminated. Loops can be nested by additional indentation.

```python
In [97]: total = 0
         for value in [2, 3, 19]:
             for weight in [3, 2, 1]:
                 total += value * weight
         print('Total is: {0}'.format(total))
Total is: 144
```

Above, we summed over each combination of `value` and `weight`. We also took advantage of the _increment_ notation in `Python`: the expression `a += b` is equivalent to `a = a + b`. Besides being a convenient notation, this can save time in computationally heavy tasks in which the intermediate value of `a + b` need not be explicitly created.

Perhaps a more common task would be to sum over `(value, weight)` pairs. For instance, to compute the average value of a random variable that takes on possible values 2, 3 or 19 with probability 0.2, 0.3, 0.5 respectively we would compute the weighted sum. Tasks such as this can often be accomplished using the `zip()` function that loops over a sequence of tuples.

```python
In [98]: total = 0
         for value, weight in zip([2, 3, 19],
                                  [0.2, 0.3, 0.5]):
             total += weight * value
         print('Weighted average is: {0}'.format(total))
Weighted average is: 10.8
```

## String Formatting

In the code chunk above we also printed a string displaying the total. However, the object `total` is an integer and not a string. Inserting the value of something into a string is a common task, made simple using some of the powerful string formatting tools in `Python`. Many data cleaning tasks involve manipulating and programmatically producing strings.

For example we may want to loop over the columns of a data frame and print the percent missing in each column. Let’s create a data frame `D` with columns in which 20% of the entries are missing i.e. set to `np.nan`. We’ll create the values in `D` from a normal distribution with mean 0 and variance 1 using `rng.standard_normal()` and then overwrite some random entries using `rng.choice()`.

```python
In [99]: rng = np.random.default_rng(1)
         A = rng.standard_normal((127, 5))
         M = rng.choice([0, np.nan], p=[0.8, 0.2], size=A.shape)
         A += M
         D = pd.DataFrame(A, columns=['food',
                                      'bar',
                                      'pickle',
                                      'snack',
                                      'popcorn'])
         D[:3]
Out[99]:        food       bar    pickle     snack   popcorn
         0  0.345584  0.821618  0.330437 -1.303157       NaN
         1       NaN -0.536953  0.581118  0.364572  0.294132
         2       NaN  0.546713       NaN -0.162910 -0.482119

In [100]: for col in D.columns:
              template = 'Column "{0}" has {1:.2%} missing values'
              print(template.format(col,
                                    np.isnan(D[col]).mean()))
Column "food" has 16.54% missing values
Column "bar" has 25.98% missing values
Column "pickle" has 29.13% missing values
Column "snack" has 21.26% missing values
Column "popcorn" has 22.83% missing values
```

We see that the `template.format()` method expects two arguments `{0}` and `{1:.2%}`, and the latter includes some formatting information. In particular, it specifies that the second argument should be expressed as a percent with two decimal digits.

The reference `docs.python.org/3/library/string.html` includes many helpful and more complex examples.
