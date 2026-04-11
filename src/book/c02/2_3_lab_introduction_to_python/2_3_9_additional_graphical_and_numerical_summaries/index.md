---
layout: default
title: "index"
---

# _2.3.9 Additional Graphical and Numerical Summaries_

# _2.3.9 부가적인 그래픽적 및 수치적 요약들_

We can use the `ax.plot()` or `ax.scatter()` functions to display the quantitative variables.

우리는 양적 변수들(quantitative variables)을 표시하기 위해 `ax.plot()` 이나 `ax.scatter()` 함수들을 사용할 수 있습니다.

However, simply typing the variable names will produce an error message, because `Python` does not know to look in the `Auto` data set for those variables.

그러나, `Python` 은 그 변수들을 위해 `Auto` 데이터 세트 안을 보아야 하는 것을 알지 못하기 때문에, 단순하게 변수 이름들을 타이핑하는 것은 하나의 에러 메시지를 생산할 것입니다.

```python
In [101]: fig, ax = subplots(figsize=(8, 8))
          ax.plot(horsepower, mpg, 'o');
NameError: name 'horsepower' is not defined
```

We can address this by accessing the columns directly:

우리는 열들을 직접적으로 접근함으로써 이것을 부를(address) 수 있습니다:

```python
In [102]: fig, ax = subplots(figsize=(8, 8))
          ax.plot(Auto['horsepower'], Auto['mpg'], 'o');
```

Alternatively, we can use the `plot()` method with the call `Auto.plot()`.

대안으로서, 우리는 `Auto.plot()` 호출과 함께 `plot()` 메서드를 사용할 수 있습니다.

Using this method, the variables can be accessed by name.

이 메서드를 사용하여, 그 변수들은 이름에 의해 접근되어질 수 있습니다.

The plot methods of a data frame return a familiar object: an axes.

데이터 프레임의 그 플롯(plot) 메서드들은 하나의 친숙한 객체를 반환합니다: 바로 하나의 축들(axes) 객체입니다.

We can use it to update the plot as we did previously:

우리가 이전에 했던 것처럼 우리는 그 플롯을 업데이트하기 위해 그것을 사용할 수 있습니다:

```python
In [103]: ax = Auto.plot.scatter('horsepower', 'mpg')
          ax.set_title('Horsepower vs. MPG');
```

If we want to save the figure that contains a given axes, we can find the relevant figure by accessing the `figure` attribute:

우리가 주어진 축들을 포함하는 해당 피겨(figure)를 저장하기를 원한다면, 우리는 `figure` 속성(attribute)에 접근함에 의하여 관련 피겨를 찾을 수 있습니다:

```python
In [104]: fig = ax.figure
          fig.savefig('horsepower_mpg.png');
```

We can further instruct the data frame to plot to a particular axes object.

우리는 나아가 데이터 프레임이 특정 축들(axes) 객체에 플롯하도록 지시할 수 있습니다.

In this case the corresponding `plot()` method will return the modified axes we passed in as an argument.

이 경우 해당하는 `plot()` 메서드는 우리가 인자로서 전달한 수정된 축들을 반환할 것입니다.

Note that when we request a one-dimensional grid of plots, the object `axes` is similarly one-dimensional.

우리가 1차원의 플롯들의 그리드를 요청할 때, 객체 `axes` 는 유사하게 1차원이라는 것에 주목하십시오.

We place our scatter plot in the middle plot of a row of three plots within a figure.

우리는 하나의 피겨(figure) 안 세 개 플롯들의 행 중 중간 플롯 안에 우리의 산점도(scatter plot)를 배치합니다.

```python
In [105]: fig, axes = subplots(ncols=3, figsize=(15, 5))
          Auto.plot.scatter('horsepower', 'mpg', ax=axes[1]);
```

Note also that the columns of a data frame can be accessed as attributes: try typing in `Auto.horsepower`.

데이터 프레임의 열들이 속성들로서 또한 접근되어질 수 있음에 주목하십시오: `Auto.horsepower` 를 타이핑해 넣기를 시도해 보십시오.

We now consider the `cylinders` variable.

우리는 이제 `cylinders` 변수를 고려합니다.

Typing in `Auto.cylinders.dtype` reveals that it is being treated as a quantitative variable.

`Auto.cylinders.dtype` 을 타입하는 것은 그것이 양적 변수로서 다루어지고 있음을 드러냅니다.

However, since there is only a small number of possible values for this variable, we may wish to treat it as qualitative.

그러나, 이 변수에 대해 오직 가능한 값들의 작은 수가 존재하기 때문에, 우리는 질적(qualitative)으로서 이것을 다루기를 바랄 수 있습니다.

Below, we replace the `cylinders` column with a categorical version of `Auto.cylinders`.

아래에서, 우리는 `cylinders` 열을 `Auto.cylinders` 의 범주형 종류로 대체합니다.

The function `pd.Series()` owes its name to the fact that `pandas` is often used in time series applications.

함수 `pd.Series()` 의 이름은 시계열(time series) 적용들 안에서 `pandas` 가 종종 사용된다는 사실에 빚을 지고 있습니다.

```python
In [106]: Auto.cylinders = pd.Series(Auto.cylinders, dtype='category')
          Auto.cylinders.dtype
```

Now that `cylinders` is qualitative, we can display it using the `boxplot()` method.

이제 `cylinders` 가 질적이므로, 우리는 `boxplot()` 메서드를 사용하여 그것을 표시할 수 있습니다.

```python
In [107]: fig, ax = subplots(figsize=(8, 8))
          Auto.boxplot('mpg', by='cylinders', ax=ax);
```

The `hist()` method can be used to plot a _histogram_.

그 `hist()` 메서드는 하나의 _히스토그램(histogram)_ 을 그리기 위해 사용될 수 있습니다.

```python
In [108]: fig, ax = subplots(figsize=(8, 8))
          Auto.hist('mpg', ax=ax);
```

The color of the bars and the number of bins can be changed:

막대들의 색상과 빈(bin)들의 개수는 변경되어질 수 있습니다:

```python
In [109]: fig, ax = subplots(figsize=(8, 8))
          Auto.hist('mpg', color='red', bins=12, ax=ax);
```

See `Auto.hist?` for more plotting options.

더 많은 플롯 옵션들을 위해 `Auto.hist?` 를 보십시오.

We can use the `pd.plotting.scatter_matrix()` function to create a _scatterplot matrix_ to visualize all of the pairwise relationships between the columns in a data frame.

우리는 개별 데이터 프레임 안의 열들 간 순서쌍 관계들의 모두를 시각화하기 위하여 하나의 _산점도 메트릭스(scatterplot matrix)_ 생성을 목적으로 함수 `pd.plotting.scatter_matrix()` 를 사용할 수 있습니다.

```python
In [110]: pd.plotting.scatter_matrix(Auto);
```

We can also produce scatterplots for a subset of the variables.

우리는 또한 변수들의 한 부분 집합을 위한 산점도들을 산출할 수 있습니다.

```python
In [111]: pd.plotting.scatter_matrix(Auto[['mpg',
                                           'displacement',
                                           'weight']]);
```

The `describe()` method produces a numerical summary of each column in a data frame.

그 `describe()` 메서드는 데이터 프레임 안의 각 열에 대한 하나의 수치적 요약(numerical summary)을 생성 산출합니다.

```python
In [112]: Auto[['mpg', 'weight']].describe()
```

We can also produce a summary of just a single column.

우리는 또한 그저 단일 열 하나의 요약을 산출할 수 있습니다.

```python
In [113]: Auto['cylinders'].describe()
          Auto['mpg'].describe()
```

To exit `Jupyter`, select `File / Close and Halt`.

`Jupyter` 를 종료하기 위해, `File / Close and Halt` 를 선택하십시오.
