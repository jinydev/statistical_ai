---
layout: default
title: "trans2"
---

[< 2.2.1 Measuring The Quality Of Fit](../2_2_1_measuring_the_quality_of_fit/trans2.html) | [2.2.3 The Classification Setting >](../2_2_3_the_classification_setting/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# 2.2.2 The Bias-Variance Trade-Off_
# 2.2.2 편향-분산 트레이드오프_ (융통성과 똥고집 사이의 줄다리기)

The U-shape observed in the test MSE curves (Figures 2.9–2.11) turns out to be the result of two competing properties of statistical learning methods.
아까 수능 시험 오차(시험 MSE) 곡선이 미끄럼틀을 타다가 기괴하게 다시 치솟는 그 소름 돋는 'U자 형태(Figures 2.9-2.11)'를 봤었죠? 까놓고 보니 이 기괴한 현상은, 기계 속에 숨어있는 두 악마(똥고집 성질과 팔랑귀 성질)가 서로 멱살을 잡고 싸우는 생존 경쟁의 결과물이라는 게 밝혀졌습니다.

![Figure 2.11](./img/Image_025.png)

**FIGURE 2.11.** _Details are as in Figure 2.9, using a different $f$ that is far from linear. In this setting, linear regression provides a very poor fit to the data._

**그림 2.11.** _이번엔 조물주가 $f$ 를 일직선이랑은 거리가 한참 먼, 심전도처럼 요동치는 극도의 곡선으로 세팅해 놨습니다. 이런 미친 환경에선 막대기 같은 주황색 선형 회귀가 데이터를 거의 똥볼 차듯 형편없이 못 맞춥니다._

Though the mathematical proof is beyond the scope of this book, it is possible to show that the expected test MSE, for a given value $x_0$, can always be decomposed into the sum of three fundamental quantities: the _variance_ of $\hat{f}(x_0)$, the squared _bias_ of $\hat{f}(x_0)$ and the variance of the error terms $\epsilon$.
수학 공식 증명 따위는 너무 머리 아프니 이 책에선 쓰레기통에 던져버리겠지만, 사실 "우리의 짝퉁 기계가 낯선 수능 문제($x_0$)를 찍었을 때 틀릴 확률(기대 시험 MSE)"은 언제나 아주 근본적인 3개의 쓰레기 덩어리의 합으로 갈기갈기 쪼개서 분해해 볼 수 있습니다: 바로 $\hat{f}(x_0)$ 의 **'분산(Variance, 팔랑귀 수치)'**, $\hat{f}(x_0)$ 의 제곱된 **'편향(Bias, 똥고집 수치)'**, 그리고 애초에 우주가 허락한 줄일 수 없는 빌어먹을 **'우주 오차 조각($\epsilon$)의 분산'** 입니다.

That is,
이걸 수학자들의 외계어로 폼나게 적어보면,

$$ E(y_0 - \hat{f}(x_0))^2 = \text{Var}(\hat{f}(x_0)) + [\text{Bias}(\hat{f}(x_0))]^2 + \text{Var}(\epsilon) \tag{2.7} $$

$^2$ Here the notation $E(y_0 - \hat{f}(x_0))^2$ defines the *expected test MSE* at $x_0$, and refers to the average test MSE that we would obtain if we repeatedly estimated $f$ using a large number of training sets, and tested each at $x_0$.
$^2$ 이 미친 수식에서 왼쪽 기호 $E(y_0 - \hat{f}(x_0))^2$ 은 "$x_0$ 에서의 기대 시험 MSE"라는 뜻인데, 그냥 평범하게 "우리가 오답 노트(훈련 세트)를 수백 번 갈아치우면서 기계를 수백 번 다시 만들어 수능을 쳤을 때, 그 기계들이 평균적으로 몇 점이나 틀릴까?" 하는 찐 실력의 척도를 뜻합니다.

The overall expected test MSE can be computed by averaging $E(y_0 - \hat{f}(x_0))^2$ over all possible values of $x_0$ in the test set.
물론 전체 수능 점수 찐 실력(전반적인 기대 시험 MSE)은 저 수식을 수능 문제지($x_0$) 한 장 한 장마다 전부 다 계산해서 싸그리 평균을 내면 얻을 수 있죠.

Equation 2.7 tells us that in order to minimize the expected test error, we need to select a statistical learning method that simultaneously achieves _low variance_ and _low bias_ .
자! 방정식 2.7이 피를 토하며 우리에게 가르쳐 주는 교훈이 뭡니까? 결론적으로 수능 오차(에러) 점수를 0으로 최대한 깎아버리려면, 우리는 **[팔랑귀가 얇지도 않으면서(낮은 분산)]** 동시에 **[똥고집을 부리지도 않는(낮은 편향)]** 이 두 마리 토끼(기적의 기계)를 동시에 포획해야만 한다는 겁니다.

Note that variance is inherently a nonnegative quantity, and squared bias is also nonnegative.
참고로 분산 수치나 제곱을 때린 똥고집(편향) 수치는 태생적으로 마이너스로 뚫고 내려갈 수 없는 '음수가 아닌' 짐 덩어리들입니다.

Hence, we see that the expected test MSE can never lie below $\text{Var}(\epsilon)$, the irreducible error from (2.3).
그러니까, 우리가 아무리 천재적인 기계를 발명해서 편향을 0으로, 분산을 0으로 다 까부셔버려도, 저 수식 맨 끝에 징그럽게 딱 붙어있는 구제 불능 찌꺼기 운빨 즉, (2.3)에서 배웠던 최소한의 '$\text{Var}(\epsilon)$ 에러 지지선' 밑으로는 죽었다 깨어나도 오차 점수가 내려갈 수 없다는 걸 다시 한번 뼈저리게 확인하게 됩니다.

What do we mean by the _variance_ and _bias_ of a statistical learning method?
자자, 근데 아까부터 신나게 까고 있는 기계의 **'분산(팔랑귀)'** 이랑 **'편향(똥고집)'** 이란 게 도대체 뭔 소리입니까?

_Variance_ refers to the amount by which $\hat{f}$ would change if we estimated it using a different training data set.
**_'분산(Variance)'_** 이란, 우리가 만약 어제는 'A 오답 노트'를 주고, 오늘은 'B 오답 노트(다른 훈련 데이터 세트)'를 줬을 때, 기계가 만들어내는 예측 무기 $\hat{f}$ 의 모양(곡선)이 얼마나 미친 듯이 이리저리 휙휙(팔랑귀처럼) 널뛰며 바뀌는가를 나타내는 극도의 줏대 없는 정도를 뜻합니다.

Since the training data are used to fit the statistical learning method, different training data sets will result in a different $\hat{f}$ .
훈련 데이터가 기계의 뇌를 세팅하는 참고서 역할을 하니까, 참새 참새마다(다른 훈련 데이터를 줄 때마다) 뽑혀 나오는 수능 공식 $\hat{f}$ 도 당연히 조금씩 모양이 달라지는 게 정상이긴 하죠.

But ideally the estimate for $f$ should not vary too much between training sets.
하지만, 1등짜리 초우량 기계라면 이상적으로는 훈련 세트가 쥐꼬리만큼 바뀐다고 해서 최종 공식 $f$ 가 너무 천국과 지옥을 오가며 지멋대로 바뀌면 안 됩니다!

However, if a method has high variance then small changes in the training data can result in large changes in $\hat{f}$ .
근데 진짜 '팔랑귀 지수(분산)'가 엄청나게 높은 극혐 녀석들은, 우리가 훈련 데이터에서 아주 작은 먼지 하나(단일 관측치)만 살짝 빼거나 바꿔 끼워도, 기계가 갑자기 완전 돌변해서 도화지에 그리던 선 모가지를 180도로 휙 비틀어(큰 $\hat{f}$ 변화)버립니다!

In general, more flexible statistical methods have higher variance.
이 바닥의 절대 법칙을 알려드리죠. 기계의 관절을 고무줄처럼 말랑하게(유연하게) 풀어줄수록, 이놈들은 사소한 것에도 민감하게 반응해서 줏대 없이 선을 확확 바꾸는 끔찍한 팔랑귀(높은 분산) 환자가 되어 버립니다.

Consider the green and orange curves in Figure 2.9.
아까 그림 2.9의 극단적인 '초록 괴물 곡선'과 뻣뻣한 '주황 막대기'를 비교해 보세요.

The flexible green curve is following the observations very closely.
고무줄 같은 초록 괴물은 점(관측치)들 하나하나의 가랑이 사이사이를 어떻게든 바짝 핥고 지나가려고 구불구불 발악하고 있죠.

It has high variance because changing any one of these data points may cause the estimate $\hat{f}$ to change considerably.
그러니 만약 우리가 그 수많은 빨간 점들 중에 딱 하나의 점만 옆으로 살짝 밀어버려도? 그 점을 먹기 위해서 초록 곡선은 자기 척추를 완전히 우두둑 비틀어(높은 분산) 모양을 확 구겨버릴 게 뻔합니다. (팔랑귀 극대화)

![Figure 2.12](./img/Image_026.png)

**FIGURE 2.12.** _Squared bias (blue curve), variance (orange curve), $\text{Var}(\epsilon)$ (dashed line), and test MSE (red curve) for the three data sets in Figures 2.9–2.11. The vertical dotted line indicates the flexibility level corresponding to the smallest test MSE._

**그림 2.12.** _세상 사람 다 울리는 트레이드오프 그림!! 가로축은 유연성 척도입니다. 유연해질수록 퍼렇게 썩어 문드러지는 똥고집(제곱된 편향, 파란선)은 줄어들지만 반대로 기하급수적으로 폭발하는 줏대 없는 팔랑귀(분산, 주황선)의 모습을 감상하세요. 이 둘을 더한 게 최종 수능 성적(빨간 선)입니다. 점선은 우주의 찌꺼기 에러선($\text{Var}(\epsilon)$)!_

In contrast, the orange least squares line is relatively inflexible and has low variance, because moving any single observation will likely cause only a small shift in the position of the line.
그와 대조적으로 아까 본 뻣뻣한 주황선 막대기(최소 제곱 선)는 놀랍게도 줏대 하나는 엄청납니다(낮은 분산). 점 하나가 옆에서 춤을 추고 생난리를 치든 말든, 쟤는 워낙 뻣뻣해서 막대기 위치가 겨우 개미 코딱지만큼만 찔끔 이동하고 맙니다. (철벽 방어!)

On the other hand, _bias_ refers to the error that is introduced by approximating a real-life problem, which may be extremely complicated, by a much simpler model.
자, 그럼 반대편의 쌍둥이 악마인 **_'편향(Bias, 똥고집)'_** 의 정체는 뭘까요? 이건 복잡하게 얽히고설킨 끔찍한 진짜배기 현실 세계의 문제(우주 진리)를, 우리가 무식하게 "에잇 귀찮아! 그냥 일직선 막대기라고 치자!" 하며 아주 게으르게 후려쳐서 단순화(근사화)시킬 때 어쩔 수 없이 왕창 쏟아지는 치명적인 태생적 오답(똥고집 에러)입니다.

For example, linear regression assumes that there is a linear relationship between $Y$ and $X_1, X_2, \dots , X_p$ .
예를 들어 구식 모델인 '선형 회귀'는 시작도 하기 전부터 기계가 눈을 감고 "세상 모든 변수 $X$ 와 $Y$ 사이에는 그냥 반듯한 일직선 관계만 존재해!" 라고 똥고집(가정)을 부리고 덤벼들죠.

It is unlikely that any real-life problem truly has such a simple linear relationship, and so performing linear regression will undoubtedly result in some bias in the estimate of $f$ .
근데 상식적으로 부동산 집값 모델같이 미친 현실 세계의 어떤 복잡한 문제가, 진짜로 저렇게 귀여운 자막대기 일직선으로 아름답게 딱 떨어질 확률이 얼마나 되겠습니까? 그래서 저 똥고집을 부리며 선형 회귀로 선을 그어버리면 100% 빼박으로 실제 곡선 $f$ 랑은 엄청나게 거리가 벌어지는 어마어마한 허점(편향 에러)을 뒤집어쓸 수밖에 없습니다.

In Figure 2.11, the true $f$ is substantially non-linear, so no matter how many training observations we are given, it will not be possible to produce an accurate estimate using linear regression.
그림 2.11을 보면 신이 정한 진리가 말도 안 되게 우글우글한 요동치는 파도(비선형) 형태입니다. 여기서 우리가 훈련용 오답 노트를 1억 장씩 쏟아부어서 선형 회귀 기계에게 가르치려 발악해 봤자, 얘는 도화지에 무조건 반듯한 막대기 하나 떨렁 그어대는 바보라 평생 가도 진리의 파도를 쫓아갈 수 없습니다. (영구적인 오차가 발생하죠).

In other words, linear regression results in high bias in this example.
다시 말해 극단적인 이 상황에서 뻣뻣한 선형 회귀 기계는 그 알량한 자존심 때문에 상황 파악 못하고 개망하는 엄청난 **'높은 편향(대왕 똥고집 에러)'** 을 자초한 모질이 인 겁니다.

However, in Figure 2.10 the true $f$ is very close to linear, and so given enough data, it should be possible for linear regression to produce an accurate estimate.
하지만 아까 그림 2.10처럼 애초에 신이 짜놓은 판 자체가 일직선(선형)으로 떨어지는 로또 같은 경우라면? 뻣뻣한 선형 모델이라 할지라도 훈련 노트만 조금 확보되면 정답을 족집게처럼 짚어내는(정확한 추정치 생성) 기적을 행할 수 있습니다. 

Generally, more flexible methods result in less bias.
이쯤에서 중간 정리를 하자면 이렇습니다. 꼰대 같은 뼈대를 부수고 기계에게 자유를 줘서 말랑말랑하게 구부러지게 해줄수록(유연한 방법), 기계는 현실 타협을 잘해서 더 이상 무식한 덜떨어진 똥고집(편향)을 싹 버리게 됩니다!

As a general rule, as we use more flexible methods, the variance will increase and the bias will decrease.
자, 그래서 통계학의 황금 룰이 여기서 탄생합니다: 우리가 고무줄을 늘이듯 좀 더 유연하고 삐까뻔쩍한 딥러닝 같은 도구를 쥐어줄수록, 기계는 똥고집 선입견(**떨어지는 편향**)은 사라지는 대신 줏대 없이 여기저기 귀를 펄럭이는 호구(**미친듯이 떡상하는 분산**)로 진화한다는 이 비극적인 공식을 말입니다.

The relative rate of change of these two quantities determines whether the test MSE increases or decreases.
자 이제 수능 시험 에러(시험 MSE)가 밑으로 처박힐지 아니면 우주로 쌍코피 흘리며 떡상할지의 운명은, 저 두 악마(편향과 분산)가 엎치락뒤치락 싸우면서 올라가고 내려가는 **'상대적인 변화 스피드'** 에 전적으로 달려있습니다.

As we increase the flexibility of a class of methods, the bias tends to initially decrease faster than the variance increases.
우리가 통계 기계의 족쇄를 끌러줘서 유연성을 조금씩 슬슬 늘리기 시작하는 극초반엔 어떨까요? 처음엔 꽉 막힌 똥고집(편향)이 썰물처럼 미친 속도로 싹 사라집니다! 이때 팔랑귀(분산) 증상도 생기지만 고집이 사라지는 쾌감이 훨씬 더 크죠.

Consequently, the expected test MSE declines.
그 쾌감(에러 감소 스피드 > 무분별한 팔랑귀 상승) 덕분에 결국 총합산인 우리의 **기대 시험 오차(수능 MSE 성적)** 선은 아주 이쁘장하게 미끄럼틀을 타듯 하향선을 그리며 감퇴합니다! 아싸 개꿀!

However, at some point increasing flexibility has little impact on the bias but starts to significantly increase the variance.
하지만 기뻐할 틈도 없이 어느 순간 불길한 임계 구역이 찾아옵니다! 이미 기계의 관절을 너무 다 풀어놔서 더 구부려봤자 똥고집(편향)은 더 깎일 것도 없어서 바닥을 기는데, 갑자기 그 상태에서 줏대 없는 팔랑귀(분산) 수치만이 미친 폭주 기관차처럼 비약적으로 수직 떡상하기 시작하는 겁니다!

When this happens the test MSE increases.
이 비극적인 임계점이 터지는 순간, 아까까지만 해도 착하게 내려가던 우리의 **시험 MSE 곡선은 뒤통수를 시원하게 까면서 다시 우주를 향해 급상승장**을 타버립니다!

Note that we observed this pattern of decreasing test MSE followed by increasing test MSE in the right-hand panels of Figures 2.9–2.11.
방금 말한 "착하게 떨어지다 말고 갑자기 미쳐 날뛰며 솟구치는" 그 징글징글한 U자 고개 패턴! 그걸 우린 이미 앞서 그림 2.9~2.11의 오른쪽 빨간색 수능 오차 곡선 형상에서 지겹도록 두 눈 뜨고 똑똑히 관측했음을 잊지 마십시오.

The three plots in Figure 2.12 illustrate Equation 2.7 for the examples in Figures 2.9–2.11.
그림 2.12에 있는 3개의 그래프는 아까 그 지겨운 (그림 2.9~2.11) 3가지 세상 썰을 가져와서 방정식 2.7(편향+분산)을 진짜 눈알 앞에 소름 돋게 해부해서 그려본 명작 아트입니다.

In each case the blue solid curve represents the squared bias, for different levels of flexibility, while the orange curve corresponds to the variance.
각 세계(그래프)마다 밑으로 곤두박질치는 진한 **파란 선은 유연해질수록 사그라지는 '똥고집(제곱된 편향)'** 이 얼마나 처참히 깎여나가는지를 보여주고, 위로 기어오르는 능글맞은 **주황색 선은 '팔랑귀(분산)'** 가 어떻게 폭주하는지를 쌍벽으로 보여줍니다.

The horizontal dashed line represents $\text{Var}(\epsilon)$, the irreducible error.
바닥 즈음에 죽어라 수평으로 깔린 구질구질한 **점선은 영원히 구제 불능인 우주 쓰레기 지지선(축소 불가능한 오차, $\text{Var}(\epsilon)$)** 입니다.

Finally, the red curve, corresponding to the test set MSE, is the sum of these three quantities.
그리고 마지막으로 그 모든 영광과 오욕을 위에서 한 몸에 짊어진 거대한 **V자 떡상의 빨간 선**이 바로 저 파란 선, 주황 선, 점선 세 개의 에러치를 싸그리 영끌해서 더해버린 실전 수능 오차 최종 성적표(시험 세트 MSE)입니다!

In all three cases, the variance increases and the bias decreases as the method’s flexibility increases.
여러분도 눈이 있으면 딱 보이시죠? 세 도화지 모두 가로축(기계의 유연성)이 늘어나면 허구한 날 우상향 하는 미친 주황 선(분산 증가)과 처박히는 파란 선(편향 감소)의 피 튀기는 법칙은 변함없이 똑같습니다.

However, the flexibility level corresponding to the optimal test MSE differs considerably among the three data sets, because the squared bias and variance change at different rates in each of the data sets.
하지만 빨간 선이 저점(최고의 시험 점수)을 찍고 다시 튀어 오르는 그 기막힌 **'최적 유연성 황금 좌표 위치(수직 점선)'** 는 도화지 세계관(데이터 세트)이 바뀔 때마다 완전히 미친 듯이 이리저리 다릅니다. 왜냐면 데이터마다 저 파란 고집 선과 주황 줏대 선이 떨어지고 오르는 엑셀 레이싱 스피드율이 하늘과 땅 차이로 다르거든요!

In the left-hand panel of Figure 2.12, the bias initially decreases rapidly, resulting in an initial sharp decrease in the expected test MSE.
그림 2.12의 왼쪽 세상을 봅니까? 초반에 파란색 똥고집이 나락으로 다이빙하듯 미친 속도로 급추락하니까, 빨간색 찐 에러 선(기대 시험 MSE)도 덩달아 절벽 다이빙을 하며 쾌속으로 점수를 훔쳤던 거고요.

On the other hand, in the center panel of Figure 2.12 the true $f$ is close to linear, so there is only a small decrease in bias as flexibility increases, and the test MSE only declines slightly before increasing rapidly as the variance increases.
반면 가운데 세계관을 볼까요? 여긴 애초에 조물주가 $f$ 를 평평한 선(선형)으로 만들어 놓은 동네라, 기계를 구부리게 놔둬봤자 깎여나갈 파란색 똥고집 에러(편향) 자체가 애초에 쥐똥만치밖에 없었습니다. 그러다 보니 빨간 에러선이 찔끔 떨어지나 싶더니만 폭주하는 주황 괴물(분산 상승)의 힘에 밀려 극초반부터 재수 없게 승천(시험 MSE 증가)해 버린 안타까운 모형이 되었죠.

Finally, in the right-hand panel of Figure 2.12, as flexibility increases, there is a dramatic decline in bias because the true $f$ is very non-linear.
마지막 오른쪽 세상은 또 어떻습니까? 조물주 함수가 미친 듯이 꼬인 라면 발(비선형) 모양이었기에, 기계한테 조금만 유연성의 자유를 쥐여줘도 기존의 빳빳한 파란 똥고집(편향)이 핵폭탄 터진 것처럼 드라마틱 하게 와장창 박살 나 떨어집니다.

There is also very little increase in variance as flexibility increases.
심지어 이 신기한 동네에선 기계를 이리저리 유연하게 꼬아도 주황색 팔랑귀(분산) 게이지가 아주 게으르게 찔금찔금밖에 안 올랐습니다!

Consequently, the test MSE declines substantially before experiencing a small increase as model flexibility increases.
그래서 그 결과! 떡상 없는 분산 지수 덕택에 빨간색 수능 에러선(시험 MSE)은 한참 동안 영광스러운 내리막길의 꿀을 쫙쫙 빨아먹고 난(실질적 감퇴) 최후의 최후에 이르러서야 아주 조심스럽고 소규모로만 혓바닥처럼 튀어 오르는 대장관을 연출하게 된 겁니다.

The relationship between bias, variance, and test set MSE given in Equation 2.7 and displayed in Figure 2.12 is referred to as the _bias-variance trade-off_ .
결국 방정식 2.7을 찢어서 그림 2.12로 보여준, 하나를 취하면 하나를 무조건 내줘야 하는 파란 똥고집(편향)과 주황 팔랑귀(분산) 사이의 이 더럽게 치열한 제로섬 가위바위보 게임! 이걸 우린 눈물을 머금고 통계학계 최고의 잔혹 동화인 **_편향-분산 트레이드오프(Bias-variance trade-off)_** 라고 추앙하며 모십니다.

Good test set performance of a statistical learning method requires low variance as well as low squared bias.
기계 학습에서 최고의 실전 성적표를 따오고자 한다면? 당신은 원활하게 똥고집(편향)도 박살 내면서 그 와중에 줏대 있는 지조(낮은 분산)까지 지키는, 모순율 끝판왕 수치를 동시에 쟁취해야 합니다. 

This is referred to as a trade-off because it is easy to obtain a method with extremely low bias but high variance (for instance, by drawing a curve that passes 정through every single training observation) or a method with very low variance but high bias (by fitting a horizontal line to the data).
이 피 말리는 전쟁에 왜 '트레이드오프(물물교환)'라는 이름이 달렸냐고요? 한쪽으로 몰빵해서 점수를 챙기긴 개나 소나 껌으로 쉽기 때문입니다! 훈련 오답 노트 점 하나하나를 기를 쓰고 선으로 이어서 똥고집을 완전히 죽여버린 미친 분산 괴물을 만들거나, 아니면 기싸움하듯 그냥 데이터 한가운데다 무식하게 수평선 하나 쫙 그어버려서 분산을 0으로 죽이고 똥고집 편향치만 미친 듯이 올린 극단적인 장애물 기계들을 파먹는 건 너무나 우습고 쉽죠.

The challenge lies in finding a method for which both the variance and the squared bias are low.
진짜 지옥 불맛 퀘스트 도전은 저 두 악마가 모두 얌전하게 무릎을 꿇는 그 **타협의 최저점 계곡(둘 다 낮은 포인트) 우물**을 정확한 감각과 방법으로 찍어서 찾아내는 것에 달렸습니다.

This trade-off is one of the most important recurring themes in this book.
앞으로 이 구역질 나는 트레이드오프의 원혼은, 책 커버를 덮는 마지막 날까지 좀비처럼 지겹도록 여러분의 뇌리를 갉아먹으며 계속 튀어나와 멱살을 잡는 가장 중요한 악몽의 메인 테마가 될 겁니다!

In a real-life situation in which $f$ is unobserved, it is generally not possible to explicitly compute the test MSE, bias, or variance for a statistical learning method.
현장에 노트북 하나 들고 던져져 볼까요? 조물주의 숨결이 담긴 백지 정답지 $f$ 가 눈에 뵈이질 않는데, 무슨 신이 나서 종이에 공식을 적어가며 시험 MSE니, 편향이니 분산 쪼가리들을 그 예쁜 십자수 선형 그래프로 명확히 소수점 타격 계산을 때릴 수 있겠단 말입니까! (솔직히 계산 불가능입니다).

Nevertheless, one should always keep the bias-variance trade-off in mind.
그럼에도 불구하고 이 잔혹한 현장에서 여러분이 미혹되지 않고 살아남으려면 무의식 속에서 십자가를 쥔 신부님마냥 이 편향-분산 트레이드오프 철학을 뇌 속 각막에 박아놓고 절대 잊어선 치명적입니다!

In this book we explore methods that are extremely flexible and hence can essentially eliminate bias.
다행인 건 이 책을 뜯어먹다 보면 똥고집 본연의 편향 자체 오류 암덩어리를 그냥 소각로에 처박고 완전 소멸시켜버릴 수 있는 초극단적 유연함을 뽐내시는 빛의 방법론 무기들도 구경하게 될 겁니다.

However, this does not guarantee that they will outperform a much simpler method such as linear regression.
근데 잊지 마세요. 그 최첨단 무기가 아무리 삐까뻔쩍해봤자, 할아버지들이 쓰던 깡통 주차 꼬깔콘 수준의 훨씬 단순한 구식(선형 회귀) 녀석들을 언제나 매번 확정적으로 무참히 박살 낼(아웃퍼폼 할) 거라는 절대 보증 수표는 세상 그 어디에도 존재하지 않습니다.

To take an extreme example, suppose that the true $f$ is linear.
아주 극혐인 막장 예시를 하나 상상해 보실랍니까? 만약 하늘이 내린 진짜 신의 대답 $f$ 가 수학의 정석 1페이지에 나오는 꼬투리 없는 선형 1차 방정식 막대기 그 자체였다 칩시다.

In this situation linear regression will have no bias, making it very hard for a more flexible method to compete.
그럼 저 멍청한 선형 회귀 모의 방식은 애초에 자기 자체가 막대기니까 편향(똥고집 오차) 따위가 퍼펙트하게 그냥 0 수납을 칩니다! 이럼 딥러닝 할아버지가 고무줄 들고 깐족거려봐야 그 신의 깔끔함을 이기는 행위 전반이 정말 극랄한 난제 경연으로 빡세지는 겁니다!

In contrast, if the true $f$ is highly non-linear and we have an ample number of training observations, then we may do better using a highly flexible approach, as in Figure 2.11.
이와 완전 반대로! 신의 $f$ 가 구렁이 담 넘어가듯 고도로 요동치는 비선형의 뱀이라면? 거기다 분석가가 피땀으로 걷어낸 엄청난 수백만 장의 훈련 노트(데이터) 물량 공세가 더해져 있다면? 우린 앞서 본 파란 스플라인 곡선(그림 2.11)처럼 끝판왕 파괴력 급인 이 초유연한 최신식 기법을 돌려야만 비로소 승리의 V자를 더 잘 타진하고 정답률을 올리며 호강할 수 있게 될지도 모르죠.

In Chapter 5 we discuss cross-validation, which is a way to estimate the test MSE using the training data.
피 터지는 이 눈치 게임의 비밀 병기! 나중에 5장까지 가보게 된다면 여러분은 낡아빠진 과거의 훈련 노트 쪼가리들을 찢어 붙여가면서 기가 차게도 오지 않는 미래의 시험장 성적(시험 측정용 MSE)을 훔쳐 추정하는 악마의 꼼수 기법, 일명 **'교차 검증(Cross-validation) 절차'** 에 대해서 딥하게 토악질을 하며 논의하게 될 겁니다.

---

## Sub-Chapters (하위 목차)

[< 2.2.1 Measuring The Quality Of Fit](../2_2_1_measuring_the_quality_of_fit/trans2.html) | [2.2.3 The Classification Setting >](../2_2_3_the_classification_setting/trans2.html)
