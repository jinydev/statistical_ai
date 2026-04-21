import codecs

content = r"""---
layout: default
title: "trans1"
---

# 능선 회귀 (Ridge Regression)

We will use the function `skl.ElasticNet()` to fit both ridge and the lasso. To fit a _path_ of ridge regressions models, we use `skl.ElasticNet.path()` , which can fit both ridge and lasso, as well as a hybrid mixture; ridge regression corresponds to `l1_ratio=0` . It is good practice to standardize the columns of `X` in these applications, if the variables are measured in different units. Since `skl.ElasticNet()` does no normalization, we have to take care of that ourselves. Since we standardize first, in order to find coefficient estimates on the original scale, we must _unstandardize_ the coefficient estimates. The parameter $\lambda$ in (6.5) and (6.7) is called `alphas` in `sklearn` . In order to be consistent with the rest of this chapter, we use `lambdas` rather than `alphas` in what follows.[^10]
우리는 능선(ridge) 회귀 모델과 라쏘(lasso) 회귀 모델 양쪽 모두를 적합시키기 위해 `skl.ElasticNet()` 함수 객체를 사용할 것입니다. 능선 회귀 모델들의 연속된 궤적(_path_)을 적합시키기 위해 우리는 `skl.ElasticNet.path()`를 사용하며, 이 함수는 능선 회귀와 라쏘 회귀뿐만 아니라 두 가지 방식이 혼합된 하이브리드 교잡 모델 역시 무리 없이 적합시킬 수 있습니다; 이 중에서 능선 회귀(ridge regression)는 `l1_ratio=0` 옵션 설정에 직접 상응하여 동작합니다. 이러한 분석 응용 단면에서 만약 입력 변수 조각들이 저마다 서로 판이하게 다른 단위(units)들로 제각기 측정된 관측치 상태라면, 사전에 통계 매트릭스 `X`의 열(columns) 배열 지표들을 정규화(standardize) 표준 전처리해 주는 과정이 아주 좋은 실무 관행 조치입니다. 유감스럽게도 `skl.ElasticNet()` 함수는 자체적으로 어떠한 정규화 프로세스도 수행 제공하지 않기 때문에, 우리는 그 귀찮은 단위 스케일 통제 작업을 오롯이 우리 손으로 직접 신경 써 선행 착수해 단행해야만 합니다. 우리가 사전에 강제로 정규화를 우선 실시해 두었으므로, 추후 원래 규격 스케일로 측정되어 있던 원본 계수 추정 반환값을 찾으려면 우린 해당 변형 파생 계수 측정치들을 또 한 번 반대로 _역 정규화(unstandardize)_ 하여 수동 변환 원위치 되돌려야만 합니다. 수학 논의 도출 수식 식 (6.5) 파트 및 (6.7) 항목 궤도에서 주로 $\lambda$라고 명명 불렸던 그 핵심 파라미터 제약 변수는, 이 파이썬 `sklearn` 개발 연산 환경에선 주로 `alphas`라는 다른 파라미터 명칭 코드로 치환 지정되어 불리고 있습니다. 하지만 본 문서 6장 챕터 전체에 흐르는 거시 통일 기조 흐름과 일관성을 유지하기 위해, 아래로 설명될 진행 파트들에선 줄곧 파이썬 문법의 `alphas` 용어를 끌어 쓰기보단 원문 그대로인 `lambdas` 키워드를 고집하여 대체 지칭 사용토록 하겠습니다.[^10]

[^10]: At the time of publication, ridge fits like the one in code chunk [22] issue unwarranted convergence warning messages; we expect these to disappear as this package matures.
[^10]: 본 번역본 및 원서 자료의 출판 공표 시점 기준, 추후 이어지는 [22]번 코드 청크(chunk) 무대와 같은 전형적인 능선(ridge) 적합 회귀 동작 단계 구역 부근에서 까닭 없는 수치 미 수렴 도달 경고(convergence warning messages) 오류 출력문이 간혹 튀어나와 보고되고 있습니다 ; 그러나 우리는 조만간 이 회귀 분석 패키지 운영 생태계 소프트웨어가 지속 업데이트를 거치며 성숙의 단계를 거침에 따라 이러한 이례적 경고 문구들도 곧 조용히 시정되어 사라지리라 예상 전망하고 있습니다.

```python
In [22]: Xs = X - X.mean(0)[None, :]
X_scale = X.std(0)
Xs = Xs / X_scale[None, :]
lambdas = 10**np.linspace(8, -2, 100) / Y.std()
soln_array = skl.ElasticNet.path(Xs,
                                 Y,
                                 l1_ratio=0.,
                                 alphas=lambdas)[1]
soln_array.shape
```

```
Out[22]: (19, 100)
```

Here we extract the array of coefficients corresponding to the solutions along the regularization path. By default the `skl.ElasticNet.path` method fits a path along an automatically selected range of $\lambda$ values, except for the case when `l1_ratio=0` , which results in ridge regression (as is the case here).[^11] So here we have chosen to implement the function over a grid of values ranging from $\lambda = 10^8$ to $\lambda = 10^{-2}$ scaled by the standard deviation of $y$ , essentially covering the full range of scenarios from the null model containing only the intercept, to the least squares fit.
우리는 이 부분에서 정규화 강제 조율 회귀선 탐색 궤도를 통과함에 따라 도출 솔루션 해결 결과값들에 상응 대응되는 계수(coefficients)들의 배열 덩어리를 추출 파생시켜 분리해 냅니다. 기본 설정상, `skl.ElasticNet.path` 작동 메서드는 시스템이 자동 선별한 광범위 구간 스펙트럼 구간 범위의 $\lambda$ 임계값 배열들을 따라 경로를 적합 가동시킵니다. 그러나 단, 릿지 회귀로 귀결되는 (바로 지금 우리가 겪고 있는 실습 케이스처럼 말이죠) 조건 옵션인 `l1_ratio=0` 지점 통제가 가해진 상황 절차일 땐 그 자동 선별 가동 예외 편차가 발생합니다.[^11] 그로 인해 여기에서 우리는 시스템을 우회 설정하고자, 목표 결과 객체 무리 $y$의 표준 편차(standard deviation) 치수를 곱해 환산 비율로 조정 적용한 상태의 $\lambda = 10^8$ 수치부터 최하 $\lambda = 10^{-2}$ 범위 분포 구간에 이르는 광활한 가상 값들의 그리드(grid) 격자 변수 망 한도 위에서 해당 탐색 함수 구현 동작 이행을 강제 관철시키도록 구조를 직접 채택 세팅했습니다. 이로써 오로지 초근본 뼈대인 절편 지점 하나만 남긴 최하 최소한의 깡통 무 모델(null model) 성과 치수 구간 상태로부터 온전하고 거대한 최소 제곱 적합(least squares fit) 완전 이수 체제 단계 파트까지 달하는 모든 광범위 시나리오 풀스펙트럼 궤도를 필수적으로 전부 포섭, 커버 통제 관측하게끔 모의 환경 조율을 구축 구성해 낸 셈입니다. 

We transpose this matrix and turn it into a data frame to facilitate viewing and plotting.
그런 다음 이렇게 수합된 데이터를 도표 차트로 찍어 도식화(plotting) 하거나 편하게 눈으로 열어 확인(viewing)하기 쉽도록, 우리는 산출된 예측 결괏값 매트릭스를 반대로 뒤집어 회전 전치 처리 변환(transpose) 역전시켰고, 더 보기 편한 체계인 판다스 베이스 데이터 프레임(data frame) 덩어리 양식으로 변환 틀 교체하여 단정히 정비해 모아주었습니다.

```python
In [23]: soln_path = pd.DataFrame(soln_array.T,
                                  columns=D.columns,
                                  index=-np.log(lambdas))
soln_path.index.name = 'negative log(lambda)'
soln_path
```

|**`Out[23]:`**||`AtBat`|`Hits`|`HmRun`|`Runs`|`...`|
|---|---|---|---|---|---|---|
||`negative`||||||
||`log(lambda)`||||||
||`-12.310855`|`0.000800`|`0.000889`|`0.000695`|`0.000851`|`...`|
||`-12.078271`|`0.001010`|`0.001122`|`0.000878`|`0.001074`|`...`|
||`-11.845686`|`0.001274`|`0.001416`|`0.001107`|`0.001355`|`...`|
||`-11.613102`|`0.001608`|`0.001787`|`0.001397`|`0.001710`|`...`|
||`-11.380518`|`0.002029`|`0.002255`|`0.001763`|`0.002158`|`...`|
||`...`|`...`|`...`|`...`|`...`|`...`|
||`100 rows × 19 columns`||||||

We plot the paths to get a sense of how the coefficients vary with $\lambda$ . To control the location of the legend we first set `legend` to `False` in the plot method, adding it afterward with the `legend()` method of `ax`.
이윽고 마침내 파라미터 $\lambda$ 변수 조정 값에 따라 그에 결부된 회귀 계수들이 구체적으로 어떻게 시시각각 통제 변화하는지에 대한 감(sense)을 얻고자 궤적 경로 도식 결괏값을 점진 선분 그래픽 차트 도표화(plot) 출하합니다. 범례(legend) 박스의 위치를 원하는 적소에 두루 제어 통제 설정하기 위해 우리는 처음 도표 작성 메서드를 켤 때 `legend` 옵션을 끄기 옵션인 `False` 상태 시그널 우선 설정하여 일단 지워버렸고, 도표 윤곽 그리기 가동 직후 그 뒤쪽 수식 줄에 이어서 단독으로 `ax` 변수에 소속 내장된 `legend()` 강제 호출 메서드를 덧붙여 연결 실행함으로써 나중에 재첨가해 세팅 추가했습니다.

```python
In [24]: path_fig, ax = subplots(figsize=(8, 8))
soln_path.plot(ax=ax, legend=False)
ax.set_xlabel(r'$-\log(\lambda)$', fontsize=20)
```

[^11]: The reason is rather technical; for all models except ridge, we can find the smallest value of $\lambda$ for which all coefficients are zero. For ridge this value is $\infty$.
[^11]: 이 예외 조치가 발동 걸린 사유는 무척이나 내부 수리적이고 기술적인 단절 상황 때문입니다 ; 기본 능선(ridge) 회귀 구조를 배제한 여타 모형들에선, 우리는 파생된 모든 계수의 값이 '0'으로 처참히 소멸할 수 있는 최소한의 가장 치수가 작은 극솟값 $\lambda$ 지수를 쉽게 찾아 발굴 방산해 낼 방도가 됩니다. 그러나 유독 이 릿지를 설정한 환경 모델 체제에선 그 값이 파악 한계를 넘어선 무한대 영역 $\infty$ 무궤에 처박혀 달해 버리기 때문입니다.

```python
ax.set_ylabel('Standardized coefficients', fontsize=20)
ax.legend(loc='upper left')
```

(We have used `latex` formatting in the horizontal label, in order to format the Greek $\lambda$ appropriately.) We expect the coefficient estimates to be much smaller, in terms of $\ell_2$ norm, when a large value of $\lambda$ is used, as compared to when a small value of $\lambda$ is used. (Recall that the $\ell_2$ norm is the square root of the sum of squared coefficient values.) We display the coefficients at the 40th step, where $\lambda$ is 25.535.
(우리는 가로 수평축 도표 표시 라벨 꼬리표 항목에 그리스어 기호인 $\lambda$를 적절한 형태로 어색하지 않게 잘 포맷 표출시키고자, 특수 수식기인 `latex` 형태 포맷 양식을 빌려 부착 차용 적용했습니다.) 우리는 $\lambda$ 모수 수치가 상대적으로 작게 주어졌을 무대 환경과 대조 비교했을 때, 만약 거대 값이 치솟은 수치의 $\lambda$ 파라미터가 억압 사용되었을 무대 환경 측면 전황에서는 상대적으로 $\ell_2$ 노름(norm) 치수 잣대 관점 영역에서 바라봤을 때 모델 내부 회귀 결합 계수 추산 산출 크기 변형치들이 정말 처참히 쪼그라들고 왜소하게 축소 상실될 것이라 예측 기대 전망합니다. (앞서 이론부에서 살펴봤듯 지수 단위인 $\ell_2$ 노름이란 도출된 계수 값들을 제곱한 합계 덩어리에 수학적 제곱근을 씌워 처리 연산시킨 거리 잣대 단위량 수리 임을 다시금 리마인드 회상 기억해 내십시오.) 우리는 통제 설정 파라미터 $\lambda$ 값이 마침내 딱 25.535로 안착 적중 파생 도달하게 되는, 대망의 제40번째 궤도 연산 통과 스텝 지점에서 추출 산출된 그 정식 회귀 산정 계숫값을 화면에 노출 표기하여 전시합니다.

```python
In [25]: beta_hat = soln_path.loc[soln_path.index[39]]
lambdas[39], beta_hat
```

|**`Out[25]:`**|`(25.535,`||
|---|---|---|
||`AtBat`|`5.433750`|
||`Hits`|`6.223582`|
||`HmRun`|`4.585498`|
||`Runs`|`5.880855`|
||`RBI`|`6.195921`|
||`Walks`|`6.277975`|
||`Years`|`5.299767`|
||`...`|`...`|

Let’s compute the $\ell_2$ norm of the standardized coefficients.
이 산출 가공되어 토출된 표준화 형태 계수 인자 측정 객체들의 $\ell_2$ 노름 결과 거리를 재빨리 타산 계산해 봅니다.

```python
In [26]: np.linalg.norm(beta_hat)
```

```
Out[26]: 24.17
```

In contrast, here is the $\ell_2$ norm when $\lambda$ is 2.44e-01. Note the much larger $\ell_2$ norm of the coefficients associated with this smaller value of $\lambda$ .
이 전황의 양상 대조 관찰 차원에서, 반대 편향 임계점인 파라미터 $\lambda$ 통제치가 겨우 2.44e-01(0.244) 수치 수준으로 대폭 축소 억압되었을 극한 환경의 종착$\ell_2$ 노름 산출 결과를 대조 공개 배포합니다. 이처럼 더 작게 쪼그라든 임계 제약 수치 $\lambda$ 세팅 구간에 결부 결합된 이 산단 계수 값 모델들의 산출 노름 거리 $\ell_2$ 치수가 앞선 상황 환경에 대비해 단연 압도적으로 더 폭발 파급 거대하게 치솟아 팽창해 파생 증가해 버렸다는 현상 현안을 예의 주시해 목격 인지하십시오.

```python
In [27]: beta_hat = soln_path.loc[soln_path.index[59]]
lambdas[59], np.linalg.norm(beta_hat)
```

```
Out[27]: (0.2437, 160.4237)
```

Above we normalized `X` upfront, and fit the ridge model using `Xs` . The `Pipeline()` object in `sklearn` provides a clear way to separate feature normalization from the fitting of the ridge model itself.
앞서 맨 처음 연산 시작 부분 과정 단락 중에, 저희는 원천 투입 데이터 구역인 `X` 체제를 선행 지시 작업으로써 제일 먼저 선별 정규화 조작 환산 단행했으며, 그로 얻어진 조작 환산 객체 상태 훈련 세트인 `Xs` 변형 배열 무대를 투입 사용해 최종 릿지(ridge) 정규 회귀 목표 다중 구조 모델 체형을 차례로 종속 적합 구현 가동했음을 인지 상기시켜 드립니다. 파이썬 `sklearn` 연산 장치 엔진에 모듈 파생되어 내장 탑재되어 얹혀 존재하는 강력 탑 티어 부속품 객체 톱 툴 장비 기능 `Pipeline()` (파이프라인) 조립 구조체는, 일전 무대처럼 앞단의 특성 지표 차원 정규화(feature normalization) 변환 전처리 이행 과정 단계를 그 뒤 후단의 실질 본체인 릿지 모델의 완전 적합 수행 본체 모델 구현 연결 과정 체계에서 아주 매끄러운 단절 투 트랙 시야 설계로 단일 명쾌히 떨어져 분할 독립 분리 운용 조율 모의 구동 시연할 수 있도록 제공하는 참으로 명확하고 단단한 직관 통로 역할을 제공 분리 시사해 줍니다.

```python
In [28]: ridge = skl.ElasticNet(alpha=lambdas[59], l1_ratio=0)
scaler = StandardScaler(with_mean=True, with_std=True)
pipe = Pipeline(steps=[('scaler', scaler), ('ridge', ridge)])
pipe.fit(X, Y)
```

We show that it gives the same $\ell_2$ norm as in our previous fit on the standardized data.
우리는 이 대체 파이프라인 방편 통제 가동 절차 도출 과정이 결국 앞서 직접 정오 차원 산단 전처리 조작 통제를 거친 복구 수치 표준 정규 상태 데이터 환경 무대에서 종단 이행 연산 돌렸던 이전 선동 노름 평가 도출 객체 결과 잣대와 아예 티 한 점 편차 없는 완전하게 판박이처럼 정교히 톱니바퀴 맞물린 똑같은 도출 수치 값 동일 $\ell_2$ 측정 아웃풋 노름 반사를 끌어 무단 결론 토해낸다는 팩트 사실 쾌거를 단 숨 확인 노출 증명 증빙합니다.

```python
In [29]: np.linalg.norm(ridge.coef_)
```

```
Out[29]: 160.4237
```

Notice that the operation `pipe.fit(X, Y)` above has changed the `ridge` object, and in particular has added attributes such as `coef_` that were not there before.
파이프 조작 구동 지시가 걸린 상기 명령 코드 체제인 `pipe.fit(X, Y)` 지시 구문 통제 조작은 단번에 바로 자기 앞단의 훈련 주체 껍데기 변수인 `ridge` 구속 객체 자체를 고차원 조작 교환 탈바꿈 세팅 변이시켰다는 단서 변화 사실을 단단히 인식해 주목 파악하십시오, 그리고 그 특단 교체 사항 스펙 중에서도 이전 깡통 탑재 상태일 땐 결코 발견 관측 볼 수 없었던 `coef_` (산출 완료된 측정 연산 결론 계수 표본 팩트 값 단위체) 항목과 같은 탑재형 무단 모형 속성 애트리뷰트 구조 파편을 자신 시스템 모형 안에 새롭게 부가 탑재 단독 결착시켜 삽입 포워딩 심어 두었다는 강력 변경점 이 차별 파격 지점을 예의 세심 관찰 파견 파악 추격해 보십시오.

## Estimating Test Error of Ridge Regression
## 릿지(능선) 정규 회귀 평가 단면 모델의 테스트 오차 예측 추정 산단 평가

Choosing an _a priori_ value of $\lambda$ for ridge regression is difficult if not impossible. We will want to use the validation method or cross-validation to select the tuning parameter. The reader may not be surprised that the `Pipeline()` approach can be used in `skm.cross_validate()` with either a validation method (i.e. `validation` ) or _k_-fold cross-validation.
어떤 종류의 릿지(능선) 정규 회귀 구조 모형을 구축하려 시도할 때든, 예측 평가 투입 무대에 앞서 _선험적(a priori)_ 지식만으로 미리 완벽하고 이상적인 $\lambda$ 튜닝 파라미터 수치값을 정교히 콕 집어 결정해 놓는다는 것은 기적에 가까울 만큼 어려운 일입니다. 따라서 우리는 이 튜닝 파라미터를 현명하게 선택하기 위해 검증 세트 방식이나 교차 검증(cross-validation) 기법을 적극 활용하고 싶어질 것입니다. 독자 여러분은 지금까지 봐왔던 강력한 `Pipeline()` 객체 접근법이 검증 검사 방식(즉, `validation` 인자)이든 혹은 _k_-폴드 분할 교차 검증 구조이든 양쪽 모델 진영 모두에서 `skm.cross_validate()` 평가 연산기 속에 던져져 자연스럽게 호환 사용될 수 있다는 사실에 그다지 깊게 놀라지 않으실 겁니다.

We fix the random state of the splitter so that the results obtained will be reproducible.
우리는 측정된 계산 연산 지표 도출 결괏값들이 추후 언제 테스트해도 똑같이 재현(reproducible) 산출 가능할 수 있도록 파편 분할기(splitter)의 난수 발생 위치(random state)를 임의 고정 조치합니다.

```python
In [30]: validation = skm.ShuffleSplit(n_splits=1,
                                       test_size=0.5,
                                       random_state=0)
ridge.alpha = 0.01
results = skm.cross_validate(ridge,
                             X,
                             Y,
                             scoring='neg_mean_squared_error',
                             cv=validation)
-results['test_score']
```
"""

try:
    with open(r'd:\site\jinydev\Statistical\src\book\c06\6_5_lab_linear_models_and_regularization_methods\6_5_2_ridge_regression_and_the_lasso\6_5_2_1_ridge_regression\trans1.md', 'w', encoding='utf-8') as f:
        f.write(content)
except Exception as e:
    print(e)
