---
layout: default
title: "trans1"
---

[< 2.3.7 Loading Data](../2_3_7_loading_data/trans1.html) | [2.3.9 Additional Graphical And Numerical Summaries >](../2_3_9_additional_graphical_and_numerical_summaries/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 2.3.8 For Loops

# 2.3.8 for 루프들

A `for` loop is a standard tool in many languages that repeatedly evaluates some chunk of code while varying different values inside the code.

하나의 `for` 루프는 코드 안의 여러 값들을 변경하면서 코드의 어떤 부분(chunk)을 평가하기를 반복하는, 다수의 언어들에서의 표준 도구입니다.

For example, suppose we loop over elements of a list and compute their sum.

예를 들어, 우리가 한 리스트의 원소들을 루프하며 그들의 합을 계산한다고 가정해 봅시다.

```python
In [96]: total = 0
         for value in [3, 2, 19]:
             total += value
         print('Total is: {0}'.format(total))
Total is: 24
```

The indented code beneath the line with the `for` statement is run for each value in the sequence specified in the `for` statement.

`for` 구문이 있는 줄 아래로 들여쓰기된(indented) 코드는 그 `for` 구문 안에 명시된 시퀀스 안의 각 값에 대해 실행됩니다.

The loop ends either when the cell ends or when code is indented at the same level as the original `for` statement.

그 셀이 끝나거나 코드가 처음의 `for` 구문과 동일한 수준으로 들여쓰기될 때 그 루프가 끝납니다.

We see that the final line above which prints the total is executed only once after the for loop has terminated.

우리는 위에서 합계를 출력하는 마지막 줄은 for 루프가 종료된 이후 오직 한 번만 실행됨을 봅니다.

Loops can be nested by additional indentation.

루프들은 추가적인 들여쓰기로 중첩될 수 있습니다.

```python
In [97]: total = 0
         for value in [2, 3, 19]:
             for weight in [3, 2, 1]:
                 total += value * weight
         print('Total is: {0}'.format(total))
Total is: 144
```

Above, we summed over each combination of `value` and `weight`.

위에서, 우리는 `value` 및 `weight` 의 각 조합에 대해 합산했습니다.

We also took advantage of the _increment_ notation in `Python`: the expression `a += b` is equivalent to `a = a + b`.

우리는 또한 `Python` 의 _증가(increment)_ 표기법을 활용했습니다: 표현식 `a += b` 는 `a = a + b` 와 동일합니다.

Besides being a convenient notation, this can save time in computationally heavy tasks in which the intermediate value of `a + b` need not be explicitly created.

단지 편리한 표기법인 것 외에도, 이것은 `a + b` 의 중간 값이 명시적으로 생성될 필요가 없는 계산적으로 무거운 작업들에서 시간을 절약할 수 있습니다.

Perhaps a more common task would be to sum over `(value, weight)` pairs.

아마도 보다 흔한 작업은 `(value, weight)` 짝들에 대해 합산하는 것일 것입니다.

For instance, to compute the average value of a random variable that takes on possible values 2, 3 or 19 with probability 0.2, 0.3, 0.5 respectively we would compute the weighted sum.

예를 들어, 각각 0.2, 0.3, 0.5 의 확률들로 2, 3 또는 19 의 가능한 값들을 가지는 임의 변수 하나의 평균값을 구하기 위해 우리는 가중치 합을 계산할 것입니다.

Tasks such as this can often be accomplished using the `zip()` function that loops over a sequence of tuples.

이와 같은 작업들은 종종 튜플들의 시퀀스를 루프하는 `zip()` 함수를 사용하여 성취될 수 있습니다.

```python
In [98]: total = 0
         for value, weight in zip([2, 3, 19],
                                  [0.2, 0.3, 0.5]):
             total += weight * value
         print('Weighted average is: {0}'.format(total))
Weighted average is: 10.8
```

## String Formatting

## 문자열 폼 형성(Formatting)

In the code chunk above we also printed a string displaying the total.

위 코드 부분에서 우리는 또한 그 합을 표시하는 하나의 문자열을 출력했습니다.

However, the object `total` is an integer and not a string.

그러나, 그 객체 `total` 은 정수이며 문자열이 아닙니다.

Inserting the value of something into a string is a common task, made simple using some of the powerful string formatting tools in `Python`.

어떤 것의 값을 하나의 문자열로 삽입하는 것은 평범한 작업이며, `Python` 내 강력한 조립 문자열 포매팅 도구들을 사용하여 단순하게 만들어 집니다.

Many data cleaning tasks involve manipulating and programmatically producing strings.

많은 데이터 정제(cleaning) 작업들은 프로그래밍 방식으로 문자열들을 조작하고 만들어내는 것을 수반합니다.

For example we may want to loop over the columns of a data frame and print the percent missing in each column.

예를 들어 우리는 데이터 프레임의 열들을 루프하고 각각의 열에서 누락된 퍼센트를 출력하기를 원할 수도 있습니다.

Let’s create a data frame `D` with columns in which 20% of the entries are missing i.e. set to `np.nan`.

그 항목들 중 20%가 누락된, 즉 `np.nan` 으로 설정된 열들을 가지는 데이터 프레임 체제 `D` 하나를 생성해 봅시다.

We’ll create the values in `D` from a normal distribution with mean 0 and variance 1 using `rng.standard_normal()` and then overwrite some random entries using `rng.choice()`.

우리는 `rng.standard_normal()` 을 사용하여 평균 0 과 분산 1 의 하나의 정규 분포로부터 `D` 안의 값들을 생성하고, 그런 다음 `rng.choice()` 를 이용하여 무작위 항목들을 덮어 씌울 것입니다.

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

We see that the `template.format()` method expects two arguments `{0}` and `{1:.2%}`, and the latter includes some formatting information.

우리는 `template.format()` 메서드가 두 인수들 `{0}` 그리고 `{1:.2%}` 를 기대하며, 이후의 후자는 덧붙여 약간의 포매팅 정보들을 포함하고 있음을 봅니다.

In particular, it specifies that the second argument should be expressed as a percent with two decimal digits.

특히, 그것은 그 두 번째 인수가 거듭 두 자리 소수점들과 함께 하나의 퍼센트로 표현되어져야만 한다고 지정합니다.

The reference `docs.python.org/3/library/string.html` includes many helpful and more complex examples.

해당 참고용의 문서 `docs.python.org/3/library/string.html` 는 도움이 되고 또한 더 복잡한 많은 예제들을 수록 포함합니다.

---

## Sub-Chapters (하위 목차)

[< 2.3.7 Loading Data](../2_3_7_loading_data/trans1.html) | [2.3.9 Additional Graphical And Numerical Summaries >](../2_3_9_additional_graphical_and_numerical_summaries/trans1.html)
