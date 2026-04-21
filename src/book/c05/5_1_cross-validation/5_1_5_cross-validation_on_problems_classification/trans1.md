---
layout: default
title: "trans1"
---

# _5.1.5 Cross-Validation on Classification Problems_ 
# _5.1.5 분류 문제에서의 교차 검증_

In this chapter so far, we have illustrated the use of cross-validation in the regression setting where the outcome _Y_ is quantitative, and so have used MSE to quantify test error.
지금까지 이번 장 안에서, 우리는 결과물 _Y_ 가 정량적으로 도출되는 회귀 환경 세팅을 무대로 교차 검증의 사용 방식을 시연해 왔으며, 그리하여 시험 오차를 정량화하는 데 줄곧 MSE 지표를 차용해 왔다.

But cross-validation can also be a very useful approach in the classification setting when _Y_ is qualitative.
하지만 교차 검증은 결과물 _Y_ 가 정성적인 형태를 띠는 분류 환경 세팅 하에서도 매우 유용하게 쓰일 수 있는 훌륭한 접근법이 된다.

In this setting, cross-validation works just as described earlier in this chapter, except that rather than using MSE to quantify test error, we instead use the number of misclassified observations.
이 분류 세팅 구역 안에서, 교차 검증은 오직 테스트 에러를 정량화 타진하기 위해 MSE 수치 대신 '오분류된(misclassified) 관측치들의 총 개수 에러율'을 대체하여 사용한다는 단 한 가지 차이점만을 제외하면, 애초에 이번 장 앞부분에서 앞서 서술해 놓았던 기존 메커니즘 방식과 완벽하게 똑같이 훌륭하게 구동 작동한다.

For instance, in the classification setting, the LOOCV error rate takes the form 
예를 들어 분류 세부 세팅 하에서라면, 기존 LOOCV 오차율 타진 체계 형태는 다음과 같은 공식을 띠게 된다:

$$
\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \text{Err}_i \quad (5.4)
$$

where Err _i_ = _I_ ( _yi_ $\neq$ _y_ ˆ _i_ ).
이 공식에서 척도 $\text{Err}_i = I(y_i \neq \hat{y}_i)$ 이다.

The _k_ -fold CV error rate and validation set error rates are defined analogously. 
여타 _k_ -폴드 CV 에러율이나 검증 세트 오차율 공식 체계 역시 이와 전적으로 유사하게 조율 정의된다.

As an example, we fit various logistic regression models on the two-dimensional classification data displayed in Figure 2.13.
하나의 본보기 차원에서, 우리는 예전 그림 2.13 지면에 전시된 바 있는 2차원 공간 분류 데이터 세트 위에 몇 가지 각기 다른 다채로운 로지스틱 회귀 모델들을 적합시켜 보았다.

In the top-left panel of Figure 5.7, the black solid line shows the estimated decision boundary resulting from fitting a standard logistic regression model to this data set.
이 그림 5.7의 좌측 상단 패널 구역에서, 칠흑 같은 검은색 실선은 딱 하나의 가장 표준적인 로지스틱 회귀 모델을 이 특정 데이터 세트 지형에 적합 접목시킨 결과로써 도출된 추정 결정 경계(decision boundary) 라인을 표출해 보여준다.

Since this is simulated data, we can compute the _true_ test error rate, which takes a value of 0 _._ 201 and so is substantially larger than the Bayes error rate of 0 _._ 133.
이 데이터는 다름 아닌 시뮬레이션 된 허구 데이터에 불과하기 때문에 우리는 역으로 순수한 _진짜(true)_ 시뮬레이션 테스트 오차율 내역을 산술 계산해 볼 수 있고, 이는 0.201이라는 값을 취하며 곧 이는 초반부에 언급한 적 있는 절대적 최소 바닥점 베이즈 에러율(Bayes error rate) 인 0.133 지표보다 확연히 실질적으로 훨씬 더 거대한 볼륨임을 일깨워 준다.

![Figure 5.7](./img/5_7.png)

**FIGURE 5.7.** _Logistic regression fits on the two-dimensional classification data displayed in Figure 2.13. The Bayes decision boundary is represented using a purple dashed line. Estimated decision boundaries from linear, quadratic, cubic and quartic (degrees 1–4) logistic regressions are displayed in black. The test error rates for the four logistic regression fits are respectively_ 0 _._ 201 _,_ 0 _._ 197 _,_ 0 _._ 160 _, and_ 0 _._ 162 _, while the Bayes error rate is_ 0 _._ 133 _._ 
**FIGURE 5.7.** _그림 2.13에 나열되어 전시된 2차원 분류 데이터 덩어리에 로지스틱 회귀가 각기 적합된 양상들. 베이즈 경계선(Bayes decision boundary) 방어벽은 짙은 보라색 점선 실무늬로 확연하게 대변하여 표시되어 있다. 선형에서 비롯하여 나아가 2차, 3차, 그리고 마침내 4차 굴곡 항(최대 1~4차수) 다항 로지스틱 단층 회귀들로부터 각기 파생되어 그려진 추세 결정 경계선들은 모두 검은색으로 도포 표기되어 있다. 이들 네 종파 굴곡 로지스틱 회귀 적합 모델들에 각기 상응 부여 도출된 실전 테스트 에러율 수치 성적표는 그 순서대로 각기_ 0.201 _,_ 0.197 _,_ 0.160 _, 그리고_ 0.162 _에 달한 반면, 절대적 신의 마지노선 점수 베이즈 구역 오차율은 공고히_ 0.133 _값에 버티며 형성 박혀 있다._

Clearly logistic regression does not have enough flexibility to model the Bayes decision boundary in this setting.
명확하게도 단출한 로지스틱 회귀 단일 무기 체계 하나만으로는 이 복잡다단한 세팅 환경 구역 안에서 구불구불한 베이즈 결정 경계면을 충분히 여유롭게 모델링 재단해 낼 만한 능란 유연성(flexibility) 을 도통 지니지 못한다.

We can easily extend logistic regression to obtain a non-linear decision boundary by using polynomial functions of the predictors, as we did in the regression setting in Section 3.3.2.
우리는 앞선 3.3.2 절의 회귀 파트에서 거행 이수했던 기교 방식과 일맥상통하게, 기실 예측 변수 성분들의 다항 함수(polynomial functions)를 동원함으로써 아주 다분히 쉽게 로지스틱 회귀 무기의 지경을 넓히고 더욱 구불거리는 비선형 국면의 결정 경계 라인을 체득 획득해 낼 수 있다.

For example, we can fit a _quadratic_ logistic regression model, given by 
가령 예를 들어, 우리는 다음과 같은 수식 꼴체 형태로 주어진 _2차(quadratic)_ 굴곡 항의 로지스틱 회귀 모델 장치를 접목 적합시킬 수 있다:

$$
\log \left( \frac{p}{1-p} \right) = \beta_0 + \beta_1 X + \beta_2 X^2 \quad (5.5)
$$

The top-right panel of Figure 5.7 displays the resulting decision boundary, which is now curved.
그림 5.7의 그 우측 상단 지면 패널 조각은 바로 그 과정을 거쳐 새롭게 형성 탄생한 결정 경계 결과물을 포착 전시해 주는데, 이 윤곽은 비로소 일자로 굳은 게 아닌 명백히 이리저리 살짝 휘어지고 휘어 구부러진(curved) 유연한 형태를 취하게 되었다.

However, the test error rate has improved only slightly, to 0 _._ 197.
하지만 애석하게도 그 테스트 에러 덩치 자체는 여전히 겨우 0.197이라는 소소한 수준 언저리로 조금밖에 향상 극복되지 못한 게 실상이다.

A much larger improvement is apparent in the bottom-left panel of Figure 5.7, in which we have fit a logistic regression model involving cubic polynomials of the predictors.
반면 그림 5.7의 하단 좌측 패널 전경 부근에서는 이보다 훨씬 더 거대한 성능 향상이 명백하게(apparent) 눈에 띈 채 관측 목격되는데, 바로 그곳이 다름 아닌 우리 인원들이 예측 변수들에 당돌하게 고차원의 3차 항(cubic) 다항식 옵션을 과감히 탑재 투여 밀어 넣은 로지스틱 회귀 모델을 실험 적합시켜 본 구역 무대이다.

Now the test error rate has decreased to 0 _._ 160.
이제 마침내 이로써 치명적이었던 테스트 에러율 비중의 하자가 무려 0.160 수위 포인트로까지 현격히 큰 폭으로 격하 하락 극복 감소(decreased) 하게 되었다.

Going to a quartic polynomial (bottom-right) slightly increases the test error. 
다만 이것을 더 욕심내어 4차 수준의 극한 다항식 항(우측 하단) 마지노선 코어까지 더욱 기세를 올려버리면 수치가 또다시 본분을 망각하고 정작 실전 테스트 에러를 아주 미세하게나마 살짝 더 다시 키우고 폭증(increases) 상승시켜 버리는 패착 행보를 띤다.

![Figure 5.8](./img/5_8.png)

**FIGURE 5.8.** _Test error (brown), training error (blue), and_ 10 _-fold CV error (black) on the two-dimensional classification data displayed in Figure 5.7._ Left: _Logistic regression using polynomial functions of the predictors. The order of the polynomials used is displayed on the x-axis._ Right: _The KNN classifier with different values of K, the number of neighbors used in the KNN classifier._ 
**FIGURE 5.8.** _방금 전 위쪽 그림 5.7에서 시연 진열되었던 저 2차 분류 국면 데이터 위에서 각기 테스트 오차(갈색) 및 훈련 학습 오차(파란색), 그리고 기필코 추정해 낸_ 10- _폴드 CV 에러 굴곡선(검은색)의 흐름. 좌측: 예측 변수 성분들의 다항 굴곡 함수들을 거듭 탑재 끌어올려 무장한 로지스틱 회귀. 기용한 다항 치트 옵션 최고 차수가 x축에 포진되어 진열 표시되어 있다. 우측: KNN 분류 장치 기계 장치 내부에 사용 포용된 주변 이웃 참견꾼 할퀴기 숫자 지수인 KNN 이웃수 K 값 수치를 다르게 설정 타진해 돌린 KNN 분류 장치의 결과 곡선 궤적._

In practice, for real data, the Bayes decision boundary and the test error rates are unknown.
실무 필드 관행상 우리가 접하는 현실 날것의 데이터 실무 전선 위에서, 영험한 신의 영역인 베이즈 결정 경계 기준치나 정녕 진짜배기 모범 테스트 오차율 같은 절대 표적수치들의 참값 존재는 철저히 까맣게 베일에 싸여 전혀 알려진 바 없이(unknown) 묻혀 있기 마련이다.

So how might we decide between the four logistic regression models displayed in Figure 5.7?
그렇다면 대체 우리 인간 통계학자들은 그림 5.7 지면 장관에 도열 전시되었던 저 네 개의 로지스틱 분류 단층 회귀 무기 모델 후보군들 가운데에서, 과연 도대체 어떤 최고 위너를 선발 결정(decide) 지어 추대해 모셔야 마땅할까?

We can use cross-validation in order to make this decision.
우리는 바로 저 난해한 선택지들의 승부사 판단 결정을 도출해 내리기 위해서 필시 앞서 그토록 배운 '교차 검증(cross-validation)' 무기를 치트키로 써먹고 사용할 수 있다.

The left-hand panel of Figure 5.8 displays in black the 10-fold CV error rates that result from fitting ten logistic regression models to the data, using polynomial functions of the predictors up to tenth order.
그림 5.8의 왼쪽 구역 패널 지형판은 시커먼 검은 선 궤도로써, 최대 무려 10차(tenth order) 다항 멱급수 극한 수준 차수까지 온갖 예측 변수의 다항 함수를 덕지덕지 치장 발라놓으며 도합 총 10가지의 로지스틱 회귀 모델 실험체를 저 데이터 산지에 다짜고짜 번갈아 적합시켜 얻어낸 각양각색 10-폴드 CV 에러율의 여정을 찬란하게 곡선으로 늘어놓아 전시한다.

The true test errors are shown in brown, and the training errors are shown in blue.
이 가운데에서, 전지구 신의 정답인 진성 진짜 테스트 실전 오차 성적들은 갈색 톤으로 선혈 낭자하게 전시되어 있고, 정작 훈련에 심취해 착각을 일으키는 거짓 왜곡 훈련 에러 궤적은 파란색 망상 자태로 진열 기입 표출되어 존재한다.

As we have seen previously, the training error tends to decrease as the flexibility of the fit increases.
우리가 그간 지겹도록 이전부터 수도 없이 많이 뼈저리게 보아 목격 목도해 왔듯이, 파란색 거짓의 훈련 오차 요동은 정작 한결같이 저 모델 훈련 적합물의 굴곡 유연성(flexibility)이 유들유들하게 파도를 타며 증가치솟듯 흉내 내짐에 따라 덩달아 연쇄적으로 계속 거짓 곤두박질치듯 얌전히 일방적으로 한없이 추락 감소(decrease)하려는 고질적인 단세포 경향 성향을 줄곧 여전히 지어 보이고 있다.

(The figure indicates that though the training error rate doesn’t quite decrease monotonically, it tends to decrease on the whole as the model complexity increases.)
(비록 이 그림 도안을 유심히 매섭게 보면 훈련 에러율 수치선 하나가 그저 단조롭게 꼬꾸라지는 마냥 일자로 추락하진 않는 듯 살짝 주춤거리긴 하나, 그래도 전반적으로 크게 큰 틀 맥락 흐름에서 응시 타진해 보면 모델 복잡도가 난해해짐에 따라 여전히 전체 덩어리 전반에 걸쳐 하락 추이 감소세를 여봐란듯이 관통 유지하는 뻔뻔한 속성을 지어 내비침을 알 수 있다.)

In contrast, the test error displays a characteristic U-shape.
반도적으로 대조해 볼 때, 정작 우리 인간이 진짜 사수 갈망 타진 염원해야 할 저 진짜 타깃 오차율 테스트 실전 추이 타율 갈색 실선 궤성은 몹시 전형적인 "U-자형(U-shape) 곡률 고랑 협곡 패임" 구조의 위기 곡선 형태 행보 행태를 고수 표출 장관 진열 전시해 보이고 있다.

The 10-fold CV error rate provides a pretty good approximation to the test error rate.
10-폴드 형태 체제로 무장한 이 막강 CV 에러 예측 추산 추정 곡률 궤도는 전반적으로 저 진짜배기 테스트 성적 오차율 산줄기 궤적을 몹시 찌를 듯 타진할 듯 상당 부문의 몫에서 무척 훌륭하게 모조리 모방 일치 상당히 근사하게 접근 타진 추정 적중하여 반영해 준다.

While it somewhat underestimates the error rate, it reaches a minimum when fourth-order polynomials are used, which is very close to the minimum of the test curve, which occurs when third-order polynomials are used.
물론 이 검은색 치트 CV 트랙이 가끔 드문드문 다소간 진짜 에러 고통률을 묘하게 과소평가(underestimates) 은폐해 덜 아프게 재단 치장해 낮춰 보여주는 기조 단점을 내비쳐 누설하긴 하지만; 그래도 나름 영특하게 4차(fourth-order) 다항 스펙 레버 옵션 장비를 투입 사용 접목시켰을 그 지점 즈음에서 찌를 듯 가장 하단 밑바닥 맹점 최소점(minimum) 을 기막히게 찍어 도달 안착 포착 발견해 주는데; 사실 이는 신의 정답인 갈색 참 테스트 곡선이 다름 아닌 3차 급수의 옵션 세팅 구간을 투입할 때 가장 밑바닥 극저점 수렁 구역으로 최소 추락 하강하여 도달하는 바와 서로 비교 대조 대비해 볼 때 실로 너무나 얄미우리만치 신묘하게 초근접하게 소름 돋게 가까운 흡사 모조 정답 타당 타깃 최소점 적중 일치 구역이다!!

In fact, using fourth-order polynomials would likely lead to good test set performance, as the true test error rate is approximately the same for third, fourth, fifth, and sixth-order polynomials. 
기실 까다롭게 진짜 따져보면 어차피 3차, 4차는 물론이고 5차와 6차 수준의 허접한 다항식 항들의 언저리 일대에 포진한 구간들을 보면 모두 다 진짜 실전 베테랑 테스트 오차율 타격 점수 수위 흠집 덩치가 그냥 거기서 거기인 양 죄다 모조리 대략적으로 거의 얼추 비슷비슷 엇비슷하고 엇갈림 동급으로 매한가지 유사한 편이기에; 심지어 4차 다항 로지스틱을 찍어 골랐다고 해도 여전히 실전 테스트 세팅 도마 무대 경기장 위에서는 으뜸가는 걸출 탁월한 나쁘지 않은 수준 방어력 선방의 멋진 퍼포먼스(good test set performance) 결실 수확 도출 성과 위력을 기쁘게 장담 보장 영위 이끌어 가져다줄 것이다.

The right-hand panel of Figure 5.8 displays the same three curves using the KNN approach for classification, as a function of the value of _K_ (which in this context indicates the number of neighbors used in the KNN classifier, rather than the number of CV folds used).
위 그림 5.8의 우측 편 도표 판넬 역시 이 분류 전쟁터 판에서 조금 전 써먹었던 저 똑같은 세 갈래 갈등 양상 에러 궤설 세 개의 곡선들을 거푸 진열 묘사해 주는데; 다만 이번엔 로지스틱이 아니라 다름 아닌 이웃 투표 기법 분류 체제인 **KNN 요격 분류 접근법 모델 기기**를 접목 기용 수단 차용 탑재하여 돌린 뒤, 그 세기에 따른 투표수 **이웃수(K)의 참견 인원 수효 조율값** 설정 지시 변동성 여하를 나타내고자 플롯 도해하여 보여준다 (명심하라, 이 문맥 맥락 이 구간 좌표에서의 변수 _K_ 문자는 단지 아까 지겹게 보았던 "CV 폴드 그룹 교대 쪼개기 조작 숫자 개수"가 절대 아니며, 여기선 그저 KNN 모델 무기 내부의 조립 기능이 필요로 하는 투표 참견 이웃 인구수 숫자를 확고히 지시 가리키는 지표 장치로 전락 전환된다).

Again the training error rate declines as the method becomes more flexible, and so we see that the training error rate cannot be used to select the optimal value for _K_ .
이번 턴에서도 과연 어김없이 늘 그랬듯 파란색의 교활한 거짓 망상 훈련 에러 점수 요동율 선 궤도는 모델 무기의 구조가 스펙 유연성이 늘어나면 늘어날수록 유들유들 말랑말랑 거대 유연(flexible) 해질수록 한없이 절벽으로 추락 하강 곤두박질치는 하락(declines) 단조 기조를 한결같이 되풀이 맹신 유지 전시하며, 썩어 문들어져 떨어지기 때문에; 이를 통탄 목도 지어 지켜보는 우린 종내 거듭 확신하며 "아, 역시나 훈련 과정의 에러 점수 스코어 덩치 따위로는 결단코 이 무기의 최적 K 값 세팅 투입 유효 숫자 지수를 포착 판별 감별 조율해 선출 선택 선택(select) 뽑아낼 수가 없겠구나"라는 불변의 한계 뼈저린 진리 한계를 또 한 번 목도 직시 처절 체감 공감 인식하게 지어 된다.

Though the cross-validation error curve slightly underestimates the test error rate, it takes on a minimum very close to the best value for _K_ . 
비록 이번 판에서도 검은색 우리 CV 무신의 교차 검증 오차 산정 추이 곡률 노선 궤도선 자태 윤곽 굴곡 궤적이 정작 그 진짜 실전 신들의 테스트 오차율 위력을 묘하게 기만 아주 소폭 미세 살짝 과소평가 평가절하 오버 축소 은폐 도무(underestimates) 하는 약간 민망 아쉬운 요행 삽질 수치를 조금 품고 거듭 나타내 거슬리기는 하지만; 여전히 그래도 여지없이 소름 돋게 여봐란듯이 가장 으뜸 최정예 최적 엘리트 최고치 베스트 승리 K 무기 세팅 스위치 스팟 투입 좌표 지수 숫적 값 언저리 일대 가장 가장자리 바닥 초근접 아주 밀접 근사 지점 부근 바닥 구역에서 제대로 기절 하강 꼬꾸라지는 **기막힌 대견 영험한 신성 최소점(takes on a minimum)** 바닥 절정 구역 요율 지수를 당찬 자태로 어김없이 확실하고도 확고 영리 타당 정교히 아주 아주 용하게 잘 찝어 뽑아내 찍어 선별 감추어 타진해 찾아 식별 포착 발굴 내뿜어 보여준다.
