---
layout: default
title: "index"
---

# _2.3.8 For Loops_
# 2.3.8 For 반복문 (For Loops)

A `for` loop is a standard tool in many languages that repeatedly evaluates some chunk of code while varying different values inside the code. For example, suppose we loop over elements of a list and compute their sum.

`for` 반복문(loop)은 코드 내부의 여러 값들을 다양하게 변경해 가며 특정 코드 덩어리를 반복적으로 평가하고 실행하는, 대부분의 프로그래밍 언어에서 쓰이는 매우 표준적인 도구입니다. 예를 들어 우리가 어느 리스트의 요소들을 반복해서 순회 탐색하며 그 요소들의 합계를 계산한다고 가정해 봅시다.

```python
In [96]: total = 0
         for value in [3, 2, 19]:
             total += value
         print('Total is: {0}'.format(total))
Total is: 24
```

The indented code beneath the line with the `for` statement is run for each value in the sequence specified in the `for` statement. The loop ends either when the cell ends or when code is indented at the same level as the original `for` statement. We see that the final line above which prints the total is executed only once after the for loop has terminated. Loops can be nested by additional indentation.

`for` 구문이 쓰인 줄 바로 밑에 들여쓰기 된 코드는 해당 `for` 문에서 지정된 시퀀스의 각 값들에 대해 순차적으로 실행됩니다. 이 반복문은 작성 셀이 완전히 끝나거나, 혹은 코드가 본래의 `for` 구문과 똑같은 레벨 위치로 다시 내어쓰기 될 때 종료됩니다. 위 출력에서 총계를 출력하는 마지막 줄 코드가 결과적으로 반복문이 전부 종료된 이후에 단 한 번만 실행되었음을 볼 수 있습니다. 또한 반복문들은 코드를 추가로 들여쓰기 함으로써 내부에 또 다른 반복문을 중첩(nested)시켜 작성할 수도 있습니다.

```python
In [97]: total = 0
         for value in [2, 3, 19]:
             for weight in [3, 2, 1]:
                 total += value * weight
         print('Total is: {0}'.format(total))
Total is: 144
```

Above, we summed over each combination of `value` and `weight`. We also took advantage of the _increment_ notation in `Python`: the expression `a += b` is equivalent to `a = a + b`. Besides being a convenient notation, this can save time in computationally heavy tasks in which the intermediate value of `a + b` need not be explicitly created.

위 코드에서, 우리는 `value` 와 `weight` 의 가능한 모든 조합 결과들을 반복하며 하나씩 합산했습니다. 우리는 여기서 `Python` 의 _증감(increment)_ 표기법 기능도 함께 활용했습니다: 수식 `a += b` 는 곧 수식 `a = a + b` 와 원리상 완벽히 동등합니다. 이것은 단지 표기상 펼쳐 쓰기 편리한 방법일 뿐만 아니라, 굳이 `a + b` 의 중간 연산 값을 메모리상에 명시적으로 생성할 필요가 없으므로 연산 처리가 무거운 작업에서는 속도와 시간을 절약해 줄 수도 있습니다.

Perhaps a more common task would be to sum over `(value, weight)` pairs. For instance, to compute the average value of a random variable that takes on possible values 2, 3 or 19 with probability 0.2, 0.3, 0.5 respectively we would compute the weighted sum. Tasks such as this can often be accomplished using the `zip()` function that loops over a sequence of tuples.

아마 앞선 중첩 반복보다 실무에서 훨씬 더 흔한 반복 작업은 `(value, weight)` 처럼 짝지어진 쌍 자체를 하나씩 순회하며 합산하는 일일 것입니다. 예컨대 확률 0.2, 0.3, 0.5 에 따라 각각 2, 3, 19 의 값을 취할 수 있는 무작위 변수의 평균값을 계산한다고 칠 때 우리는 그런 것들의 가중합을 계산할 것입니다. 이런 종류의 작업은 보통 일련의 튜플 시퀀스를 한데 묶고 순회하는 `zip()` 함수를 사용하면 간단하게 달성할 수 있습니다.

```python
In [98]: total = 0
         for value, weight in zip([2, 3, 19],
                                  [0.2, 0.3, 0.5]):
             total += weight * value
         print('Weighted average is: {0}'.format(total))
Weighted average is: 10.8
```

## String Formatting
## 문자열 포매팅 (String Formatting)

In the code chunk above we also printed a string displaying the total. However, the object `total` is an integer and not a string. Inserting the value of something into a string is a common task, made simple using some of the powerful string formatting tools in `Python`. Many data cleaning tasks involve manipulating and programmatically producing strings.

위의 코드 블록에서 우리는 결과 총합을 화면에 나타내는 텍스트 문자열도 함께 출력했습니다. 하지만 데이터상 `total` 객체 자체는 사실 문자열이 아니고 하나의 정수 숫자입니다. 이렇게 어떤 형태의 데이터를 문자열 텍스트 내부 한가운데에 끼워 넣어 합치는 작업은 `Python` 이 제공하는 매우 강력한 문자열 포매팅 도구들을 사용하면 굉장히 단순해지며 아주 흔하게 쓰입니다. 수많은 데이터 정제 과정들은 이런 식으로 문자열을 프로그래밍 통제로 제작하고 조작하는 작업을 거치게 됩니다.

For example we may want to loop over the columns of a data frame and print the percent missing in each column. Let’s create a data frame `D` with columns in which 20% of the entries are missing i.e. set to `np.nan`. We’ll create the values in `D` from a normal distribution with mean 0 and variance 1 using `rng.standard_normal()` and then overwrite some random entries using `rng.choice()`.

하나의 예시로서, 우리는 데이터 프레임 안에 늘어선 열(columns)들을 순차 반복하며 각 열마다 어느 정도의 데이터가 결측 손실(missing)되었는지 그 퍼센트 백분율을 출력하고 싶을 수 있습니다. 그럼 지금부터 데이터 내 항목의 20%가 누락된, 즉 `np.nan` 값으로 대체 설정된 열들을 지닌 연습용 예제 데이터 프레임 `D` 를 만들어 보겠습니다. 우리는 `rng.standard_normal()` 을 사용하여 먼저 평균 0, 분산 1 인 정규 분포 수치들로 `D` 내부 값을 채운 뒤, 그 위로 `rng.choice()` 를 사용해 난수 위치들을 뽑아내 일부 누락 값을 무작위로 덮어쓰겠습니다.

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

`template.format()` 메서드가 현재 내부적으로 `{0}` 과 `{1:.2%}` 라는 두 개의 구멍 인수 자리를 요구 기대하고 있으며, 그중 후자는 어떤 형식으로 이를 표시할지에 대한 포매팅 정보도 함께 규정하여 포함하고 있음을 알 수 있습니다. 특히나 저 후자의 형식은, 뒤에 들어올 두 번째 인수 값이 반드시 소수점 이하 두 자리 수를 지닌 퍼센트(%) 형태로 숫자가 변환 표현되어야 함을 명시적으로 지시합니다.

The reference `docs.python.org/3/library/string.html` includes many helpful and more complex examples.

파이썬 공식 웹사이트 `docs.python.org/3/library/string.html` 의 참조 문서를 확인해 보면 문자열 포매팅에 관련한 훨씬 복잡하고도 유용한 예시들을 다수 확인해 볼 수 있습니다.

---

## Sub-Chapters (하위 목차)

현재 2.3.8 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)
