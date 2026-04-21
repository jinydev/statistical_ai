---
layout: default
title: "trans1"
---

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/trans1.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.7.3 Linear Discriminant Analysis
# 4.7.3 선형 판별 분석

We begin by performing LDA on the `Smarket` data, using the function `LinearDiscriminantAnalysis()`, which we have abbreviated `LDA()`.
우리는 `LDA()` 로 짧게 축약해 둔 `LinearDiscriminantAnalysis()` 함수를 사용하여 `Smarket` 데이터에 대해 선형 판별 분석(LDA)을 수행함으로써 시작합니다.

We fit the model using only the observations before 2005.
우리는 오직 2005년 이전의 수집 관측치들만을 엄선 사용하여 모델을 모의 적합시킵니다.

```python
In [22]: lda = LDA(store_covariance=True)
```

Since the `LDA` estimator automatically adds an intercept, we should remove the column corresponding to the intercept in both `X_train` and `X_test`.
`LDA` 추정기는 전산 과정상 자동으로 절편(intercept)을 추가하므로, 우리는 `X_train` 과 `X_test` 모두에서 강제로 기존 절편에 해당하는 열(column) 변수를 반드시 수동 제거해야만 합니다.

We can also directly use the labels rather than the Boolean vectors `y_train`.
우리는 또한 모호한 부울(Boolean) 기호 벡터들인 `y_train` 대신 직접적으로 명시된 반응 레이블들을 지정 사용할 수 도 있습니다.

```python
In [23]: X_train, X_test = [M.drop(columns=['intercept']) for M in [X_train, X_test]]
lda.fit(X_train, L_train)
```

```python
Out[23]: LinearDiscriminantAnalysis(store_covariance=True)
```

Here we have used the list comprehensions introduced in Section 3.6.4.
여기서 우리는 단원 3.6.4에서 소개되었던 특별 파이썬 구문인 리스트 내포(list comprehensions) 기법들을 적용 다용하여 사용했습니다.

Looking at our first line above, we see that the right-hand side is a list of length two.
바로 위의 우리 코드 첫 번째 줄을 시계열 주의 깊게 살펴보면, 우리는 바로 우변(right-hand side) 항이 길이 2의 배열 리스트(list) 구성 요소임을 확연히 볼 수 있습니다.

This is because the code `for M in [X_train, X_test]` iterates over a list of length two.
이것은 반복문 코드 `for M in [X_train, X_test]` 가 길이 2의 작은 리스트에 대해 전체를 순회 돌며 반복 지정(iterates) 하기 때문입니다.

While here we loop over a list, the list comprehension method works when looping over any iterable object.
이 지정 범위 내에서 우리가 단일 리스트 배열에 대해 루프를 돌리는 반면에, 강력한 리스트 내포(list comprehension) 접근 메서드는 어떠한 반복 가능한 지정 객체(iterable object) 위에서 루핑(looping) 할 때도 일관되게 잘 작동합니다.

We then apply the `drop()` method to each element in the iteration, collecting the result in a list.
우리는 그런 다음 연산 반복(iteration) 내의 각 종속 요소들에 파이썬 `drop()` 메서드를 일일이 직접 적용하고, 그 도출 결과를 하나의 단일 리스트에 수집 모아 담습니다.

The left-hand side tells `Python` to unpack this list of length two, assigning its elements to the variables `X_train` and `X_test`.
좌변(left-hand side) 구조는 `Python` 환경에 지시하여 요소 길이를 2로 지닌 이 단일 리스트 묶음을 압축 해제(unpack) 하도록 하고, 나뉜 그 분리된 요소들을 각각의 개별 변수 지정 `X_train` 과 `X_test` 변수 요소 값들에 일대일로 할당(assigning) 합니다.

Of course, this overwrites the previous values of `X_train` and `X_test`.
물론, 이 동작 결과는 데이터 변수인 `X_train` 과 `X_test` 의 이전 데이터 객체 값들을 전면적으로 완전히 덮어씁니다(overwrites).

Having fit the model, we can extract the means in the two classes with the `means_` attribute.
모델 기계를 우선적으로 적합시키고 나면, 우리는 `.means_` 속성 지표를 사용하여 산출된 각 두 분류 클래스들 그룹 내에 도출된 개별적 도출 평균(means) 수치들을 객관적으로 추출 산출할 수 있습니다.

These are the average of each predictor within each class, and are used by LDA as estimates of $\mu_k$.
이런 도출 요소들은 각 구분 속성 클래스 집단 내부 안에 계산된 각 타겟 입력 예측 변수의 산출 평균(average) 치수들이며, LDA 내부 통계학 전산 논리에 의해 강제 측정으로 공식 파라미터 $\mu_k$ 들의 모의 추정치들(estimates) 로서 치환 강제 실용 활용 사용됩니다.

These suggest that there is a tendency for the previous 2 days’ returns to be negative on days when the market increases, and a tendency for the previous days’ returns to be positive on days when the market declines.
이 추출 점수들은 향후 주식 시장이 지표상 상승(increases) 국면 상황 발생한 단일 날들에는 모델 예측상 이전 2일간의 단절 목표 과거 일일 수익률(returns) 치수 기록들이 마이너스 음수(negative)를 강력히 기록하는 지배적 통계 경향성(tendency)이 나타나고 있으며, 반면 시장 지표가 침체 하락(declines) 발생한 날들 장세에는 도리어 기존 역으로 이전 날들의 단절 수익률 지표들이 플러스로써 양수(positive) 반환치를 기록하는 이상한 경향성 징후 체계가 짙게 존재함을 확연하게 부분 시사합니다.

```python
In [24]: lda.means_
```

```python
Out[24]: array([[ 0.0426,  0.0338],
                [-0.0395, -0.0313]])
```

The estimated prior probabilities are stored in the `priors_` attribute.
사전에 통계 예측 평가 모형으로 추정된 강력한 사전 확률들(prior probabilities) 도출 양 요소의 몫 데이터 수치는 통계 작동 모형의 `.priors_` 속성 인덱스 메모리 구조 내에 보존 저장됩니다.

The package `sklearn` typically uses this trailing `_` to denote a quantity estimated when using the `fit()` method.
프로그래밍 도구 패키지 라이브러리인 `sklearn` 모듈 은 전형적으로 대개 통상 `fit()` 추정 계산 적합 메서드를 강제 구동 사용할 때 도출 산출 발생하는 결과물 양(quantity) 추정치 들을 확증 구분 표기하기 위해, 특별히 관례로 이러한 변수명 뒤에 붙는 꼬리표 기호 특수 문자 `_` 표식 언어를 고유 변별 부호 기호로 지정 사용합니다.

We can be sure of which entry corresponds to which label by looking at the `classes_` attribute.
우리는 정확하고 확실하게 각 도출 스코어 요소 정보 항목(entry) 배열 인덱스 체계 데이터가 대체 순차적으로 어느 분리 예측 레이블 지표 값에 짝지어 대응 매칭하는지 확신 지어 구분 알기 위해 모의 기계의 독립 `.classes_` 속성 배열 구조를 눈여겨 들여다봄으로써 확실히 안전히 파악 상호 추론 구분할 수 있습니다.

```python
In [25]: lda.classes_
```

```python
Out[25]: array(['Down', 'Up'], dtype='<U4')
```

The LDA output indicates that $\hat{\pi}_{Down} = 0.492$ and $\hat{\pi}_{Up} = 0.508$.
반환된 확인 통계 LDA 기계 구동 출력물은 수치 지표 파악상 $\hat{\pi}_{Down} = 0.492$ 그리고 상승 확률 도출 $\hat{\pi}_{Up} = 0.508$ 수치 임을 데이터로 정확하게 분명히 나타냅니다(indicates).

```python
In [26]: lda.priors_
```

```python
Out[26]: array([0.49198397, 0.50801603])
```

The linear discriminant vectors can be found in the `scalings_` attribute:
기계 내에서 조작 설계된 구조 선형 판별 벡터(linear discriminant vectors) 부품 조각들은 모형 안의 내부 `.scalings_` 정보 제공 속성 지표 안에서 필히 강제적으로 도출 특정 발견 전산 획득 될 수 있습니다:

```python
In [27]: lda.scalings_
```

```python
Out[27]: array([[-0.64201906],
                [-0.51352928]])
```

These values provide the linear combination of `Lag1` and `Lag2` that are used to form the LDA decision rule.
이 모의 확보 도출 산점 결괏값 수치 요소들은 모조리 총합 하여 그 거대한 상위 LDA 모델의 본질 결정 규칙(decision rule) 체제를 확립 창출 생성 전개 형성하기 위해 조립 투입 기초 사용되는 핵심 근간 속성 변수 `Lag1` 그리고 종속 `Lag2` 지표 간의 최종 추출 부분 집합 선형 결합(linear combination) 합산식 공식을 우리 기계 산술 단에게 명확하게 최종 제공(provide) 합니다.

In other words, these are the multipliers of the elements of $X = x$ in (4.24).
더욱더 확연히 단언코 다시 말해 강조하자면, 이 점수 지표들 도출 부품 조각 계수들은 전 단원 (4.24) 공식 조립 파편들 본문 안에서 1차 단조 산술 요소식 기호 $X = x$ 를 명시 대변 지칭하는 투입 요소 인자들의 곱셈 승수들(multipliers) 파라미터 계수 가중치 스탯 자체입니다.

If $-0.642 \times Lag1 - 0.513 \times Lag2$ is large, then the LDA classifier will predict a market increase, and if it is small, then the LDA classifier will predict a market decline.
결론적으로 철저한 연산 기계론적 등식 판별 로직상으로 만약 주어진 계산식 공식인 $-0.642 \times Lag1 - 0.513 \times Lag2$ 단위 선형 대입 조합 합산식 결괏값이 최종적으로 통계상 더 크게(large) 산출 계산 도출되면, 즉각 망설임 판단 없이 시스템 LDA 분류기 장치는 지체 없이 증시 시장 지표의 상승장(market increase) 도래를 확신 판단하여 단언 예측할 것이며, 그리고 만약 모의 공식 산술 결괏값이 도출 기작 스코어가 적게 축소 도출 결론 산술(small) 되면 그때 기점은 역으로 LDA 자동 분류 시스템 기작 로직이 무참히 가차 없이 증시 시장 장세 판도의 향상 없는 떡락 하락(decline) 곡선 전개 방향성을 여지없이 단언 지어 특정 방향 예측 도출 판단 지시 하달 수행할 것입니다.

```python
In [28]: lda_pred = lda.predict(X_test)
```

As we observed in our comparison of classification methods (Section 4.5), the LDA and logistic regression predictions are almost identical.
우리가 본질적으로 이전 거대 챕터 단원 4.5 항의 수많은 통계 판별 분류 다중 예측 기법 및 메서드들의 대대적 전면 비교군 성립 성능 대전 구도 기획 장 테이블 환경 속에서 객관적인 눈초리로 사전에 미리 주의 깊게 파악 탐지 관측(observed) 결론지어 보았듯이 거시적 비교 우위 성능 판별 구도 양상 결과에서, 지금의 산출 LDA 예측 추정 타점 성적 결과 도출과 또 다른 동일 비교 대조군 부류 로지스틱 회귀 모델 장치 시스템 기동의 쌍벽 파편 예측치 결괏값 산출치 판별 타격 스코어 예측치 들 기록 비교 결과는 대개 모조리 모의 서로 간의 어떠한 확연한 특이 구분이 판별 분간 불가할 만큼 거의 복사본의 쌍둥이 구조로 서로 대부분 매우 대단히 전격 흡사하여 본질적으로 거의 동등 수준으로 동일합니다(identical).

```python
In [29]: confusion_table(lda_pred, L_test)
```

```python
Out[29]: Truth      Down   Up
Predicted            
Down         35   35
Up           76  106
```

We can also estimate the probability of each class for each point in a training set.
우리는 기계 망라 계산을 통해 모조리 추가적으로 한 단계 더 나아가 추출된 과거 훈련 모의 전산 세트 표본 집단 데이터 바운더리 내부 안의 지정 각 도출 특정 개별 위치 고유 단위 점(point) 하나하나 국지적 표본 단서 각 조건들 개별 에 대하여 배당 분류 도출 지정되는 그 각각 배당 팀 소속 후보 속성 클래스들의 전격 분류 배정 확률 스코어(probability) 자체 단위 도 국소 산출 판별 측정 정밀 개별 임의 핀포인트 계산 추정해 낼 수도 (estimate) 존재 합니다.

Applying a 50% threshold to the posterior probabilities of being in class one allows us to recreate the predictions contained in `lda_pred`.
이론 통계 사후 확률 체제 스코어 산점 기준에서 파악할 때 모델 첫 번째 도출 주도 상위 그룹 타깃 클래스 분표 그룹 진영 1 집군에 강제적으로 데이터가 온전히 쏠려 지정 포함 안착 속해 귀속 있을 판별 확률이라는 사후 확률들(posterior probabilities) 전산 점수 조각 파편들에 대해 임의로 고정 50% 임계치 컷오프 커트라인 구간(threshold) 제한 조건선을 강매 조율 부여 개입 강제 적용하는 전산 치환 투입 과정 작동은, 역으로 치환 구동하여 우리가 바로 직전 앞에서 이미 만들어낸 변환 이전 초기 결과 단서인 예측 벡터 `lda_pred` 객체 통계 배열 변수에 포획 저장 압축 파편 포함 보존 보유되어 있던 과거 동일 첫 똑같은 도출 예측치 판별 도출 분류 기록 파편 점수군 요소 들을 다시 거슬러 역추적 똑같이 판별 기준 구동을 반복 지시해 완벽한 복사판 확률 복제 체계 창조 기점 재창조 유도(recreate) 연산 재현을 해 내도록 구동 허용 기능 조작 구현 길을 조작 터줍니다 능동 지원 발동 합니다.

```python
In [30]: lda_prob = lda.predict_proba(X_test)
np.all(
    np.where(lda_prob[:,1] >= 0.5, 'Up','Down') == lda_pred
)
```

```python
Out[30]: True
```

Above, we used the `np.where()` function that creates an array with value `'Up'` for indices where the second column of `lda_prob` (the estimated posterior probability of `'Up'`) is greater than 0.5.
바로 전 구동 위쪽 기계 조작 박스 블록에서 코딩으로, 우린 조작 `lda_prob` 변수의 추출 지정 2번째 강제 지정 추출 타점 열(`'Up'` 상승 타깃 목표 예측 결과치 방향 에 대한 맹목적인 강제 확증 수치 추산 도출 추정 사후 기점 계산 최종 확률 판별 도출량 인덱스) 지표 수치 기록치 스코어 값이 정량 단위 스코어 0.5 점을 넘을 때 이를 무조건 강압 유효 기준 통과 커트라인 수치로 취합하여, 측정치가 그것보다 정립 기준선 스코어 이상 단연코 큰(greater) 산술 통계 조건을 통과 달성 도달 만족하는 도식화된 요소 행 인덱스 표본(indices)들만의 아주 국소적 일부 파편 인덱스 집군 부분 구역 공간 란 한하여 한정적으로 고립 제한적 표기 타깃 적용으로써 조준 타겟 표본 대체 문자열 `'Up'` 이란 텍스트 정적 고정 치 입력 삽입 값(value) 을 강압 부착 삽입 적용 치환 억지 강제 덮어쓰기 지정 포함 탑재 강압 부여 소유하는 또 다른 변종 진입 종속 파편 산출 특수 부분 집합 단서 하위 행 배열 요소(array) 파편 단위 집단을 특정 도출 생성 재구성 산출 기능 수행 하는 파이썬 핵심 `np.where()` 기계 분별 추출 검색 치환 함수 톱니를 채택 전격 사용 조작 구동했습니다.

For problems with more than two classes the labels are chosen as the class whose posterior probability is highest:
오직 다항 종속 배정 추출 후보 클래스 집군 분류 선택지 군 소속 집단이 단순 이항 흑백 양자 분류가 아니라, 더 거대 다중 범주 종속 집합 분류인 2개 이상 종속 계층 집군 이상 후보 도출 파편 들로 더 다수 분열 도출 보유 발현 존재하는 혼잡하고 어지럽고 복잡한 실전 다항 범주 선택지 도출 문제 환경(problems) 구조 전제에 대해서 돌이켜 본 다면, 산출 기계 판독 예측 선택지 최종 판별 지목 선택 채택 라벨(labels) 후보군 낙인 선택 승자 도출 방식 구조 확정은 후보 간의 경쟁에서 개별 단수 종속 사후 스코어 판별 수치 경쟁 산출 결괏값 추정 획득 확률(posterior probability) 수치 퍼센트 득점이 타의 추종을 불허하고 개별 클래스 상호간 경합 투투 안에서 가장 독보적으로 제일 월등하고 절대 압도 최상위 우위 수치 극단치 로서 가장 타점 이 도달 높은(highest) 압승 단일 절대 최상위 1등 집군 우선 타격권 지정 특정 집군 통계 클래스 우승 그룹 으로서 오직 최종 지목 분류 분별 절대 강제 지정 경쟁 도출 선택 전담 확정 지점 배당 선택되어 질 것입니다.

```python
In [31]: np.all(
    [lda.classes_[i] for i in np.argmax(lda_prob, 1)] == lda_pred
)
```

---

## Sub-Chapters

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/trans1.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/trans1.html)
