---
layout: default
title: "trans2"
---

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/trans2.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.3 Linear Discriminant Analysis
# 4.7.3 선형 판별 분석(LDA): 직선의 수호자, 선 그어 반으로 쪼개기!

We begin by performing LDA on the `Smarket` data, using the function `LinearDiscriminantAnalysis()`, which we have abbreviated `LDA()`. We fit the model using only the observations before 2005.
자, 이번엔 방금 전 로지스틱 회귀를 밀어내고 이 바닥의 두 번째 해결사, **선형 판별 분석(LDA, Linear Discriminant Analysis)** 머신을 우리 `Smarket` 빙고판 위에 등판시켜 보겠습니다. 너무 기니까 이름표는 엣지있게 `LDA()` 로 줄여 씁니다. 여기서도 아까 했던 똑같은 클리셰 전략! 우린 기계의 머릿속을 세팅(피팅) 하기 위해 오직 "2005년 이전에 발생한 과거 데이터 파편" 들만 쏙쏙 골라 훈련 캠프에 처넣을 겁니다.

```python
In [22]: lda = LDA(store_covariance=True)
```

Since the `LDA` estimator automatically adds an intercept, we should remove the column corresponding to the intercept in both `X_train` and `X_test`. We can also directly use the labels rather than the Boolean vectors `y_train`. 
여기서 아주 귀찮은 숨은 덫이 하나 있습니다. 파이썬의 이 똑똑한 `LDA` 추정기(estimator) 녀석은 지가 알아서 몰래 뱃속에 '절편(intercept)' 이란 부품 블록을 스리슬쩍 하나 추가해 달고 다닙니다. 그래서 우리가 앞서 정성껏 만들어둔 타깃 훈련지(`X_train`) 랑 시험지(`X_test`) 두 곳 모두에서, 괜히 충돌이 안 나게 저 'intercept' 기둥 자리를 톱으로 썰어 깔끔히 날려 제거해 줘야만 기계가 체하지 않습니다. 덤으로 굳이 참/거짓 불리언 쪼가리였던 `y_train` 대신 직관적이고 깔끔한 텍스트 팻말(레이블) 을 그대로 꽂아줘도 기계가 아주 찰떡같이 알아먹습니다.

```python
In [23]: X_train, X_test = [M.drop(columns=['intercept']) for M in [X_train, X_test]]
lda.fit(X_train, L_train)
```

```python
Out[23]: LinearDiscriminantAnalysis(store_covariance=True)
```

Here we have used the list comprehensions introduced in Section 3.6.4. Looking at our first line above, we see that the right-hand side is a list of length two. This is because the code `for M in [X_train, X_test]` iterates over a list of length two. While here we loop over a list, the list comprehension method works when looping over any iterable object. We then apply the `drop()` method to each element in the iteration, collecting the result in a list. The left-hand side tells `Python` to unpack this list of length two, assigning its elements to the variables `X_train` and `X_test`. Of course, this overwrites the previous values of `X_train` and `X_test`. 
위의 파이썬 코드 한 줄은 예술이자 타격기입니다. 저 멀리 옛날 3.6.4절에서 써먹었던 전설의 단축 스킬 '리스트 컴프리헨션(list comprehensions 한눈에 리스트 말아 쥐기)' 흑마법을 소환했죠. 맨 윗줄 수식을 째려보면 우측에서 길이가 2칸짜리 짤막한 리스트 짐 꾸러미가 도는 걸 볼 수 있습니다. `for M in [X_train, X_test]` 란 주문 자체가 원래 훈련용/시험용 종이 2장짜리 꾸러미 속에서 루프(loop 빙빙 돌림)를 돌리겠다는 억지거든요! (리스트 컴프리헨션은 리스트 말고도 돌릴 수만 있으면 아무 데나 다 먹히는 좀비 마법입니다.) 암튼 그 2장을 한 장씩 꺼내 돌리면서 지독한 `drop()` 분쇄기 메서드를 찰박찰박 먹여 요리한 다음, 결과 덩어리를 예쁜 리스트 상자에 쏙쏙 모아 담습니다. 그러고 나면 좌측 등호 세팅에서 파이썬은 이 2개들이 짐 꾸러미를 와장창 폭발해 열어젖혀(unpack) 내용물을 양 갈래 변수 `X_train`, `X_test` 에 터프하게 냅다 욱여넣습니다. 당연히 이 전리품이 들어가면서 과거에 있던 낡은 훈련용/시험용 종이 나부랭이 데이터들은 끔찍하게 박살 나 덮어 씌워집니다(overwrites).

Having fit the model, we can extract the means in the two classes with the `means_` attribute. These are the average of each predictor within each class, and are used by LDA as estimates of $\mu_k$. These suggest that there is a tendency for the previous 2 days’ returns to be negative on days when the market increases, and a tendency for the previous days’ returns to be positive on days when the market declines. 
힘들게 훈련 단련(fit) 을 끝마쳤으니 이제 이 LDA 전사에게서 꿀을 빨 시간이죠. 이 모델의 배때지에 `means_` (평균 추적기) 속성 스위치를 꽂아 넣으면, `Up` 과 `Down` 두 극단적 파벌 구역의 한가운데 심장 코어 결집 좌표(평균치) 를 쪽 빨아 추출할 수 있습니다. 이것들의 정체는 각 분류 파편(클래스) 방 안에 널브러진 힌트(예측 변수) 들의 한가운데 짭짤한 평균 점수들이며, 이 수학적 평균 결집치가 바로 LDA가 뼛속 깊이 숭배하는 '핵심 추정치 수식 $\mu_k$' 부품으로 빙의 되어 쓰입니다. 이 추출된 숫자 덩이의 내면을 들여다보면 꽤 소름 끼치는 암시가 깔려 있습니다! 무려 주식 장이 떡상 호황(increases) 인 날에는 그 전 이틀치 과거 지표가 처참히 마이너스(음수) 로 꼬꾸라져 있는 묘한 변태적 경향(tendency) 이 드러나고, 반대로 주식 장이 나락 하락장(declines) 인 날에는 오히려 과거 일자 지표가 붉게 물든 플러스(양수) 로 뜨거웠던 미친 반항기 경향성을 폭로합니다.

```python
In [24]: lda.means_
```

```python
Out[24]: array([[ 0.0426,  0.0338],
                [-0.0395, -0.0313]])
```

The estimated prior probabilities are stored in the `priors_` attribute. The package `sklearn` typically uses this trailing `_` to denote a quantity estimated when using the `fit()` method. We can be sure of which entry corresponds to which label by looking at the `classes_` attribute. 
이번엔 `priors_` 란 무기를 까볼 차례입니다. 여긴 LDA 모델이 전투에 앞서 몰래 계산해 박아둔 '사전 확률(prior probabilities, 각 세력이 원래 얼마나 세력이 큰지에 대한 밑밥 예측)' 이 봉인되어 담겨 있습니다. 눈치 빠른 분들은 알겠지만 파이썬 `sklearn` 장비 녀석들은 모델이 헉헉대며 `fit()` 훈련 헬스장에서 피땀 흘려 만들어낸 추정 근육 부위(결과 수치) 타투 끝에는 항상 저 `_` 꼬리표 밑줄 마크를 훈장처럼 자랑스레 새겨놓는 변태적 취향이 있습니다. 혹시 이 숫자들이 각각 어느 쪽 "Up? Down?" 클래스 편인지 헷갈리신다면 안심하십시오, `classes_` 이름표 속성을 까보면 누구 건지 백일하에 확연히 보증 확인이 가능합니다.

```python
In [25]: lda.classes_
```

```python
Out[25]: array(['Down', 'Up'], dtype='<U4')
```

The LDA output indicates that $\hat{\pi}_{Down} = 0.492$ and $\hat{\pi}_{Up} = 0.508$. 
밑밥용 사전 확률 수치를 뽑아보니 결과가 아주 적나라합니다: 떡락 방(`Down`) 비율인 $\hat{\pi}_{Down} = 0.492$, 그리고 떡상 방(`Up`) 파벌 비율인 $\hat{\pi}_{Up} = 0.508$ 로, 시장이 오를 확률 쪽으로 야금야금 아주 약간 기울어져 세팅되어 있음이 탄로 납니다.

```python
In [26]: lda.priors_
```

```python
Out[26]: array([0.49198397, 0.50801603])
```

The linear discriminant vectors can be found in the `scalings_` attribute: 
드디어 결전의 무기! 이 바닥을 일자로 서늘하게 그어 쪼개버리는 LDA의 필살기, **선형 판별 벡터(linear discriminant vectors 쪼개기 레이저 칼날 벡터)** 무기는 `scalings_` 인벤토리에 곱게 모셔져 있습니다. 확인해 보죠!

```python
In [27]: lda.scalings_
```

```python
Out[27]: array([[-0.64201906],
                [-0.51352928]])
```

These values provide the linear combination of `Lag1` and `Lag2` that are used to form the LDA decision rule. In other words, these are the multipliers of the elements of $X = x$ in (4.24). If $-0.642 \times Lag1 - 0.513 \times Lag2$ is large, then the LDA classifier will predict a market increase, and if it is small, then the LDA classifier will predict a market decline. 
저 음산한 소수점 숫자 덩어리들의 정체가 뭐냐고요? 바로 LDA가 편 가르기 할 때 휘두르는 절대 규칙 **결정 법전(decision rule)** 을 조립 완성하기 위해 `Lag1` 힌트와 `Lag2` 힌트를 얼마의 타격 스케일 비율로 배합할지를 결정짓는 선형 결합(linear combination) 배율 파츠입니다. 쉽게 말해 저 옛날 수식 (4.24) 시절 배웠던 $X = x$ 부품 기호 옆에 덕지덕지 붙어 덩치를 키웠다 줄였다 가중치를 때려 곱하는 마법의 승수 장치(multipliers 배율 폭탄) 들이란 거죠. 규칙은 살벌하고 명쾌합니다. 만일 힌트를 갈아 넣은 결합 식 **$-0.642 \times Lag1 - 0.513 \times Lag2$ 계산 덩어리 맷집 판정이 엄청나게 막대하게 거대하다면(large)**, LDA 심판관 머신은 주저 않고 "이야 오늘 주식 떡상(increase) 분위기 폭발이네!" 라고 망치를 땅땅 두들겨 예측 판정하고, 만약 저 계산 식 수치가 쪼그라들어 부실하고 왜소하다면(small) "글렀네 주식 나락 갈 각(decline) 이다!" 라고 가차 없이 지옥행을 예언 때립니다.

```python
In [28]: lda_pred = lda.predict(X_test)
```

As we observed in our comparison of classification methods (Section 4.5), the LDA and logistic regression predictions are almost identical. 
아까 우리가 Section 4.5 통계 배틀장(분류 방법 전쟁 비교) 에서 매의 눈으로 스캔하며 까발렸듯, 지금 이 LDA 머신 용사랑 아까 전 4.7.2 에 뛰었던 로지스틱 회귀 좀비가 뱉어내는 떡상/떡락 미래 점괘 예측 결과물은 거의 쌍둥이 도플갱어 급으로 일치(identical) 하는 수준의 똑같은 삽질 무브먼트를 보여줍니다.

```python
In [29]: confusion_table(lda_pred, L_test)
```

```python
Out[29]: Truth      Down   Up
Predicted            
Down         35   35
Up           76  106
```

We can also estimate the probability of each class for each point in a training set. Applying a 50% threshold to the posterior probabilities of being in class one allows us to recreate the predictions contained in `lda_pred`. 
덤으로 이 LDA 시스템은, 우주에 흩뿌려진 훈련 세트 속 파편 같은 수많은 각각의 점 하나하나마다 녀석이 어느 파벌(클래스) 호적에 떨어질지에 대한 각자 개별적 확률 점수를 얄밉게 추산 스캐닝해 냅니다. 그렇게 뽑아낸 1번 반(class one 떡상 방) 에 떨어질 기괴한 '사후 확률(posterior probability 나중 평가 확률)' 점수 위에다가 무식하게 극단적 칼날 **50% 절단 임계치 커트라인(threshold)** 을 가차 없이 찍어 내려버리면? 소름 돋게도 방금 전 `lda_pred` 가 뱉어냈던 그 단순명쾌한 `Up/Down` 과녁 표식 예언판과 100% 똑같은 기계적 재현 복원술(recreate) 이 창조 완성됩니다.

```python
In [30]: lda_prob = lda.predict_proba(X_test)
np.all(
    np.where(lda_prob[:,1] >= 0.5, 'Up','Down') == lda_pred
)
```

```python
Out[30]: True
```

Above, we used the `np.where()` function that creates an array with value `'Up'` for indices where the second column of `lda_prob` (the estimated posterior probability of `'Up'`) is greater than 0.5. For problems with more than two classes the labels are chosen as the class whose posterior probability is highest:
위 파이썬 매직 스펠 지시에서, 우리는 `np.where()` 이라는 잔인한 편 가르기 요술 채찍을 휘둘렀습니다. 이 채찍은 확률 뭉치 판때기인 `lda_prob` 의 두 번째 기둥 라인(즉, 녀석들의 뼛속에 서린 `'Up' 떡상행 사후 확률 지표치`) 이 0.5(50%) 반 넘기 커트라인을 뚫고 솟구쳤는지 미친 듯이 검증해서, 조건 충족된 놈들 자리에만 `'Up'` 인증 팻말을 쾅쾅 박아 넣은 새로운 통짜 배열 판을 통째 조립해 냅니다. 참고로 나중에 맞닥뜨려야 할 클래스 파벌 문이 두세 개를 뛰어넘는 대형 다자간 난투극 문제 세팅에서는, 그냥 무지성으로 찍는 대신 기계 뇌가 뽑아낸 사후 확률 수치가 **"가장 가장 무지막지하게 제일 높은 대장(highest)"** 클래스 문양을 승리자 레이블(label 팻말) 로 군림 채택 시키는 룰이 돌진 법칙으로 지배 적용됩니다. 

```python
In [31]: np.all(
    [lda.classes_[i] for i in np.argmax(lda_prob, 1)] == lda_pred
)
```

---

## Sub-Chapters

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/trans2.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/trans2.html)
