---
layout: default
title: "trans1"
---

[< 4.7 Lab Logistic Regression Lda Qda And Knn](../trans1.html) | [4.7.2 Logistic Regression >](../4_7_2_logistic_regression/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.1 The Stock Market Data
# 4.7.1 주식 시장 데이터

In this lab we will examine the `Smarket` data, which is part of the `ISLP` library. This data set consists of percentage returns for the S&P 500 stock index over 1,250 days, from the beginning of 2001 until the end of 2005. For each date, we have recorded the percentage returns for each of the five previous trading days, `Lag1` through `Lag5`. We have also recorded `Volume` (the number of shares traded on the previous day, in billions), `Today` (the percentage return on the date in question) and `Direction` (whether the market was `Up` or `Down` on this date).
이 랩에서 우리는 `ISLP` 라이브러리의 일부인 `Smarket` 데이터를 검토할 것입니다. 이 데이터 세트는 2001년 초부터 2005년 말까지 1,250일 동안의 S&P 500 주가지수에 대한 백분율 수익률(percentage returns)로 구성됩니다. 매 날짜마다 우리는 이전 5번의 거래일 각각에 대한 백분율 수익률인 `Lag1` 부터 `Lag5` 를 기록했습니다. 우리는 또한 `Volume` (이전 날 거래된 주식 수, 10억 단위), `Today` (해당 날짜의 백분율 수익률), 그리고 `Direction` (이 날짜에 시장이 상승(`Up`)했는지 하락(`Down`)했는지 여부)을 기록했습니다.

We start by importing our libraries at this top level; these are all imports we have seen in previous labs.
최상위 레벨에서 라이브러리를 임포트(import)하는 것으로 시작하겠습니다; 이것들은 모두 이전 랩에서 보았던 임포트입니다.

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
또한 이 랩에 필요한 새로운 임포트들을 함께 모았습니다.

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
이제 `Smarket` 데이터를 로드할 준비가 되었습니다.

```python
In [3]: Smarket = load_data('Smarket')
Smarket
```

This gives a truncated listing of the data, which we do not show here. We can see what the variable names are.
이것은 여기서는 표시하지 않은, 잘린 데이터 목록을 제공합니다. 변수 이름이 무엇인지 확인할 수 있습니다.

```python
In [4]: Smarket.columns
```

```python
Out[4]: Index(['Year', 'Lag1', 'Lag2', 'Lag3', 'Lag4', 'Lag5', 'Volume',
               'Today', 'Direction'],
              dtype='object')
```

We compute the correlation matrix using the `corr()` method for data frames, which produces a matrix that contains all of the pairwise correlations among the variables. (We suppress the output here.) The `pandas` library does not report a correlation for the `Direction` variable because it is qualitative.
우리는 데이터 프레임에 대해 `corr()` 메서드를 사용하여 변수들 사이의 모든 쌍별(pairwise) 상관 관계를 포함하는 행렬을 생성하는 상관 관계 행렬(correlation matrix)을 계산합니다. (여기서는 출력을 생략합니다.) `pandas` 라이브러리는 `Direction` 변수가 정성적(qualitative)이기 때문에 이 변수에 대한 상관 관계를 보고하지 않습니다.

```python
In [5]: Smarket.corr()
```

As one would expect, the correlations between the lagged return variables and today’s return are close to zero. The only substantial correlation is between `Year` and `Volume`. By plotting the data we see that `Volume` is increasing over time. In other words, the average number of shares traded daily increased from 2001 to 2005.
예상할 수 있듯이, 지연(lagged) 수익률 변수들과 오늘의 수익률 사이의 상관 관계는 0에 가깝습니다. 유일하게 실질적인 상관 관계는 `Year` 와 `Volume` 사이에 있습니다. 데이터를 통해 플롯을 그려보면 자전거 대여량인 아님을, 오히려 주식 `Volume`이 시간이 지남에 따라 증가하고 있음을 알 수 있습니다. 즉, 매일 거래되는 평균 주식 수가 2001년에서 2005년까지 증가했습니다.

```python
In [6]: Smarket.plot(y='Volume');
```

---

## Sub-Chapters

[< 4.7 Lab Logistic Regression Lda Qda And Knn](../trans1.html) | [4.7.2 Logistic Regression >](../4_7_2_logistic_regression/trans1.html)
