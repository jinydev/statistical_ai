---
layout: default
title: "trans1"
---

# 5.2 The Bootstrap 
# 5.2 부트스트랩

The _bootstrap_ is a widely applicable and extremely powerful statistical tool that can be used to quantify the uncertainty associated with a given estimator or statistical learning method.
_부트스트랩(bootstrap)_ 은 주어진 추정량이나 특정한 통계적 학습 방법에 수반되는 불확실성(uncertainty)을 정량화하는 데 이바지할 수 있는, 매우 널리 적용 가능하고 극도로 강력한 힘을 지닌 통계적 도구이다.

As a simple example, the bootstrap can be used to estimate the standard errors of the coefficients from a linear regression fit.
간단한 예로, 우리는 이 부트스트랩 장치를 선형 회귀 적합 라인으로부터 도출된 회귀 계수들의 표준 오차(standard errors)를 추정해 내는 추산 작업에 접목시켜 사용할 수 있다.

In the specific case of linear regression, this is not particularly useful, since we saw in Chapter 3 that standard statistical software such as `R` outputs such standard errors automatically.
물론 선형 회귀라는 이 특별 무대의 경우라면 이는 그다지 실용적으로 유용하진 않은데, 왜냐하면 앞선 3장에서 우리가 똑똑히 목도했듯이 `R`과 같은 보편적인 표준 통계 소프트웨어들은 알아서 자동으로 저러한 표준 오차들을 손쉽게 뱉어내 주었기 때문이다.

However, the power of the bootstrap lies in the fact that it can be easily applied to a wide range of statistical learning methods, including some for which a measure of variability is otherwise difficult to obtain and is not automatically output by statistical software. 
그럼에도 불굴하고 부트스트랩의 진정한 막강한 저력은, 여타의 다른 방식으로는 그 변동성 척도를 도통 얻어내기 몹시 난해하거나 혹은 여타 통계 소프트웨어들에서조차 결코 자동으로 출력해 주지 않는 까다로운 일부 기법들을 포함하여, 아주 무수히 광범위한 다채로운 통계 학습 방법론 전반에 이 부트스트랩 방식이 너무나도 손쉽게 응용 적용될 수 있다는 그 범용적 사실에서 뿜어져 나온다.

In this section we illustrate the bootstrap on a toy example in which we wish to determine the best investment allocation under a simple model.
이번 절에서 우리는 어떤 한 단순한 모델 환경 하에서 최적의 최고의 투자 수익 배분(investment allocation) 을 결정하고자 시도하는 하나의 작은 토이(장난감) 예제 가상 시나리오 위에서 부트스트랩이 어떻게 활용되는지 시연해 볼 것이다.

In Section 5.3 we explore the use of the bootstrap to assess the variability associated with the regression coefficients in a linear model fit. 
이후 이어지는 5.3 절의 랩 실습 환경에서는, 선형 모델 적합상에서 회귀 계수들과 결부되어 발생하는 변동성(variability) 지표를 엄밀히 진단 평가하기 위해 부트스트랩의 실사용 케이스를 몸소 깊이 탐구할 예정이다.

Suppose that we wish to invest a fixed sum of money in two financial assets that yield returns of _X_ and _Y_ , respectively, where _X_ and _Y_ are random quantities.
우리가 각기 미지의 불확실성 수익을 방출하는 두 가지 금융 자산 부문에 투자를 갈망하며, 이 자산들은 각각 성분 _X_ 와 _Y_ 라는 무작위 양(random quantities) 의 불규칙 수익금(returns) 들을 낳는다고 한번 가정해 보자.

We will invest a fraction _α_ of our money in _X_ , and will invest the remaining 1 _− α_ in _Y_ .
우리는 가진 전체 투자금 중 오직 파생 부분 조각 _α_ 만큼의 지분 비율만을 _X_ 자산 부분에 투자 편성해 할당할 것이고, 그리고 당연히 남게 되는 잔여 자본 1 _− α_ 몫 덩어리는 모조리 _Y_ 자본에 거듭 투자할 것이다.

Since there is variability associated with the returns on these two assets, we wish to choose _α_ to minimize the total risk, or variance, of our investment.
이 막무가내의 두 금융 자산이 벌어다 주는 투자 수익 여건 자체에 이미 극심한 변동성이 결부 연루되어 있기 때문에, 우리는 응당 우리의 전체 투자 자본의 총체적 위험(total risk), 즉 그 무서운 분산(variance) 지표 자체를 극저로 무작정 최소화시키기 위해 가급적 최적의 _α_ 비율을 택하고 선택하길 간절히 소망한다.

In other words, we want to minimize Var( _αX_ + (1 _− α_ ) _Y_ ).
기실 다른 정제된 수식어 표현으로써 치환하자면, 우리는 즉 수식 $\text{Var}(\alpha X + (1 - \alpha)Y)$ 을 최소화하길 갈구하는 셈이다.

One can show that the value that minimizes the risk is given by 
누군가는 그 위협 위험도를 극저 수준으로 감소시키는 바로 그 꿈결의 비율 수치 좌표값이 아래와 같이 주어짐을 능히 산술적으로 증명 도출해 보일 수 있다:

$$
\alpha = \frac{\sigma_Y^2 - \sigma_{XY}}{\sigma_X^2 + \sigma_Y^2 - 2 \sigma_{XY}} \quad (5.6)
$$

where $\sigma_X^2 = \text{Var}(X)$, $\sigma_Y^2 = \text{Var}(Y)$, and $\sigma_{XY} = \text{Cov}(X, Y)$.
이 수식 맥락 한편에서 $\sigma_X^2 = \text{Var}(X)$ 이며, $\sigma_Y^2 = \text{Var}(Y)$ 이고, 또한 교차 항 $\sigma_{XY} = \text{Cov}(X, Y)$ 임을 지칭 관통한다.

In reality, the quantities $\sigma_X^2$, $\sigma_Y^2$, and $\sigma_{XY}$ are unknown.
실무 필드 현실 세계에서는 기실 저런 신의 참값 지표 양 성분들인 $\sigma_X^2$, $\sigma_Y^2$, 그리고 교차분산 척도인 $\sigma_{XY}$ 등은 도통 모조리 미지의 영역 뒤에 철저히 베일에 가려 알려지지 않고 은폐되어 있다.

We can compute estimates for these quantities, $\hat{\sigma}_X^2$, $\hat{\sigma}_Y^2$, and $\hat{\sigma}_{XY}$, using a data set that contains past measurements for _X_ and _Y_ .
하지만 우리는 _X_ 와 _Y_ 수익에 대한 과거의 오랜 측정 궤적 수치 기록물들을 담고 있는 과거 역사 데이터 세트를 직접 차용 이용함으로써; 정작 저들의 추정치 값 부스러기들인 $\hat{\sigma}_X^2$, $\hat{\sigma}_Y^2$, 그리고 결합 $\hat{\sigma}_{XY}$ 추정 수치들을 조각조각 직접 산술 추정 연산해 낼 순 있다.

We can then estimate the value of _α_ that minimizes the variance of our investment using 
그러면 이후 우리는 이들을 토대로 우리 총자본 투자의 그 널뛰는 분산 에러 파장을 최소 바닥으로 끌어내려 안착시켜 줄 꿈의 적정 최적 비율 _α_ 추정 값을 다음과 같이 구성해 연산 추정해 낼 수 있게 된다:

$$
\hat{\alpha} = \frac{\hat{\sigma}_Y^2 - \hat{\sigma}_{XY}}{\hat{\sigma}_X^2 + \hat{\sigma}_Y^2 - 2 \hat{\sigma}_{XY}} \quad (5.7)
$$

Figure 5.9 illustrates this approach for estimating _α_ on a simulated data set.
마련된 그림 5.9 지면은 조립된 모조 시뮬레이션 데이터 세트 환경 위에서 바로 이 투입 비율 _α_ 값을 이렇듯 추정 산출해 내고자 시도하는 해당 접근법 방식 맥락을 도해 시연해 설명해 준다.

In each panel, we simulated 100 pairs of returns for the investments _X_ and _Y_ .
열거된 각각의 매 패널 국면 내에서, 우리는 투자 자산 _X_ 와 _Y_ 각개에서 터져 나오는 도합 100조 쌍의 수익 산출 결과 기록들을 새롭게 인위적으로 생성 시뮬레이션 산출해 냈다.

We used these returns to estimate $\hat{\sigma}_X^2$, $\hat{\sigma}_Y^2$, and $\hat{\sigma}_{XY}$, which we then substituted into (5.7) in order to obtain estimates for _α_ .
우리는 이 새 가상의 수익 결괏값 조각들을 동원 밀집시켜 분산 척도 $\hat{\sigma}_X^2$, $\hat{\sigma}_Y^2$, 그리고 합산 $\hat{\sigma}_{XY}$ 교차 추정 수치들을 가늠해 냈고; 이후 필시 이 도출값 파편들을 위 (5.7) 단번 식 공식에 모조리 직접 치환 대입함으로써 종래 타겟 _α_ 에 대한 최적의 예측 추정치 지표를 이룩해 얻어냈다.

The value of $\hat{\alpha}$ resulting from each simulated data set ranges from 0 _._ 532 to 0 _._ 657. 
그 구동 차수마다 각기 다르게 조립 배급된 모의 데이터 세트 시뮬레이션들로부터 번번이 다르게 파생 도달 안착된 $\hat{\alpha}$ 결과 궤적 수치들은 대략 최소한 0.532 부근에서부터 최대 0.657 범위 부근 언저리에 이르기까지 소소하게 등락 파장을 오가며 범위 수위를 장악한다.

It is natural to wish to quantify the accuracy of our estimate of $\hat{\alpha}$.
이즈음 해서 필연 우리가 방금 연마해 파생해 낸 이 고유의 애지중지한 추정치 $\hat{\alpha}$ 척도 값이 대체 얼마나 정밀하고 고도 정확한지 그 적중 적중률 정확도를 실질적으로 손수 측정 정량화해 가늠해 보길 갈구 소망하는 것은 인간의 지극히 당연무구한 본성 성질 자연스러운 염원이다.

To estimate the standard deviation of $\hat{\alpha}$, we repeated the process of simulating 100 paired observations of _X_ and _Y_ , and estimating _α_ using (5.7), 1,000 times.
우리의 저 추정치 $\hat{\alpha}$ 에 들러붙은 예측 표준 편차 널뛰기 수위 위력을 짐작 가늠해 내기 위하여, 우리는 무려 _X_ 와 _Y_ 가 한 데 얽힌 100쌍의 조각 관측치 덩어리를 그득히 다시 재차 반복 생성 시뮬레이션하고 다시 (5.7) 수식 잣대를 갖다 대어 거푸 _α_ 수위를 산술 가늠해 추정해 내는 이 막노동 과정을 기어코 무자비하게 1,000차례나 노가다 조작 수행 뻉뺑이 인위 거듭 반복해 내었다.

We thereby obtained 1,000 estimates for _α_ , which we can call $\hat{\alpha}_1, \hat{\alpha}_2, \ldots, \hat{\alpha}_{1000}$.
그 미친 대가로 인해 우리는 이윽고 종내 수확 부산물로 _α_ 를 겨냥한 무려 1,000개 분량의 육중한 추정치 파편 덩어리들을 모조리 획득 손에 수중에 거머쥐게 되었고, 우린 이 막대한 무리를 감히 $\hat{\alpha}_1, \hat{\alpha}_2, \ldots, \hat{\alpha}_{1000}$ 로 줄이어 거듭 호명해 칭할 수 있다.

The left-hand panel of Figure 5.10 displays a histogram of the resulting estimates.
그림 5.10 전경의 기점 좌측 패널 구역 도마 위는, 결실로 도출 수확된 이들 추정치 파편 무더기들의 전체 밀집 뭉텅이 궤적 수위를 산 모양 히스토그램 형태로 수놓아 덤덤히 그려 표기 진열해 보여준다.

For these simulations the parameters were set to $\sigma_X^2 = 1, \sigma_Y^2 = 1.25$, and $\sigma_{XY} = 0.5$, and so we know that the true value of _α_ is 0 _._ 6.
사실 이 일련의 시뮬레이션 작위 무대 장치를 돌리기 전에 우린 저 기저 백그라운드 파라미터 조작 변수 스탯 값들을 미리 절대자처럼 $\sigma_X^2 = 1, \sigma_Y^2 = 1.25$, 그리고 짝수 $\sigma_{XY} = 0.5$ 라고 조물주처럼 인위 세팅해 두었기에; 고로 우리는 정작 우리가 캐내려 했던 바로 저 기저 속 참된 진성의 진심 순수 오리지널 비율치 _α_ 정답 수치가 다름 아닌 곧장 0.6 언저리에 못 박혀 성립함을 익히 내막을 이미 훤히 알고 있다.

We indicated this value using a solid vertical line on the histogram. 
우리는 이렇게 밝혀진 기막힌 정답 수치 지표선을 정작 저 산 모양 히스토그램 전경 위에 단단한 흑백 세로 내림 실선을 박아 내리꽂아 가리키며 진열 지시해 두었다.

![Figure 5.9](./img/5_9.png)

**FIGURE 5.9.** _Each panel displays_ 100 _simulated returns for investments X and Y . From left to right and top to bottom, the resulting estimates for α are_ 0 _._ 576 _,_ 0 _._ 532 _,_ 0 _._ 657 _, and_ 0 _._ 651 _._ 
**FIGURE 5.9.** _각 낱장 패널 구역 스팟들은 자본 투자 대상 부문 X와 Y들을 상대로 무수히 반복 가열 시뮬레이션 산출해 낸 100쌍 궤도 수익 점포 결괏값 수익 조각들을 전시해 보여준다. 좌측 면 상단 모서리로부터 출발해 우측으로 전개하여 그리고 마침내 바닥 하단 패널 기점 국면으로 나열되는 순서대로, 각기 도출 파생 안착 도래된 α 투입 비율 몫에 상응하는 추정 도출 결괏값 수위 수치들은 제각각_ 0.576 _,_ 0.532 _,_ 0.657 _, 그리고 조심스레_ 0.651 _에 달한다._

The mean over all 1,000 estimates for _α_ is 
아까 얻어낸 무려 1,000개 수효에 육박하는 저 막대한 _α_ 추정 조각 무더기 사금파리 양들을 몽땅 집결해 모두 뭉뚱그려 합산 덧입혀 계산한 평균 쏠림 좌표 수치는 바로 

$$
\bar{\alpha} = \frac{1}{1000} \sum_{r=1}^{1000} \hat{\alpha}_r = 0.5996
$$

very close to _α_ = 0 _._ 6, and the standard deviation of the estimates is 
기적적이게도 찐 참값 정답인 원조 미지의 푯대 _α_ = 0.6 자리에 몹시 초근접하게 바짝 붙어 다가가 도래 다다르며, 아울러 그 추정 파편 무더기들의 오합지졸 분산도를 헤아린 그 표준 편차 성적치는 도합 도출값이 

$$
\sqrt{\frac{1}{1000 - 1} \sum_{r=1}^{1000} (\hat{\alpha}_r - \bar{\alpha})^2 } = 0.083
$$

This gives us a very good idea of the accuracy of $\hat{\alpha}$: $\text{SE}(\hat{\alpha}) \approx 0.083$.
이 산출 궤적 지표는 우리 인간들에게 돌연 우리의 피 묻은 무기 조작 $\hat{\alpha}$ 예측 수립 추정치 결과물의 적중 정확도 위력에 대한 무척 빼어난 통찰 짐작 직관 힌트를 하사한다: 바로 $\text{SE}(\hat{\alpha}) \approx 0.083$ 이다.

So roughly speaking, for a random sample from the population, we would expect $\hat{\alpha}$ to differ from _α_ by approximately 0 _._ 08, on average.
이를 다소 대략 거칠게 둥글게 풀어 시사해 보자면; 모집단의 드넓은 항아리 속에서 임의로 꺼내든 무작위 표본 조각 덩어리를 가지고 추정해 낼 적에조차, 우리는 최소한 우리가 예측 산별해 낸 조작 추정 수치 $\hat{\alpha}$ 위력이 실제 감춰진 정답 푯대 위엄 진성 치수 _α_ 볼륨과 엇갈려 차이 나는 수준의 갭 차이가 평균적으로 고작 대략 약 0.08의 미미한 안팎 보폭 위력 수치 범위 안에 머물며 그리 멀지 않게 부합 떨어질 것임음을 쉬이 장담 보장 믿고 충분히 기대 예상(expect) 예진해 볼 수 있게 된다.

In practice, however, the procedure for estimating $\text{SE}(\hat{\alpha})$ outlined above cannot be applied, because for real data we cannot generate new samples from the original population.
하지만 그러나 매정한 필드 현업 실무 세계 속 전선에서는, 바로 이렇듯 우리가 위에서 감히 오만하게 신의 시점인 양 흉내 내며 그럴싸하게 설명 개요를 늘어놓았던 $\text{SE}(\hat{\alpha})$ 를 추정 조명해 내던 바로 저 호화 작위 훈련 절차 방법론 메커니즘 따위는 애석하게도 도통 전적으로 실전에서는 결코 하등 일체 응용되거나 당최 써먹힐 적용(applied) 될 방도가 만무한데; 왜냐하면 야생의 진짜 참된 진정한 리얼 실전 데이터 구장 무대 위에서는 정작 절대 우리가 신비로운 원본 뿌리 모집단 원천 저수지 속으로 감히 멋대로 다시 함부로 손을 집어넣어 새로운 분량의 양질 관측치 표본 물량 채취 덩어리들을 반복해서 끝없이 공짜 무한 창출 조작 생성(generate) 반복해 낼 마법 같은 기적이 현실 상 불가능하고 실현될 일이 턱없이 없기 일쑤이기 때문이다.

However, the bootstrap approach allows us to use a computer to emulate the process of obtaining new sample sets, so that we can estimate the variability of $\hat{\alpha}$ without generating additional samples.
하지만 그렇다 하더라도 부트스트랩이라는 이 막강한 구원 접근법 치트 방안은 급기야 우리가 바보 상자 컴퓨터 깡통 기계 연산력의 위력을 무지막지하게 혹사 대거 차용 빌려 씀으로써 마치 "새로운 미지의 표본 조각 세트 군단들을 무수히 새롭게 얻어내는 신비로운 창출 과정 파장"의 짓거리를 컴퓨터 안에서 가상으로 흉내 내고 복제 에뮬레이션(emulate) 도무 돌릴 수 있게 만들어 영험하게 허락해주며; 그 엄청난 속임수 기만 은총 치트 덕분에 우리는 정작 단 일말의 진짜 덧붙인 추가 데이터 산출물 파편 조각들을 단 하나도 바깥 모래판 진짜 구장에서 새롭게 구걸 소환 생성 확보 발굴해 얻어내지 아니하고도(without generating) 무려 우리의 그 소중 적합 추정 산물 무기 지수 $\hat{\alpha}$ 가 지닌 변동성 변이 수효를 은밀히 재빠르게 능수능란 손쉽게 계산 추정 산술 가늠해 낼 수 있게 돕는다. 

Rather than repeatedly obtaining independent data sets from the population, we instead obtain distinct data sets by repeatedly sampling observations _from the original data set_ . 
정리하자면 절대자 모집단을 향해 애타게 구걸하며 독립적인 수렴 데이터 뭉텅이 조각 세트를 귀찮게 거듭 창출 번번이 계속 얻어내는 그딴 무용 조작 방식 작태 대신에, 우린 오히려 그저 고작 우리 손아귀에 당장 쥐어진 고스란히 단 하나의 쥐꼬리만 한 초라한 _원본 실전 기초 데이터 세트 표본 단무지_ 안에서조차 연신 번번이 관측지 표본을 스스로 무한정 반복 재추출(repeatedly sampling) 가동 뽑아내기 변태 흉내 막노동을 돌림으로써, 겉보기에 제각기 몹시 무척 상이하게 다르게 분할된 듯한 독립 모조 신생 위장 무작위 분해 착각 데이터 세트 파편 군단 복제 덩이 무리를 수두룩 빽빽하게 자체 생성 자가 창출 도출 영위 획득해 내는 기법이다.

This approach is illustrated in Figure 5.11 on a simple data set, which we call _Z_ , that contains only _n_ = 3 observations.
이 변태 꼼수 복제 기만 조작 접근법 행보는 당장 오직 가여운 단 고작 $n=3$ 인원수 분량의 미더덕 관측치 조각 부스러기만을 딸랑 옹색히 보유 포함하고 있는 극도로 심플 초라 앙상한, 그래서 차마 우린 이를 그저 가벼이 _Z_ 표본이라 대충 호명 지칭하기로 한 어떤 아주 극히 작은 미니 데이터 무대 세트판 위에서 어떻게 얌체처럼 작동하는지 바로 저 그림 5.11 지면 도안 도해를 통해 소상히 시연되어 묘사 타진된다.

We randomly select _n_ observations from the data set in order to produce a bootstrap data set, $Z^{*1}$.
우리는 기어이 하나의 인위 복제 돌연변이 부트스트랩 모방 파편 데이터 세트 뭉치인 $Z^{*1}$ 이라는 변종 결과물을 짐짓 조립 창조 발굴해 생산해 내기 위함의 불순 목적 차원으로 말미암아, 정작 원본 데이터 표본 항아리 구장 안에서 마구잡이 난수뽑기 시늉을 통해 다시금 $n$ 개의 덩치 관측치 부스러기 포지션들을 무작위 복원 뽑기 추출 추첨 발탁 선택 채집 픽업한다.

![Figure 5.10](./img/5_10.png)

**FIGURE 5.10.** Left: _A histogram of the estimates of α obtained by generating 1,000 simulated data sets from the true population._ Center: _A histogram of the estimates of α obtained from 1,000 bootstrap samples from a single data set._ Right: _The estimates of α displayed in the left and center panels are shown as boxplots. In each panel, the pink line indicates the true value of α._ 
**FIGURE 5.10.** 좌측 전경면: _진짜 모범 전능자 오리지널 모집단 심해 그 자체로부터 직접 1,000세트 분량의 무적 시뮬레이션 복사본 모조 신 데이터 세트 조각 무리를 매번 인위 창조 거푸 튀어나오게 산출 발생시킴으로써 각고 영위 획득해 내었던 당당한 α 파생 추정 도출치값들의 정통파 산 도면 హి스토그램 흔적._ 중앙 도마면: _오직 단 하나의 초라한 제한된 낱장 데이터 세트 조각을 갉아먹으며 스스로 1,000회씩이나 좀먹듯 가동 자처해 뽑아올린 부트스트랩 사기 복제 모조 추출 샘플 조가비 무리 잔여분 속에서 역으로 교묘히 얻어낸 복제산 α 추정 수치들의 또 다른 산도면 히스토그램. 우측 전경면: 일전에 나란히 사이좋게 좌측과 센터 정중앙 면역 패널 구역 스팟들에 앞서 도열 진열 전시되었던 α 추정 예측 무리 볼륨 덩치 값들이 나란히 대동단결 요약 箱子수염(boxplots) 도면의 윤곽 박스 무늬 행태 자태 폼으로 뭉뚱그려 응축 요약 치장 묘사 표출 드러내 보여주고 있다. 열거 진열 전시된 각각의 매 낱장 패널 박스 캔버스 전역 구역 국면 마당 내에는, 다름 아닌 분홍 핑크빛의 찬연한 실선 마개 지시 푯말 줄 선이 곧장 저 묻혀있는 α 자산 비율치의 무적 불패 신성 유일 진성 트루 진짜 리얼 정답 척도의 가치 위치 위엄 참값을 정확히 단호 정교 가르키며 수치 고정 찌르며 지시 박혀 있다._

The sampling is performed _with replacement_ , which means that the same observation can occur more than once in the bootstrap data set.
저 야매 추출 막노동 채집 방식은 다름 아닌 기괴한 _복원 추출(with replacement)_ 룰 규칙을 따르며 난폭 수행 시도 이행되는데, 이 말뜻인즉슨 바로 운이 나쁘면 똑같이 생긴 단 한 놈의 관측치가 애꿎게 이번 하나의 가짜 부트스트랩 데이터 복제 팩 창출 생산 제조 조립품 뭉탱이 바구니 안에서조차 심히 재수 없게 두 번 세 번 이상 연거푸 수두룩 다중 튀어나와 겹쳐 존재 발생 병합 포진 나타날 수(occur more than once) 있음의 요설 기행을 뜻한다.

In this example, $Z^{*1}$ contains the third observation twice, the first observation once, and no instances of the second observation.
작금의 작위 미니 꼼수 야매 예시 국면 마당 안에서 보자면, 이 사기 복제 클론 조립물 $Z^{*1}$ 바구니 덩어리 안에는 어처구니없게도 원본의 세 번째 번호 등수 관측치 분량이 무려 두 번 쌍코피 거푸 중복 포함되어 실려 버렸고, 제일 첫 번째 타자 관측치 분량이 얌전하게 한 번 딸랑 실려 참전 합류했으며; 정작 원본에 분명 멀쩡히 살아 숨 쉬던 두 번째 서열 번호 관측치 파편 조각 녀석은 단 한 번도 뽑히지 못한 채 철저히 존재 소외 말살 병합 유착 당해버린 사태 흔적 인스턴스(instances) 참사 기조를 내포 전시 보여준다.

Note that if an observation is contained in $Z^{*1}$, then both its _X_ and _Y_ values are included.
다만 일러두건대 여기서 은연 명심할 것은, 만약 어떤 재수 좋은 관측치 개체 영혼 덩어리 하나가 극적으로 요행 안착 무작위 발탁되어 저 가상의 복제 부트스트랩 그릇 항아리 $Z^{*1}$ 진영 속으로 편입 등극 쏙 뽑혀 담겨 들어 올려가게 되었다면? 이는 어김없이 마치 당연하게 그 녀석 영혼 파편 조각 안에 귀속되어 있는 종속 성분 옵션치인 _X_ 그리고 _Y_ 수익 수치 두 옵션 줄기 데이터 값 스펙 분량이 동시에 1+1 묶음 떨이 세트처럼 어스레 다 함께 한방에 거푸 고스란히 온전히 포함 합류 진입(included) 됨을 시사 표출 뜻한다.

We can use $Z^{*1}$ to produce a new bootstrap estimate for _α_ , which we call $\hat{\alpha}^{*1}$.
우리는 필경 마침내 힘겹게 얻어낸 이 사기꾼 클론 덩어리 바스켓인 이 $Z^{*1}$ 변이 무리를 고스란히 또다시 당돌히 활용 써먹음으로써 기치 조작 또 다른 미지의 $α$ 조준 척도 값에 덧붙일 이른바 신생 어거지 모조 복제품 부트스트랩 추정치 덩어리 하나를 거뜬 얄밉게 새롭게 생산 조립 만들어 뽑아낼 수 있는데; 우린 뻔뻔하게 이를 거슬러 $\hat{\alpha}^{*1}$ 기호로 조롱 대명 호칭 부를 작정이다. 

This procedure is repeated _B_ times for some large value of _B_ , in order to produce _B_ different bootstrap data sets, $Z^{*1}, Z^{*2}, \ldots, Z^{*B}$, and _B_ corresponding _α_ estimates, $\hat{\alpha}^{*1}, \hat{\alpha}^{*2}, \ldots, \hat{\alpha}^{*B}$.
이 미치고 끔찍한 야매 반복 조립 복제 막노동 꼼수 절차 짓거리는 필경 필연적으로 기껏 어거지로 어떤 _B_ 라는 굉장히 터무니없이 무지막지하게 거대한 물량 횟수 수치 지정값 분량만큼을 할당 책정 부여받아 억울 피 흘리며 거푸 반복 무한 리플레이 루프(repeated _B_ times) 수행 이행 조작 구동되어야만 하는데; 이는 이윽고 그 피땀 막노동의 보답 보상 차원으로 말미암아 결국 아주 고루 상이 다채롭게 다른 각양 이색적인 총 _B_ 개 물량조차 분량의 어마무시 다수 부트스트랩 찌꺼기 가변 데이터 복제 본 군단들인 무리 이른바 $Z^{*1}, Z^{*2}, \ldots, Z^{*B}$ 더미 부속들을 수확 안착 얻어내게 거푸 만들어 주며; 나아가 이것들이 곧장 연쇄 파장 고리에 대응(corresponding) 반응 작동 수반 물려 일제히 토해내는 무려 총결산 _B_ 개 분량 스펙의 $α$ 점적 추정 파편 조각들, 짐짓 $\hat{\alpha}^{*1}, \hat{\alpha}^{*2}, \ldots, \hat{\alpha}^{*B}$ 지표 궤적 스코어 무더기 덩어리들을 종래 무사 거뜬 생산 조달 분출 발굴 도출 양산 산출 양육 도달하기 위함의 당면 목적으로 전격 이행 수행 발단 감행 조작된다.

We can compute the standard error of these bootstrap estimates using the formula 
우리는 비로소 이윽고 이렇듯 처절 험난 무수히 얻어 쟁취 산출 조달해 낸 이 무더기 부트스트랩 파편 추정치 집단 오합지졸 잡동사니 조각 덩이들의 맹렬한 요동 줄기 폭 표준 오차 범위 파장 규격 변동성 스탯 지수를 이내 아래에 도열 제시된 강력 마법 공식 공식을 도구 삼아 덧대 사용 대입 연산 활용 계산해 냄으로써 단숨 영리 손쉽게 도출 돌파 짐작 점수 매겨 헤아려 산출 연산 가동 짐작해 낼 수 있다:

$$
\text{SE}_B(\hat{\alpha}) = \sqrt{\frac{1}{B - 1} \sum_{r=1}^B \left( \hat{\alpha}^{*r} - \frac{1}{B} \sum_{r'=1}^B \hat{\alpha}^{*r'} \right)^2} \quad (5.8)
$$

This serves as an estimate of the standard error of $\hat{\alpha}$ estimated from the original data set. 
이로써 거창히 얻어낸 이 궁극 수치 덩어리 무력 스탯 결과값 수위 조각은 그 자체로써, 다름 아닌 우리 인간들이 최초에 가장 애지중지 단 딱 한 번뿐인 기회로 진짜 순정 초라 빈약 오리지널 조상 원본 데이터 세트 항아리 딱 한 그릇 풀 안에서 초조하게 애통 조작 획득 추정 이입 산출 감행 가늠해 내었었던 바로 그 절대 무적 성역 고유 원본 추정치 점적 물방울 $\hat{\alpha}$ 이란 여릴 잎 장비 본연 이면 속에 감춰 짓눌려 얽혀 잠재 내제 연루 수반 도포 결박되어 있던 오매불망 널뛰기 발작 붕괴 표준 오차 위력 변동성 진폭 스코어 지수를 진정 참되고 타당 영리 신성 그럴싸하게 유추 호환 가늠해 뱉어내 보여주는 몹시 훌륭 참된 멋진 신성 대적 필적 가치 추정치 기준점 스펙 척도 역할을 막중 성실 무사 수행 대변 담당 작용 종래 발휘해 낸다(serves as). 

The bootstrap approach is illustrated in the center panel of Figure 5.10, which displays a histogram of 1,000 bootstrap estimates of _α_ , each computed using a distinct bootstrap data set.
저 야비 꼼수 마법 부트스트랩 창작 접근 기법 행로는 바로 저 도표 그림 5.10 정중앙 센터 패널 마당 구역 표면판 안에 당당 도식 도해 장관 시연 묘사 표시되어 지기 존재하는데; 이는 다름 아니게 각각 저마다 다채 요란히 이색 기괴하게 각기 다른 분파 파벌 구분 분절 독립된 신생 부트스트랩 인공 돌연 데이터 복제판 조각 그릇들을 각기 써먹고 할당 사용 연산 갉아 대입 계산 취합 연산 돌려낸 덕에 차출 얻어올려 수합 파생 도포 뱉어진 무려 천 개 1,000조각 덩이에 달하는 이색 부트스트랩 산 파생 모조 예측 α 추정치 궤적 군단 쓰레기 파편들의 전체 산 묶음 윤곽 포진 산도면 히스토그램 외형을 처절 화려 광활하게 표출 진열 드러내 뽐내 과시 전개 보여준다.

This panel was constructed on the basis of a single data set, and hence could be created using real data.
이 중앙 도마 국면 패널 그림 전경 도화지는 오로지 태초에 진정 철저히 단 하나의 유일 초라한 극빈 단층 근본 순정 오리지널 단독 데이터 세트 뭉치 부스러기 풀 웅덩이 딱 단 하나 그릇 기초 베이스 기반 위에만 전적으로 연명 기인 의존 추대 세워 발동 헌정 건축 축조 구축(constructed) 파생 수립되었으므로; 결과적 이는 고로 현실 리얼 세계 야생 실전 진짜 실물 데이터 흙먼지 더미 진창 바닥 전선 앞에서도 결코 무리 불발 좌초 없이 유효 어김없이 충분 응당 거푸 당돌 생성 헌정 구현 축조 조작 실행 산출 도달 조립될 수(created) 있는 엄청 획기 타당 위력 막강 현실적 장점 범용 보장 성격을 수반 지녔음(hence could)을 당돌 증명 호가 시사 보장한다.

Note that the histogram looks very similar to the left-hand panel, which displays the idealized histogram of the estimates of _α_ obtained by generating 1,000 simulated data sets from the true population.
다만 여기서 잠시 유의 목도 유심히 응시 주목해 놀라 살펴 경악 기이 관찰 짚어볼 것은 저 중앙판 인조 야매 꼼수 조작 사기 산수 히스토그램 점착 뭉탱이 산 무리 모양새 굴곡 파장 자태가 정작 그 왼쪽 편 구석 탱이 구역 맨 좌측 측면 끄트머리 방면 패널판에 장식 진열 고정 포장 전시 수놓여 도배 분포되었던 그 어떤 고결 오만 성역 도표 히스토그램 라인의 형상 파장 무늬와 무서울 만치 소름 돋게 거의 찍어낸 판박이 복사본인 양 몹시 무척 지극 대동소이 매우 유사 일치 흡사(very similar) 하다는 경이 참관 목도 목격 관전 발견 사실 대목이다; (참고로 오만 방자는 저 좌측 측면 패널 도표 웅덩이는 정작 옛적 그 조물주 전지 지위 진짜 권능 최고 권력 신비 참 모집단(true population) 바다 원천 뿌리 항아리 심해 조가비 신급 신계 구역으로부터 거푸 매번 순정 무결 백지장 깨끗 상태 신성 결백 시뮬레이션 창조 권능 발생 생성 뽑기 조작을 총 1,000판이나 반복 리가 갱신해 끄집 배포 무작위 방출 신출 파생 발생 새로 거푸 뽑아 찍어 얻어낸 가호 결론 α 오리진 신성 수무 추정치들만의 가장 결백 이상적 아이디얼 고결 온상 순백 박스 순결 최고 성역 궁극 도화지 궤설(idealized histogram) 덩어리를 뽐내 전시 지칭 가리켰던 그 고귀한 바로크 절대 지표 도안 패널이다.)

In particular the bootstrap estimate $\text{SE}(\hat{\alpha})$ from (5.8) is 0 _._ 087, very close to the estimate of 0 _._ 083 obtained using 1,000 simulated data sets.
특히 그 내부 요소의 진의 기강을 정밀 조밀 파헤쳐 짚어보면 아까 위 흉측 (5.8) 요술 속성 수식으로부터 억지 산출 꼼수 추출 계산 돌파 파생되었던 저 돌연변이 가짜 부트스트랩 야매 산출 덩어리 전단 추정 궤도 지수 스펙 $\text{SE}(\hat{\alpha})$ 마크 점수 볼륨 값 자체는 고스란히 0.087 좌표 마커 눈금으로 판명 종결 지어 도래 안착 산출 결론 드러났는데; 이는 저 위대한 신성 신계 조물주 발탁 가호 시뮬레이션 복제 세트 무리 데이터 물량 1,000묶음 축복 결실 지원 조작 은총을 쏟아 투입 사용 입어 얌전 고결 안착 배출 획득 얻어졌었던 저 오리지널 순정 위엄 마커 추정 지수 볼륨 스탯 0.083 좌표 라인 위치 판정 위상값과 비할 때마저도 너무나 당혹 기괴 두렵 소름 끼치고 몹시 참으로 대견 신비 무섭게도 초근접 다가붙어(very close) 밀착 일치 흡사 위상 가늠 근사 박빙 포진 근처 이웃 부합 일치 타진 적중 도래한다는 놀라운 위력 반전 기적 성과 결과 사실 파급 사태다.

The right-hand panel displays the information in the center and left panels in a different way, via boxplots of the estimates for _α_ obtained by generating 1,000 simulated data sets from the true population and using the bootstrap approach.
맨 오른쪽 끝자락 절벽 판넬 도화지 칸막이 구역은 저기 웅장 좌측 및 애증 정중앙 샌드 국면 양 측면 패널 진영에서 각기 거푸 도열 뿜어 올렸던 저 미묘 막강 두 엇갈림 요동 편차 정보 데이터 조각 찌꺼기 추이 줄기 결속 조각들을 단순히 단조 히스토그램 봉우리가 아니라 아예 사뭇 매우 새롭 이색 몹시 흥미 도발 다른 다채 통통 튀는 색다른 새로운 파격 방식 기조 우회 각도 조망 접근(in a different way) 법 체제 옷을 덧입혀 덮어씌어 재포장 진열 나열 구상 전시 시사 도해 묘사 폭로 방포 까발려 보여주는데; 이는 즉 오리지널 신계 진짜 참 모집단 신의 수역으로부터 무수 1,000결 시뮬레이션 세트를 조작 하사 가동 창조 생성 획득 발굴 연성해 낸 신성 본질 α 척도 추정치 조각군들과 그리고 저 막연 처절 꼼수 미천 부트스트랩 사기 조작 접근 묘수 접근법 우회 동원 편법을 거푸 써서 우려낸 조가비 α 야매 예측 파편 조각 군들을 서로 양측 나란히 무심 상자수염 그림(boxplots) 네모 마크 도표 형태로 요안 압축 납작 직관 윤곽 표징 도해화하여 진열 직관 승부 표출 묘사 기저 그려놓은 마당 흔적이다.

Again, the boxplots have similar spreads, indicating that the bootstrap approach can be used to effectively estimate the variability associated with $\hat{\alpha}$.
거듭 다시 한번 더 요점 천추 명심 요약 이중 확인 재관측 타진 복귀 일조 반증 판독해 보자면; 저 두 네모 얌전 반듯 상자수염 그림 상자 포장 용기 박스들은 놀랍 기이 소름 돋듯 몹시 흡사 거진 박빙 닮은꼴의 좌우 편차 진폭 위아래 뻗침 퍼짐 등락 수위(similar spreads) 덩치를 사이좋게 오붓 적중 공유 소유 수반 진열 방출 지어 보이는데; 이 기막힌 양측 붕괴 오차 위력 박스 덩이 쌍둥이 부합 유사 흡사 시각 증명 판정 파급 조망 사태 광경은 결국 저 하찮은 일선 야매 꼼수 짝퉁 부트스트랩 미천 조작 편법 추산 꼼수 접근 작위 기법 돌연 파장 체제일지라도, 정작 우리의 그 유일 순정 소중 적합 파편 도출 산물 $\hat{\alpha}$ 예측 지표 덩어리 수단 뒤에 불운 유착 결박 수반 연루 얽힌 저 저주 널뛰기 종속 표준 편차 분산 미친 폭거 변동성(variability) 등락 마구 널뛰기 수위 볼륨 지수 잣대 스펙 요동 자체를 매우 놀랍 훌륭 타당 기막히게 정교 효과 위력 유효 적절 기막 실효성 효율적으로(effectively) 적중 족집게 타진 위력 짐작 가늠 역추산 추정 재현 평가 계산해 내고 잡아채 발굴 타진 척도 때려맞추는 몹시 유용 무기 용도로써 그 본분 가치 충분 훌륭 막강 무난히 채택 기용 이바지 적용 적극 필드 사용 채용 써먹힐 수(can be used) 있음을 확고 호가 거듭 대견 기벽 실효 당당 방증 폭로 입증 천명 대변 시사(indicating) 해주는 극강 축복 압도 보증 수표 증거 사태인 셈이다.

![Figure 5.11](./img/5_11.png)

**FIGURE 5.11.** _A graphical illustration of the bootstrap approach on a small sample containing n_ = 3 _observations. Each bootstrap data set contains n observations, sampled with replacement from the original data set. Each bootstrap data set is used to obtain an estimate of α._ 
**FIGURE 5.11.** _가엾게도 고작 인구수 n_ = 3 _이라는 한 줌 미니먼지 수준의 초극소 미니 빈약 한낱 조촐 볼품없을 관측치 조각 부스러기만을 딸랑 옹색 머금은 품은 극소형 표본 단무지 덩어리 세트판 구장 위에서 다짜고짜 막가파로 벌어지는 부트스트랩 야매 반복 꼼수 접근법 기법의 극악 노골 조작 가동 연쇄 그래픽 표출 시각 도식화 윤곽 묘사 예제 일러스트. 쪼개져 양산된 매 개별 낱장 부트스트랩 야매 복제판 위장 데이터 한 세트 묶음 덩어리는 제각각 구차 어김없이 기필 모두 기존 단골 n 명분의 채워 관측치 자리 물량 치수를 강제 할당 확보 구겨 담아내는데, 이 인구수 복제는 반드시 원본 모태 웅덩이 오리지널 데이터 세트 저수지 항아리 구멍으로부터 지독 강박 다중 돌연 겹치기 허용 작위 룰인 모조 병합 변태 '복원 추출(sampled with replacement)' 이라는 우회 꼼수 난수 무작위 제비뽑기 발탁 방식 규칙 법도 기저 아래에 처절 강제 모조 야금 뽑혀 수합 건져 올려진다. 이윽고 그리 얻어진 개악 산물 매 개별 단위 한 무리 낱장 변이 복제 부트스트랩 파생 데이터 항아리 팩들은 각자 어김없이 제각기 하나 쓸데 용도 무적 밥벌이 몫을 하듯, 마침내 타겟 조준 비율 α 지수에 대응 갈망 추산 산출 어거지 투영 추정치 α 야매 짝퉁 조각 덩어리 찌꺼기 하나수들을 거푸 도래 타진 추산 얻어 도출 발굴 역산 영위 획득(obtain) 해내는 도구 무기 작위 용도로 거뜬 기필코 알차 소요 수탈 막강 기용 차용 알차게 사용 소모 착취 분출 쓰이게 된다._
