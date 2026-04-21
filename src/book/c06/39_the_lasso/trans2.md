---
layout: default
title: "trans2"
---

# The Lasso 
# 라쏘 (The Lasso): 단호한 변수 사냥꾼

We saw that ridge regression with a wise choice of $\lambda$ can outperform least squares as well as the null model on the `Hitters` data set. We now ask whether the lasso can yield either a more accurate or a more interpretable model than ridge regression. In order to fit a lasso model, we once again use the `ElasticNetCV()` function; however, this time we use the argument `l1_ratio=1`. Other than that change, we proceed just as we did in fitting a ridge model. 
자, 우리는 앞선 튜토리얼에서 페널티 조율 강도($\lambda$) 스위치를 아주 기가 막히게 세팅했던 **[릿지 회귀(Ridge Regression)]** 부대가, `Hitters` 데이터 전장에서 맨주먹의 영 모델(null model) 은 물론 이거니와 기존 고인물 사령관 오리지널 최소 제곱법(least squares) 녀석의 실적까지도 가볍게 압도(outperform)하며 무쌍을 찍는 모습을 똑똑히 지켜보았습니다. 

이제 우리는 여기서 피 끓는 호기심 하나를 던집니다. **"그렇다면, 이 무법자 라쏘(Lasso)가 출동한다면 릿지보다 더 타점 높은 명중률(accurate)을 찍거나, 최소한 사후 보고서를 더 깔끔하게 읽히게 만들어 줄(more interpretable) 수 있지 않을까?"**

이 무법자 라쏘(Lasso) 모델을 피팅 기계에 태우기 위해, 우리는 귀에 못이 박히도록 썼던 친숙한 파이썬 모듈 `ElasticNetCV()` 를 다시 소환합니다. 그런데 말이죠, 단 한 가지! 이번엔 함수 인자 세팅 파츠에서 **`l1_ratio=1`** 로 기어 단수를 바꿔줍니다. 이거 하나 빼고는(Other than that change) 우리가 릿지 모델을 훈련 시킬 때 썼던 과정과 똑.같.이 전진 기어를 밟아줍니다.

```python
In [43]: lassoCV = skl.ElasticNetCV(n_alphas=100,
                                    l1_ratio=1,     # <-- 여기! L1 페널티만 활성화!
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
표준화 평탄화 공사를 마친 계수들의 성적 추이 그래프를 매의 눈으로 스캔해 보십시오. 라쏘의 이 조율 파라미터($\lambda$) 강도를 당신이 어떻게 높여 잡느냐에 따라서, 무능력한 일부 변수들의 계수 게이지가 자비라고는 일절 없이 완.벽.하.게 **'0' 통장 잔고 수준(exactly equal to zero)** 으로 증발해 버린다는 사실을 목격할 수 있습니다. 

```python
In [45]: path_fig, ax = subplots(figsize=(8,8))
         soln_path.plot(ax=ax, legend=False)
         ax.legend(loc='upper left')
         ax.set_xlabel('$-\log(\lambda)$', fontsize=20)
         ax.set_ylabel('Standardized coefficients', fontsize=20);
```

The smallest cross-validated error is lower than the test set $\text{MSE}$ of the null model and of least squares, and very similar to the test $\text{MSE}$ of 115526.71 of ridge regression (page 278) with $\lambda$ chosen by cross-validation. 
수십 번의 교차 검증 훈련 뺑뺑이를 돌려 찾아낸 영광스러운 가장 매끈한 **최소 교차 검증 오차율(The smallest cross-validated error)** 은, 멍텅구리 영 모델(null model)이나 OLS 최소 제곱법이 실전 테스트에서 거둔 $\text{MSE}$ 파이 차트 따위보다 훨씬 날씬하고 매력적입니다. 더 흥미로운 건, 똑같이 교차 검증 훈련장 출신인 릿지 회귀가 앞서 찍었던 테스트 $\text{MSE}$ 기록인 115526.71 점수와 소름 돋게 비슷한 퍼포먼스(very similar)를 냈다는 사실이죠!

```python
In [46]: np.min(tuned_lasso.mse_path_.mean(1))
```

```python
Out[46]: 114690.73
```

Let’s again produce a plot of the cross-validation error. 
백문이 불여일견, 자 우리도 교차 검증 오차 추이(cross-validation error)를 추적하는 엑스레이 플롯 차트를 시원하게 하나 뽑아봅시다.

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
성능 점수가 릿지와 엇비슷하다고 무시하면 큰코다칩니다. 라쏘(Lasso)에게는 릿지 녀석들을 절망하게 만들 **치명적이고 압도적인 강점 마검(substantial advantage)** 이 하나 숨어 있습니다! 바로 도출된 계수 추정치 결과물 데이터 뼈대가 굉장히 듬성듬성 날씬해지고 다이어트되어 **희소해진다는(sparse)** 기적입니다. 

자, 여기 실시간 콘솔 출력창을 보십시오. 전체 19마리의 계수 참가자들 중 무려 **6마리의 스코어가 가차 없이 '0 (exactly zero)'** 이라는 단두대 처형을 당해 증발했습니다. 결론적으로 교차 검증 트레이닝을 거쳐 최적의 무기 $\lambda$를 집어 든 이 라쏘 부대는, 쓸모없는 방해꾼 요원들을 모두 목 날려버리고 오직 핵심 요원 13마리 만을 정예 멤버로 데리고 다닌다(contains only 13 variables)는 엄청난 가독성 효율을 보여줍니다.

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
물론 릿지 회귀 때 우리가 이미 한탕 뛰었던 것처럼, 최초에 데이터를 훈련소 세트와 실전 테스트 세트로 먼저 칼같이 도려내 가른(splitting) 다음, 그 훈련소 안방 철창 속 내부 구조(internally) 안에서 다시 팽팽한 교차 검증 트레이닝을 치르게 하여 이 교차 검증된 라쏘 모델의 최종 테스트 파괴력 에러율을 도출 계산 평가해 볼(evaluate) 수도 있었습니다. 하지만 이번 랩 실습 분위기에선, 학습자 여러분들의 피지컬 단련을 위한 가벼운 연습용 홈 트레이닝 숙제(exercise) 거리 용도로 이걸 매끄럽게 남겨두겠습니다. 파이팅!
