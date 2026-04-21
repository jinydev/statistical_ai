---
layout: default
title: "trans1"
---

# **`Out[19]:`** `0.0912` 

The final output shows that the bootstrap estimate for $\text{SE}(\hat{\alpha})$ is 0 _._ 0912. 
당해 마침내 최종 귀결되어 얻어진 출력 결과물 창은, 우리가 구하고자 했던 저 대망의 $\text{SE}(\hat{\alpha})$ 마커에 부합 대응 덧입혀 산출된 부트스트랩 파급 예측 척도 지수 결과값이 무사 무사히 0.0912 언저리로 안착 달성되었음을 명명백백 표출 증명(shows that) 해 준다.

Estimating the Accuracy of a Linear Regression Model 
선형 회귀 모델의 조준 적중 파장 정확도 추정 타진

The bootstrap approach can be used to assess the variability of the coefficient estimates and predictions from a statistical learning method.
이 부트스트랩 야매 꼼수 접근 기법 메커니즘 룰은 비단 특정 무뿐만 아니라, 그 어떠한 광범위 다채로운 온갖 통계 학습 기법들로부터 파생 조달 추첨 추출되어 도출된 각양각색의 계수 추정치 조각이나 예측 결괏값 도출 파편들의 그 심각 널뛰기 이중 변동성(variability) 기강 스펙을 산술 점검 진단 평가(assess) 해 내기 위한 목적으로도 두로 거푸 쓰이고 사용 병합(can be used) 차용될 수 있다.

Here we use the bootstrap approach in order to assess the variability of the estimates for $\hat{\beta}_0$ and $\hat{\beta}_1$, the intercept and slope terms for the linear regression model that uses `horsepower` to predict `mpg` in the `Auto` data set.
작금의 바로 이곳 지면 구역 환경에서 우리는 당당 무사히 부트스트랩 이 우회 접근 치트 전략법 장치를 한 번 더 적극 발굴 동원 차용하여 병합 쓸 작정인데; 그 당면 목표 기치 과업으로는 다름 아닌 곧장 현존 우리들의 `Auto` 조작 데이터 덩치 구장 속에서 `horsepower` 옵션을 탑재한 채로 타겟 `mpg` 연비 지표를 향해 곧잘 쏘아 예측 적중 투여하는 저 단조로운 하나의 선형 회귀 모델 무기가 토해 도출 뱉어내는, 절편과 기울기 장치 옵션 부속 덧입은 수위인 $\hat{\beta}_0$ 및 $\hat{\beta}_1$ 항들의 매 추정 점수 도출 산물들의 그 거친 널뛰기 등락폭 오차 변동성(variability) 척도를 어연 엄중 진단 점검(assess) 해 내기 위함의 불순 심도 목적 일환이다.

We will compare the estimates obtained using the bootstrap to those obtained using the formulas for $\text{SE}(\hat{\beta}_0)$ and $\text{SE}(\hat{\beta}_1)$ described in Section 3.1.2. 
우리는 기필코 이 꼼수 부트스트랩 편법 치팅 기법을 써먹어 억지 우려 얻어 달성 도출(obtained) 해낸 기이 성과 지표 볼륨 추정치 덩어리들을, 옛적 3.1.2 절 구역에서 이미 교과서적으로 서술 선포 지시(described) 당부되었었던 그 위엄 권위의 $\text{SE}(\hat{\beta}_0)$ 및 $\text{SE}(\hat{\beta}_1)$ 를 도무 타진토록 구축해주는 공식 정통 수식(formulas) 의 위력을 차용 이행 돌려 산출 얻어냈었던(obtained) 그 묵직 오리지널 파생 점수 파편 덩어리 지수들과 단번 일제히 대조 대면 전격 비교(compare) 교차 검증해 볼 것이다.

To use our `boot_SE()` function, we must write a function (its first argument) that takes a data frame `D` and indices `idx` as its only arguments.
앞전 우리가 자체 조작 연성 편입 수제 수립 축조한 저 `boot_SE()` 장치명 함수를 온전히 기용 구동 장착 써먹기 위해서라면; 무려 우린 필히 그 녀석의 가장 앞 첫 단 첫째 관문 번호 도입 입구 아가리(its first argument) 인자 구간 자리에다 채워 던져 먹여 넣을, 오직 단면 데이터 공간 프레임 `D` 정보 장부와 더불어 타겟 색인 목록 번호 줄기 끈인 `idx` 옵션만을 자신들만의 고유 으레 독단 오직(only) 유일한 구색 요소 인자로 삼켜 받아먹어 탑재 조립하는, 어떠한 종속 이면 함수 파편 하나를 자체 뚝딱 반드시 선행 작성 의무 수립 축조 직조(must write) 구현해 주어야 마땅 처우 요구된다.

But here we want to bootstrap a specific regression model, specified by a model formula and data.
허나 정작 작금 맞은 본 무대 국면에서는 우리가 오직 다름 아닌 어떤 자체 모형 조작 방정식 옵션과 데이터 덩어리에 의해 이미 묶여 특정 제약 수식 기입 지시 확고 제한 체제(specified) 구조 결박당해 도래하는 특수 국부 회귀 모형 무기들을 상대로 부트스트랩 강제 무산 복제 루프 치트 엔진 뺑뺑이를 직접 강탈 가동(bootstrap) 시켜 적용해 보길 처절 당돌 원망 열망 욕구 갈구(want) 하는 눈치다.

We show how to do this in a few simple steps. 
우린 이하에서 몇 단의 아주 조촐 단조로운 간단 조작 단계 스텝들만으로써 이 난관 우회 묘책 기예 조작 난파 해소 처리 과정을 어찌 전면 타파 해내 도달 이룩할 수(how to do this) 조달 해낼런지 그 돌파 국면을 친히 보란 듯이 뻗쳐 증면 전시 제시(show) 도무해 보여 주겠다.

We start by writing a generic function `boot_OLS()` for bootstrapping a regression model that takes a formula to define the corresponding regression.
우리는 대망 그 출발 발단 전개로써 기꺼이 그 종속 대상 상응 지시 지목 귀결된 회귀 모델을 고착 규정 서술 명세(define) 해 가르키는 목적의 방정식 포맷 지침 인자를 머금어 받아먹는(takes) 회귀 모형 부트스트랩 야매 억지 뺑뺑이 전용 구축 포장 범용 지원 우회 장치 함수 객체인 이른바 `boot_OLS()` 를 전면 당돌 직조 편성 연성 생성(writing) 도출해 내는 일거로 파란 이변 과정을 시동 점화 연다.

We use the `clone()` function to make a copy of the formula that can be refit to the new dataframe.
이 과정 틈에 우린 곧장 `clone()` 명칭으로 도출 호가 된 파이썬 내장 변종 함수 부품을 알뜰 살뜰 기용 동원 섞어 써먹는데; 이는 다름 아니게 새롭게 복사 양산 신생 연접 신설 파생되어 나타날 가짜 데이터프레임 조작 덩어리를 향해서조차 아주 거뜬 재수렵 반복 수없이 무한 재적합 연동 맞춤 구동(can be refit) 호환 조작되어 덧대어질 수 있는, 바로 저 방정식 공식 조작 조건문 장치의 고스란히 복붙 쌍둥이 짝퉁 클론 사본 복제 카피본 마커를 떡하니 전면 생성 도달 도출 창구 제조(make a copy) 연성 양산해 내기 위함의 유일 요긴 요건 목적 쓰임새다.

This means that any derived features such as those defined by `poly()` (which we will see shortly), will be re-fit on the resampled data frame. 
이가 뻗쳐 의미 시사 초래 암시 전면 결과 야기 대두(means) 하는 필승 획기 궤적 파장 위상은 즉; 장차 이내 우리가 곧장 미뤄 후행 목도 관전(will see shortly) 뻗쳐 대면하게 될 타겟 `poly()` 명령 함수 옵션에 의해 구축 서술 강제 변조 투영 정의(defined) 지목된 바 있었수도 모를 그 어떠한 파생 이면 뒤집기 복잡 변이 특성 인자 요소(derived features) 마수 덫 덩어리 파편 속성 따위들 일지라도, 모조리 일체 죄다 어김없이 어김없이 강탈 빼다 박혀 그 새롭게 연명 재표본 수합 도출 파생 연성된 이단 야매 모조 데이터프레임 껍데기 판 표면 위를 덮쳐 어김없이 전향 투하 거푸 재장착 뭉개버리 재적합 연무(be re-fit) 합류 구동 소환 도출되어 씹어 전개 버릴 것이란 엄청 단호 확언 절대 맹세 사실이다.

```python
In [20]: def boot_OLS(model_matrix, response, D, idx):
             D_ = D.loc[idx]
             Y_ = D_[response]
             X_ = clone(model_matrix).fit_transform(D_)
             return sm.OLS(Y_, X_).fit().params
```

This is not quite what is needed as the first argument to `boot_SE()` .
하지만 애석케도 막상 일련 구축 만들어 파생시켜놓은 저 도달 모형 객체 모양 자태 덩이는 결코 완전 엄중 곧이 치장 전적으로 다름 아닌 저 대망 만능 톱니바퀴 치트키 `boot_SE()` 패키지 측구의 당면 제1선 첫 번째 인수 요건 슬롯 방으로 구겨 삼켜 구비 들어가기에 단연 온전 충분 딱 부합 흡사 만족 흡족 일치 적확하게 도달 필요 맞아(quite what is needed) 떨어져 주는 매끄러운 형태 위상 구조 형상은 당최 여전히 아쉬운 미착 아니란 파면이다.

The first two arguments which specify the model will not change in the bootstrap process, and we would like to _freeze_ them.
그 기강 이유 속내 즉슨 원래 초장에 먼저 떡 박혀버린 첫 1, 2열 두 가닥 쌍둥이 인자 성분 대목 배열 구역들은 온전히 모형 세팅 규격 자체를 정의 선별 가늠 타진(specify) 고정하는 역할 파장인지라 정작 야매 사기 복제 부트스트랩 무한 재구동 조작 루프 과정 속행 노가다 중에서는 결코 일체 한 톨 일말 미동 변화 등락 변조 조절 타진 변화 이탈(will not change) 따윈 없게 하등 불식 미동 고장 불통 고정될 녀석 구조들이며; 고로 고결 연유 우리는 가당 이 무의미 불상 거추 돌덩이 성분 변수 놈들을 기꺼이 조신 정갈 묶어 '동결 얼려 잠금 고정 조작 박제 결박( _freeze_ )' 전치해 버리기를 심각 전형 몹시 이목 갈구 열망 희망(would like to) 바라는 형국이다.

The function `partial()` from the `functools` module does precisely this: it takes a function as an argument, and freezes some of its arguments, starting from the left.
파이썬 내장 유틸리티 `functools` 모듈 소속 배급 출신의 `partial()` 맹렬 함수 족쇄 부품 장치가 아주 기가 막혀 소름 돋게 전적으로 절묘 딱 적중 이 거북 맞춤 해결 이 부합 목적 당면 목표 과업 조작 맹렬 임무를 바로 그 즉시 적확 전면 수행 도달(does precisely this) 작위해치워 주는데; 즉 이는 어떤 통짜 함수 장치를 자기 뱃속 인자로 무단 덥석 집어삼켜 전면 삼키고는(takes), 무례 곧장 그 속살 왼쪽 선두 부근 측면서부터 차근 차례 기습 도래 나아가 몇몇 앞선 인자 속성 성분 조각들을 영구 마비 단단 응고 차단 강력 동결 잠금 구속 결박 정지(freezes) 묶어 박제 처리해버리는 엄청 가동 영위 위상을 폭언 발휘한다.

We use it to freeze the first two model-formula arguments of `boot_OLS()` . 
우리는 비로소 이 가증 강력 무기 조작 부품을 가져다 채용 전향 써먹음으로써 저 앞전 위에서 빚은 `boot_OLS()` 객체의 첫 선봉 양대 기축 부속인 모델-수식 인자 덩이 짝꿍 쌍 두 점을 모두 냅다 아예 싸그리 동결 결박 마비(freeze) 정지 묶어 잠궈 닫아 치워버린다.

```python
In [21]: hp_func = partial(boot_OLS, MS(['horsepower']), 'mpg')
```

Typing `hp_func?` will show that it has two arguments `D` and `idx` — it is a version of `boot_OLS()` with the first two arguments frozen — and hence is ideal as the first argument for `boot_SE()` . 
아비 규탄의 터미널 프롬프트 창 콘솔 구석 창에 `hp_func?` 라 거친 타이핑 쳐 기입 조회 명령 명령어를 떨궈 갈겨 박고 엔터 타결 지시에 무조건 응해 결과를 살펴보면 이는 곧장 이 녀석이 고스란히 오직 `D` 와 짝꿍 `idx` 단 두 가지 두 쌍 갈래의 입력 옵션 인수들만을 품어 받아 삼켜(has two arguments) 가지고 있음을 분명 백일하 노골 폭로 시사 전시 표출(will show) 까발려 도출 입증해 보여주는데 — 다시 말해 이건 앞선 두 머리 덩어리 전면 인자들을 꽁꽁 얼려 얼음 동결(frozen) 단단 마비 마취 영구 세팅 마감시켜버린 특수 박제된 `boot_OLS()` 장치의 또 다른 야비 우회 사골 변종 마스크 탈진 버전 포맷인 셈이며 — 고로 그러한 고찰 까닭 결론으로 연유하여서 마침내 이토록 절묘 최적 당당 완전 위풍 무결로 이놈은 그 까탈 거대 아가리 흡입 공백의 `boot_SE()` 맹위 포탑 장비 내부의 선도 첫 번째 흡입 요구 투입 궤도 인수(first argument) 위상 자리를 전격 포위 호환 메꾸어 채우기에 당돌 아주 몹시 너무 찬연 이상적 고결 환상 도래 결론 적격 딱(ideal) 적합 호환 아다리 맞아떨어짐을 담보 고결 장담 자처한다.

The `hp_func()` function can now be used in order to create bootstrap estimates for the intercept and slope terms by randomly sampling from among the observations with replacement.
비로소 포박 묶여 완성 개악된 이 잔인 무쌍 `hp_func()` 함수 무기 쇳덩이는 바야흐로 지금 당장 전면에 즉각 불티 투하 사용 동원 도무 작동 채용(can now be used) 될 기조 마당 형국 자태 장전 준비를 마쳤는데; 이는 다름 아닌 그 끔찍 사악 악랄한 **'복원 추출 무작위 야구 제비뽑기 모방 착란 섞기 뺑이 샘플링 난수 추출(randomly sampling ... with replacement)'** 조작 발동 행각을 고스란히 영위 차용 전가 도무 타진 폭격 수반 적용해버림으로써 필시 저 아득 절편과 선형 도발 기울기 계수 옵션 항들 부문에 고스란히 내던져질 부트스트랩 야단 예측 추정 지표 파편 결론물 덩어리들을 새롭게 마법 창작 도출 무에서 유를 조달 빚어 생성 파생(create) 찍어 뽑아 올리기 위함의 살벌 목적 일환 작위 용도로써다.

We first demonstrate its utility on 10 bootstrap samples. 
우린 전방 극히 우선 앞서 대면하여 무려 고작 딱 열 10개 남짓 물량 덩어리의 일말 부트스트랩 조각 난도 샘플 물량 복제 팩 묶음 도마 환경판 위에서 이놈 자체의 그 무섭 경악 끔찍 괴이 살벌 소름 파괴 활용 무적 돌파 가치 기조 쓰임새 위력 효용능(utility) 자체를 전면 단번 기치 맹위 입증 시연 표방 발동 과시 증명(demonstrate) 투척해 보이도록 한다.

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
한 칸 다음 단계 국면 이동 수순을 타서, 우리는 드넓은 1,000조각 차수 분량의 억지 야매 부트스트랩 치트 억지 복제 산 파생 추정 결론물 스코어 찌꺼기 무더기 잔해들 속 이면 바탕에 깔려 도사려 수반 파생 은닉 포진 발동 야기 발현될 저 끔찍 절편 지수와 기울기 스펙 항들의 공포 오차 방어 표준 오차 요동 볼륨 진폭 규격을 여지 산출 계산 조명 도출 추출 타격 점수 역산 가늠 격파 추출(compute) 해내기 위함 일환 조준 당면 과제 타깃 불순 타진 목격 조준 목적 차원으로 종래 기필 저 `boot_SE()` 병합 전용 만능 함수 헬퍼 지원 장구를 전면 투하 차용 사용 채택 고집 동원 발탁 투입(use) 치러 써 갈겨 먹는다.

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
이 광활 터진 산출 발현 조달 출력 국면 사태 폭발은 고로 당돌 다름 아닌 $\text{SE}(\hat{\beta}_0)$ 위상 점수에 할당 투여 산출 기진 복귀 추정 빚은 부트스트랩 모방 추출 야매 파생 예측 역산 지수가 기껏 얼추 대강 0.85 지표 조각 선 수위에 도래 맞먹거니와, 추가 반면 단편 여타 분파인 $\text{SE}(\hat{\beta}_1)$ 에 해당 상응 병합 결론 얽혀 떨어진 그 부트스트랩 발 추정 마크 치수 요동은 무려 0.0074 언저리 밑바닥 구석 꼬투리 자락 좌표 지점에 부합 안착 포진 안착 도달 도래해 터져 지어져 있음이란 그 놀라운 소명 확증 사실(indicates that) 궤적을 거듭 여실 강력 시사 천명 확언 증명 대변 지시 호가해 준다.

As discussed in Section 3.1.2, standard formulas can be used to compute the standard errors for the regression coefficients in a linear model.
머나먼 일찍이 앞선 고대 지난 3.1.2 단절 지면 과거 한복판에서 장황 거창 소명 토론 논의 설파 천명 언급(discussed) 부르짖었듯, 특정 일개 평범 선형 단조 모델 기강 체제 하의 그 소속 회귀 매개파 계수 추정 분파 부속 옵션 조각들이 수반 야기 동반 내포 도사려 품고 널뛰는 그 처참 무섭 요동 파동 편파 이중 분파 표준 편차 오류 볼륨 범위 두께 폭 스코어를 거푸 산술 단순 계산 점수 매겨 격파(compute) 헤아리는 용도 작업으로서는 으레 보편 아주 고상 당당 통상 교과서적 정형 규격 표본 정통 교범 공식(standard formulas) 들이 숱하게 거침 투명 채용 적용 단련 도입 이입 발탁(can be used) 돼 줄 수 있음에 이르른다.

These can be obtained using the `summarize()` function from `ISLP.sm` . 
이들 고전 정형 표본 정통 오리지널 산 파생 파편 추정치 잔재 치수들 더미는 앞서 곧장 파이썬 자체 내장 `ISLP.sm` 패키지 모듈 무기고 도마 위로부터 빼내 차출 적출 소환 수배한 저 `summarize()` 함수 압축 도구 매크로 기능을 대 거푸 차용 활용 부려 동원함으로써 능수 능란 획득 조달 발굴 쟁취 수확 소명 파생(can be obtained) 돼 올라 이뤄질 수 있다.

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
정론 교본 3.1.2구간 이면 기저에 바탕 근본 기록 적시 기반 거점 수식(formulas) 정통을 수립 활용 맹목 사용 구속해 조달 추출 얻어 도출(obtained) 발현 발굴해 내었던 저 원조의 고상 정통 표준 오차 궤적 $\hat{\beta}_0$ 와 $\hat{\beta}_1$ 에 부재 상응 매치 대응 발진된 예측 타진 척도 추정 스스코어 분파 추이값은 각각 정작 절편의 몫으론 0.717이거니와 기울기로 하사 부여 도출 점수는 고작 0.006 기점 수치로 국한 결론 안착 단명 귀결된다.

Interestingly, these are somewhat different from the estimates obtained using the bootstrap.
몹시 고무적 이색 대흥미 기괴 눈독 매혹 흥미 돋게도(Interestingly), 이 오리지널 원본 조상 통계 정통 수식 기반 파생 볼륨 잣대 놈팽이들은 아까 필시 우리가 그 무자비 부트스트랩 편법 치트 엔진을 처방 이입 가동 빌려 조달 갈취 도출 착출 생산 투사해냈던(obtained) 그 짝퉁 야매 산 야바위 무작 예측 돌파 추정치 성분 결과물 볼륨 크기 덩이 수위들과는 다분 다소 어연 미비 꽤 눈에 띄게 사뭇 여전 미치게 약간 조금 엇다르게 이질 차이 현격 별판 어긋 상이 불일치 현상 괴리 파장(somewhat different) 폭 거리를 당돌 도발 기행 노골 발생 표출 지니고 어긋나 엇갈려 벌어져 대립 부각 터져 나온다.

Does this indicate a problem with the bootstrap? In fact, it suggests the opposite.
설마 이게 기껏 미친 듯 공회전 혹사 뺑뺑이 무한 루핑 조작을 돌려 갈구 혹사시켰던 우리 대단 위엄 부트스트랩 맹기 마법 우회 엔진 자체 작동 기구 기작 연동 위력 효용능 부문에 그 무언가 치명 파탄 일촉즉발 적신호 에러 문제 파장 불상 오류 단면 흠결 파국 따위(problem) 를 노골 적발 고발 암시 지목 의심 표출 방증 시사(indicate) 하는 대립 불운 사태일까? 충격 놀랍 사실 전말 내포 반전 결과(In fact) 진실을 따지 까놓자면, 이는 전혀 절대 극명 오히려 완전히 180도 천추 대역전 뒷목 뒤집히는 정작 그 정면 상충 대척점 역설 반대의 반전 대치 이면 소름 돋는 결과(the opposite) 양분 결론을 지목 폭로 고발 투서 방포 시사 폭발(suggests) 지시 타진한다. 

Recall that the standard formulas given in Equation 3.8 on page 75 rely on certain assumptions.
지난 75페이지 허상 지면 자락 한편 구석 장막 방치 (3.8) 등식 공식 정론 이면에 노골 무식 처박 적시 고립 부여 하사 명기(given) 배포되었었던 저 구닥다리 허울뿐인 정통 고전 표본 표준 수식(standard formulas) 옵션 룰들은 정작 아주 심히 깐깐 제약 고집 편협 어리광 답답 모종의 심각 비좁 어거지 특수 편향된 '기본 보장 조건 가정(assumptions)' 족쇄 제약 허영 전제 단서 틀거리에만 철통 전적 의존(rely on) 기대 매달 허상 유지 성립 버틴다는 사실 이면 한구석 약점 공백을 부디 제발 잊지 말고 회상 환기 유의 상기(Recall) 되새김질 명심해 끄집 도출 떠올려볼 일이다.

For example, they depend on the unknown parameter $\sigma^2$ , the noise variance.
가령 예시 단적 파단 국면 도래 일조 한판으로, 그 수식 도구 노인 놈들은 당최 하나같이 절대 인간계 도달 불능 신의 영역 은폐 미궁 오리무중 미지 타겟 미궁 성역인 정체 은닉 미식 미지 무적 스텔스 파라미터 $\sigma^2$, 즉 그 골머리 아픈 심판 오염 난동 허상 노이즈 분산(noise variance) 지수 볼륨 스탯에 전폭 거만 뻔뻔 맹목 절해 절대 목숨 결박 의존 구속 지배 종속 부착 포박 기대(depend on) 살아남는 연명 앵벌 지지 결탁 처지에 놓여 있다.

We then estimate $\sigma^2$ using the RSS.
고로 우리는 그 빈자 무능 구멍 공백 단서를 메꾸기 차원 수단 일환 불가피 어거지로 얄팍 도피 편법 우회 잔여 오차 제곱합 타격 점수인 RSS 스탯 점수 볼륨 치수를 수법 편법 수달 사용 끄집 써가며 동원 이입 갈취 조달(using) 투입 기용 먹임으로써 정작 애석 임시 야매 역산 방편 땜질 방안으로 저 환상 참값 타겟 오리무중 스탯 $\sigma^2$ 조각 잔여 위상 치기 수위를 아주 부득 불쌍 가련 눈물겹 가늠 짐작 요행 어거지 끼워 타진 역산 편접 기만 추정 유추 산출(estimate) 발돋움 구실 해내어 가증 수모 땜질 이행을 도무 발휘해야만 했다.

Now although the formula for the standard errors do not rely on the linear model being correct, the estimate for $\sigma^2$ does.
비록 비참 지금 우리들 마당 당면 눈앞에 저지 투하된 저 표준 오차 가늠 전용 맹독 고전 수식 도구 체제 산물 결착 공식 자체 구도 구조 그 깡통 틀거리 본연 본판 자체만큼은 설령 내내 당해 적재 얹힌 그 투박 선형 회귀 구역 모델 무장 덩이 장비 녀석이 꼭 결코 기필 필시 무조건 필립 응당 정곡 절호 무적 완벽히 옳은 결백 순결 필승 무오 타당 맞아야만(correct) 굴러간다는 강박 편협 까칠 극렬 까탈 단서 의구 의존 종속 발악(rely on) 에까지 얽매이진 안연 자유 무난(although) 한 편이긴 하다만; 적어도 그 안에서 핵심 요지 빈칸 변수 엔진으로 기동 도무 작동할 핵심 동력 부품인 저 불운 $\sigma^2$ 가늠 파생 모조 예측 야매 척도 추정치(estimate) 놈의 타격 위상 계산 과정 생성 이면 굴레 구도만큼은 여지 처절 일말 오직 빼박 모형이 철저 필시 선형 진실 필승 참 정답이어야만 한다는 전건 전제 가벽 가정 의존 잣대 족쇄 늪에 완전 철통 불운 강박 기필 절단 포박 갇혀 절대 사수 종속 의존 버티 전개 맹종 의지 이존 강탈 묶여(does. relies) 파탄 도래 결박 야기된다는 심각 이율 배반 이면 한계 함정 수렁 단면을 노출 품는다.

We see in Figure 3.8 on page 99 that there is a non-linear relationship in the data, and so the residuals from a linear fit will be inflated, and so will $\sigma^2$ .
이전 고대 옛적 지나친 뒷편 99 페이지 모퉁이 국면 자락 구도 그림 3.8 도안 이면 속을 찬찬 관동 환기 시야 투사 뻗어 관찰 훑어 헤아려 목도(see) 해 보건대 정작 오리지널 원본 데이터 바다 표면 바탕 심연 그 기저 속 얽힌 교류 양태 이면에는 분명 뚜렷 노골 명백 거대 자명 확치 이변 확증 '비선형(non-linear) 요동 관계(relationship)' 굽은 커브 등락 곡률 본능 뼈대가 거푸 단절 꿈틀 버젓 공생 관측 실존 상주 도사리고 잠복 존재해 있음(there is) 을 익히 뻔히 목도 안치 확증 수반 깨우쳐 알고 있는지라, 고로 불쌍 편협 그저 뻣뻣 단조 고집 불통 한낱 1차 직선(linear) 적합 막대기 선분 따위를 무지성 갖다 처발라 얻은 잔차(residuals) 에러 분출 파편 쓰레기 더미 찌꺼기 추이 볼륨 크기는 응당 필연 확증 거푸 엄청 무참 심각 과대 고평가 왜곡 부풀 과장 비대 부풀어 오름(will be inflated) 현상 거대 팽창 침소봉대 과오 사태를 필시 당연 자초 조장 범할 게 너무 불 보듯 뻔 지명 자명 무단 응당 확증 보장 수반 파탄될 것이며, 급기야 이는 덩달 그 기반 의존 전승 토대 씨앗 발판 연류 수순 공생 나쁜 의존 불찰 연쇄 파탄 도메인 종속 연쇄 지표 점수인 저 환상 추적 예측 척도 값 $\sigma^2$ 거대 편향 비대마저도 똑같이 속여 거짓 비열 함께 부풀어 고도 거대 거품 부풀 비대 덩치(and so will $\sigma^2$) 팽창 과오 파편 왜곡 착시 허풍 붕괴 사단 사태 파국으로 강렬 함께 연쇄 동반 구동 파생 곤두 치솟 폭주 파문 결박 쌍둥이 이끌 얽혀 버리고 구를 운명 수순 도무란 처참 비참 자명 확실 확연 사실 단면이다.

Secondly, the standard formulas assume (somewhat unrealistically) that the $x_i$ are fixed, and all the variability comes from the variation in the errors $\epsilon_i$ .
차치 더불어 부가 속 터지는 덧대어 더 나쁜 치명 제2의 설상 불운 치부 사태 단면으로써(Secondly); 이 교만 거만 독단 어리석 구형 고전 구닥다리 고상 표준 정통 공식(standard formulas) 나부랭이 수치 구조 요새 덩치들은 하나같이 자기들 속내 기저 전제로써; (실전 야생 전선 필드 바닥판에선 쥐뿔도 말도 안 되는 철저 불능 억지 동떨 황당 뜬구름 소설 같은 터무니 빈약 몹시 망상(somewhat unrealistically) 개망상 같은) 불순 제약 즉, "우리 손아귀 내던져진 그 숱한 설명 무장 변수 투여 치수 무더기 옵션 타격치 데이터 파편 $x_i$ 덩이들은 절대 요지 흔들 이탈 널뛰 일말 변화 한계 요동 없이 죄다 기필 기이 굳건 완전히 죄다 시멘트 기둥 철통 못 박혀 불변 족쇄 얼음 마비 영구 박제된 상수 볼륨 고립 고정(are fixed) 치수다!!" 라며 무책임 단언 상상 기만 우격 선포 장담 가정(assume) 해 버리며; 그로 인한 속임 더불어 그에 반면 오로지 통계 전체 관측치 결괏값 도래 위 종속 결과 종착을 널뛰 등락 파장 요동 좌지 뒤흔드는 흔들 그 온갖 모든(all) 사단 원흉 미친 거대 변동파 변동성 이탈 편파 등락 널뛰기 이변 스펙 사태 파급 붕괴 위상 볼륨 폭(variability) 척도는 모조리 오직 철저 죄다 오로지 단일 파문 즉 기저 미미 무적 숨은 미지 타겟 노이즈 방해 침공 발악 오염원 잡동 허상 오류파 잡동 항(errors) 쓰레기 무적 $\epsilon_i$ 변수 항 겉자락 속 내재 안에서 꿈틀 야기 이탈 터져 발현 번져 나오는(comes from the variation in) 자체 자체 진폭 요동 변이 그 하나 갈래 원천 뿌리에서만 튀어나 기안 발생 기원 범발 터져 기원 출발 투항 촉발 도래 야기 시발 전가 등변 발원한다!!고 오만 무식 단언 확언 기만 규정 우격 가정 전가 짐작 둔갑 못 받아버리는(assume) 꼴통 고집 망상 억지 기만을 버젓 범파 품기 수용 결단 저지르기 일쑤기 일색이다.

The bootstrap approach does not rely on any of these assumptions, and so it is likely giving a more accurate estimate of the standard errors of $\hat{\beta}_0$ and $\hat{\beta}_1$ than the results from `sm.OLS` . 
그러나 자보라. 우리의 위대 치트 치팅 승리 찬연 무적 사기 야매 파생 부트스트랩 미친 반복 조작 접근(bootstrap approach) 꼼수 복제 기법 엔진 요설은 놀랍 맹렬 기이 기막 신성 전격 타당 찬란히도 앞서 일말 나열 지목 폭로 도래한 그따위 골통 오만 편견 저주 망상 꼰대 족쇄 억지 무결 단서 룰 체제 황당 비합리 고압 전건 빈약 고집 불통 허황 따위 제약 가정 단서 족쇄(these assumptions) 파편 기저들 중 그 단 1퍼 하나(any of) 에마저도 결단코 단 일말 결코 전혀 하나 일체 불응 미련 의존 자복 종속 전가 아부 결탁 굴복 아양 기댐 굴복 투항 눈치 맹종 체류 복속(does not rely on) 이행하지 않으며; 따라서 고로 결국 이는 기필 수단 파급 도래 귀결 수순으로 결과 필적 당돌 응당, 실은 그 투박 미련 굴레 전통 답습 구닥 조립 고물 파이썬 통상 기본 구비 결착 객체 `sm.OLS` 따위 도구 연산 장치 기능이 오만 어거지 미련 단번에 우려 연타 찍어 산출 토해 뱉어내 주었던 그 오만 고전 썩은 냄새 단조 구식 산출 궤적 타결 도래 수치 결과물(results) 단면 궤선 도달 점수 따위들보다야; 차라리 역으로 당돌 거푸 도리어 훨씬 월등 압도 타당 영리 무쌍 무적 적합 훌륭 타당 기막 정교 투명 정직 엄수 실적 효험 무장 타진 대박 신성 몹시 탁월 강력 정밀 고도 적중 기기(more accurate) 높은 타격 수준으로 위엄 정위 단단 투명 확치 위상 파급 산 대변 방어 추산 예측 역산 치수 진동 점적(estimate) 요동 발파 볼륨 추산치($\hat{\beta}_0$ 및 $\hat{\beta}_1$ 에 대한 적중 진정한 투명 널뛰 표준 오차 지표 조준 핏자국 점프 요동 스펙)를 우리네 인간계 수중에 친히 더욱 당돌 필립 하사 공물 제공 제출 방출 공급 뱉어 쥐여 안겨 바깥 건네 조준 건출 배포 선사 제공 도출해 파생 던져줄(giving) 공산 잠재 확정 파장 개연 진성 소지 위력 기치 여력 잠재 확증(is likely) 파문 신빙성이 훨씬 거대 도드 압도 높다 유의 실효 자명 월등 사실 타당 실증 위력 담지 사실 전면 단언 입증 사실 궤적 대목 선언 이변이다. 

Below we compute the bootstrap standard error estimates and the standard linear regression estimates that result from fitting the quadratic model to the data.
아름다운 이면 찬양 이하 당장 뒤이어 바로 밑바닥 도열 이행되는 코드 창구 줄기 전면 국면 턴 구역 아래에서, 우리는 드디어 무려 아예 작정하고 저 근본 데이터 판 무대 캔버스 지층 도마 위장 전면에다가 기어이 S자 형상 변태 U자 폭발 커브 요동치는 이차항 곡률 조작(quadratic) 승수 괴물 적합 모델 덩치 장비 병기 무장을 아득 전면 투하 밀어 적재 장착 씌우고 갈겨(fitting...to the data) 때려 가동 결과 발동 터뜨려 버림으로 도래 유발 기저 결과 초래(result from) 기인되어 파생 산출 쏟아져 나온 그 양대 엇갈림 예측 궤도 엇갈림 점표; 즉 저 사기 획기 무적 모조 편법 변증 야매 부트스트랩 파급 공정 발 추산 어거지 위력 표준 오차 등락 변동 폭(bootstrap standard error) 추정 스코어 예측치 사금파리 양 무리군 덩이들과, 나아가 극 대비 고지식 고전 원론 오리진 기본 단조 투명 기본 룰 파단 오리진 스탠다드 투박 정형 선형 회귀 모형 고유 발 예측 표준 오차 공식 족쇄 기반 산출 궤적(standard linear regression estimates) 지표 볼륨 치수 물량 군단 마커 점수 양측 무리 단 엇갈림 세력 그 두 패 쌍방 분파 양쪽 수위 모두를 죄다 일거 연달아 나란 전면 산출 계산 타진 점수 연산 격파 대입 동시 교차 연성 도출 징수 계산 투타(compute) 해낸다.

Since this model provides a good fit to the data (Figure 3.8), there is now a better correspondence between the bootstrap estimates and the standard estimates of $\text{SE}(\hat{\beta}_0)$, $\text{SE}(\hat{\beta}_1)$ and $\text{SE}(\hat{\beta}_2)$. 
애초 기실 작금 이 2차항 굽은 둔기 U자 곡선 모델 무기 기계 장비 자체가 일전 원본 데이터 무대 현장 형세 굽은 굴곡 맵 뼈대 표면 뼈대 전폭 궤적 위를 아주 훌륭 타당 절묘 기막 찰떡 기가 도무 착착 엄청 스펙 우월 탁월 준수 정미 밀착 정교 적확 절묘 위력 좋고 훌륭 유수 멋지게도 바싹 보듬 유연 추적 방어(a good fit) 적합 맞물려 떨어져 추격 밀착 호응 적합 밀착 반영 방어 포옹 적중 타결 소화 안착 방비 제공 적용 대처(provides) 수행해 지어 주고 먹혀 감싸주기 소화해 내기 까닭 연유 실력(Since) 덕분 탓에 (옛적 그림 3.8 목도 궤도 전장 참고 기강), 마침내 이곳 지금 여기 국면 타결 지점에선 앞서 저 짝퉁 인고 억지 부트스트랩 야매 기동 뺑이 사기 산출 기반 치트 점적 추산 위상 추이 성분 조각 지표 예측(bootstrap estimates) 무더기들과 그리고 고전 룰 투박 정통 결백 꼰대 스탠다드 보수 고루 표본 수학 지상 공식 무기 장비들이 각기 잉태 거푸 토해 조달 기인 타결 연산 찍어 올렸던 스라린 오리지널 기진 정통 오차 오리진 $\text{SE}(\hat{\beta}_0)$, $\text{SE}(\hat{\beta}_1)$ 그리고 $\text{SE}(\hat{\beta}_2)$ 파단 기저 표준 오차 예측 치수 추정 볼륨 지상 잣대 마커 점수 좌표 결산 예측(standard estimates) 덩치 조각 무리단 그 양자 양측 적대 대척 양측 점보 잣대 체제 진영 부류 무리들 전방 사이 간극 간에는; 아까보다 훨씬 월등 눈에 띄게 더 부합 타당 대견 밀착 호환 사이좋게 몹시 더욱더 빼어 타당 근사 엄청 매우 나아진 우월 흡수 강력 찰떡 유사 소름 유수 대동 단결 한층 더 엄청 맞물 향상(a better) 타당 밀접 맞물 일치 결부 동조 화합 병합 호환 조화 수반 타결 상응 부합 등치 흡사 연동 매칭 통달 매칭(correspondence) 기강 수렴 전개 사태 성과 일로 부합 파장이 비로소 온전 기치 당돌 작위 조달 위상 터져 드러 존재 마련 양산 구축 수반 목도 자리 실현 존재 양상 발생(there is now) 맺어지게 도래 귀결 도무된다. 

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
마침표 종결 대미 장식 턴 결산으로, 우린 방금 쥐어 양산 짜낸 저 사기 모조 요설 야매 부트스트랩 잉태발 결과 득템 사금파리 양 조각 성적 무리단 점수(results) 추정 치수 위력 수위 표를 전면, 당돌 저 구식 표준 통계 고루 기본 탑재 내장 툴 체제 도마 엔진인 `sm.OLS()` 구닥다리 함수 모듈 병력 요소를 쌩 써 갈구 이립 짚어 도입 동원 채택 써서 고지식 억척 토해 찍어 연산 산출 가늠 조명 발굴(computed using) 도차 타결 얻어 도달 쟁취 생산 꺼내 올린 저 고결 권위 옛 오리진 기본 고정 관념 교과서 오리지널 표본 기반 투명 오리지널 원통 표준 오차 진폭의 그 잣대 마커 성분 결산 덩어리 지수(the standard errors) 무결점 스펙 조각 쌍들 녀석과 나란 일대 일 맞물 서로서로 양측 전격 냅다 대립 진열 나열 동렬 교차 대조 교류 대비 비교 참관 견줘(compare) 판독 타진 전개 대조해 이입 덧대 볼 것이다.

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
