---
layout: default
title: "trans1"
---

[< 4.7 Lab Logistic Regression Lda Qda And Knn](../index.html) | [4.7.2 Logistic Regression >](../4_7_2_logistic_regression/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.1 The Stock Market Data
# 4.7.1 주식 시장 데이터

In this lab we will examine the `Smarket` data, which is part of the `ISLP` library.
이 실습에서 우리는 `ISLP` 라이브러리의 일부인 `Smarket` 데이터를 살펴볼 것입니다.

This data set consists of percentage returns for the S&P 500 stock index over 1,250 days, from the beginning of 2001 until the end of 2005.
이 데이터 세트는 2001년 초부터 2005년 말까지 1,250일 동안의 S&P 500 주가 지수의 백분율 수익률(percentage returns)로 구성되어 있습니다.

For each date, we have recorded the percentage returns for each of the five previous trading days, `Lag1` through `Lag5`.
각 날짜에 대해 우리는 이전 5일간의 각 거래일의 백분율 수익률인 `Lag1` 부터 `Lag5` 까지를 기록했습니다.

We have also recorded `Volume` (the number of shares traded on the previous day, in billions), `Today` (the percentage return on the date in question) and `Direction` (whether the market was `Up` or `Down` on this date).
우리는 또한 `Volume` (이전 날에 거래된 주식의 수, 10억 단위), `Today` (해당 날짜의 백분율 수익률), 그리고 `Direction` (이 날짜에 시장이 `Up` (상승) 이었는지 또는 `Down` (하락) 이었는지 여부)을 기록했습니다.

We start by importing our libraries at this top level; these are all imports we have seen in previous labs.
우리는 이 최상위 레벨에서 라이브러리들을 불러오기(importing)하는 것으로 시작합니다; 이것들은 모두 이전 실습들에서 본 적 있는 임포트들입니다.

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
우리는 또한 이 실습에 필요한 새로운 임포트들을 한데 모았습니다.

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
이제 우리는 `Smarket` 데이터를 로드할 준비가 되었습니다.

```python
In [3]: Smarket = load_data('Smarket')
Smarket
```

This gives a truncated listing of the data, which we do not show here.
이것은 데이터의 잘린(truncated) 목록을 제공하지만, 문서 지면상 여기에 표시하지는 않습니다.

We can see what the variable names are.
우리는 변수 이름들이 무엇인지 확인할 수 있습니다.

```python
In [4]: Smarket.columns
```

```python
Out[4]: Index(['Year', 'Lag1', 'Lag2', 'Lag3', 'Lag4', 'Lag5', 'Volume',
               'Today', 'Direction'],
              dtype='object')
```

We compute the correlation matrix using the `corr()` method for data frames, which produces a matrix that contains all of the pairwise correlations among the variables. (We suppress the output here.)
우리는 데이터 프레임에 대해 `corr()` 메서드를 사용하여 상관 행렬(correlation matrix)을 계산하며, 이는 변수들 간의 모든 쌍별(pairwise) 상관관계들을 포함하는 행렬을 생성합니다. (우리는 여기서 출력 결과를 생략(suppress)합니다.)

The `pandas` library does not report a correlation for the `Direction` variable because it is qualitative.
`pandas` 라이브러리는 `Direction` 변수가 정성적(qualitative)이기 때문에 그 상관관계를 보고하지 않습니다.

```python
In [5]: Smarket.corr()
```

As one would expect, the correlations between the lagged return variables and today’s return are close to zero.
예상할 수 있듯이, 지연된(lagged) 수익률 변수들과 오늘(today)의 수익률 간의 상관관계는 거의 0에 가깝습니다.

The only substantial correlation is between `Year` and `Volume`.
유일한 실질적인(substantial) 상관관계는 `Year` 와 `Volume` 사이에서만 존재합니다.

By plotting the data we see that `Volume` is increasing over time.
데이터를 도표로 그려봄으로써, 우리는 `Volume` 이 시간이 지남에 따라 증가하고 있음을 확인하게 됩니다.

In other words, the average number of shares traded daily increased from 2001 to 2005.
다시 말해, 일평균 거래된 주식의 수는 2001년에서 2005년까지 추세적으로 증가했습니다.

```python
In [6]: Smarket.plot(y='Volume');
```

---

## Sub-Chapters

[< 4.7 Lab Logistic Regression Lda Qda And Knn](../index.html) | [4.7.2 Logistic Regression >](../4_7_2_logistic_regression/trans1.html)
