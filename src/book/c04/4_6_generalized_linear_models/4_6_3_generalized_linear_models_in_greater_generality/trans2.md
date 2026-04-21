---
layout: default
title: "trans2"
---

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/trans2.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.6.3 Generalized Linear Models in Greater Generality
# 4.6.3 더 넓은 세계로의 확장: 우주 융합 끝판왕 '일반화 선형 모델 (GLM)'의 진짜 정체

We have now discussed three types of regression models: linear, logistic and Poisson.
자, 숨 가쁘게 달려오면서 우리는 방금 전까지 전장을 휩쓸었던 3개의 강력한 예측 병기, 즉 직선기둥 '선형 회귀', 누르기 달인 '로지스틱 회귀', 그리고 카운트 킬러 '포아송 회귀' 기계 장치 시스템에 대해 낱낱이 파헤쳐 논의해 봤습니다.

These approaches share some common characteristics:
그런데 말입니다, 이 전혀 다르게 생겨 먹은 듯한 3개의 기계들이, 사실 뜯어보면 아주 소름 돋게 똑같은 유전자(공통 특성) 2가지를 지니고 있다는 사실을 눈치채셨나요?

1. Each approach uses predictors $X_1, \dots, X_p$ to predict a response $Y$. We assume that, conditional on $X_1, \dots, X_p$, $Y$ belongs to a certain family of distributions. For linear regression, we typically assume that $Y$ follows a Gaussian or normal distribution. For logistic regression, we assume that $Y$ follows a Bernoulli distribution. Finally, for Poisson regression, we assume that $Y$ follows a Poisson distribution.
**1. 출신 성분(족보)을 가린다!**
모든 기계는 단서($X$)를 집어넣고 타깃($Y$)을 쏘아 맞춥니다. 그런데 기계마다 "이 결과물 $Y$ 는 무조건 특정 확률 가문의 피를 이어받았을 거야!"라는 강압적인 통제(가정)를 씌웁니다. 
- 통나무 **선형 회귀**는 "우리 타깃은 명문 **가우시안(정규) 분포** 집안 출신뿐이야!" 라고 우깁니다.
- 조폭 **로지스틱 회귀**는 "내 과녁은 동전 던지기 판인 **베르누이 분포** 족속이지!" 라고 못 박습니다.
- 마지막 최신 병기 **포아송 회귀**는 "여긴 카운트 가문의 영광, **포아송 분포** 밭이야!" 라고 선언하죠.

2. Each approach models the mean of $Y$ as a function of the predictors. In linear regression, the mean of $Y$ takes the form
**2. 결국 조종석은 선형 스틱 하나뿐!**
결국 기계들이 타깃 $Y$의 최종 기댓값(평균) 예측 스코어를 뽑아낼 때, 엔진 속에 들어있는 조종대는 결국 변수들의 선형 덧셈(1차 방정식) 하나뿐이라는 겁니다. 선형 회귀에선 그 평균 타점이 아주 정직하게 이런 직선 조종대 형태를 띱니다.

$$
\text{E}(Y \mid X_1, \dots, X_p) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.39)
$$

i.e. it is a linear function of the predictors. For logistic regression, the mean instead takes the form
즉, 변수들을 곱하고 더한 군더더기 없는 직선(linear function) 엔진이죠. 반면 로지스틱 회귀의 엔진룸은 약간 꼬인 분수 형태를 취합니다.

$$
\text{E}(Y \mid X_1, \dots, X_p) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}} \quad (4.40)
$$

while for Poisson regression it takes the form
그리고 갓 배운 포아송 회귀 녀석의 엔진룸은 이런 지수 폭발 형태의 엔진을 달고 있죠.

$$
\text{E}(Y \mid X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.41)
$$

Equations (4.39)–(4.41) can be expressed using a _link function_, $\eta$, which applies a transformation to $E(Y \mid X_1, \dots, X_p)$ so that the transformed mean is a linear function of the predictors. That is,
자, 이 3개의 복잡한 엔진 도면 (4.39)–(4.41) 을 가만히 뚫어지게 들여다보면 하나의 거대한 퍼즐이 맞춰집니다. 타깃의 기댓값을 적절히 변형시켜서, 결국엔 그 수식을 깔끔하고 속 편한 1차 직선 방정식($\beta_0 + \beta_1 X_1 \dots$) 뼈대로 환원시켜 한방에 조종 통제하는 마법의 번역기 부속, 일명 **'연결 함수(link function)'**, 즉 기호 $\eta$ 플러그 하나면 이 세 기계의 공식이 모조리 통합된다는 겁니다! 즉 3대의 기동 도면이 스위치 하나로 요약돼버립니다!

$$
\eta(\text{E}(Y \mid X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.42)
$$

The link functions for linear, logistic and Poisson regression are $\eta(\mu) = \mu$, $\eta(\mu) = \log(\mu / (1 - \mu))$, and $\eta(\mu) = \log(\mu)$, respectively.
기계마다 저 번역기 볼트 $\eta$ 만 다르죠. 
- 선형 기계는 그냥 있는 그대로 쓰는 생얼치기: $\eta(\mu) = \mu$
- 로지스틱은 복잡한 오즈 비율 마취제: $\eta(\mu) = \log(\mu / (1 - \mu))$
- 포아송은 마이너스 방어 지수벽 마취제: $\eta(\mu) = \log(\mu)$

The Gaussian, Bernoulli and Poisson distributions are all members of a wider class of distributions, known as the _exponential family_.
여기에 숨겨진 대반전! 처음에 이 기계들이 모시는 가문(정규, 베르누이, 포아송)들이 서로 철저한 남남인 줄 알았죠? 충격적이게도 이 가문들은 통계학 세계관에서 **'지수족(exponential family)'** 이라 불리는 거대한 분포 무리 클래스의 일원, 결국 배다른 한 식구 소속 똘마니들이었을 뿐입니다! 

Other well-known members of this family are the _exponential_ distribution, the _Gamma_ distribution, and the _negative binomial_ distribution.
이 거대 지수족 패밀리 우주 안에는 우리가 몰랐던 살벌한 조직원들이 더 득실거리는데, 유명한 수명 예측 분포인 **지수(exponential) 분포**, **감마(Gamma) 분포**, 괴상한 킬러인 **음이항(negative binomial) 분포** 등도 같은 지수족 깃발 아래 서 있는 녀석들입니다.

In general, we can perform a regression by modeling the response $Y$ as coming from a particular member of the exponential family, and then transforming the mean of the response so that the transformed mean is a linear function of the predictors via (4.42).
통계의 달인들은 결국 이 거대한 우주 법칙을 깨달은 겁니다: 
"야, 어차피 타깃 $Y$ 가 저 거대 지수족 가문 놈들 중 한 놈 출신이라면 쫄지 마! 그냥 대충 그놈 성질(분포)에 맞는 **번역기 연결 함수 장착 치트키 (식 4.42)** 만 꽂아 돌리면, 복잡한 꼬라지들은 싹 변환 해결되고 내부 엔진은 전부 우리가 가장 만만하게 잘 다루는 단조로운 1차 몽둥이(선형 방정식) 조종 방식을 통해 모조리 우주 통합 계산 기동이 끝나버려!"

Any regression approach that follows this very general recipe is known as a _generalized linear model_ (GLM).
바로 이 혁명적인 꼼수 레시피! 무조건 지수족 가설을 깔고 번역기 볼트를 꽂아 직선 모델 방정식만 돌리는 이 광범위하고 포괄적인 만능 기계 모델 시스템의 철학 귀결 규범을 일컬어, 우리는 그 거룩하고 두려운 전체주의 통일 제국 이름인 **일반화 선형 모델(GLM, Generalized Linear Model)** 이라고 경외하며 부릅니다. 

Thus, linear regression, logistic regression, and Poisson regression are three examples of GLMs.
따라서 이 세계관의 거시적 관점에서 보면, 우리가 앞서 그토록 대단하게 여겼던 통나무 선형 회귀, 로지스틱, 포아송 회귀 변종 병기들은, 결국 저 거대하고 넓은 GLM (일반화 선형 모델) 만능 우주 전함 체제 안에서 각기 다른 부품 번역기 볼트만 갈아 끼운 흔한 부속 전투기, 즉 **아주 국지적이고 대표적인 3가지 작은 파생 사례 예시 기종에 불과하다**는 통쾌하고 짜릿한 소름 역전의 반전 구조 서사로 대단원의 막을 내리게 됩니다! 

Other examples not covered here include _Gamma regression_ and _negative binomial regression_.
물론, 이 거대 GLM 전함 안에는 우리가 이번에 시간상 다뤄보진 못한 **감마 회귀(Gamma regression)** 장치나 **음이항 회귀(negative binomial regression)** 전차 등, 아주 기상천외한 특수 목적의 다른 돌연변이 기동 예시 무기들도 여전히 발진 대기 중입니다!

---

## Sub-Chapters

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/trans2.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/trans2.html)
