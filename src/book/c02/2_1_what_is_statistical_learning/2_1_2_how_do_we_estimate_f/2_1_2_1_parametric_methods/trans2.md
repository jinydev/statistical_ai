---
layout: default
title: "trans2"
---

[< 2.1.2 How Do We Estimate F](../trans2.html) | [2.1.2.2 Non-Parametric Methods >](../2_1_2_2_non-parametric_methods/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# Parametric Methods
# 모수적 방법론 (답정너: 모양은 내가 정할 테니, 넌 숫자나 맞춰!)

Parametric methods involve a two-step model-based approach.
모수적(Parametric) 방법은 딱 2단계로 끝나는 아주 계산적이고 틀에 박힌 접근법입니다.

1. First, we make an assumption about the functional form, or shape, of _f_.
**1단계: 눈 감고 모양부터 우기기.** 제일 먼저 우리는 신의 돗자리 _f_ 가 도대체 어떻게 생겨 먹었을지, 데이터를 제대로 보기도 전에 그냥 모양(형태)부터 무작정 가정해버립니다.

For example, one very simple assumption is that _f_ is linear in _X_:
가장 흔하고 무식한 가정이 바로 "에이, 복잡할 거 뭐 있어? _f_ 는 힌트 _X_ 들을 쓱쓱 자를 대고 그은 **일직선(Linear)** 이야!" 라고 우기는 겁니다:

$$ f(X) \approx \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \tag{2.4} $$

This is a _linear model_, which will be discussed extensively in Chapter 3.
이게 바로 3장 내내 여러분을 괴롭힐 전설의 **선형 모델(Linear model)** 입니다.

Once we have assumed that _f_ is linear, the problem of estimating _f_ is greatly simplified.
자, 이렇게 _f_ 가 반듯한 직선이라고 우리끼리 합의(가정)하고 나면, 찰흙을 빚어 돗자리를 깎아내야 했던 그 끔찍한 _f_ 추정 문제가 갑자기 초등학교 산수 문제로 전락합니다.

Instead of having to estimate an entirely arbitrary _p_-dimensional function _f_(_X_), one only needs to estimate the _p_ + 1 coefficients $\beta_0, \beta_1, \dots, \beta_p$.
허공에 둥둥 떠다니는 알 수 없는 $p$-차원의 괴상한 구름 덩어리 $f(X)$ 전체를 다 잡아낼 필요 없이, 우리는 그냥 저 공식에 들어갈 빈칸 숫자(계수 파라미터)들인 $\beta_0, \beta_1, \dots, \beta_p$ 만 핀셋으로 쏙쏙 뽑아내(추정) 채워 넣으면 끝이거든요.

2. After a model has been selected, we need a procedure that uses the training data to _fit_ or _train_ the model.
**2단계: 훈련 데이터로 빈칸 채우기(적합).** 뼈대(직선)를 세웠으니, 이제 우리가 모아둔 오답 노트(훈련 데이터)를 집어넣어서, 저 직선의 기울기와 높이가 데이터 점들에 쫙 들러붙게끔 기계를 학습(훈련)시킬 차례입니다.

In the case of the linear model fit (2.4), we need to estimate the parameters $\beta_0, \beta_1, \dots, \beta_p$.
앞서 만든 직선 방정식 (2.4)의 경우엔 저 수학 기호들(파라미터들)인 $\beta_0, \beta_1, \dots, \beta_p$ 에 들어갈 가장 완벽한 '숫자'들을 때려 맞추는 게 목표죠.

That is, we want to find values of these parameters such that
즉, 툭 튀어나오는 야매 정답이 진짜 데이터 점이랑 거~의 똑같아지도록 파라미터 구멍을 기가 막히게 메워버리고자 합니다:

$$ Y \approx \hat{\beta}_0 + \hat{\beta}_1 X_1 + \dots + \hat{\beta}_p X_p \tag{2.5} $$

The most common approach to fitting the model (2.4) is referred to as _(ordinary) least squares_, which we discuss in Chapter 3.
선을 데이터 점들에 찰싹 달라붙게 욱여넣는 가장 유명하고 만만한 스킬이 바로 3장에서 죽어라 배울 **'최소 제곱법(Least squares)'** 입니다. 점 사이의 오차 거리를 제곱해서 미친듯이 깎아버리는 원리죠.

However, least squares is one of many possible ways to fit the linear model.
물론 최소 제곱법이 유일한 정답은 아닙니다. 그냥 선을 긋는 수많은 스킬 트리 중 제일 편해서 쓰는 것일 뿐이죠.

In Chapter 6, we discuss other approaches for estimating the parameters in (2.4).
나중에 6장에 가면 저 파라미터들을 훨씬 변태적이고 우아하게 찾아내는 다른 업그레이드 기법들도 신나게 다룰 겁니다.

The model-based approach just described is referred to as _parametric_; it reduces the problem of estimating $f$ down to one of estimating a set of parameters.
방금 말한 이 모든 짓거리가 뼈대를 세워놓고 빈칸 숫자만 찾는, 이른바 **모수적(parametric)** 접근법의 진수입니다. 우주적인 함수 $f$ 를 찾는 거대한 미션을, 단순히 (숫자 파라미터 몇 개 찾기)라는 하찮은 알바 수준으로 확 깎아버린 마법이죠!

Assuming a parametric form for $f$ simplifies the problem of estimating $f$ because it is generally much easier to estimate a set of parameters, such as $\beta_0, \beta_1, \dots, \beta_p$ in the linear model (2.4), than it is to fit an entirely arbitrary function $f$.
사실 $f$ 를 특정한 뼈대(직선 등)로 가정하고 출발하는 이 짓이 꿀 빠는 이유가 뭐냐면, 눈에 보이지도 않는 알 수 없는 형태주의 함수 $f$ 를 찰흙 빚듯 구불구불 맨땅에 헤딩하며 그리는 것보다, 그냥 공식 하나 적어두고 $\beta$ 빈칸들을 쏙쏙 맞추는 게 컴퓨터 입장에서도 훨씬 계산하기가 오지게 쉽기 때문입니다.

The potential disadvantage of a parametric approach is that the model we choose will usually not match the true unknown form of $f$.
하지만 편한 데엔 대가가 따르는 법! 이 모수적 파벌의 최고 약점은, 우리가 제멋대로 "직선일 거야!"라고 우겨서 선택한 그 모델 뼈대가, 실제 조물주가 짠 진짜 $f$ 의 구불구불한 꼬라지랑 **완전히 다를 가능성이 100%**라는 겁니다.

If the chosen model is too far from the true $f$, then our estimate will be poor.
만약 진짜 $f$ 는 미친 롤러코스터처럼 요동을 치는데 우리가 무식하게 젓가락(일직선) 하나 딱 얹어놨다면? 그 예측 결과물은 진짜 쓰레기통에나 처박힐 정도로 처참할 겁니다.

We can try to address this problem by choosing _flexible_ models that can fit many different possible functional forms for $f$.
그래서 사람들은 젓가락(일직선) 대신에 철사처럼 알아서 약간씩 구부러질 수 있는 좀 더 **유연한(Flexible)** 모델 뼈대를 들고나오는 꼼수로 이 똥볼을 커버 쳐보려고 노력합니다.

But in general, fitting a more flexible model requires estimating a greater number of parameters.
근데 문제가 하나 또 터집니다! 철사를 구부리려면 젓가락 1개론 안 되고 철사 마디마디마다 구부리는 힌지(파라미터)가 필요합니다. 즉, 유연해질수록 우리가 찾아내야 할 파라미터의 숫자가 기하급수적으로 폭발하게 되죠.

These more complex models can lead to a phenomenon known as _overfitting_ the data, which essentially means they follow the errors, or _noise_, too closely.
이 파라미터가 드글드글한 머리 아픈 복잡한 모델들은 데이터 점들에 너무 찰싹 달라붙으려 발악하다가, 결국 진리의 선이 아니라 아까 말했던 억울한 잡음 찌꺼기(노이즈, 운빨)까지 몽땅 다 외워버리는 최악의 참사인 **'과적합(Overfitting)'** 현상에 빠져 허우적거리게 됩니다.

These issues are discussed throughout this book.
적당히 딱딱한 것과, 너무 무르지도 않은 그 유연함 사이의 딜레마! 이것이 바로 이 책 끝까지 여러분을 피 말리게 괴롭힐 주제입니다.

Figure 2.4 shows an example of the parametric approach applied to the `Income` data from Figure 2.3.
그림 2.4를 한 번 보실까요? 우리가 앞서 본 `Income(수입)` 아저씨들 장부에다가 '모수적(직선 판자)' 접근을 폭력적으로 때려 박은 현장입니다.

We have fit a linear model of the form
우리는 다음과 같은 공식을 짜와서 저 점들 사이에 욱여넣었습니다:

$$ \text{income} \approx \beta_0 + \beta_1 \times \text{education} + \beta_2 \times \text{seniority} $$

![Figure 2.4](./img/Image_018.png)

**FIGURE 2.4.** _A linear model fit by least squares to the_ `Income` _data from Figure 2.3. The observations are shown in red, and the yellow plane indicates the least squares fit to the data._

**그림 2.4.** _`Income(수입)` 아저씨 데이터(빨간 점들) 사이에다가 '최소 제곱법'으로 아크릴 판때기(선형 모델)를 억지로 끼워 넣은 참상. 저 노랗고 빳빳한 판때기가 우리가 찍어낸 수입 예측 모델입니다._

**FIGURE 2.5.** _A smooth thin-plate spline fit to the_ `Income` _data from Figure 2.3 is shown in yellow; the observations are displayed in red. Splines are discussed in Chapter 7._

**그림 2.5.** _반대로 이건 그림 2.3에다가 플라스틱 수건(얇은 판 스플라인, thin-plate spline) 같이 유연한 모델을 던져서 덮은 겁니다(노란색). 더 굴곡이 있죠? 이 신기한 기술은 7장에서나 배울 겁니다._

Since we have assumed a linear relationship between the response and the two predictors, the entire fitting problem reduces to estimating $\beta_0, \beta_1$, and $\beta_2$, which we do using least squares linear regression.
우리가 대차게 "수입과 저 힌트들은 빳빳한 판때기(선형) 관계다!"라고 우겼기 때문에, 저 거평한 돗자리를 찾는 대공사가 고작 숫자 $\beta_0, \beta_1, \beta_2$ 세 개를 최소 제곱법으로 구하는 초급반 산수 문제로 확 쪼그라든 겁니다.

Comparing Figure 2.3 to Figure 2.4, we can see that the linear fit given in Figure 2.4 is not quite right: the true _f_ has some curvature that is not captured in the linear fit.
자, 아까 우리가 살짝 엿봤던 진리의 파란 돗자리(그림 2.3)랑 빙고 판때기(그림 2.4)를 비교해 볼까요? 그림 2.4의 노란 판때기는 솔직히 구립니다! 왜냐하면 원래 진리의 파란 함수 $f$ 는 허리가 살짝 휘어진 S라인(곡률)이 있는데, 저 빳빳한 노란 판때기(선형 적합)는 그 곡률을 1도 못 잡아내고 그냥 통나무처럼 서 있으니까요.

However, the linear fit still appears to do a reasonable job of capturing the positive relationship between `years of education` and `income`, as well as the slightly less positive relationship between `seniority` and `income`.
하지만 놀랍게도! 이 빳빳하고 멍청해 보이는 노란 판때기도 생각보다 선방을 쳐줍니다. '가방끈(교육)'이 길면 '월급'이 쭉 올라간다거나, '짬바(연공서열)'가 차면 수입이 살짝 오르는 그 긍정적인 오르막길 흐름(양의 관계) 자체는 기가 막히게 잘 짚고 넘어갔거든요.

It may be that with such a small number of observations, this is the best we can do.
게다가 빨간 점 30개라는 코딱지만 한 힌트들 속에서는 어쭙잖게 선을 구부리느니, 그냥 이렇게 무식한 판때기 하나를 때려 박는 게 차라리 최선의 성과일 수 있습니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.2 How Do We Estimate F](../trans2.html) | [2.1.2.2 Non-Parametric Methods >](../2_1_2_2_non-parametric_methods/trans2.html)
