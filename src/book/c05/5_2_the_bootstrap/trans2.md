---
layout: default
title: "trans2"
---

# 5.2 The Bootstrap 
# 5.2 무에서 유를 창조하는 사기극: 부트스트랩 (The Bootstrap)

The _bootstrap_ is a widely applicable and extremely powerful statistical tool that can be used to quantify the uncertainty associated with a given estimator or statistical learning method.
_부트스트랩(bootstrap)_ ! 이름부터가 "신발 끈을 스스로 당겨 하늘을 난다"는 뜻의 뮌히하우젠 남작의 허풍에서 따온 말입니다. 이 미친 통계 기법은 우리가 뽑은 예측 덩어리(추정량)나 통계 모델이 언제 무너질지 모르는 **'불안감(불확실성, 분산)'을 숫자로 계산해 내는 통계학계 최고의 범용 치트키이자 사기극**입니다.

As a simple example, the bootstrap can be used to estimate the standard errors of the coefficients from a linear regression fit.
가장 흔한 튜토리얼 예제로, 선형 회귀 경기장을 뛰고 나서 나온 가중치(회귀 계수) 수치들이 얼마나 오들오들 떨리며 변동하는지 그 진폭(표준 오차)을 가늠할 때 이 부트스트랩을 쓸 수 있습니다.

In the specific case of linear regression, this is not particularly useful, since we saw in Chapter 3 that standard statistical software such as `R` outputs such standard errors automatically.
물론 선형 회귀처럼 빤한 판에서는 굳이 이 치트키를 쓸 필요도 없죠. 3장에서 이미 뼈저리게 봤듯, `R`이나 파이썬 같은 통계 툴들이 그냥 엔터 한 번 치면 수학 공식으로 알아서 그 에러 진폭을 다 토해내 주니까요.

However, the power of the bootstrap lies in the fact that it can be easily applied to a wide range of statistical learning methods, including some for which a measure of variability is otherwise difficult to obtain and is not automatically output by statistical software. 
하지만 부트스트랩의 진짜 공포스러운 저력은 다른 곳에 있습니다. 세상엔 파이썬 툴도 "이거 오차가 얼만지 수식으로 계산 못 함!" 하고 뻗어버리는 복잡하고 괴랄한 통계 장비들이 넘쳐납니다. 부트스트랩은 이렇게 **수학적으로 오차를 헤아리기 극도로 난해해 툴조차 포기한 그 어떤 무기 앞에서라도, 아주 무식하고 단순한 방법으로 그 변동성 에러(variability)를 손쉽게 때려 맞춰버립니다.**

In this section we illustrate the bootstrap on a toy example in which we wish to determine the best investment allocation under a simple model.
이 징그러운 기법의 작동 방식을 구경하기 위해, 이번 절에서는 우리가 벼락부자를 꿈꾸며 **"어디에 내 돈을 몰빵해야 가장 덜 망할까?(최적의 투자 수익 배분)"** 를 고민하는 아주 귀여운 장난감 금융 시나리오 하나를 가져와 시연해 보겠습니다.

In Section 5.3 we explore the use of the bootstrap to assess the variability associated with the regression coefficients in a linear model fit. 
이후 곧 배울 5.3 절 랩(Lab) 실습 구역에 가서는, 선형 모델 장막 안에서 회귀 계수가 떨리는 그 불확실성(variability)을 잴 때 이 부트스트랩 삽질을 직접 코드로 후벼 파보겠습니다.

Suppose that we wish to invest a fixed sum of money in two financial assets that yield returns of _X_ and _Y_ , respectively, where _X_ and _Y_ are random quantities.
자, 상상해 보세요. 당신에겐 전 재산이 있고 이걸 각기 $X$ 자산(코인) 과 $Y$ 자산(주식) 이라는 두 가지 미친 금융 풀에 분산 투자하려고 합니다. 문제는 이 $X$ 와 $Y$ 가 토해내는 수익(returns) 이 매일 요동치는 무작위의 도박수(random quantities) 라는 점입니다.

We will invest a fraction _α_ of our money in _X_ , and will invest the remaining 1 _− α_ in _Y_ .
당신은 현명하게도 전 재산을 쪼개어, $α$ (알파) 라는 비율만큼만 $X$ (코인) 에 묻고, 나머지 잔돈 $1 - α$ 퍼센트를 모조리 $Y$ (주식) 에 꼬라박기로 결심합니다.

Since there is variability associated with the returns on these two assets, we wish to choose _α_ to minimize the total risk, or variance, of our investment.
이 두 자산은 매일 미친 듯이 널뛰는 수익 변동성(variability) 지옥을 품고 있습니다. 쫄보인 우리는 당연히 내 전 재산이 하루아침에 반토막 나는 끔찍한 총체적 위험(total risk, 즉 분산) 을 극저로 끌어내릴 수 있는 어떤 **마법의 방어 황금 비율 $α$** 를 찾아 헤매게 됩니다.

In other words, we want to minimize Var( _αX_ + (1 _− α_ ) _Y_ ).
우아한 수학의 언어로 번역하자면, 우리의 지상 목표는 저 $\text{Var}(\alpha X + (1 - \alpha)Y)$ 라는 끔찍한 변동성 공식을 최소 바닥점(minimize) 으로 억눌러버리는 것입니다.

One can show that the value that minimizes the risk is given by 
수학 천재들이 끄적거려 본 결과, 그 위험을 아주 기막히게 잠재우는 황금의 비율 알파($α$) 가 다음의 역학 공식 구조로 딱 떨어진다는 걸 증명해 냈습니다:

$$
\alpha = \frac{\sigma_Y^2 - \sigma_{XY}}{\sigma_X^2 + \sigma_Y^2 - 2 \sigma_{XY}} \quad (5.6)
$$

where $\sigma_X^2 = \text{Var}(X)$, $\sigma_Y^2 = \text{Var}(Y)$, and $\sigma_{XY} = \text{Cov}(X, Y)$.
여기서 저 기호들은 별거 없습니다. $\sigma_X^2$ 는 코인($X$) 이 널뛰는 분산 리스크고, $\sigma_Y^2$ 는 주식($Y$) 의 분산 리스크이며, $\sigma_{XY}$ 는 이 녀석 둘이 동시에 같이 미쳐 날뛰는지 보여주는 공분산(Covariance) 일 뿐이죠.

In reality, the quantities $\sigma_X^2$, $\sigma_Y^2$, and $\sigma_{XY}$ are unknown.
하지만 이게 현실의 주식판이라면? 저 $\sigma_X^2$, $\sigma_Y^2$ 같은 신의 장부(진짜 리스크 수치) 는 아무도 모릅니다(unknown). 모니터 너머 세력만이 알겠죠.

We can compute estimates for these quantities, $\hat{\sigma}_X^2$, $\hat{\sigma}_Y^2$, and $\hat{\sigma}_{XY}$, using a data set that contains past measurements for _X_ and _Y_ .
그래도 인간들은 꼼수를 씁니다. 지난 몇 년간 $X$ 와 $Y$ 가 어떻게 떡상하고 떡락했는지 기록해 둔 '과거 역사 데이터'를 영끌해 모아서, 대충 "이 정도 떨리겠지" 하며 추정치 조각들인 $\hat{\sigma}_X^2$, $\hat{\sigma}_Y^2$, $\hat{\sigma}_{XY}$ 를 가늠해 찍어냅니다.

We can then estimate the value of _α_ that minimizes the variance of our investment using 
그러면 우린 이 긁어모은 추정 쪼가리들을 공식에 다시 우겨 넣어서, 우리의 피 같은 전 재산을 지켜줄 최적의 요새 비율 $α$ 추정치를 마침내 타진할 수 있게 됩니다!:

$$
\hat{\alpha} = \frac{\hat{\sigma}_Y^2 - \hat{\sigma}_{XY}}{\hat{\sigma}_X^2 + \hat{\sigma}_Y^2 - 2 \hat{\sigma}_{XY}} \quad (5.7)
$$

Figure 5.9 illustrates this approach for estimating _α_ on a simulated data set.
그림 5.9가 바로 이 눈물겨운 여정, 즉 가짜 시뮬레이션 데이터를 조립해서 저 투자 황금 비율 $α$ 를 찍어 맞춰보려는 과정을 우아하게 보여줍니다.

In each panel, we simulated 100 pairs of returns for the investments _X_ and _Y_ .
저 조그만 4개의 매 패널 네모칸마다, 우린 조물주처럼 행세하며 투자 $X$ 와 $Y$ 가 토해낸 100일 치 가상의 수익 쌍을 와장창 새롭게 돌려서 뿜어내 보았습니다.

We used these returns to estimate $\hat{\sigma}_X^2$, $\hat{\sigma}_Y^2$, and $\hat{\sigma}_{XY}$, which we then substituted into (5.7) in order to obtain estimates for _α_ .
그리고 뿜어진 그 100개의 조각들을 싹 주워 담아 리스크 추정치인 $\hat{\sigma}_X^2$ 따위를 계산해 내고, 그걸 저기 위 (5.7) 마법 공식에 치환해 밀어 넣은 뒤 기어코 한 판마다의 최적 몫 $α$ 예측 도출물을 토해내게 만들었죠.

The value of $\hat{\alpha}$ resulting from each simulated data set ranges from 0 _._ 532 to 0 _._ 657. 
그 결과, 가상의 데이터를 돌릴 때마다 판마다 다르게 나온 $\hat{\alpha}$ 의 결과율 스펙 궤적들은 조용하게 하단 0.532대에서 위로는 0.657 부근 일대까지 소소하게 진폭을 오르락내리락거리며 요동치는 걸 구경할 수 있습니다.

It is natural to wish to quantify the accuracy of our estimate of $\hat{\alpha}$.
자, 내가 내복 차림 컴퓨터 앞에서 뽑아낸 저 투자 비율 $\hat{\alpha}$ 가 내일 내 전 재산을 안 날릴 만큼, 과연 얼마나 오차 없이 예리하게 정확할지 그 적중도를 측정(quantify) 해 평가해 보고 싶은 건 사람의 당연한 본능입니다.

To estimate the standard deviation of $\hat{\alpha}$, we repeated the process of simulating 100 paired observations of _X_ and _Y_ , and estimating _α_ using (5.7), 1,000 times.
저 예측치 $\hat{\alpha}$ 가 대체 얼마나 믿음직하게 덜 흔들리는지(표준 편차) 알아보려고, 우린 아예 실험실을 풀가동해 "100일 치 $X, Y$ 기록을 뽑아내고 (5.7) 공식을 갈겨서 알파를 계산하는 미친 짓"을 아예 기계처럼 무자비하게 **1,000번(1,000 times)** 이나 반복 재생해 뺑뺑이 돌려보았습니다!

We thereby obtained 1,000 estimates for _α_ , which we can call $\hat{\alpha}_1, \hat{\alpha}_2, \ldots, \hat{\alpha}_{1000}$.
그 노가다의 눈물겨운 결실로, 우리의 수중엔 무려 1,000조각의 알파 추정 파편 부스러기(결과물) 가 쌓였습니다. 자랑스럽게 얘네들에게 $\hat{\alpha}_1, \hat{\alpha}_2, \ldots, \hat{\alpha}_{1000}$ 이라고 훈장을 달고 번호를 매겨줍시다.

The left-hand panel of Figure 5.10 displays a histogram of the resulting estimates.
그림 5.10의 제일 첫 왼쪽 구역 도마를 보시죠. 우리가 이 노가다로 겨우겨우 모은 저 1,000개의 추정 파편 조각 덩어리들이 수치별로 얼만큼 쌓여 집중 포화 분포되었는지를 나타내는 멋진 산 모양의 히스토그램 군락 도안입니다.

For these simulations the parameters were set to $\sigma_X^2 = 1, \sigma_Y^2 = 1.25$, and $\sigma_{XY} = 0.5$, and so we know that the true value of _α_ is 0 _._ 6.
(사실 우리끼리 몰래 까놓고 말하자면. 우린 컴퓨터로 이걸 시뮬레이션할 때부터 애초에 내부 스탯 변수값을 $\sigma_X^2 = 1$, $\sigma_Y^2 = 1.25$, $\sigma_{XY} = 0.5$ 로 몰래 설정해 뒀습니다! 즉 이 세상 조물주인 우린, 그 진정한 신의 황금 비율 _α_ (진짜 참값) 이 다름 아닌 0.6 언저리라는 걸 속으로 훤히 꿰고 알고 있죠.)

We indicated this value using a solid vertical line on the histogram. 
그래서 우린 잘난 척하며, 저 산 모양 판넬 그림(히스토그램) 한가운데에 "이게 진짜 정답 신의 참값 0.6 이야 임마!" 라며 당당하게 굵고 시커먼 세로 내림선을 확 박아 못 박아 놓았습니다.

![Figure 5.9](./img/5_9.png)

**FIGURE 5.9.** _조그만 4개의 각 전광판 패널 스팟 구역들은, 컴퓨터가 인위 가상으로 빚어 투척해 뽑아낸 투자 칩 (X, Y) 들의 수익 장부 100쌍씩의 결과를 도식해 보여줍니다. 좌측 상단부터 대각을 타 시계 방향, 그리고 하단까지 흘러가는 턴 동안 획득된 투자 최고 효율 몫 비율 예측선 수위 결과는 얼추 제각기_ 0.576 _,_ 0.532 _,_ 0.657 _, 그리고_ 0.651 _에 안착하여 포진하네요._

The mean over all 1,000 estimates for _α_ is 
아까 피 땀 흘려 얻었던 그 막대한 1,000조각 분량의 _α_ 추정 찌꺼기 덩어리들을 싹 다 긁어모아서 평균을 때려보면 

$$
\bar{\alpha} = \frac{1}{1000} \sum_{r=1}^{1000} \hat{\alpha}_r = 0.5996
$$

very close to _α_ = 0 _._ 6, and the standard deviation of the estimates is 
진짜 소름 끼치게도 원래의 신의 참값 정답 0.6 좌표 위치에 거진 빨랫줄처럼 초근접하게 ба짝 달라붙어 다가섭니다! 나아가 그 1,000명 패거리들의 오합지졸 분산도를 헤아린 그 변동성 위엄 '표준 편차' 성적을 까보면 

$$
\sqrt{\frac{1}{1000 - 1} \sum_{r=1}^{1000} (\hat{\alpha}_r - \bar{\alpha})^2 } = 0.083
$$

This gives us a very good idea of the accuracy of $\hat{\alpha}$: $\text{SE}(\hat{\alpha}) \approx 0.083$.
이게 우리에게 말해주는 진리는 막강합니다. 아, 우리가 대충 100개 뽑아서 찍어 만든 그 한 줌 추정 쪼가리 무기 $\hat{\alpha}$ 라도, 실제 정답에서 얼마나 빗나갈지 흔들리는 적중률 방어선(표준 오차, SE)이 $\text{SE}(\hat{\alpha}) \approx 0.083$ 밖에 안 되는 아주 믿음직한 기특한 녀석이구나! 하는 통찰을 하사하죠.

So roughly speaking, for a random sample from the population, we would expect $\hat{\alpha}$ to differ from _α_ by approximately 0 _._ 08, on average.
이걸 그냥 동네 아저씨 말투로 대충 퉁쳐 번역하자면; 아무렇게나 항아리에서 꺼낸 데이터 덩어리로 무기를 만들어 찍어내도, 내 추정 쪼가리 $\hat{\alpha}$ 가 몰래 숨은 정답 $α$ 에서 아무리 빗나가봐야 평균적으로 고작 약 0.08 수준 안팎의 한 보폭거리 안에서 안전하게 맴돌(expect) 거다! 라고 자신 있게 베팅할 수 있다는 뜻입니다. 

In practice, however, the procedure for estimating $\text{SE}(\hat{\alpha})$ outlined above cannot be applied, because for real data we cannot generate new samples from the original population.
**하지만, 꿈에서 깨십쇼.** 이건 오직 우리 통계학자 조물주들이 시뮬레이션을 조작해 1000번 반복할 수 있을 때에나 가능한 신선놀음입니다. 차가운 현실 실무 야생 데이터 필드 위에서라면요? **애초에 우린 진짜 원본(모집단) 세계에서 100개짜리 데이터 묶음을 1000번 더 찍어 발굴해 달라며 끝없는 신규 채굴 생성(generate)을 할 마법도 없고, 예산도 뭣도 없습니다.** 고로 저 따위 위에서 떠든 호화로운 오차 검증 방식은 실전에선 일체 써먹을 수(applied)가 없는 개소리인 셈입니다.

However, the bootstrap approach allows us to use a computer to emulate the process of obtaining new sample sets, so that we can estimate the variability of $\hat{\alpha}$ without generating additional samples.
**자, 바로 이 지점에서 우리가 칭송하는 꼼수 사기극, "부트스트랩(bootstrap)" 대마왕이 등판하여 구원을 선사합니다!** 이 미친 부트스트랩 접근법은 그저 멍청한 컴퓨터 깡통 연산기를 미치게 조져대고 굴림으로써, 마치 우리가 "초라한 100개의 데이터 세트 하나를 가지고 수백, 수천 개의 가상 멀티버스 복제 팩 세상 샘플 세트를 새로 얻는 것 같은 신의 기적 연성 흉내(emulate)"를 치트 모방하도록 기만 허락 권능을 부여해 줍니다! 이 미친 모방 마법 덕에 피 같은 현실 자원을 태워 추가 표본을 쥐어짤 필요조차 전혀 없이(without generating!!) 단독으로 우리가 만든 고귀한 $\hat{\alpha}$ 무기의 진동 폭(불안정성) 위력을 공짜로 은밀 쉽게 가늠 계산 추정 돌파해 낼 수 있죠.

Rather than repeatedly obtaining independent data sets from the population, we instead obtain distinct data sets by repeatedly sampling observations _from the original data set_ . 
정리하자면 이건 맹랑한 '자급자족' 기만 사기 추출법입니다. 그 저 멀리 절대자 큰 바다(모집단) 에 애원하며 번번이 기어나가 독립된 데이터 세트 파편 조각 더미를 거푸 조달 받아오는 구걸 짓거리 따위 대신; 그냥 고작 쥐꼬리만 하게 주어진 단 하나의 허접한 내 앞마당 원본 실물 데이터 무더기 봉투 안에서조차, 오히려 쉴 새 없이 스스로 손을 집어 관측치들을 도로 넣고 넣고 마구 휘젓고 다시 뽑아대는 **변태 뺑뺑이 재뽑기 짓(repeatedly sampling)** 조작을 통해 은폐 돌연 자가 생식 창출하여 마치 수천 개의 다 다른 독립 이색 데이터 군단 묶음들을 뚝딱 거푸 얻어내는 착각 치트를 터뜨리는 기똥찬 발상 묘수입니다.

This approach is illustrated in Figure 5.11 on a simple data set, which we call _Z_ , that contains only _n_ = 3 observations.
이 변태 같은 야비한 자가 복제 꼼수 치기가 그림 5.11 무대 위 극단적으로 단순 비루 빈약한 현장에 적나라하게 도식 전개됩니다. 구장에 무려 달랑 단 3명(n=3) 의 불쌍한 미니 먼지 관측치 쪼가리가 포진 박힌 "Z" 라 대강 불리는 그릇 세트 표본이 있습니다. 이걸로 해보죠!

We randomly select _n_ observations from the data set in order to produce a bootstrap data set, $Z^{*1}$.
우리는 인조 뮤턴트 복제 쓰레기 하나인 이른바 '부트스트랩 가상 변이 조립 세트'인 불멸의 $Z^{*1}$ 마스크 데이터 그릇 한 팩을 기꺼이 우겨넣어 조립 구축 조달 양산해내기 위해, 정작 저 오리지널 3명짜리 바닥 그릇통 안에서 다시 난수를 돌려 막무가내 장님 코끼리 만지기 뽑기로 똑같은 수효인 n명의 관측치 목을 뽑아 픽(select) 채집해 봅니다.

![Figure 5.10](./img/5_10.png)

**FIGURE 5.10.** 왼쪽판: _조물주 진짜배기 모집단 해저 심해 수역에서 1,000가지 막강 신규 무적의 모조 세트들을 거푸 번번 얻어내어 그린 가장 교과서적인 예측 α 히스토그램 스무스 산맥의 위엄 자태._ 정중앙판: _단 한 줌의 초라하고 유일한 데이터 찌꺼기 세트에 대고 1000번의 야금 좀먹는 사기 복제 뽑기인 '부트스트랩의 마법'을 걸어 우회 조각 창출해 낸 야매 예측 α 결과 부스러기들의 또 다른 히스토그램 모조 봉우리._ 오른쪽판: _왼쪽 신계 정답판과 정중앙 야매 짝퉁 요술판에서 도포 폭격 도출된 α 무리 추정파 성적 궤도를 네모반듯 뭉쳐 박스상자수염(boxplots) 도면의 폼 윤곽으로 짜내 압축 보여주는 광활한 전경 국면입니다. 모든 패널 낱장 위에 강직하게 박힌 분홍 핑크 푯말 라인 막대기는 우리의 무적불패 진성 타겟 참 정답 오리지널 α 위치 좌표 수위의 절대 성역 치수를 찍어주고 있죠._

The sampling is performed _with replacement_ , which means that the same observation can occur more than once in the bootstrap data set.
이 막가파 뽑기 짓거리는 저 악명높은 **복원 추출(with replacement)** 변태 룰 체계를 강제로 따르며 시전 이수되는데; 이 기괴한 말뜻인즉슨 한 번 뽑힌 관측치 녀석의 영혼 장부를 다시 바스켓 안에 던져 넣고 돌리기에 한 명의 억울한 녀석이 똑같이 재수 없이 거푸 거푸 번번 두세 배수 이상(more than once) 마구 좀비처럼 부트스트랩 조립 통바구니 덩어리에 강제 출격 겹치기 소환 포진 발생 발현 당할 수 있다는 호러블한 괴기 기작을 뜻합니다.

In this example, $Z^{*1}$ contains the third observation twice, the first observation once, and no instances of the second observation.
자 보세요 우리 작위 꼼수 예시 놀이 결과물을, 이 신생 돌연 짝퉁 클론 복제 그릇인 $Z^{*1}$ 내부를 들여다보니 미쳐 돌아갑니다. 원본 3번 출석 번호 타자 관측치 조각이 억울하게 **쌍코피 터지게 두 번 겹쳐** 복제 소환 포함 거머쥐어졌고, 1번 번호 관측치 녀석은 얌전히 단 한 차례 지분 차출 이적되었으나, 비운의 2번 영혼 파편 개체 녀석은 단 한 번도 이름표 불리지 못한 채 철저히 왕따 소외 버림받아 완전 0회 궤멸 멸종 배출 부재 증발 당해버린 사태 기행 참전 흔적 참사가 도래합니다.

Note that if an observation is contained in $Z^{*1}$, then both its _X_ and _Y_ values are included.
여기서 작은 팁 유의 사항. 만일 한 요행 기운 좋은 관측치 덩어리가 $Z^{*1}$ 감옥 방어막 내부에 진입 등극 발동 착출 구출되었다면? 당연하지만 그 짐짝 영혼 내부 장부에 얽혀진 고귀 $X$ (코인) 성분 수익율 값어치 스탯과 그 $Y$ (주식) 성적표 수치 지표 두 파편 궤적 장비 모두가 강제 한 묶음으로 줄줄이 비엔나 거푸 연루 함께 세트로 포함 싹쓸이 등극 편입 진입(included) 됨을 암시 뜻합니다. 

We can use $Z^{*1}$ to produce a new bootstrap estimate for _α_ , which we call $\hat{\alpha}^{*1}$.
우리는 기어코 구질구질히 우려낸 사골 이 짝퉁 바스켓 조각 $Z^{*1}$ 무리를 고스란히 버리지 않고 거듭 야무지게 재활 치트 창조 조작 써먹음으로써 기치 새 미지의 무언가 $α$ 지수를 쏘아 맞출 목적의 이른바 신규 신장판 인공 모조 사기 복주 부트스트랩 추정치 덩어리 파편 하나를 새롭게 기만 조작 탄생 제조 이끌어 생산해 낼 수 있는데; 이를 뻔뻔 지칭 우린 야매 $\hat{\alpha}^{*1}$ 조각이라는 우스꽝 오만 대명 문구로 호가 조롱 지칭할 참입니다.

This procedure is repeated _B_ times for some large value of _B_ , in order to produce _B_ different bootstrap data sets, $Z^{*1}, Z^{*2}, \ldots, Z^{*B}$, and _B_ corresponding _α_ estimates, $\hat{\alpha}^{*1}, \hat{\alpha}^{*2}, \ldots, \hat{\alpha}^{*B}$.
바로 이 끔찍 미치광이 노가다 야매 뺑뺑이 재복제 도무 루프 굴레 절차 치기 짓거리는 어마무시 막강 엄청나게 높은 물량 부여 짐 지어진 큰 치수 숫자 분량 할당치 _B_ 번 동안 필시 무자비 끝단 피눈물 나게 루프 다중 연달(repeated) 무한 이행 가동 거푸 조작 수행 전개 이행되는데; 이는 즉 그렇게 무식 미련 굴려서라도 종래 마침내 가지각색 제각각 고루 괴팍 다르고 요상 이질 뒤틀린 개성 강한 총 _B_ 종량 바구니 묶음치에 달하는 다수 부트스트랩 사기 거대 조각 복제 파편 무더기 더미인 $Z^{*1}, Z^{*2}, \ldots, Z^{*B}$ 바구니 군단 팩들을 조작 도출 수확 창조 얻어내고; 이와 연계 결박 자극 맹렬 동조 수반되어 연신 각자 다르게 토해 터져 나오는 총대 필연 대응(corresponding) 반응 $B$ 묶음 조각 척도 분량의 $α$ 모조 야매 족집게 타진 추이 파편 지표 궤적 스코어 추정 성분 점수들 $\hat{\alpha}^{*1}, \hat{\alpha}^{*2}, \ldots, \hat{\alpha}^{*B}$ 사금파리 양산 도출 수확 결과물들 기필 거머쥐기 위함 목표 전선 목적 고착 연명 이행으로 당당 시행 가동 영위 전향 전개됩니다.

We can compute the standard error of these bootstrap estimates using the formula 
우리는 비로소 우수수 피땀 노력 갈려 우수수 대거 양산 조립 산출 덧입혀 터진 이 무더기 짝퉁 부트스트랩 모방 추출 추산 궤적 사금파리 무더기들 낱장 파편들의 그 심각 진동폭 오들거림 널뛰는 전진 진영 잣대 지표 스코어, 일명 그 표준 무적 오차 변동 파장 뇌동 폭 편차 요동수 점수를 단번에 시원스레 이하 강력 수록 하사 도래 기재 제시된 척도 공식 요술 연산(formula) 검을 차용 도구 덧대 무기 삼아 계산 산전 가늠 산술 때려 도출 단번 격파 구해낼 수 있게 이릅니다:

$$
\text{SE}_B(\hat{\alpha}) = \sqrt{\frac{1}{B - 1} \sum_{r=1}^B \left( \hat{\alpha}^{*r} - \frac{1}{B} \sum_{r'=1}^B \hat{\alpha}^{*r'} \right)^2} \quad (5.8)
$$

This serves as an estimate of the standard error of $\hat{\alpha}$ estimated from the original data set. 
이 얄팍 기만 대단 산출 기적 획득 얻어진 스탯 마크 볼륨 숫자는 그 자체가, 옛적 아주 조신 경건 무구 단 한 번 최초 주어졌었던 우리 빈궁한 손아귀 밑천 전재산 오리지널 원본 조상 데이터 진성 한 풀 뿌리 항아리 속에서 우리가 1회 기회로 단독 조심 떨며 기어 초조 가냘피 뻗치고 찍어 이뤄 산출 계산 연산 가늠해 내었었던 바로 그 신성 불가침 우리들의 참다운 지표 표식 등불 나침반 무기 추정 점적 마스코트 자태 $\hat{\alpha}$ 라인 이면 장막 등짝 뒤 속에서 늘 끔찍 결박 연루 발목 잡고 조폭 엉겨 매복 내재 탑재 진영 수반 도사리고 있던 그 가공 끔찍 불안 무아 표준 편차 분열 편차 붕괴 진동 편파 붕괴 에러 널뛰기 점수폭을 거의 소름 기가 막히고 정교 위력 타당 흡사 참되게 가늠 대리 유추 포착 짐작 산 대변 일조 거든 이행 위임 기조 역할 지표 대타 호안 구역 (serves as) 을 아주 대견하게 종래 탁월 무결 방증 이수 도달 마침내 해냅니다.

The bootstrap approach is illustrated in the center panel of Figure 5.10, which displays a histogram of 1,000 bootstrap estimates of _α_ , each computed using a distinct bootstrap data set.
저 사기 도박 꼼수 속임 복제 부트스트랩 우회 타협 야매 치트 접근 마법 작위가 앞선 图표 도안 5.10 장막 센터 한가운데 정중앙 판넬 도마 무대 위 국면 지형에 기막 극적 시연 노골 전격 묘사 전경 과시 포착 드러나 존재되는데; 이는 즉 컴퓨터 혹사 노가다 개별 각 번 차출 수탈 다르게 이지별로 독립 가공 사기 파편 창출 얻어진 단판 이색 짝퉁 고유 부트스트랩 독립 복판 바구니 조각 덩이들마다 다 긁어 먹이고 하나씩 계산 쥐똥 뽑아 올린 이른바 거대한 합산 1,000조각 파편 볼륨 스탯에 버금 웅장 달하는 부트스트랩 $\alpha$ 파생 돌연 모조 점적 추정 족집게 타진값 덩이들의 그 난무하는 거대 폭발 뭉탱 분포 빈도 형세 외곽을 기치 드높 솟구치는 웅장 산등성이 히스토그램 거대 무늬 장막 도면으로 당돌 징그럽 노골 자랑 폭로 적나라 전 방포 진열 표출해 전개 보여줍니다.

This panel was constructed on the basis of a single data set, and hence could be created using real data.
놀랍게도 저 웅장 찬란 중앙 요술 히스토그램 패널 도마는 태초 일전 단독 단 하나의 찌그러 초라 가엾은 유일 진성 극빈 단 무적 한정 제약 볼륨 덩어리 빈자 베이스 오리지널 데이터 기저 바닥 항아리 수영장 물 한 줌 조각 기반 토대 베이스 위에 의거 결단 기대서면 오직 홀로 전격 파생 성립 조립 구축 증식 파생(constructed) 도모 산출되었었던 까닭인지라; 따라서 고로 결국 향후 미지 오리무중 오프라인 현실 세계 리얼 척박 진짜 현장 野생 데이터 진흙탕 전선 더미 수풀 속에 내던져 던질 지라도 하등 전혀 무리 무마 일체 불능 불발 어불성설 없이 실전에서도 아주 거뜬 당당 응당 창조 산출 활용 복제 구현 재현 도달 기치 생성 이행 써먹 작용 발동 응용해 낼 수 있음(could be created) 을 감히 증명 선언 시사 강력 호가 통보합니다.

Note that the histogram looks very similar to the left-hand panel, which displays the idealized histogram of the estimates of _α_ obtained by generating 1,000 simulated data sets from the true population.
다만 여기서 잠시 침 꼴깍 삼키고 두 눈 부릅 조명 응시 전율 소름 돋게 경악 주의 통감해 볼 충격 실존 광경 사태 사실 단면 대목은; 기실 저 중앙 구역 배치 야매 복근 사기 조각 복붙 좀먹기 조작 부트스트랩 요술 도안 산도표 히스토그램 아웃라인 봉우리 실세 외곽 굴곡 파장 스펙이 정작 저 左측 구석 저편 머나먼 곳에 모셔 고고히 빛나 자리 잡았던 '진짜' 절대 오리지널 신들 모집단 바다 원천부터 정당 모범 당당 무려 1,000세력 조작 덩어리 복제 신규 조가비 가오 생산 도출 작위 발생 얻어내 포착 연성 빚어 그렸던 '완벽 유일 이상 신계 고결 무적 아이디얼' α 정통 신성 예지 적중 타진 점수 봉우리 히스토그램 형세 파장과 너무나 어눌 기괴 두렵 무섭고 섬뜩하게도 거의 복본 쌍둥이 영기 겹칠 만큼 몹시 똑닮게 판박이 일치 맹렬 대동 흡사(very similar) 하다는 전율 목격 현실 전복 목도 사실 사태에 봉착 도래 기조 이른 단락입니다.

In particular the bootstrap estimate $\text{SE}(\hat{\alpha})$ from (5.8) is 0 _._ 087, very close to the estimate of 0 _._ 083 obtained using 1,000 simulated data sets.
특히 까다 정교 내맥 파고 내시 들여다보아 그 기적 파장 정중 조준 콕 찝어 속살 살피면 저 구차 (5.8) 편견 마법 꼼수 공식 타진 기조 부적 부트스트랩 야매 도출 $\text{SE}(\hat{\alpha})$ 스코어 볼륨 편차 널뛰기 점수가 기어코 0.087 판정 좌표로 점수 못 안착 기록 종결 도출 해냈는데; 이 영험 성적표 위력은 다름 아니 그 정통 전능 무적 신 기계 가호 축복을 오롯 다 덧입고 신급 천 개 1000묶임 시뮬레이션 지원 사격 진영 돌파를 써 얻어 결론 성역 신계 발탁 달성 구출했던 그 오리지널 정통 순혈 마크 좌표점수 볼륨 0.083 지수 대목 부근 라인 궤도 곁 몹시 살벌 심장 초근접 바싹 턱밑 근사 소름 밀착 위치 박빙 추격 아주 가까이(very close) 도래 안착 맞닿아 맞먹는 미친 엄청난 기적 조작 파괴 위력 도달 기염 성공 일치 진영 위상 결과 적중 파급 사태임에 다다릅니다.

The right-hand panel displays the information in the center and left panels in a different way, via boxplots of the estimates for _α_ obtained by generating 1,000 simulated data sets from the true population and using the bootstrap approach.
맨 오른쪽 동편 최우측 돌출 끄트머리 방면 전경 패널 국면 수역은 그동안 무수 저 좌측과 가운데 양 단 진영 도마 국면 위에서 거푸 뽑아 올리고 도포 양측 나열 진열 분배 전시 열거 진열되었던 저 무적 대비 엇갈린 두 줄기 묘한 정보 정보 덩어리 추이 성분 잔재 편차들을 이참 단순 밋밋 산 히스토그램 노선 노골 무늬 방식을 아예 뒤엎 탈피 거부 거침없이 아주 기똥 새롭 통통 독특 완전히 판이 상이 대조 차별 다색 신선 다른 이색 도발 각도 전개 채택 돌파(in a different way); 이른바 정당 조물주 참 오리지널 신 모집단으로부터 공수 진수 파생 도무 생산 시뮬 1000 무기 창출 조달 얻어낸 순결 참배α 도출 점수 무리단과 부트스트랩 사기 편법 접근 기망 기술 전향 사용 수단 우회로 발굴 영위 뽑아 얻어올린 찌꺼기 꼼수 아류 야매 α 무법 편법 결론 추정 스코어 부락 단들을 모두 일괄 단단 네모 박스 박스상자수염(boxplots) 네모 마크 도해 형태 윤곽 위장 축소 직관 상자 표징 옷 포장 둔갑 형태로 탈바꿈 압축 으레 전시 까발 진열 도출 투표 묘사 기저 그려놓아 그 적중 양측 위력 대비 분포 조망 차이를 엿보 폭로 전경 보여줍니다.

Again, the boxplots have similar spreads, indicating that the bootstrap approach can be used to effectively estimate the variability associated with $\hat{\alpha}$.
다시 한번 목에 핏대 높 세워 명심 최후 각인 강조 확인 뇌쇄 요약 주지 타진 직시 응당 선포 어깃 결론 판단 찍어 선언해 보자면; 저기 나열 네모 반듯 두 개 듬직 상자 박스수염 무늬 도안 궤적통들은 심장 덜컹 놀랍 기절 흡사 무섭 소름 미치고 등골 똑닮은 고저 편차 상하 널뛰기 진동 폭 보폭 확산 진폭 분열 양날 볼륨 떡대 규모 위력 스펙 한도(similar spreads) 범위를 위격 나란 기꺼 공유 몽땅 수반 내포 도출 기기 지녀 전시 양분 소유 과시 방출해 버리는데; 이는 결국 아무리 속 구질 저급 야매 짝퉁 노가다 천박 사기 미천 조종 부트스트랩 편법 도피 접근 야망 우회 조작 체제 발상일지언정, 당당 정작 가장 핵심 필승 과업 난제 목적 타깃 목표였던 우리 귀하 소중무쌍 $\hat{\alpha}$ 마스코트 추정치 무기 파리 목숨 점수 뒤편 척추에 고착 기세 연루 도포 점착 기만 감춰 수반 연루 얽힌 저 가공 극강 불안 공포 요동 진동 분산 표준 분파 변동성 고저 맥박 스펙 볼륨 덩치(variability) 요율 파장을 너무나도 당돌 영리 타당 합당 실질 엄청 무섭 매섭 유효 적절 실효성 넘치 영험 대박 효과 정적 정밀 놀랍(effectively) 기막히 타진 점쳐내 거푸 가늠 계산 산출 요격 점적 추정 잡아채 측량 발굴 평가 판독 결별 가늠해 뚫어낼 수 있는 초극강 엄청 기치 막강 파워 치트 용도 공략 대안 무기 스킬 채택 병기로써 현역 필드 전선 위 아주 찰떡 당당 만사 능숙 허용 기조 응당 수월 맹렬 채무 사용 기용 도입 활용 차출 써먹 다뤄질 수(can be used) 있음을 노골 단호 대견 극명 호가 여실 기벽 증명 확치 대변 보증 선포 입증 천벌 표출 시사(indicating) 해주는 우렁찬 필연 개가 승리 축포 확증 선서 광경입니다!

![Figure 5.11](./img/5_11.png)

**FIGURE 5.11.** _세상 초라 미니 빈약 한낱 조촐 가련 단 3명(n_ = 3 _. 관측치 쪼가리) 인구수만을 딸랑 품고 옹색 안타깝 생색낸 궁핍 도마 미니 데이터 세트 샘플판 무대 위에서 노골 펼쳐지는 미친 부트스트랩 사기극 꼼수 조작 작위 발동의 노골 그래픽 전개 흐름 시각 일러스트 전역 도식 묘사. 무한 도마 복제 양산 분파 쪼개 기만 파생 배출된 매 낱장 팩 조각 부트스트랩 위장 모조 짝퉁 데이터 솥단지 통 바스켓 진영 속 수효는 단 하나 기구 한 치 오차 어김없이 늘 본판 근본 기둥 n 명분 인구 머릿수 인원 티켓 할당 정원 채워 억지 강박 담아내 구축 조성 거푸 구겨 강제 담아내야 마땅 기필 필연 지어지는데, 아뿔싸 정작 이 빌어먹 강탈 인구 인원 무한 복제 빼기 채굴 과정 조달 공급 꼼수 난수 창출은, 본 무대 원천 근본 오리지널 베이스 캠프 원본 데이터 기초 토대 항아리 웅덩이 심해 속 수렁 구역에서 가차 극악 변태 병합 무작위 강제 돌연 반복 이중 겹침 차출 추출 조가비 작위 용도 허용 마법 굴레 변종 룰 포진 기반인 저 기괴 요설 '복원 추출(sampled with replacement)' 룰 치트 속박 조건 도무 꼼수 끄집 무작위 제비뽑기 발탁 법도에 의결 속발 처절 수합 전적 투항 맹종 기인 건져 끌려 올라 수합된다. 고로 이어 그따위 도출 이단 변종 파단 파생 쟁취 거둔 매 낱장 단위 팩 부트스트랩 개체 더미 독립 조가비 항아리 바구니 데이터 군단 무리 개체 팩들 전역 일괄 모두는 전부 필립 이단 본수 이탈 없이 각기 모두 오로지 목적 부합 하나같이 타겟 과업 우리들의 지존 비율 종착 조준 절대 α 추정 거푸 투영 조작 야매 치수 짝퉁 잔재 추정 조각 수수 덩어리 지표 하나수씩을 거푸 제련 방출 이끌어 타진 도무 도래 추산 산탄 발탁 획득 영위 역산 조작 획득(obtain) 도달해 내어 건져 구출 캐내버리려는 불순 극도 영험 막중 기만 도구 작위 실질 무기 투입 수단 타겟 용도 공물 소모 무기 작위로써 능수 능란 맹위 기필 아낌 거침 수시 적극 타파 쓰이게 소모 착취 조작된다._
