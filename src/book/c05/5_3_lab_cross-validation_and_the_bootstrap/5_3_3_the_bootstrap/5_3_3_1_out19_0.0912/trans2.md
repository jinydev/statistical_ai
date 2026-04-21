---
layout: default
title: "trans2"
---

# `Out[19]:` `0.0912`

The final output shows that the bootstrap estimate for $\text{SE}(\hat{\alpha})$ is $0.0912$. 
계산기가 뱉어낸 영수증을 보니, 방금 부트스트랩 호문쿨루스가 뽑아낸 마법의 파이 $\hat{\alpha}$ 오차율 타점(표준 오차 $\text{SE}$) 이 $0.0912$ (약 9%) 언저리를 돌고 있음을 입증하네요(shows)!

### Estimating the Accuracy of a Linear Regression Model 
### 응용편: 선형 회귀 뼈대 모델에 부트스트랩 폭격 타진하기

The bootstrap approach can be used to assess the variability of the coefficient estimates and predictions from a statistical learning method. Here we use the bootstrap approach in order to assess the variability of the estimates for $\beta_0$ and $\beta_1$, the intercept and slope terms for the linear regression model that uses `horsepower` to predict `mpg` in the `Auto` data set. We will compare the estimates obtained using the bootstrap to those obtained using the formulas for $\text{SE}(\hat{\beta}_0)$ and $\text{SE}(\hat{\beta}_1)$ described in Section 3.1.2. 
설마 부트스트랩 이 사기급 연금술이 고작 펀드 투자 장난감 놀이에만 쓰일 거라고 상상하신 겁니까? 놉! 부트스트랩은 세상 모든 잡다한 통계 머신러닝 기계에서 튀어나오는 온갖 파라미터 계수 덩어리들이나 예측 점수들의 "오락가락 널뛰기 판도(variability)" 를 심판하는 전천후 폭격기로 투입(used to assess) 됩니다. 자, 우리들의 구 여친 같은 `Auto` 데이터를 데려옵시다. 우린 마력(`horsepower`) 으로 연비(`mpg`) 를 쑤셔 맞히는 1차선 뼈대(선형 회귀 모델) 의 두 기둥, $\beta_0$ (기본 마일리지 절편) 와 $\beta_1$ (엑셀 밟을 때 깎이는 연비 기울기) 녀석들이 실전에서 얼마나 출렁거리는지 부트스트랩 몽둥이로 털어보겠습니다. 그다음 꿀잼 관전 포인트! 이렇게 최첨단 해킹 부트스트랩으로 짜낸 신식 오차율 견적서랑, 옛날 3.1.2 챕터 꼰대들이 쓰던 곰팡내 나는 고전 수학 공식표로 뽑아낸 $\text{SE}(\hat{\beta}_0)$, $\text{SE}(\hat{\beta}_1)$ 구식 견적서를 나란히 세워놓고 맞짱 대조(compare) 시켜보겠습니다.

To use our `boot_SE()` function, we must write a function (its first argument) that takes a data frame `D` and indices `idx` as its only arguments. But here we want to bootstrap a specific regression model, specified by a model formula and data. We show how to do this in a few simple steps. 
이 꿀잼 배틀을 위해 방금 만든 매크로 함수 `boot_SE()` 에 시동을 걸어야 하는데요. 한 가지 귀찮은 룰이 있습니다(must write). 이 매크로 엔진 입구(첫 번째 인자) 안에는 오직 데이터 덩어리 `D` 랑 번호표 `idx` 단 두 개의 구멍만 뚫려 있는 '부품 함수' 를 만들어서 끼워 넣어야 하거든요. 근데 우리는 그냥 단순 계산이 아니라, 아예 '어떤 데이터로 무슨 공식을 돌릴지' 각 잡고 세팅해 놓은 무거운 회귀 모델 덩어리 자체를 부트스트랩 뺑뺑이판 위에 얹고 싶잖아요(want to)? 파이썬 짬바를 발휘해서 이 귀찮은 세팅을 단 몇 줄 코딩(few simple steps) 만에 우회 타격하는 해킹쇼(show) 를 보여드리겠습니다.

We start by writing a generic function `boot_OLS()` for bootstrapping a regression model that takes a formula to define the corresponding regression. We use the `clone()` function to make a copy of the formula that can be refit to the new dataframe. This means that any derived features such as those defined by `poly()` (which we will see shortly), will be re-fit on the resampled data frame. 
일단 다재다능한 십자드라이버 같은 예비 함수 `boot_OLS()` 를 하나 깎아냅니다(writing). 이 녀석은 우리가 점지해 준 회귀 모델의 뼈대 수식 자체를 집어삼킬(takes a formula) 수 있죠. 여기서 파이썬의 치트키 `clone()` 이란 녀석을 갈아 넣을 겁니다. 얘가 뭐냐? 찌그러진 오리지널 뼈대 공식을 순식간에 복제(copy) 해서, 나중에 끝없이 생성될 가짜 클론 데이터 부대 위에도 딱딱 리-피팅(refit) 이 되도록 문줄을 녹여주는 놈입니다. 이 미친 기능이 왜 사기냐고요(means that)? 잠시 뒤 우리가 마력 파라미터에다 2차 커브니 3차 곡선이니 온갖 조미료를 버무려 파생시킨 `poly()` 변이 괴물들을 집어넣어도(derived features), 매번 새롭게 뽑히는 클론 부트스트랩 군단 데이터판 위에서 알잘딱깔센으로 알아서 리-피팅(re-fit) 되어 찰떡 융화된다는 무시무시한 의미가 강제 부여되거든요!

```python
In [20]: def boot_OLS(model_matrix, response, D, idx):
             D_ = D.loc[idx]
             Y_ = D_[response]
             X_ = clone(model_matrix).fit_transform(D_)
             return sm.OLS(Y_, X_).fit().params
```

This is not quite what is needed as the first argument to `boot_SE()`. The first two arguments which specify the model will not change in the bootstrap process, and we would like to _freeze_ them. The function `partial()` from the `functools` module does precisely this: it takes a function as an argument, and freezes some of its arguments, starting from the left. We use it to freeze the first two model-formula arguments of `boot_OLS()`. 
근데 이 드라이버만 만들어놓고 보면 치명적 결함이 하나 있습니다. 입구 모양새가 아직 메인 엔진 `boot_SE()` 구멍에 안 맞아요(not quite what is needed). 저 함수 앞단 1번 2번 구멍은 "야 나 이 모델 공식 쓸 거야!" 라고 선언하는 구멍인데, 솔직히 이 뼈대는 부트스트랩 수천 번 뺑뺑이를 도는 내내 절!대! 안 바뀔(will not change) 고정 뼈대잖아요? 그래서 우린 코딩 치트키를 써서 이 구멍들을 아예 시멘트로 공구리 쳐서 **"동결(freeze)"** 파업시켜 버릴 겁니다(would like to). 바로 파이썬 창고 `functools` 에서 꺼내온 `partial()` 광선총의 능력이죠(precisely this). 이 총을 함수에 쏘면, 왼쪽 앞단 구멍부터 차례차례 원하는 인자들을 얼음 땡 시켜서 평생 그 값만 품고 고착화되게 동결(freezes) 마비시킬 수 있습니다. 오케이, 이 광선총으로 아까 만든 드라이버 `boot_OLS()` 의 앞 구멍 두 개(모델과 뼈대 수식) 를 차갑게 고정(freeze) 시켜 버립시다!

```python
In [21]: hp_func = partial(boot_OLS, MS(['horsepower']), 'mpg')
```

Typing `hp_func?` will show that it has two arguments `D` and `idx` — it is a version of `boot_OLS()` with the first two arguments frozen — and hence is ideal as the first argument for `boot_SE()`. 
자 이렇게 개조된 부품 `hp_func` 에다 물음표(`?`) 딱 찍어서 터미널에 스펙을 취조해 보면? 짜잔! 앞쪽 모델 뼈대 구멍 2개는 얼음 땡 당해서 완전히 숨겨졌고(frozen), 오직 `D`(어항판) 랑 `idx`(번호표) 라는 두 구멍만 덩그러니 살아있는 게 보일 겁니다(show). 크~ 이거죠! 드디어 아까 그 까다롭던 `boot_SE()` 메인 엔진의 1번 타자 구멍에 한 치의 오차 없이 딱 들어맞는 완벽한 조립 부속(ideal as) 이 창조된 겁니다(hence)! 

The `hp_func()` function can now be used in order to create bootstrap estimates for the intercept and slope terms by randomly sampling from among the observations with replacement. We first demonstrate its utility on 10 bootstrap samples. 
이제 장전 완료된 저 개조 함수 `hp_func()` 권총 방아쇠만 당기면(can now be used), 알아서 `Auto` 어항판 전체 표본에서 미친 듯이 뺑뺑이 복원 낚시질(sampling with replacement) 을 조지면서 쉴 새 없이 두 개의 기둥(절편과 기울기 타자 intercept and slope terms) 파라미터의 변동치 견적서를 인쇄해(create) 뱉어냅니다! 본격 매크로를 돌리기 전 간 보는 심정으로 딱 10발짜리 스몰 테스트(demonstrate) 격발을 해보겠습니다.

```python
In [22]: rng = np.random.default_rng(0)
         np.array([hp_func(Auto,
                           rng.choice(392,
                                      392,
                                      replace=True)) for _ in range(10)])
```

```python
Out[22]: array([[ 39.8806, -0.1568],
                [ 38.733 , -0.147 ],
                [ 38.3173, -0.1444],
                [ 39.9145, -0.1578],
                [ 39.4335, -0.1507],
                [ 40.3663, -0.1591],
                [ 39.6233, -0.1545],
                [ 39.0581, -0.1495],
                [ 38.6669, -0.1452],
                [ 39.6428, -0.1556]])
```

Next, we use the `boot_SE()` function to compute the standard errors of 1,000 bootstrap estimates for the intercept and slope terms. 
10발 연습 사격 이상 무! 다음 코스(Next), `boot_SE()` 메인 매크로 엔진의 터보 버튼을 눌러서, 절편 기둥과 연비 기울기 타자에 날아갈 **1,000발(B=1000) 의 부트스트랩 견적 미사일** 을 모조리 폭격(compute) 해 그 요동 오차(standard errors) 타율을 싹 다 파내봅시다!

```python
In [23]: hp_se = boot_SE(hp_func,
                         Auto,
                         B=1000,
                         seed=10)
         hp_se
```

```python
Out[23]: intercept     0.8488
         horsepower    0.0074
         dtype: float64
```

This indicates that the bootstrap estimate for $\text{SE}(\hat{\beta}_0)$ is $0.85$, and that the bootstrap estimate for $\text{SE}(\hat{\beta}_1)$ is $0.0074$. As discussed in Section 3.1.2, standard formulas can be used to compute the standard errors for the regression coefficients in a linear model. These can be obtained using the `summarize()` function from `ISLP.sm`. 
타깃 포획 스코어보드를 보시라(indicates)! 우리의 자랑스러운 부트스트랩 클론 부대가 1,000번의 전투 끝에 물어온 정보입니다. 뼈대 절편 $\text{SE}(\hat{\beta}_0)$ 오차율 파동은 약 $0.85$! 그리고 마력 기울기 $\text{SE}(\hat{\beta}_1)$ 변이 오차 폭은 고작 $0.0074$ 로 좁혀졌네요. 자 이 영수증을 손에 꽉 쥐고 계세요. 왜냐고요? 아까 도발했던 메인 이벤트! 옛날 Section 3.1.2 꼰대들이 무식하게 외워 쓰던 선형 판 고전 수학 공식(standard formulas) 의 낡은 스코어판과 맞장 뜰 시간(discussed) 이니까요. 그 낡은 옛날 성적표 쪼가리(These)? 훗, `ISLP.sm` 서랍에 굴러다니는 `summarize()` 딸깍 스위치 한 번만 눌러도 우주선 티켓 뽑히듯 손쉽게(can be obtained) 튀어나옵니다.

```python
In [24]: hp_model.fit(Auto, Auto['mpg'])
         model_se = summarize(hp_model.results_)['stderr']
         model_se
```

```python
Out[24]: intercept     0.717
         horsepower    0.006
         Name: stderr, dtype: float64
```

The standard error estimates for $\hat{\beta}_0$ and $\hat{\beta}_1$ obtained using the formulas from Section 3.1.2 are 0.717 for the intercept and 0.006 for the slope. Interestingly, these are somewhat different from the estimates obtained using the bootstrap. Does this indicate a problem with the bootstrap? In fact, it suggests the opposite. Recall that the standard formulas given in Equation 3.8 on page 75 rely on certain assumptions. For example, they depend on the unknown parameter $\sigma^2$, the noise variance. We then estimate $\sigma^2$ using the RSS. Now although the formula for the standard errors do not rely on the linear model being correct, the estimate for $\sigma^2$ does. We see in Figure 3.8 on page 99 that there is a non-linear relationship in the data, and so the residuals from a linear fit will be inflated, and so will $\sigma^2$. Secondly, the standard formulas assume (somewhat unrealistically) that the $x_i$ are fixed, and all the variability comes from the variation in the errors $\epsilon_i$. The bootstrap approach does not rely on any of these assumptions, and so it is likely giving a more accurate estimate of the standard errors of $\hat{\beta}_0$ and $\hat{\beta}_1$ than the results from `sm.OLS`. 
꼰대들의 낡은 교과서 공식 타율(obtained using formulas) 을 봅시다. 절편 구역 $0.717$, 마력 기울기 파트 $0.006$. 어라? 개꿀잼 몰카인가요(Interestingly)? 방금 우리가 파이썬 헬기 팬 갈아서 뽑은 최첨단 부트스트랩 견적서($0.85$ / $0.0074$) 랑 은근슬쩍 격차(somewhat different) 가 벌어져 있습니다. 이 사태를 보면 코린이들은 이렇게 호들갑을 떨 겁니다. "헐! 킹갓 부트스트랩 기계에 뻑이 났나 보네(problem)?" 하.지.만! 코딩판 진실(In fact) 은 그 완전 정반대(the opposite) 역설을 가르킵니다. 자, 기억의 늪을 건너 옛날 75페이지 꼰대 족보 방정식 "Equation 3.8" 기조를 뇌세포에서 복원해 봅시다(Recall). ඒ 옛날 수학 뼈대 수식들은 어줍짢게 "데이터가 이러이러할 것이다" 라는 개소리 환상 전제 조건(certain assumptions) 몇 개를 독단적으로 깔고 맹신(rely on) 해요. 예를 들어(For example), 그 낡은 공식은 $\sigma^2$ (에러 찌꺼기들이 미쳐 날뛰는 정도) 라는, 원래 아무도 모르는 신계 비밀치에 목숨 걸고 의탁(depend on) 합니다. 근데 우린 이 비밀치를 모르잖아요? 그래서 에러 잔차 제곱합 쓰레기(RSS) 로 대충 퉁쳐서 조작 날조(estimate) 했죠. 근데 여기서 맹점이 터집니다(Now)! 아무리 낡은 수학 공식 자체는 이 선형 1차선 직진 모델이 개판이든 말든 상관상관 안 한다(do not rely on) 쳐도요, 퉁쳐서 만든 저 $\sigma^2$ 라는 가짜 부품만큼은 완전히 이 1차선 구닥다리 모델이 내뿜는 에러 찌꺼기에 100% 매몰 종속된다(does) 는 딜레마입니다! 우리 다 봤잖아요(see)? 옛날 99페이지 Figure 3.8에서 이 데이터 바닥 모양은 부드러운 U-커브형(non-linear relationship) 인데, 그걸 무식하게 1차선 꼬챙이로 후벼 팠으니 거기서 떨어진 잔차 찌꺼기 점수(residuals) 들이 얼마나 미친 듯이 펑튀기되고 과포장(inflated) 됐겠습니까! 그러니까 딸려온 $\sigma^2$ 도 덩달아 뻥튀기되고 뭉개져버린 거죠(so will $\sigma^2$). 거기다 결정타 하나 더(Secondly)! 그 낡은 학자들 공식은 "야, 관측치 $x_i$ 변수 애들은 돌부처처럼 가만있어. 오직 오차 $\epsilon_i$ 파편들만 미치광이처럼 돌아다니는 거야(all the variability comes from)" 라고 아~주 비현실적으로 뇌피셜 행복 기만 상상(assume somewhat unrealistically) 을 우겨 넣고 있습니다. 자 끝났죠? 우리의 사기급 연금술 부트스트랩! 이 미친 공법은 방금 조롱한 그따위 망상 뇌피셜 전제(any of these assumptions) 나 족쇄에 눈곱만큼도 의지하거나 굴복하지 않는 패기 보소(does not rely on)! 고로(and so), `sm.OLS` 꼰대 기계가 방출한 쓰레기 결과물(results from) 이랑은 비교도 안 되게 아득히 쾌속으로 훨씬 더 정확하고 영리하게(more accurate estimate) 팩트 타점인 진짜 오차 스펙을 때려 부수고 있는 건 다름 아닌 부트스트랩 연금술의 승리(is likely) 인 겁니다!

Below we compute the bootstrap standard error estimates and the standard linear regression estimates that result from fitting the quadratic model to the data. Since this model provides a good fit to the data (Figure 3.8), there is now a better correspondence between the bootstrap estimates and the standard estimates of $\text{SE}(\hat{\beta}_0)$, $\text{SE}(\hat{\beta}_1)$ and $\text{SE}(\hat{\beta}_2)$. 
자, 증명 들어갑니다(Below). 이번엔 데이터를 무식하게 찌르던 1번 선형 창을 버리고 부드러운 U자형 2차 커브 곡선(quadratic model) 을 데이터에 얹은 뒤(fitting), '부트스트랩의 쾌속 산출판' 과 '고전 수학 꼰대 산출판' 양쪽 파벌의 멱살을 잡고 동시에 점수를 계산(compute) 해봤습니다. 아까 말했듯 이 2차 커브 곡선이야말로 이 자동차 데이터 늪지대 곡률에 예술적으로 쫙 달라붙잖아요(good fit)? 그랬더니 세상에! 드디어 엉터리 망상이 걷어지며, 우리의 최첨단 부트스트랩 지어 오차율과 고전파 꼰대 수학 측량 지표들 사이에 아주 아름답고 놀라운 동!기!화! 일치율(better correspondence) 기적이 발발합니다! $\text{SE}(\hat{\beta}_0)$ 는 물론, $\text{SE}(\hat{\beta}_1)$, $\text{SE}(\hat{\beta}_2)$ 까지 싹 다요!

```python
In [25]: quad_model = MS([poly('horsepower', 2, raw=True)])
         quad_func = partial(boot_OLS,
                             quad_model,
                             'mpg')
         boot_SE(quad_func, Auto, B=1000)
```

```python
Out[25]: intercept                          2.067840
         poly(horsepower, 2, raw=True)[0]   0.033019
         poly(horsepower, 2, raw=True)[1]   0.000120
         dtype: float64
```

We compare the results to the standard errors computed using `sm.OLS()`. 
자, 방금 도출한 그 영광스런 결과물들(results) 을 낡은 `sm.OLS()` 통계 보증 수표(the standard errors) 에 갖다대고 교차 검증 대조전(compare) 을 스캔해 마무리합니다.

```python
In [26]: M = sm.OLS(Auto['mpg'],
                    quad_model.fit_transform(Auto))
         summarize(M.fit())['stderr']
```

```python
Out[26]: intercept                          1.800
         poly(horsepower, 2, raw=True)[0]   0.031
         poly(horsepower, 2, raw=True)[1]   0.000
         Name: stderr, dtype: float64
```
