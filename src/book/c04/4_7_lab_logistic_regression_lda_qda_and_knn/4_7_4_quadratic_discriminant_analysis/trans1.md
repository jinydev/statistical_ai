---
layout: default
title: "trans1"
---

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/trans1.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.4 Quadratic Discriminant Analysis
# 4.7.4 이차 판별 분석

We will now fit a QDA model to the `Smarket` data.
우리는 이제 `Smarket` 데이터에 단조롭지 않은 QDA 모델을 적합시킬 것입니다.

QDA is implemented via `QuadraticDiscriminantAnalysis()` in the `sklearn` package, which we abbreviate to `QDA()`.
QDA 분석 체계는 `sklearn` 패키지 모듈 구성 안의 `QuadraticDiscriminantAnalysis()` 도구를 통하여 구현 산출되며(implemented), 우리는 편의를 위해 이것을 짧게 `QDA()` 로 축약 부릅니다.

The syntax is very similar to `LDA()`.
기계 작동 문법 구문(syntax) 패턴은 이전의 `LDA()` 와 그 형식이 매우 유사합니다.

```python
In [33]: qda = QDA(store_covariance=True)
qda.fit(X_train, L_train)
```

```python
Out[33]: QuadraticDiscriminantAnalysis(store_covariance=True)
```

The `QDA()` function will again compute `means_` and `priors_`.
`QDA()` 함수 머신은 데이터 훈련 조작을 통하여 앞서처럼 다시 `means_` 스탯 속성과 `priors_` 고유 속성치들을 내부에 자동으로 계산해(compute) 저장해 냅니다.

```python
In [34]: qda.means_, qda.priors_
```

```python
Out[34]: (array([[ 0.04279022,  0.03389409],
                 [-0.03954635, -0.03132544]]),
          array([0.49198397, 0.50801603]))
```

The `QDA()` classifier will estimate one covariance per class.
작업 진행상 특수하게 이 `QDA()` 분류 예측 시스템기 장치는 반드시 구역 각 클래스당 한 개씩의 독립된 할당 공분산(covariance) 결괏값을 내부적으로 개별 분리 추정할(estimate) 것입니다.

Here is the estimated covariance in the first class:
여기 추출 출력 산출된 값은 그렇게 분리된 첫 번째 지목 클래스 내의 개별 추정된 고유 공분산 도출 측정 값입니다:

```python
In [35]: qda.covariance_[0]
```

```python
Out[35]: array([[ 1.50662277, -0.03924806],
                [-0.03924806,  1.53559498]])
```

The output contains the group means.
이 속성 결괏값 도출 출력물은 여전히 분류된 각 통계 그룹의 도출 평균들(group means) 요약 데이터를 포괄 포함 보존합니다.

But it does not contain the coefficients of the linear discriminants, because the QDA classifier involves a quadratic, rather than a linear, function of the predictors.
그러나 놀랍게도 그것 출력 체계 결과 기판 내에서는, 이전과 달리 선형 예측 도출 판별식들의 단원 가중치 계수들(coefficients of the linear discriminants)을 전혀 관측 포함 발견되지 않는데, 그 주된 기전 원인은 특수한 QDA 단독 분류 장치가 기동 작동 투입 시 단순한 직선적 선형 기반의 식이 아니라 오히려 유연한 다변량 분류 예측 구조 변수들의 거대 이차형 곡선(quadratic) 구조 함수 수식 공식을 자기 내부적으로 필수 채택 포함하여 연산 수반(involves) 작동하기 때문입니다.

The `predict()` function works in exactly the same fashion as for LDA.
하지만 겉보기 조작 방식인 실전 타격 `predict()` 예측 구동 함수 조작 구조 절차는, 기존 LDA 사용 작동 방식에서와 구문상 정확히 일치 똑같은 동일한 조작 작동 방식(fashion) 절차로 일치 구동하며 기능적 기동 작동합니다.

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
매우 흥미롭게도(Interestingly), 비록 이 기계의 훈련 적응 적합 시 단 한 번도 사전 유출용 검정용인 타겟 2005년의 실전 미래 예측 데이터가 기계 모의 모델 훈련 모델 적합 과정에 일절 단 하나도 섞여 유입 사용되지 않았음에도 불구하고, 최종 실전 투입 결과 전산 분석된 이 QDA 모델 장치의 도출 실전 예측 정확도 타점은 1년 시간의 전체 도박 중 거의 놀랍게도 무려 대거 60%나 도달하며 정확명중 전개를 이룹니다(accurate).

```python
In [37]: np.mean(qda_pred == L_test)
```

```python
Out[37]: 0.5992063492063492
```

This level of accuracy is quite impressive for stock market data, which is known to be quite hard to model accurately.
기계가 도출 산출해 낸 이러한 성능 수준급 의 엄청난 파괴적 분류 체계 측정 정확도(accuracy)는, 본래 통계 분석상 결코 정확하게 모델링하고 모의 단적으로 기계 파악을 성립하기가 도저히 극악무도하게 매우 어려운(hard) 불가능의 영역인 것으로 세상 논리에 매우 널리 익히 통계상으로 알려진 변동성 거대 주식 증권 시장 데이터 관측 기반 실체에 대해서는, 사실상 꽤 엄청난 수준의 상당히 매우 이례적이고 기괴하게 놀랍고 성과 인상적인(impressive) 수치 타점 도출 결과입니다.

This suggests that the quadratic form assumed by QDA may capture the true relationship more accurately than the linear forms assumed by LDA and logistic regression.
이 거대 적중 결과 팩트 파편이 시사하는 바는 바로 유연하게 작동하는 기계인 QDA 모델 시스템 모형 기판에 의해 강제 수학적으로 가정 채택 추정 설계 채택된 곡선의 이차형 단층 공식 형태(quadratic form) 조립 구조 판별 구조 구동 체계 방식 자체 가, 오히려 이전 단원 과거의 뼈대 경직 선형된 이전 구도의 무식한 LDA 모형이나 단조롭고 무식한 로직 조작 단조 로지스틱 회귀 계산 단위 추정 체제 로직 기계에 의해 확고히 강압 일괄적으로 융합 가정 채택되었던 평면 스키마 선형 직선 예측 형태들(linear forms) 보다도 오히려, 어쩌면 내부 비밀 패턴 진리의 참된 무구한 주가 예측 연관 인과 변수들의 숨겨진 연동 관계(true relationship) 실체 지표 흐름을 통계적으로 한층 더 월등하게 정밀 파악하고 미세하고 더 섬세하게 정확하게(accurately) 패턴 포착 탐지(capture) 해서 산출해 낼 수도 있다는 미지의 무구한 통계 맹점을 극도로 강하게 시사합니다(suggests).

However, we recommend evaluating this method’s performance on a larger test set before betting that this approach will consistently beat the market!
그러나 통계학도, 우리는 여러분이 도박판 시장에서 이 알량한 통계 투기 기법 접근법 단일 모델 조작 방식이 시종일관 지속적으로(consistently) 통계 시장 변동 장세를 완전히 확실히 상회해 전복 이기고 절대 붕괴 물리칠(beat the market) 절대 법칙일 것이라고 맹신하여 현실 전재산 투입 확신 베팅(betting) 조작 거래라는 매우 극단적인 큰 도박을 섣부르게 맹목 전개 걸기 이전에, 반드시 이론적 스키마 차원에서 이와 동류 파생의 훨씬 엄청나게 배수로 더 방대한 크기 제원의 다른 초대량 모의 실전 테스트 검정 시뮬레이터 세트(test set) 장치상 환경 기반 속에서 이 통계 수학적 예측 작동 메서드의 진짜 확실성 있는 실전 모의 생존 실성능(performance) 도출 결과 전개를 냉정하게 거듭 재차 모의 반복 평가(evaluating) 해 보는 사전 필수 주의 및 자제력 검토를 강력히 필수로 권장(recommend) 경고 합니다!

---

## Sub-Chapters

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/trans1.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/trans1.html)
