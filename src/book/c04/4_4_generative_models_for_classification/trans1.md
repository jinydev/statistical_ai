---
layout: default
title: "trans1"
---

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/trans1.html) | [4.4.1 Linear Discriminant Analysis For P 1 >](4_4_1_linear_discriminant_analysis_for_p_1/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.4 Generative Models for Classification
# 4.4 분류를 위한 생성 모델 (Generative Models for Classification)

Logistic regression involves directly modeling $\text{Pr}(Y = k \mid X = x)$ using the logistic function, given by (4.7) for the case of two response classes. In statistical jargon, we model the conditional distribution of the response $Y$, given the predictor(s) $X$. We now consider an alternative and less direct approach to estimating these probabilities. In this new approach, we model the distribution of the predictors $X$ separately in each of the response classes (i.e. for each value of $Y$). We then use Bayes’ theorem to flip these around into estimates for $\text{Pr}(Y = k \mid X = x)$. When the distribution of $X$ within each class is assumed to be normal, it turns out that the model is very similar in form to logistic regression.
로지스틱 회귀는 반응 카테고리가 2개인 상황에서 로지스틱 함수 식 (4.7)을 이용하여 저 $Y$가 발생할 확률인 $\text{Pr}(Y=k \mid X=x)$ 를 아주 직접적으로 모델링합니다. 통계학 전문 용어로는, 우리가 예측 변수 $X$가 통째로 주어졌을 때 반응 $Y$에 대한 '조건부 분포'를 모델링한다고 일컫습니다. 이제 우리는 이 확률들을 추정하기 위해 다소 직접적이지 않고 우회하는 '대안적' 접근법을 심도 있게 다룹니다. 이 완전히 새로운 접근법에서는, 우리는 반응 클래스 측면(결과값 $Y$가 파산이냐, 정상인이냐의 조건)에서 각각 거꾸로 역산하여 예측 변수들 $X$의 분포를 역으로 추정해 모델링합니다. 그런 뒤에 베이즈 정리(Bayes' theorem) 공식을 사용해서 이것들을 홀딱 뒤집어 우리가 원래 원하던 관측치 기준 진짜 확률 모형, 즉 $\text{Pr}(Y=k \mid X=x)$ 의 추정치로 뒤집어 환산해 내는 묘기를 부립니다. 여기서 각각의 타겟 클래스 내부에 분포하는 예측 변수 집단 $X$의 성향이 완벽히 가우시안 정규 분포를 띠고 있다고 가정하면, 놀랍게도 이 빙글 돌아가는 방식으로 유도된 모형이 수학적으로 결국 로지스틱 회귀 수식 체계의 형태와 상당히 흡사하게 도출된다는 사실이 증명되었습니다.

Why do we need another method, when we have logistic regression? There are several reasons:
아니 다 좋은데, 이미 우리가 로지스틱 회귀라는 전천후 방패 무기를 가지고 있는데 왜 굳이 또 다른 변덕스러운 방법론 체계가 필요한 겁니까? 거기엔 몇 가지 심각한 통계적 이유가 있습니다:

- When there is substantial separation between the two classes, the parameter estimates for the logistic regression model are surprisingly unstable. The methods that we consider in this section do not suffer from this problem.
- 두 개의 클래스 분포 그룹 데이터가 칼로 무 자르듯 서로 선명하게 나누어져(Separation) 동떨어져 있을 때, 로지스틱 회귀 모형의 선형 추정 파라미터는 놀라울 정도로 요동치고 발산하며 불안정해집니다. 하지만 우리가 이번 섹션에서 배우게 될 새로운 이 기법들은 그런 분단 결함 문제에서 완전히 면역되어 고통받지 않습니다.
- If the distribution of the predictors $X$ is approximately normal in each of the classes and the sample size is small, then the approaches in this section may be more accurate than logistic regression.
- 만약 예측 변수 $X$들의 분포가 각각의 클래스들 타겟 종속 내부에서 거의 정규 분포(종 모양 곡선)에 가까운 상태를 띠고 있고 게다가 샘플 사이즈 수량(N) 마저 엄청 작을 경우라면, 이번 섹션의 접근법 모델이 오히려 로지스틱 회귀기보다 훨씬 더 정확할 수 있습니다.
- The methods in this section can be naturally extended to the case of more than two response classes. (In the case of more than two response classes, we can also use multinomial logistic regression from Section 4.3.5.)
- 마지막으로 이번 단원의 이 생성 방식 방법론들은 질적 타겟 반응 클래스가 2개를 한참 넘어서는 3개, 4개의 그 이상의 다중 클래스의 상황에서도 그 어떠한 억지스러움 없이 아주 부드럽고 자연스럽게 공식이 연장되어 확장 세팅됩니다. (물론 2개 초과 다중 클래스의 경우 방금 앞 4.3.5에서 배운 소프트맥스 다항 로지스틱 회귀를 써먹을 수도 있습니다.)

Suppose that we wish to classify an observation into one of $K$ classes, where $K \ge 2$. In other words, the qualitative response variable $Y$ can take on $K$ possible distinct and unordered values. Let $\pi_k$ represent the overall or _prior_ probability that a randomly chosen observation comes from the $k$th class. Let $f_k(x) \equiv \text{Pr}(X = x \mid Y = k)$ denote the _density function_ of $X$ for an observation that comes from the $k$th class. In other words, $f_k(x)$ is relatively large if there is a high probability that an observation in the $k$th class has $X \approx x$, and $f_k(x)$ is small if it is very unlikely that an observation in the $k$th class has $X \approx x$. Then _Bayes’ theorem_ states that
이제 우리가 예측 관측치를 단 2개가 아니라 $K$ 개의 광활한 클래스 (이때 $K \ge 2$ 임) 중 하나로 분류하고 싶다고 열망한다 쳐봅시다. 다른 말로 하자면, 질적 반응 변수 타겟 $Y$가 아무런 대소 순서가 없는 $K$ 가지의 확연히 다른 가능성의 성질 값을 지닐 수 있다는 점입니다. 여기서 $\pi_k$ 를 그냥 무작위로 아무나 하나 눈 감고 뽑았을 때 그 친구가 $k$ 번째 클래스 출신일 전체적인 혹은 **사전(prior)** 확률을 나타낸다고 가정합니다. 그리고 $f_k(x) \equiv \text{Pr}(X = x \mid Y = k)$ 라고 두고, 이 친구를 "$k$번째 그룹 타겟 클래스 출신에서 굴러나온 개인 관측치가 지닌 특성 $X$에 대한 **밀도 함수(Density function)**" 라고 정의해 봅시다. 알아먹게 풀어서 쓰자면, $k$번째 병에 걸린 어느 병동의 특성 그룹 덩어리 안에서, 하필 이 환자의 특성 심박수 수치가 $X \approx x$ 와 아주 절묘하게 비슷할 확률이 졸라 높은 상황이라면 저 밀도 함수 우도 수치인 $f_k(x)$ 가 상대적으로 아주 거대해진다는 말이고, 반대로 그 병에 걸린 사람 치고는 도무지 낼 수가 없는 기괴한 $X$ 수치를 냈을 경우엔 $f_k(x)$ 함수값이 아주 작아질 거라는 말입니다. 그리고 나서 우린 이 두 통계 인자를 우당탕 섞기 위해 위대한 **베이즈 정리(Bayes' theorem)** 를 소환하여 당당하게 이 공식 수식을 내지릅니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^{K} \pi_l f_l(x)} \quad (4.15)
$$

In accordance with our earlier notation, we will use the abbreviation $p_k(x) = \text{Pr}(Y = k \mid X = x)$; this is the _posterior_ probability that an observation $X = x$ belongs to the $k$th class. That is, it is the probability that the observation belongs to the $k$th class, _given_ the predictor value for that observation.
우리가 조금 전 이전 단원들에서 편의상 계속 쭉 썼던 약어 표기법과 부합되게, 베이즈 정리에서 튀어나온 이 최후의 통계 결괏값 $\text{Pr}(Y = k \mid X = x)$ 도 역시나 짧게 퉁쳐서 $p_k(x)$ 라는 명칭으로 쓰겠습니다. 이것은 어떤 성질 $X=x$ 를 띈 관측치가 결국 우리가 목표로 하는 $k$번째 예측 타겟 클래스 집단에 최종 스코어로 속하게 될 것을 말해주는 가장 최신의 통찰인 **사후(posterior)** 확률이라 일컫습니다. 다시 말해, 그 사람에 대한 특정 예측 변숫값들이 주어졌을 때($given$), 그놈이 저쪽 무리 클래스 출신임에 틀림없을 것이라는 최종 검찰 마감 확률입니다.

We know from Chapter 2 that the Bayes classifier, which classifies an observation $x$ to the class for which $p_k(x)$ is largest, has the lowest possible error rate out of all classifiers. In the following sections, we discuss three classifiers that use different estimates of $f_k(x)$ in (4.15) to approximate the Bayes classifier: _linear discriminant analysis, quadratic discriminant analysis,_ and _naive Bayes_.
우리는 아득히 먼 2장에서, 관측치 인자 $x$를 집어넣어 저 맨 마지막 괄호 $p_k(x)$ 사후 점수가 가장 압도적으로 크게 터져 나오는 우승자 클래스로 분류 낙인을 찍어버리는 베이즈 분류기(Bayes classifier)가 지상에 존재하는 현존 가능한 모오든 분류기 모델들을 통틀어 그론적으로 가장 낮은 예측 오류 에러율(error rate)의 극한을 자랑한다는 것을 이미 피나게 배웠습니다. 이어질 후속 섹션들에서, 우리는 (4.15) 베이즈 방정식 속에 들어간 저 미지의 역추적 밀도 곡선 $f_k(x)$ 덩어리를 조금씩 각기 다른 가정과 방식으로 멋대로 추정해내서 그 신성한 베이즈 분류기 성역 한도에 끝없이 인위적으로 근사시키려(approximate) 시도하는 세 가지 현실적인 꼼수 분류기들을 논의할 것입니다: 그것은 바로 **선형 판별 분석(LDA)**, **이차 판별 분석(QDA)**, 그리고 **나이브 베이즈(Naive Bayes)** 라 불리는 기법들입니다.

---

### 4.4.1 Linear Discriminant Analysis for p = 1 (p=1인 경우의 선형 판별 분석)

### 4.4.2 Linear Discriminant Analysis for p > 1 (p>1인 경우의 선형 판별 분석)

### 4.4.3 Quadratic Discriminant Analysis (이차 판별 분석)

### 4.4.4 Naive Bayes (나이브 베이즈)

---

## Sub-Chapters (하위 목차)

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/trans1.html) | [4.4.1 Linear Discriminant Analysis For P 1 >](4_4_1_linear_discriminant_analysis_for_p_1/trans1.html)
