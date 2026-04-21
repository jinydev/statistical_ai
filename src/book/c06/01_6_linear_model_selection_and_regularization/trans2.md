---
layout: default
title: "trans2"
---

# 6 Linear Model Selection and Regularization
# 6 선형 모델 선택 및 규제: 가지치기와 군기 반장 (Vibe Coding Version)

In the regression setting, the standard linear model

$$
Y = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon \quad (6.1)
$$

is commonly used to describe the relationship between a response $Y$ and a set of variables $X_1, X_2, \dots, X_p$. We have seen in Chapter 3 that one typically fits this model using least squares. 
데이터 세상에서 과녁인 $Y$(정답)를 맞추려고 $X_1, X_2, \dots, X_p$라는 이름의 요원(변수)들을 쫙 펼쳐놓을 때, 우리는 흔히 가장 클래식한 공식 (6.1)의 **표준 선형 모델(Standard Linear Model)** 을 차출합니다. 이건 마치 훈련병들을 일렬로 세우고 각각에게 가중치 무기($\beta$)를 쥐여주는 것과 같죠. 3장에서 우리는 이미 **최소 제곱법(Least Squares)** 이라는 노련한 교관이 이 모델을 어떻게 혹독하게 훈련(피팅)시키는지 찐하게 경험했습니다.

In the chapters that follow, we consider some approaches for extending the linear model framework. In Chapter 7 we generalize (6.1) in order to accommodate non-linear, but still additive, relationships, while in Chapters 8 and 10 we consider even more general non-linear models. However, the linear model has distinct advantages in terms of inference and, on realworld problems, is often surprisingly competitive in relation to non-linear methods. Hence, before moving to the non-linear world, we discuss in this chapter some ways in which the simple simple linear model can be improved, by replacing plain least squares fitting with some alternative fitting procedures. 
이어지는 후반부 시즌(7장, 8장, 10장)에서 우리는 이 선형 모델이라는 옛날 방식 굴레를 박차고 나가, 곡선으로 휘어지고 차원을 넘나드는 **'비선형(Non-linear)'** 이라는 화려한 SF 영화 같은 세계로 넘어갈 예정입니다. 하지만 잠깐만요! 이 오래된 1차원 선형 모델은 '원인과 결과 해석(Inference)'에 있어서만큼은 타의 추종을 불허하는 압도적인 명쾌함(투명성)을 가지고 있습니다. 그래서 현실의 거친 데이터 정글에서도 화려한 최신 비선형 기법들과 붙었을 때 의외로 팽팽하게 맞서는 괴력을 발휘하곤 하죠. 
따라서 삐까뻔쩍한 비선형 차원으로 훌쩍 로켓을 타고 떠나버리기 전에, 이번 6장에서는 **이 투박한 초기 선형 모델에 최신식 터보 엔진을 달아주는 업그레이드 작업**을 해보려 합니다. 바로 "최소 제곱법"이라는 고인물 교관 체제를 내쫓고, 그 자리에 아주 신박하고 세련된 대안 훈련 기법(Alternative Fitting Procedures)들을 새롭게 투입하는 개조 공사입니다!

Why might we want to use another fitting procedure instead of least squares? As we will see, alternative fitting procedures can yield better _prediction accuracy_ and _model interpretability_. 
대체 왜 멀쩡하게 일 잘하던 최소 제곱법 교관을 해고하고 다른 교관(피팅 방식)을 데려오려고 안달일까요? 곧장 눈으로 확인하게 되겠지만, 이 새로운 교관들은 모델의 **‘실전 예측 명중률(Prediction Accuracy)’** 과 **‘가독성/해석 투명도(Model Interpretability)’** 라는 두 마리 토끼를 한 방에 기가 막히게 잡아내기 때문입니다.

- _Prediction Accuracy_: Provided that the true relationship between the response and the predictors is approximately linear, the least squares estimates will have low bias. If $n \gg p$—that is, if $n$, the number of observations, is much larger than $p$, the number of variables—then the least squares estimates tend to also have low variance, and hence will perform well on test observations. However, if $n$ is not much larger than $p$, then there can be a lot of variability in the least squares fit, resulting in overfitting and consequently poor predictions on future observations not used in model training. And if $p > n$, then there is no longer a unique least squares coefficient estimate: there are infinitely many solutions. Each of these least squares solutions gives zero error on the training data, but typically very poor test set performance due to extremely high variance. By _constraining_ or _shrinking_ the estimated coefficients, we can often substantially reduce the variance at the cost of a negligible increase in bias. This can lead to substantial improvements in the accuracy with which we can predict the response for observations not used in model training. 
- **예측 타점 (Prediction Accuracy)**: 세상의 법칙이 어느 정도 1차원 선형 구조에 맞물려 돌아간다면, 최소 제곱법이 찾아낸 각도는 편견(Bias)이 아주 낮습니다. 여기에 더해 훈련병(변수, $p$)보다 총알 데이터(관측치 수, $n$)가 압도적으로 풍부한 $n \gg p$ 전장이라면? 모델은 널뛰기 진동(Variance)을 멈추고 묵직한 돌직구를 날려 실전 테스트에서도 연전연승합니다. 
하지만 총알($n$)이 훈련병($p$) 숫자를 겨우 간당간당 윗도는 열악한 세팅이라면 이야기가 무참히 달라집니다. 최소 제곱 부대는 거대한 변동성(Variability)이라는 풍랑에 흔들리며 '과적합(Overfitting)'이라는 최악의 자아도취 상태에 빠지고 맙니다. 훈련장 타겟은 다 맞춰놓고, 정작 내일 투입될 실전 전장 타겟(새로운 관측치)엔 아예 엉뚱한 총을 갈기고 마는 형편없는 사격수가 되는 거죠. 
심지어 데이터 총알($n$)보다 훈련병($p$)이 더 득실거리는 배보다 배꼽이 큰 $p > n$ 환경에서는? 아예 모델의 해답(Coefficient estimate) 자체가 붕괴해 무한대의 쪼개진 해결책 파편들이 난무해버립니다. 이 파편들은 훈련 과녁에서는 에러 '0' 이라는 눈속임을 하지만, 실전에서는 미친 듯이 치솟는 광기의 널뛰기 폭등(Extremely high variance) 때문에 장렬히 폭망하고 맙니다. 
바로 이때! 계수(Coefficient)라는 **예측 무기들의 파워를 멱살 잡아 강제로 짓누르고 제약(Constraining)하거나, 헬륨 가스 빼듯 확 쪼그라뜨리는(Shrinking)** 군기 반장 기법을 쓰게 됩니다. 아주 눈곱만큼의 편견 타점(Bias)을 손해보는 대신, 그 미친 듯 요동치던 모델의 널뛰기 변동성(Variance)을 한 방에 잠재우는 엄청난 이득 교환비! 결과적으로 이는 실전 미개척 데이터를 맞이했을 때 우리의 타격 적중률 스펙을 엄청나게 상승(Substantial improvements)시키는 마법의 엔진오일 역할을 합니다.

- _Model Interpretability_: It is often the case that some or many of the variables used in a multiple regression model are in fact not associated with the response. Including such _irrelevant_ variables leads to unnecessary complexity in the resulting model. By removing these variables—that is, by setting the corresponding coefficient estimates to zero—we can obtain a model that is more easily interpreted. Now least squares is extremely unlikely to yield any coefficient estimates that are exactly zero. In this chapter, we see some approaches for automatically performing _feature selection_ or _variable selection_—that is, for excluding irrelevant variables from a multiple regression model. 
- **모델 가독성과 해석 능력 (Model Interpretability)**: 다중 회귀라는 빅사이즈 항공모함 안에는 별의별 잡다한 녀석들(Variables)이 다 타고 있습니다. 하지만 슬프게도 그들 중 상당수는 과녁(Response)과 아무런 접점 하나 엮인 거 없는 쓸고퀄 잉여 승객들(not associated)입니다. 이따위 관련 1도 없는 잉여 관종(irrelevant) 승객들을 꾸역꾸역 태우고 가는 건 결국 모델 항공모함 내부 구조만 불필요하게 꼬여대고 복잡(unnecessary complexity)해지는 자승자박 꼴입니다. 
가장 멋진 해결책은 이 잉여 승객들을 과감하게 바다로 밀어 던져버리는(Removing) 겁니다. 즉, 걔네들 머리 위 통행증 스펙트럼(Coefficient estimates)을 아예 잔인하게 **숫자 '0'으로 리셋 박아 버리는 세팅(Setting to zero)** 입니다! 이를 통해 우리는 뼈대만 남아 아주 날렵하고 해독하기 직관적이고 쉬워진(More easily interpreted) 슬림형 모형을 손에 넣습니다. 
그런데 문제가 뭐냐? 순진한 옛날 도구인 최소 제곱법(Least squares) 로봇은 무작정 식을 최적화할 뿐, 누군가의 계수를 칼로 자르듯 예리하게 정확히 통째로 '0 (Exactly zero)'으로 만들 줄 아는 센서 파츠가 태생적으로 아예 장착되어 있지 않다는 뼈아픈 함정입니다. 그래서 우리는 이번 챕터에서 이 무쓸모 잉여 승객들을 발가벗겨 모델에서 자동으로 강제 축출(Excluding) 추방 시켜버리는, 이름하여 **특징 선택(Feature selection)** 또는 **변수 가지치기(Variable selection)** 라는 쾌도난마의 스마트 장비(Approaches) 조작 체계들을 집중 관찰하게 됩니다.

There are many alternatives, both classical and modern, to using least squares to fit (6.1). In this chapter, we discuss three important classes of methods. 
최소 제곱법(OLS)을 맹목적으로 추종하는 태세를 버리고, 식 6.1에 꽂을 수 있는 대안 플랜 파츠(Alternatives)들은 고전적인 낡은 철퇴부터 최첨단 레이저건까지 부지기수로 깔려 있습니다. 우리는 그중에서도 이 판도를 뒤흔들 가장 결정적인 3대 메인 스트림 학파(Classes of methods)들을 무대 위로 소환해 해부해보려 합니다.

- _Subset Selection_. This approach involves identifying a subset of the $p$ predictors that we believe to be related to the response. We then fit a model using least squares on the reduced set of variables. 
- **1. 치열한 오디션 선발대 "부분집합 선택 (Subset Selection)"**: 전체 $p$ 명의 참가자(Predictors) 무리 중에서 오직 타겟 Y를 향해 쏠 줄 아는 진짜 실력파 '진성 연관 멤버' 들만의 엘리트 미니 그룹(A subset)을 레이더로 스캔해 잡아내는 전략입니다. 그다음 그 축소되고 선별된 정예 멤버 군단(Reduced set)만을 판 위에 세워두고 최소 제곱법(Least squares)으로 컴팩트한 맞춤형 과녁 타격을 시도하게 됩니다.

- _Shrinkage_. This approach involves fitting a model involving all $p$ predictors. However, the estimated coefficients are shrunken towards zero relative to the least squares estimates. This shrinkage (also known as _regularization_) has the effect of reducing variance. Depending on what type of shrinkage is performed, some of the coefficients may be estimated to be exactly zero. Hence, shrinkage methods can also perform variable selection. 
- **2. 핏줄까지 조여버리는 군기 반장 "축소 기법 (Shrinkage)"**: 일단 이 방식은 쿨하게 거대 $p$ 명의 변수 무리를 한 명도 남김없이 통째로 다 끌고(involving all $p$ predictors) 출전합니다. 대신 이면적으로 어마무시한 페널티 통제 장치를 걸어, 기존에 치솟던 가중치 게이지(Coefficients)들을 절대 원점 거점구역인 눈금 '0' 바닥을 향해 몹시 강제로 윽박질러 쪼그라뜨리는 침전 압박(Shrunken towards zero)을 가합니다. 이처럼 팽창된 권력을 찍어 누르는 위축 수단(이 업계에선 흔히 **규제(Regularization)** 라는 섬뜩한 이름으로 불립니다)은 모델 전체의 진폭 오류 거품(Variance)을 눈녹듯 증발시키는 엄청난 치유 효과를 지닙니다. 어떤 방식의 족쇄(Shrinkage type)를 채우느냐에 따라 특정 변수의 권력(계수)은 소수점조차 남기지 못한 채 칼같이 단박에 '0 (Exactly zero)' 에 못 박혀 즉사하기도 합니다. 아예 존재감을 삭제 당하는 셈이죠. 따라서 이 규제 기법은 무의식중에 변수 가지치기 축출(Variable selection) 역할까지 1타 2피로 달성하는 사기 캐릭터급 능력을 발휘합니다.

- _Dimension Reduction_. This approach involves _projecting_ the $p$ predictors into an $M$-dimensional subspace, where $M < p$. This is achieved by computing $M$ different _linear combinations_, or _projections_, of the variables. Then these $M$ projections are used as predictors to fit a linear regression model by least squares. 
- **3. 데이터 용광로 차원 압축기 "차원 축소 (Dimension Reduction)"**: 방대한 $p$ 가닥의 개별 변수들을 그대로 쓰지 않고 이들을 통째로 거대한 데이터 압축 용광로에 밀어 넣어 버리는 조치입니다. 그럼으로써 기존 $p$ 보다 확연히 차원 껍데기가 작은 $M$ 차원($M < p$) 이라는 완전히 새로운 형태의 가상 우주 공간(Subspace) 안으로 투과 및 재조합 재배치 투사(Projecting) 시킵니다. 기존 날것의 변수들을 이리저리 교잡, 결합해 완전히 이질적인 새로운 신소재 인공 예측 파츠인 $M$ 개의 선형 융합 덩어리(Linear combinations / Projections)를 뽑아 연성해 내는 거죠. 그러고 나선 이 $M$ 개의 초압축 신규 인공 벡터 엑기스들을 마치 메인 투수(Predictors)인 양 세워두고, 익숙한 1차 최소 제곱 선형 모델 베이스 위에서 최종 저격을 완료 짓는(Fit) 심오하고 매혹적인 스킬 구조입니다.

In the following sections we describe each of these approaches in greater detail, along with their advantages and disadvantages. Although this chapter describes extensions and modifications to the linear model for regression seen in Chapter 3, the same concepts apply to other methods, such as the classification models seen in Chapter 4. 
곧바로 이어질 막(Sections)들에서, 우리는 이 3가지 거대 판도를 뒤바꿀 병기 시스템(Approaches)들이 각각 어떠한 치명적 무기이자 아킬레스건(Advantages and Disadvantages)을 감추고 있는지 낱낱이 해부하고 심층 스캐닝에 들어갈 대작전을 개시합니다. 
> 💡 비록 지금 6장 이 지면 모퉁이가, 3장에서 뼛속까지 겪어본 그 낡은 '회귀용 선형 모델(Linear model for regression)'의 틀을 개조 조립 튜닝 확장(Extensions and modifications)하는 작업에 초점이 쏠려 있지만! 여기서 터득할 심오한 규제와 변수 통제라는 우주적 매커니즘의 근본 진리(Same concepts)는, 앞서 4장에서 우리가 혈투를 벌이던 로지스틱이나 판별분석 같은 분류 클래스 병기 모델(Classification models)들 위에서도 토시 하나 안 틀리고 똑.같.이 장착 투입 발사 적용(Apply to)될 수 있는 마스터키 범용 기술이라는 점, 절대 잊지 마세요!

> [!NOTE]
> 1 번역 노트: $p \gg n$ 환경 (초고차원 매트릭스의 악몽). 훈련병 $p$ 가 총알 관측치 $n$ 보다 많으면, 제곱합 에러 0 을 만드는 최소 제곱 솔루션 답안지는 무한개로 다차원 분리 파생되는 공포가 펼쳐집니다. 하지만 그중에서도 '가중치 계수의 제곱합' 크기를 극한까지 최소치로 억제 조율해 낸 특정 예시 솔루션(the smallest sum)은 실전에서 의외로 상당히 괴물 같은 성능(quite well)을 내기도 합니다. (10.8 절 참고)

---

## Sub-Chapters (하위 목차)

### 6.1 Subset Selection (부분집합 선택)
* [문서로 이동하기](./6_1_subset_selection/trans2.html)

### 6.2 Shrinkage Methods (축소 기법)
* [문서로 이동하기](./6_2_shrinkage_methods/trans2.html)

### 6.3 Dimension Reduction Methods (차원 축소 기법 분석)
* [문서로 이동하기](./6_3_dimension_reduction_methods/trans2.html)

### 6.4 Considerations in High Dimensions (초고차원 환경 분석 구조에서의 한계점과 고려사항)
* [문서로 이동하기](./6_4_considerations_in_high_dimensions/trans2.html)

### 6.5 Lab: Linear Models and Regularization Methods (실습: 데이터 사이언티스트를 위한 파이썬 선형 모델 선택 및 규제법 랩)
* [문서로 이동하기](./6_5_lab_linear_models_and_regularization_methods/trans2.html)

### 6.6 Exercises (변수 축소 기법들의 기본 응용 문제 수리적 종합 지식 검증 코스 모음집)
* [문서로 이동하기](./6_6_exercises/trans2.html)
