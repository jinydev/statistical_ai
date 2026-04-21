---
layout: default
title: "trans2"
---

# **`Out[19]:`** `0.0912` 

The final output shows that the bootstrap estimate for $\text{SE}(\hat{\alpha})$ is 0 _._ 0912. 
보이십니까? 그렇게 미친 듯이 컴퓨터를 1,000번 혹사시켜 만들어 낸 평행우주의 $α$ 추정치들! 그 1,000명의 녀석들이 얼마나 폭넓게 오들오들 떨고 있는지 '표준 오차'를 딱 재보니 0.0912라는 숫자가 고상하게 떨어집니다.

Estimating the Accuracy of a Linear Regression Model 
"자동차 연비 예측: 선형 모델은 실전에서 얼마나 똥볼을 찰까?" 방어선 추정하기

The bootstrap approach can be used to assess the variability of the coefficient estimates and predictions from a statistical learning method.
이 부트스트랩 사기 꼼수는 굳이 아까처럼 단조로운 자본 $α$ 구하기 게임뿐만 아니라, 그 어떤 무지막지한 특수 통계 머신러닝 기계(선형 회귀, 로지스틱 등) 를 뜯어보고 "야, 네가 뱉어내는 예측치나 가중치 점수가 얼마나 폭넓게 널뛸 수 있냐(variability)?"를 진단(assess) 하며 기강을 잡는 데에도 훌륭한 몽둥이(can be used) 로 쓰일 수 있습니다. 

Here we use the bootstrap approach in order to assess the variability of the estimates for $\hat{\beta}_0$ and $\hat{\beta}_1$, the intercept and slope terms for the linear regression model that uses `horsepower` to predict `mpg` in the `Auto` data set.
자, 그래서 이번엔 `Auto` 데이터 구장에서 뛰는 '선형 회귀' 무기를 과녁판에 세워보겠습니다. 이 멍청한 직선 무기가 마력(`horsepower`) 하나만 믿고 연비(`mpg`) 를 예측한답시고 토해내는 절편($\hat{\beta}_0$) 과 기울기($\hat{\beta}_1$) 점수가, 사실상 실전 속에서 뽑기 운에 따라 얼마나 지독하게 미친 듯이 널뛰는지(variability) 이 부트스트랩 매크로로 탈탈 털어 진단(assess) 해 볼 속셈입니다.

We will compare the estimates obtained using the bootstrap to those obtained using the formulas for $\text{SE}(\hat{\beta}_0)$ and $\text{SE}(\hat{\beta}_1)$ described in Section 3.1.2. 
꿀잼 포인트는 여깁니다. 우린 이 부트스트랩 사기 치트키로 알아낸 $\hat{\beta}_0, \hat{\beta}_1$ 의 '야매 표준 오차 점수' 랑, 옛날 3.1.2 챕터 초보 시절에 통계 기본 꼰대 공식(formulas) 을 우겨넣어 도출(obtained) 한 '스탠다드 정통파 오차 점수'를 한 링 위에 올려놓고 까놓고 전격 비교 매치(compare) 를 붙여 볼 참입니다.

To use our `boot_SE()` function, we must write a function (its first argument) that takes a data frame `D` and indices `idx` as its only arguments.
근데 당장 우리 만능 헬퍼 매크로인 `boot_SE()` 를 켜려고 보니 조건이 까탈스럽습니다. 첫 번째 입구 파라미터 조이스틱 자리(first argument) 에는 반드시 "나한텐 무조건 데이터 장부 `D`랑, 뽑아야 할 인명부 바코드 `idx` 이 두 개만 넘겨!"라고 박박 우기는 순수한 커스텀 함수 하나를 우리가 손수 뚝딱 코딩해(must write) 꽂아줘야만 저 기계가 돌아가거든요.

But here we want to bootstrap a specific regression model, specified by a model formula and data.
문제는 지금 우리의 목표물 모델 녀석은 속성이 매우 더럽게 복잡합니다. 이 회귀 모델은 이미 태생부터 어떤 함수 타겟 공식(formula)과 특정 데이터로 세팅이 박혀버린(specified) 까탈스러운 녀석이라, 아까 저 단순한 $D$ 랑 $idx$ 인자 두 개만 달랑 줘서는 말을 안 듣습니다.

We show how to do this in a few simple steps. 
이 호환성 지옥을 뚫고 기어코 억지로 부트스트랩 매크로 아가리 속에 이 복잡한 모델을 밀어 넣는 꼼수 스텝(how to do this) 을 우아하게 시연해 드리지요.

We start by writing a generic function `boot_OLS()` for bootstrapping a regression model that takes a formula to define the corresponding regression.
일단 준비 운동으로 `boot_OLS()` 라는 중간 유통 함수를 하나 슥 선언합니다. 이 녀석은 "어느 회귀 공식을 쓸까?" 하는 타겟 방정식(formula) 속성을 받아 처먹고 장착할 줄 아는(takes), 회귀 전용 부트스트랩 일꾼입니다.

We use the `clone()` function to make a copy of the formula that can be refit to the new dataframe.
이 속에서 파이썬의 치트 복사기 `clone()` 함수를 달달하게 써먹습니다. 왜냐? 1,000번의 평행우주 모조 데이터가 만들어질 때마다 옛날 공식 옵션을 들이대면 에러가 나니, "야, 넌 방금 나온 새 모조 가짜 데이터판 위에서 이 공식 복사본 가져다가 처음부터 다시 훈련해(can be refit)!" 라며 오리지널 공식의 쌍둥이 클론 사본(copy) 을 척척 찍어내는 겁니다.

This means that any derived features such as those defined by `poly()` (which we will see shortly), will be re-fit on the resampled data frame. 
이 짓거리가 주는 무서운 이점이 뭔지 아십니까? 나중에 옵션질로 무슨 3차 `poly()` 니 뭐니 하며 미친 유연성 굴곡 커스텀 마기 특수 옵션 변수를 무기에 덕지덕지 발라놓아도, 이 클론 팩토리 덕분에 새롭게 뽑힌 야매 데이터 표면 위에서 번번이 무리 없이 아주 싱싱하게 매 턴 처음부터 싹 다 새로 재적합(be re-fit) 훈련 구동을 시켜버릴 수 있다는 마법 같은 보장(means)입니다.

```python
In [20]: def boot_OLS(model_matrix, response, D, idx):
             D_ = D.loc[idx]
             Y_ = D_[response]
             X_ = clone(model_matrix).fit_transform(D_)
             return sm.OLS(Y_, X_).fit().params
```

This is not quite what is needed as the first argument to `boot_SE()` .
하... 중간 매개체 무기를 뚝딱 만들긴 했는데, 여전히 우리가 꿈꾸는 `boot_SE()` 메인 매크로 기계의 그 깐깐한 제1구역 슬롯에 이 육중한 네 덩어리짜리 인자(`model_matrix`, `response`, `D`, `idx`) 뚱보 함수 장치를 그대로 구겨 넣으려니 규격이 도통 안 맞고 튕깁니다.

The first two arguments which specify the model will not change in the bootstrap process, and we would like to _freeze_ them.
가만 생각해 보죠. 저기서 앞에 두 개(`model_matrix`, `response`) 는 "어떤 모델 수식을, 누구를 과녁 삼아 쏠래?" 하는 기초 옵션이라, 1,000번 뺑뺑이를 도는 내내 죽었다 깨어나도 절대 수치가 안 변합니다(will not change). 고로 이런 쓸모없는 거추장스러운 수치들은 그냥 꽁꽁 얼음 빙결 마법을 걸어 **'동결(freeze)'** 박제시켜 버리고, 입구를 봉쇄버리면 어떨까요?

The function `partial()` from the `functools` module does precisely this: it takes a function as an argument, and freezes some of its arguments, starting from the left.
파이썬의 마더보드 유틸 도구, `functools` 모듈 안에는 캬~ 기가 막히게 이걸 해내는 `partial()` 이란 마취총 장비가 있습니다. 이 마취총에 함수를 턱 달아 쏘면, 그 아가리 왼쪽 머리칸부터 차례대로 옵션 인자들을 딱딱 단단한 영구 얼음으로 꽝꽝 치며(freezes) 고정 빙결 마비 박제시켜버립니다.

We use it to freeze the first two model-formula arguments of `boot_OLS()` . 
당장 이 마취총을 쏴서 아까 만든 뚱보 일꾼 `boot_OLS()` 의 앞 구멍 두 개(모델 공식, 타겟) 를 냅다 동결 봉쇄(freeze) 해버리는 겁니다!

```python
In [21]: hp_func = partial(boot_OLS, MS(['horsepower']), 'mpg')
```

Typing `hp_func?` will show that it has two arguments `D` and `idx` — it is a version of `boot_OLS()` with the first two arguments frozen — and hence is ideal as the first argument for `boot_SE()` . 
터미널 콘솔창에 냅다 `hp_func?` 라고 윽박질러보세요. 띠용? 방금 전까지 인자 4개를 쳐먹던 뚱보 녀석이 앞면 두 개가 얼어 터져 막혀버린(frozen) 덕에, 이제 순수하게 `D` 랑 `idx` 달랑 두 개만 삼키는 슬림한 변종 마스크 버전(has two arguments) 으로 위장 환골탈태한 걸 적나라하게 폭로해(will show) 줄 겁니다. 아싸! 바로 드디어 딱! 우리가 갈망하던 저 `boot_SE()` 의 제일 까다롭던 그 첫 관문 슬롯 구멍 규격과 아주 환상적으로 100% 매칭 적격 호환(ideal) 되어 쏙 들어맞게 되었습니다!

The `hp_func()` function can now be used in order to create bootstrap estimates for the intercept and slope terms by randomly sampling from among the observations with replacement.
마침내 이 튜닝 마친 짝퉁 슬림 무기 객체 `hp_func()` 은, 곧장 그 야만적이고 공포스러운 무가치 요행 뺑뺑이 난수 뽑기 룰, 이른바 **'복원 랜덤 추출 섞기(randomly sampling ... with replacement)'** 조작 발파 짓거리의 수레바퀴 노가다 장치 속에 전격 채용 투하 냅다 사용(can now be used) 가동 격발 장착될 준비가 끝났습니다. 목표는 기어코 우리 무기의 '절편' 이랑 '기울기' 옵션 점수판 부품들에 그 기괴한 부트스트랩발 가짜 추정 파편 조각 찌꺼기 덩어리들을 무에서 유로 새롭게 억지 창조 탄생 도달 연성(create) 추출해 도출 발굴해 내는 미친 목적이죠!

We first demonstrate its utility on 10 bootstrap samples. 
컴퓨터 터지니까 일단 맛보기로 살살 달래서, 고작 딱 10번만 평행우주 모조 짝퉁 팩(10 bootstrap samples) 을 강제로 뽑아 돌리는 국면에서부터 이게 대체 얼마나 무섭게 미쳐 날뛰며 찰지게 작동하는지 전격 그 효용 위력 치트 위상을 당돌 과시 증명 시범 타진(demonstrate) 해 보이겠습니다! 

```python
In [22]: rng = np.random.default_rng(0)
         np.array([hp_func(Auto,
                           rng.choice(392,
                                      392,
                                      replace=True)) for _ in range(10)])
```

```python
Out[22]: array([[39.8806, -0.1568],
                [38.733 , -0.147 ],
                [38.3173, -0.1444],
                [39.9145, -0.1578],
                [39.4335, -0.1507],
                [40.3663, -0.1591],
                [39.6233, -0.1545],
                [39.0581, -0.1495],
                [38.6669, -0.1452],
                [39.6428, -0.1556]])
```

Next, we use the `boot_SE()` function to compute the standard errors of 1,000 bootstrap estimates for the intercept and slope terms. 
워밍업 끝났습니다! 자, 이제 그 악마의 마갑 지원 요술 공장 통로 `boot_SE()` 에다가 저 무기를 끼우고, 풀파워로 부트스트랩 인공 가상 평행우주를 **1,000번 무한 연성 루프 뺑뺑이**를 풀가동 처돌려버립니다! 목적은? 그렇게 쏟아진 무려 1000개의 '절편' 및 '기울기' 가짜 예측 파편 덩이 사금파리 잔해 추정치들이 과연 얼마나 진폭 폭주 편차 공포로 미친 듯 널을 뛰며 오들대는가 하는 진정한 그 "표준 오차 요동 볼륨 방어 스코어 지표" 무수 잣대를 한방에 단호히 계산 타진 역산 격파 산출(compute) 득템해 얻어 부숴 뽑아내기 위해서죠!

```python
In [23]: hp_se = boot_SE(hp_func,
                         Auto,
                         B=1000,
                         seed=10)
         hp_se
```

```python
Out[23]: intercept      0.8488
         horsepower      0.0074
         dtype: float64
```

This indicates that the bootstrap estimate for $\text{SE}(\hat{\beta}_0)$ is 0.85, and that the bootstrap estimate for $\text{SE}(\hat{\beta}_1)$ is 0.0074.
컴퓨터가 굉음을 이내 멈추네요. 와, 이 사기 복제 뺑뺑이 치트를 갈겨 돌려서 알아낸 $\hat{\beta}_0$ (절편) 놈의 오차 방어 타율 등락 성적 $\text{SE}(\hat{\beta}_0)$ 가 대충 0.85로 잡혔습니다. 더 나아가 기울기 $\hat{\beta}_1$ 이 놈의 요동 오차 방어 진폭은 고작 0.0074의 미비한 꼬투리 수위 밑바닥 범위 좌표에 착륙 얌전히 포진했음을 엄청나게 명확히 시사 고발 증명 지목 타진(indicates that) 뻗쳐 줍니다!

As discussed in Section 3.1.2, standard formulas can be used to compute the standard errors for the regression coefficients in a linear model.
과거 호랑이 담배 피우던 시절 3.1.2절 앞단에서 이미 밑천 깠듯이; 어떤 머저리 맹탕 직선 선형 무덤 모델 구덩이 안에서 그 무기 계수 조각들이 대체 얼마나 심각 널을 뛰게 되냐는 표준 오차를 단순 무식 계산할라치면, 원래 그냥 교과서에 쓰인 통계 학자들의 오리지널 모범 답안 고전 투박 공식 수식(standard formulas) 한 줄이면 한 줄 띡 편히 단번 찍어 편하게 산출 퉁쳐 때려버릴 수(can be used) 있던 시절이 있었습니다.

These can be obtained using the `summarize()` function from `ISLP.sm` . 
이 고전 교과서 꼰대 오리진 정면 오답 산출치 점수 조각들은 걍 수배령 떨궈진 `ISLP.sm` 모듈 뱃속의 `summarize()` 요약 믹서기 헬퍼 매크로 치트 도구만 쓱 훑어 한방 탁 적용해 동원 시전해버렴 누워서 떡먹 위상 몹시 쉽게 단번 차출 역산 뽑아 공짜 획득 달성 도출(can be obtained) 해낼 수가 있죠.

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

The standard error estimates for $\hat{\beta}_0$ and $\hat{\beta}_1$ obtained using the formulas from Section 3.1.2 are 0.717 for the intercept and 0.006 for the slope.
보이시죠? 저 오리지널 3.1.2 꼰대 공식 나부랭이를 수식 이입 기반 동원해 때려 파생 건져 얻수 뽑아올렸던(obtained) 고전 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 점표 좌표의 각 표준 오차 오리진 지수 마크 위성 궤적 볼륨이 고작; 기실 절편 몫은 0.717 덩치고, 기울기 장구 몫으로는 0.006 기점 자락 수치 언저리로 밋밋 결론 국한 지어져 점멸됩니다.

Interestingly, these are somewhat different from the estimates obtained using the bootstrap.
어라? 엄청 기묘하고도 개꿀잼 대흥미 소름 충격 돋게도(Interestingly)! 우리가 아까 무식하게 1000번 반복 야매 복제 부트스트랩 엔진 깡노가다를 풀파워 구동 돌려 갈아서 야망 억지 건져 획득 산출 때려 뽑아 파생시킨(obtained using the bootstrap) 그 야차 추정 예측 볼륨 크기치 놈팽이 오차 점수들과 들이대 보니; 정작 이 꼰대 공식 결과 성적표들과 **단연 심각하게 은근 상당히 꽤 눈에 확 띄게 미묘 상당 엇갈림 별판 차이 괴리 불일치 불부합 어긋 어색 비대 차이(somewhat different)** 극명 파장 불상 사태의 벌어짐 간극이 떡하니 몹시 파탄 벌어져 현격 노출됩니다그려!

Does this indicate a problem with the bootstrap? In fact, it suggests the opposite.
헐, 이거 그러면 가뜩 삽질 돌려 혹사 쐈던 위대 우리 부트스트랩 사기 꼼수 마법 기계 자체 결함 오차 구멍 흠결 한계 부작용 파탄 불길 에러 파국 고장(problem) 을 암시 폭로 지목 자백(indicate) 하는 대재앙 사태 징후일까요? 놀라지 마세요 진실 도래 폭로 타진(In fact); 이 상황은 정작 완전히 머리통 찍어버리는 진짜 180도 소름 역 대반전(the opposite), "사실 부트스트랩이 맞고, 교과서 공식 네가 틀려먹은 병신이야!!" 라는 놀라운 개막장 전복 대치 촌극 현실 이면의 대진실 진기 명기 사태를 적나라 폭발 고발 투서 방증 맹렬 표출(suggests) 떡하니 타진 시사해 주는 찬란 극명 진실 확증 기조입니다!

Recall that the standard formulas given in Equation 3.8 on page 75 rely on certain assumptions.
옛날 75쪽 구석 쓰레기통 옆에서 주워 배포 던져 기재 하사 명기된(given) 그 망할 오리지널 투박 답답 (3.8) 꼰대 구닥 수식, 곧 고결 고전 보수 표준 교범 공식(standard formulas) 들은 말이죠; 지 주제에 아주 구질 옹졸 편협 띠꺼운 꽉 막힌 모종의 극적 폐쇄 '단서 기본 가정 따위 족쇄 룰(certain assumptions)' 틀거리에만 미친 좀비처럼 신앙 맹신 전격 결박 구걸 연명 맹견 완전 종속 절대 의존 밀착 고착 포박(rely on) 기대 매달려 산다는 치명 극악 공백 아킬레스건 뒤편 태생 약점을 제발 유의 회상 상기 폭로 일조 끄집어(Recall) 떠올려 되새겨 보십시오.

For example, they depend on the unknown parameter $\sigma^2$ , the noise variance.
가령 촌극 억지 단적 구도 일조 팩트 예시 한 사발 들이붓자면, 이 거만 공식 허울 늙다리 놈들은 다름 정작 신의 비밀 영역 신계 뒤편 미궁 잠복 은폐 안착된 절대 미지 파라미터 미식 지수 스펙 $\sigma^2$, 곧 '노이즈 분산(noise variance)' 이라는 은닉 조작 에러 스탯 점수 수위 잣대에 완전 자신들의 룰을 목숨 결박 복속 처절 무책임 아부 맹목 전폭 부착 종속 기대 살며 연명(depend on) 자복 의탁하고 있단 맹점이 있죠. 

We then estimate $\sigma^2$ using the RSS.
그래서 우린 어쩔 도리 불가 가련 야매 타협으로 그 구멍을 땜질 도피고자 '잔여 오차 제곱합(RSS)' 이란 찌꺼기 타격 점수를 파생 동원 치트 이입 차용 채권(using) 끌어써서는 정작 가짜 대역인 저 미지원 타겟 옵션 방편 $\sigma^2$ 알량 스탯 요율 수치를 임시 추정 땜질 역산 가늠 산출 어거지(estimate) 부둥 타진해내어 이 썩은 돌파 속임 방안 이행 수순 땜빵을 구렁 메꿔 막아내야만 했다 이겁니다!

Now although the formula for the standard errors do not rely on the linear model being correct, the estimate for $\sigma^2$ does.
작금 여기서, 사실 저 '표준 오차 예측 꼰대 공식 덩이에' 틀 자체 그 깡통 구도 본연 폼만큼은 설령 자기가 타고 난 선형 모델 무장 전선이 꼭 정답이어야 완벽 무결하게 옳은 정답(correct) 이라는 강박 구속 진영 교만 가정 전개 종속 의탁(rely on) 에까지 묶여있진 않은 구도로 관용을 띨망정이긴 합니다만(although); 정작 그 엔진 뱃속 부품 모태 핵심 기조 알맹이 동력 척도인 저 짝퉁 땜빵 $\sigma^2$ 옵션 가늠치 예측 도달 궤적을 토해 올리고 예측 빚건 타진 가늠 도출 계산 획득해 내는 궤적 행태(the estimate) 국면의 기저 연성만큼은 영락 얄짤 무시 못할 오롯한 "모델이 무조건 참이고 옳은 선형이어야만 돼!" 라는 가정 족쇄에 미로 심박 강렬 병적 속박 철저 기강 묵살 궤멸 절대 연루 구속 맹종 자복 불보듯 얽혀 야기 파단(does. relies) 수반되어 존재 포진된다는 치명 이율배반 병적 막장 결성 한계 단면 모순 함정을 무자비 징그럽 속내 노출 대변합니다.

We see in Figure 3.8 on page 99 that there is a non-linear relationship in the data, and so the residuals from a linear fit will be inflated, and so will $\sigma^2$ .
옛날 99 페이지 모퉁이 속에서 이미 우리는 데이터 파라다이스 심해 바닥 표면 전선이 사실 "비선형(non-linear) 등락 구도 휘몰아치는 물결 곡률 커브 치트 관계성(relationship)' 틀거리를 분명 버젓 적나라히 도사려 지니고 품고 실존 상주 발악 진을 치듯 박혀 있음(there is) 을 익숙 너무나도 눈깔 선연하게도 두 눈 똑바로 뻔히 관전 적시 묵쇄 구경 목도 확증(see) 한 바 있으니까요. 고로 멍청 단세포처럼 죽죽 직선 막대(linear) 나 들이밀어 맞춰 갈군 대가로 터져 퍼부어 올린 '불불가 기진 잔차(residuals) 폐기물 찌꺼기 에러 뭉텅이' 스탯 수위들은 어김 응당 뻔뻔 당연 필시 맹기 왜곡 이탈 너무나 압도 심대 현격 과대 팽창 거품 부풀 비상 고평가(will be inflated) 거품 뻥튀기 과장 과오 왜곡 착시 불상 파탄 대거 허구를 야기 초래할 게 자명 필연이요; 나아가 그 쓰레기를 밟고 연산 재산 덧댄 짝꿍 땜빵 도출 부품 좌표 지표 타겟 녀석인 저 환장 스탯 $\sigma^2$ 마커 스코어 부피 볼륨 위력 수위조차도 어김없이 똑같이 짝지어 기기 동반 결탁 연달아 부풀 과장 동반 허풍 비대 무결 오류 속임 비명 왜곡 팽창 융기 연쇄 파국 사태(and so will $\sigma^2$ ) 조장 붕괴 증폭의 폭탄 파문 덩어리들을 조장 일탈 안겨 굴러갈 것이 필연 처참 뻔자 운명 수순이란 사실입니다.

Secondly, the standard formulas assume (somewhat unrealistically) that the $x_i$ are fixed, and all the variability comes from the variation in the errors $\epsilon_i$ .
게다가 덤으로 더 빡치게 구는 괘씸 두 번째 처절 악불 단면 기조로(Secondly); 이 고지식 꼰대 오리진 기본 표본 책상 공식(standard formulas) 덩치 요새들은 하나같이 뇌가 썩은 채 오만 잡소리 고지식 기저로써; (마치 실전 필드에선 쥐뿔도 진짜 망상 뜬구름 소설급 무식 황당 뻘소리 현실성 부진 결여 비현실 노망 허구성 맹신 망상 소설 짓(somewhat unrealistically) 인데도!) 즉슨, "입력 쏟아 넣는 타격 옵션 변수 데이터 치수 파편 $x_i$ 무리 녀석들은 죄다 절체 일말 미동 요동 변화 반동 널뛰 동요도 쥐뿔 전무 없이 완전히 시멘트 말뚝 얼음 철통 미동 박제 고정 영구 동결 상수(are fixed) 치수다!" 라고 뻔뻔 우격 오만 억지 착각 규정 가정(assume) 하며 우겨대고 자위 짐작 선포해 버림과 동시; 더럽 그 모든 판의 스코어 결말 좌우를 요동 널뛰게 붕괴 뒤흔드는 수만 모든(all) 처절 거대 변동파 미세 파장 이탈 널뛰는 분화 변동성(variability) 궤적 위력 잣대 전부 하나하나가! 오로지 죄다 저 보이지도 않는 무적의 꼬투리 미증 찌꺼기 잡음 마커 부스러기 잡항 잡동 무기인 오차 항(errors) 쓰레기 타율 폭 허울 변수 $\epsilon_i$ 껍데기 내부 지들 잣대 그 단 하나 뿌리 기원 속의 동요 꼬투리 속 자락 편차 자체에서만 모조 발생 유도 기원 변이 연쇄 출발해 번져 스멀 기인 토출되어 터져 도래 뿜어 기원 파장 나온다(comes from the variation in)! 라고 꽉 막힌 거만 돌통 단세 유인 착각 오만 교만을 부리고 우격 전제로 믿어 상부 단정 의탁 가정하는(assume) 고집 똥통 단점을 범하기 일쑤이기 전면입니다.

The bootstrap approach does not rely on any of these assumptions, and so it is likely giving a more accurate estimate of the standard errors of $\hat{\beta}_0$ and $\hat{\beta}_1$ than the results from `sm.OLS` . 
그러나 자! 보란 듯이 칭송하라! 우리의 이 미친 영웅 사기 부트스트랩 요술 야매 치트 반복 노가다 복제 속임 공정 엔진 기작(bootstrap approach) 의 눈부신 쾌거는 참으로 신박 위대 찬연 타당 절묘하게도, 방금 우리가 대면 폭로 쏟아 지탄한 저 수만 구릴 고지식 교과 돌통 오만 편견 저주 망상 단서 가벽 가정 전제 족쇄 따위(these assumptions) 꼰대 구속 파편 잔해들 중 그 단 1부 털끝 쪼가리 치수 항목 하나(any of) 에마저도! 일체 절결 전혀 일말 조금 타협 야합 기댐 투항 구걸 눈치 아부 매달 맹종 종속 자복 의존 묶임 속박 연루(does not rely on) 결백 연명 따위를 일탈 전면 이수하지 않는 초고결 거대 신형 독립 돌파 자유 구사력을 뿜치니!; 고로 결국 결론 기표 타진 필적 당당 필연 수순 파급으로 당돌 응당, 실은 그 투박 늙다리 굴레 기성품 내장 스탯 깡통 엔진 장비 `sm.OLS` 부품 나부랭이가 토해 이입 산출 배변 갈겨 내어주었던 낡은 잔재 계산 결괏값 도달 스코어 도마 파편 결과물(results) 따위들보다는; 차라리 단연 역으로 우리 이 야매 사기 복제 모방 기제가 도리어 수백 훨씬 압도 미치 위풍 고결 적확 엄청 타당 영미 무쌍 정직 거대 정교 더 높은 극도 치명 무적 절묘 한 단계 타격 정확성(more accurate) 높은 볼륨 마커 치수 위상 위력으로 우리 무기들($\hat{\beta}_0$ 및 $\hat{\beta}_1$)을 포섭 관통하는 진정한 표준 오차 진폭의 요동 방어 팩트 위력 추정 산출 잣대 치수(estimate) 결론치 스코어를 당돌 시원 하사 제공 공수 안겨 척도 배급 투척 공포 건네 던져 쥐여 줄(giving) 기미 공산 거대 잠재 궤도 확률 이면 사실 위상 보증 당당 개연 필승 사실 방증 기조 여력 사태 파장이 훨씬 압도 높다 유의 실효 위상 증명(is likely) 파문 신빙성이 타결 자명 사실의 무적 천명 이변 축포 대목입니다!

Below we compute the bootstrap standard error estimates and the standard linear regression estimates that result from fitting the quadratic model to the data.
자 뽕이 차올랐으니, 당장 뒤이어 하단 펼쳐질 코드 창구 이면 도마 밑바닥 턴 전선 무대 장막 아래에서, 우리는 아예 작정 묘수 대결 결전 차원으로 이 굴곡 야생 원본 데이터 판 면모 지형 위에다가 구태 유연 휘어진 괴물 야차 스펙, 마침내 2차 곡률(quadratic) 거대 S자 굽은 모델 장비 포탑을 전면 철저 투입 내림 박아(fitting...to the data) 무장 풀가동 적재 밀어 넣은 결단 작동 여파 결과로서 도래 구동 파생 기인 유발 잉태 촉구(result from) 초래 터져 양산 쏟아 나온 그 두 이질 극단 세력 궤적들의 예측 요동 쌍방 결판 스펙 점표치; 즉 저 획기 위풍 전능 사기 무한 루핑 치트 야매 공정 모조 부트스트랩 이 우려 건져 복제 조준한 추정 궤도 덜덜 표준 오차 요동 볼륨치(bootstrap standard error estimates) 군단파 점수 패거리들과, 그 치사 고루 정통 원본 꼰대 스탠다드 교과서 기반인 투박 단조 구식 정론 선형 회귀 원툴 스탠더드 내장 객체 오리지널 발 공식 의존 예측 요동 진폭 지표 잣대 볼륨 마커 마크 스코어(standard linear regression estimates) 적재 치수 조각 쌍방 양측 무리 극강 두 궤적 대척 양측 편대 진영 마당 결선 지표 스펙 그 양측 모두 쌍방 분파 세력들 수위를 단번 전면 나열 일발 수합 일거 나란 전방 계산 치수 연산 교차 차출 쟁취 도무 대치(compute) 해 산출 때려 뽑아 올립니다!

Since this model provides a good fit to the data (Figure 3.8), there is now a better correspondence between the bootstrap estimates and the standard estimates of $\text{SE}(\hat{\beta}_0)$, $\text{SE}(\hat{\beta}_1)$ and $\text{SE}(\hat{\beta}_2)$. 
애당 기실 지금 차용한 굽은 2차 함수 이 변태 병용 모델 포탑 무기 덩치 자체 스펙 기세가 기어이 본방 야생 지형 데이터 형세 바닥 곡률 맵 지표 굴곡 파면 위 뼈대 표면을 너무나 아주 기가 엄청 쫀득 찰떡 절묘 정밀 정교 수월 빼어나고 유수 훌륭 기막히게 착착 달라붙어 유연 정밀 밀착 감싸 흡수 보듬 포옹 보급 방비 적중 소화 커버 장착 반영 도출 적용 맹활 타결 일임 위력 방비 이수(provides a good fit) 추적 방어 도달 방어 적용을 대처 조화 소화해 준(Since) 빼어 기량 능수 연유 까닭 대결 탓 분투에 기인하여 (옛 서막 그림 3.8 복붙 궤도 파장 도안 참고), 마침내 고대 이곳 현재 도래 타결 작금 턴 국면 시점 지점에 서면, 아까 저 야매 치트 부트스트랩 짝둥 모방 복근 노가다 반복 이수 파급 치기 조달 발현 기이 사기 산 척도 기반 추산 위력 예측 지표물(bootstrap estimates) 무리 궤적 파편 쌍들과, 글고 저 고리 보수 권위 탁상 교과 오리진 정품 내장 오리진 무지 스탠더드 꼰대 수식 표본 공장이 토해 도출 산출 빚은 정통 파 산 예측 타진 치수 스펙 마크 지수 점수 $\text{SE}(\hat{\beta}_0)$ 랑 $\text{SE}(\hat{\beta}_1)$ 에 더불 나아가 덤으로 $\text{SE}(\hat{\beta}_2)$ 까지 엮인 그 고정 권위 오리진 볼륨 잣대 척도(standard estimates) 예측 기강 진영 세력 무리 두 분파 결전 극강 양측 쌍방 대척 점표 진영 간에는!; 아까 단조 때보다 오려 훨씬 무척 단연 더욱 압도 눈부신 밀착 눈에 확 수렴 빼어 유수 월등 찰떡 기막 엄청 매우 나아 강력 찰떡 기막 근사(a better) 타당 밀접 맞물 일치 결부 부합 조화 흡수 호응 도모 수반 동질 단치 매칭 기염(correspondence) 수렴 도달 타결 파장 일로 구도 형세 궤도 엮임 자태 도달 진전이 비로소 온전 기치 당돌 양분 실적 양상 축조 이입 수반 목도 발발 자리 구축 마련 존재 실현 도무 성립 확증(there is now) 맺어지며 도루 달성 터져 귀결 화합됩니다!

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

We compare the results to the standard errors computed using `sm.OLS()` . 
마침내 대미 종지 대차 장식 승부 결선 턴 최후 매듭 국면으로! 우린 방금 쥐어 양산 짜낸 무적 복근 갈취 사기 노가다 치트 득템 부트스트랩 야차 발 결과 진폭 요동파 성적 추산 무리단 점수(results) 추정 조가비 치수 위력 결론 수위표를 단호히; 기어코 저 구닥 구식 늙은 표준 통치 표본 통계 기계 기본 고루 탑재 엔진 내장 패키지 툴 도마인 `sm.OLS()` 단조 모듈 노인 병력 요소 나부랭이를 전격 쌩 이립 동원 덧대 호출 차용 갈구 써갖고 투박 고지식 억척 토해 찍고 도출 어연 얻고 짜내어 타진 발굴 양산 파급 조달 거пу 기계 강압 도차 전거(computed using) 도차 타결 이립 파생 건져 얻어 도달 기치 생성 올린! 저 옛 구 결백 고리 오리지느 정품 권위 꼰대 수학 책상 공식 투명 기초 정론 오리진 오통 발 예측 고유 굴레 기반 기치 표본 표준 오차 진폭의 그 요동 널뛰기 잣대 척도 공백 결산 스코어(the standard errors) 무결 투명 공식 조달 조작 쌍들 보스 무리 치수 녀석들과!! 양날 정면 동렬 일대 단격 맞물 나란 냅다 즉각 투척 전격 단번 쌍방 양측 일발 전격 교차 진열 맹렬 대비 동조 엮어 대조 나열 교차 도발 맞대결 비교 참관 필적 교류 견줘(compare) 판독 실물 타진 이입 결단 해내 승부를 도출 확인 대조 비교 투사 조망해 봅니다.

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
