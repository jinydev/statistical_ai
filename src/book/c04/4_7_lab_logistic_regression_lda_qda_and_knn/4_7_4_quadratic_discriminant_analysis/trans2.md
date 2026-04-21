---
layout: default
title: "trans2"
---

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/trans2.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.4 Quadratic Discriminant Analysis
# 4.7.4 이차 판별 분석 (QDA): 뻣뻣한 직선은 가라, 유연한 곡선 폭격기가 떴다!

We will now fit a QDA model to the `Smarket` data. QDA is implemented via `QuadraticDiscriminantAnalysis()` in the `sklearn` package, which we abbreviate to `QDA()`. The syntax is very similar to `LDA()`. 
자, 지루한 선 긋기 놀이는 끝났습니다. 이번엔 좀 더 유연하고 짐승 같은 폭격기 **QDA(이차 판별 분석)** 머신을 `Smarket` 격전지에 피팅 참전시킬 차례입니다. `sklearn` 무기고에서 가장 긴 이름셔틀 중 하나인 `QuadraticDiscriminantAnalysis()` 라는 함수로 소환되는데, 타자 치다 손가락에 쥐가 날 수 있으니 우린 폼나게 `QDA()` 로 줄여서 부르겠습니다. 요 녀석 조종법(syntax) 은 형님 격인 아까 그 `LDA()` 모델과 완전 붕어빵 쌍둥이처럼 똑같아서 꿀 빠는 세팅이 가능합니다.

```python
In [33]: qda = QDA(store_covariance=True)
qda.fit(X_train, L_train)
```

```python
Out[33]: QuadraticDiscriminantAnalysis(store_covariance=True)
```

The `QDA()` function will again compute `means_` and `priors_`. 
방금 피팅 훈련 먹방을 끝낸 이 `QDA()` 머신 고철 덩어리에게 똑같이 스위치를 넣어보면, 아까 LDA처럼 지겹게 `means_` (평균 추적기) 랑 `priors_` (사전 밑밥 확률기) 두 핵심 스탯 창을 계산해 뽑아냅니다. 

```python
In [34]: qda.means_, qda.priors_
```

```python
Out[34]: (array([[ 0.04279022,  0.03389409],
                 [-0.03954635, -0.03132544]]),
          array([0.49198397, 0.50801603]))
```

The `QDA()` classifier will estimate one covariance per class. Here is the estimated covariance in the first class: 
여기서 QDA만의 변태 같은 필살기가 등장합니다! 아까 LDA 놈은 "에이 세상 만사 뭐 다 똑같지~" 라며 모든 분류 파벌 덩어리들의 분산 널뛰기 진동 폭(공분산 행렬) 이 몽땅 100% 동일하다고 싸잡아 퉁치는(공통 분산) 게으른 가정을 썼죠? 하지만 우리의 결벽증 완벽주의 QDA 기계는 "**클래스(파벌) 놈들마다 놀고먹는 공분산(covariance) 세팅을 전부 따로따로 독립적으로 1:1 견적 내서 측정**" 하는 엄청난 노가다 추정 스킬을 발동합니다. 한번 까볼까요? 여기 밑에 토해낸 행렬포 수치가 바로 첫 번째 클래스(떡락 방 `Down`) 구역 놈들만의 처절한 전용 공분산 추정치 수치 폭탄입니다!

```python
In [35]: qda.covariance_[0]
```

```python
Out[35]: array([[ 1.50662277, -0.03924806],
                [-0.03924806,  1.53559498]])
```

The output contains the group means. But it does not contain the coefficients of the linear discriminants, because the QDA classifier involves a quadratic, rather than a linear, function of the predictors. The `predict()` function works in exactly the same fashion as for LDA. 
이 녀석이 뱉어낸 인벤토리 안에는 그룹별 평균 좌표들은 고스란히 담겨 있지만, 아까 LDA 때 봤던 뻣뻣한 '선형 판별의 배수 계수(coefficients)' 같은 단단한 일자 막대기 부품들은 쥐뿔도 존재하지 않습니다. 왜냐고요? 이 QDA 괴물은 예측 변수 힌트들을 이을 때 유치한 일자(linear 선형) 직선 막대기를 쓰는 게 아니라, 부드럽고 유연하며 미친 듯이 구부러지는 뱀 같은 형태의 **이차(quadratic 곡선) 함수 폭탄 무기**를 탑재해서 곡면 궤도로 잘려 쪼개 버리기 때문입니다! (직선의 계수 따윈 곡선 세계선 필요 없단 소방이죠). 무기는 달라졌어도 발사 방아쇠 스위치인 `predict()` 함수는 LDA 형님 쏠 때랑 1도 안 틀리고 똑같이 통일된 방식(fashion) 으로 찰지게 탁탁 잡아 돌아갑니다!

```python
In [36]: qda_pred = qda.predict(X_test)
confusion_table(qda_pred, L_test)
```

```python
Out[36]: Truth      Down   Up
Predicted            
Down         30   20
Up           81  121
```

Interestingly, the QDA predictions are accurate almost 60% of the time, even though the 2005 data was not used to fit the model. 
야생의 모의고사 실전 테스트 성적표가 터졌습니다! 채점 판결 스코어가 무지 흥미로운 반전을 그립니다! 세상에나 마상에나, 2005년도 실전 종이 쪼가리들을 훈련 진입 때 단 한 장 한 톨도 슬쩍 컨닝 구경조차 못 했음에도 불구하고, 이 곡선 폭격기 QDA 예측 머신은 수능 시험 타율을 **무려 60% 가까운 영점 명중률 적중 결괏값**으로 기막히게 미친 듯 터뜨려 스매싱해 버렸습니다!

```python
In [37]: np.mean(qda_pred == L_test)
```

```python
Out[37]: 0.5992063492063492
```

This level of accuracy is quite impressive for stock market data, which is known to be quite hard to model accurately. This suggests that the quadratic form assumed by QDA may capture the true relationship more accurately than the linear forms assumed by LDA and logistic regression. However, we recommend evaluating this method’s performance on a larger test set before betting that this approach will consistently beat the market!
이 60% 급의 적중 타율 성적표가 얼마나 무시무시한 수치냐면, 애초에 정확히 모델로 씹어 삼키기란 악마도 불가능한 최상급 기괴한 난이도로 악명 높은 이 막장 '주식 시장(stock market) 데이터' 바닥에서는 실로 입이 떡 벌어지는(quite impressive) 극강의 레전드 감동 명중률입니다!! 이 짜릿한 승리 스코어는 우리에게 아주 거대한 통찰을 시사합니다. 그동안 LDA나 로지스틱 회귀 몽둥이들이 들이밀던 그 융통성 없는 뻣뻣한 억지 일자 직선(linear) 형태 잣대 조각들보다, 이 QDA 녀석이 탑재한 유연한 뱀파이어 **'이차 곡선(quadratic) 폼(form) 형태' 야말로 주식 시장 속 그 복잡 다 변태 같은 은밀하고도 진짜 진실 된 '찐 유착 관계' 를 훨씬 더 예리하고 날카롭게 적중 조준 포착(capture) 해 냈을지 모른다는 추론 폭발**입니다!  하지만! 너무 뽕에 취해 흥분해서 당신의 전 재산을 들고 "이 모델 기계만 있으면 난 죽을 때까지 일관성 있게(consistently) 주식 시장 타짜들을 모조리 개박살 물리칠(beat the market) 수 있다!" 며 도박장에 베팅(betting) 뛰어들기 전에, 제발 더 거대하고 빡센 다른 수능 시험장(larger test set) 에다 굴려보면서 이 녀석의 실전 검증 타격 맷집 평판 성적을 더 처절하게 테스트해 보길 뼛속 깊이 간곡히 추천하고 권고하는 바입니다! (돈 잃고 이 책 탓하지 마십시오!)

---

## Sub-Chapters

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/trans2.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/trans2.html)
