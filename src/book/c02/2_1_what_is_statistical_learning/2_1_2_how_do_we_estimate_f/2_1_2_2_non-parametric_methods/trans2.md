---
layout: default
title: "trans2"
---

[< 2.1.2.1 Parametric Methods](../2_1_2_1_parametric_methods/trans2.html) | [2.1.3 The Trade-Off Between Prediction Accuracy And Model Interpretability >](../../2_1_3_the_trade-off_between_prediction_accuracy_and_model_interpretability/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# Non-Parametric Methods
# 비모수적 방법론 (자유방임주의: 데이터가 이끄는 대로!)

![Figure 2.5](./img/Image_019.png)

**FIGURE 2.5.** _A smooth thin-plate spline fit to the_ `Income` _data from Figure 2.3 is shown in yellow; the observations are displayed in red. Splines are discussed in Chapter 7._

**그림 2.5.** _이건 아까 그림 2.3의 30명 아저씨 데이터(빨간 점) 위에다가 플라스틱 수건(얇은 판 스플라인, thin-plate spline) 같이 아주 부드러운 유연한 판때기(노란색 표면)를 덮어 씌워본 겁니다. 저 스플라인이라는 신기한 마법 수건은 7장에 가서나 제대로 뜯어볼 겁니다._

Non-parametric methods do not make explicit assumptions about the functional form of _f_.
비모수적(Non-parametric) 방법은 아까 봤던 꼰대 같은 파벌(모수적)이랑은 정반대입니다. 이 쿨한 녀석들은 조물주의 함수 _f_ 가 선형인지 곡선인지 도대체 어떻게 생겨 먹었는지에 대해서 1도 가정하거나 우기지 않습니다.

Instead they seek an estimate of _f_ that gets as close to the data points as possible without being too rough or wiggly.
애초에 정해진 틀이 없으니까, 이 녀석들은 그냥 "모양은 내 알 바 아님!" 하고 붓을 든 채, 데이터 점들이 찍힌 곳들을 향해 구불구불 유연하게 흘러가면서 최대한 점들에 찰싹 달라붙는 짝퉁 _f_ 를 그려내려고 발악합니다. (단, 너무 미친 듯이 삐죽삐죽 요동치지 않는 선에서 말이죠.)

Such approaches can have a major advantage over parametric approaches: by avoiding the assumption of a particular functional form for _f_, they have the potential to accurately fit a wider range of possible shapes for _f_.
이렇게 프리스타일로 그리면 꼰대(모수적) 방법보다 엄청나게 강력한 깡패 같은 장점을 하나 가지게 됩니다. 애초에 "넌 무조건 직선이야!"라는 멍청한 제약 자체가 없으니까, 진짜 _f_ 가 S라인이든 Z라인이든 별의별 미친 모양을 하고 있어도 그걸 다 고무줄처럼 기가 막히게 따라가며 베껴 그릴(정확한 적합) 수 있는 잠재력이 있는 거죠.

Any parametric approach brings with it the possibility that the functional form used to estimate _f_ is very different from the true _f_, in which case the resulting model will not fit the data well.
반면에 모수적 꼰대들은 자기 고집대로 "난 무조건 직선으로만 그릴래!" 했다가, 막상 진짜 _f_ 모양이랑 척화비처럼 엇갈려버리는 순간, 데이터랑 하나도 안 맞는 쓰레기 모델을 뽑아낼 수밖에 없는 치명적인 위험성을 항상 안고 살아야 하거든요.

In contrast, non-parametric approaches completely avoid this danger, since essentially no assumption about the form of _f_ is made.
이와 대조적으로 비모수적 자유영혼들은 애초에 _f_ 의 생김새에 대한 '멍청한 가정' 자체를 일절 안 하니까 애먼 똥볼을 찰 위험(가정 오류)을 원천적으로 완벽하게 피할 수 있습니다.

But non-parametric approaches do suffer from a major disadvantage: since they do not reduce the problem of estimating _f_ to a small number of parameters, a very large number of observations (far more than is typically needed for a parametric approach) is required in order to obtain an accurate estimate for _f_.
하지만... 이 멋진 자유영혼들도 뼈아픈 단점 앞에서는 무릎을 꿇습니다. 뼈대를 정해서 구멍(파라미터) 몇 개만 핀셋으로 찾으면 됐던 그 개꿀을 포기해 버렸으니, 이젠 백지 도화지에 허공부터 모래알을 빚어 돗자리를 전부 새로 짜내야 합니다. 결국 이렇게 프리하게 그림을 다 완성하려면 힌트 데이터가 진짜 산더미처럼 무식하게 많이 필요하다는 거죠! (직선 그릴 땐 점 10개면 됐는데 여긴 점 1,000개가 있어야 봐줄 만한 그림이 나오는 식입니다.)

An example of a non-parametric approach to fitting the `Income` data is shown in Figure 2.5.
이 프리스타일(비모수적) 방식을 써서 아저씨들 수입(Income) 장부를 그려낸 게 바로 앞서 본 그림 2.5의 노란색 수건입니다.

A _thin-plate spline_ is used to estimate _f_.
여기서는 구불구불한 **'얇은 판 스플라인(thin-plate spline)'** 이라는 기법을 동원해서 짝퉁 _f_ 를 유연하게 그려냈습니다.

This approach does not impose any pre-specified model on _f_.
이 방식은 "모양은 어때야 해!"라고 _f_ 한테 갑질(사전 지정 모델 부과)을 전혀 하지 않습니다.

It instead attempts to produce an estimate for _f_ that is as close as possible to the observed data, subject to the fit—that is, the yellow surface in Figure 2.5—being _smooth_.
대신에 이 방식은 "최대한 저 빨간 데이터 점들에 머리를 비비고 밀착해서 모양을 덮어 씌우자!"라고 노력할 뿐입니다. 단, 결과물(노란 플라스틱 수건)이 너무 까슬까슬거리지 않고 **마치 융단처럼 매끄럽다(smooth)** 는 전제조건 하나만 간신히 지키면서요.

![Figure 2.6](./img/Image_020.png)

**FIGURE 2.6.** _A rough thin-plate spline fit to the_ `Income` _data from Figure 2.3. This fit makes zero errors on the training data._

**그림 2.6.** _이건 그림 2.3의 30개 점에 아까 그 스플라인 수건을 덮은 건데, 이번엔 "매끄러움 따윈 개나 줘!" 하고 극한으로 구불거리게 바늘(거친 적합)을 쑤셔 넣은 모습입니다. 놀랍게도 이 극단적인 적합은 훈련 데이터(빨간 점 30개)마다 정확히 뚫고 지나가 오차가 무려 0입니다!_

In this case, the non-parametric fit has produced a remarkably accurate estimate of the true _f_ shown in Figure 2.3.
그림 2.5의 노란 융단은 (비록 데이터가 겨우 30명분이라 부족했지만) 꽤나 기가 막히게 진짜 S라인 _f_ (그림 2.3의 파란 돗자리)와 소름 돋게 비슷한 모양새를 성공적으로 뽑아냈습니다.

In order to fit a thin-plate spline, the data analyst must select a level of smoothness.
그런데 이 스플라인 수건도 사람이 직접 조종해야 합니다. 분석가가 "수건을 고무줄처럼 좍좍 늘어나게(유연하게) 구불구불 접어줄까, 아니면 다림질한 것처럼 빳빳하게 펴줄까?" 하고 **'부드러움의 강도(수준)'** 를 다이얼로 직접 선택해줘야 하거든요.

Figure 2.6 shows the same thin-plate spline fit using a lower level of smoothness, allowing for a rougher fit.
방금 본 그림 2.6이 바로 그 다이얼을 '다림질 끄기(낮은 부드러움 수준)'로 돌렸을 때 대참사가 벌어진 현장입니다. 수건이 데이터 점 하나하나를 강제로 관통하려고 마치 뾰족한 산봉우리처럼 거칠게 요동치며 찢어질 듯 구부러져(거친 적합) 있죠.

The resulting estimate fits the observed data perfectly!
놀랍게도 저 결과물은 우리가 가진 30개의 빨간 점들(관측 데이터)을 단 하나의 오차도 없이 과녁 정중앙으로 **완벽하게 꿰뚫고 지나갑니다!**

However, the spline fit shown in Figure 2.6 is far more variable than the true function _f_, from Figure 2.3.
하지만 세상 속지 마십시오! 그림 2.6의 저 헐떡이는 뾰족 수건은 부드럽게 흘러가야 할 진짜 원본 함수 _f_ (그림 2.3)에 비해서 완전히 정신병에 걸린 것처럼 신경질적으로 요동치고 있습니다.

This is an example of overfitting the data, which we discussed previously.
맞습니다! 이게 바로 아까 우리가 침을 튀기며 욕했던 데이터 점들의 더러운 잡음(운빨)마저 미친 듯이 외워버려서 생긴 대참사, 극악무도한 **'과적합(Overfitting)'** 의 교과서적인 예시입니다.

It is an undesirable situation because the fit obtained will not yield accurate estimates of the response on new observations that were not part of the original training data set.
이건 우리가 원하는 짝퉁 모델이 아닙니다! 왜냐고요? 이렇게 우리가 애지중지 훈련용 오답 노트(빨간 점 30개)에만 목숨 걸게 훈련시킨 이 바보 뾰족 모델에다가, 나중에 처음 보는 생면부지의 실전 데이터(새 관측치)를 집어넣으면? 핀트가 완전 엇나가서 정답을 하나도 못 찍어 맞추고 똥볼만 차댈 게 뻔하거든요!

We discuss methods for choosing the _correct_ amount of smoothness in Chapter 5.
그래서 도대체 이 다이얼, 즉 빳빳함과 구불구불함 사이에서 어디쯤이 '황금 밸런스(정확한 매끄러움 양)'인지 잡는 극강의 타협 기술은 나중에 5장(교차 검증 파트)에서 신나게 배우게 됩니다.

Splines are discussed in Chapter 7.
그리고 이 마법의 수건 '스플라인(Splines)'의 정체에 대해서는 7장에 가면 질리도록 뜯어볼 겁니다.

As we have seen, there are advantages and disadvantages to parametric and non-parametric methods for statistical learning.
자, 지금까지 보셨다시피 꼰대(모수적) 방법과 자유영혼(비모수적) 방법에는 마치 빛과 그림자처럼 아주 뼈아픈 장점과 치명적인 단점들이 함께 공존합니다.

We explore both types of methods throughout this book.
앞으로 이 책을 항해하는 내내 우리는 이 두 가지 다른 맛의 파벌 방법론들을 넘나들며 모험을 즐기게 될 것입니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.2.1 Parametric Methods](../2_1_2_1_parametric_methods/trans2.html) | [2.1.3 The Trade-Off Between Prediction Accuracy And Model Interpretability >](../../2_1_3_the_trade-off_between_prediction_accuracy_and_model_interpretability/trans2.html)
