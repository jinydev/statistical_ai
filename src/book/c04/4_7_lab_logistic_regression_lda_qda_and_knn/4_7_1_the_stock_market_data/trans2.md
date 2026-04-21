---
layout: default
title: "trans2"
---

[< 4.7 Lab Logistic Regression Lda Qda And Knn](../trans2.html) | [4.7.2 Logistic Regression >](../4_7_2_logistic_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.1 The Stock Market Data
# 4.7.1 Smarket 주식 데이터: 살벌한 월스트리트 주가 예측 구역 입장!

In this lab we will examine the `Smarket` data, which is part of the `ISLP` library. This data set consists of percentage returns for the S&P 500 stock index over 1,250 days, from the beginning of 2001 until the end of 2005. For each date, we have recorded the percentage returns for each of the five previous trading days, `Lag1` through `Lag5`. We have also recorded `Volume` (the number of shares traded on the previous day, in billions), `Today` (the percentage return on the date in question) and `Direction` (whether the market was `Up` or `Down` on this date).
드디어 기다리던 실전 랩(Lab) 코딩 연습장의 첫 무대에 올랐습니다. 이 구역에선 전설의 `ISLP` 라이브러리 안에 숨겨진 진짜배기 야생 데이터인 **`Smarket` 주식 데이터 뭉치**를 해부할 예정입니다. 이 데이터 보따리는 2001년 새해 아침부터 2005년 연말 종소리가 울릴 때까지 장장 1,250일 동안 피 튀기게 오르락내리락한 미국 S&P 500 주식 시장의 살벌한 '일일 백분율 수익률(percentage returns)' 기상도 역사를 담고 있습니다. 무기로 쓸 데이터 속 열(Column)들을 하나씩 까보면, 각 날짜마다 어제, 그제, 엊그제 등등 **과거 5일 치 거래일 동안의 뼈아픈 수익률 행적을 꼬리표처럼 달아놓은 `Lag1`부터 `Lag5`까지의 힌트 변수**들이 도열해 있죠. 그리고 덤으로 어제 터진 억 단위 총 주식 거래량 덩치인 `Volume`, **"그래서 오늘 결국 타깃 수익률은 얼마였는데?"** 하고 정답을 알리는 `Today`, 그리고 피날레 결론으로 오늘 장이 상승장 떡상이었는지(`Up`) 하락장 떡락이었는지(`Down`)를 박제해 놓은 궁극의 분류 과녁판 `Direction` 이라는 영광의 정답 변수까지 살뜰하게 전부 기록되어 있습니다.

We start by importing our libraries at this top level; these are all imports we have seen in previous labs.
코딩의 밥줄이자 시작, 우리의 든든한 파이썬 장비 도구함(라이브러리) 들을 맨 꼭대기 옥상에 세팅해 놓고 출격합니다. 이것들은 지난 랩 실습 구역에서 이미 눈도장을 쾅쾅 찍어뒀던 아주 익숙하고 시시한 단골 손님들입니다.

```python
In [1]: import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots
import statsmodels.api as sm
from ISLP import load_data
from ISLP.models import (ModelSpec as MS,
                         summarize)
```

We also collect together the new imports needed for this lab.
거기다 이번 뉴 페이스 분류 배틀 로얄을 위해 새롭게 공수해 온 최신식 라이브러리 무기들도 한가득 옆에 챙겨둡니다.

```python
In [2]: from ISLP import confusion_table
from ISLP.models import contrast
from sklearn.discriminant_analysis import     (LinearDiscriminantAnalysis as LDA,
     QuadraticDiscriminantAnalysis as QDA)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
```

Now we are ready to load the `Smarket` data.
장비 셋업 끝! 이제 본격적으로 도마 위에 저 `Smarket` 데이터를 불러와 얹어봅시다.

```python
In [3]: Smarket = load_data('Smarket')
Smarket
```

This gives a truncated listing of the data, which we do not show here. We can see what the variable names are.
이 명령어를 때리면 위아래가 살짝 뭉텅 잘려 나간 채 엑셀 표 같은 데이터의 단면이 출력되는데, 여백이 부족하니 시시한 출력물은 굳이 여기에 도배하지 않고 넘깁니다. 대신 이 표에 어떤 변수 기둥 이름들이 달렸는지만 살짝 까서 정찰해 보죠.

```python
In [4]: Smarket.columns
```

```python
Out[4]: Index(['Year', 'Lag1', 'Lag2', 'Lag3', 'Lag4', 'Lag5', 'Volume',
               'Today', 'Direction'],
              dtype='object')
```

We compute the correlation matrix using the `corr()` method for data frames, which produces a matrix that contains all of the pairwise correlations among the variables. (We suppress the output here.) The `pandas` library does not report a correlation for the `Direction` variable because it is qualitative.
자, 이제 이 변수 놈들끼리 서로 뒤에서 짬짜미로 얽히고설켜 얼마나 강력한 끈끈함을 자랑하는지 그 유착 비리 현장을 덮쳐볼 차례입니다. 판다스(pandas) 데이터 판때기의 무적 해킹 스킬 `corr()` 함수 지시 하나면, 변수들 모조리 일대일로 멱살을 잡고 거대한 **'상관 관계 행렬표(correlation matrix)'** 를 쫙 뽑아내 줍니다. (너무 표가 길어서 여백 부족으로 막았습니다.) 참고로 똑똑한 판다스 머신은 알아서 우리 정답 과녁인 `Direction` 변수 녀석만큼은 "에이, 이건 숫자가 아니라 떡상/떡락 문자로 된 분류 팻말(Qualitative)이잖아!" 하고 무시한 채, 표에서 아예 빼버리는 눈치 빠른 센스를 발휘합니다.

```python
In [5]: Smarket.corr()
```

As one would expect, the correlations between the lagged return variables and today’s return are close to zero. The only substantial correlation is between `Year` and `Volume`. By plotting the data we see that `Volume` is increasing over time. In other words, the average number of shares traded daily increased from 2001 to 2005.
뻔한 결과! 우리의 슬픈 예감대로, 어제그제 아무리 주식판이 요동쳤던 저 과거 잡동사니 이력(Lag) 힌트들과, 가장 궁금한 오늘 장의 대박 수익률(Today) 변수 사이의 상관관계 유착 점수는 그야말로 가차 없이 **바닥을 기는 싸늘한 0(Zero 무관심) 수치**에 처참히 가까웠습니다. (주식을 과거만 보고 쉽게 예측할 수 있다는 환상이 여기서 산산조각 흩어지죠!) 그 수많은 숫자 파편 중에 유일하게 튀는 실질적 덩치 유착 연관성은 오직 연도 세월 수치인 `Year` 와 주식 거래 물량 덩치인 `Volume` 둘 사이에만 강렬하게 존재했습니다. 이걸 눈요기 그래프(plot) 로 까발려 그려보면, 세월이 주욱 주욱 흐르면서 주식 시장의 투기장 덩치 볼륨이 기하급수적으로 부풀어 커져가고 있다는 팩트를 목격하게 됩니다. 돌려 말하면, 2001년부터 2005년까지 월가의 눈먼 개미와 세력들이 하루 평균 거래하는 주식 쇼핑 거래 횟수 물량 자체가 미친 듯 폭주하며 우상향으로 떡상했다는 잔인한 증거입니다.

```python
In [6]: Smarket.plot(y='Volume');
```

---

## Sub-Chapters

[< 4.7 Lab Logistic Regression Lda Qda And Knn](../trans2.html) | [4.7.2 Logistic Regression >](../4_7_2_logistic_regression/trans2.html)
