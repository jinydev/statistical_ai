---
layout: default
title: "trans1"
---

# The Lasso 
# 라쏘 (The Lasso)

We saw that ridge regression with a wise choice of $\lambda$ can outperform least squares as well as the null model on the `Hitters` data set. We now ask whether the lasso can yield either a more accurate or a more interpretable model than ridge regression. In order to fit a lasso model, we once again use the `ElasticNetCV()` function; however, this time we use the argument `l1_ratio=1` . Other than that change, we proceed just as we did in fitting a ridge model. 
우리는 앞서 지혜로운 $\lambda$ (튜닝 파라미터) 선택을 동반한 릿지 회귀(ridge regression) 방식이 `Hitters` 데이터 세트 상에서 영 모델(null model)은 물론이거니와 능히 구형 최소 제곱법(least squares)의 성능마저도 앞질러 추월 압도(outperform)할 수 있다는 사실을 살펴본 바 있습니다. 이제 우리는 라쏘(lasso) 기법이 릿지 회귀보다 과연 더 높은 예측 정확도를 보이거나, 혹은 한층 더 매끄러운 해석이 가능한(more interpretable) 훌륭한 산출 모델을 이끌어 낼(yield) 수 있을지에 대한 질문을 던집니다. 라쏘 모델을 피팅 적합하기 위해, 우리는 여기서 다시 한 번 기존의 `ElasticNetCV()` 파이썬 함수를 가져다 사용할 것입니다; 하지만 이번에는 함수 인자 조건문으로 `l1_ratio=1` 을 부여해 사용합니다. 오직 단 하나, 그 변경 사항 조건만을 제외한다면(Other than that change), 다른 나머지 모든 코딩 조작 과정은 우리가 릿지 모델을 피팅했던 당시의 수순 그대로 이어서 속행 진행(proceed just as we did)하게 될 것입니다.

```python
In [43]:lassoCV = skl.ElasticNetCV(n_alphas=100,
                                   l1_ratio=1,
                                   cv=kfold)
        pipeCV = Pipeline(steps=[('scaler', scaler),
                                 ('lasso', lassoCV)])
        pipeCV.fit(X, Y)
        tuned_lasso = pipeCV.named_steps['lasso']
        tuned_lasso.alpha_
```

```python
Out[43]: 3.147
```

```python
In [44]: lambdas, soln_array = skl.Lasso.path(Xs,
                                              Y,
                                              l1_ratio=1,
                                              n_alphas=100)[:2]
         soln_path = pd.DataFrame(soln_array.T,
                                  columns=D.columns,
                                  index=-np.log(lambdas))
```

We can see from the coefficient plot of the standardized coefficients that depending on the choice of tuning parameter, some of the coefficients will be exactly equal to zero. 
표준화 스케일 처리가 된 계수들의 추이 그래프를 유심히 들여다 봄으로써, 튜닝 파라미터를 어떻게 선택 조정하느냐에 따라 특정 일부 파라미터 계수들이 아주 정확하게 '0' 과 완벽히 일치(exactly equal to zero)하는 수준으로 수렴하게 될 것이란 사실을 우리는 육안으로 목격 진단(We can see)할 수 있습니다.

```python
In [45]: path_fig, ax = subplots(figsize=(8,8))
         soln_path.plot(ax=ax, legend=False)
         ax.legend(loc='upper left')
         ax.set_xlabel('$-\log(\lambda)$', fontsize=20)
         ax.set_ylabel('Standardized coefficients', fontsize=20);
```

The smallest cross-validated error is lower than the test set $\text{MSE}$ of the null model and of least squares, and very similar to the test $\text{MSE}$ of 115526.71 of ridge regression (page 278) with $\lambda$ chosen by cross-validation. 
교차 검증을 통해 얻어진 지표 중 그 스코어가 가장 작은 최소 교차 검증 오차율(The smallest cross-validated error)은 이전에 구했던 영 모델 및 최소 제곱법의 테스트 세트 $\text{MSE}$ 결괏값들보다 훨씬 낮은 강세 하위 수위를 기록합니다. 또한 이는, 교차 검증을 통해 $\lambda$를 채택했던 릿지 회귀의 지난번 테스트 $\text{MSE}$ 115526.71 (278페이지 참고) 기록치와 대단히 유사한(very similar) 수준을 보여주고 있습니다.

```python
In [46]: np.min(tuned_lasso.mse_path_.mean(1))
```

```python
Out[46]: 114690.73
```

Let’s again produce a plot of the cross-validation error. 
자, 그럼 이제 다시 한번 교차 검증 오차 지표에 대한 플롯 차트(plot)를 하나 기동해 그려 만듭시다.

```python
In [47]: lassoCV_fig, ax = subplots(figsize=(8,8))
         ax.errorbar(-np.log(tuned_lasso.alphas_),
                     tuned_lasso.mse_path_.mean(1),
                     yerr=tuned_lasso.mse_path_.std(1)/np.sqrt(K))
         ax.axvline(-np.log(tuned_lasso.alpha_), c='k', ls='--')
         ax.set_ylim([50000, 250000])
         ax.set_xlabel('$-\log(\lambda)$', fontsize=20)
         ax.set_ylabel('Cross-validated MSE', fontsize=20);
```

However, the lasso has a substantial advantage over ridge regression in that the resulting coefficient estimates are sparse. Here we see that 6 of the 19 coefficient estimates are exactly zero. So the lasso model with $\lambda$ chosen by cross-validation contains only 13 variables. 
하지만 한편으로 보면, 라쏘는 릿지 회귀 모델과는 철저히 대비되는 엄청난 강점 매력(substantial advantage) 하나를 가지고 있습니다. 바로, 도출되어 도달한 산물인 계수 추정치 결과물 표면이 희소(sparse)한 성향을 띠게 된다는 사실 때문입니다. 여기 콘솔 화면을 보시게 되면, 도합 19개의 전체 계수 추정치들 중 무려 6개의 타점치들이 참으로 완벽 정확하게 제로 '0' 치수(exactly zero) 상태에 놓여 있음을 포착할 수 있습니다. 그래서 교차 검증(cross-validation)에 의해 최적으로 선택된 $\lambda$를 기반으로 한 이 라쏘 모델은, 최종적으로 따지고 보면 오직 13개만의 유효 예측 변수(variables)만을 포함 내장(contains)하게 된 셈입니다.

```python
In [48]: tuned_lasso.coef_
```

```python
Out[48]: array([-210.01008773,  243.4550306 ,    0.        ,    0.        ,
           0.        ,   97.69397357,  -41.52283116,   -0.        ,
           0.        ,   39.62298193,  205.75273856,  124.55456561,
        -126.29986768,   15.70262427,  -59.50157967,   75.24590036,
          21.62698014,  -12.04423675,   -0.        ])
```

As in ridge regression, we could evaluate the test error of cross-validated lasso by first splitting into test and training sets and internally running cross-validation on the training set. We leave this as an exercise. 
우리가 이미 릿지 회귀의 파트 부문에서 거쳐 보았던 바와 같이, 우리는 먼저 전체 관측 데이터 단위를 테스트 검정 세트와 예비 훈련 세트로 물리적 분할 분리 조치(splitting)를 단행한 뒤, 훈련 세트 생태계의 자체 내부 안단(internally) 안에서 독자적으로 교차 검증 루프 시스템을 실행 전개 시킴으로써 교차 검증된 라쏘 엔진에 대한 테스트 에러 오차율을 계산 평가(evaluate)해 도출해 낼 수도 있었습니다. 본 교재 문맥 편의를 위해, 이 연산 증명 절차는 학습자 여러분들을 위한 스스로의 과제 연습(exercise) 용도로 남겨(leave) 두도록 하겠습니다.
