---
layout: default
title: "trans2"
---

[< 2.3.3 Introduction To Numerical Python](../2_3_3_introduction_to_numerical_python/trans2.html) | [2.3.5 Sequences And Slice Notation >](../2_3_5_sequences_and_slice_notation/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.4 Graphics
# 2.3.4 그래픽 시각화 (Matplotlib)

In `Python`, common practice is to use the library `matplotlib` for graphics.
전 세계 `Python` 데이터 과학자들 사이에서 그림을 그리거나 차트를 띄워야 할 때 묻지도 따지지도 않고 꺼내 드는 국민 도화지 라이브러리가 있습니다. 바로 `matplotlib` 입니다.

However, since `Python` was not written with data analysis in mind, the notion of plotting is not intrinsic to the language.
솔직히 말해 `Python` 이란 언어는 애초에 "우리 다 같이 데이터 분석을 해보자!" 하고 만들어진 게 아니었기 때문에, 태생적으로 파이썬 내장 쌩-얼굴 기능엔 무언가를 그리는(plotting) 예술적 유전자가 전혀 존재하지(intrinsic) 않습니다.

We will use the `subplots()` function from `matplotlib.pyplot` to create a figure and the axes onto which we plot our data.
그래서 우린 외부에서 그 유전자를 빌려옵니다! `matplotlib.pyplot` 이라는 기나긴 요술 지팡이 묶음 안에서 `subplots()` 함수를 꺼내, 우리가 빈 도화지(Figure) 한 장을 쫙 펴고 데이터를 무자비하게 투척할 좌표축(axes) 뼈대를 멋지게 생성해 보겠습니다.

For many more examples of how to make plots in `Python`, readers are encouraged to visit `matplotlib.org/stable/gallery/`.
참고로, `Python` 붓으로 얼마나 기가 막힌 피카소급 명작 차트 결괏물들을 찍어낼 수 있는지 직접 눈으로 목격하고 싶다면 다방면 공식 미술관인 `matplotlib.org/stable/gallery/` 에 직접 방문해 온갖 꼼수 기법들을 훔쳐 보시길 강력히 권장합니다.

In `matplotlib`, a plot consists of a _figure_ and one or more _axes_.
`matplotlib` 미술 교실의 핵심 법칙! 하나의 그럴싸한 그래프(plot)는 거대한 도화지 틀인 **_피겨(figure)_** 와, 실질적으로 물감을 칠하는 안쪽 네모난 좌표 틀 영역인 **_축상(axes)_** 하나 혹은 그 이상들의 치밀한 결합으로 구성되어 있습니다.

You can think of the figure as the blank canvas upon which one or more plots will be displayed: it is the entire plotting window.
피겨(figure)가 뭐냐고요? 텔레비전 껍데기 프레임 같은 겁니다. 하나 혹은 수십 개의 여러 차트 플롯들이 동시에 전시될 가장 밑바탕의 하얀 무지 빈 캔버스, 즉 윈도우 전체 창을 아우르는 물리적 배경(entire plotting window)이라 생각하시면 이해가 빠릅니다.

The _axes_ contain important information about each plot, such as its $x$- and $y$-axis labels, title, and more.
반면 **_축(axes)_** 들은 알맹이입니다. 이 캔버스 위에 그려지는 하나하나의 실물 차트 구역을 뜻하며, 밑바닥 $x$- 및 $y$-축 라벨 이름표기부터 차트의 지엄한 제목(title), 눈금 단위 등 핵심적인 시각 정보들을 모두 품고(contain) 지배하는 실세죠.

(Note that in `matplotlib`, the word _axes_ is not the plural of _axis_: a plot’s _axes_ contains much more information than just the $x$-axis and the $y$-axis.)
(영어 문법 깨알 팁! `matplotlib` 구역질 나는 단어장에서 _axes_ 라는 단어는 단순한 _axis_(가로축, 세로축 선 1개)의 복수형이 아닙니다! 차트 구역 전체를 통치하는 네모 박스 단위(Plot's axes)이므로, 선명한 데이터뿐만 아니라 그 테두리를 감싼 모든 부수 정보를 관리하는 광역 통제구역을 의미합니다.)

We begin by importing the `subplots()` function from `matplotlib`.
자, 거두절미하고 실전 돌입! 가장 먼저 서랍에서 `matplotlib` 물감을 뒤져 `subplots()` 그리기 함수부터 단연 빼내어(import) 가져와 보겠습니다.

We use this function throughout when creating figures.
앞으로 우리가 그림다운 그림(figures)을 생산할 찰나의 때마다 수만 번은 주야장천 계속 불러 쓸 함수니까 외워두세요.

The function returns a tuple of length two: a figure object as well as the relevant axes object.
이 요술 함수는 기특하게도 우리가 부르면 항상 무기 2개를 튜플(tuple) 소포 세트로 묶어서 반환합니다: 바로 빈 도화지 틀(figure object) 1장과 그림 그릴 네모 칸 공간(axes object) 1개 말이죠!

We will typically pass `figsize` as a keyword argument.
이때 우리는 스케치북 주문을 넣으며 전형적으로 "가로 8인치 세로 8인치로 좀 뽑아줘"란 의미로 `figsize` 란 열쇠말 옵션을 건네주곤(pass) 합니다.

Having created our axes, we attempt our first plot using its `plot()` method.
마침내 내 전용 그리기 도구(axes)를 품에 안았으니, 감격스러운 첫 선 긋기(`plot()` 메서드)를 데이터 위에 팍팍 시도해 보겠습니다.

To learn more about it, type `ax.plot?`.
이 붓질(plot)로 얼마나 다양한 기교를 부릴 수 있는지 설명서가 당기신다면 가볍게 `ax.plot?` 을 쳐보세요.

```python
In [39]: from matplotlib.pyplot import subplots
         fig, ax = subplots(figsize=(8, 8))
         x = rng.standard_normal(100)
         y = rng.standard_normal(100)
         ax.plot(x, y);
```

We pause here to note that we have _unpacked_ the tuple of length two returned by `subplots()` into the two distinct variables `fig` and `ax`.
여기서 잠깐 타임! 아까 `subplots()` 함수가 도화지와 그림 칸 쌍을 튜플 소포로 찍어 보낸다 했죠? 우리는 두 녀석을 동시에 뽁뽁이에서 강제로 찢어 _풀어헤쳐(unpacked)_ 각각 독립적인 이름을 지니게 `fig` 와 `ax` 변수로 가볍게 쏙쏙 갈라 받아 쥐어버렸습니다.

Unpacking is typically preferred to the following equivalent but slightly more verbose code:
사실 아래 예시처럼 주저리주저리 박스를 받아서 일일이 0번 인덱스, 1번 인덱스로 배분하는 무식하고 장황한(verbose) 낡고 등신 같은 코드보다, 방금 위에서 쓴 '풀어헤치기(unpacking 한 줄 배정)' 기법이 파이썬 코더들 사이에선 국룰로 선호됩니다.

```python
In [40]: output = subplots(figsize=(8, 8))
         fig = output[0]
         ax = output[1]
```

We see that our earlier cell produced a line plot, which is the default.
아까 그린 첫 결괏물을 가만히 보면, 점을 안 찍고 무식하게 선으로 모든 난수를 쭉쭉 미로처럼 이어 놨을 겁니다. 네, 아무 옵션 안 주고 `plot`만 부르면 밋밋한 꺾은 선 그래프(line plot)로 찍 긋는 게 저놈들의 기본값(default) 종특이거든요.

To create a scatterplot, we provide an additional argument to `ax.plot()`, indicating that circles should be displayed.
징그러운 실타래가 아니라 멋진 주근깨 같은 산점도(scatterplot) 도장을 찍고 싶으신가요? 아주 쉽습니다. `ax.plot()` 뒤꽁무니에다 동그라미(circle) 모양의 점을 찍어주길 지시하는 사소하지만 중요한 암호표 하나만 얹어 제공하면 끝장납니다.

```python
In [41]: fig, ax = subplots(figsize=(8, 8))
         ax.plot(x, y, 'o');
```

Different values of this additional argument can be used to produce different colored lines as well as different linestyles.
이 끝자락 알파벳 암호(`'o'`, `'-'`, `'--'`, `'r'` 등) 하나로 점 모양은 물론이고 빨주노초 색깔 선부터 점선 형태까지 카멜레온처럼 별의별 스타일(linestyles)의 시각 예술을 마음껏 창조해 낼 수 있단 말씀!

As an alternative, we could use the `ax.scatter()` function to create a scatterplot.
아니면 꼼수 쓰지 말고 정석대로, 오롯이 점만 전문으로 촵촵 찍어내는 전용 함수인 `ax.scatter()` 를 듬직하게 쓰는 게 더 나은 대안(alternative)일 수도 있습니다.

```python
In [42]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o');
```

Notice that in the code blocks above, we have ended the last line with a semicolon.
눈썰미가 매의 눈이신가요? 아까 위쪽 파이썬 소스 코드 박스들의 맨 마지막 줄 끝자락에, 뭔가 기분 나쁘게 작은 땀방울, 즉 세미콜론(`;`) 부호가 찝찝하게 붙어 끝났다는 걸 혹시 눈치채셨습니까?

This prevents `ax.plot(x, y)` from printing text to the notebook.
파이썬은 말 많은 아우라지여서 그림 그릴 때 항상 좌표나 객체 이름표기 같은 거추장스러운 "텍스트 메모리 주소"를 주피터 창에 주절주절 함께 토해냅니다. 바로 저 마법의 세미콜론이 파이썬의 입을 꽉 틀어막아(prevents) 못생긴 텍스트 문구가 화면에 쏟아지는 걸 기가 막히게 원천 차단해주죠.

However, it does not prevent a plot from being produced.
근데 입을 막는다고 손까지 불구가 되진 않죠! 그림 자체를 뿜어져 나오게 그리는 행위(plot being produced) 만큼은 방해하지 않고 묵묵히 놔둡니다. 깔끔하죠!

If we omit the trailing semi-colon, then we obtain the following output:
만일 우리가 뒤꽁무니의 세미-콜론(`;`) 부호를 실수로 빼먹어(omit) 버리면, 파이썬 입을 못 막아서 아래처럼 되도 않는 이상한 기계어 메모리 텍스트 출력물 하나를 덤으로 얻게 될 겁니다:

```python
In [43]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o')
Out[43]: <matplotlib.collections.PathCollection at 0x7fb3d9c8f310>
```

In what follows, we will use trailing semicolons whenever the text that would be output is not germane to the discussion at hand.
앞으로 우리가 이어갈 모든 코딩 예제들에서, 당면한 논의 흐름과 딱히 상관도 없이 저런 쓰레기 기계어 텍스트 문건들이 눈살을 찌푸리게 끼어들 우려가 있는 모든 귀찮은 상황마다 주야장천 세미콜론을 써서 입막음에 나설 겁니다.

To label our plot, we make use of the `set_xlabel()`, `set_ylabel()`, and `set_title()` methods of `ax`.
자, 차트가 벌거벗은 민둥산 같습니다. 가로축/세로축 이름도 달아주고 멋들어진 차트 위 대문짝 제목 표찰을 달아 이정표(label)를 꽂아주려면 `ax` 도구함의 `set` 시리즈 3대장 메서드들을 요긴하게 사용 조치하면 됩니다.

```python
In [44]: fig, ax = subplots(figsize=(8, 8))
         ax.scatter(x, y, marker='o')
         ax.set_xlabel("this is the x-axis")
         ax.set_ylabel("this is the y-axis")
         ax.set_title("Plot of X vs Y");
```

Having access to the figure object `fig` itself means that we can go in and change some aspects and then redisplay it.
아까 튜플 풀기 공법으로 외곽 도화지 변수인 피겨(figure) 객체 즉 `fig` 의 통제권을 우리가 확보해 두었단 사실은 실로 엄청난 기행을 가능하게 합니다. 그림을 다 그린 뒤에도 언제든 본진 도화지 설정 내부로 잠입해 틀을 찢고 비율 측면(aspects)을 조작 변경한 뒤 다시 송출(redisplay)해 버릴 수 있단 뜻이죠.

Here, we change the size from `(8, 8)` to `(12, 3)`.
까짓것, 지금 여기서 도화지 비율을 애초 정사각형 `(8, 8)` 체형에서 뱀처럼 날씬하고 길쭉한 `(12, 3)` 직사각형 비율로 확 바꿔쳐 보겠습니다.

```python
In [45]: fig.set_size_inches(12, 3)
         fig
```

Occasionally we will want to create several plots within a figure.
어쩌다 보면 한 장의 거대한 벽면 캔버스(피겨) 도화지 안에 소형 플롯(미니 차트) 여러 장을 액자처럼 오밀조밀 모아 넣고 모둠 갤러리를 구축해 만들고 싶을 때가 짜릿하게 생깁니다.

This can be achieved by passing additional arguments to `subplots()`.
이건 도화지 여백을 나눌 때 `subplots()` 초기 생성 주문에 "도마 좀 썰어 줘"라는 의미의 부가적인 추가 요청 옵션 인자들을 꽂아 넘김으로써 아주 손쉽게 목표 성취 달성될 수 있죠.

Below, we create a $2 \times 3$ grid of plots in a figure of size determined by the `figsize` argument.
그리하여 아래에 등장할 마법! 우리는 `figsize` 로 체형을 지목해 만든 널찍한 도화지 한 장 안에, 가로 3칸 세로 2칸짜리로 깔끔하게 쪼개진 아파트 창문 격자 모양의 $2 \times 3$ 그리드(grid) 차트 단지 구역을 분양 생성해 내 보겠습니다.

In such situations, there is often a relationship between the axes in the plots.
이런 다중 격자 구역 상황에 직면하면요, 각 구역의 미니 차트 도구(axes)들 사이에는 서로 형제애처럼 하나의 깊은 축 공유 공생 관계성(relationship)이 은밀히 존재하기도 합니다.

For example, all plots may have a common $x$-axis.
가령 예를 들어, 6개의 크고 작은 미니 차트들이 전부 다 밑바닥 거대 X축 눈금 하나(common x-axis)를 똑같이 복제해 공유 쓰는 상황이 터질 수도 있죠.

The `subplots()` function can automatically handle this situation when passed the keyword argument `sharex=True`.
이때 집주인 `subplots()` 함수에게 몰래 `sharex=True`라는 삐삐(키워드 인자) 하나만 패스쳐 몰래 구문 전달해 주면, 저 복잡한 X축 공용 배분 상황을 함수 스스로 뒤에서 알아서 은밀하게 모두 컨트롤(handle) 해결해버립니다. 편하죠?

The `axes` object below is an array pointing to different plots in the figure.
참고로 치밀하게! 아래에서 우리가 받아쥔 `axes` 변수는 그냥 변수가 아니라 아까 쪼개 놓은 6개의 독립 미니 플롯 구역들의 정확한 건물 동/호수 좌표 위치를 각각 콕콕 가리키는 파워 배열(Array) 시스템입니다.

```python
In [45]: fig, axes = subplots(nrows=2,
                              ncols=3,
                              figsize=(15, 5))
```

We now produce a scatter plot with `'o'` in the second column of the first row and a scatter plot with `'+'` in the third column of the second row.
말 나온 김에, 배열 시스템 동/호수에 맞춰 저 넓은 빌라 단지 안에 딱 두 놈만 선별해서 입주시킬까요? 무조건 첫 번째 층의 두 번째 방 타일 위에 거대 동그라미 `'o'` 산점도를 입주시키고, 곧장 두 번째 행 아랫집의 세 번째 구석방 유리창 엔 날 선 십자가 `'+'` 표식 산점도를 무단 입주시켜 생산 산출시켜 보겠습니다.

```python
In [46]: axes[0, 1].plot(x, y, 'o')
         axes[1, 2].scatter(x, y, marker='+')
         fig
```

Type `subplots?` to learn more about `subplots()`.
마법의 공간 분할 주문 `subplots()` 의 숨겨진 기능들을 더 깊이 있게 폭넓게 탈탈 털어 알고 싶다면, 주저 없이 `subplots?` 구문을 타이핑해 지식 사냥을 떠나시길!

To save the output of `fig`, we call its `savefig()` method.
자, 이렇게 영혼 탈곡하며 예쁘게 피땀 흘려 그린 명작 `fig` 그림 도화지를 휘발되게 날려 먹긴 아깝죠? 하드디스크에 영구 박제(저장)하려면 그것의 전속 도구인 `savefig()` 저장 버튼 메서드를 가볍게 호출하면 됩니다.

The argument `dpi` is the dots per inch, used to determine how large the figure will be in pixels.
저장할 때 들어가는 옵션 파라미터 `dpi` 요 놈의 정체는 '1인치 안에 도트(점)를 몇 개나 처박아 드릴까(dots per inch)?'를 설정하는 화질 척도입니다. 즉, 내 픽셀 해상도를 얼마나 눈부시게 키워 대형 화면으로 볼 수 있을지를 섬세하게 통제 결정하죠.

```python
In [47]: fig.savefig("Figure.png", dpi=400)
         fig.savefig("Figure.pdf", dpi=200);
```

We can continue to modify `fig` using step-by-step updates; for example, we can modify the range of the $x$-axis, re-save the figure, and even re-display it.
그림 그리는 여정은 아직 안 끝났습니다! 저장 버튼 눌렀다고 못 바꾸냐? 천만에요. 우리는 방금 저장한 그 캔버스 `fig` 모델을 그대로 들고 단계-별 업데이트 조작(step-by-step updates)을 먹여서 쪼물딱 계속 변형 수리해 나갈 수 있습니다. 가령 맘에 안 드는 $x$-축의 구간 커버리지를 가차 없이 자르고 늘려 강제로 수정하고, 훗 맘에 들군 하며 피겨를 거듭 재-저장(re-save)할 수 있으며 심지어 화면에 또 띄워(re-display) 감상할 수조차 있는 극강의 재탕 유연성을 자랑합니다.

```python
In [48]: axes[0, 1].set_xlim([-1, 1])
         fig.savefig("Figure_updated.jpg")
         fig
```

We now create some more sophisticated plots.
애들 장난 같은 점 찍기는 이만 접고, 이제 조금 더 있어 보이고 고오급진 입체형의 3차원적 정교한 차트 폭격(sophisticated plots)을 창조해 띄워 보겠습니다.

The `ax.contour()` method produces a _contour plot_ in order to represent three-dimensional data, similar to a topographical map.
산에 등산 가면 흔히 보는 지형도 지도 아시죠? 그게 바로 3차원의 복잡한 데이터들을 2차원 화면 속에 멋들어지게 찍어누르고 굴곡을 나타내는 **_등고선 플롯(contour plot)_** 입니다. 바로 위대한 `ax.contour()` 메서드가 이걸 생산 담당합니다!

It takes three arguments:
이 등고선 공장을 가동하려면 컨베이어 벨트에 딱 세 가지 핵심 재료 구조(인수)를 갖다 무자비하게 던져 넣어야 합니다:

- A vector of `x` values (the first dimension),
- X축을 깔아줄 지반, `x` 값 덩어리 벡터 체계 (첫 번째 차원 단락 축),

- A vector of `y` values (the second dimension), and
- Y축을 쫙 뻗어 올릴 수직 기둥, `y` 값들의 벡터 덩어리 지주 (두 번째 차원 면모 축), 그리고

- A matrix whose elements correspond to the `z` value (the third dimension) for each pair of `(x, y)` coordinates.
- 대망의 마지막 하늘방향. 저 `x, y` 두 좌표가 크로스 만나는 바둑판 교차점들(pair) 바닥 하나하나 치수마다 수직으로 치솟을 높이(`z`값) 체계에 상응해 조응하는 거대한 통짜 판때기 행렬 매트릭스(세 번째 조작 차원 높낮이 지표)! 이렇게 3개가 풀 세트입니다.

To create `x` and `y`, we’ll use the command `np.linspace(a, b, n)`, which returns a vector of `n` numbers starting at `a` and ending at `b`.
밑바닥 격자를 깔 `x` 와 `y` 재료를 손쉽게 공수해 오기 위해 파이썬 전용 칼잡이 명령어 `np.linspace(a, b, n)` 을 써보겠습니다. 요놈은 시작점 `a` 와 끝점 `b` 구간 사이의 공간을 정확무오하게 칼로 내리쳐서 무려 똑같은 등분 간격 `n` 조각 수치들로 쫙 무썰듯 쪼개 썰어내 반환해 치우는 진정한 살인 도구이자 마법 지팡이입니다.

```python
In [49]: fig, ax = subplots(figsize=(8, 8))
         x = np.linspace(-np.pi, np.pi, 50)
         y = x
         f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
         ax.contour(x, y, f);
```

We can increase the resolution by adding more levels to the image.
우와 그림이 나왔는데 등고선 선이 너무 듬성듬성 별로라고요? 옵션 끈(`levels=`)을 살짝 조여 차트 이미지 위에 등고선 절단 층수 두께(levels)를 촘촘히 왕창 더하면 미친 듯이 징그러울 정도의 극강의 고화질 해상도(resolution)를 시야로 만끽 증가시킬 수 있습니다.

```python
In [50]: fig, ax = subplots(figsize=(8, 8))
         ax.contour(x, y, f, levels=45);
```

To fine-tune the output of the `ax.contour()` function, take a look at the help file by typing `?plt.contour`.
저 무지막지한 등고선 공장 시스템 `ax.contour()` 결과물을 내 입맛에 맞게 살살 어르고 달래가며 더 정교하게 미세-조정(fine-tune)하는 오타쿠짓을 계속 즐기고프다면, `?plt.contour` 란 주문을 치고 도우미 마법사 설명서 브로슈어나 구석구석 훑어 정독해 보시길!

The `ax.imshow()` method is similar to `ax.contour()`, except that it produces a color-coded plot whose colors depend on the `z` value.
한술 더 뜰까요? 등고선(`contour`)과 친척 뻘 쌍둥이인 열화상 카메라 `ax.imshow()` 란 녀석이 있습니다. 이놈은 등고선 선 긋기 노가다는 피하되, 그 대신 산 꼭대기(`z` 변수 체계)가 높으면 빨갛게, 계곡이 깊으면 퍼렇게 빔을 쏴서 전 구역 픽셀을 온도 지도 색상 코드(color-coded)로 페인팅해서 화려한 조명 플롯을 거둔다는 오직 이 화려한 하나의 시각적 사실 조작 기능만을 빼면 기존 놈과 매우 판박이로 유사 작동합니다.

This is known as a _heatmap_, and is sometimes used to plot temperature in weather forecasts.
네, 맞습니다! 이게 바로 그 유명한 일명 **_히트맵(heatmap·열 지도)_** 이라 통용되어 불리는 녀석이며, 옛날 옛적 저녁 9시 뉴스 주간 야간 일기예보 체제 방송에서 모름지기 기상 캐스터 누나 뒤로 체감 온도가 벌겋고 시퍼렇게 플로팅(그려져) 나와 우리를 압도하던 바로 그 그래픽의 원조이기도 합니다.

```python
In [51]: fig, ax = subplots(figsize=(8, 8))
         ax.imshow(f);
```

---

## Sub-Chapters

[< 2.3.3 Introduction To Numerical Python](../2_3_3_introduction_to_numerical_python/trans2.html) | [2.3.5 Sequences And Slice Notation >](../2_3_5_sequences_and_slice_notation/trans2.html)
