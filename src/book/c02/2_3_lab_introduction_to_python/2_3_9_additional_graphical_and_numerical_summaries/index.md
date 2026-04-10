---
layout: default
title: "index"
---

# _2.3.9 Additional Graphical and Numerical Summaries_
# 2.3.9 추가적인 그래픽 및 수치 요약 (Additional Graphical and Numerical Summaries)

We can use the `ax.plot()` or `ax.scatter()` functions to display the quantitative variables. However, simply typing the variable names will produce an error message, because `Python` does not know to look in the `Auto` data set for those variables.

우리는 양적 변수들을 화면에 그래프로 시각화하기 위해 `ax.plot()` 이나 `ax.scatter()` 함수를 직접 사용할 수 있습니다. 그러나 단순히 변수 이름만 입력하게 되면 곧장 에러 메시지가 발생할 텐데, 왜냐하면 `Python` 시스템 자체는 해당 변수들을 찾기 위해 `Auto` 데이터 세트 내부를 스스로 들여다봐야 한다는 사실을 알지 못하기 때문입니다.

```python
In [101]: fig, ax = subplots(figsize=(8, 8))
          ax.plot(horsepower, mpg, 'o');
NameError: name 'horsepower' is not defined
```

We can address this by accessing the columns directly:

우리는 데이터 세트 내부의 특정 열에 직접 접근 지시함으로써 이 문제를 해결할 수 있습니다:

```python
In [102]: fig, ax = subplots(figsize=(8, 8))
          ax.plot(Auto['horsepower'], Auto['mpg'], 'o');
```

Alternatively, we can use the `plot()` method with the call `Auto.plot()`. Using this method, the variables can be accessed by name. The plot methods of a data frame return a familiar object: an axes. We can use it to update the plot as we did previously:

대안으로서, 우리는 `Auto.plot()` 처럼 직접 호출하는 방식의 통합 `plot()` 메서드를 사용할 수도 있습니다. 이 메서드를 통하면 안에 포함된 변수 이름만으로 수치에 접근할 수 있게 됩니다. 데이터 프레임 전용 `plot` 메서드들은 우리에게 이미 무척 친숙한 특정 객체를 반환하는데: 그것은 바로 축(axes)입니다. 우리는 앞서 그랬듯 이를 활용해 그래프 그림을 다양하게 업데이트할 수 있습니다:

```python
In [103]: ax = Auto.plot.scatter('horsepower', 'mpg')
          ax.set_title('Horsepower vs. MPG');
```

If we want to save the figure that contains a given axes, we can find the relevant figure by accessing the `figure` attribute:

만일 주어진 축(axes) 정보가 담긴 이 그림 객체를 파일로 저장하고 싶다면, 축의 내장 `figure` 속성에 직접 접근함으로써 해당 전체 그림을 획득할 수 있습니다:

```python
In [104]: fig = ax.figure
          fig.savefig('horsepower_mpg.png');
```

We can further instruct the data frame to plot to a particular axes object. In this case the corresponding `plot()` method will return the modified axes we passed in as an argument. Note that when we request a one-dimensional grid of plots, the object `axes` is similarly one-dimensional. We place our scatter plot in the middle plot of a row of three plots within a figure.

나아가 우리는 데이터 프레임이 아예 특정한 기존 축(axes) 객체 위에 직접 그림을 그리도록 세부 지시할 수도 있습니다. 이런 경우 해당 `plot()` 메서드는 애초에 우리가 인수로 전달했던 바로 그 축 객체를, 변경된 상태 그대로 다시 반환하게 됩니다. 우리가 하나의 큰 그림 판 내부에 플롯들로 이루어진 1차원 그리드를 요청 생성할 때, 객체 `axes` 역시도 동일하게 1차원 배열 형태를 띈다는 사실을 유의하십시오. 아래 코드에서는 내부 행렬 그림 중 세 번째 공간들로 이루어진 1열 3행 구획에서 가장 정중앙 위치에 산점도를 배치합니다.

```python
In [105]: fig, axes = subplots(ncols=3, figsize=(15, 5))
          Auto.plot.scatter('horsepower', 'mpg', ax=axes[1]);
```

Note also that the columns of a data frame can be accessed as attributes: try typing in `Auto.horsepower`.

참고로 데이터 프레임의 열(columns) 역시도 내부 속성(attributes) 형식으로 접근 가능합니다: 지금 당장 콘솔에 `Auto.horsepower` 라고 입력해 보십시오.

We now consider the `cylinders` variable. Typing in `Auto.cylinders.dtype` reveals that it is being treated as a quantitative variable. However, since there is only a small number of possible values for this variable, we may wish to treat it as qualitative. Below, we replace the `cylinders` column with a categorical version of `Auto.cylinders`. The function `pd.Series()` owes its name to the fact that `pandas` is often used in time series applications.

이제 우리는 또 다른 내부 변수인 `cylinders` 를 다룹니다. 콘솔에 `Auto.cylinders.dtype` 을 입력해 보면 현재 시스템이 이를 양적(quantitative) 변수로 취급하고 있음이 드러납니다. 그러나 이 변수가 가질 수 있는 값의 종류 수가 실상 매우 적기 때문에, 우리는 이를 차라리 질적(qualitative) 변수로 관리 취급하고 싶을 수 있습니다. 아래 코드에서 우리는, 기존 `cylinders` 열 전체를 다시 질적 범주형 특성으로 구성한 `Auto.cylinders` 의 새로운 대체 버전으로 전면 교체합니다. 여기서 사용된 `pd.Series()` 라는 함수의 이름 자체는, 실제 `pandas` 패키지가 실무에서 시계열(time series) 데이터 애플리케이션 작업에 고질적으로 잦게 쓰인다는 기여 사실에서 빚어져 비롯되었습니다.

```python
In [106]: Auto.cylinders = pd.Series(Auto.cylinders, dtype='category')
          Auto.cylinders.dtype
```

Now that `cylinders` is qualitative, we can display it using the `boxplot()` method.

이제 `cylinders` 변수가 질적(qualitative) 속성 형태를 띠게 되었으므로, 우리는 전용 `boxplot()` 메서드를 사용해 데이터를 상자 수염 그림으로 표현할 수 있습니다.

```python
In [107]: fig, ax = subplots(figsize=(8, 8))
          Auto.boxplot('mpg', by='cylinders', ax=ax);
```

The `hist()` method can be used to plot a _histogram_.

메서드 구분인 `hist()` 구문을 사용하면 특정 데이터에 대한 _히스토그램(histogram)_ 을 그릴 수 있습니다.

```python
In [108]: fig, ax = subplots(figsize=(8, 8))
          Auto.hist('mpg', ax=ax);
```

The color of the bars and the number of bins can be changed:

지정된 막대의 고유 색상이나 수량 구간별 막대 수용통(bins)의 개수는 얼마든지 바꿀 수 있습니다:

```python
In [109]: fig, ax = subplots(figsize=(8, 8))
          Auto.hist('mpg', color='red', bins=12, ax=ax);
```

See `Auto.hist?` for more plotting options. We can use the `pd.plotting.scatter_matrix()` function to create a _scatterplot matrix_ to visualize all of the pairwise relationships between the columns in a data frame.

추가적인 시각화 플로팅 옵션이 더 필요하다면 콘솔에 `Auto.hist?` 를 검색 참조하십시오. 또한 파이썬 내장 `pd.plotting.scatter_matrix()` 함수를 사용하면 하나의 거대한 _산점도 행렬(scatterplot matrix)_ 모양을 생성하여, 전체 데이터 프레임 내에 위치한 내부 열(columns)들의 가능한 모든 상호 쌍(pairwise) 변수 관계들을 종합 시각화할 수 있습니다.

```python
In [110]: pd.plotting.scatter_matrix(Auto);
```

We can also produce scatterplots for a subset of the variables.

혹은, 전체가 아닌 부분 변수들의 특정 하위 모집단 집합에 대해서만 산점도를 개별 산출할 수도 있습니다.

```python
In [111]: pd.plotting.scatter_matrix(Auto[['mpg',
                                           'displacement',
                                           'weight']]);
```

The `describe()` method produces a numerical summary of each column in a data frame.

통계 함수 `describe()` 메서드를 호출 적용하면 해당 변수 데이터 프레임 안의 각 모든 열에 대해 의미 있는 전체 수치적 요약 결과물을 산출 작성해 줍니다.

```python
In [112]: Auto[['mpg', 'weight']].describe()
```

We can also produce a summary of just a single column.

필요하다면, 오직 단일 단독 열에 대해서만 관련 요약본을 출력할 수도 있습니다.

```python
In [113]: Auto['cylinders'].describe()
          Auto['mpg'].describe()
```

To exit `Jupyter`, select `File / Close and Halt`.

`Jupyter` 노트북 환경을 완전히 종료하려면 상단 메뉴 창에서 `File / Close and Halt` 조작을 선택하십시오.

---

## Sub-Chapters (하위 목차)

현재 2.3.9 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)
