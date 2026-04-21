---
layout: default
title: "trans1"
---

[< 2.3.3 Introduction To Numerical Python](../2_3_3_introduction_to_numerical_python/trans1.html) | [2.3.5 Sequences And Slice Notation >](../2_3_5_sequences_and_slice_notation/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 2.3.4 Graphics

# 2.3.4 그래픽스

In `Python`, common practice is to use the library `matplotlib` for graphics.

`Python`에서, 그래픽스를 위해 `matplotlib` 라이브러리를 사용하는 것이 흔한 관행입니다.

However, since `Python` was not written with data analysis in mind, the notion of plotting is not intrinsic to the language.

그러나, `Python`이 데이터 분석을 마음에 두고 작성되지 않았기 때문에, 플로팅(plotting)의 개념은 언어에 본질적이지 않습니다.

We will use the `subplots()` function from `matplotlib.pyplot` to create a figure and the axes onto which we plot our data.

우리는 하나의 피겨(figure)와 우리가 우리의 데이터를 플롯팅할 축들(axes)을 생성하기 위해 `matplotlib.pyplot` 으로부터 `subplots()` 함수를 사용할 것입니다.

For many more examples of how to make plots in `Python`, readers are encouraged to visit `matplotlib.org/stable/gallery/`.

`Python`에서 플롯(plot)들을 만드는 방법에 대한 더 많은 예시들을 위해, 독자들은 `matplotlib.org/stable/gallery/` 를 방문하도록 권장됩니다.

In `matplotlib`, a plot consists of a _figure_ and one or more _axes_.

`matplotlib`에서, 하나의 플롯은 하나의 _피겨(figure)_ 와 하나 또는 그 이상의 _축들(axes)_ 로 구성됩니다.

You can think of the figure as the blank canvas upon which one or more plots will be displayed: it is the entire plotting window.

당신은 피겨를 하나 혹은 하나보다 더 많은 플롯들이 그 위에 표시될 빈 캔버스로서 생각할 수 있습니다: 이것은 전체 플로팅 창(window)입니다.

The _axes_ contain important information about each plot, such as its $x$- and $y$-axis labels, title, and more.

_축들(axes)_ 은 그것의 $x$- 및 $y$-축 라벨들, 제목, 그리고 더 많은 것들과 같이, 각각의 플롯에 단연 중요한 정보들을 포함합니다.

(Note that in `matplotlib`, the word _axes_ is not the plural of _axis_: a plot’s _axes_ contains much more information than just the $x$-axis and the $y$-axis.)

(`matplotlib` 안에서, _축들(axes)_ 이라는 단어는 _축(axis)_ 의 복수형이 아님에 유의하십시오: 한 플롯의 _축들_ 은 단지 $x$-축 및 $y$-축보다 더 많은 그 이상의 정보를 담습니다.)

We begin by importing the `subplots()` function from `matplotlib`.

우리는 `matplotlib` 으로부터 `subplots()` 함수를 임포트(import)함으로써 시작합니다.

We use this function throughout when creating figures.

우리는 피겨들을 생성할 때 내내 이 함수를 사용합니다.

The function returns a tuple of length two: a figure object as well as the relevant axes object.

이 함수는 길이 2의 하나의 튜플을 반환합니다: 하나의 피겨 객체와 아울러 관련된 축들 객체입니다.

We will typically pass `figsize` as a keyword argument.

우리는 전형적으로 `figsize` 를 키워드 인자로서 전달할 것입니다.

Having created our axes, we attempt our first plot using its `plot()` method.

우리의 축들을 생성하고서, 우리는 그것의 `plot()` 메서드를 사용하여 우리의 첫 번째 플롯을 시도합니다.

To learn more about it, type `ax.plot?`.

그것에 관해 더 많이 알기 위해서, `ax.plot?` 을 타이핑하십시오.

```python
In [39]: from matplotlib.pyplot import subplots
         fig, ax = subplots(figsize=(8, 8))
         x = rng.standard_normal(100)
         y = rng.standard_normal(100)
         ax.plot(x, y);
```

We pause here to note that we have _unpacked_ the tuple of length two returned by `subplots()` into the two distinct variables `fig` and `ax`.

우리는 여기서 우리가 `subplots()` 에 의해 반환된 길이 2의 그 튜플을 두 개의 구별되는 변수들인 `fig` 와 `ax` 안으로 _풀어헤쳤다(unpacked)_ 는 것을 주목하기 위해 잠시 멈춥니다.

Unpacking is typically preferred to the following equivalent but slightly more verbose code:

풀어헤치기(unpacking)는 이어지는 다음의 동일하지만 약간 더 장황한(verbose) 코드보다 전형적으로 선호되어집니다:

```python
In [40]: output = subplots(figsize=(8, 8))
         fig = output[0]
         ax = output[1]
```

We see that our earlier cell produced a line plot, which is the default.

우리는 우리의 이전 셀이 하나의 선(line) 플롯을 생산했음을 봅니다, 그리고 그것은 기본값(default)입니다.

To create a scatterplot, we provide an additional argument to `ax.plot()`, indicating that circles should be displayed.

하나의 산점도(scatterplot)를 생성하기 위해, 우리는 원들이 표시되어야만 한다는 것을 가리키도록 하나의 부가적인 인자를 `ax.plot()` 에 제공합니다.

```python
In [41]: fig, ax = subplots(figsize=(8, 8))
         ax.plot(x, y, 'o');
```

Different values of this additional argument can be used to produce different colored lines as well as different linestyles.

이러한 부가적 인자의 상이한 값들은 이내 상이한 선-스타일들(linestyles) 뿐 만 아니라 상이하게 색칠된 선들을 생산하도록 사용될 수 있습니다.

As an alternative, we could use the `ax.scatter()` function to create a scatterplot.

하나의 대안으로서, 우리는 산점도를 생성하기 위하여 `ax.scatter()` 함수를 사용할 수 있습니다.

```python
In [42]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o');
```

Notice that in the code blocks above, we have ended the last line with a semicolon.

위 코드 블록들 안에서, 우리가 마지막 줄을 하나의 세미콜론(semicolon)으로 끝맺었음에 주의하십시오.

This prevents `ax.plot(x, y)` from printing text to the notebook.

이것은 `ax.plot(x, y)` 가 그 노트북에 텍스트를 출력하는 것을 막아 줍니다.

However, it does not prevent a plot from being produced.

그러나, 이것은 플롯이 생산되는 것을 막지는 않습니다.

If we omit the trailing semi-colon, then we obtain the following output:

만약 우리가 그 뒤따르는(trailing) 세미-콜론을 생략한다면, 그러면 우리는 다음 출력을 반환 획득합니다:

```python
In [43]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o')
Out[43]: <matplotlib.collections.PathCollection at 0x7fb3d9c8f310>
```

In what follows, we will use trailing semicolons whenever the text that would be output is not germane to the discussion at hand.

다음에 따르는 내용들에서, 우리는 출력될 텍스트가 당면한 토론과 더이상 관련이 없는 경우마다 뒤따르는 세미콜론들을 사용할 것입니다.

To label our plot, we make use of the `set_xlabel()`, `set_ylabel()`, and `set_title()` methods of `ax`.

우리의 플롯을 명목 지칭 라벨하기 위해, 우리는 `ax` 의 `set_xlabel()`, `set_ylabel()`, 그리고 `set_title()` 메서드들을 사용합니다.

```python
In [44]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o')
         ax.set_xlabel("this is the x-axis")
         ax.set_ylabel("this is the y-axis")
         ax.set_title("Plot of X vs Y");
```

Having access to the figure object `fig` itself means that we can go in and change some aspects and then redisplay it.

피겨(figure) 객체 `fig` 그 자체에 접근 권한을 갖는다는 것은 곧 우리가 내부로 들어가서 몇 가지 측면들을 변경하고 그런 다음 그것을 재-표시(redisplay)할 수 있음을 의미합니다.

Here, we change the size from `(8, 8)` to `(12, 3)`.

여기서, 우리는 크기를 `(8, 8)` 에서 `(12, 3)` 으로 변경합니다.

```python
fig.set_size_inches(12, 3)
fig
```

Occasionally we will want to create several plots within a figure.

때때로 우리는 하나의 피겨 내부에 여러 플롯들을 생성하길 원할 것입니다.

This can be achieved by passing additional arguments to `subplots()`.

이것은 추가적인 단락 부과 인자들을 `subplots()` 측에 전달함으로써 실현 도달 성취 달성될 수 있습니다.

Below, we create a $2 \times 3$ grid of plots in a figure of size determined by the `figsize` argument.

아래에서, 우리는 `figsize` 인자에 의해 결정된 크기의 하나의 피겨 안에 $2 \times 3$ 격자의 플롯들을 생성합니다.

In such situations, there is often a relationship between the axes in the plots.

그러한 상황들 속에서, 플롯들 내의 축들 사이에는 매우 종종 하나의 매개 관계성이 있습니다.

For example, all plots may have a common $x$-axis.

예를 들어, 모든 제반 플롯들은 다같이 한 단면의 공통된 $x$-축을 가질 수도 있습니다.

The `subplots()` function can automatically handle this situation when passed the keyword argument `sharex=True`.

`subplots()` 함수는 키워드 인자 `sharex=True` 가 넘겨 전달될 때 이러한 상황들을 단연 자동으로 조치 처리할 수 있습니다.

The `axes` object below is an array pointing to different plots in the figure.

아래 지표 `axes` 변수 객체는 당 피겨(figure) 안의 다분 상이한 여러 플롯들을 전면 각각 가리키는 하나의 배열입니다.

```python
In [45]: fig, axes = subplots(nrows=2,
                              ncols=3,
                              figsize=(15, 5))
```

We now produce a scatter plot with `'o'` in the second column of the first row and a scatter plot with `'+'` in the third column of the second row.

우리는 이제 첫 번째 행의 두 번째 열 안에서 `'o'` 기호를 구비한 하나의 산점도를 생성하고, 두 번째 행의 세 번째 열 안에서 `'+'` 인표를 구비한 하나의 산점도를 생산 산출합니다.

```python
In [46]: axes[0, 1].plot(x, y, 'o')
         axes[1, 2].scatter(x, y, marker='+')
         fig
```

Type `subplots?` to learn more about `subplots()`.

`subplots()` 에 관해 더 폭넓게 알기 위해 `subplots?` 구문을 타이핑하십시오.

To save the output of `fig`, we call its `savefig()` method.

`fig` 의 출력을 저장 보관하기 위해, 우리는 그것의 `savefig()` 메서드를 호출합니다.

The argument `dpi` is the dots per inch, used to determine how large the figure will be in pixels.

그 인자 `dpi` 는 1인치당 지정 점들(dots per inch)로써, 픽셀들 상에서 해당 단일 피겨 크기가 과연 얼마나 클지 여부를 결정하기 위해 쓰이고 사용됩니다.

```python
In [47]: fig.savefig("Figure.png", dpi=400)
         fig.savefig("Figure.pdf", dpi=200);
```

We can continue to modify `fig` using step-by-step updates; for example, we can modify the range of the $x$-axis, re-save the figure, and even re-display it.

우리는 단계-별(step-by-step) 업데이트들을 조작 사용하여 이 `fig` 대상을 계속해서 변형 수정할 여력이 있습니다; 가령 예를 들어, 우리는 $x$-축의 구간 범위를 전면 수정하고, 해당 피겨를 재-저장(re-save)하며, 및 나아가 심지어 그것을 재-표시(re-display)할 수 조차 있습니다.

```python
In [48]: axes[0, 1].set_xlim([-1, 1])
         fig.savefig("Figure_updated.jpg")
         fig
```

We now create some more sophisticated plots.

우리는 이제 약간의 더 섬세하고 정교한 플롯들을 생성합니다.

The `ax.contour()` method produces a _contour plot_ in order to represent three-dimensional data, similar to a topographical map.

`ax.contour()` 메서드는 어느 지형도(topographical map)와 무척 유사하게 3-차원적 관련 데이터를 나타내기 위해 하나의 _등고선 플롯(contour plot)_ 을 생산합니다.

It takes three arguments:

그것은 다음의 세 가지 인자들을 취해 가집니다:

- A vector of `x` values (the first dimension),

- `x` 값들의 하나의 벡터 객체 (첫 번째 차원 단락),

- A vector of `y` values (the second dimension), and

- `y` 지정 값들의 하나의 벡터 객체 (두 번째 차원 면모), 그리고

- A matrix whose elements correspond to the `z` value (the third dimension) for each pair of `(x, y)` coordinates.

- 그 이면 구성 원소들이 각각의 `(x, y)` 여러 쌍 지표 좌표 위치에 대한 기준 `z` 값(세 번째 조작 차원)에 직후 개별 상응하는 하나의 매트릭스 행렬 단위.

To create `x` and `y`, we’ll use the command `np.linspace(a, b, n)`, which returns a vector of `n` numbers starting at `a` and ending at `b`.

단위 `x` 와 `y` 양방을 생성하기 위해, 우리는 명령어 조치 `np.linspace(a, b, n)` 구문을 사용할 터인데, 그것은 곧 기점 `a` 에서 일순 시작하고 종단 `b` 에서 거듭 끝나는 무려 총 `n` 개의 숫자들의 하나의 객체적 벡터 덩이를 필시 반환합니다.

```python
In [49]: fig, ax = subplots(figsize=(8, 8))
         x = np.linspace(-np.pi, np.pi, 50)
         y = x
         f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
         ax.contour(x, y, f);
```

We can increase the resolution by adding more levels to the image.

우리는 대상 조작 이미지 상에 한결 더 여러 많은 도출 레벨들(levels)을 가미하고 더함으로써 시야 해상도를 당면 가중치 증가 시킬 수 있습니다.

```python
In [50]: fig, ax = subplots(figsize=(8, 8))
         ax.contour(x, y, f, levels=45);
```

To fine-tune the output of the `ax.contour()` function, take a look at the help file by typing `?plt.contour`.

`ax.contour()` 단위 함수의 결과물 단면 출력을 더 미세-조정(fine-tune)하기 위해서, 기입 `?plt.contour` 구문을 수동 타이핑함으로써 딸린 도움말 참고 파일을 한 번 훑어보아 살펴보십시오.

The `ax.imshow()` method is similar to `ax.contour()`, except that it produces a color-coded plot whose colors depend on the `z` value.

`ax.imshow()` 당 메서드는 오직 그것 결과물이 `z` 변수 단면 값에 의지하는 색깔들로 일체 색상-코드된(color-coded) 플롯을 거둔다는 오직 이 한 사실을 제외하고는, `ax.contour()` 구문 체제 작동과 매우 유사합니다.

This is known as a _heatmap_, and is sometimes used to plot temperature in weather forecasts.

이것은 일종의 하나의 _히트맵(heatmap)_ 으로서 일컫어 알려져 있으며, 때때로 기상 주간 일기예보 등 내에서 체감 온도를 모름지기 플로팅 그리기 위해 간혹 사용됩니다.

```python
In [51]: fig, ax = subplots(figsize=(8, 8))
         ax.imshow(f);
```

---

## Sub-Chapters (하위 목차)

[< 2.3.3 Introduction To Numerical Python](../2_3_3_introduction_to_numerical_python/trans1.html) | [2.3.5 Sequences And Slice Notation >](../2_3_5_sequences_and_slice_notation/trans1.html)
