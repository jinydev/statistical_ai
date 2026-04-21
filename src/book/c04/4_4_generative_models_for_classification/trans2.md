---
layout: default
title: "trans2"
---

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/trans2.html) | [4.4.1 Linear Discriminant Analysis For P = 1 >](4_4_1_linear_discriminant_analysis_for_p_1/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.4 Generative Models for Classification
# 4.4 분류를 위한 생성 모델 (거꾸로 뒤집어 확률을 캐내는 베이즈의 마법)

Logistic regression involves directly modeling $\text{Pr}(Y = k \mid X = x)$ using the logistic function, given by (4.7) for the case of two response classes. In statistical jargon, we model the conditional distribution of the response $Y$, given the predictor(s) $X$. We now consider an alternative and less direct approach to estimating these probabilities. In this new approach, we model the distribution of the predictors $X$ separately in each of the response classes (i.e. for each value of $Y$). We then use Bayes’ theorem to flip these around into estimates for $\text{Pr}(Y = k \mid X = x)$. When the distribution of $X$ within each class is assumed to be normal, it turns out that the model is very similar in form to logistic regression.
로지스틱 회귀 요원은 타깃 돌연변이 반응 카테고리가 2개인 전투 상황에서 그 유명한 S자 로지스틱 함수 체제 식 (4.7)을 여과 없이 들이밀어 이용하여, 어찌 됐든 저 $Y$가 터질 직접적 확률인 $\text{Pr}(Y=k \mid X=x)$ 를 아주 무식하고 '직접적(directly)'으로 모델링 압박합니다. 조금 고상한 통계학 전문 용어를 섞어 쓰자면, 우리가 무수히 던져 준 예측 수치 변수 $X$ 단서들 뭉치가 통째로 이미 우리 손에 주어졌을(given) 찰나 조건일 때 타깃 범인 반응 $Y$ 에 대한 직접적인 '조건부 분포'의 그 자체를 멱살 잡아 모델링한다고 그럴듯하게 일컫습니다. 자, 하지만 이제 우리는 이 목표 확률들을 추정 타진해 내기 위해, 앞문으로 들어가는 듯 다소 직접적이지 기조 않고 살짝 우회 기만하는 **'대안적(alternative)이고 덜 직접적인'** 비밀 접근법을 심도 깊게 대조 다룹니다. 이 완전히 돌변한 **새로운 우회 접근법(Generative Models)** 체제 점거에서는, 시작 위치를 아예 거꾸로 뒤집어 반응 클래스 결과 측면(즉, 이미 벌어진 결과값 $Y$ 가 파산이냐 정상이냐의 각 파벌별 조건 계층)에서 각기 반대 산입으로 뻗어 시작해, 굴러온 그 파벌 병에 걸린 집단의 예측 변수들 $X$ 의 개별 생태적 밀도 분포를 역으로 추산 역산해 모델링합니다. 그런 통계 뒤에 우리는 위대한 마법사 **베이즈 정리(Bayes' theorem)** 공식을 야심 차게 기동 사용해서 돌연 이것들을 앞뒤 홀딱 뒤집어(flip around) 우리가 원초 애당초 원래 원하던 관측치 타깃 기준 진짜 타격 확률 모형, 즉 $\text{Pr}(Y=k \mid X=x)$ 로 귀결 시켜내는 찰나의 추정치 치환 묘기를 부립니다. 여기서 만일 우리가 통계 억지를 써서 '각각의 분리된 타겟 파벌 클래스 내부에 진을 치고 분포하는 고유 예측 변수 집단 $X$ 들의 성향 특성 밀도가 모두 완벽히 흔한 정규 분포(종 모양 가우시안 곡선)를 띠고 얌전히 있다'고 가설 치부해 점거 가정하면, 놀랍게도 이 빙글 우회해 돌아가는 희한한 방식으로 연쇄 유도 조립된 모형이 수학적으로 정작 파고들면 결국 앞서 질리도록 배운 로지스틱 회귀 수식 체계의 구조 형태 전초와 수상하게 상당히 소름 돋게 흡사하게 파생 도출된다는 결론 사실이 증명되었습니다.

Why do we need another method, when we have logistic regression? There are several reasons:
아니 다 좋은데, 이미 우리가 든든한 로지스틱 회귀 무기라는 훌륭 전천후 S자 방패를 굳건 가지고 수중에 무장돼 있는데 뭣하러 굳이 또 이런 복잡하고 변덕스러운 빙 돌아가는 대안 방법론 우회 체계가 거듭 필요한 수반 겁니까? 거기엔 사실 버릴 수 결단 없는 막강 몇 가지 심각한 통계 전술적 이유 우위가 단연 있습니다:

- When there is substantial separation between the two classes, the parameter estimates for the logistic regression model are surprisingly unstable. The methods that we consider in this section do not suffer from this problem.
- 두 개의 대결 구도 클래스 분포 조각 데이터 무리가 애매하게 겹치지 않고 아예 칼로 무를 두부 자르듯 서로 선명 확고하게 분단 쪼개어져 나누어져(Separation) 아예 동떨어져 멀리 이탈해 있을 때, 로지스틱 회귀 모형 기입 머신에 들어간 선형 방정식 추정 파라미터 다이얼 수치들은 컴퓨터가 허둥지둥 길을 잃으며 놀라울 정도로 미친 듯이 제멋대로 요동치고 수렴하지 못해 극도 불안정해집니다. 하지만 우리가 이번 섹션 장에서 배우게 단연 될 거꾸로 된 이 생성 기법 모델들은 파벌 그딴 분단 결함 데이터 붕괴 문제에서 완전히 면역되어 하등 타격 고통받지 않습니다.
- If the distribution of the predictors $X$ is approximately normal in each of the classes and the sample size is small, then the approaches in this section may be more accurate than logistic regression.
- 만약 우리 예측 단서 변수 $X$ 구획들의 분포 상태가 각각의 파벌 클래스들 타겟 조각 종속 내부 생태계에서 거의 대충 정규 분포(예쁜 종 모양 곡선)에 가까운 정갈 기조 상태를 다수 띠고 있고 게다가 심지어 우리 손에 쥐어진 데이터 샘플 증거 사이즈 수량(n) 양 덩이 마저 엄청 빈약 작을 척추 경우라면, 이번 섹션 단락의 이 우회 역산 접근법 모델이 오히려 구식 로지스틱 단조 회귀기보다 훨씬 훠씬 더 적중 정밀하고 놀랍도록 수식 단연 정확할 수 공산 있습니다.
- The methods in this section can be naturally extended to the case of more than two response classes. (In the case of more than two response classes, we can also use multinomial logistic regression from Section 4.3.5.)
- 마지막 단면, 이번 단원의 단연 이 새 생성 방식 모델 체계 방법론들은 억지 조율할 질적 양산 타겟 결착 반응 클래스가 고작 단 2개를 한참 우스갯 소리 넘어서는 3개, 4개의 그 이상의 다발 무리 '다중 클래스' 의 복잡 난세 상황 국면에서도 그 어떠한 수치적 억지스러움 조립이나 변질 버그 없이 아주 부드럽고 매끄럽게 물 흐르듯 자연스럽게 공식 결판이 다중 연장되어 구조 확장 세팅됩니다. (물론, 아까 봤듯 2개 초과 다발 다중 클래스 척결의 경우 우리가 방금 앞 4.3.5 단락에서 배운 그 꼼수 소프트맥스 '다항 로지스틱 회귀'를 써먹어 무마 방어할 수도 있기는 단연 합니다.)

Suppose that we wish to classify an observation into one of $K$ classes, where $K \ge 2$. In other words, the qualitative response variable $Y$ can take on $K$ possible distinct and unordered values. Let $\pi_k$ represent the overall or _prior_ probability that a randomly chosen observation comes from the $k$th class. Let $f_k(x) \equiv \text{Pr}(X = x \mid Y = k)$ denote the _density function_ of $X$ for an observation that comes from the $k$th class. In other words, $f_k(x)$ is relatively large if there is a high probability that an observation in the $k$th class has $X \approx x$, and $f_k(x)$ is small if it is very unlikely that an observation in the $k$th class has $X \approx x$. Then _Bayes’ theorem_ states that
이제 본격적으로 우리가 어떤 수사 낯선 예측 타깃 관측치를 딸랑 단 2개가 아니라 어마무시한 $K$ 개의 광활한 여러 집단 클래스 조각 (이때 통계 제약상 수식적으로 무조건 $K \ge 2$ 위상임) 집단 중 오직 하나로 핀셋 구속 분류해 내고 치부하고 단연 싶다고 간절 열망한다 상황 단연 쳐봅시다. 다른 수단 말로 역산 하자면, 우리 질적 범주 타겟 반응 변수 종착지 가차 없는 $Y$가 아무런 대소 우월 순열 서열 짬짜미 순서가 없는 그저 무식한 $K$ 가지의 각기 확연히 서로 이율 분단 다른 가능성의 독립 성질 명판 값을 폭넓게 이리저리 지닐 구역 수 조율 있다는 단연 점입니다. 여기서 미지의 임의 조작 편견 없는 기표 $\mathbf{\pi_k}$ 변수를 그냥 세상 전체 무리에서 무식 무작위로 아무 인원 하나 눈 조차 감고 무심코 대충 쑥 뽑았을 국면 때 재수 없게 그 친구 덩어리가 단연코 $k$ 번째 분류 클래스 진영 출신 소속일이라는 전체 확률적인 혹은 맹목 단서 **'사전(prior) 확률'** 조각 게이지를 단연코 나타내 표상한다고 지표 무마해 결론 가정합니다. 그리고 거창하게 조작식 $\mathbf{f_k(x) \equiv \text{Pr}(X = x \mid Y = k)}$ 라고 무단 수식 정의해 두고, 이 친구 덩어리에 감표를 "$k$번째 병에 걸린 특수 그룹 타겟 단연 클래스 뱃속 출신 그룹에서 굴러나온 어떤 오염 개인 환자 병 관측치가 지닌 특수 종속 특성 관찰값 수위 $X$ 에 관해 지닐 만한 **밀도 함수(Density function)**" 라고 거창 통계 지표 정의해 봅니다. 좀 더 인간이 알아먹기 쉽게 다시 혀를 풀어서 번역 쓰자면, $k$번째 고약한 병에 걸려 병동에 격리된 수용 무리 특성 그룹 덩어리 전단 생태계 안에서, 하필 무작위 이번에 찍은 이 환자의 특성 발현 심박수 수치나 특성 척도가 $X \approx x$ 주변 마진값과 아주 절묘 단연하게 소름 돋게 흡사하게 수비게 발견 발발될 수맥 확률 치수가 엄청 졸라 높은 기형 흔한 단연 상황이라면 저 계산 도출 밀도 점유 함수 우도 반환 수치인 $\mathbf{f_k(x)}$ 가 덩달아 상대적으로 덩치 아주 거대해진다는(large) 압도 말이고, 반대 현상으로 만약 그 $k$ 병에 걸린 수용 사람 치고는 도무지 현실 상식에선 낼 수가 전무 없는 아주 극도로 기괴 희박한 미친 별종의 $X \approx x$ 척도 수치를 냈을 희귀 관측 경우엔 단연 그 발현 지표 기압 함수 $\mathbf{f_k(x)}$ 덩어리 함수값이 바닥을 쳐 아주 처참 쥐꼬리 작아질(small) 비현실 확률 일 거라는 전면 단연결 말입니다. 그리고 나서 우린 이 미지의 두 분리 전장 통계 기지 인자를 극복 무마 우당탕 한 냄비에 섞기 마법을 위해, 지수 위대한 기적 수식 **베이즈 정리(Bayes' theorem)** 기조를 소환하여 당당 확고하게 결단 이 수식 마법의 연산 공식을 전면 장식 단도직입 내지릅니다:

$$
\text{Pr}(Y = k \mid X = x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^{K} \pi_l f_l(x)} \quad (4.15)
$$

In accordance with our earlier notation, we will use the abbreviation $p_k(x) = \text{Pr}(Y = k \mid X = x)$; this is the _posterior_ probability that an observation $X = x$ belongs to the $k$th class. That is, it is the probability that the observation belongs to the $k$th class, _given_ the predictor value for that observation.
우리가 조금 전 지루 이전 챕터 단원들에서 쭉 편의상 간소 계속 쓰며 밀었던 약어 표기법 척도 방식과 단조 부합 연동되게, 이 무서운 베이즈 수학자 방정식 기계의 필터를 거쳐 튀어나온 기표 이 최후의 응축된 통계 결과 도출 마감 증빙값인 위대한 $\text{Pr}(Y = k \mid X = x)$ 도 단연코 역시나 짧게 퉁쳐서 거친 형태인 $\mathbf{p_k(x)}$ 라는 조작 명칭으로 그냥 쓰겠습니다. 단연 이것은 대체 어떤 특성 $X=x$ 인자를 몸에 비참하게 띈 낯선 관측치가 빙빙 돌아온 결과를 안겨 결국 우리가 무단 목표로 치부하는 $k$번째 분류 파벌 예측 타겟 클래스 집단 감옥에 최종 스코어로 확정 갇혀 속하게 될 조미 결단을 말해주는, 가장 확실 체감된 최신의 통찰 결론인 전단 **사후(posterior) 확률** 마감 지표라 명제 일컫습니다. 다시 말해 환언하자면, 오롯이 그 사람 타겟에 대장 대한 오염 특정 단서 예측 변숫값 형상 조합들이 우리 정보 망에 딱 손에 모두 주어졌을 때(조건부, given), 그놈이 바로 저쪽 무리 $k$ 해당 그룹 클래스 소속 출신임에 틀림없을 무구 것이라는 것을 단연 가리키는 최종 법정 판결 검찰의 구속 확률 선고 마감장입니다.

We know from Chapter 2 that the Bayes classifier, which classifies an observation $x$ to the class for which $p_k(x)$ is largest, has the lowest possible error rate out of all classifiers. In the following sections, we discuss three classifiers that use different estimates of $f_k(x)$ in (4.15) to approximate the Bayes classifier: _linear discriminant analysis, quadratic discriminant analysis,_ and _naive Bayes_.
우리는 아득히 기나긴 옛날 챕터 먼 단락 2장에서의 지옥 훈련 경험에서, 낯선 관측치 인자 $x$ 덩어리를 냅다 집어넣어 도출 연산해 저 맨 괄호 마지막 끝판 공식인 사후 확률 단출 $p_k(x)$ 마감 결재 점수가 $K$ 그룹 중 가장 압도 수위 덩치적으로 최고 크게 터져 피크 나오는 기조 단상 우승자 클래스로 그대로 무자비 관측치 분류 구속 낙인을 찍어버리는 이 막강 우상 **'베이즈 분류기(Bayes classifier)'** 모델 머신이, 지상에 고안 필경 존재하는 현존 가능 모오든 분류기 잡동사니 모델들을 죄다 통틀어서 이론 수학 그론적으로 가장 오판을 안 하는, 세상에서 제일 억제 낮은 무오류 예측 한계 오류 에러율(error rate)의 물리적 극한 경계 하방을 무결 자랑 보증한다는 사실을 이미 귀에 딱지가 피나게 쥐어 박혀 배웠습니다. 이어질 조치 후속 섹션 뒷 전투 단락들에서, 우리는 이 궁극 공식 베이즈 덩어리 전단 방정식 (4.15) 속에 도무지 무구 알 수 없어 구역 들어간 전 단락 저 미지의 역추적 요괴 밀도 곡선 스펙 함수 $\mathbf{f_k(x)}$ 덩어리 부품을, 조금씩 각각 제각기 각기 사뭇 다른 무리수 가정 착시와 엉뚱 방식으로 멋대로 무작위 추정 타진해내서, 오로지 이 오판 없는 저 신성한 절대 영역 베이즈 황제 분류기 성역 점수선 한도에 티끌 다가 끝없이 가짜 인위적으로라도 근사 억지로 모방 시키려(approximate) 처절하게 시도하는 실전 세 가지의 현실적 꼼수 짝퉁 무기 분류기 모델들을 차례로 심판 논의할 예정 공산입니다: 그것은 그 유명 일컬어 부르는 수위 바로 수학계의 **선형 판별 분석(LDA)**, 그리고 굽은 **이차 판별 분석(QDA)**, 마침내 끝으로 멍청한 **나이브 베이즈(Naive Bayes)** 라 칭해 불리는 예측기 비법 마법들입니다.

---

### 4.4.1 Linear Discriminant Analysis for p = 1 (p=1인 경우의 선형 판별 분석)

### 4.4.2 Linear Discriminant Analysis for p > 1 (p>1인 경우의 선형 판별 분석)

### 4.4.3 Quadratic Discriminant Analysis (이차 판별 분석)

### 4.4.4 Naive Bayes (나이브 베이즈)

---

## Sub-Chapters

[< 4.3.5 Multinomial Logistic Regression](../4_3_logistic_regression/4_3_5_multinomial_logistic_regression/trans2.html) | [4.4.1 Linear Discriminant Analysis For P = 1 >](4_4_1_linear_discriminant_analysis_for_p_1/trans2.html)
