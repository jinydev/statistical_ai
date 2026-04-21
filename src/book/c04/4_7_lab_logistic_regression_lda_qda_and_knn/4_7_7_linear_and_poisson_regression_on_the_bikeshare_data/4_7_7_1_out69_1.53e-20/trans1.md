---
layout: default
title: "trans1"
---

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../trans1.html) | [4.7.7.1 Poisson Regression >](../4_7_7_1_poisson_regression/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# **`Out[69]:`** `1.53e-20` 

The sum of squared differences is zero. We can also see this using the `np.allclose()` function: 
제곱된 차이의 합(sum of squared differences)은 0입니다. 우리는 `np.allclose()` 함수를 사용하여 이것을 확인할 수도 있습니다:

```python
In [70]: np.allclose(M_lm.fittedvalues, M2_lm.fittedvalues)
```

```python
Out[70]: True
```

To reproduce the left-hand side of Figure 4.13 we must first obtain the coefficient estimates associated with `mnth`. The coefficients for January through November can be obtained directly from the `M2_lm` object. The coefficient for December must be explicitly computed as the negative sum of all the other months. We first extract all the coefficients for month from the coefficients of `M2_lm`. 
Figure 4.13의 왼쪽 부분을 재현하려면 먼저 `mnth` 와 관련된 계수 추정치를 얻어야 합니다. 1월부터 11월까지의 계수는 `M2_lm` 객체에서 직접 얻을 수 있습니다. 12월에 대한 계수는 다른 모든 달의 합계의 음수로 명시적으로 계산되어야 합니다. 우리는 먼저 `M2_lm` 의 계수들로부터 월에 대한 모든 계수를 추출합니다.

```python
In [71]: coef_month = S2[S2.index.str.contains('mnth')]['coef']
coef_month
```

```python
Out[71]: mnth[Jan]      -46.0871
         mnth[Feb]      -39.2419
         mnth[March]    -29.5357
         mnth[April]     -4.6622
         mnth[May]       26.4700
         mnth[June]      21.7317
         mnth[July]      -0.7626
         mnth[Aug]        7.1560
         mnth[Sept]      20.5912
         mnth[Oct]       29.7472
         mnth[Nov]       14.2229
         Name: coef, dtype: float64
```

Next, we append `Dec` as the negative of the sum of all other months. 
다음으로, 우리는 모든 다른 달의 합계의 음수로서 `Dec` 를 추가(append)합니다.

```python
In [72]: months = Bike['mnth'].dtype.categories
coef_month = pd.concat([
    coef_month,
    pd.Series([-coef_month.sum()],
              index=['mnth[Dec]'])
])
coef_month
```

```python
Out[72]: mnth[Jan]      -46.0871
         mnth[Feb]      -39.2419
         mnth[March]    -29.5357
         mnth[April]     -4.6622
         mnth[May]       26.4700
         mnth[June]      21.7317
         mnth[July]      -0.7626
         mnth[Aug]        7.1560
         mnth[Sept]      20.5912
         mnth[Oct]       29.7472
         mnth[Nov]       14.2229
         mnth[Dec]        0.3705
         Name: coef, dtype: float64
```

Finally, to make the plot neater, we’ll just use the first letter of each month, which is the 6th entry of each of the labels in the index. 
마지막으로 도표(plot)를 더 깔끔하게 만들기 위해 각 월의 첫 글자만 사용할 것인데, 이는 인덱스에 있는 각 레이블의 6번째 항목(entry)입니다.

```python
In [73]: fig_month, ax_month = subplots(figsize=(8,8))
x_month = np.arange(coef_month.shape[0])
ax_month.plot(x_month, coef_month, marker='o', ms=10)
ax_month.set_xticks(x_month)
ax_month.set_xticklabels([l[5] for l in coef_month.index], fontsize=20)
ax_month.set_xlabel('Month', fontsize=20)
ax_month.set_ylabel('Coefficient', fontsize=20);
```

Reproducing the right-hand plot in Figure 4.13 follows a similar process. 
Figure 4.13의 오른쪽 도표를 재현하는 것도 유사한 과정을 따릅니다.

```python
In [74]: coef_hr = S2[S2.index.str.contains('hr')]['coef']
coef_hr = coef_hr.reindex(['hr[{0}]'.format(h) for h in range(23)])
coef_hr = pd.concat([coef_hr,
                     pd.Series([-coef_hr.sum()], index=['hr[23]'])])
```

We now make the hour plot. 
우리는 이제 시간 도표(hour plot)를 만듭니다.

```python
In [75]: fig_hr, ax_hr = subplots(figsize=(8,8))
x_hr = np.arange(coef_hr.shape[0])
ax_hr.plot(x_hr, coef_hr, marker='o', ms=10)
ax_hr.set_xticks(x_hr[::2])
ax_hr.set_xticklabels(range(24)[::2], fontsize=20)
ax_hr.set_xlabel('Hour', fontsize=20)
ax_hr.set_ylabel('Coefficient', fontsize=20);
```

---

## Sub-Chapters

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../trans1.html) | [4.7.7.1 Poisson Regression >](../4_7_7_1_poisson_regression/trans1.html)
