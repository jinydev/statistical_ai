---
layout: default
title: "trans2"
---

[< 4.8 Exercises](../trans2.html) | [4.8.2 Applied >](../4_8_2_applied/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.8.1 Conceptual
# 4.8.1 개념 문제: 뇌 근육 단련을 위한 이론 스파링!

1. Using a little bit of algebra, prove that (4.2) is equivalent to (4.3). In other words, the logistic function representation and logit representation for the logistic regression model are equivalent. 
1. 수학 교과서에 나오는 가벼운 대수학(algebra) 잔기술을 좀 부려서, 로지스틱 확률 공식 (4.2)와 승률(오즈)에 로그를 씌운 로짓 공식 (4.3)이 결국 똑같은 애(equivalent)라는 걸 증명해 보세요. 한마디로, 로지스틱 회귀 모델의 겉모습만 다른 '확률판 얼굴' 과 '로짓판 얼굴' 이 완전한 판박이 동업자라는 걸 들춰내라는 소리입니다.

2. It was stated in the text that classifying an observation to the class for which (4.17) is largest is equivalent to classifying an observation to the class for which (4.18) is largest. Prove that this is the case. In other words, under the assumption that the observations in the $k$th class are drawn from a $N(\mu_k, \sigma^2)$ distribution, the Bayes classifier assigns an observation to the class for which the discriminant function is maximized. 
2. 아까 본문에서 우리가 은근슬쩍 넘어갔던 명제 하나! 타겟을 (4.17) 공식 스코어가 가장 높은 집단(클래스)에 냅다 꽂아버리는 게, 사실 (4.18) 판별 함수 스코어가 최대로 뜨는 집단에 꽂아버리는 거랑 영혼까지 똑같다(equivalent)고 우겼었죠? 이게 진짜 기만질이 아님을 수학적으로 증명해 보세요. 다시 말해, 각 타벌 클래스 소속의 힌트들이 예쁜 정규 분포 종소리 $N(\mu_k, \sigma^2)$ 에서 튀어나왔다고 믿어 의심치 않을 때, 절대 권력의 베이즈 분류기(Bayes classifier) 는 그 판별 함수(discriminant function) 점수가 폭발하는 곳으로 당신의 편을 갈라버린다는 팩트를 증명하는 겁니다.

3. This problem relates to the QDA model, in which the observations within each class are drawn from a normal distribution with a class-specific mean vector and a class-specific covariance matrix. We consider the simple case where $p = 1$; i.e. there is only one feature. 
3. 자, 이 문제는 각 파벌마다 자기들만의 고유한 평균 코어(mean vector) 와 요동치는 분산 폭(covariance matrix) 을 각자도생으로 따로 챙겨 먹는 유연한 폭격기, QDA 모델 이야기입니다. 뇌에 쥐 나지 않게, 이번엔 힌트 특성이 단 하나($p=1$)뿐인 초단순 1차원 배틀 필드를 깔아볼게요.
   - Suppose that we have $K$ classes, and that if an observation belongs to the $k$th class then $X$ comes from a one-dimensional normal distribution, $X \sim N(\mu_k, \sigma_k^2)$. Recall that the density function for the one-dimensional normal distribution is given in (4.16). Prove that in this case, the Bayes classifier is _not_ linear. Argue that it is in fact quadratic. 
   - 우리가 $K$ 개의 파벌 세력(클래스) 을 가지고 있다고 칩시다. 어떤 타겟이 $k$ 번째 파벌에 소속되어 있다면, 힌트 점수 $X$ 는 그 파벌 특유의 1차원 정규 분포 $X \sim N(\mu_k, \sigma_k^2)$ 에서 찍혀 나온 겁니다. (4.16)에 적혀있던 그 무시무시한 정규 분포 밀도 함수 공식을 기억 되살려 보세요. 자, 이 각자도생의 상황 구도에서는 베이즈 분류기가 절대 뻣뻣한 직선 잣대(_not_ linear) 로 칼부림하지 않는다는 걸 증명해 내는 겁니다! 오히려 그 본질이 포물선처럼 휘어지는 이차 방정식 곡선(quadratic) 임을 수학 판사 앞에서 주장(Argue) 하세요.
   - _Hint: For this problem, you should follow the arguments laid out in Section 4.4.1, but without making the assumption that $\sigma_1^2 = \dots = \sigma_K^2$._ 
   - _힌트: Section 4.4.1 에서 LDA가 "모든 파벌의 요동폭(분산) 은 무조건 다 똑같아!" 라고 우겼던 그 논리적 흐름을 그대로 따라가 보되, 이번 QDA 특권인 "모든 분산 $\sigma_k$ 가 평등하다는 그 공산당 같은 강제 가정은 당장 집어던지고" 전개해 보세요._

4. When the number of features $p$ is large, there tends to be a deterioration in the performance of KNN and other _local_ approaches that perform prediction using only observations that are _near_ the test observation for which a prediction must be made. This phenomenon is known as the _curse of dimensionality_, and it ties into the fact that non-parametric approaches often perform poorly when $p$ is large. We will now investigate this curse. 
4. 우리가 참고할 힌트 스펙 개수 $p$ 가 수십, 수백 개로 미친 듯이 늘어날 때, 테스트 타겟 반경에 아슬아슬하게 _꼭 붙어있는 동네 이웃(near)_ 만 믿고 무지성 예측을 갈기는 KNN 류의 _동네 마실(local)_ 알고리즘들은 그 성적표가 처참하게 썩어 문드러지는(deterioration) 고질병을 앓습니다. 우리는 이 치명상을 그 유명한 **_차원의 저주(curse of dimensionality)_** 라고 부릅니다! 이건 틀 없는(non-parametric) 자유 영혼 모델들이 왜 스펙 변수가 많아질수록 삽질을 하는지와 맞닿아있죠. 이 무시무시한 저주의 흑마법 본질을 살을 발라내듯 까봅시다.
   - (a) Suppose that we have a set of observations, each with measurements on $p=1$ feature, $X$. We assume that $X$ is uniformly (evenly) distributed on $[0, 1]$. Associated with each observation is a response value. Suppose that we wish to predict a test observation’s response using only observations that are within 10% of the range of $X$ closest to that test observation. For instance, in order to predict the response for a test observation with $X = 0.6$, we will use observations in the range $[0.55, 0.65]$. On average, what fraction of the available observations will we use to make the prediction? 
   - (a) 딱 하나의 스펙 라인($p=1$) 인 $X$ 축 하나만 덩그러니 놓인 1차원 세상이라고 칩시다. 데이터 $X$ 들은 $[0, 1]$ 구간 사이에 편애 없이 골고루(uniformly) 흩뿌려져 살고 있습니다. 각 집집마다 찍혀 나온 정답 타겟(반응값) 이 달려 있고요. 자, 어떤 미지의 테스트 타겟을 예측하고 싶은데, 그 타겟 주변 거리 기준, 전체 $X$ 영토 길이의 딱 10% 반경 이내에 사는 최측근 이웃들만 끌어모아 여론조사를 돌리고 싶습니다. (예: 타겟이 0.6 에 떨어졌다면, $[0.55, 0.65]$ 구간 주민들만 징집하는 식이죠). 자, 이렇게 여론조사를 돌리면, 평균적으로 전체 데이터 주민들 중에서 과연 몇 퍼센트(비율 fraction) 나 예측 투표에 써먹을 수 있을까요?
   - (b) Now suppose that we have a set of observations, each with measurements on $p=2$ features, $X_1$ and $X_2$. We assume that $(X_1, X_2)$ are uniformly distributed on $[0, 1] \times [0, 1]$. We wish to predict a test observation’s response using only observations that are within 10% of the range of $X_1$ _and_ within 10% of the range of $X_2$ closest to that test observation. On average, what fraction of the available observations will we use to make the prediction? 
   - (b) 자 레벨 업! 이번엔 스펙트럼이 $p=2$, 즉 가로/세로 축($X_1, X_2$) 이 있는 2차원 부동산 평면 $[0, 1] \times [0, 1]$ 위에 데이터들이 평등하게 깔린 아파트 단지라고 칩시다. 이번에도 예측 투표를 하려고 가장 가까운 녀석들을 징집하는데, 조건이 빡세졌습니다. "$X_1$ 영토 기준으로도 반경 10% 이내에 살아야 하고, _동시에(and)_ $X_2$ 영토 기준으로도 반경 10% 이내에 사는" 주민만 뽑으려 합니다. 이런 까다로운 기준으로 징집하면, 평균적으로 전체 단지 주민 중 몇 퍼센트 타박이나 건져낼 수 있을까요?
   - (c) Now suppose that we have a set of observations on $p=100$ features. Again the observations are uniformly distributed on each feature, and again each feature ranges in value from 0 to 1. We wish to predict a test observation’s response using observations within the 10% of each feature’s range that is closest to that test observation. What fraction of the available observations will we use to make the prediction? 
   - (c) 광기의 레벨 풀 악셀! 스펙 특성 축이 $p=100$ 개인 100차원의 안드로메다 우주 하이퍼공간입니다. 역시나 각 축의 길이는 0~1 이며 데이터들은 고르게 떠다닙니다. 이번에도 테스트 타겟 주위에서 "100개의 축 전부 다 반경 10% 이내의 거리를 만족하는" 외계인 이웃들만 예측 레이더에 걸리도록 세팅했습니다. 평균적으로 전체 외계 데이터 표본 중 티끌만 한 비율 몇 퍼센트를 우리 징집망에 건져 올릴 수 있겠습니까? 
   - (d) Using your answers to parts (a)–(c), argue that a drawback of KNN when $p$ is large is that there are very few training observations “near” any given test observation. 
   - (d) 당신이 (a) 부터 (c) 까지 풀면서 느낀 멘붕의 공포를 바탕으로, 스펙 차원 $p$ 가 100차원처럼 무식하게 커져버리면 무지성 일진 KNN 머신이 왜 개망하는지 뼈 때리는 비판(argue)을 하세요. 즉, "야 너 차원이 그렇게 넘사벽이면, 아무리 넓게 그물을 던져도 니 테스트 타겟 '근처(near)' 엔 쓸만한 훈련 이웃 데이터 자체가 씨가 말라서 텅텅 비어있단 말이다!" 를 주장해 보세요.
   - (e) Now suppose that we wish to make a prediction for a test observation by creating a $p$-dimensional hypercube centered around the test observation that contains, on average, 10% of the training observations. For $p=1, 2$, and $100$, what is the length of each side of the hypercube? Comment on your answer. 
   - (e) 아 너무 극단적이었나요? 그렇다면 룰을 슬쩍 뒤집어봅시다. "이웃을 전체 주민 중 무조건 딱 10% 덩어리를 여론조사에 모아 예측을 갈기겠다!" 라고 목표량을 정한 채, 타겟 주변에 이웃 10%가 들어올 만큼 $p$ 차원의 상자(하이퍼큐브) 덫을 치려 합니다. 차원 수가 $p=1, p=2,$ 그리고 대망의 $p=100$ 차원으로 변할 때, 이 목표 할당량 10%를 잡기 위해 우리가 늘려야 하는 **상자 덫의 한쪽 그물 모서리 길이**는 각각 우주적으로 얼마만큼 거대해져야 합니까? 그 충격적인 길이에 대해 코멘트하세요.
   _Note: A hypercube is a generalization of a cube to an arbitrary number of dimensions. When $p=1$, a hypercube is simply a line segment, when $p=2$ it is a square, and when $p=100$ it is a 100-dimensional cube._
   _참고: 상식 타임! 하이퍼큐브(hypercube) 는 우리가 아는 주사위 상자를 상상 속의 N차원으로 쭉 잡아 늘린 마법의 덫입니다. $p=1$ 이면 그냥 평범한 선분(빨대 길이)이고, $p=2$ 이면 납작한 정사각형 방구석이고, $p=100$ 이 나타나면 그건 현실을 아득히 초월한 100차원의 투명 미로 큐브입니다._

5. We now examine the differences between LDA and QDA. 
5. 자, 뻣뻣한 선형 잣대 LDA 와 짐승 같은 유연 곡선 QDA 듀오의 피 터지는 배틀 비교 들어갑니다.
   - (a) If the Bayes decision boundary is linear, do we expect LDA or QDA to perform better on the training set? On the test set? 
   - (a) 세상의 진짜 정답인 베이즈 결정 경계(Bayes boundary) 가 완벽히 자를 대고 그은 **원래 '선형(직선)'** 이라면, 연습 훈련장에서는 LDA 랑 QDA 중 누가 스코어를 더 잘 딸까요? 그럼 진짜 실전 수능(테스트 세트) 에선 누가 최후의 승자가 됩니까?
   - (b) If the Bayes decision boundary is non-linear, do we expect LDA or QDA to perform better on the training set? On the test set? 
   - (b) 반대로 이 세계의 진짜 정답 경계선이 꼬불꼬불 휘어진 **'비선형(곡선)'** 이라면! 연습장과 실전 수능장, 두 곳에서 각각 LDA 와 QDA 중 누가 1짱을 먹겠습니까?
   - (c) In general, as the sample size $n$ increases, do we expect the test prediction accuracy of QDA relative to LDA to improve, decline, or be unchanged? Why? 
   - (c) 현실의 법칙입니다. 모아온 힌트 데이터 묶음의 크기 덩치 수량 $n$ (문제집 개수) 이 무한대로 펌핑될수록, LDA 선배님에 대항하는 우리 QDA 곡선 머신의 타격 명중률(예측 정확도) 은 떡상(개선) 할까요, 나락(감소) 으로 갈까요, 아니면 노잼 유지 상태일까요? 왜 그렇게 생각합니까?
   - (d) True or False: Even if the Bayes decision boundary for a given problem is linear, we will probably achieve a superior test error rate using QDA rather than LDA because QDA is flexible enough to model a linear decision boundary. Justify your answer. 
   - (d) 명제 게임 참(True) OR 거짓(False): "주어진 문제의 진짜 세계 정답 경계 모양이 완벽한 직선(선형) 이라고 치자. 그래도 우리는 틀딱 LDA보다 QDA를 굴리는 게 개이득이다! 왜냐? QDA는 워낙 고무줄처럼 유연해서 마음만 먹으면 직선 흉내도 완벽하게 낼 수 있는 씹사기 만능 무기니까 최강의 실전 스코어(superior test error rate) 를 꽂아줄 확률(probably) 이 높다!" 이 달콤한 악마의 속삭임은 팩트일까요 개구라일까요? 논리적 팩트 체크를 박아보세요.

6. Suppose we collect data for a group of students in a statistics class with variables $X_1 =$ hours studied, $X_2 =$ undergrad GPA, and $Y =$ receive an A. We fit a logistic regression and produce estimated coefficient, $\hat{\beta}_0 = -6, \hat{\beta}_1 = 0.05, \hat{\beta}_2 = 1$. 
6. 통계학 강의실에서 영혼이 털린 학생들을 납치해 이런 데이터를 털었다고 칩시다. $X_1 =$ 도서관 쳐박힌 시간, $X_2 =$ 학부 졸업 평점(GPA), 그리고 과녁 타겟 $Y = $ 꿈의 A학점 쟁취 여부. 여기에 우리의 로지스틱 회귀 기계를 피팅했더니, 요런 파워 스코어 딱지를 뱉었습니다: $\hat{\beta}_0 = -6, \hat{\beta}_1 = 0.05, \hat{\beta}_2 = 1$. 
   - (a) Estimate the probability that a student who studies for 40 h and has an undergrad GPA of 3.5 gets an A in the class. 
   - (a) 도서관에서 40시간(h) 동안 엉덩이 짓무르며 공부했고, 학부 평점이 무려 3.5 점에 빛나는 엘리트 학생이, 이번 강의에서 A를 날먹할 그 당첨 '확률' 을 점괘 뽑듯 맞춰보세요.
   - (b) How many hours would the student in part (a) need to study to have a 50% chance of getting an A in the class? 
   - (b) 아까 (a) 번 그 평점 3.5 짜리 학생 녀석이, 가성비 개꿀로 "A학점 받을 확률 덤덤하게 절반 딱 50%" 까지만 끌어치기 하려면 최소 몇 시간을 도서관에서 버텨야 합니까?

7. Suppose that we wish to predict whether a given stock will issue a dividend this year (“Yes” or “No”) based on $X$, last year’s percent profit. We examine a large number of companies and discover that the mean value of $X$ for companies that issued a dividend was $\bar{X} = 10$, while the mean for those that didn’t was $\bar{X} = 0$. In addition, the variance of $X$ for these two sets of companies was $\sigma^2 = 36$. Finally, 80% of companies issued dividends. Assuming that $X$ follows a normal distribution, predict the probability that a company will issue a dividend this year given that its percentage profit was $X = 4$ last year. 
7. 당신은 작년 수익 폭발률($X$) 이라는 꿀단지 지표 하나만 보고, 올해 이 빌어먹을 주식 작전주가 짭짤한 배당금 봉투를 돌릴지 말지(“Yes” or “No”) 점을 치려는 여의도의 야수의 심장입니다. 미친 듯이 상장사들을 탈탈 털어보니, 가뭄에 콩 나듯 배당을 던져준 착한 파벌들(Yes 파벌) 의 작년 평균 수익 스코어는 $\bar{X} = 10$ 이었지만, 배당을 입 싹 닦은 악마 파벌들(No 파벌) 의 수익 평균 스코어는 바닥 그 자체인 $\bar{X} = 0$ 이었습니다. 게다가 두 파벌의 주가 멀미 약동성, 즉 분산 널뛰기 수치는 공평하게 $\sigma^2 = 36$ 으로 똑같았습니다. 결정적으로, 전체 상장사 중 무려 80% 라는 기적의 다수가 배당 선물을 뿌리고 다녔네요. 자, 이 $X$ (수익 지표) 가 고상하게 정규 분포를 타고 나타난다고 믿어 의심치 않을 때, 작년에 $X=4$ 라는 애매한 성적표를 뱉어낸 어떤 개잡주가 올해 뜬금포로 배당 상자를 터트릴 진짜 배팅 '확률' 을 도출해 내십시오!
   _Hint: Recall that the density function for a normal random variable is $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2 / 2\sigma^2}$. You will need to use Bayes’ theorem._ 
   _힌트: 무식한 정규 확률 곡선의 텐트 공식이 $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2 / 2\sigma^2}$ 따위였다는 걸 당신의 해마에서 소환하세요. 그리고 우아하게 베이즈 정리(Bayes’ theorem) 폭탄을 떨어뜨려야만 풀립니다._

8. Suppose that we take a data set, divide it into equally-sized training and test sets, and then try out two different classification procedures. First we use logistic regression and get an error rate of 20% on the training data and 30% on the test data. Next we use 1-nearest neighbors (i.e. $K=1$) and get an average error rate (averaged over both test and training data sets) of 18%. Based on these results, which method should we prefer to use for classification of new observations? Why? 
8. 우리가 방대한 데이터를 쓱싹 스틸해 연습 훈련장용이랑 실전 모의고사 테스트용으로 반반 공평하게 쪼갰다고 칩시다. 그리고 두 깡패 알고리즘 파벌을 데려와 격투 데스매치를 돌립니다. 첫 빠따인 '로지스틱 회귀' 선수! 이놈은 훈련장에선 틀릴 오류 확률방어율이 20%로 선방하더니, 정작 잔인한 실전 테스트장에 던져놓으니 버퍼링 걸리며 30% 로 오답 폭망률이 터졌습니다. 다음 조커 카드, 내 눈앞의 딱 1명만 믿는 극단주의 '1-최근접 이웃($K=1$ 인 KNN)' 출격! 근데 이 변태 같은 놈은 성적표를 까보니, 훈련장이랑 실전 시험지 오작동 확률 콤보 평균이 "18%" 란 꽤 달달해 보이는 점수가 적혀있네요! 자, 당신이 새롭게 미지의 미래 적군을 마주해서 단 하나의 방패를 쥐어야 한다면, 이 두 성적표만 보고 누구를 영입해 분류 방어 막을 세우고 싶습니까? 그리고 이런 변태적 결정을 내린 이유는 대체 뭡니까?

9. This problem has to do with _odds_. 
9. 도박사들의 고향, 승률 배팅의 정수인 **_오즈(odds)_** 에 관한 두뇌 퀴즈입니다.
   - (a) On average, what fraction of people with an odds of 0.37 of defaulting on their credit card payment will in fact default? 
   - (a) 신용카드를 긁고 배 째라 파산할(채무 불이행) '오즈 스코어' 가 0.37 이라고 찍혀 나온 시한폭탄 인간계층을 모아놨다고 합시다. 진짜로 까보면, 이들 중 평균적으로 도대체 몇 퍼센트(비율 fraction) 의 노양심들이 진짜로 은행 채무 불이행 파산을 터트리고 폭망할까요?
   - (b) Suppose that an individual has a 16% chance of defaulting on her credit card payment. What are the odds that she will default? 
   - (b) 반대로, 어떤 양심 불량녀가 은행을 상대로 먹튀 파산할 본질적(chance) 확률이 16% 라고 점쳐졌습니다. 그렇다면 그녀가 그 무대 위의 배팅판에 올랐을 때, 그녀의 배 째라 파산 배팅 '오즈 스코어' 는 얼마로 튕겨 나올까요?

10. Equation 4.32 derived an expression for $\log(\text{Pr}(Y=k|X=x) / \text{Pr}(Y=K|X=x))$ in the setting where $p > 1$, so that the mean for the $k$th class, $\mu_k$ is a $p$-dimensional vector, and the shared covariance $\Sigma$ is a $p \times p$ matrix. However, in the setting with $p=1$, (4.32) takes a simpler form, since the means $\mu_1, \dots, \mu_K$ and the variance $\sigma^2$ are scalars. In this simpler setting, repeat the calculation in (4.32), and provide expressions for $a_k$ and $b_{kj}$ in terms of $\pi_k, \pi_K, \mu_k, \mu_K$, and $\sigma^2$. 
10. 본문 교과서의 매운맛 수식 (4.32) 를 기억하시나요? 이 미친 방정식은 수십 개의 스펙 축($p > 1$) 이 난무하는 하이퍼 공간을 전제로 $\log(\text{Pr}(Y=k|X=x) / \text{Pr}(Y=K|X=x))$ 구구절절 수식을 쥐어짜 내서(derived), 각 파벌의 대빵 코어 $\mu_k$ 가 뚱뚱한 다차원 벡터가 되고, 공유 평화 협정 공분산 덩어리 $\Sigma$ 마저 거대 빌딩 $p \times p$ 행렬로 부풀어 올랐었습니다. 근데 억지 텐션을 쫙 빼고 딱 하나의 변수 $p=1$ 만 남긴 소박한 방구석 세팅으로 돌리면 이 (4.32) 공식은 아기자기한 다이어트 폼(simpler form) 에 빠집니다. 무서운 행렬 따위 증발하고, $\mu_k$ 랑 분산 $\sigma^2$ 도 그냥 동네 꼬마 스칼라(일반 숫자) 단위로 쪼그라들거든요. 자, 이 귀염뽀짝한 세팅 방안에서 (4.32) 짓거리를 한 번 더 쪼물딱거리며 분해해 보시고, 방 탈출 암호문 같은 잔여물 $a_k$ 랑 $b_{kj}$ 의 본질이 도대체 뭐였는지 $\pi_k, \pi_K, \mu_k, \mu_K$ 그리고 $\sigma^2$ 라는 장난감 블록들을 조립해서 당당히 공식으로 표현해 내세요!

11. Work out the detailed forms of $a_k, b_{kj}$, and $b_{kjl}$ in (4.33). Your answer should involve $\pi_k, \pi_K, \mu_k, \mu_K, \Sigma_k$, and $\Sigma_K$. 
11. 자, 노가다 퍼즐 (4.33)의 속살을 남김없이 파헤쳐, 미지의 암호화 스파이 세력 $a_k, b_{kj}$, 그리고 극강의 $b_{kjl}$ 요원들의 밑바닥 설계도를 도화지에 전부 갈아 넣어 까발리십시오(Work out). 단, 당신의 정답 설계도에는 무조건 $\pi_k, \pi_K, \mu_k, \mu_K, \Sigma_k$, 그리고 대망의 마피아 보스 $\Sigma_K$ 들이 멱살 잡고 엮여(involve) 있어야만 합니다.

12. Suppose that you wish to classify an observation $X \in \mathbb{R}$ into `apples` and `oranges`. You fit a logistic regression model and find that 
12. 당신의 정체불명 외계인 과일 $X \in \mathbb{R}$ 를 주머니에서 꺼내어 `사과(apples)` 팀 스티커를 붙일지 `오렌지(oranges)` 팀 스티커를 붙일지 심판을 보려 합니다. 그래서 우리의 믿음직한 로지스틱 회귀 기계를 뼛속까지 피팅시켜 요따위 결론을 뽑아냈습니다:

$$
\text{Pr}(Y = \text{orange} \mid X = x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}
$$

Your friend fits a logistic regression model to the same data using the _softmax_ formulation in (4.13), and finds that 
그런데 당신 옆에서 나대던 밉상 친구놈은, 똑같은 데이터를 주워 먹고도 굳이 자기 잘난 맛에 다중 선택지용 오지랖 공식인 _소프트맥스(softmax)_ (4.13) 쌍권총 폼을 잡고 피팅을 돌려서 이런 그로테스크한 폼을 뱉어냅니다:

$$
\text{Pr}(Y = \text{apple} \mid X = x) = \frac{e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x} + e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}
$$

$$
\text{Pr}(Y = \text{orange} \mid X = x) = \frac{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x}}{e^{ \alpha_{\text{orange} 0} + \alpha_{\text{orange} 1} x} + e^{ \alpha_{\text{apple} 0} + \alpha_{\text{apple} 1} x}}
$$

- (a) What is the log odds of `orange` versus `apple` in your model? 
- (a) 자, 당신의 그 심플한 클래식 모델 세상 속에서, 촌스러운 `apple` 따위 구석에 처박고 반짝이는 `orange` 가 이겨버릴 통쾌한 '로그 오즈(log odds, 배팅률 배수 로그값)' 전투력은 대체 어떻게 표시됩니까?
- (b) What is the log odds of `orange` versus `apple` in your friend’s model? 
- (b) 그럼, 당신 친구의 그 현학적인 잡동사니 소프트맥스 세상 속에선 `apple` 이 발리고 `orange` 가 이길 로그 오즈 전투력이 과연 수식으로 어떻게 변태같이 뽑혀 나옵니까?
- (c) Suppose that in your model, $\hat{\beta}_0 = 2$ and $\hat{\beta}_1 = -1$. What are the coefficient estimates in your friend’s model? Be as specific as possible. 
- (c) 당신의 심플 모델 안에서 마침 파워 스코어가 $\hat{\beta}_0 = 2$ 이고 빔 기울기가 $\hat{\beta}_1 = -1$ 이 떴다고 상상해 보세요. 그렇다면 친구놈의 복잡한 모델에 박혀 굴러가야 할 그 미지의 스코어 계수(알파 덩어리)들은 도대체 무슨 숫자로 세팅되어 있어야 둘이 공평한가요? 소름 돋게 집요하고 구체적으로 낱낱이 파헤쳐 밝혀(specific) 보세요.
- (d) Now suppose that you and your friend fit the same two models on a different data set. This time, your friend gets the coefficient estimates $\hat{\alpha}_{\text{orange} 0} = 1.2, \hat{\alpha}_{\text{orange} 1} = -2, \hat{\alpha}_{\text{apple} 0} = 3, \hat{\alpha}_{\text{apple} 1} = 0.6$. What are the coefficient estimates in your model? 
- (d) 이번엔 분위기를 바꿔서, 둘 다 새로운 농장 데이터로 이사를 간 뒤 또 피팅을 갈겼다고 치죠. 아니 웬걸? 이번엔 기고만장한 친구 녀석이 먼저 자기 계량기에 숫자를 딱 띄웁니다! $\hat{\alpha}_{\text{orange} 0} = 1.2, \hat{\alpha}_{\text{orange} 1} = -2, \hat{\alpha}_{\text{apple} 0} = 3, \hat{\alpha}_{\text{apple} 1} = 0.6$. 자, 이 숫자를 훔쳐본 당신은 굳이 컴퓨터 안 돌리고 당신의 심플 모델 계량기($\hat{\beta}$) 에 뜰 숫자를 이미 간파했을 겁니다. 그게 얼마입니까?
- (e) Finally, suppose you apply both models from (d) to a data set with 2,000 test observations. What fraction of the time do you expect the predicted class labels from your model to agree with those from your friend’s model? Explain your answer.
- (e) 피날레! 당신과 당신의 친구가 세팅 완료한 (d)판 듀얼 머신을 들고, 2,000개의 야생 테스트 과일 타겟이 날아다니는 거대한 배틀 필드에 서 있습니다! 이 난장판에서 과연, 당신 모델이 "오렌지다!" 라고 쐈을 때 친구 모델도 "오옷 오렌지!" 라고 똑똑하게 맞장구치는 도플갱어급 일심동체 합의 타율(agree with) 이 전체 판의 대체 몇 퍼센트 비율(fraction) 급이나 터질지 예언해 보세요. 그 이유도 밑밥을 깔아 논리적으로 폭격(Explain) 하시길!

---

## Sub-Chapters

[< 4.8 Exercises](../trans2.html) | [4.8.2 Applied >](../4_8_2_applied/trans2.html)
