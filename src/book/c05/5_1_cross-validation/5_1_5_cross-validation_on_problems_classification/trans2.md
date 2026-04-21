---
layout: default
title: "trans2"
---

# _5.1.5 Cross-Validation on Classification Problems_ 
# _5.1.5 막고라의 룰이 바뀐다: 분류 문제에서의 교차 검증_

In this chapter so far, we have illustrated the use of cross-validation in the regression setting where the outcome _Y_ is quantitative, and so have used MSE to quantify test error.
지금껏 우리가 5장에서 굴렸던 교차 검증 서바이벌의 무대는, 정답 $Y$ 가 숫자로 뿜어져 나오는 '회귀(Regression)' 환경이었습니다. 그래서 테스트 에러 점수판을 매길 때 과녁에서 얼마나 벗어났는지 재는 줄자인 'MSE'라는 무기를 타격 척도로 삼았죠.

But cross-validation can also be a very useful approach in the classification setting when _Y_ is qualitative.
하지만 교차 검증의 뺑뺑이 서바이벌은 정답 $Y$ 가 숫자가 아니라 범주(A냐 B냐)로 딱 나뉘는 '분류(Classification)' 환경에서도 미치도록 유용한 생존 확인 접근법이 됩니다.

In this setting, cross-validation works just as described earlier in this chapter, except that rather than using MSE to quantify test error, we instead use the number of misclassified observations.
이 분류의 전장 구역에서도 룰은 똑같습니다. 단 하나 달라지는 건 타격 점수판뿐입니다. 거리 줄자인 MSE 대신, 모델이 멍청하게 "적군을 아군으로 잘못 쏜 횟수", 즉 **오분류 된(misclassified) 삑사리 관측치의 개수**를 세어서 에러율로 때려 넣는다는 점만 바뀝니다.

For instance, in the classification setting, the LOOCV error rate takes the form 
이를테면 분류 세상에서의 그 끔찍한 막노동 LOOCV 뺑뺑이 에러 점수 공식은 이렇게 바뀝니다:

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \text{Err}_i \quad (5.4)
$$

where Err _i_ = _I_ ( _yi_ $\neq$ _y_ ˆ _i_ ).
여기서 $\text{Err}_i = I(y_i \neq \hat{y}_i)$ 입니다. 말이 복잡한데, 걍 정답 $y_i$ 랑 모델이 찍은 $\hat{y}_i$ 가 다르면 "너 삑사리! 에러 1점 추가!" 라고 장부에 적는 단단한 룰입니다.

The _k_ -fold CV error rate and validation set error rates are defined analogously. 
물론 우리의 타협안 _k_ -폴드 CV나, 구닥다리 반반 쪼개기(검증 세트) 가 채점하는 방식도 전부 똑같이 저 "삑사리 개수"를 세는 방식으로 굴러갑니다.

As an example, we fit various logistic regression models on the two-dimensional classification data displayed in Figure 2.13.
백문이 불여일견이죠. 우리는 예전 그림 2.13에서 놀았던 그 2차원 분류 구장에다가 몇 가지 로지스틱 회귀 모델 부대원들을 무기별로 가져가서 투입해 봤습니다.

In the top-left panel of Figure 5.7, the black solid line shows the estimated decision boundary resulting from fitting a standard logistic regression model to this data set.
그림 5.7의 제일 첫 번째(좌측 상단) 패널을 보세요. 시커먼 실선이 보이죠? 저게 바로 가장 멍청하고 평범한 '표준 로지스틱 회귀'가 적군과 아군을 가른다며 어설프게 그어놓은 '결정 경계(decision boundary)' 방어벽입니다.

Since this is simulated data, we can compute the _true_ test error rate, which takes a value of 0 _._ 201 and so is substantially larger than the Bayes error rate of 0 _._ 133.
다행히 이건 우리가 실험실에서 조립한 시뮬레이션 데이터라, 우린 신의 시점에서 쟤가 그은 선이 실제론 얼마나 폭망한 점수(_true_ 테스트 에러율) 인지 몰래 계산해 볼 수 있습니다. 까보니 에러율이 무려 0.201이나 되네요. 이건 절대적 물리 법칙상 도달 가능한 신의 에러 마지노선 점수(베이즈 구역 오차율) 인 0.133에 비하면 구멍이 숭숭 뚫린 심각하게 큰 폭망 수치입니다.

![Figure 5.7](./img/5_7.png)

**FIGURE 5.7.** _2차원 분류 데이터 전장에 투입된 로지스틱 회귀 부대원들. 신의 방어선인 '베이즈 결정 경계'는 보라색 점선으로 위엄 있게 쳐져 있습니다. 반면 1차(직선), 2차, 3차, 4차 곡률 템을 먹여서 뻗어 나간 우리 로지스틱 부대의 추정 방어선들은 각기 검은색 실선으로 칠해졌죠. 네 부대가 차례로 실전 테스트에서 거둔 삑사리 에러율 성적은 0.201, 0.197, 0.160, 0.162 로 나오는데, 신의 마지노선 0.133보단 여전히 다들 한참 모자랍니다._

Clearly logistic regression does not have enough flexibility to model the Bayes decision boundary in this setting.
명확합니다. 저 기본 로지스틱 회귀라는 직선 무기만 들고서는, 이 복잡하게 굽이친 베이즈 신의 방어선을 베껴 그릴 짬바(유연성, flexibility) 가 턱없이 부족해서 터진 겁니다.

We can easily extend logistic regression to obtain a non-linear decision boundary by using polynomial functions of the predictors, as we did in the regression setting in Section 3.3.2.
그래서 우린 예전 3장에서 회귀 무기를 개조했던 것처럼, 예측 정보들에 **'다항식(제곱, 세제곱)' 폭탄 옵션**을 끼얹어서 로지스틱 회귀가 휘어지는 비선형 방어선을 그릴 수 있도록 가볍게 무기 업그레이드를 때려 넣을 수 있습니다.

For example, we can fit a _quadratic_ logistic regression model, given by 
가령, $X^2$ 라는 옵션을 더해서 2차(quadratic) 다항 굴곡을 먹인 로지스틱 모델을 투입하면 수식 장비가 이렇게 바뀝니다:

$$
\log \left( \frac{p}{1-p} \right) = \beta_0 + \beta_1 X + \beta_2 X^2 \quad (5.5)
$$

The top-right panel of Figure 5.7 displays the resulting decision boundary, which is now curved.
그 결과물이 우측 상단 패널입니다! 드디어 시커먼 방어선이 직선을 벗어나 살짝 낭창낭창하게 휘어지기(curved) 시작했습니다.

However, the test error rate has improved only slightly, to 0 _._ 197.
근데 안타깝게도... 방어선을 좀 휘었음에도 실전 삑사리 점수는 0.201에서 고작 0.197로 쥐꼬리만큼 떨어지는 허접한 성과를 보였습니다.

A much larger improvement is apparent in the bottom-left panel of Figure 5.7, in which we have fit a logistic regression model involving cubic polynomials of the predictors.
그런데 좌측 하단 패널을 주목하세요. 확연하게 눈에 띄는 압도적 성장이 터졌습니다! 이건 예측 장비에 무려 **3차(cubic) 굴곡폭탄 옵션** 타격을 박아 넣고 로지스틱 모델을 미치게 꺾어버린 결과입니다.

Now the test error rate has decreased to 0 _._ 160.
이 과감한 유연성 도핑 덕분에, 실전 테스트 에러율 비중이 단숨에 0.160으로 떡락(decreased) 하며 엄청난 실전 방어력을 거두게 됩니다!

Going to a quartic polynomial (bottom-right) slightly increases the test error. 
신나서 "더 꺾어보자!" 하고 제일 우측 하단의 4차 항 극한 옵션까지 괴물처럼 유연성을 키우면 어떻게 될까요? 오히려 투머치하게 꼬여서 다시 에러 점수가 0.162로 튕겨 폭증(increases) 하는 과적합의 패착이 시작됩니다.

![Figure 5.8](./img/5_8.png)

**FIGURE 5.8.** _저 2차원 분류 전투에서 각기 투입된 에러들의 향연. (테스트 에러는 갈색 실선 / 모델의 망상인 훈련 에러는 파란색 실선 / 그리고 대망의 검증 타협안 10-fold CV는 칠흑색 선입니다). 좌측: 다항 굴곡 옵션(가로축)을 올리며 로지스틱 회귀를 돌린 판. 우측: 이번엔 참견 이웃수(K)를 달리하며 KNN 분류기로 돌려본 국면입니다._

In practice, for real data, the Bayes decision boundary and the test error rates are unknown.
자, 현실로 돌아오죠. 우리가 필드에서 마주치는 야생의 날것 데이터 환경에서는, 결코 우린 저 신의 베이즈 라인이 얼마인지, 절대적 테스트 오차율 정답이 얼마인지 모릅니다. 신만이 알죠. 

So how might we decide between the four logistic regression models displayed in Figure 5.7?
그렇다면 애초에 우린 정답지도 없는데 대체 어떻게 저 그림 5.7에 나왔던 네 가지 로지스틱 장비 중 **누굴 에이스(최적 모델)로 선발 출전시킬지** 결정(decide) 할 수 있을까요?

We can use cross-validation in order to make this decision.
이때 등판하는 우리의 치트키 무기가 바로 그 지독한 고문, '교차 검증(CV)'인 것입니다.

The left-hand panel of Figure 5.8 displays in black the 10-fold CV error rates that result from fitting ten logistic regression models to the data, using polynomial functions of the predictors up to tenth order.
그림 5.8의 왼쪽 전광판에 드리운 저 시커먼 라인이 뭔가요? 저게 바로 그 다항 굴곡 옵션을 무려 10차(tenth order) 레벨까지 이빠이 땡겨 치장하면서 각 모델마다 우리 **10-폴드 CV 뺑뺑이를 돌려 얻어낸 처절한 CV 에러 오차율 성적표 궤적**입니다. 

The true test errors are shown in brown, and the training errors are shown in blue.
참고로 진짜 신의 세계의 테스트 실전 오차 정답은 갈색 줄, 자기 혼자 훈련장에 틀어박혀 착각하는 '가짜 에러'인 훈련 에러는 파란 줄입니다. 

As we have seen previously, the training error tends to decrease as the flexibility of the fit increases.
우리가 귀에 못이 박히게 들어왔죠? 저 파란색 가짜 에러(훈련 에러) 라인은, 모델 무기의 굴곡 유연성이 기괴해지게 올라갈수록 지 혼자 신나서 정답을 다 맞춘다면서 밑도 끝도 없이 바닥으로 처박혀 자만하는(decrease) 못된 단세포 습성을 지니고 있습니다.

(The figure indicates that though the training error rate doesn’t quite decrease monotonically, it tends to decrease on the whole as the model complexity increases.)
(그림을 아주 예민하게 후벼파면 파란 선이 일자로 매끈하게 처박히진 않고 살짝 꿀렁거리긴 하지만, 누가 봐도 큰 판으로 보면 결국 모델이 변태같이 복잡해질수록 지 혼자 자만하며 바닥을 찍으려는 모순된 기조를 노골적으로 뿜어냅니다.)

In contrast, the test error displays a characteristic U-shape.
반면 우리가 진정 찾아 헤매는 신비로운 갈색 성적표(진짜 실전 테스트 에러) 는 그 악명 높은 전형적인 "U-자형 고랑 협곡"의 미친 딜레마 곡률을 무자비하게 뽐내고 있네요.

The 10-fold CV error rate provides a pretty good approximation to the test error rate.
여기서 우리의 검은 치트키, 10-폴드 CV 에러선이 엄청난 위력을 발휘합니다. 이 녀석이 저 신의 정답인 갈색 실전 테스트 라인을 마치 거울처럼 상당 부분 훌륭하게 모방하여 거의 엇비슷한 궤적으로 따라 그려냈기(approximation) 때문입니다!

While it somewhat underestimates the error rate, it reaches a minimum when fourth-order polynomials are used, which is very close to the minimum of the test curve, which occurs when third-order polynomials are used.
물론 아쉽게도 이 검은색 치트 라인이 간헐적으로 진짜 에러율을 조금 낮춰 잡아 "우린 이 정도 에러만 나와. 할만해!" 라며 약간 과소평가(underestimates) 하는 잔재주는 피우고 있긴 합니다. 하지만 보십시오! 이 검은 선은 정확히 **"4차 다항 옵션"을 끼워 넣었을 때 가장 오차가 바닥을 긁는 깊은 협곡 최소점(minimum)** 을 기가 막히게 찍어버립니다!! 이걸 신의 정답인 갈색선이 "3차 다항 옵션" 부근에서 깊은 계곡 최소점으로 처박히는 위치와 나란히 놓고 대조해 보면? 무서울 정도로 엄청나게 근접하게 좌표 위치를 쪽집게처럼 찾아 감별해 때려 맞춘 겁니다!

In fact, using fourth-order polynomials would likely lead to good test set performance, as the true test error rate is approximately the same for third, fourth, fifth, and sixth-order polynomials. 
심지어 까다롭게 까놓고 보면, "어라 신의 정답은 3차인데 CV 녀석은 4차를 최적이라고 찍었네? 실패 아닌가?" 할 필요도 없습니다. 갈색 라인(진짜 실전 테스트 오차) 의 협곡 바닥 구간을 보면 3차든 4차든 5차, 6차든 사실 그 일대에선 다들 도긴개긴, 점수가 거진 비슷비슷(the same)하게 밑바닥을 길고 있거든요. 그러니 비록 우리 CV녀석이 대안으로 4차 스위치를 에이스라 찍었다 한들, 이 무기를 실전에 던져놓아도 여전히 충분히 무쌍을 찍는 탁월하고 걸출한 성능 선방 방어 효율(good test set performance) 을 누릴 수 있다는 게 보장이 확증된다는 소리입니다. 

The right-hand panel of Figure 5.8 displays the same three curves using the KNN approach for classification, as a function of the value of _K_ (which in this context indicates the number of neighbors used in the KNN classifier, rather than the number of CV folds used).
자, 우측 전광판을 봅니다. 이번엔 로지스틱 전투가 아니라, 주변 패거리들의 다수결 투표를 믿고 나대는 **KNN 분류기 전투 요격망** 무기를 들고 왔습니다. 변수는 그 참견하는 이웃들의 수결을 뜻하는 지수 $K$ 조율값 이고요. (오해 마세요! 여기서 말하는 _K_ 는 아까 우리가 교대근무 뺑뺑이 조각으로 나눴던 그 폴드 조각수 _K_ 가 아닙니다. 그냥 KNN 모델 뱃속의 이웃 숫자 용량 수치일 뿐입니다!) 

Again the training error rate declines as the method becomes more flexible, and so we see that the training error rate cannot be used to select the optimal value for _K_ .
이번 턴에서도 역시나 저 파란색 거짓 훈련 에러 트랙 망상 곡선은, 무기가 무대뽀로 극도로 치명적 유연(flexible) 해지면 해질수록 영락없이 눈치 없이 바닥 지하 수렁으로 떨어져 내리꽂히며 감소 몰락(declines) 해버리는 뻘짓 행태를 고수합니다. 결국 이거 하나는 절실히 처절하게 뼈저리게 다시 깨닫게 되죠. **"훈련장 점수표 따위로는, 내 총(진짜 최적의 K 세팅 무기 옵션 투입값) 을 언제 어떻게 당길지 절대 골라(select) 정할 수가 없구나!"** 라는 걸 말이죠.

Though the cross-validation error curve slightly underestimates the test error rate, it takes on a minimum very close to the best value for _K_ . 
그리고 이 우측 전투 국면에서도 여전히 우리의 까만 치트키 CV 곡선은 정작 진짜 신의 테스트 갈색 에러율의 공포보단 살짝 데미지 거품을 낮게 깎아먹으며 빼주는 약간의 과소평가(underestimates) 엄폐 단막 삽질 기조를 일부 보이긴 하나; 그럼에도 그 본연의 미친 쪽집게 감별 타진 본능은 사그라지지 않습니다. 기필코 **저 갈색 라인이 가리키는 진정한 최적 무기 K의 세팅 스위치 좌표 그 부근을 정확하게 정조준해 포착해내며 거기에 자기 자신의 최소점 바닥점(takes on a minimum) 을 기막히게 맞물려 찍어 안착 도달해 내고 있으니까요!**
