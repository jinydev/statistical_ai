---
layout: default
title: "trans2"
---

[< 4.7 Lab Logistic Regression Lda Qda And Knn](../index.html) | [4.7.2 Logistic Regression >](../4_7_2_logistic_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.1 The Stock Market Data
# 4.7.1 무자비한 도박장: 주식 시장(`Smarket`) 데이터 살펴보기

In this lab we will examine the `Smarket` data, which is part of the `ISLP` library.
이번 코딩 실습(Lab)에서는 통계학 바닥에서 아주 유명한 예제인 `Smarket` (주식 시장) 데이터를 도마에 올려 해부해 볼 것입니다. 이 녀석은 우리가 깔아둔 `ISLP` 장난감 상자(라이브러리) 안에 얌전히 들어있습니다.

This data set consists of percentage returns for the S&P 500 stock index over 1,250 days, from the beginning of 2001 until the end of 2005.
이 데이터 세트는 진짜 잔혹한 피바람이 부는 실전 도박장 데이터입니다. 2001년 새해 첫 장부터 2005년 연말 폐장일까지 무려 1,250일 동안 피 튀기게 오르내린 미국의 'S&P 500 주가 지수'의 **일일 백분율 수익률(상승/하락 퍼센트)** 기록을 꽉꽉 눌러 담고 있죠.

For each date, we have recorded the percentage returns for each of the five previous trading days, `Lag1` through `Lag5`.
우리는 오늘 시장이 과연 오를지 내릴지 점치기 위해 과거의 '패턴'을 훔쳐봐야 합니다. 그래서 표의 각 날짜마다, 우리는 바로 어제(`Lag1`)부터 5일 전(`Lag5`)까지 지난 5일치 과거의 주가 수익률 지표들을 '후행 단서 지표(Lags)'로 꼼꼼하게 기록해 두었습니다.

We have also recorded `Volume` (the number of shares traded on the previous day, in billions), `Today` (the percentage return on the date in question) and `Direction` (whether the market was `Up` or `Down` on this date).
그것뿐만이 아닙니다. 총알이 얼마나 터졌는지 알려주는 `Volume` (어제 시장에서 거래된 주식의 총 물량, 무려 10억 주 단위!), 우리가 때려 맞춰야 할 진짜 정답인 `Today` (오늘의 정확한 수익률 수치), 그리고 궁극의 사활이 걸린 타깃이자 정성적 꼬리표인 `Direction` (그래서 오늘 진짜로 올랐냐(`Up`) 내렸냐(`Down`)?) 지표까지 모조리 채집해 두었죠.

We start by importing our libraries at this top level; these are all imports we have seen in previous labs.
자, 코딩 짐을 꾸려봅시다. 언제나 그랬듯 파이썬 코드의 가장 꼭대기 층에다가 우리가 전투에서 써먹을 공구(라이브러리)들을 줄줄이 소환(import)합니다. 익숙한 얼굴들이 많네요.

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
거기에 더해, 이번 분류 전투(Classification Lab) 실습에서 새로 투입될 첨단 특수 기동 무기(로지스틱, 판별 분석, KNN 등)들도 모조리 수배해서 미리 소환해 둡니다.

```python
In [2]: from ISLP import confusion_table # 이놈이 얼마나 맞췄는지 체점할 성적표 출력기
from ISLP.models import contrast
from sklearn.discriminant_analysis import     (LinearDiscriminantAnalysis as LDA,     QuadraticDiscriminantAnalysis as QDA) # 직선과 곡선의 판별 암살자들!
from sklearn.naive_bayes import GaussianNB # 심플 이즈 베스트 나이브 베이즈
from sklearn.neighbors import KNeighborsClassifier # 다구리의 신 KNN
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression # 우리의 전통 깡패 무기
```

Now we are ready to load the `Smarket` data.
자, 특수 부대 무기 소환이 끝났으니, 본격적으로 지옥의 `Smarket` (주식) 데이터를 디스크에서 메모리로 띄워 올릴 준비가 되었습니다.

```python
In [3]: Smarket = load_data('Smarket')
Smarket
```

This gives a truncated listing of the data, which we do not show here.
코드를 때리면 터미널 창에 1,250일 치 과거 주식 기록이 쫘아악 뿜어져 나오겠지만, 너무 길어서 위아래가 댕강 잘린 채(truncated) 프리뷰만 보일 겁니다. 지면상 여기에 그대로 다 쓰진 않겠습니다.

We can see what the variable names are.
우리가 가진 힌트 무기 이름표(컬럼명)들이 정확히 어떻게 생겨 먹었는지 한번 슬쩍 확인해 보죠.

```python
In [4]: Smarket.columns
```

```python
Out[4]: Index(['Year', 'Lag1', 'Lag2', 'Lag3', 'Lag4', 'Lag5', 'Volume',
               'Today', 'Direction'],
              dtype='object')
```

We compute the correlation matrix using the `corr()` method for data frames, which produces a matrix that contains all of the pairwise correlations among the variables. (We suppress the output here.)
이제 이 변수들끼리 뒷구멍으로 어떤 꿍꿍이(상관관계)를 맺고 있는지 까발려야 합니다. 판다스(Pandas)의 `corr()` 메서드 지팡이를 휘두르면, 숫자 변수들 간에 서로 얼마나 함께 움직이는지를 -1부터 1 상간으로 측정해 주는 **전체 상관관계 엑스레이 행렬(correlation matrix)** 을 아주 단숨에 쫙 뽑아내 줍니다. (너무 표가 커서 여기선 결괏값을 숨겼습니다.)

The `pandas` library does not report a correlation for the `Direction` variable because it is qualitative.
참고로 판다스 엑스레이 기계는 `Direction`(`Up` 아님 `Down`) 변수만큼은 무시하고 패스해 버립니다. 왜냐고요? 이 녀석은 숫자가 아니라 영어 알파벳 문자가 박혀있는 범주형(qualitative) 꼬리표 팻말이라서 숫자 기반의 상관관계 연산을 때릴 수가 없기 때문이죠.

```python
In [5]: Smarket.corr()
```

As one would expect, the correlations between the lagged return variables and today’s return are close to zero.
엑스레이를 돌려본 결과, 우리가 (어렴풋이 절망적으로) 예상했던 대로 나옵니다. 과거 5일간의 주식 지표(`Lag` 변수들)와 진짜 우리가 맞추고 싶은 '오늘의 주식 수익률(`Today`)' 사이의 상관관계 점수는 거의 쓰레기에 가까운 '0점' 근방을 맴돌고 있었습니다. 어제 주식이 올랐다고 오늘 오르는 게 아니라는, 도박장의 냉혹한 현실이죠!

The only substantial correlation is between `Year` and `Volume`.
이 쓰레기 더미 행렬 속에서 유일하게 눈에 띄는 의미 있는(substantial) 양의 상관관계 커넥션은 딱 하나, 바로 흘러가는 시간(`Year`)과 주식 거래량(`Volume`) 사이에만 존재했습니다.

By plotting the data we see that `Volume` is increasing over time.
이 거래량 데이터를 그래프로 스윽 시각화해서 뿌려보니, 거래량(`Volume`) 녀석이 세월이 감에 따라 멈추지 않고 미친 듯이 쭉쭉 우상향하며 치솟는 게 보입니다.

In other words, the average number of shares traded daily increased from 2001 to 2005.
즉 다시 말해, 2001년부터 2005년까지 시간이 흐르면서 사람들이 도박장(주식 시장)에 미친 듯이 몰려들어 하루 평균 주식 거래 거래량(Volume) 사이즈 카운트 판돈 자체가 어마어마하게 커지게 증가했다는 아주 자명한 사실을 우리에게 귀띔해 주는 겁니다.

```python
In [6]: Smarket.plot(y='Volume');
```

---

## Sub-Chapters

[< 4.7 Lab Logistic Regression Lda Qda And Knn](../index.html) | [4.7.2 Logistic Regression >](../4_7_2_logistic_regression/trans2.html)
