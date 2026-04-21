---
layout: default
title: "trans2"
---

# _5.1.2 Leave-One-Out Cross-Validation_ 
# _5.1.2 단 하나만 희생한다: 단일 관측치 제외 교차 검증 (LOOCV)_

_Leave-one-out cross-validation_ (LOOCV) is closely related to the validation set approach of Section 5.1.1, but it attempts to address that method’s drawbacks. 
_단일 관측치 제외 교차 검증(LOOCV)_ 기법은 방금 우리가 씹고 뜯었던 그 무식한 반반 무 많이 쪼개기 전략인 '검증 세트 접근법'과 사촌 지간입니다. 하지만 이 녀석은 앞선 녀석이 남긴 끔찍한 부작용(결과의 널뛰기와 훈련 데이터의 심각한 결핍)을 철저하게 타파하기 위한 무기로 탄생했습니다.

Like the validation set approach, LOOCV involves splitting the set of observations into two parts.
물론 이 녀석도 시작은 다른 기법들과 비슷합니다. 우리의 데이터를 훈련시킬 병력과, 테스트할 희생양으로 무조건 두 갈래로 나눕니다. 

However, instead of creating two subsets of comparable size, a single observation ( _x_ 1 _, y_ 1) is used for the validation set, and the remaining observations _{_ ( _x_ 2 _, y_ 2) _, . . . ,_ ( _xn, yn_ ) _}_ make up the training set.
그런데 파격적인 지점은 여기서 나옵니다. 데이터를 무식하게 5:5로 쪼개서 병력의 절반을 날려 먹는 대신, **딱 1명(단 하나의 관측치) 만을 불행하게 지목하여 '검증용 감옥'에 가둬 희생양**으로 던지고, 나머지 n-1명이라는 거대한 전원 병력을 오롯이 모델 훈련에 전부 때려 박습니다!

The statistical learning method is fit on the _n −_ 1 training observations, and a prediction _y_ ˆ1 is made for the excluded observation, using its value _x_ 1.
이렇게 압도적인 물량인 _n −_ 1 명의 데이터를 다 먹어치우며 훈련을 마친 똑똑해진 모델은, 아까 혼자 지하실에 갇혀있던 불쌍한 1명( _x_ 1) 의 특성값을 보고 이 녀석이 도대체 정답이 무엇일지(예측값 _y_ ˆ1) 를 맞혀 보려는 처절한 진검승부를 치릅니다.

Since ( _x_ 1 _, y_ 1) was not used in the fitting process, $\text{MSE}_1$ = ( _y_ 1 _− y_ ˆ1)[2] provides an approximately unbiased estimate for the test error.
그 가혹한 감옥에 갇혀있던 희생양 1번 ( _x_ 1 _, y_ 1) 데이터는 무대가 끝날 때까지 단 한 번도 모델에게 얼굴을 비춘 적 없이 철저히 배제(not used) 되었기 때문에, 이 1명을 상대로 뱉어낸 에러 점수 공식 $\text{MSE}_1$ 은 (비록 한 명 상대로 잰 거지만) 어쨌든 편향이 덜 묻은 깨끗한 실전 모의고사 점수가 됩니다.

But even though $\text{MSE}_1$ is unbiased for the test error, it is a poor estimate because it is highly variable, since it is based upon a single observation ( _x_ 1 _, y_ 1). 
하지만 함정이 있습니다! 이 $\text{MSE}_1$ 점수는 너무나 큰 치명타가 있죠. 단 딱 1명의 예외적 특성에만 의존해 평가를 내려버렸기 때문에 이 단 한 번의 점수로는 변동성이 미친 듯이 날뛰어 도저히 믿을 수 없는 엉망진창(poor) 인 성적표라는 겁니다.

We can repeat the procedure by selecting ( _x_ 2 _, y_ 2) for the validation data, training the statistical learning procedure on the _n −_ 1 observations ˆ _{_ ( _x_ 1 _, y_ 1) _,_ ( _x_ 3 _, y_ 3) _, . . . ,_ ( _xn, yn_ ) _}_ , and computing $\text{MSE}_2$ = ( _y_ 2 _−y_ 2)[2] .
그래서 통계학자들은 악마적인 아이디어를 냅니다. **"아, 그래? 그럼 1번을 감옥에 보냈던 걸 무효로 하고, 이번엔 2번만 감옥에 가두고 나머지 전원을 또다시 훈련시켜서 또 맞혀볼까?"** 즉, 두 번째 관측치를 다시 나홀로 희생양으로 삼고 나머지(1번 포함) 가 모조리 다시 훈련에 들어간 뒤 $\text{MSE}_2$  를 만들어 봅니다.

Repeating this approach _n_ times produces _n_ squared errors, $\text{MSE}_1$ _, . . . ,_ MSE _n_ .
이 잔혹한 서바이벌을 총 인원수(n명) 만큼 일일이 한 번씩 다 돌아가며 감옥에 가두는 짓거리(n번 반복) 를 저지르면, 우리는 n개의 피 터지는 $\text{MSE}_1$ 부터 MSE _n_ 에 이르는 낱개의 에러 조각들을 얻게 됩니다.

The LOOCV estimate for the test MSE is the average of these _n_ test error estimates: 
이렇게 개고생해서 얻어낸 이 n명의 단독 에러 파편들을 싹 다 긁어모아 공평하게 합치고 평균을 낸 궁극의 값이, 바로 우리가 그토록 찾아 헤매던 실전 테스트 MSE가 되는 것입니다:

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \text{MSE}_i \quad (5.1)
$$

**FIGURE 5.3.** _A schematic display of LOOCV. A set of n data points is repeatedly split into a training set (shown in blue) containing all but one observation, and a validation set that contains only that observation (shown in beige). The test error is then estimated by averaging the n resulting MSEs. The first training set contains all but observation 1, the second training set contains all but observation 2, and so forth._ 
**FIGURE 5.3.** _LOOCV의 잔혹한 뺑뺑이 구조입니다. 파란색 집단은 다 함께 훈련 중인 병력이고, 단 한 명의 베이지색 녀석만 외딴 검증용 감옥에 격리되어 있습니다. 첫판엔 1번을, 두 번째 판엔 2번을 버리는 식으로 이 뺑뺑이를 인원수만큼 돌려버리고, 나중에 이걸 다 합쳐 평균을 내어 진짜 에러율의 궤적을 짐작합니다._ 

A schematic of the LOOCV approach is illustrated in Figure 5.3. 
LOOCV가 작동하는 이런 살벌한 방식이 그림 5.3에 도해로 나와 있죠.

LOOCV has a couple of major advantages over the validation set approach.
이 LOOCV 기법은 예전에 무식하게 반으로 쪼개던 단순 기법보다는 압도적이고 엄청난 이점 두 가지를 손에 쥡니다.

First, it has far less bias.
**첫째, 편향(bias) 이 거의 사라집니다!** 

In LOOCV, we repeatedly fit the statistical learning method using training sets that contain _n −_ 1 observations, almost as many as are in the entire data set.
LOOCV 구장에서는, 모델을 한 번 훈련시킬 때 무려 전체 인원수에서 딱 한 명 빠진(_n −_ 1) 막강한 거대 병력을 꾸려서 투입시킵니다. 즉 전체 데이터 덩치 거의 100% 흡사한 녀석을 모조리 구겨 너어 공부시키는 대규모 학원이 열리는 겁니다.

This is in contrast to the validation set approach, in which the training set is typically around half the size of the original data set.
이는 예전 방식에서 모델 짬밥을 강제로 절반으로 굶겨 축소시키던 무식한 짓과 완벽하게 대조됩니다.

Consequently, the LOOCV approach tends not to overestimate the test error rate as much as the validation set approach does.
결과적으로, 이 LOOCV로 훈련된 녀석은 학습량이 충분해 엄청 똑똑하기에 "아 나 이거밖에 점수 안 나와..." 라며 실제 오차보다 엉망으로 숫자를 무참하게 깎아내려 **과대평가(overestimate)** 하는 끔찍한 족쇄 경향을 지니지 않게 됩니다!

Second, in contrast to the validation approach which will yield different results when applied repeatedly due to randomness in the training/validation set splits, performing LOOCV multiple times will always yield the same results: there is no randomness in the training/validation set splits. 
**둘째, 로또 운(무작위성)의 장난이 완벽하게 사라집니다!** 단순 반반 분할 때는 컴퓨터 난수 스위치에 따라 재수 없게 극단적인 녀석만 모이거나 하는 등 돌릴 때마다 결과가 요동쳤었죠? 하지만 LOOCV는 전원을 순서대로 한 번씩 돌아가면서 똑같이 감옥에 가둬 공평하게 피를 보기 때문에(무작위성 제로), 천 번 만 번을 다시 돌려도 **소름 돋게 늘 똑같은 결과**만 딱 떨어지게 됩니다!

We used LOOCV on the `Auto` data set in order to obtain an estimate of the test set MSE that results from fitting a linear regression model to predict `mpg` using polynomial functions of `horsepower` .
우리는 `horsepower` 파워 기운을 척도로 삼아 연비 `mpg` 를 점쳐보려는 선형 모델을 짰을 때 과연 실전 성능과 오차가 어떻게 나올지 알아보기 위해, 직접 `Auto` 자동차 데이터 세트를 구장에 투입해 이 LOOCV 서바이벌 게임을 거칠게 돌려보았습니다.

The results are shown in the left-hand panel of Figure 5.4. 
그 놀라운 결과치가 저 그림 5.4 좌측에 박혀 있습니다.

LOOCV has the potential to be expensive to implement, since the model has to be fit _n_ times.
**하지만 세상에 공짜 구원은 없죠.** LOOCV는 이 무지막지한 짓(어마어마한 병력을 밀어 넣기)을 전체 인원수 n번만큼 뺑뺑이 돌려 다시 훈련(fit) 시켜 고생해야만 하기에, 연산 비용이 그야말로 억소리나게 비싸게 깨져서(expensive) 슈퍼컴퓨터도 뻗어버릴 잠재적 병폐가 있습니다.

This can be very time consuming if _n_ is large, and if each individual model is slow to fit.
만약 구성 인구 n명이 백만 명 규모 단위로 치솟고, 한 번 훈련하는 데도 무거워서 등골 빠지는 복잡한 모델 구조를 썼다면? 이 뺑뺑이에 소모되는 자원 비용(time consuming)은 시간 낭비의 재앙급이 될 수 있습니다.

With least squares linear or polynomial regression, an amazing shortcut makes the cost of LOOCV the same as that of a single model fit!
그런데 통계학자들의 마법은 끝이 없습니다! 놀랍게도 만일 당신의 주 무기가 고전적인 최소 제곱 베이스의 '선형 회귀' 나 '다항 회귀' 식이라면, 아주 기가 막힌 꼼수(경이로운 수학 지름길) 공식 덕에 수만 번 모델을 재건축해야 하는 LOOCV 비용을 **"단 한 번 모델 학습시키는 비용"과 정확히 동일한 속도**로 뭉개버리는 기적을 발동시킵니다!!

The following formula holds: 
바로 아래의 역학 방정식 마법 카드가 성립하거든요:

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \left( \frac{y_i - \hat{y}_i}{1 - h_i} \right)^2 \quad (5.2)
$$

![Figure 5.4](./img/5_4.png)

**FIGURE 5.4.** _`Auto` 데이터 세트에서 연비를 예상해 보려 할 때 터져 나오는 실전 테스트 오차 타율들을, 교차 검증이라는 무기를 덧대어 실증 타진 평가해 낸 성적표 도표입니다._ 좌측: _n번 뺑뺑이를 돌려 나온 깔끔한 LOOCV 단일 에러 커브입니다._ 우측: _이것은 나중에 속성반으로 곧 배울 10-Fold 방식을 각각 다르게 랜덤 섞어서 9번 찍어 그려본 여러 갈래 에러 굴곡선입니다._

where _y_ ˆ _i_ is the _i_ th fitted value from the original least squares fit, and _hi_ is the leverage defined in (3.37) on page 105.[1]
이 흑마법(마법 연산 수식) 안에서 _y_ ˆ _i_ 는 전체를 다 털어놓고 한방에 훈련시킨 최소 제곱 라인에서 나온 적합 푯값이고, _hi_ 는 저 멀리 105페이지 (3.37) 단락에서 살펴봤던 그 악명높은 권력 지표 **레버리지(leverage)** 입니다.[1]

This is like the ordinary MSE, except the _i_ th residual is divided by 1 _− hi_ .
이 공식 구조를 슬쩍 보세요. 그냥 우리가 뻔히 쓰던 기존 일반 MSE 점수 내는 공식에서 딱 하나, _i_ 번째 잔차 밑바닥에 $1 - h_i$ 로 한 번 나눠 쳐내는 필터 마법만 하나 들어간 채로 평범하게 생겼습니다. 이게 요술을 부리죠.

The leverage lies between 1 _/n_ and 1, and reflects the amount that an observation influences its own fit.
이 레버리지란 스펙은 기본적으로 1 _/n_ 에서 1 수치까지 권력 띠를 형성하는데, 특정 녀석 하나가 전체 여론 모델 선 긋기 형성 과정에 얼마나 막강하게 조폭 두목처럼 자기 지분을 반영해 흔들어댔는지(influences) 그 힘의 위력을 뽐내는 지표잖아요?

Hence the residuals for high-leverage points are inflated in this formula by exactly the right amount for this equality to hold. 
참으로 절묘하게도, 이 수식 체계 아래에선 권력이 높았던 녀석(레버리지가 높은 위험인물)이 뱉어낸 에러 수치들은, 스스로가 저질렀을지도 모를 분탕질을 정확히 상쇄하도록 방정식 공식 안에서 교묘하게 뻥튀기 부풀려져(inflated) 그 1번씩 뺑뺑이 빼고 돌린 n번 고생한 결과치 수식 항등식을 단번에 똑같이 조율 보정해 줍니다. 

LOOCV is a very general method, and can be used with any kind of predictive modeling.
정리하자면 LOOCV 뺑뺑이는 통계학 전투에서 극강의 범용 무기입니다, 당신이 맞닥뜨릴 상상도 못 할 그 어떤 희귀한 예측 모델링 전투 장비에서도 아주 무난히 활용 가능한 슈퍼 범용 호환 칩이죠.

For example we could use it with logistic regression or linear discriminant analysis, or any of the methods discussed in later chapters.
예컨대 훗날 다룰 악명 높은 로지스틱 회귀 돌파 장치나 선형 판별 분석 요격 무기 등, 무슨 짓과 조합해도 다 매끄럽고 신명 나게 연동(used) 됩니다.

The magic formula (5.2) does not hold in general, in which case the model has to be refit _n_ times. 
다만 딱 한 가지 몹시 가슴 아픈 통곡의 사실이 있다면... 아까 칭송한 저 '요술 꼼수 1번 돌리기 연산 수식 (5.2)' 마법 카드는, 일반 선형 장르 구역을 벗어난 타 험난한 특수 장비 결합 사안들 앞에서는 일반적으로 **약발이 전혀 돌지 않습니다(does not hold).** 그래서 만약 그런 다른 복잡한 모델로 무장하셨다면 어쩔 수 있나요, 깡통 컴퓨터가 뻗지 않길 기도하며 억울하게 **n번씩 모델을 밤새 처음부터 끝까지 완전 재연마(refit)시키는 막노동 절벽**을 직접 굴러야만 버틸 수 있는 무서운 체력전의 굴레를 안고 있기도 합니다.
