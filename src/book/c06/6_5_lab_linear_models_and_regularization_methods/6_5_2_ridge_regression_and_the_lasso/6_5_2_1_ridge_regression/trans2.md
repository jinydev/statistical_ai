---
layout: default
title: "trans2"
---

# 능선 회귀 (Ridge Regression)

We will use the function `skl.ElasticNet()` to fit both ridge and the lasso. To fit a _path_ of ridge regressions models, we use `skl.ElasticNet.path()` , which can fit both ridge and lasso, as well as a hybrid mixture; ridge regression corresponds to `l1_ratio=0` . It is good practice to standardize the columns of `X` in these applications, if the variables are measured in different units. Since `skl.ElasticNet()` does no normalization, we have to take care of that ourselves. Since we standardize first, in order to find coefficient estimates on the original scale, we must _unstandardize_ the coefficient estimates. The parameter $\lambda$ in (6.5) and (6.7) is called `alphas` in `sklearn` . In order to be consistent with the rest of this chapter, we use `lambdas` rather than `alphas` in what follows.[^10]
이번 랩 실습 과정에서 우리는 거칠고 변덕스러운 능선(ridge) 회귀 모델과 파라미터를 확 잡아채는 라쏘(lasso) 회귀 양쪽 전부를 멋지게 적합시키기 위해 특별한 장비인 `skl.ElasticNet()` 라이브러리 함수를 꺼내 들 것입니다. 먼저, 능선 회귀가 점차 파라미터를 조여가며 만들어내는 여러 모델의 도출 변화 궤적(_path_)들을 연달아 추적해 적합시켜 보려면, 우린 `skl.ElasticNet.path()`라는 강력한 지시 모듈을 끌어다 써야 합니다. 이 장비는 릿지(ridge)와 라쏘(lasso) 모델 단일 무대뿐 아니라, 둘을 반반씩 요리조리 섞어버린 기괴한 하이브리드 교잡 모델 무대까지도 막힘없이 돌려낼 수 있는 뛰어난 만능 장비입니다; 만약 이 구동 모듈 속에 `l1_ratio=0`이라는 꼬리표 옵션을 고정 지침으로 달아주면, 이 모듈은 오직 능선 회귀 전용 동작 모드로 각 잡고 작동하게 됩니다. 이런 류의 데이터 응용 분석 무대에서는 각 변수 요소들이 지닌 본래 스케일 측정 단위(units) 덩치가 제각기 천차만별인 경우가 허다합니다. 이럴 땐, 매트릭스 `X`에 속한 모든 세로 열(columns) 데이터들의 기를 똑같이 표준화(standardize) 전처리해 주고 시작하는 것이 아주 교과서적이고 모범적인 훌륭한 조치입니다. 애석하지만 `skl.ElasticNet()` 함수엔 스스로 정규화 평탄 작업을 해주는 친절한 자동 배려 기능 따위가 탑재되어 있지 않습니다. 그러니 우린 그 잡다하고 잔인한 수치 조정 과정을 손수 하나하나 전부 통제해 맡아서 챙겨줘야 합니다. 애초에 처음 전제로 모델 투입 직전 데이터들을 강제로 찍어 눌러 억지 정규화해 두었으니, 이 산출 작업의 맨 꼭대기 마지막 종착지에 도달했을 땐 원래 스케일 기준의 계수 측정 반환값을 되찾기 위해서 앞서 변형을 가해 도출해 둔 파생 계수 결과치들을 또 한 번 수동으로 조작해 _역 정규화(unstandardize)_ 과정을 거쳐 원래의 몸집 형체로 꼭 복원해내야만 합니다. 참고로 6장 초반 본문 수식 (6.5) 파트 및 (6.7) 항목 이론에서 다뤘던 제약의 핵심 조율 변수인 $\lambda$ 파라미터는, 파이썬의 `sklearn` 제어 생태계 환경 체제에선 `alphas`라는 독자 명칭으로 살짝 탈바꿈되어 불리고 있습니다. 하지만 우리는 남은 장 전체에 깔린 분위기 통일성을 해치지 않기 위해, 아래로 설명될 진행 파트 구간들에선 `alphas` 대신 책 원문과 똑같이 `lambdas` 키워드를 고집하여 억지로 유지 작성해 나아가겠습니다.[^10]

[^10]: At the time of publication, ridge fits like the one in code chunk [22] issue unwarranted convergence warning messages; we expect these to disappear as this package matures.
[^10]: 이 실습의 원문 도서 공표 시점 기준, 추후 출현할 [22]번 코드 구역 같은 전형적인 능선(ridge) 적합 회귀 동작 단계 주변에서 까닭을 알 수 없는 수치 미 수렴 경고(convergence warning messages) 출력 오류가 간간이 발생하는 것으로 집계되고 있습니다 ; 여담이지만 우린 조만간 이 회귀 분석 패키지 운영 생태계 소프트웨어가 거듭된 업데이트를 거치며 한 층 성숙해짐에 따라, 이런 알 수 없는 자잘한 오류 경고 문구들도 곧 조용히 잡초 뽑히듯 사라지리라 예상 전망하고 있습니다.

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
이 지점에서, 우리는 정규화 조율 회귀선 탐색 가도를 거치면서 단계별로 도출된 해결 해결책 결로 값 수치들에 그대로 상응되는 계수(coefficients)들의 무더기 파편 배열 덩어리를 쏙쏙 뽑아내어 도출해 추출시킵니다. 근본 디폴트 세팅 상태에서, 이 `skl.ElasticNet.path` 가동 메서드는 아무 범위 제재 통제를 가하지 않으면 시스템이 멋대로 자동 지정한 광범위 $\lambda$ 임계값 잣대 기준들을 무작위 범위 차원으로 쭉 돌며 경로 적합 모의를 가동시킵니다. 하지만 유독 능선(ridge) 회귀 기법 체계 전용 옵션 제약인 `l1_ratio=0` 통제가 투입된 상황 조건일 땐 (지금 우리가 부려먹고 처리 중인 실습과 똑같은 상황 말이죠) 유감스럽게도 저 자동 스윕 예외가 튕겨 파단되어 버립니다.[^11] 그런 귀찮은 연유로 여기에서 우리는 시스템을 고정 우회해 통제하고자, 타겟 종속 객체 무리 $y$의 표준 편차(standard deviation) 치수를 곱해 환산 비율 축소 조작한 $\lambda = 10^8$ 수치부터 최하 $\lambda = 10^{-2}$ 범위 분포 단 구간 격자(grid) 수형 망 한도 위에서 해당 탐색 함수 구현 동작 이행 도출을 강제하도록 무식하게 세팅 우회 처리를 단행했습니다. 이렇게 치밀히 우회 세팅을 조립한 결과, 우리는 기둥 뼈대만 겨우 남긴 깡통 베이스 무 모델(null model) 성과 치수 구간으로부터 온전 거대한 무피해 최소 제곱 적합(least squares fit) 완전 완료 결론에 이르는 기나긴 스펙트럼 궤도를 전체 무사히 커버 통제 및 감시, 관측하게끔 모델 시나리오를 탄탄히 엮어 두르게 되었습니다. 

We transpose this matrix and turn it into a data frame to facilitate viewing and plotting.
그런 다음 결론지어 수합된 모형의 시각 정보 가독 상황 기조를 훨씬 예쁘게 향상 보기 보완시킬 목적으로, 도출 결과 객체 변환 매트릭스 배열 덩어리를 고스란히 엎어 전치 돌림 변환(transpose) 역전 전환해 주었으며, 더 편하게 판다스 표 체계에 맞는 데이터 프레임 덩어리 양식 포맷 구조로 틀 교체 환산하여 단정히 찍어 정렬 도식화(plotting) 하도록 뽑아 지시했습니다.

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
마침내 $\lambda$ 변수 모수 제약 파라미터를 들쑤셔 바꿨을 때 그로 인해 내부 적합 회귀 계수들이 어떻게 극적으로 휘어지며 반응 변화하는지를 더 쉽게 파악, 구체적 변동 궤적 결괏값 감(sense)을 선명 선분 그래픽 차트 도표화(plot)로 단숨에 직관 확보하도록 찍어 출하합니다. 범례(legend) 박스의 위치 꼬리표 좌표를 사용자 지시에 맞게 깔끔 통제 제어하고자, 우린 처음에 도표 윤곽 그리기 파라미터를 켤 땐 일단 `legend` 옵션을 눈치껏 끄기 시그널 징후인 `False` 상태로 고의 지정해 한 번 치워 감춰두었고, 도표 그리기 가동 직후 곧바로 뒤쪽 꼬리 단에서 오로지 `ax` 공간 변수에 소속 탑재된 `legend()` 강제 호출 전용 메서드를 기습 덧붙여 호출 부가 결속함으로써 범례를 무리 없이 다시 세팅 추가해 단단히 재배치 구축 명시했습니다.

```python
In [24]: path_fig, ax = subplots(figsize=(8, 8))
soln_path.plot(ax=ax, legend=False)
ax.set_xlabel(r'$-\log(\lambda)$', fontsize=20)
```

[^11]: The reason is rather technical; for all models except ridge, we can find the smallest value of $\lambda$ for which all coefficients are zero. For ridge this value is $\infty$.
[^11]: 이런 지질한 예외 조치가 걸린 연유엔 아주 수리적인 한계 조건 장벽 단절 변환 사유들이 얽혀 있습니다 ; 릿지 능선 회귀를 제쳐둔 여타 다른 류의 회귀 예측 모형들 무대 환경에선, 산출 파생된 모든 적합 예측 변수 도출의 계수 값 무리를 모두 다 강제로 짜부시켜 '0' 치수로 처참히 전멸 소멸시킬 수 있는 아주 작은 규모의 극소치 마지노선 $\lambda$ 도달 측정 한계선을 손쉽게 발굴해 낼 수 있는 물리력이 통용 지원됩니다. 하지만 이 빌어먹을 릿지 능선 제약 환경에선, 애달프게도 당장 그 극소 한계 추락 소급 종결 마지노선 값이 무려 눈에 보이지도 않는 무한대 좌표인 $\infty$ 무궤 스케일 늪까지 파고들어야 처박혀 달해 버리는 까닭 때문입니다.

```python
ax.set_ylabel('Standardized coefficients', fontsize=20)
ax.legend(loc='upper left')
```

(We have used `latex` formatting in the horizontal label, in order to format the Greek $\lambda$ appropriately.) We expect the coefficient estimates to be much smaller, in terms of $\ell_2$ norm, when a large value of $\lambda$ is used, as compared to when a small value of $\lambda$ is used. (Recall that the $\ell_2$ norm is the square root of the sum of squared coefficient values.) We display the coefficients at the 40th step, where $\lambda$ is 25.535.
(우리는 가로 좌표 수평선 항목의 표기 라벨 네이밍 파트에 번거로운 그리스어 기호 문자 $\lambda$를 떡하니 깨지지 않고 무사 표출 반영시키고자, 특수 서식기인 `latex` 형태 포맷 양식 객체를 살짝 빌려 치환 차용 지정했습니다.) 우리는 만약 거대하고 무거운 $\lambda$ 제약 파라미터가 억압 가해져 들어갔을 당시 전황 무대의 적합 도출 성과가, 아주 병아리 솜털같이 보잘것없고 작은 미세 $\lambda$ 무대 파라미터 통제 환경에서 나온 성과 객체 파급 예측치들에 대비해 비교해 보았을 경우엔 응당 $\ell_2$ 노름(norm) 관점 영역에서 측정된 통계 회귀 계수 산출 결괏값 크기 스펙트럼 덩어리들이 극단적인 차이를 보이며 처참히 쪼그라들고 폭삭 왜소하게 축소 몰락해 버릴 것이라 기대 전망 시뮬레이션 합니다. (혹여나 이 $\ell_2$ 노름 평가의 명료 수리 조건을 잠시 잊으셨을까 봐 친절히 다시금 첨언 팁 하자면, 이 거시 지표는 도출된 계수 값들의 무리를 죄다 제곱해 더하여 수합한 총합 규모 덩어리에 강제로 수학적 거듭제곱근 루트 식을 한 방 크게 덧씌워 역산 연산 치환 합산시킨 단면 거리 단 잣대량 수리 체계 임을 상기 회상 기억해 내시길 독려 바랍니다.) 마침내 우린 그 패널티 제어 튜닝 세팅 기준 변수 타겟 $\lambda$ 값이 도합 25.535 치수로 단연 무사 안착 적중 궤적에 도달 서는 위치 지점인, 대망의 제40번째 궤도 전진 연산 패스 스텝에서 강제 추출 포획 발굴해 낸 통계 적합 회귀 계숫값을 여러분 앞에 짜잔 도표 노출하여 화려하게 대놓고 단면 투시 전시 결산합니다.

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
자, 그러면 이렇게 보기 좋게 뽑혀 나와 가공된 표준화 형태 계수 측정 진단 인자 객체 무리들을 가지고서 그 문제의 $\ell_2$ 노름 결과 거리를 직접 단 번에 쾅 때려 타산 계산 산출 비교해 봅니다.

```python
In [26]: np.linalg.norm(beta_hat)
```

```
Out[26]: 24.17
```

In contrast, here is the $\ell_2$ norm when $\lambda$ is 2.44e-01. Note the much larger $\ell_2$ norm of the coefficients associated with this smaller value of $\lambda$ .
이와 반전되는 역상황 환경 측면에 대한 대조 관찰 체험 차원에서, $\lambda$ 파라미터가 겨우 2.44e-01(0.244) 치수라는 한 대 툭 쳐도 날아갈 수준의 미약 극소 제재 압박 조치로 대폭 풀려버렸을 그 널찍한 통제 무대 환경을 다시 관통 조율해 이끌 파생 산출해 낸 극과 극 궤도 대조 결과 $\ell_2$ 노름 쾌거 계산치를 과감히 대조 공개합니다. 위 지표 전황과 뼈저릴 정도로 대조 비교 대비되듯, 이처럼 미약 허약하기 짝이 없는 작게 쪼그라든 임계 제재 수치 $\lambda$ 세팅에 묶인 모델들의 도출 결괏값 계수 노름 $\ell_2$ 치수가 앞선 단단 탄탄한 세팅 구속 상황과는 전면 다르게 아예 압도 거대 풍선 팽창하듯 폭발적으로 파급 치솟아 확장 상승 점거해 버렸다는 단적인 현상 반증 메커니즘을 두 눈똑똑히 확연 감시 지각해 주시길 부탁 당부합니다.

```python
In [27]: beta_hat = soln_path.loc[soln_path.index[59]]
lambdas[59], np.linalg.norm(beta_hat)
```

```
Out[27]: (0.2437, 160.4237)
```

Above we normalized `X` upfront, and fit the ridge model using `Xs` . The `Pipeline()` object in `sklearn` provides a clear way to separate feature normalization from the fitting of the ridge model itself.
앞선 거대 시작 첫 연산의 도달 관문에서 짚었듯, 우린 척박한 무 모델 원천 변수 `X` 매트릭스 전체 체계를 아주 먼저 단호 선행 지시 작업으로써 정밀한 정규화 강제 변환 조작 처리 전파 단계를 이식 단행했었으며, 결론으로 얻은 `Xs` 치환 파생 객체 배열을 바탕에 뿌리 깊게 통제 이행시켜 타겟인 릿지(ridge) 다중 정규화 회귀 구축 모델 구조를 차례로 종속 적합 달성시켰음을 명확히 상기해 보십시오. 무려 파이썬 통계 모듈 체제 `sklearn` 연산 장치 엔진 속에 애초부터 구축 탑재 접합 내장되어 파생 제공되는 어마어마한 성능 탑 툴 장비 `Pipeline()` (파이프라인) 객체 조립 연결 조인트 장치는, 이러한 앞단에 머물던 까탈스런 특질 전위 전처리 정규화(feature normalization) 데이터 치환 과정 수수 이행 단계를 무사히 그 뒤를 잇는 릿지 체계 모형의 완전 결합 적합 수행 실체 연결 본선 모형 조작 단체 체계로부터 아주 무결한 분리, 단절된 투 트랙 설계 조각 모의로 단일 명쾌하게 동떨어져 단독 독립 분리 구동 분 관제할 수 있는 말문 막히게 절묘 신통하고 깔끔 예리한 수동 독립 모의 도출 시연 컨트롤 지침 가동 통로 구조 체제를 친절 안내 결연해 제공 시사합니다.

```python
In [28]: ridge = skl.ElasticNet(alpha=lambdas[59], l1_ratio=0)
scaler = StandardScaler(with_mean=True, with_std=True)
pipe = Pipeline(steps=[('scaler', scaler), ('ridge', ridge)])
pipe.fit(X, Y)
```

We show that it gives the same $\ell_2$ norm as in our previous fit on the standardized data.
우리는 이런 대체 파이프라인 우회 방편 통제 이행 가동 절차 도출 과정 결론지가 결국엔 앞서 우리가 손발 동원 노가다로 선행 사전 차단 치환해 두었던 조작 정규 상태 규격 데이터 토대 무대 위에서 종단 거쳐 연산 회전시켰던, 기존의 스펙 평가 결과 잣대 도출 객체의 $\ell_2$ 노름 수확물과 단 한 줌 일말의 오차 편차율도 없는 소름 돋게 전면 똑같은 붕어빵 카피 노름 도출 아웃풋 치수값을 무단 산출 결론 토해낸다는 짜릿한 사실 증명을 여러분 눈앞 증빙 화면에 노출합니다.

```python
In [29]: np.linalg.norm(ridge.coef_)
```

```
Out[29]: 160.4237
```

Notice that the operation `pipe.fit(X, Y)` above has changed the `ridge` object, and in particular has added attributes such as `coef_` that were not there before.
이 절묘한 접합 지점에서, 무릇 방금 투입한 저 파이프 도출 구동 연결 단락 상기 파이썬 코드 `pipe.fit(X, Y)`의 지시 작동 통제 조작 결단 명령이, 단 한 번의 엔터 연산으로 앞단의 훈련 빈 깡통 본체 주체였던 `ridge` 무대 훈련 구속 객체 체계 자체를 완전 고차원 단계 조작 변환, 탈바꿈 셋업 세팅시켰단 사실 조작 현황 변화 지표를 결코 가볍게 넘기지 마시고 단단히 포착 경계 포착 주의해 인지 살피십시오. 덧붙여 그러한 특단 변경 사항 내부 스펙 사양 표면 변화의 파급 여파 중에서도 부수적으로, 모형 모델이 맨 처음 태어났던 최초 탑재 구성 깡통일 적엔 두 눈 비비고 찾아봐도 없었던 `coef_` (마침내 연산을 마친 단면 계수 산출 체제 확정 수치) 애트리뷰트 구조 파편 단위를 객체의 무결성 속 무단 강제 자기 모델 안으로 단독 추가 생성, 영구 접합 이식시켜 뼈에 각인 심어 두었다는 아주 무서운 강력 특이점 팽창 변화 구조 단계를 제발 꼼꼼 예의 세심히 관찰 주시 투시해 보십시오.

## Estimating Test Error of Ridge Regression
## 릿지(능선) 정규 회귀 모델 테스트 오차율 도출 평가 예측 검증 산출

Choosing an _a priori_ value of $\lambda$ for ridge regression is difficult if not impossible. We will want to use the validation method or cross-validation to select the tuning parameter. The reader may not be surprised that the `Pipeline()` approach can be used in `skm.cross_validate()` with either a validation method (i.e. `validation` ) or _k_-fold cross-validation.
어떤 형태의 능선 릿지(ridge) 정규 회귀 모형 무대를 맨바닥에 삽질해 만들려 시도할 때든, 예측 평가 투입 직전 고작 통계학 교재로 배운 얄팍한 _선험적 직관력(a priori)_ 지식만 빌려다가 수많은 파라미터 후보 바다 중에서 완벽한 조율 튜닝 성능을 끌어올릴 억압 파라미터 $\lambda$ 수치값을 신 들린 듯이 미리 콕 집어 골라내는 행위는 기적에 가깝습니다. 따라서 우리들은 파라미터 결단 조율 단계에서 현명한 기교 수단으로 단일 검증(validation) 방식이나 교차 검증(cross-validation) 기법을 적극 채용해 무난히 넘어가고자 할 것입니다. 독자 여러분은 지금까지 줄곧 써왔던 이 신통방통한 '파이프라인 결합 장치(`Pipeline()`)' 접근법이, 단순한 단일 쪼개기 검증 세트 방식이든 험난하게 잘게 부숴 여러 번 돌려 깎는 _k_-폴드 분할 교차 검증 기법이든 방법론을 따지지 않고 양쪽 모두 매끄럽게 호환되어 `skm.cross_validate()` 평가 장치 안에서 자연스레 연동 가동된다는 파격적 확장성에 대해 그다지 크게 놀라 자빠지진 않으셨으리라 짐작됩니다.

We fix the random state of the splitter so that the results obtained will be reproducible.
우리는 측정된 계산 연산 지표 도출 결괏값들이 추후 언제 다시 테스트해도 똑같이 소름 돋게 재현(reproducible) 산출 가능할 수 있도록 파편 분할기(splitter)의 난수 발생 위치(random state)를 임의 단독 고정 조치합니다.

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
