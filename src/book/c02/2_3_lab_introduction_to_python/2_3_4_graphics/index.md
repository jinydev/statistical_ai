---
layout: default
title: "index"
---

# _2.3.4 Graphics_
# 2.3.4 그래픽 (Graphics)

In `Python`, common practice is to use the library `matplotlib` for graphics. However, since `Python` was not written with data analysis in mind, the notion of plotting is not intrinsic to the language. We will use the `subplots()` function from `matplotlib.pyplot` to create a figure and the axes onto which we plot our data. For many more examples of how to make plots in `Python`, readers are encouraged to visit `matplotlib.org/stable/gallery/`.

`Python`에서는 그래픽 시각화 작업을 위해 `matplotlib` 라이브러리를 주로 사용하는 것이 일반적입니다. 그러나 `Python` 자체가 원래 데이터 분석을 염두에 두고 만들어진 언어는 아니기 때문에, 그래프를 그리는 플로팅(plotting) 기능이 언어에 자체적으로 내장되어 있지는 않습니다. 따라서 우리는 데이터를 화면에 그려낼 그림 틀(figure)과 축(axes)을 별도로 생성하기 위해 `matplotlib.pyplot` 내부의 `subplots()` 함수를 사용할 것입니다. `Python`에서 다양한 그래프를 그리는 방법에 대해 더 알아보고 싶다면, `matplotlib.org/stable/gallery/` 웹사이트를 방문해 보시기 바랍니다.

In `matplotlib`, a plot consists of a _figure_ and one or more _axes_. You can think of the figure as the blank canvas upon which one or more plots will be displayed: it is the entire plotting window. The _axes_ contain important information about each plot, such as its $x$- and $y$-axis labels, title, and more. (Note that in `matplotlib`, the word _axes_ is not the plural of _axis_: a plot’s _axes_ contains much more information than just the $x$-axis and the $y$-axis.)

`matplotlib` 환경에서 그래프 객체는 하나의 커다란 _그림 틀(figure)_ 과 하나 이상의 _축(axes)_ 구간으로 구성됩니다. 여기서 그림 틀(figure)은 그 위에 여러 그래프들이 전시될 빈 도화지 캔버스로 생각하면 됩니다: 즉, 전체 윈도우 창 자체를 의미합니다. 한편 _축(axes)_ 은 $x$축과 $y$축의 라벨, 제목 등 개별 그래프 공간에 관한 중요한 정보들을 모두 담고 있습니다. (참고로, `matplotlib`에서 _axes_ 라는 단어는 단순히 _axis_ 의 복수형 명사를 뜻하지 않습니다: 객체의 _axes_ 영역은 단순한 $x$축과 $y$축 선반을 넘어서 그래프의 훨씬 더 많은 화면 정보 속성을 포함합니다.)

We begin by importing the `subplots()` function from `matplotlib`. We use this function throughout when creating figures. The function returns a tuple of length two: a figure object as well as the relevant axes object. We will typically pass `figsize` as a keyword argument. Having created our axes, we attempt our first plot using its `plot()` method. To learn more about it, type `ax.plot?`.

우선 `matplotlib` 패키지에서 `subplots()` 함수를 가져오는 것으로 시작하겠습니다. 이 함수는 그림을 새로 생성할 때 전반적으로 반복 사용됩니다. 함수를 실행하면 길이가 2인 튜플을 반환하는데, 하나는 그림(figure) 전체 객체이고 다른 하나는 관련된 축(axes) 통제 객체입니다. 일반적으로 그래프 크기를 정하기 위해 `figsize` 치수를 키워드 인수로 전달합니다. 축(axes) 객체를 생성하고 나면, 내부의 기본 `plot()` 메서드를 사용해 첫 번째 그래프 선분 그리기를 시도할 수 있습니다. 자세한 정보를 원한다면 명령어 `ax.plot?` 을 언제든 입력해 보십시오.

```python
In [39]: from matplotlib.pyplot import subplots
         fig, ax = subplots(figsize=(8, 8))
         x = rng.standard_normal(100)
         y = rng.standard_normal(100)
         ax.plot(x, y);
```

We pause here to note that we have _unpacked_ the tuple of length two returned by `subplots()` into the two distinct variables `fig` and `ax`. Unpacking is typically preferred to the following equivalent but slightly more verbose code:

여기서 잠시 주목할 점은, `subplots()` 가 반환한 길이가 2인 튜플의 결과물들을 우리가 `fig` 와 `ax` 라는 두 개의 개별 변수로 손쉽게 나누어 _언패킹(unpacked)_ 했다는 사실입니다. 이러한 언패킹 방식은 출력 결과는 같지만 다소 코드가 장황해지는 다음과 같은 일반 방식보다 실무에서 훨씬 더 많이 선호됩니다:

```python
In [40]: output = subplots(figsize=(8, 8))
         fig = output[0]
         ax = output[1]
```

We see that our earlier cell produced a line plot, which is the default. To create a scatterplot, we provide an additional argument to `ax.plot()`, indicating that circles should be displayed.

우리가 위에서 실행한 앞선 셀의 결과가 기본 설정인 선 그래프(line plot)로 그려졌음을 볼 수 있습니다. 만약 이를 점이 찍히는 산점도(scatterplot)로 만들고 싶다면, 동그라미(circle) 기호를 각 지점에 표시하라는 추가 인수를 아래처럼 `ax.plot()` 내부에 직접 제공하면 됩니다.

```python
In [41]: fig, ax = subplots(figsize=(8, 8))
         ax.plot(x, y, 'o');
```

Different values of this additional argument can be used to produce different colored lines as well as different linestyles. As an alternative, we could use the `ax.scatter()` function to create a scatterplot. 

이 추가 인수 위치에 지정된 문자와 다른 기호 값을 넣으면 선의 색상을 바꾸거나 선의 스타일 패턴을 각기 다르게 변경할 수도 있습니다. 또 다른 그에 대한 대안으로, 애초부터 `ax.scatter()` 함수 자체를 사용하여 단숨에 산점도를 직접 전용으로 생성할 수도 있습니다.

```python
In [42]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o');
```

Notice that in the code blocks above, we have ended the last line with a semicolon. This prevents `ax.plot(x, y)` from printing text to the notebook. However, it does not prevent a plot from being produced. If we omit the trailing semi-colon, then we obtain the following output:

위의 코드 블록들에서 우리가 항상 마지막 줄의 끝을 세미콜론(;) 문자로 굳이 마무리지었음에 주목하십시오. 이것은 `ax.plot(x, y)` 가 실행될 때 특정 객체 정보의 지저분한 텍스트가 화면 노트북에 함께 직접 출력되는 것을 깔끔히 방지합니다. 물론 텍스트만 가릴 뿐 그래프가 멀쩡히 그려지는 본원적 작동 자체를 막지는 않습니다. 만약 이 끝의 세미콜론을 생략해 버린다면, 우리는 다음과 같이 지저분한 텍스트 출력 문구가 위에 표시되는 것을 보게 됩니다:

```python
In [43]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o')
Out[43]: <matplotlib.collections.PathCollection at 0x7fb3d9c8f310>
```

In what follows, we will use trailing semicolons whenever the text that would be output is not germane to the discussion at hand. 

따라서 차후 앞으로 이어질 교육 내용에서도, 출력될 텍스트 정보 결과물이 우리가 현재 진행 중인 분석 논의와 별로 관련이 없을 경우에는 우리는 항상 코드 줄 끝에 통제용 세미콜론을 조달 붙일 것입니다.

To label our plot, we make use of the `set_xlabel()`, `set_ylabel()`, and `set_title()` methods of `ax`.

전개된 축 그래프에 축 이름을 명시해 붙이기 위해, 우리는 축 `ax` 객체가 지닌 `set_xlabel()`, `set_ylabel()`, 그리고 `set_title()` 메서드들을 차례차례 유용하게 사용합니다.

```python
In [44]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o')
         ax.set_xlabel("this is the x-axis")
         ax.set_ylabel("this is the y-axis")
         ax.set_title("Plot of X vs Y");
```

Having access to the figure object `fig` itself means that we can go in and change some aspects and then redisplay it. Here, we change the size from `(8, 8)` to `(12, 3)`.

`fig` 원형의 그림 뼈대 객체 그 자체에 언제든 주소 접근할 수 있다는 것은, 우리가 마음대로 임의로 접근해 일부 그래프 속성 설정을 원하는 대로 변경하고 뒤이어 동일한 그래프를 바뀐 설정으로 다시금 화면에 표시할 수 있음을 의미합니다. 여기서는 크기 설정을 기존의 `(8, 8)` 파라미터에서 기표 `(12, 3)` 수치로 변경해 봅니다.

```python
fig.set_size_inches(12, 3)
fig
```

Occasionally we will want to create several plots within a figure. This can be achieved by passing additional arguments to `subplots()`. Below, we create a $2 \times 3$ grid of plots in a figure of size determined by the `figsize` argument. In such situations, there is often a relationship between the axes in the plots. For example, all plots may have a common $x$-axis. The `subplots()` function can automatically handle this situation when passed the keyword argument `sharex=True`. The `axes` object below is an array pointing to different plots in the figure.

때때로 우리는 하나의 거대한 캔버스 그림 판 안에 여러 개의 작은 분할 그리드 그래프들을 한데 모아 생성하고 싶을 때가 있습니다. 이는 단순히 `subplots()` 함수에 단면 추가 인수를 전달하는 방식으로 간단히 달성 구동할 수 있습니다. 아래 코드에서는 `figsize` 인수로 전체 캔버스 크기를 정한 그림 판 통틀어 안에 $2 \times 3$ 그리드 격자 형태의 소규모 분할 그래프 구역들을 만듭니다. 이런 상황에서는 분할된 각각의 소규모 축들 그래프 사이에 일련의 연관 관계가 존재하는 경우가 많습니다. 예를 들어, 모든 분할 그래프 면적이 모조리 하단의 특정 $x$축 숫자를 위아래로 서로 공통되게 하나로 공유할 수 있습니다. `subplots()` 함수에 `sharex=True` 라는 특수 상태 키워드 인수를 함께 전달하면 함수가 이러한 축 병합 공유 상황을 알아서 자동으로 손쉽게 맞춤 처리해 줍니다. 아래 코드에 등장 선언되는 변수 `axes` 객체는 그림 판 내에 위치한 각기 서로 다른 격자 공간 구역의 소규모 그래프들을 1대1로 지칭 가리키는 관리 배열 구조입니다.

```python
In [45]: fig, axes = subplots(nrows=2,
                              ncols=3,
                              figsize=(15, 5))
```

We now produce a scatter plot with `'o'` in the second column of the first row and a scatter plot with `'+'` in the third column of the second row.

배열에 지정하여, 이제 우리는 캔버스의 첫 번째 행의 두 번째 열 배열 위치에 `'o'` 모양 기호를 가진 산점도를 구성해 특정하여 그리고, 두 번째 행의 세 번째 열 구역 위치에는 이와 다르게 `'+'` 모양을 갖춘 단면 산점도를 도출해 특정 전용 그립니다.

```python
In [46]: axes[0, 1].plot(x, y, 'o')
         axes[1, 2].scatter(x, y, marker='+')
         fig
```

Type `subplots?` to learn more about `subplots()`. To save the output of `fig`, we call its `savefig()` method. The argument `dpi` is the dots per inch, used to determine how large the figure will be in pixels.

함수 `subplots()` 동작에 대해 자세히 더 배우고자 궁금하다면 `subplots?` 를 콘솔에 입력하십시오. 저장 도출된 전체 `fig` 의 조달 결과 캔버스 그래프를 내부 컴퓨터 파일로 직접 영구 저장 보관하려면 자체 내부의 `savefig()` 메서드를 시스템 호출합니다. 여기서 `dpi` 인수는 1인치당 점의 개수를 의미하는 인치당 도트 수(dots per inch) 약자를 뜻하며, 실제 그림 이미지가 생성될 때 픽셀 단위로 해상도가 얼마나 세밀하게 크게 화질을 지닐지를 직접 통제 결정합니다.

```python
In [47]: fig.savefig("Figure.png", dpi=400)
         fig.savefig("Figure.pdf", dpi=200);
```

We can continue to modify `fig` using step-by-step updates; for example, we can modify the range of the $x$-axis, re-save the figure, and even re-display it.

우리는 코드의 단계적인 조작 업데이트를 사용하여 계속해서 객체 `fig` 를 화면 수정할 수 있습니다. 예를 들어 $x$축 기표가 나타나는 수치 범위를 수정하여 한정 자르고, 수정된 해당 그림을 다시 같은 이름의 파일로 덮어 재저장한 다음, 최종 노트북 화면에 그 조작된 그림을 명령으로 다시 띄워 전개 표시할 수 있습니다.

```python
In [48]: axes[0, 1].set_xlim([-1, 1])
         fig.savefig("Figure_updated.jpg")
         fig
```

We now create some more sophisticated plots. The `ax.contour()` method produces a _contour plot_ in order to represent three-dimensional data, similar to a topographical map. It takes three arguments:

이제 조금 더 복잡하고 정교한 고급 그래프들을 소개합니다. `ax.contour()` 메서드는 3차원 입체 데이터를 2차원 평면 위에 색상으로 표현하기 위해, 마치 지리 책의 지형도 산점 데이터와 유사한 방식의 특성 _등고선 그래프(contour plot)_ 를 시각화해 돌려 줍니다. 이 메서드는 필수적으로 아래 세 가지 핵심 지정 인수를 전달받습니다:

- A vector of `x` values (the first dimension),
- A vector of `y` values (the second dimension), and
- A matrix whose elements correspond to the `z` value (the third dimension) for each pair of `(x, y)` coordinates.

- `x` 기표 수치가 담긴 고유 배열 벡터 (첫 번째 차원축 구실),
- `y` 기표 수치가 담긴 고유 배열 벡터 (두 번째 차원축 구실), 그리고
- 각각의 모든 짝지은 쌍 `(x, y)` 표면 좌표 쌍에 정확히 매칭되어 위로 대응 솟아오르는 높이 `z` 고도 수치값 (세 번째 차원축 구실)을 요소로 갖춘 구조 배열 행렬.

To create `x` and `y`, we’ll use the command `np.linspace(a, b, n)`, which returns a vector of `n` numbers starting at `a` and ending at `b`.

데이터의 기저 바닥을 구성할 축 `x` 와 `y` 의 벡터 공간을 일정하게 생성 편하게 하기 위해, 우리는 앞서 파이썬 내장 명령어 `np.linspace(a, b, n)` 구문을 사용할 텐데, 이 명령어 구문은 기표 수치 `a` 시작점에서 시작해 도착 데이터 `b` 로 끝나는 구간 사이 내부를 아주 일정히 나눈 총 `n` 개의 간격 등분 숫자들의 벡터 덩어리 무리를 고스란히 돌려줍니다.

```python
In [49]: fig, ax = subplots(figsize=(8, 8))
         x = np.linspace(-np.pi, np.pi, 50)
         y = x
         f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
         ax.contour(x, y, f);
```

We can increase the resolution by adding more levels to the image.

이미지 위에 그릴 때 함수에 직접 더 수많은 층위별 등고선 선분 레벨 인수를 세밀히 더 추가 지정함으로써 화면 고저 해상도를 극상으로 한층 더 세밀히 높일 수 있습니다.

```python
In [50]: fig, ax = subplots(figsize=(8, 8))
         ax.contour(x, y, f, levels=45);
```

To fine-tune the output of the `ax.contour()` function, take a look at the help file by typing `?plt.contour`. The `ax.imshow()` method is similar to `ax.contour()`, except that it produces a color-coded plot whose colors depend on the `z` value. This is known as a _heatmap_, and is sometimes used to plot temperature in weather forecasts.

`ax.contour()` 함수의 시각 결괏값을 더욱 미세하게 내 입맛대로 세부 조율 통제하고 싶다면, 콘솔에 터미널 입력 `?plt.contour` 를 치고 튀어나온 도움말 상세 문서를 찬찬히 살펴 참조하십시오. 이와 대응하는 `ax.imshow()` 그림 메서드는 `ax.contour()` 선분 방식과 그 원리가 무척이나 근접 유사하지만, `z` 고도 높이 값의 강약 수준에 따라 색상을 선이 아닌 면적 자체에 다르게 적용해 칠한 색상 면적 코딩 척도 그래프를 화면에 그려낸다는 점이 유일한 차이점입니다. 이것은 통계 영역에서 일명 _히트맵(heatmap)_ 수리라고도 잘 알려져 있으며, 흔히 지상 일기 예보 시스템에서 기온 분포도 지표를 전국 단위로 플롯할 때 시각적으로 광범위하게 쓰입니다.

```python
In [51]: fig, ax = subplots(figsize=(8, 8))
         ax.imshow(f);
```

---

## Sub-Chapters (하위 목차)

현재 2.3.4 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)
