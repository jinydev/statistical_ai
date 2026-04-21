---
layout: default
title: "trans2"
---

[< 2.3.8 For Loops](../2_3_8_for_loops/trans2.html) | [2.4 Exercises >](../../2_4_exercises/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.9 Additional Graphical and Numerical Summaries
# 2.3.9 부가적인 그래픽 보너스 및 수치적 요약 기술들

We can use the `ax.plot()` or `ax.scatter()` functions to display the quantitative variables.
우리는 앞에서 맛봤던 기본기인 `ax.plot()` 선 긋기나 `ax.scatter()` 점 찍기 함수들을 조작 사용해서 우리가 방금 세로로 세워 뽑았던 그 수치형 양적 변수(quantitative variables) 기둥들을 캔버스에 화려하게 표시할 수 있습니다.

However, simply typing the variable names will produce an error message, because `Python` does not know to look in the `Auto` data set for those variables.
그러나 여기서 초보들의 단골 실수! 만약 당신이 텅 빈 허공 캔버스에 대고 단순하게 `horsepower` 나 `mpg` 라는 기둥 변수 이름들만 당당하게 타이핑한다면 즉각 참혹한 에러 메시지를 생산해 마주하게 될 것입니다. 왜냐고요? 멍청한 `Python` 은 당신이 말한 그 단어가 저 멀리 주차된 `Auto` 데이터 세트 컨테이너 속을 헤집어 보아야만 겨우 찾을 수 있는 이름임을 전혀 알지 못하기 때문이죠.

```python
In [101]: fig, ax = subplots(figsize=(8, 8))
          ax.plot(horsepower, mpg, 'o');
NameError: name 'horsepower' is not defined
```

We can address this by accessing the columns directly:
우리는 이 멍청한 불상사를, 파이썬의 뒤통수를 치듯 열들의 정확한 주소망(`Auto` 뱃속의 것임을 명시)을 직접적으로 무단 접근해 불러줌으로써 시원하게 부르고 해결(address)할 수 있습니다:

```python
In [102]: fig, ax = subplots(figsize=(8, 8))
          ax.plot(Auto['horsepower'], Auto['mpg'], 'o');
```

Alternatively, we can use the `plot()` method with the call `Auto.plot()`.
하지만 매번 `Auto` 를 반복해 쓰긴 혀가 기니까 대안으로서! 아예 거대 원본 데이터 프레임 컨테이너 자체에 전속된 `Auto.plot()` 내장 호출기와 함께 내부 편의 `plot()` 메서드를 다이렉트로 써재낄 수도 있습니다.

Using this method, the variables can be accessed by name.
이 편의점급 숏컷 메서드를 시원하게 사용해서, 그 안의 미세 변수들은 마치 자기 집 안방인 양 간판 이름(`'horsepower'`, `'mpg'`)만으로도 아주 가볍게 수색 및 접근되어질 수 있습니다.

The plot methods of a data frame return a familiar object: an axes.
참고로 데이터 프레임에 전속 딸린 그 자체 플롯(plot) 메서드 도구들은 임무를 마치면 결국 우리에게 아주 친숙한 녀석 하나를 배달해 반환합니다: 바로 앞 단락들에서 지겹게 봐온 그 네모난 그림 영역 세팅기, 하나 단원의 축들(axes) 객체 말입니다.

We can use it to update the plot as we did previously:
그래서, 우리가 이전에 했던 것처럼 돌려받은 그 축 박스(`ax`) 객체를 다시 조물딱거려 그 플롯에 마법의 제목을 달거나, 스펙을 업데이트하기 위해 여느 때와 다름없이 그것을 이어서 사용할 수 있습니다:

```python
In [103]: ax = Auto.plot.scatter('horsepower', 'mpg')
          ax.set_title('Horsepower vs. MPG');
```
(이로써 훨씬 문장이 짧고 우아해졌죠?)

If we want to save the figure that contains a given axes, we can find the relevant figure by accessing the `figure` attribute:
이제 그림을 다 그렸고, 우리가 그 주어진 네모 축들(axes)이 매달려 기생하는 거대 캔버스 도화지 전체인 피겨(figure) 자체를 저장 액자로 뽑아버리기를 원한다면? 우리는 `ax` 가 품고 있는 속성 단추 중 `figure` 스위치에 역추적 접근함에 의하여 부모 격인 그 관련 도출 피겨를 단박에 역으로 거슬러 찾을 수 있습니다:

```python
In [104]: fig = ax.figure
          fig.savefig('horsepower_mpg.png');
```

We can further instruct the data frame to plot to a particular axes object.
우리는 나아가 이 건방진 데이터 프레임 화물차에게 "네 멋대로 도화지 깔지 말고, 내가 여기 지정해 둔 특정 캔버스 구역 축들(axes) 객체 위에다가만 딱 강제로 플롯으로 찍어 그려라!"라고 표적 지시할 수조차 있습니다.

In this case the corresponding `plot()` method will return the modified axes we passed in as an argument.
이 통제된 경우, 덩달아 해당하는 `plot()` 메서드는 반항 없이 우리가 구역 인자(ax=)로서 강제 할당해 건네 전달한 바로 그 표적 수정된 축들 영역 자체를 얌전히 순응해 반환할 것입니다.

Note that when we request a one-dimensional grid of plots, the object `axes` is similarly one-dimensional.
방금 조치에 따라, 우리가 1차원의 한 줄짜리 단면 플롯들의 분할 그리드 아파트(예: 3칸짜리 가로 건물)를 요청해 깔아버릴 때, 우리에게 던져지는 객체 `axes` 는 그 안의 3개의 방위치를 순서대로 담은 유사한 1차원 배열표라는 점에 단연 조목 주목하십시오.

We place our scatter plot in the middle plot of a row of three plots within a figure.
우리는 하나의 거대한 피겨(figure) 창문 안, 세 개의 연속 생성된 플롯들의 행 나열 중 한가운데 정중앙 플롯 방 구역, 즉 1번방(`axes[1]`) 안에 우리의 명작 산점도(scatter plot)를 무자비하게 욱여넣어 배치 배정합니다.

```python
In [105]: fig, axes = subplots(ncols=3, figsize=(15, 5))
          Auto.plot.scatter('horsepower', 'mpg', ax=axes[1]);
```

Note also that the columns of a data frame can be accessed as attributes: try typing in `Auto.horsepower`.
또 하나 파이썬의 신묘한 단축키 팁! 데이터 프레임 컨테이너의 등뼈인 열(columns) 기둥들은 굳이 대괄호를 안 쓰고도 점 하나 찍고 마치 내장 속성(attributes) 단추를 누르는 것처럼도 다이렉트 접근되어질 수 있음에 주목하십시오: 믿기지 않는다면 대괄호를 버리고 당장 `Auto.horsepower` 란 코드를 타이핑해 넣기를 시도해 결정을 구경 보십시오.

We now consider the `cylinders` variable.
우리는 이제 자동차의 엔진 실린더 수치를 담은 `cylinders` 변수 녀석의 상태를 점검 고려합니다.

Typing in `Auto.cylinders.dtype` reveals that it is being treated as a quantitative variable.
스캔 코드 `Auto.cylinders.dtype` 을 타입하여 스위치를 켜는 것은, 그 실린더 녀석이 단순한 연속 숫자인 양적 변수(quantitative variable)로서 무식하게 다루어지고 있음을 여실히 세상에 드러냅니다. (사실 4기통, 6기통, 8기통 등 종류별 계급인데 말이죠!)

However, since there is only a small number of possible values for this variable, we may wish to treat it as qualitative.
그러나! 솔직히 이 변수에 대해서 발현 가능한 값들의 숫자가 3기통~8기통 등 오직 자잘하고 작은 몇 안 되는 수로 한정되어 존재하기 때문에, 우리는 이것을 단순 무식한 연속형 숫자가 아니라 질적(qualitative) 등급 계급 즉 카테고리(범주형)로서 이 기둥을 전격 대우 다루기를 간절히 바랄 수 있고 또 그래야만 합니다.

Below, we replace the `cylinders` column with a categorical version of `Auto.cylinders`.
그리하여 아래에 등장할 조치에서, 우리는 무식한 기존 `cylinders` 기둥렬을 뽑아버리고 그 자리를 범주형 버전으로 싹 등급화 개조된 성형 버전의 `Auto.cylinders` 타운으로 말끔 대체시킵니다.

The function `pd.Series()` owes its name to the fact that `pandas` is often used in time series applications.
이때 돌연 호출되는 1차원 데이터 주조기, 파워 함수 `pd.Series()` 의 이름 구조에 얽힌 일화는, 해당 `pandas` 도구가 주식 차트 같은 시계열(time series) 적용들 안에서 종종 주름잡아 사용된다는 치명적 사실 단면에 큰 빚을 지고 파생되어 지어졌다는 무용담입니다.

```python
In [106]: Auto.cylinders = pd.Series(Auto.cylinders, dtype='category')
          Auto.cylinders.dtype
```
(자, 이제 속성 스위치(`dtype='category'`)를 강제로 끼워 넣어서 계급으로 승급된 겁니다!)

Now that `cylinders` is qualitative, we can display it using the `boxplot()` method.
마침내 우리의 `cylinders` 녀석은 어엿한 카테고리 등급, 질적 통계 요소가 되었습니다. 그러므로! 이제 우리는 이 등급별 칸막이를 활용해, 데이터의 배를 가르고 각 계층별 평균과 분포를 잔인하게 일렬로 까뒤집어 보여주는 통계학의 꽃 **`boxplot()` 상자수염그림 메서드**를 사용하여 그것을 당당히 디스플레이 표시할 수 있습니다.

```python
In [107]: fig, ax = subplots(figsize=(8, 8))
          Auto.boxplot('mpg', by='cylinders', ax=ax);
```
('by=실린더'를 넣었으니, 실린더 기통 수 계급별로 연비(mpg)의 분포 뼈가 적나라하게 상자그림으로 쪼개져 나옵니다!)

The `hist()` method can be used to plot a _histogram_.
통계 요약의 또 다른 묘수! 그 유명한 막대그래프 뭉치인 기초 함수 `hist()` 메서드 구문은 해당 구간들의 숫자가 얼마나 많이 몰려있는지 탑 쌓기를 하는 하나의 **_히스토그램(histogram)_** 을 웅장하게 그리기 위해 아주 쏠쏠하게 사용될 수 있습니다.

```python
In [108]: fig, ax = subplots(figsize=(8, 8))
          Auto.hist('mpg', ax=ax);
```

The color of the bars and the number of bins can be changed:
당연히, 쌓아 올린 히스토그램 막대들의 화려한 색상 껍질 스킨이나, 밑바닥 구획을 몇 개 통(bin)으로 잘게 쪼개 세울지 빈(bin)들의 옵션 개수는 입맛대로 철저히 통제 변경되어질 수 있습니다:

```python
In [109]: fig, ax = subplots(figsize=(8, 8))
          Auto.hist('mpg', color='red', bins=12, ax=ax);
```
(막대를 12개 통으로 쪼개서 새빨간 색으로 다시 칠해버렸습니다!)

See `Auto.hist?` for more plotting options.
이 히스토그램 건축의 더 다채롭고 사악한 많은 플롯 세공 옵션들을 알고 싶다면 당장 명령 줄 기기에 `Auto.hist?` 를 타건해 도움말 문서를 까 뒤져보십시오.

We can use the `pd.plotting.scatter_matrix()` function to create a _scatterplot matrix_ to visualize all of the pairwise relationships between the columns in a data frame.
자, 스케일 한 번 키워 볼까요! 우리는 파이썬의 거대 폭격 함수 `pd.plotting.scatter_matrix()` 지휘 기능 단락을 거두어 사용하여, 개별 데이터 프레임 컨테이너 배 안에서 같이 뒹구는 모든 변수 열(기둥)들 간의 치밀한 1:1 순서쌍 얽힌 관계성의 모두를 한 캔버스에 무자비하게 시각화하여 폭격하기 위해, 하나의 경이로운 그물 무늬 예술 **_산점도 매트릭스(scatterplot matrix) 종합 차트판_** 생성이라는 위대한 목적을 능히 이뤄낼 도구로 이를 가감 사용할 수 있습니다.

```python
In [110]: pd.plotting.scatter_matrix(Auto);
```
(명령어 한 줄에 바둑판처럼 펼쳐진 어마어마한 양의 전수조사 산점도 매트릭스가 쏟아져 내립니다!)

We can also produce scatterplots for a subset of the variables.
물론 너무 넓어서 눈이 아프다면, 우리는 또한 수많은 기둥 녀석들 중 내가 점 찍은 딱 몇몇 변수 타깃들의 한 부분 집합 결성 연맹체만을 위한 타깃 지목 산점도들을 소폭 도출해 축소 생성 산출할 수단도 지닙니다.

```python
In [111]: pd.plotting.scatter_matrix(Auto[['mpg',
                                           'displacement',
                                           'weight']]);
```

The `describe()` method produces a numerical summary of each column in a data frame.
그림 말고 숫자 보고서가 필요하신가요? 판다스의 핵심, 데이터 요약 비서인 그 치명적인 `describe()` 메서드를 호출하면! 녀석은 눈 깜짝할 새 데이터 프레임 안의 각 열 기둥에 대한 온갖 통계 수치(평균, 최소 분포 수치 등)가 일목요연 정리 담긴 하나의 파워풀한 데이터 수치적 요약(numerical summary) 보고서 서류를 번쩍 생성해 산출합니다.

```python
In [112]: Auto[['mpg', 'weight']].describe()
```

We can also produce a summary of just a single column.
이 요약 비서에게 여러 명이 아니라 우리는 덤으로 또한 그저 단일 구획의 외톨이 열 단 하나 기둥만의 특정 독립 요약 스펙을 독단 산출해 도출할 수도 있습니다.

```python
In [113]: Auto['cylinders'].describe()
          Auto['mpg'].describe()
```

To exit `Jupyter`, select `File / Close and Halt`.
길고 길었던 파이썬 랩(Lab) 지옥문을 닫기 직전이군요. 지긋지긋한 `Jupyter` 노트북 창 환경을 완전히 끊고 무사 종료 탈출하기 위해, 상단 메뉴에서 `File / Close and Halt` 명령 버튼 줄기를 눌러 가볍게 선택해 전원 코드를 뽑고 이탈하십시오. 수고하셨습니다!

---

## Sub-Chapters

[< 2.3.8 For Loops](../2_3_8_for_loops/trans2.html) | [2.4 Exercises >](../../2_4_exercises/trans2.html)
