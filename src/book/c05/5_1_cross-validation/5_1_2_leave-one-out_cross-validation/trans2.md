---
layout: default
title: "trans2"
---

# 5.1.2 Leave-One-Out Cross-Validation
# 5.1.2 극한의 모의고사: 단 1명만 빼고 다 훈련시킨다! (LOOCV)

_Leave-one-out cross-validation_ (LOOCV) is closely related to the validation set approach of Section 5.1.1, but it attempts to address that method’s drawbacks. 
앞에서 뼈 때리게 까였던 반반 무 많이 쪼개기 시스템(검증 세트 접근법) 때문에 빡친 학자들이 만들어낸 초진화 시스템이 바로 **_단일 관측치 제외 교차 검증(Leave-one-out cross-validation, LOOCV)_** 입니다. 근본 줄기는 비슷하지만, 앞선 방식의 그 환장할 가변성 주사위 도박(drawbacks)을 완전히 박살 내버리기 위해(address) 영혼을 갈아 넣은 방법론이죠.

Like the validation set approach, LOOCV involves splitting the set of observations into two parts. However, instead of creating two subsets of comparable size, a single observation $(x_1, y_1)$ is used for the validation set, and the remaining observations $\{(x_2, y_2), \dots, (x_n, y_n)\}$ make up the training set. The statistical learning method is fit on the $n - 1$ training observations, and a prediction $\hat{y}_1$ is made for the excluded observation, using its value $x_1$. Since $(x_1, y_1)$ was not used in the fitting process, $\text{MSE}_1 = (y_1 - \hat{y}_1)^2$ provides an approximately unbiased estimate for the test error. But even though $\text{MSE}_1$ is unbiased for the test error, it is a poor estimate because it is highly variable, since it is based upon a single observation $(x_1, y_1)$. 
이 방식도 일단 데이터를 훈련용과 모의고사용 두 뭉치로 가르긴 합니다. 하지만 예전처럼 50대 50 멍청하게 반반 자르는 짓은 안 합니다. 극한의 무자비함! 전체 학생 군단 중에서 **딱 1명(단일 관측치 $x_1, y_1$)만 콕 집어서 불쌍하게 '검증(모의고사)' 방으로 유배**를 보냅니다. 그리고? 남은 미친 대규모 군단(나머지 $n-1$명 전체) 을 모조리 '훈련 캠프(training set)' 에 쏟아부어 지옥 훈련(fit) 을 시킵니다. 훈련을 마친 이 거대괴수 모델에게 아까 빼뒀던 그 1명의 외계인 데이터($x_1$) 를 던져주고 예언치($\hat{y}_1$) 를 맞추게 시켜 버립니다. 그 불쌍한 1명의 제물은 훈련 과정에 1밀리초도 참여 못 했으니 여기서 발생한 $\text{MSE}_1 = (y_1 - \hat{y}_1)^2$ 타격 스코어는 꽤 훌륭하게 과장 없는(편향되지 않은 unbiased) 아주 정직한 실전 에러 점수 역할을 해줍니다. 오! 완벽하네요? 하지만 까고 보면 함정이 있습니다. 아무리 정직해도, 달랑 1명의 녀석만 보고 낸 점수라서 "아 그놈이 유독 못생긴 예외 데이터였으면 어쩔 건데?" 라는 딜레마에 부딪히며 점수가 널뛰는(highly variable) 끔찍한(poor) 견적서가 되어버립니다.

We can repeat the procedure by selecting $(x_2, y_2)$ for the validation data, training the statistical learning procedure on the $n - 1$ observations $\{(x_1, y_1), (x_3, y_3), \dots, (x_n, y_n)\}$, and computing $\text{MSE}_2 = (y_2 - \hat{y}_2)^2$. Repeating this approach $n$ times produces $n$ squared errors, $\text{MSE}_1, \dots, \text{MSE}_n$. The LOOCV estimate for the test MSE is the average of these $n$ test error estimates: 
그래서 우리 지독한 통계학자들은 어떻게 할까요? 이 짓거리를 "모든 학생이 딱 한 번씩 그 희생양이 될 때까지" 끝까지 반복무한루프 시킵니다. 두 번째 턴! 이번엔 2번 학생($x_2, y_2$) 을 독방(validation) 으로 빼고, 1번을 포함한 남은 전원을 다시 훈련소로 굴려서 $\text{MSE}_2$ 를 뜯어냅니다. 이런 식으로 전체 학생 수인 **$\mathbf{n}$ 번 내내 반복 노가다(Repeating)** 를 뜁니다! 결국 $n$ 개의 희생양 오답 노트 $\text{MSE}_1$ 부터 $\text{MSE}_n$ 까지 쌓이겠죠. LOOCV 가 최종적으로 내미는 빛나는 "테스트 MSE 견적서" 는 이 N번의 오답 노트들 싹 다 끌어모아 달달하게 **평균(average)** 낸 스코어입니다!

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \text{MSE}_i \quad (5.1)
$$

**FIGURE 5.3.** _A schematic display of LOOCV. A set of n data points is repeatedly split into a training set (shown in blue) containing all but one observation, and a validation set that contains only that observation (shown in beige). The test error is then estimated by averaging the n resulting MSEs. The first training set contains all but observation 1, the second training set contains all but observation 2, and so forth._ 
**FIGURE 5.3.** _극한의 노가다 머신 LOOCV 구조도. 전체 타겟들을 상대로 빙글빙글 턴을 돌며, 한 턴마다 오직 운 나쁜 녀석 딱 1명만 베이지색 유배지(검증 방)에 감금하고 나머지 전원을 파란색 훈련소로 강제 징용합니다. 나중에 그 불쌍한 희생양이 남긴 피의 모의고사 오답 점수 $n$ 개를 탈탈 털어 합산 평균을 냅니다._

A schematic of the LOOCV approach is illustrated in Figure 5.3. 
LOOCV의 무자비한 뺑뺑이 개념도는 Figure 5.3에 절찬리 상영 중입니다.

LOOCV has a couple of major advantages over the validation set approach. First, it has far less bias. In LOOCV, we repeatedly fit the statistical learning method using training sets that contain $n - 1$ observations, almost as many as are in the entire data set. This is in contrast to the validation set approach, in which the training set is typically around half the size of the original data set. Consequently, the LOOCV approach tends not to overestimate the test error rate as much as the validation set approach does. Second, in contrast to the validation approach which will yield different results when applied repeatedly due to randomness in the training/validation set splits, performing LOOCV multiple times will always yield the same results: there is no randomness in the training/validation set splits. 
이 짓거리가 주는 보상은 확실합니다. 아까 봤던 반반 쪼개기보다 차원이 다른 혜택(major advantages) 이 두 가지나 쏟아집니다. **첫째, 비겁한 축소 왜곡(Bias 체급 편향) 이 거의 사라집니다.** LOOCV 훈련소에는 매 턴마다 1명 빼고 전원($n-1$명) 이 입소하기 때문에, 사실상 백분율 100% 실전 환경이나 다름없는 꽉 찬 덩치로 훈련을 치릅니다. 아까 고작 50% 반토막 부대만 공부시켜서 실전 대비를 망쳐버렸던 반반 무 많이 전략과는 궤를 달리하죠. 덕분에 자신의 에러율을 과대망상으로 뻥튀기(overestimate) 하는 억까 현상이 자취를 감춥니다. **둘째, 주사위 복불복(무작위성)의 종말!** 반반 쪼개기는 돌릴 때마다 파벌이 달라져서 스코어가 춤을 췄지만, 이건 "어차피 전원이 무조건 한 번씩 순번제로 쳐 맞게" 시스템이 고정되어 있습니다(no randomness). 즉, 당신이 내일 돌리든 10년 뒤에 돌리든 무조건 한 치의 오차 없이 완벽히 똑같은 결과 값(same results) 을 선사합니다.

We used LOOCV on the `Auto` data set in order to obtain an estimate of the test set MSE that results from fitting a linear regression model to predict `mpg` using polynomial functions of `horsepower` . The results are shown in the left-hand panel of Figure 5.4. 
아까 했던 그 `Auto` 차 연비(`mpg`) 맞추기 마력(`horsepower`) 곡선 베팅 게임에 이번엔 이 극한의 LOOCV 머신을 풀 가동시켜 진짜 정직한 실전 모의고사 스코어를 쥐어 짜보았습니다. 그 서늘한 결과 성적표는 Figure 5.4의 왼쪽 차트에 걸려있습니다.

LOOCV has the potential to be expensive to implement, since the model has to be fit $n$ times. This can be very time consuming if $n$ is large, and if each individual model is slow to fit. With least squares linear or polynomial regression, an amazing shortcut makes the cost of LOOCV the same as that of a single model fit! The following formula holds: 
물론 세상에 꽁짜는 없듯, 이 극찬받는 LOOCV 에도 무서운 청구서가 날아옵니다. 데이터가 100만 개라면 모델을 무려 100만 번($n$ 번) 이나 재부팅해서 처음부터 끝까지 풀 사이즈로 훈련(fit) 시켜야 합니다! 완전 미니 데이터가 아니면 서버 컴이 불타버리겠죠(expensive to implement). 하지만 여기서 소름 돋는 반전! 여러분이 만약 찌그러진 최소 제곱 통계망치(OLS 선형회귀 or 다항회귀) 를 쓰고 있다면, 모델을 100만 번 뺑뺑이 돌릴 필요 없이, 단 1번만 모델을 가동하고도 100만 번 돌린 LOOCV 점수를 그대로 복사해올 수 있는 **마법의 패스워드 지름길(amazing shortcut)** 수식이 존재합니다!

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \left( \frac{y_i - \hat{y}_i}{1 - h_i} \right)^2 \quad (5.2)
$$

![Figure 5.4](./img/5_4.png)

**FIGURE 5.4.** _Cross-validation was used on the_ `Auto` _data set in order to estimate the test error that results from predicting_ `mpg` _using polynomial functions of_ `horsepower` _._ Left: _The LOOCV error curve._ Right: 10 _-fold CV was run nine separate times, each with a different random split of the data into ten parts. The figure shows the nine slightly different CV error curves._ 
**FIGURE 5.4.** _`Auto` 데이터 주차장에 마력 곡선을 구겨 넣어 연비 테스트 오차를 추론하려고 나선 우리의 구원자 교차 검증(CV) 형님들입니다._ 왼쪽 차트: _누구도 의심 못 할 철통방어, LOOCV(1명 빼기 뺑뺑이) 에러 곡선._ 오른쪽 차트: _이번엔 반을 10조각 내서 조장들 뺑뺑이를 돌리는 10-겹(10-fold) 타협안 CV를 돌린 건데, 파티션 무작위 나누기를 9번 갈아엎으며 그렸더니 살짝살짝 미세 잔떨림 곡선이 9가닥 생긴 그림입니다._

where $\hat{y}_i$ is the $i$th fitted value from the original least squares fit, and $h_i$ is the leverage defined in (3.37) on page 105. This is like the ordinary MSE, except the $i$th residual is divided by $1 - h_i$. The leverage lies between $1/n$ and $1$, and reflects the amount that an observation influences its own fit. Hence the residuals for high-leverage points are inflated in this formula by exactly the right amount for this equality to hold. 
위에 적힌 (5.2) 수식이 그 악마의 금서 공식입니다. $\hat{y}_i$ 는 단 1번 풀 훈련시킨 여러분 통계망치의 평범한 예언치입니다. 그리고 밑에 깔린 $h_i$ 란 놈이 진짜 괴물인데, 옛날 105페이지에서 잠깐 눈팅했던 그 기득권 파워 '레버리지(leverage)' 입니다. 가만 보면 그냥 흔해 빠진 에러 스코어(MSE)를 구하는 꼴인데, 오답 판별치(잔차) 녀석의 다리를 슬쩍 $1 - h_i$ 방패로 쳐서 나눠버렸죠? 레버리지 녀석의 수치는 0~1 근방에 서식하면서, "이 관측치 놈 하나가 전체 회귀선을 지 맘대로 뒤틀고 휘두르는 파워(influences)"를 측정해둔 특권 점수입니다. 권력이 쎈 고-레버리지 왕따 관측치놈들은 자기가 유배됐을 땐 엄청난 오답을 유발할 거라서, 이 마법 공식이 알아서 $1 - h_i$ 몫으로 오답 뺨 데미지를 훅 뻥튀기시켜 올려줍니다(inflated). 그 부풀리는 비율이 진짜 소름 돋게도 $n$번 실제로 노가다를 돌린 값이랑 수학적으로 완벽히 똑같게(equality) 설계되어 버린 거죠!

LOOCV is a very general method, and can be used with any kind of predictive modeling. For example we could use it with logistic regression or linear discriminant analysis, or any of the methods discussed in later chapters. The magic formula (5.2) does not hold in general, in which case the model has to be refit $n$ times. 
이 무친 LOOCV 뺑뺑이 작전은 선형회귀뿐 아니라, 나선환이든 뭐든 뒤에 배울 어떤 머신러닝 무기를 쓰더라도(predictive modeling) 깡패처럼 다 범용적으로 들어붙습니다. 로지스틱 회귀나 분류망치 LDA 에도 멋지게 호환되죠. 단지, 위에서 찬양했던 그 '단 1번 만에 끝내는 치트키 마법 수식 (5.2)' 은 선형망치 외의 딴 머신을 굴릴 땐 통하지 않습니다! (does not hold). 그럴 땐 꼼수 없이 얌전히 당신 컴퓨터 쿨러 터지도록 진짜로 $n$ 번을 풀 재가동 인코딩(refit) 돌리셔야만 합니다. 애도.
