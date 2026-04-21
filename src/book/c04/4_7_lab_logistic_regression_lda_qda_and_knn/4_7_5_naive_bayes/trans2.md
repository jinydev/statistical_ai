---
layout: default
title: "trans2"
---

[< 4.7.4 Quadratic Discriminant Analysis](../4_7_4_quadratic_discriminant_analysis/trans2.html) | [4.7.6 K-Nearest Neighbors >](../4_7_6_k-nearest_neighbors/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.5 Naive Bayes
# 4.7.5 나이브 베이즈: 극좌파 독립 맹신도, "난 남의 눈치 안 봐!"

Next, we fit a naive Bayes model to the `Smarket` data. The syntax is similar to that of `LDA()` and `QDA()`. By default, this implementation of the naive Bayes classifier models each quantitative feature using a Gaussian distribution. However, a kernel density method can also be used to estimate the distributions. 
자, 다음 선수 입장입니다! 이번엔 `Smarket` 투기판 데이터에 아주 순진하고도 무식한 극단주의자, **나이브 베이즈(naive Bayes)** 머신을 꽂아볼 차례입니다. 파이썬 조종 명령(syntax) 은 형님들인 `LDA()` 나 `QDA()` 부를 때와 아주 비슷해서 지루할 정도입니다. 참고로 이 나이브 베이즈라는 녀석은 뼛속까지 맹신하는 철학이 있는데, 주입되는 하나하나의 숫자형 힌트(특성) 들이 전부 고상한 가우시안(정규) 분포의 종 모양 텐트에서 놀고 있다고 (디폴트로) 철석같이 믿어 의심치 않습니다. 하지만 정 모양이 맘에 안 들면, 은근슬쩍 커널 밀도(kernel density) 스킬이라는 유연한 곡선 깎기 장비를 대신 달아줘서 분포 모양을 입맛대로 굴릴 수도 있습니다.

```python
In [38]: NB = GaussianNB()
NB.fit(X_train, L_train)
```

```python
Out[38]: GaussianNB()
```

The classes are stored as `classes_`. 
이 무식한 녀석도 적군의 파벌 이름(클래스) 들은 똑똑히 `classes_` 란 방에 박제해 놓습니다.

```python
In [39]: NB.classes_
```

```python
Out[39]: array(['Down', 'Up'], dtype='<U4')
```

The class prior probabilities are stored in the `class_prior_` attribute. 
전투 시작 전 눈치싸움용 배당률 스펙, 즉 참/거짓 클래스별 베이스캠프 지분율(사전 확률 prior probabilities) 은 `class_prior_` 란 이름의 문신으로 몸에 새겨 넣습니다. (이것도 아까랑 거의 반반 비율이네요).

```python
In [40]: NB.class_prior_
```

```python
Out[40]: array([0.49198397, 0.50801603])
```

The parameters of the features can be found in the `theta_` and `var_` attributes. The number of rows is equal to the number of classes, while the number of columns is equal to the number of features. We see below that the mean for feature `Lag1` in the `Down` class is $0.043$. 
이제 힌트 변수(feature) 들이 뿜어내는 찐 스탯들을 해부해 볼까요? 이 비밀은 저 이상한 창고 이름 `theta_` (이게 평균입니다) 와 `var_` (요게 분산입니다) 란 두 금고 안에 꽁꽁 숨겨져 있습니다. 뽑혀 나온 행렬 표를 보면, 행(가로줄) 개수는 양쪽 파벌 세력(클래스) 수를 나타내고, 기둥(세로방) 개수는 우리가 집어넣은 예측 특성 무기 개수를 나타냅니다. 아래 통계판을 스윽 째려보면, 그 더러운 나락 하락장(`Down`) 파벌 소속의 `Lag1` 힌트 녀석이 가진 정중앙 코어 덩치(평균) 점수가 대략 $0.043$ 근방에서 맴돈다는 걸 잡아낼 수 있습니다.

```python
In [41]: NB.theta_
```

```python
Out[41]: array([[ 0.04279022,  0.03389409],
                [-0.03954635, -0.03132544]])
```

Its variance is $1.503$. 
그 옆 금고 `var_` 를 뜯어보니 녀석의 널뛰는 요동 오차폭(분산 variance) 수치는 약 $1.503$ 에 달하네요.

```python
In [42]: NB.var_
```

```python
Out[42]: array([[1.50355424, 1.53246652],
                [1.51397116, 1.4870335 ]])
```

How do we know the names of these attributes? We use `NB?` (or `?NB`). We can easily verify the mean computation: 
"아니, 저기요! 기계에 저딴 `theta_` 나 `var_` 같은 변태 이름이 숨겨져 있는지 내가 도대체 어찌 알아요?" 라고 분노하신다면? 그냥 코딩창에 `NB?` (혹은 `?NB`) 라고 물건의 사용 설명서 도움말 호출 매직 주문을 때려 넣으면 만사형통입니다! 그럼 방금 기계가 속성으로 뱉어낸 저 평균 점수가 진짜 사기 친 게 아닌지 수동 노가다 코딩으로 멱살 잡고 검증(verify) 비교 타격을 해봅시다!

```python
In [43]: X_train[L_train == 'Down'].mean()
```

```python
Out[43]: Lag1    0.042790
         Lag2    0.033894
         dtype: float64
```

Similarly for the variance: 
내친김에 분산 요동치 계산도 수동 모드로 직접 비교 사격!

```python
In [44]: X_train[L_train == 'Down'].var(ddof=0)
```

```python
Out[44]: Lag1    1.503554
         Lag2    1.532467
         dtype: float64
```

The `GaussianNB()` function calculates variances using the $1/n$ formula. Since `NB()` is a classifier in the `sklearn` library, making predictions uses the same syntax as for `LDA()` and `QDA()` above. 
참고로 저 `GaussianNB()` 통계 머신 놈은 꼰대처럼 $1/n$ (n-1 이 아니라!) 공식 나눗셈 작두를 사용해서 무식하게 분산값을 베어 도출해 냅니다. 어쨌든 이 `NB()` 빙고판 요정 녀석도 결국 아까 위에서 봤던 그 일관성 쩌는 군대 조직 `sklearn` 라이브러리의 일개 졸개(분류기) 일 뿐입니다. 고로! 예측 미래의 발사 방아쇠 스위치 조작법은 선배들인 `LDA()` 나 `QDA()` 쏠 때랑 단 1밀리미터의 토씨도 틀리지 않고 똑같은 무적의 군대식 공산품 코딩(syntax) 을 그대로 복붙 돌려 막기 하면 됩니다. 매우 편—안하죠!

```python
In [45]: nb_labels = NB.predict(X_test)
confusion_table(nb_labels, L_test)
```

```python
Out[45]: Truth      Down   Up
Predicted            
Down         29   20
Up           82  121
```

Naive Bayes performs well on these data, with accurate predictions over 59% of the time. This is slightly worse than QDA, but much better than LDA. 
야생의 테스트 전투 결과판! 이 무식한 맹신도 나이브 베이즈가 이 주식판 뻘밭에서 생각보다 미친 폼으로 선방(performs well) 하며 날뜁니다! 자그마치 전체 타겟 중 **59% 이상의 백발백중 명중률(accurate predictions)** 에 도달했거든요! 방금 전 곡선 폭격기 QDA 형님보단 코딱지만큼(slightly) 딸려 뒤처지지만, 뻣뻣한 꼰대 직선충 LDA 따위는 가볍게 씹어먹고 박살 내는(much better) 압도적 포포먼스 기행을 뿜어냅니다. (이 '각자도생 맹신' 전술이 때론 이렇게 무섭습니다!)

As for `LDA`, the `predict_proba()` method estimates the probability that each observation belongs to a particular class. 
물론 잊지 마십시오, `LDA` 동네 형님들이 심심하면 꺼내 쓰던 그 확률 계산기 `predict_proba()` 사후 예언 메서드를 갈겨 넣으면, 이 나이브 베이즈 기계 녀석도 각각의 흩뿌려진 타깃 관측치 파편 하나하나가 어느 정답 클래스 문파로 굴러떨어질지 그 처절한 생존 배팅 **확률(probability)** 스코어를 낱낱이 도마 위에 스캐닝해 뽑아내 줍니다.

```python
In [46]: NB.predict_proba(X_test)[:5]
```

```python
Out[46]: array([[0.48732444, 0.51267556],
                [0.47620455, 0.52379545],
                [0.46526732, 0.53473268],
                [0.47481179, 0.52518821],
                [0.49015096, 0.50984904]])
```

---

## Sub-Chapters

[< 4.7.4 Quadratic Discriminant Analysis](../4_7_4_quadratic_discriminant_analysis/trans2.html) | [4.7.6 K-Nearest Neighbors >](../4_7_6_k-nearest_neighbors/trans2.html)
