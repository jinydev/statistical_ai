---
layout: default
title: "trans2"
---

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/trans2.html) | [4.4.1 Linear Discriminant Analysis For P 1 >](4_4_1_linear_discriminant_analysis_for_p_1/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.4 Generative Models for Classification
# 4.4. 분류를 위한 생성 모델 (역추적의 마법사들)

Logistic regression involves directly modeling $\text{Pr}(Y = k \mid X = x)$ using the logistic function, given by (4.7) for the case of two response classes.
우리가 방금까지 지겹게 달렸던 '로지스틱 회귀' 전략은, "A냐 B냐" 두 선택지가 있는 환자에게 "그 사람이 단서 $X=x$를 들이밀었을 때 무조건 $Y=k$번 방으로 떨어질 확률 $\text{Pr}$이 얼마인가?"를 로지스틱 S자 함수 식 (4.7)을 써서 다이렉트로 정면 돌파해 곧바로 확률을 찍어 맞추는 방식이었습니다.

In statistical jargon, we model the conditional distribution of the response $Y$, given the predictor(s) $X$.
전문가들이 쓰는 통계학적 잘난 척 용어로 이 행위를 멋들어지게 포장하면, "단서 $X$가 **조건으로 딱 주어졌을 때**, 반응 변수 $Y$의 사후 조건부 분포를 직접 타격해 모델링한다"고 묘사합니다.

We now consider an alternative and less direct approach to estimating these probabilities.
그런데 이쯤에서, 우리는 항상 문 앞을 막고 버티는 이 다정한 다이렉트 정면 돌파 방식을 꺾어버리고, **훨씬 더 간접적이고 뒷문으로 빙 돌아서** 이 확률을 역으로 끄집어내는 아예 새로운 대안적 세계관 접근법 하나를 고민해 보려 합니다. 

In this new approach, we model the distribution of the predictors $X$ separately in each of the response classes (i.e. for each value of $Y$).
이 기상천외한 '생성 모델(Generative Models)'이라는 새로운 역발상 접근법 방책에서는, 질문의 방향 자체가 완전히 뒤집힙니다. 즉 "각각의 반응 결과 클래스 $Y$방 안으로 먼저 들어간 다음, 그 범인 소굴 안에서 서식하는 예측 단서 점수 $X$들이 대체 그 방에서 어떤 식의 특징적인 분포로 뭉쳐 노닐고 있는가?"를 각 방마다 분리해 따로따로 추적 검사하고 모델링하는 짓을 벌입니다.

We then use Bayes’ theorem to flip these around into estimates for $\text{Pr}(Y = k \mid X = x)$.
각 방에서 $X$가 노는 그 단서들의 분포 밀도를 파악하고 나면, 우리는 인류 최고 수학의 걸작인 **베이즈 정리(Bayes’ theorem)** 의 지팡이를 휘둘러 이 퍼즐 그림을 역으로 뒤집어엎습니다. 그러면 짜잔! 빙 돌았지만 결과적으로 우리가 제일 궁금해했던 최종 목표인 "이 $X$ 단서를 들고 온 이 환자가 과연 $k$번째 클래스 방 소속일 확률 $\text{Pr}(Y = k \mid X = x)$ 은 얼마인가?"의 최종 마법 확률 결과가 기적처럼 계산되어 산출 도미노로 굴러떨어집니다.

When the distribution of $X$ within each class is assumed to be normal, it turns out that the model is very similar in form to logistic regression.
재밌는 꼼수로, 만일 각 범죄자 $Y$ 방 안에 숨어 서식하는 $X$ 단서들의 분포가 아리따운 종 모양의 '정규 분포(Normal)' 띠를 따른다고 살짝 가정을 치면, 빙 돌아서 역으로 유도된 이 괴랄한 새 모형 껍데기가 우리가 익히 알던 그 징그러운 '로지스틱 회귀' 공식의 골격과 굉장히 흡사하고 똑떨어지는 형태로 판명되는 것을 목격하게 됩니다.

Why do we need another method, when we have logistic regression? There are several reasons:
아니, 로지스틱 회귀같이 직관적이고 훌륭한 최강의 무기가 버젓이 있는데 왜 굳이 머리 복잡하게 역추적을 타고 베이즈를 씌우는 이 복잡한 대안 모델링 방식을 배워야 하나요? 여기에는 타당한 세 가지의 불만 이유가 섞여 있습니다:

- When there is substantial separation between the two classes, the parameter estimates for the logistic regression model are surprisingly unstable. The methods that we consider in this section do not suffer from this problem.
- **첫째:** 클래스 두 부류(예: 악당과 선인) 집단이 데이터 그림 상에서 서로 너무 멀리 깨끗하게 분리(separation)되어 잘 떨어져 있을 경우, 당황스럽게도 영리한 로지스틱 회귀 모델 기계의 파라미터 추정치가 허둥대며 놀라울 정도로 덜덜 떨며 '불안정해지는' 치명적 버그 쇼크가 벌어집니다. 반면 4.4 단원에서 다룰 생성 모델 방법들은 방 안의 분포도를 따로 구하기에 이런 바보 같은 당황을 하지 않습니다.

- If the distribution of the predictors $X$ is approximately normal in each of the classes and the sample size is small, then the approaches in this section may be more accurate than logistic regression.
- **둘째:** 만약 운 좋게도 클래스 각 방 안에 널브러진 예측 단서 $X$의 생김새 분포가 예쁜 '정규 분포' 구조를 대충 따르고 있고, 거기다 주워 담은 훈련 데이터 샘플링 인구 모집단 갯수 크기(`n`)가 터무니없이 '작다' 면, 놀랍게도 이 빙 돌아가는 생성 모델 접근법들이 로지스틱 다이렉트 방식보다 확률의 타겟팅 핀을 훨씬 더 정밀하게 맞추는 위력을 발휘합니다.

- The methods in this section can be naturally extended to the case of more than two response classes. (In the case of more than two response classes, we can also use multinomial logistic regression from Section 4.3.5.)
- **셋째:** 생성 모델은 태생적으로 방정식을 따로 구하기 때문에, 결과 타깃 범주 클래스가 3개든 100개든 이 이상 늘어나는 잔인한 다중 클래스 케이스 환경에서도 굉장히 무덤덤하고 스무스하게 뻗어나가 자연스러운 확장이 지원됩니다. (물론 우리는 방금 전 4.3.5 섹션에서 로지스틱 회귀를 가지고도 다항(multinomial) 억지 확장 버전을 썼지만, 생성 모델 쪽이 구조상 본래 그런 쪽으로 설계된 뼈대를 가지고 있습니다.)

Suppose that we wish to classify an observation into one of $K$ classes, where $K \ge 2$.
자, 우리가 눈먼 관측치 환자 데이터를 데려와서 총 $K$개의 방(단, $K \ge 2$) 중 유일무이한 하나로 정확히 지목하여 분류하고 싶다고 깊이 상상해 보십시오.

In other words, the qualitative response variable $Y$ can take on $K$ possible distinct and unordered values.
말을 꼬아보자면, 반응 카테고리 기호 $Y$가 서열이 없고 서로 구별되는 성질인 $K$개의 클래스 정답지 중 하나를 취할 수 있다는 뜻입니다.

Let $\pi_k$ represent the overall or _prior_ probability that a randomly chosen observation comes from the $k$th class.
이때 통계학 기호 $\pi_k$는 길거리에서 눈을 감고 사람을 하나 툭 잡았을 때 속사정 묻지도 따지지도 않고 그가 $k$번째 방 출신일 근본적인 **'사전(prior) 베이스 확률'** 을 의미하게 됩니다.

Let $f_k(x) \equiv \text{Pr}(X = x \mid Y = k)$ denote the _density function_ of $X$ for an observation that comes from the $k$th class.
그리고 함수 $f_k(x) \equiv \text{Pr}(X = x \mid Y = k)$ 는 이미 $k$번째 클래스 방에 배정되어 진을 치고 들어간 관측치들에 대해, 단서 성적 $X$ 값 자체가 어떻게 분포해 있는지 그 우드락 모형 모양(밀도 함수, Density Function)을 그리는 역할을 표기합니다.

In other words, $f_k(x)$ is relatively large if there is a high probability that an observation in the $k$th class has $X \approx x$, and $f_k(x)$ is small if it is very unlikely that an observation in the $k$th class has $X \approx x$.
이게 뭔 수학이냐고요? 겁먹지 마세요. 이 $f_k(x)$ 함수의 값이 하늘을 뚫고 솟구쳐 크다는 건, "$k$번째 악당 방에 있는 녀석들을 털어보면 그놈들은 십중팔구 단서 특징이 $X \approx x$ 주변에 우글우글 몰려 노닌다!"라는 뜻이고, 반대로 수치가 바닥을 친다는 건 "$k$방 녀석들은 절대 $x$ 같은 특징을 띄지 않을 구역이다"라는 매우 직관적인 프로파일링 단서를 뜻합니다.

Then _Bayes’ theorem_ states that
그러면, 이제 위대한 **베이즈 정리(Bayes’ theorem)** 의 거울 마법이 발동되어 다음과 같은 기적의 식을 탄생시킵니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^{K} \pi_l f_l(x)} \quad (4.15)
$$

In accordance with our earlier notation, we will use the abbreviation $p_k(x) = \text{Pr}(Y = k \mid X = x)$; this is the _posterior_ probability that an observation $X = x$ belongs to the $k$th class.
수식이 너무 길어 숨차니까, 우리는 이전 섹션들의 콧대 높은 전통 표기법 약속에 발맞추어 저 좌변의 긴 식을 짧고 쿨하게 $p_k(x) = \text{Pr}(Y = k \mid X = x)$ 라고 줄임말을 쓸 것입니다. 이 결과값 조각을 우리는 한 관측치 $X$가 증거 $x$ 특징 단서를 주머니에 푹 찔러넣고 제시했을 때, 그가 결국 $k$번 방 타깃이 됨을 확증하는 판결, 이른바 **'사후(posterior)'** 확률이라고 공식적으로 명명합니다.

That is, it is the probability that the observation belongs to the $k$th class, _given_ the predictor value for that observation.
말 그대로 현장에 남은 "단서(예측 변수 특징치)" 가 관측되어 확증으로 떡 하니 **수집(주어졌을)** 때, 재판관이 그를 $k$번방 범인으로 구형 지목할 수리적 결론 확률이 도출된다는 것입니다.

We know from Chapter 2 that the Bayes classifier, which classifies an observation $x$ to the class for which $p_k(x)$ is largest, has the lowest possible error rate out of all classifiers.
우리는 이미 아득한 옛날 2장 시절에 이 진리를 배웠습니다. 불쌍한 관측치 $x$를 데려다 놓고 모든 방 번호를 돌려본 다음, 저 사후 확률 판결 수치 $p_k(x)$ 가 제일 크게 솟구친 우승자 1등 방에다가 그를 미련 없이 던져버리는 이른바 '베이즈 분류기(Bayes classifier)'야말로, 인간이 상상할 수 있는 모든 분류 예측 장치 기계들 중에서 **우주 최강으로 가장 무적의 고달픈 최소 오답 오류율** 한계점을 달성하는 전설의 명검임을 말입니다.

In the following sections, we discuss three classifiers that use different estimates of $f_k(x)$ in (4.15) to approximate the Bayes classifier: _linear discriminant analysis, quadratic discriminant analysis,_ and _naive Bayes_.
결국 우리의 승패는 (4.15) 저 베이즈 마법 식 안에 숨겨진 진짜배기 $f_k(x)$ 모형 함수를 우리가 얼마나 잘 추정해 끼워 넣느냐에 있습니다. 다가오는 심장 쫄깃한 다음 섹션 구역들에서, 우리는 저 $f_k(x)$ 밀도 퍼즐 조각을 각각 다르게 가정하고 묘사해 어떻게든 진짜 베조스 명검 모델 분류기에 비비고 근사 도달하려 치열하게 시도하는 3대장 분류기, 즉 **선형 판별 분석(LDA)**, **이차 판별 분석(QDA)**, 그리고 **나이브 베이즈(Naive Bayes)** 라는 무기들을 세세히 차례로 해부하며 논의할 예정입니다.

---

### 4.4.1 Linear Discriminant Analysis for p = 1

### 4.4.2 Linear Discriminant Analysis for p > 1

### 4.4.3 Quadratic Discriminant Analysis

### 4.4.4 Naive Bayes

---

## Sub-Chapters (하위 목차)

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/trans2.html) | [4.4.1 Linear Discriminant Analysis For P 1 >](4_4_1_linear_discriminant_analysis_for_p_1/trans2.html)
