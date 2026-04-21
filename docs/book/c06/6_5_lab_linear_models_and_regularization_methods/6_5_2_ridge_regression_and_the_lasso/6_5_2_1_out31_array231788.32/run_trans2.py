import codecs

content = r"""---
layout: default
title: "trans2"
---

# **`Out[31]:`** `array([231788.32])`

Obviously choosing $\lambda = 0.01$ is arbitrary, so we will use cross-validation or the validation-set approach to choose the tuning parameter $\lambda$ . The object `GridSearchCV()` allows exhaustive grid search to choose such a parameter. We first use the validation set method to choose $\lambda$ .
우리가 앞서 $\lambda$ 임계 조절 변숫값을 콕 집어 $0.01$로 수동 고집 선택했던 행위 시도 자체는 사실 아무 과학적 근거가 없는 지극히 주관적이고 임의적인(arbitrary) 헛손질 행동에 지나지 않습니다. 그래서 우리는 저 튜닝 파라미터 $\lambda$를 아주 객관적이고 현명하게 파단 골라내기 위해서 검증-세트(validation-set) 접근 기법이나 혹은 한 단계 더 빡빡한 교차-검증(cross-validation) 분석 기법을 들이대 적극 부려 먹을 것입니다. 여기서 구원 투수인 파이썬 `GridSearchCV()` 모듈 탐색기 객체를 소환해 끌어다 쓰면, 설정 범위 격자 단면 내에 포섭된 모든 파라미터 조합 경우의 수의 바닥을 박박 긁어모아 이 잡듯 깡그리 전면 수색해 내는 철저 그물망형 그리드 탐색(exhaustive grid search)을 단숨에 자동 지시 수행, 제어 최적 파라미터 산출을 가능하게 만들어 줍니다. 자, 첫 시도 방침으로써 우선 가장 가벼운 단일 테스트 검증 세트 모델 방식을 사용해 최적 성능 단면 성과를 보장할 가장 정교한 최적 $\lambda$ 변숫값을 신중히 수색 발굴해 보겠습니다.

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
검증 세트 방안을 무사히 써먹은 것에 대한 대체 변환 대안으로써, 이번에는 모델을 5갈래로 아주 잘게 찢어 혹독하게 굴려 검사하는 5-폴드(5-fold) 십자-교차 검증(cross-validation) 체계를 동원 구동 사용해 보겠습니다.

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
이전 랩 파트인 실습 271페이지 단원 위치에서, 이 혹독한 5-폴드 교차 검증 통제를 구동 관리 제어할 부속품인 `kfold` 탐색기 모듈 객체 부품을 저희가 미리 짜서 무사히 조립 세팅해 두었단 지난 팩트 사실을 잊지 말고 회상 상기해 내십시오. 이제 기나긴 시동 도출 끝에 추출 확보된 이 교차-검증 기반 모델 평가지표 $\text{MSE}$ 데이터 구조 스펙트럼 배열을, $-\log(\lambda)$ 수리 제어 함수 단위로 한차례 더 변환 덧씌움 조작 치환 처리 가공하여 시각 차트 선분 도표(plot) 산출 조작 표상을 가동시킬 차례입니다. 이렇게 치환되어 그려 내진 변동 선분 궤도는 점진 차트 왼쪽에서 머나먼 오른쪽 축 좌표로 쭉 직진 진행해 나아감에 응답하듯 점차 모델 규격 하락 감퇴 곡선 축소를 띠는 변동 수축성(shrinkage decreasing) 제약 특질 궤도 파생 곡선 양상을 역력히 띱니다.

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
입맛에 가장 구미가 당길 파라미터를 골라 단박에 취하기 위해서, 여러분들은 사용 용도에 따라 각기 판이하게 다른 여러 속성 종류의 타겟 통계 평가 측정 척도 단위(metrics) 시스템 체계를 교차 검열 판단 잣대 도구로 상황에 맞춰 변형 지정 기용해 쓸 수도 있습니다. 파이썬 환경의 핵심 툴 도구 상자인 기본 내장 `skl.ElasticNet()` 연산 모듈이 맨 처음 장착 부여 출시 태생부터 속성으로 품고 나오는 디폴트 기본 측정 테스트 지표 방식 단위는 바로 $R^2$ 측정치입니다. 자 기왕 말이 나온 김에 테스트 비교 차원에서, 이번엔 이 교차 검증 무대 한복판 위 평가 단상 척도의 양대 산맥으로써 이 태생 모듈 기본 객체 $R^2$ 판독 모형과 조금 전 써먹었던 수치 $\text{MSE}$ 판독 지수 단위를 양쪽 양팔 저울에 서로 똑같이 올려놓고 상호 맞대결 대조 교차 연산 산발 비교 대조를 진행 조작 비교해 봅시다.

```python
In [35]: grid_r2 = skm.GridSearchCV(pipe,
                                    param_grid,
                                    cv=kfold)
grid_r2.fit(X, Y)
```

Finally, let’s plot the results for cross-validated $R^2$ .
이 길고 숨 가빴던 능선 회귀 $\lambda$ 찾기 여정의 마무리를 장식할 최종 단계 파편으로서, 순수 십자 교차-검증된 모델 결과인 $R^2$ 객체들의 연산 결괏값 성과 곡선 궤적 라인들을 그래픽 화면에 산출 점 찍어 그래프 가시화 도식 표출(plot) 시켜 대단원 관찰 대조 연산 마무리를 거둬 보시죠.

```python
In [36]: r2_fig, ax = subplots(figsize=(8, 8))
ax.errorbar(-np.log(lambdas),
            grid_r2.cv_results_['mean_test_score'],
            yerr=grid_r2.cv_results_['std_test_score'] / np.sqrt(K))
ax.set_xlabel(r'$-\log(\lambda)$', fontsize=20)
ax.set_ylabel(r'Cross-validated $R^2$', fontsize=20)
```
"""

try:
    with open(r'd:\site\jinydev\Statistical\src\book\c06\6_5_lab_linear_models_and_regularization_methods\6_5_2_ridge_regression_and_the_lasso\6_5_2_1_out31_array231788.32\trans2.md', 'w', encoding='utf-8') as f:
        f.write(content)
except Exception as e:
    print(e)
