---
layout: default
title: "trans1"
---

# **`Out[4]:`** `(263, 20)`

We first choose the best model using forward selection based on Cp (6.2). This score is not built in as a metric to `sklearn`. We therefore define a function to compute it ourselves, and use it as a scorer. By default, `sklearn` tries to maximize a score, hence our scoring function computes the negative Cp statistic.
가장 먼저 우리는 Cp (6.2) 통계 지표에 기초한 전진 선택법을 사용하여 최적의 모델을 고를 것입니다. 안타깝게도 이 평가 점수는 `sklearn` 모듈 내에 기본 지표(metric)로 내장되어 있지 않습니다. 따라서 우리는 이를 직접 계산하기 위해 고유의 함수를 한 가지 정의하고, 이를 평가 점수 산출기(scorer)로 사용할 것입니다. `sklearn`은 기본적으로 점숫값이 오르면 오를수록 이를 최대화하려 시도하는 속성이 존재하므로, 우리의 스코어링 평가 함수는 음수로 치환된 음의 Cp 통곗값(negative Cp statistic)을 산출하도록 설계됩니다.

```python
In [5]: def nCp(sigma2, estimator, X, Y):
    "Negative Cp statistic"
    n, p = X.shape
    Yhat = estimator.predict(X)
    RSS = np.sum((Y - Yhat)**2)
    return -(RSS + 2 * p * sigma2) / n
```

We need to estimate the residual variance $\sigma^2$, which is the first argument in our scoring function above. We will fit the biggest model, using all the variables, and estimate $\sigma^2$ based on its MSE.
우리는 앞서 정의한 스코어링 함수의 첫 번째 전달 인자인 잔차 분산(residual variance) $\sigma^2$을 필수적으로 추정해 내야만 합니다. 이를 위해 사용 가능한 모든 변수를 다 쓸어 담아 가장 덩치가 큰 최고 모델을 적합시키고, 이 모델의 평균 제곱 오차(MSE)를 기초로 삼아 온전한 $\sigma^2$ 값을 추정할 것입니다.

```python
In [6]: design = MS(Hitters.columns.drop('Salary')).fit(Hitters)
Y = np.array(Hitters['Salary'])
X = design.transform(Hitters)
sigma2 = OLS(Y, X).fit().scale
```

The function `sklearn_selected()` expects a scorer with just three arguments — the last three in the definition of `nCp()` above. We use the function `partial()` first seen in Section 5.3.3 to freeze the first argument with our estimate of $\sigma^2$.
함수 `sklearn_selected()`는 오로지 단 세 개의 인수만을 갖춘 평가 산출기(scorer)를 요구합니다 — 그것은 바로 위에 정의된 `nCp()` 함수의 마지막 세 매개변수와 동일합니다. 우리는 5.3.3절 파트에서 처음 구경했던 파이썬 내장 `partial()` 함수 모듈을 호출 사용하여, 우리가 추정한 통계 변수 $\sigma^2$를 가진 첫 번째 매개 변수 인수 결괏값을 단단히 고정(freeze)시켜 버릴 것입니다.

```python
In [7]: neg_Cp = partial(nCp, sigma2)
```

We can now use `neg_Cp()` as a scorer for model selection. Along with a score we need to specify the search strategy. This is done through the object `Stepwise()` in the ISLP.models package. The method `Stepwise.first_peak()` runs forward stepwise until any further additions to the model do not result in an improvement in the evaluation score. Similarly, the method `Stepwise.fixed_steps()` runs a fixed number of steps of stepwise search.
이제부터 우리는 `neg_Cp()`를 모델 선택 과정을 거칠 수 있는 합법적 평가 점수 산출기로 매핑 활용할 수 있습니다. 점수 체제와 함께 우리는 검색 전략 또한 함께 구체적으로 세팅 명시해야 합니다. 이는 `ISLP.models` 패키지 구역 내에 속해 있는 `Stepwise()` 객체를 통해 무사히 수행됩니다. 내장된 `Stepwise.first_peak()` 메서드는, 굴러가고 있는 모델에 추가적인 변수를 아무리 밀어 넣더라도 더 이상 평가 점수의 개선 효과가 생기지 않는 그 상한선 시점까지, 끝없이 전진 단계적(forward stepwise) 연산을 가동합니다. 흡사하게, `Stepwise.fixed_steps()` 메서드는 사용자가 단계적 무작위 탐색을 시도할 스텝 지정 횟수 고정값을 사전에 줘서 구동시킵니다.

```python
In [8]: strategy = Stepwise.first_peak(design,
                                       direction='forward',
                                       max_terms=len(design.terms))
```

We now fit a linear regression model with `Salary` as outcome using forward selection. To do so, we use the function `sklearn_selected()` from the ISLP.models package. This takes a model from `statsmodels` along with a search strategy and selects a model with its `fit` method. Without specifying a `scoring` argument, the score defaults to MSE, and so all 19 variables will be selected (output not shown).
이제 우리는 전진 선택법을 응용 사용하여 얻게 된 결과치 `Salary`를 가진 선형적 독립 회귀 모델을 무단 적합시킵니다. 이렇게 하기 위해서, `ISLP.models` 패키지에 종속된 `sklearn_selected()` 파이썬 함수를 가져다 씁니다. 이 객체 함수는 검색 탐색 전략 옵션과 함께 `statsmodels`로부터 원본 모델을 가져오며, 그 자체의 `fit` 메서드를 가동하여 알맞은 모델 체계를 선택합니다. 이 함수에 별도로 굳이 `scoring` 추가 인수 척도를 따로 명시해 주지 않으면, 점수의 평가지표는 디폴트 기본값인 MSE로 간주 설정되며, 따라서 도출되는 19개의 모든 변수들이 한무더기로 결과로 쏟아져 선택되고 말 것입니다 (가독성을 위해 해당 결과 출력치는 숨겼습니다).

```python
In [9]: hitters_MSE = sklearn_selected(OLS, strategy)
hitters_MSE.fit(Hitters, Y)
hitters_MSE.selected_state_
```

Using `neg_Cp` results in a smaller model, as expected, with just 10 variables selected.
예상했던 대로 우리가 정의 설정 세팅한 `neg_Cp`를 사용하자 모델은 고작 단 10개의 변수 인자만을 선택한 더 아담한 크기의 모델이라는 결과로 도출되었습니다.

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
기저의 지표인 Cp를 사용하는 것 외에도 또 다른 대안으로, 전진 선택 무대 세팅에서 원하는 최적 모델을 선별하기 위해 우리는 교차 검증(cross-validation) 기법 사용을 시도해 볼 수 있습니다. 이 기법 무대를 성사시키려면, 전진 선택 중에 발견된 모델들의 이행 전체 진행 궤적 정보들(full path)을 올바르게 저장해 두고 그들 각각에 대해 도출 결과를 예측할 수 있는 특별한 내부 메서드가 필요합니다. 이는 `ISLP.models` 모듈에 소속된 `sklearn_selection_path()` 추정기(estimator) 객체를 이용하면 수행 달성할 수 있습니다. `ISLP.models`의 이 `cross_val_predict()` 함수 호출 메서드는 궤적을 밟고 가는 모델의 무수한 각기 객체에 대해 교차 검증된 측정 예측치들을 연산 수행하며, 이로써 모델 진행 패스를 관통하는 매 경로마다 교차 검증된 교차 오류 $\text{MSE}$를 도출 연산해 평가하게 쓰일 수 있습니다. 여기서 우선 전진 선택 전체 이행 과정을 가장 잘 적합시키는 탐색 전략 조건을 정의 세팅해 줍니다. `sklearn_selection_path()` 객체 무대에는 비록 다채롭게 구비된 다양한 매개 변수 추가 옵션 선택지들이 즐비하지만, 여기서 우리는 그저 내장된 기본 원리값(defaults)을 편하게 그대로 가져와 쓰겠으며, 이 설정은 RSS 잔차를 최대로 통제 감소시켜 주는 지점을 평가 기준으로 삼아 각 연산 단계의 모델을 포착 선택하게 됩니다.

```python
In [11]: strategy = Stepwise.fixed_steps(design,
                                         len(design.terms),
                                         direction='forward')
full_path = sklearn_selection_path(OLS, strategy)
```

We now fit the full forward-selection path on the `Hitters` data and compute the fitted values.
이제 완성된 `Hitters` 데이터 세트 궤도 위에 전체 전진 선택 도출 궤적을 씌워 적합시키고 연산 도출된 예측 적합 값들을 직접 계산하여 봅니다.

```python
In [12]: full_path.fit(Hitters, Y)
Yhat_in = full_path.predict(Hitters)
Yhat_in.shape
```

```
Out[12]: (263, 20)
```

This gives us an array of fitted values — 20 steps in all, including the fitted mean for the null model — which we can use to evaluate in-sample MSE. As expected, the in-sample $\text{MSE}$ improves each step we take, indicating we must use either the validation or cross-validation approach to select the number of steps. We fix the y-axis to range from 50,000 to 250,000 to compare to the cross-validation and validation set $\text{MSE}$ below, as well as other methods such as ridge regression, lasso and principal components regression.
이 결과 연산 도출은 우리에게 총 20개의 가동 스텝으로 도출된 궤도의 —여기엔 아주 비좁게 무(null) 모델상에서 적합 파생된 평균 수치 또한 끼어 있습니다— 적합 수치 배열을 쥐여줍니다. 우리는 이것을 고스란히 끌어와 모델 투입 표본 내 오차율 평가지표인(in-sample MSE)을 평가 측정하는 데 바로 써먹을 수 있습니다. 예상했다시피, 모델 전진 선택 단계가 하나둘 밟아 점진 진척 전진할 때마다 기록되는 내부 측정 MSE 수치 점수는 계속 좋아지고 개선되며, 이는 곧 이 측정치에만 수치를 평가 의존할 것이 아니라 최종적으로 전체 단계를 몇 번 가동할 것인지 결정판단 하기 위해선 무조건 외부 모델 검증기(validation) 혹은 교차 검증 접근법을 수합 사용해야만 한다는 것을 암시 시사합니다. 우리는 y축 측정 범위 눈금 규격을 50,000에서 시작해 250,000으로 고정 제한하여 묶어두었습니다. 추후 교차 검사 연산과 모델 검증 모의 도출 단면이 산출할 각각의 MSE 성과와 기타 무수한 측정 모델(능선 회귀, 라쏘, 주성분 회귀 결괏값 등) 지표들과 일관적으로 나란히 공평 비교를 수행하기 위한 전제 조건 조치입니다.

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
