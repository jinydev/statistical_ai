---
layout: default
title: "trans1"
---

# **`Out[31]:`** `array([231788.32])`

Obviously choosing $\lambda = 0.01$ is arbitrary, so we will use cross-validation or the validation-set approach to choose the tuning parameter $\lambda$ . The object `GridSearchCV()` allows exhaustive grid search to choose such a parameter. We first use the validation set method to choose $\lambda$ .
앞선 과정에서 살펴봤듯, 그냥 단순히 $\lambda$ 임계 변수를 $0.01$ 값으로 고집 선택하는 행위는 몹시 자의적이고 주관적인 단편 기준일 뿐입니다. 따라서 우리는 모델 성능 평가에 최적화된 튜닝 매개 파라미터 타겟인 $\lambda$를 객관적으로 선별 골라내기 위해, 체계적인 검증-세트 접근법(validation-set approach)이나 교차-검증(cross-validation) 분석 평가 기법을 적극 채용 활용할 것입니다. 이때 부려먹는 `GridSearchCV()`라는 탐색 연산기 객체 모듈은, 주어진 허용 격자망 구간 내의 모든 제약 파라미터 경우의 수를 이 잡듯이 샅샅이 뒤져 스캔하는 철저 통제형 그리드 탐색(exhaustive grid search)을 가능케 해 줍니다. 첫 시도로써, 우리는 일단 이 단일 검증 쪼개기 세트 기법 방식을 사용해 최적 $\lambda$ 변숫값을 탐색 선별해 보겠습니다.

```python
In [32]: param_grid = {'ridge__alpha': lambdas}
grid = skm.GridSearchCV(pipe,
                        param_grid,
                        cv=validation,
                        scoring='neg_mean_squared_error')
grid.fit(X, Y)
grid.best_params_['ridge__alpha']
grid.best_estimator_
```

```python
Out[32]: Pipeline(steps=[('scaler', StandardScaler()),
                         ('ridge', ElasticNet(alpha=0.005899, l1_ratio=0))])
```

Alternatively, we can use 5-fold cross-validation.
단일 검증의 대안으로써, 이번에는 5-폴드(5-fold) 교차 십자-검증(cross-validation) 시스템을 채택해 시도해 보겠습니다.

```python
In [33]: grid = skm.GridSearchCV(pipe,
                                 param_grid,
                                 cv=kfold,
                                 scoring='neg_mean_squared_error')
grid.fit(X, Y)
grid.best_params_['ridge__alpha']
grid.best_estimator_
```

Recall we set up the `kfold` object for 5-fold cross-validation on page 271. We now plot the cross-validated $\text{MSE}$ as a function of $-\log(\lambda)$, which has shrinkage decreasing from left to right.
이전 단원 교재의 271페이지 실습 랩 무대 과정에서, 이 5-폴드 교차 검증의 뼈대가 될 `kfold` 도출 객체를 저희가 미리 세팅 성립해 두었음을 잊지 말고 상기해 내시길 바랍니다. 이제 우리는 교차 검사된 $\text{MSE}$ 도표 그래프를 $-\log(\lambda)$ 수식 제약 함수로 환산하여 선분으로 그려 도출(plot) 시킬 것입니다. 이렇게 치환 조작된 도표 선분은 그래프 진행의 왼쪽에서 오른쪽 축을 향해 뻗어 갈수록 감소하는 변동 수축성(shrinkage decreasing) 특성을 띱니다.

```python
In [34]: ridge_fig, ax = subplots(figsize=(8, 8))
ax.errorbar(-np.log(lambdas),
            -grid.cv_results_['mean_test_score'],
            yerr=grid.cv_results_['std_test_score'] / np.sqrt(K))
ax.set_ylim([50000, 250000])
ax.set_xlabel(r'$-\log(\lambda)$', fontsize=20)
ax.set_ylabel('Cross-validated MSE', fontsize=20)
```

One can cross-validate different metrics to choose a parameter. The default metric for `skl.ElasticNet()` is test $R^2$ . Let’s compare $R^2$ to $\text{MSE}$ for cross-validation here.
파라미터를 신중히 골라 채택하기 위해, 사용 목적에 따라 각기 판이하게 다른 여러 종류 평가 측정 단위(metrics) 지표 체계를 교차 검증 도구로 부려 먹을 수도 있습니다. 일례로 파이썬 도구 상자인 `skl.ElasticNet()` 객체 모듈을 부를 때의 태생 기본 내장 통계 측정치는 테스트 결과 $R^2$ 입니다. 그럼 이번엔 교차-검증 무대 평가 척도의 기준으로써 기본 $R^2$ 모델 척도 평가 지표와 이전 방식인 $\text{MSE}$ 단위 평가 지수를 상호 대조 비교해 봅시다.

```python
In [35]: grid_r2 = skm.GridSearchCV(pipe,
                                    param_grid,
                                    cv=kfold)
grid_r2.fit(X, Y)
```

Finally, let’s plot the results for cross-validated $R^2$ .
이로써 마지막 파트로, 순수 교차-검증된 모델 결과 $R^2$ 객체들의 연산 결괏값 성과 곡선을 화면에 노출 점 찍어 그래프 도식화(plot) 시켜 봅시다.

```python
In [36]: r2_fig, ax = subplots(figsize=(8, 8))
ax.errorbar(-np.log(lambdas),
            grid_r2.cv_results_['mean_test_score'],
            yerr=grid_r2.cv_results_['std_test_score'] / np.sqrt(K))
ax.set_xlabel(r'$-\log(\lambda)$', fontsize=20)
ax.set_ylabel(r'Cross-validated $R^2$', fontsize=20)
```
