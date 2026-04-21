---
layout: default
title: "trans2"
---

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../trans2.html) | [4.7.7.1 Poisson Regression >](../4_7_7_1_poisson_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# **`Out[69]:`** `1.53e-20` 

The sum of squared differences is zero. We can also see this using the `np.allclose()` function: 
저 두 모델 놈들이 내뱉은 미래 예측값들끼리 서로 빼기 빼기 해서 제곱 펀치를 날려 다 더해봤자, 오차가 코딱지만큼도 없는(거의 $10^{-20}$ 수준의 미세먼지급) 완벽한 0점에 수렴해 버립니다. 이건 파이썬 심판관인 `np.allclose()` (둘이 완전 똑같아? 묻는 함수) 를 불러서 검증해도 투명하게 밝혀집니다.

```python
In [70]: np.allclose(M_lm.fittedvalues, M2_lm.fittedvalues)
```

```python
Out[70]: True
```

To reproduce the left-hand side of Figure 4.13 we must first obtain the coefficient estimates associated with `mnth`. The coefficients for January through November can be obtained directly from the `M2_lm` object. The coefficient for December must be explicitly computed as the negative sum of all the other months. We first extract all the coefficients for month from the coefficients of `M2_lm`. 
자, 이제 교과서 구석에 폼나게 박혀있던 그 전설의 그림 Figure 4.13 의 좌측 그래프를 우리 손으로 직접 그려볼(reproduce) 차례입니다! 우린 저 빙글빙글 도는 12달 캘린더(`mnth`) 의 영향력 꼬리표(계수) 숫자들을 모조리 긁어와야 합니다. 1월부터 11월까지 11개 달의 파워 점수는 아까 만든 `M2_lm` 창고에서 그대로 퍼오면 게임 끝입니다. 하지만 왕따 당해서 창고 명단에서 치워졌던 대망의 12월(`Dec`) 녀석의 파워 점수는 어떻게 구하냐고요? 아까 배운 그 변태 룰! "형제들 11명 점수 다 더해서 마이너스 빔 맞기" 공식을 써서 우리가 수동으로 억눌러 계산(computed) 해 쥐어짜 내야만 합니다. 일단 창고 `M2_lm` 에 있는 달(month) 스코어 파편들부터 싹 쓸어 담아 봅시다.

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
싹쓸이해 온 11개 형제 스코어 맨 밑바닥에다가, 드디어 우리가 수동으로 "다 더해서 마이너스 곱박" 때린 불쌍한 `Dec` (12월) 의 영혼 스코어를 강제로 접착(append) 시킵니다.

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
마지막으로 붓질입니다! 그래프 밑바닥에 이름이 `mnth[Jan]` 처럼 징그럽게 길면 지저분해서 보기 빡치니까, 저 리스트 문자열의 딱 6번째 알파벳 글자('J', 'F', 'M' 등 달의 엣지있는 앞 글자 하나 스펠링!) 모가지만 탁탁 썰어 뽑아서 예술적으로 깔끔(neater) 한 X축 팻말 전시를 세팅해 줍니다. 

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
오른쪽 그래프, 즉 24시간(`hr`) 변화에 따른 영향력 그래프를 복제하는 과정도 이 짓거리와 100% 흡사한 좀비 노가다 사이클(similar process) 로 똑같이 돌아갑니다. 막내 밤 11시(`hr 23`) 스코어만 따로 떼내어 형들 스코어 더해 뒤집는 마이너스 빔을 때리는 식이죠.

```python
In [74]: coef_hr = S2[S2.index.str.contains('hr')]['coef']
coef_hr = coef_hr.reindex(['hr[{0}]'.format(h) for h in range(23)])
coef_hr = pd.concat([coef_hr,
                     pd.Series([-coef_hr.sum()], index=['hr[23]'])])
```

We now make the hour plot. 
수동 영혼 결합이 끝났으니, 이제 '시간 꺾은선 도표(hour plot)' 에 색칠해 피날레를 장식합니다!

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

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../trans2.html) | [4.7.7.1 Poisson Regression >](../4_7_7_1_poisson_regression/trans2.html)
