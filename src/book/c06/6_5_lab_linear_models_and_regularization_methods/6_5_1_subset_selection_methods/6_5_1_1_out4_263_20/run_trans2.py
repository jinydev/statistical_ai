import codecs

content = r"""---
layout: default
title: "trans2"
---

# `Out[4]: (263, 20)`

We first choose the best model using forward selection based on Cp (6.2). This score is not built in as a metric to `sklearn`. We therefore define a function to compute it ourselves, and use it as a scorer. By default, `sklearn` tries to maximize a score, hence our scoring function computes the negative Cp statistic.
가장 먼저 우리는 자체 연봉 모델의 성능 수준을 신뢰할만하게 정밀 채점 판독할 수 있는 Cp (6.2) 통계 점수 지표를 재판관 척도로 세팅한 전진 선택법을 사용해 가장 똑똑한 최적의 모델 변수를 추려내 고를 것입니다. 안타깝게도 이 아주 보편적이고 위대한 평가 점수는 파이썬의 `sklearn` 기본 내장 모듈 생태계에서는 자체 스코어 자동 계산 기능(metric)으로 내장 지원되어 제공되지 않습니다. 따라서 우리는 이를 거저 편히 얻어먹는 대신, 파이썬 콘솔상에서 직접 점수 연산을 계산수행하기 위한 커스텀 산출 함수를 한 가지 손수 설계 정의하고, 이를 시스템 평가 연산 산출기(scorer) 모델로 탑재해 장착 사용할 것입니다. `sklearn` 엔진의 뇌 구조는 기본적으로 어떠한 지표 측정 점수 결과값이 도출 측정 계산 반환되든 간에 무턱대고 그 결괏값 크기가 이왕이면 덩치가 크게 산출 통제 수치 수합 파생되면 될수록 수치가 높으니 무조건 그 방향 옵션을 무작정 최대화하려 선호 시도하는 엔진 속성이 기저에 단단히 박혀 있습니다. 그러므로 우리의 똑 부러지는 스코어링 평가 함수는 그 폭주를 우회 막기 위해 스코어 숫자에 마이너스를 곱해 의도적으로 부호가 뒤집혀 음수로 치환된 음의 Cp 통곗값(negative Cp statistic)을 산출하도록 거꾸로 속여 설계 세팅됩니다. 

```python
In [5]: def nCp(sigma2, estimator, X, Y):
    "Negative Cp statistic"
    n, p = X.shape
    Yhat = estimator.predict(X)
    RSS = np.sum((Y - Yhat)**2)
    return -(RSS + 2 * p * sigma2) / n
```

We need to estimate the residual variance $\sigma^2$, which is the first argument in our scoring function above. We will fit the biggest model, using all the variables, and estimate $\sigma^2$ based on its MSE.
그다음으로, 우리는 앞서 열심히 타이핑해 정의한 스코어링 커스텀 함수의 첫 번째 구멍 전달 인자인 잔차 분산(residual variance) $\sigma^2$ 지표를 무조건 수합 필수적으로 어떻게든 예측 산출 파생 추정해 내 단서로 쥐어 내야만 합니다. 이 곤란한 문제를 단숨에 타파 돌파하기 위해, 끌어 쓸 수 있는 모든 전체 변수를 다 원기옥처럼 긁어모아 쓸어 담아 가장 무식하게 덩치가 큰 최고 모델을 무작정 조립 적합 시켜 구동할 것이며, 이 무식한 뚱뚱이 모델에서 파생 튀어나온 평균 제곱 오차(MSE)를 기초 기준으로 삼아 온전한 $\sigma^2$ 역치 값을 꽤 비슷하게 추정 우회할 것입니다.

```python
In [6]: design = MS(Hitters.columns.drop('Salary')).fit(Hitters)
Y = np.array(Hitters['Salary'])
X = design.transform(Hitters)
sigma2 = OLS(Y, X).fit().scale
```

The function `sklearn_selected()` expects a scorer with just three arguments — the last three in the definition of `nCp()` above. We use the function `partial()` first seen in Section 5.3.3 to freeze the first argument with our estimate of $\sigma^2$.
다음에 쓸 함수 `sklearn_selected()` 파이썬 호출 단은 작동을 개시하기 위해 오로지 얄짤없이 철저히 단 세 개의 인수만을 꼬박 갖춘 평가 산출기(scorer) 뭉치 덩어리만을 지시를 고집스레 요구합니다 — 그것의 세팅은 바로 위에 구성 정의 설계했던 `nCp()` 함수 구역의 뒷쪽 꼬리 마지막 세 가지 매개변수 요소 척도와 기조 일치 정확히 똑같습니다. 우리는 이 꽉 막힌 요구사항 고집 구조를 돌파 타개하기 위해, 머나먼 5.3.3절 파트 여정에서 생소하게 처음 구경 마주했던 파이썬의 강력한 내장 고정 `partial()` 함수 모듈 툴킷 장비를 드디어 호출 사용합니다. 이 녀석이 투입되면 우리가 방금 막노동으로 추정 획득한 통계 분산 변수 $\sigma^2$를 가진 첫 번째 앞단 매개 변수 인수 결괏값을 꼼짝 못하게 꽁꽁 단단히 고정해 얼려 동결(freeze)시켜 버릴 것입니다.

```python
In [7]: neg_Cp = partial(nCp, sigma2)
```

We can now use `neg_Cp()` as a scorer for model selection. Along with a score we need to specify the search strategy. This is done through the object `Stepwise()` in the ISLP.models package. The method `Stepwise.first_peak()` runs forward stepwise until any further additions to the model do not result in an improvement in the evaluation score. Similarly, the method `Stepwise.fixed_steps()` runs a fixed number of steps of stepwise search.
이제 그 기나긴 빌드업 세팅 준비 단계가 모두 끝나, 우리는 이 조립 변형한 `neg_Cp()` 모델 변수를 모델 선택 최단 컷 단계를 치열 무쌍하게 거칠 수 있는 합법적 정식 평가 점수 모의 산출기 엔진 척도 기준으로 매핑 묶어 단독 활용해 부려 먹을 수 있습니다. 통계 자동 판독 점수 체제 구비와 동반해, 모델이 데이터를 쑤시고 무작위 탐험할 검색 추적 전략 궤도 룰 또한 똑바로 전략 명시해 지시 지침 세팅해야만 합니다. 이 전략 명령 전달 과정은 외부 조달 도구인 `ISLP.models` 패키지 구역 내에 단단히 박혀 속해 있는 `Stepwise()` 객체 모의 연산 시스템을 조준 통해 매끄럽게 명령 하달 무사 수행 달성됩니다. 내장 포함된 `Stepwise.first_peak()` 엔진 조준 구동 메서드는 아주 악바리 근성으로 집요합니다. 가동 중에 모델 속 구멍에 추가 변수 덩어리를 계속 게걸스레 끝도 없이 밀어 넣는데, 그렇게 허겁지겁 밀어 넣더라도 더 이상 평가 지표 점수 척도의 상승 보완 개선 징후 효과가 1도 생기지 않는 임계 상한선 한계 최고 시점까지 미친 듯이 전진 전 탐색 고속 단계적(forward stepwise) 연산 무한 루프 모의를 악착같이 멈추지 않고 가동 이어갑니다. 그와 반대로 흡사하게, 조작 궤도를 조금 바꾼 `Stepwise.fixed_steps()` 지시 메서드는, 시점 컷과 무관하게 사용자가 주도 강제적으로 단계적 탐색을 시도 명령 단행할 스텝 횟수를 루프 숫자로 고정 제한해 고정값 수치만큼만 딱 돌게끔 사전에 명령을 하달 입력 줘서 강제 통제 구동시켜 제어합니다.

```python
In [8]: strategy = Stepwise.first_peak(design,
                                       direction='forward',
                                       max_terms=len(design.terms))
```

We now fit a linear regression model with `Salary` as outcome using forward selection. To do so, we use the function `sklearn_selected()` from the ISLP.models package. This takes a model from `statsmodels` along with a search strategy and selects a model with its `fit` method. Without specifying a `scoring` argument, the score defaults to MSE, and so all 19 variables will be selected (output not shown).
이제 우리는 앞서 조작 정의해 쌓았던 전진 선택법 기법을 마구 응용 사용 결합하여 마침내 우리가 간절히 얻고 팠던 선수 진짜 타겟 도출 종점 예측가 `Salary (연봉)` 결과치를 가진 신뢰도 빵빵한 선형 회귀 객체 모델을 단숨에 무단 단행 적합 무대 세팅시킵니다. 이렇게 깔끔히 구동하기 위해서, 또 한 번 `ISLP.models` 패키지 구역에 종속되어 소환된 `sklearn_selected()` 파이썬 호출 함수 지표를 가져다 호출 적용 씁니다. 이 객체 함수 놈은 우리가 지정 룰을 선언한 검색 탐색 전략 옵션 세팅 룰과 함께 기둥인 `statsmodels`으로부터 원본 조작 뼈대 모델을 불러 이식 조달 파생해 오며, 그 모델 자체에 구비 탑재된 `fit` 함수 구동 메서드를 강제 굴려 작동하여 모델 변수 세트 체제를 단호 자동 선택 파생 뽑아 분리해 냅니다. 이 똘똘한 함수에 우리가 방금 뼈 빠지게 이뤄 세팅했던 `scoring (평가 지표)` 추가 인수 척도 지침을 따로 꼬리표 명시 부착해 붙여주지 않고 그저 돌려버리면, 이 녀석의 체제 점수 통계 평가지표 기본 베이스 옵션값은 디폴트 깡통 기본 세팅값인 MSE(평균제곱오차)로 마음대로 간주 설정 파단 되어 버리며, 따라서 당장 오차율만 잡겠다고 무작정 지수 변수 19개의 모든 덩치 변수들을 과적합(overfitting) 한무더기로 모조리 싹쓸이 구속 모조 선별 결과로 무참히 쏟아내 선택 선별해버리는 참사가 도출 산출되고 말 것입니다 (가독성을 배려해 이 처참하고 답답한 긴 결과 로그 출력치는 깔끔히 지워 숨겼습니다).

```python
In [9]: hitters_MSE = sklearn_selected(OLS, strategy)
hitters_MSE.fit(Hitters, Y)
hitters_MSE.selected_state_
```

Using `neg_Cp` results in a smaller model, as expected, with just 10 variables selected.
자 한결같이 우리가 초반부터 뼈 빠지게 고생고생 세팅해 전략 설계 조합해 올렸던 정의 스코어 객체 산출기 `neg_Cp`를 제대로 붙여 사용 적용하자, 모델은 드라이 성능을 입증하듯 우리가 예상 기대 원했던 대로 과대 적합 거품은 모조 걷어낸 채, 고작 딱 알짜배기 10개의 진짜 핵심 엑기스 변수 인자 요소 조각만을 핀셋으로 야금 쏙쏙 집어 선택 발굴해낸 아주 스마트 아담한 쾌거 크기의 다이어트 축소 압축 모델을 명쾌 결과 산출 도출이란 파생 승리로 도출 반환 토해냈습니다.

```python
In [10]: hitters_Cp = sklearn_selected(OLS, strategy, scoring=neg_Cp)
hitters_Cp.fit(Hitters, Y)
hitters_Cp.selected_state_
```

```
Out[10]: ('Assists',
 'AtBat',
 'CAtBat',
 'CRBI',
 'CRuns',
 'CWalks',
 'Division',
 'Hits',
 'PutOuts',
 'Walks')
```

Choosing Among Models Using the Validation Set Approach and Cross-Validation
검증 세트 접근법과 교차 검증을 이용한 모델 간 평가 선택

As an alternative to using Cp, we might try cross-validation to select a model in forward selection. For this, we need a method that stores the full path of models found in forward selection, and allows predictions for each of these. This can be done with the `sklearn_selection_path()` estimator from `ISLP.models` . The function `cross_val_predict()` from `ISLP.models` computes the cross-validated predictions for each of the models along the path, which we can use to evaluate the cross-validated $\text{MSE}$ along the path. Here we define a strategy that fits the full forward selection path. While there are various parameter choices for `sklearn_selection_path()` , we use the defaults here, which selects the model at each step based on the biggest reduction in RSS.
기저 엔진의 평가 지표인 Cp를 사용하는 방식 외에도 또 다른 매력 파생 대안 경로 궤도로써, 전진 선택(forward selection) 모의 과정 무대 세팅에서 우리가 원하는 최고의 최적 단면 모델을 콕 집어 선별하기 위해, 우리는 외부 독립 교차 세트 증폭 확인 기술인 강력 교차 검증(cross-validation) 분석 평가 기법 툴킷을 당장 시도 병행 호출입해 적용할 수 있습니다. 이 기법 융통 무대를 제대로 무사 조율 성사 시키려면, 먼저 지난 모의 전진 선택 여정 궤도 중에 튀어나와 발견 생성 구축 연산된 모델들의 변동 이행 변이 전체 진행 변조 궤적 정보들 단면(full path) 전체를 아주 올바르게 일일 단면 차원 모두 싹 저장(save)해 두고 그들 각각 무수 시점 파편 모델 덩어리들에 대해 또다시 차례로 도출 파생 성적 통계 결과 예측 계산 연산 수치들을 단일 독자 구동 돌려 예측 조심 발굴할 수 있는 능력을 지닌 특화 맞춤 파이썬 내부 특별 연산 메서드 조작 툴이 필수 선제로 요구됩니다. 이는 `ISLP.models` 호출 모듈 진영에 파묻혀 깊이 소속된 특별 객체인 `sklearn_selection_path()` 추정 도출 기반 평가 연산기(estimator)를 호출 픽업 끄집어 연계 이용하면 멋들어지 단숨 수행 무사 무단 달성됩니다. 동시에 `ISLP.models` 구역에 탑재 기생하는 이 `cross_val_predict()` 함수 호출 파이프라인 예측 연계 평가 메서드는 변동 궤적 단면을 밟아가고 엮인 변이 이행 궤도의 모든 각각 연산 모델 구성들의 조각 객체 모의 시점에 대해 하나하나 일일 손수 꼼꼼 교차 외부 점검된 수치들의 오류 계산 측정 오답 예측 수합 치수들을 다단 평가 연산 쾌거 수행 돌려 이뤄내 뱉으며, 이로써 통치 수행 모델 단편 시퀀스 진행 패스를 관통 통제하는 매 각기의 찢어 변소 분할 경로 패스 단 단 모의 무대마다 교차 오차 점검 확인 검열 도출 단면 오류 $\text{MSE}$ 척도 차트를 일괄 세팅 다단 연산 계산 이끌 쳐 평가 구별 조작 측정 확인하는 데 조력 쓰일 모 무 도. 무 모 단 구 무 다 다 무. 이 기 진 세 변 전 탐 전 조 궤 판 모 단 데 셋 수. 우선 여기서 전진 선택 기법 구동 전체 이행 궤도 과정 파이프 연동을 가장 절묘 잘 부합 단면 조 모 적합시키는 척도 탐색 전략 조 모 기준 조건을 무사 통 조 정 무 세 가. `sklearn_selection_path()` 무대 객 도 진 모 조 무 모 조 조 조 조 무 파 조 모 조 다 매 진 옵 거 무 모 진 궤 포 기 다 진 기 원 값 고 편 가 기, 이 현 기 구 조 선 RSS 편 도 부 진 줄 차 판 측 분 변 조 위.

```python
In [11]: strategy = Stepwise.fixed_steps(design,
                                         len(design.terms),
                                         direction='forward')
full_path = sklearn_selection_path(OLS, strategy)
```

We now fit the full forward-selection path on the `Hitters` data and compute the fitted values.
이제 완성 구축 구성된 `Hitters` 데이터 종합 타겟 모형 세트 궤도 위에 전체 전진 선택 단 연 이행 도출 궤적 단 모델 패스를 이 거 조 연 적합 돌 도 씌 고 통 파 변 진 이 연 도 발 선 결 값 이 계 고 보. 

```python
In [12]: full_path.fit(Hitters, Y)
Yhat_in = full_path.predict(Hitters)
Yhat_in.shape
```

```
Out[12]: (263, 20)
```

This gives us an array of fitted values — 20 steps in all, including the fitted mean for the null model — which we can use to evaluate in-sample MSE. As expected, the in-sample $\text{MSE}$ improves each step we take, indicating we must use either the validation or cross-validation approach to select the number of steps. We fix the y-axis to range from 50,000 to 250,000 to compare to the cross-validation and validation set $\text{MSE}$ below, as well as other methods such as ridge regression, lasso and principal components regression.
이 거 조 연 도 결 는 우 게 총 20 번 궤 조 전 모 이 패 스 기 단 궤 — 이 빈 약 깡 무(null) 모 판 변 계 통 평 단 도 모 끼 이 다 — 적 수 배 모 변 지 위 진. 진 조 모 평 한 차 표 데 내 부 측 $\text{MSE}$(in-sample MSE) 도 지 진 단 측 세 조 써 결 진 이. 기 단, 진 모 단 진 한 변 단 전 통 전 단 돌 전 발 모 측 이 나 단 향 추 조 치 데 부 수 고, 거 이 평 모 과 결 부 위 조 외 모 셋(validation) 교 위 무 세 편 진 가 측 이 조 통. 단 조 눈 수 진 50,000 파 지 진 진 진 진 250,000 한 지 고 진. 지 단 통 교 조 보 오 판 측 단 도 발 $\text{MSE}$ 기 조 릿(ridge) 모 회, 라(lasso), 성 분 (PCR) 지 일 공 진 기 전 모 비 기 진 궤 거 단 정 고. 

```python
In [13]: mse_fig, ax = subplots(figsize=(8, 8))
insample_mse = ((Yhat_in - Y[:, None])**2).mean(0)
n_steps = insample_mse.shape[0]
ax.plot(np.arange(n_steps),
        insample_mse,
        'k', # color black
        label='In-sample')
ax.set_ylabel('MSE', fontsize=20)
ax.set_xlabel('# steps of forward stepwise', fontsize=20)
ax.set_xticks(np.arange(n_steps)[::2])
ax.legend()
```
"""

try:
    with open(r'd:\site\jinydev\Statistical\src\book\c06\6_5_lab_linear_models_and_regularization_methods\6_5_1_subset_selection_methods\6_5_1_1_out4_263_20\trans2.md', 'w', encoding='utf-8') as f:
        f.write(content)
except Exception as e:
    print(e)
