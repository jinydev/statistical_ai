---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.7.1 Conceptual](../3_7_1_conceptual/trans2.html)

# _Applied_
# 응용 실습 문제: 파이썬 켜고 땀 흘려보기!

8. This question involves the use of simple linear regression on the `Auto` data set.
**8번 문제.** 자, 자동차 연비 데이터인 `Auto` 데이터셋을 파이썬에 불러오세요. 단순 1차 선형 회귀 분석의 기초 근력을 단련해 보겠습니다.

- (a) Use the `sm.OLS()` function to perform a simple linear regression with `mpg` as the response and `horsepower` as the predictor.
*(a) `sm.OLS()` 함수 믹서기를 써서, 마력(`horsepower`) 데이터 쪼가리를 쑥 밀어넣어 연비(`mpg`)라는 정답 목푯값을 예측해 내는 1차 단순 선형 회귀 모델을 시원하게 돌려보십시오!*

Use the `summarize()` function to print the results.
*그다음엔 `.summarize()` 함수를 호출해서 모델이 받아온 성적표를 화면에 떡 하니 띄워주세요.*

Comment on the output.
*그 출력 결과를 뚫어지게 쳐다보고 여러분의 날카로운 분석을 코멘트로 남겨보세요.*

For example:
*예를 들어 다음 질문들에 집중해 보세요:*

- i. Is there a relationship between the predictor and the response?
*i. 마력 빵빵한 차와 연비 사이에 과연 연관성이 눈곱만큼이라도 진짜 통계적으로 존재할까요? (P-값을 확인해 보세요!)*

- ii. How strong is the relationship between the predictor and the response?
*ii. 둘의 관계가 얼마나 질기게 막강합니까? (결정계수 $R^2$ 점수를 봐서 얼마나 설명이 되는지 보세요!)*

- iii. Is the relationship between the predictor and the response positive or negative?
*iii. 둘의 관계는 비례(양)입니까 아니면 반비례(음)입니까? (상식적으로 마력이 셀수록 연비는 개판이 되겠죠? 계수 부호를 확인하세요!)*

- iv. What is the predicted `mpg` associated with a `horsepower` of 98?
*iv. 만약 여러분이 98마력을 내는 구형 차를 샀다면, 이 똑똑한 모델은 여러분 차의 연비(`mpg`)가 도대체 얼마쯤 나올 거라고 예측할까요?*

What are the associated 95 % confidence and prediction intervals?
*그 예측값을 중심으로, 진짜 정답이 숨어있을 만한 95% 신뢰 구간과 예측 허용 범위(예측 구간) 방어막을 양옆으로 시원하게 쳐보세요!*

- (b) Plot the response and the predictor in a new set of axes `ax` .
*(b) 파이썬 matplotlib 도구를 써서 가로축에 마력, 세로축에 연비를 두는 점박이 산점도(scatterplot)를 예쁜 새 캔버스(`ax`) 위에 그려보세요.*

Use the `ax.axline()` method or the `abline()` function defined in the lab to display the least squares regression line.
*그리고 우리가 이전 랩 실습에서 배웠던 `ax.axline()`이나 `abline()` 마법을 부려서, 방금 뽑아낸 일직선 예측 모델 선(최소 제곱 회귀선)을 붉은색 펜으로 쫙! 하나 그어보세요.*

- (c) Produce some of diagnostic plots of the least squares regression fit as described in the lab.
*(c) 모델이 진정 잘 들어맞는지 뼈를 때리는 '불량 검사 플롯 진단 그림' 4종 세트(아까 랩 실습에서 배웠죠?)를 가차 없이 찍어내 보세요.*

Comment on any problems you see with the fit.
*그림을 요리조리 살피면서, 방금 만든 이 직선 모델이 도대체 뭐가 불량하고 어디서 엉망인지 여러분만의 날카로운 눈썰미로 문제점들을 지적질해 보십시오.*

9. This question involves the use of multiple linear regression on the `Auto` data set.
**9번 문제.** 방금 한 `Auto` 데이터셋의 진짜 진가를 뽐내보죠! 변수를 여러 개 한꺼번에 욱여넣는 '다중 선형 회귀'로 판을 본격적으로 키웁니다.

- (a) Produce a scatterplot matrix which includes all of the variables in the data set.
*(a) 데이터 안의 모든 열들을 한 번에 자기들끼리 십자포화로 교차 비교하는 무시무시한 전체 통판 산점도 행렬(scatterplot matrix, 예를 들면 `sns.pairplot` 같은 것) 표를 하나 대차게 뽑아보세요.*

- (b) Compute the matrix of correlations between the variables using the `DataFrame.corr()` method.
*(b) 점 그림만 보면 빙글빙글 헷갈리니까 파이썬의 `DataFrame.corr()` 함수를 떡하니 호출해서, 변수들끼리 누가 누구랑 끈적하게 짝짜꿍하고 엮였는지 전부 가로세로 십자표 숫자로 계산해 내세요.*

- (c) Use the `sm.OLS()` function to perform a multiple linear regression with `mpg` as the response and all other variables except `name` as the predictors.
*(c) 자! 이제 `sm.OLS()` 용광로에 연비(`mpg`)를 정답 목푯값으로 냅두고, 텍스트라 귀찮은 자동차 이름(`name`) 하나만 쏙 빼고 나머지 잡다한 제반 변수들을 깡그리 몽땅 다 집어넣어 회귀 모델을 시원하게 돌려버리십시오.*

Use the `summarize()` function to print the results.
*그리고 `.summarize()` 함수를 통해 이 거대한 다변수 모델의 종합 성적표를 뿜어내게 하세요.*

Comment on the output.
*결과물에 대해 여러분의 촌철살인 코멘트를 달아보세요.*

For instance:
*예를 들어:*

- i. Is there a relationship between the predictors and the response?
*i. 저 변수 떼거지와 연비 사이에 전체적으로 무슨 연관성이 통계적으로 있기는 합니까?*

Use the `anova_lm()` function from `statsmodels` to answer this question.
*`statsmodels`의 `anova_lm()` (F-통계량)의 막강한 힘을 빌려 이 질문에 속 시원히 답해 보세요.*

- ii. Which predictors appear to have a statistically significant relationship to the response?
*ii. 저 잡다한 변수 떼거지 중에서, 도대체 연비랑 통계적으로 **진짜 실질적(유의미한)** 관계가 있는 핵심 에이스 예측 변수는 누구누구입니까? (P-값이 0.05보다 작은 범인들을 색출하세요!)*

- iii. What does the coefficient for the `year` variable suggest?
*iii. 생산 연도(`year`) 변수 계수 조각은 우리에게 무슨 희망적인 힌트를 암시합니까? (해가 갈수록 차 연비가 기술 발달로 좋아집니까? 숫자는 거짓말을 하지 않죠!)*

- (d) Produce some of diagnostic plots of the linear regression fit as described in the lab.
*(d) 다시 한번 종합 병원 불량 진단 플롯(잔차 그래프)들을 돌려보세요.*

Comment on any problems you see with the fit.
*이 다변수 모델은 또 뭐가 문제인지 신랄하게 씹어보십시오.*

Do the residual plots suggest any unusually large outliers?
*혹시 잔차 산점도 그래프에서 남몰래 동떨어진 왕따 이상치(outliers) 점이 괴물처럼 솟아 보이지 않나요?*

Does the leverage plot identify any observations with unusually high leverage?
*레버리지 표에서 남들 다 찌그러져 있는데 혼자 위세 부리면서 모델 전체를 쥐락펴락하는 무시무시한 고위험 점이 혹시 감지되셨습니까?*

- (e) Fit some models with interactions as described in the lab.
*(e) 위에서 찾은 유효한 변수들을 가지고 이번엔 재밌게 '시너지 효과(상호 작용 항, 예: `weight*year`)'들을 섞어서 억지로 곱해 주는 모델들을 만들어보세요.*

Do any interactions appear to be statistically significant?
*그렇게 삽질(?)을 해본 결과, 혹시 통계적으로 대박 터진 유의미한 시너지 꿀조합 상호작용이 하나라도 등장했습니까?*

- (f) Try a few different transformations of the variables, such as $\log(X)$, $\sqrt{X}$, $X^2$.
*(f) 더 변태같이 파고들어 볼까요? 변수들을 억지로 $\log(X)$ 씌우거나, 제곱근 루트($\sqrt{X}$) 씌우고, 2차 다항 조미료($X^2$)로 꼬아보세요.*

Comment on your findings.
*그렇게 변수를 고문했더니 모델 예측이 훨씬 날카로워졌는지, 여러분이 겪은 충격적인 관찰 후기를 서술해 주십시오.*

10. This question should be answered using the `Carseats` data set.
**10번 문제.** 자, 자동차 연비는 덮고 상업적인 냄새가 물씬 풍기는 카시트(`Carseats`) 판매량 데이터로 넘어갑시다!

- (a) Fit a multiple regression model to predict `Sales` using `Price` , `Urban` , and `US` .
*(a) 카시트 판매 성과(`Sales`)를 목표 정답지로 삼고, 오직 가격(`Price`), 도심 여부(`Urban`), 국내 여부(`US`)라는 딱 3가지 변조 변수만 투입해 소박한 다변 회귀 모델을 하나 굴려 적합시켜 보십시오.*

- (b) Provide an interpretation of each coefficient in the model.
*(b) 튀어나온 성적표의 계수(coefficient) 값들을 유심히 보고, 영업 사장님께 "이건 이런 뜻입니다"라고 브리핑해 보세요.*

Be careful—some of the variables in the model are qualitative!
*주의보 발령! `Urban`이나 `US`는 숫자가 아닌 '분류성 글자 변수(질적 변수)'라는 얄궂은 사실을 절대 잊지 말고, 더미 처리를 감안해서 눈치껏 말조심 해석하십시오!*

- (c) Write out the model in equation form, being careful to handle the qualitative variables properly.
*(c) 방금 그 파이썬 코드를 실제 중학교 수학 공식 펜글씨 형태로($\text{Sales} = \beta_0 + ...$) 예쁘게 적어 보세요! 저 질적 더미 변수(Yes/No 변수)들을 수식에 어떻게 곱하기 1, 0으로 센스 있게 투입할지 솜씨를 발휘하십시오.*

- (d) For which of the predictors can you reject the null hypothesis $H_0 : \beta_j = 0$?
*(d) 투입된 저 3가지 예측 변수 후보 중에, 과연 누구누구가 "나 빼면 안 돼! 나 완전 필수야!"라며 위풍당당하게 쓸모없다는 귀무 가설 $H_0$를 통계적으로 타파(reject)해 버렸습니까?*

- (e) On the basis of your response to the previous question, fit a smaller model that only uses the predictors for which there is evidence of association with the outcome.
*(e) 방금 그 훌륭한(d)번 대답을 바탕으로... 증거도 없고 밥값 못 하는 쓸데없는 변수는 가차 없이 모가지를 쳐서 빼버리고, 오직 찐 에이스 증거형 변수만 남기는 더 날렵하고 심플한 축소(다이어트) 모델을 다시 깔끔히 적합(fit)해 살려보십쇼.*

- (f) How well do the models in (a) and (e) fit the data?
*(f) 아까 거추장스럽던 3인방 원조 모델(a)과 다이어트한 에이스 소수정예 모델(e), 둘 다 성적표를 까서 데이터 설명력($R^2$, 잔차 오차 등)을 맞대어 냉혹하게 비교해 보세요. 몸집을 줄였는데 설명력에 큰 타격이 없었다면 우리가 이긴 거겠죠?*

- (g) Using the model from (e), obtain 95 % confidence intervals for the coefficient(s).
*(g) 이 심플 에이스 모델(e)이 뽑아낸 엑기스 계수들에 대해 "제가 95% 장담하는데, 향후 이 요인들의 실제 가중치들은 이 숫자 범위(신뢰 구간) 사이에 백퍼 있을 겁니다!"라고 당당하게 오차 방어막 범위를 산출해 쳐보십시오.*

- (h) Is there evidence of outliers or high leverage observations in the model from (e)?
*(h) 에이스 모델(e)이라고 무조건 완벽할쏘냐! 진단 플롯을 차분히 그려서, "저 미친 이상치 놈 잡아라!" 할 만한 괴상망측한 아웃라이어 점이나 혼자 훌쩍 방방 뜨는 고도의 고위험 레버리지 데이터가 혹시 잠복해 있는지 셜록 홈즈처럼 샅샅이 뒤져보십시오.*

11. In this problem we will investigate the $t$-statistic for the null hypothesis $H_0 : \beta = 0$ in simple linear regression without an intercept.
**11번 문제.** 이번 문제에서는 조금 하드코어하게, "아예 절편(상수항)이 존재하지 않는" 아주 극단적인 단순 선형 회귀의 뼈대에 숨겨진 귀무 가설 $H_0 : \beta = 0$의 $t$-통계량(t-statistic) 비밀 구조를 파헤쳐보려 합니다.

To begin, we generate a predictor `x` and a response `y` as follows.
*시작하기 앞서 눈속임 없이, 다음과 같은 파이썬 코드로 신이 된 것처럼 우리 마음대로 난수를 뿌려 원인 `x`와 결과 `y` 데이터를 창조해 내겠습니다.*

```python
rng = np.random.default_rng(1)
x = rng.normal(size=100)
y = 2 * x + rng.normal(size=100)
```

- (a) Perform a simple linear regression of `y` onto `x` , _without_ an intercept.
*(a) 절편 항(intercept)을 무정하게 **잘라낸 채** 온전히 `x`만으로 `y`를 예언하는 순수 단순 선형 회귀에 돌입하십시오!*

Report the coefficient estimate $\hat{\beta}$ , the standard error of this coefficient estimate, and the $t$-statistic and $p$-value associated with the null hypothesis $H_0 : \beta = 0$.
*(저항 제로 상태인 이 모델이 예측해낸) 계수 추정치 $\hat{\beta}$, 이 자그마한 녀석이 얼마나 떨어댈지를 말해주는 표준 오차, 그리고 귀무 가설을 개박살 낼 수 있을지를 재는 $t$-통계량 수치와 운명의 $p$-값 등을 주르륵 읊어 제출해 주십시오.*

Comment on these results.
*그리고 튀어나온 이 숫자들의 의미에 대해 뼈대 있는 논평을 덧붙이세요.*

(You can perform regression without an intercept using the keywords argument `intercept=False` to `ModelSpec()` .)
*(당황하지 마십시오! `ModelSpec()` 함수 안에서 마법의 주문인 `intercept=False` 옵션을 때려 박으면 파이썬이 알아서 절편을 증발시킬 것입니다.)*

- (b) Now perform a simple linear regression of `x` onto `y` without an intercept, and report the coefficient estimate, its standard error, and the corresponding $t$-statistic and $p$-values associated with the null hypothesis $H_0 : \beta = 0$.
*(b) 이번엔 미친 짓을 해볼까요? 입장을 정반대로 쓱 뒤집어서 `y` 데이터를 투입해 원인 `x`를 맞춰보는, 역시 절편 없는 기이한 선형 회귀 실험을 해봅니다. 똑같이 계수 추정치, 표준 오차, $t$-통계량, $p$-값을 뽑아내서 보고하십시오.*

Comment on these results.
*저 역발상 실험의 결과가 아까 것과 비교해 여러분을 어떻게 당혹시키는지 논평해 보세요.*

- (c) What is the relationship between the results obtained in (a) and (b)?
*(c) 자, 위에서 나온 두 쌍의 결과물 (a)와 (b)를 매의 눈으로 노려보십시오. 둘 사이에 어떤 신비한 수학적 관계망이나 데칼코마니 같은 거울상 법칙이 포착되지 않습니까?*

- (d) For the regression of Y onto X without an intercept, the $t$-statistic for $H_0 : \beta = 0$ takes the form $\hat{\beta} / \text{SE}(\hat{\beta})$, where $\hat{\beta}$ is given by (3.38), and where
*(d) 절편 없는 야생의 수식 세계에서 Y를 X에 회귀시킬 때, $H_0 : \beta = 0$에 대항하는 $t$-통계량은 $\hat{\beta} / \text{SE}(\hat{\beta})$의 다부진 폼플릿을 갖춥니다. 여기서 $\hat{\beta}$ 은 옛날 교재 (3.38)번 공식에서 훔쳐 온 것이고, 바로 다음 요상한 분모 모양과 한 세트입니다:*

**==> picture [133 x 31] intentionally omitted <==**
**==> picture [133 x 31] intentionally omitted <==**

(These formulas are slightly different from those given in Sections 3.1.1 and 3.1.2, since here we are performing regression without an intercept.)
*(참고로 이 기이한 공식들은 앞서 3장에서 뒹굴던 공통 공식들이랑 미세하게 표정이 다릅니다. 왜냐면 우린 지금 절편 항이라는 무거운 닻줄을 끊어내 버렸기 때문이죠!)*

Show algebraically, and confirm numerically in `Python` , that the $t$-statistic can be written as
*자, 이제 종이와 펜을 들고 중학교 대수학 실력을 뽐내어 위 수식이 궁극적으로 아래처럼 멋진 대칭을 이루는 형태로 변신할 수 있음을 손으로 증명하고, 동시에 파이썬 코드로 실제 숫자를 때려 넣어 이 마법을 증명해 내십시오!*

**==> picture [181 x 32] intentionally omitted <==**
**==> picture [181 x 32] intentionally omitted <==**

- (e) Using the results from (d), argue that the $t$-statistic for the regression of `y` onto `x` is the same as the $t$-statistic for the regression of `x` onto `y` .
*(e) 기가 막히게 증명해 낸 위 (d)번의 대칭 공식 형태를 쓱 훑어보면서, "어? 보아하니 이거 `y`로 `x`를 맞추나, `x`로 `y`를 맞추나 $t$-통계량 평가 점수는 토씨 하나 안 틀리고 완전히 쌍둥이처럼 똑같네!"라는 소름 돋는 주장을 멋들어진 말발로 설득시켜 보십시오.*

- (f) In `Python` , show that when regression is performed _with_ an intercept, the $t$-statistic for $H_0 : \beta_1 = 0$ is the same for the regression of `y` onto `x` as it is for the regression of `x` onto `y` .
*(f) 이번엔 억제기를 풉니다! 다시 절편이 버젓이 **존재하는** 정상적인 회귀로 파이썬 코드를 굴려 보십시오. 그랬을 때조차도 `y`를 `x`로 맞추든 `x`를 `y`로 맞추든 핵심 변수의 $t$-통계량($H_0 : \beta_1 = 0$ 용)은 데스매치 무승부처럼 똑같게 나온다는 숨은 진실을 코드로 낱낱이 파헤쳐 보여주세요.*

12. This problem involves simple linear regression without an intercept.
**12번 문제.** 계속해서 절편 없이 벌거벗은 '원점 통과 단순 선형 회귀'의 오묘한 세계에서 놀아보는 문제 되겠습니다.

- (a) Recall that the coefficient estimate $\hat{\beta}$ for the linear regression of Y onto X without an intercept is given by (3.38).
*(a) 앞선 시련에서 맛보았던 절편 없는 Y를 X에 때려 맞추는 회귀 계수 공식(3.38) $\hat{\beta}$을 잠시 뇌 속에서 소환해 볼까요.*

Under what circumstance is the coefficient estimate for the regression of X onto Y the same as the coefficient estimate for the regression of Y onto X?
*도대체 세상이 어떻게 미쳐 돌아가야, 반대로 엎어 치는 'X의 Y에 대한 역회귀 계수'랑 'Y의 X에 대한 정방향 회귀 계수' 녀석이 소름 돋게 똑같은 쌍둥이 숫자가 되어버릴 귀이한 현상이 벌어질 수 있을까요? 바로 그 극적인 상황의 성립 조건을 수학 통찰력으로 풀어내 보십시오.*

- (b) Generate an example in `Python` with $n = 100$ observations in which the coefficient estimate for the regression of X onto Y is _different from_ the coefficient estimate for the regression of Y onto X .
*(b) 입으로만 떠들지 말고 손을 더럽힙시다! 파이썬을 켜서, 가짜 짝퉁 데이터 100알을 막 버무려 만들어, 이른바 '역방향과 정방향의 회귀 계수가 철저하게 **안 맞고 다른**' 아주 흔해 빠진 반례 상황을 코드로 창조해 보세요.*

- (c) Generate an example in `Python` with $n = 100$ observations in which the coefficient estimate for the regression of X onto Y is _the same as_ the coefficient estimate for the regression of Y onto X .
*(c) 이번엔 신기(神技)를 부려 보세요. 파이썬 마력을 총동원해, 데이터 100알을 아주 절묘하게 오만가지 조작해 내어 아까 (a)에서 예언했던 '역방향 회귀 계수와 정방향 회귀 계수의 값이 완벽하게 **대동단결 똑같아지는**' 마법 같은 특수한 찰나를 코드로 시연해 내십시오!*

13. In this exercise you will create some simulated data and will fit simple linear regression models to it.
**13번 문제.** 이 랩 실습의 백미! 우리는 직접 창조주가 되어 시뮬레이터로 가짜 세상(데이터)을 뚝딱 만들고 거기다 단순 선형 회귀의 밧줄을 칭칭 감아 볼 것입니다.

Make sure to use the default random number generator with seed set to 1 prior to starting part (a) to ensure consistent results.
*시작 파트 (a)를 건드리기 전에 딱 하나 주의사항! 파이썬 뽑기 기계(난수 생성기)의 비밀 고정 핀인 시드(seed)를 `1`로 못 박아 두세요. 그래야 당신이나 나나 똑같은 우주 결과를 보면서 채점할 수 있으니 말입니다.*

- (a) Using the `normal()` method of your random number generator, create a vector, `x` , containing 100 observations drawn from a $N(0, 1)$ distribution.
*(a) 통계 뽑기 마법 `normal()` 스킬을 질러서, 표준 정규 분포 $N(0, 1)$ (평균 0, 표준 편차 1짜리 종 모양) 우물에서 무작위로 관측치 100개의 알보석을 퍼 올려 `x`라는 길쭉한 벡터 그릇에 담으세요.*

This represents a feature, X .
*아, 이 `x`는 이제 선형 회귀판의 영원한 들러리 변수 역할을 할 특성 X입니다.*

- (b) Using the `normal()` method, create a vector, `eps` , containing 100 observations drawn from a $N(0, 0.25)$ distribution—a normal distribution with mean zero and variance $0.25$.
*(b) 또다시 `normal()` 마법을 발동! 이번엔 평균 0짜리는 맞지만 분산을 $0.25$로 확 줄여 살포시 흩뿌려지는 정규 분포 $N(0, 0.25)$에서, 100개의 미세 오차 먼지 먼지를 퍼 담아 `eps` 벡터 그릇에 만드세요.*

- (c) Using `x` and `eps` , generate a vector `y` according to the model
*(c) 위에서 애써 빚은 원인 찰흙 `x`에다가 잡음 먼지 `eps`를 섞어, 아래와 같은 진짜 세상의 모델 공식을 대입하여 100개의 결과물 그릇 `y` 벡터를 완성하십시오.*

**==> picture [182 x 11] intentionally omitted <==**
**==> picture [182 x 11] intentionally omitted <==**

What is the length of the vector `y` ?
*질문 하나! 이따위로 버무려 만든 벡터 `y` 꼬챙이의 전체 길이는 과연 몇 알입니까?*

What are the values of $\beta_0$ and $\beta_1$ in this linear model?
*우리가 이 세상에 부여한 진정한 조물주 수치(실제 모집단 파라미터), 즉 $\beta_0$(절편)과 $\beta_1$(기울기 선형 계수) 값은 각각 누구입니까? (공식을 잘 째려보면 답이 있습니다.)*

- (d) Create a scatterplot displaying the relationship between `x` and `y` .
*(d) 우리가 창조한 저 원인 `x` 녀석과 결과 `y` 결과물들이 이 세상에 어떻게 터 잡고 사는지 한눈에 보이게 밤하늘의 산점도 점그림으로 예쁘게 흩뿌려 직관해 보세요.*

Comment on what you observe.
*그 흩뿌려진 별자리(점)의 패턴을 멀찍이서 감상하고 논리적인 촌평을 갈겨주세요.*

- (e) Fit a least squares linear model to predict `y` using `x` .
*(e) 좋고요, 이제 인간의 관점! 우리가 이미 정답($\beta$)을 다 꿰고서 조작해 낸 우주인 걸 모르는 순진무구한 최소 제곱 선형 모델을 투입해 `x`로 `y`를 눈치껏 알아맞히게 적합(학습) 훈련을 굴려버립시다.*

Comment on the model obtained.
*과연 이 순진한 예측 모델 녀석이 얼마나 똑똑한 예측선을 뽑아냈는지 가볍게 입을 놀려 평을 해보십시오.*

How do $\hat{\beta}_0$ and $\hat{\beta}_1$ compare to $\beta_0$ and $\beta_1$?
*제일 재밌는 관전 포인트! 이 녀석이 엉겁결에 내놓은 추정치 $\hat{\beta}_0, \hat{\beta}_1$ 숫자가 우리가 미리 창조 단계에 심어둔 신의 정답 $\beta_0, \beta_1$ 숫자와 얼마나 오싹하게 맞아떨어지거나 어긋났는지 대조해 보세요.*

- (f) Display the least squares line on the scatterplot obtained in (d).
*(f) 아까 (d)번에서 그렸던 별자리(산점도) 화면 위에, 순진한 모델이 뱉어낸 '인간 최선의 최소 제곱 예측 회귀선' 일직선을 쭉 하고 하나 그어봐 주세요.*

Draw the population regression line on the plot, in a different color.
*거기에 대비되게, "아이고 모델아 네가 아무리 발버둥 쳐도 신이 짜놓은 진짜 이 세계 선은 바로 이거란다!" 하고, 아까 (c)에서 만든 진짜배기 조물주 회귀선(모집단 선)을 확 튀는 별색 펜으로 교차시켜 그려 넣으십시오.*

Use the `legend()` method of the axes to create an appropriate legend.
*마지막으로 어떤 선이 진짜 신의 선이고 어떤 선이 모델이 발버둥 친 인간의 선인지 나중에 봐도 안 헷갈리게 `legend()` 기법으로 정갈한 지도 범례표를 구석에 박아주세요.*

- (g) Now fit a polynomial regression model that predicts `y` using `x` and $x^2$ .
*(g) 밋밋하게 선만 그으니 심심하죠? 이번엔 괜히 "이거 곡선 아닙니까요?"라며 뽐내보려는 다항 회귀 모델 녀석을 출전시켜 `x`뿐만 아니라 얍삽한 $x^2$ (제곱) 재료까지 양손에 쥐여주고 억지로 선을 적합시켜 보게 만드십시오.*

Is there evidence that the quadratic term improves the model fit?
*과연 저 얄팍한 이차항 $x^2$ 꼼수가 모델의 설명력(피팅)을 진정 통계적으로 유의미하게 레벨업시켜줬다는 객관적 증거(P-값 등)가 쥐뿔만큼이라도 나타났습니까?*

Explain your answer.
*왜 그랬는지 이유를 데이터 조물주 시점에서 당차게 파헤쳐 설명하십시오.*

- (h) Repeat (a)–(f) after modifying the data generation process in such a way that there is _less_ noise in the data.
*(h) 데이터 조물주가 밸런스 패치에 들어갑니다! 아까 실습했던 전체 파트 (a)-(f) 과정을 처음부터 싹 다 다시 돌리되, 이번에는 피조물 데이터들의 혼란(잡음)이 훨씬 **적어지도록** 우주 규칙을 클린하게 수정해서 굴려보십시오.*

The model (3.39) should remain the same.
*(단, 뼈대가 되는 (3.39)번 조물주 공식 자체는 손대면 안 됩니다. 게임 룰은 그대로예요!)*

You can do this by decreasing the variance of the normal distribution used to generate the error term $\epsilon$ in (b).
*(팁: 이 짓을 어떻게 하느냐? 아까 (b) 파트에서 잡음 먼지 흩뿌리던 마법진의 정규 분포 분산을 과감하게 확 조여서 짓이기면 오차 $\epsilon$이 개미 눈물만 해집니다.)*

Describe your results.
*공기가 맑아진 클린 버전 우주에서 얻어낸 당신의 빛나는 결과를 술술 서술해 보십시오.*

- (i) Repeat (a)–(f) after modifying the data generation process in such a way that there is _more_ noise in the data.
*(i) 이번에는 극마라맛 하드코어 패치 발동! 파트 (a)-(f) 과정을 전부 다시 무식하게 돌리되, 데이터 세계관에 혼란한 **잡음이 미친 듯이 소용돌이치도록** 꼬아보십시오.*

The model (3.39) should remain the same.
*(역시, 저 튼튼한 (3.39) 뼈대 공식 자체는 손가락 하나 대면 안 됩니다!)*

You can do this by increasing the variance of the normal distribution used to generate the error term $\epsilon$ in (b).
*(아까 잡음 먼지 생성기 (b) 마법진의 분산 수치를 뻥튀기하면, 회오리바람 돌듯 오차 $\epsilon$ 지진이 미쳐 날뛸 겁니다.)*

Describe your results.
*시야가 썩어문드러진 이 대혼란 막장 우주에서 건져 올린 당신의 참혹한(?) 결과를 스릴 넘치게 묘사해 보십시오.*

- (j) What are the confidence intervals for $\beta_0$ and $\beta_1$ based on the original data set, the noisier data set, and the less noisy data set?
*(j) 자, 이제 최종 심판의 날! '원년 오리지널 맛 데이터', '미쳐 돌아가는 마라맛 극성 잡음 데이터', 그리고 '초순수 청정 안심 맛 데이터'. 이 세 가지 평행 우주 모델들이 토해낸 $\beta_0, \beta_1$ 계수의 95% 신뢰 구간 방어막 폭스홀(크기 범위) 값을 쫙 전시해 보세요.*

Comment on your results.
*잡음의 강도에 따라 신뢰 구간 울타리가 어떻게 처참히 오만상을 찌푸리는지 촌철살인의 총정리 감상평을 때려 넣어 주십시오.*

14. This problem focuses on the _collinearity_ problem.
**14번 문제.** 대망의 빌런 출현! 이 문제는 회귀 분석의 흉악범, 변수들끼리 목을 졸라대며 자멸하는 '_공선성(collinearity)의 저주_' 문제에 칼집을 쑤셔 넣습니다.

- (a) Perform the following commands in `Python` :
*(a) 먼저, 당신의 불쌍한 파이썬 IDE 쉘 창에 다음의 조작된 마법 저주 코드들을 타이핑해 밀어 넣으십시오:*

```python
rng = np.random.default_rng(10)
x1 = rng.uniform(0, 1, size=100)
x2 = 0.5 * x1 + rng.normal(size=100) / 10
y = 2 + 2 * x1 + 0.3 * x2 + rng.normal(size=100)
```

The last line corresponds to creating a linear model in which `y` is a function of `x1` and `x2` .
*유심히 보시면 맨 밑의 파멸의 마지막 줄 수식이, `y`를 희생양으로 삼아 기어이 `x1`과 `x2`라는 놈들을 교묘히 꼬아버려 한 모델 함수로 엮고 있다는 걸 깨달으실 겁니다.*

Write out the form of the linear model.
*그렇다면 조물주인 당신이 창조한 저 파이썬 코드를 뜯어보고, 수학적 선형 모델의 뼈대 형태가 도대체 어떻게 꼬여 생겨 먹었는지 종이에 적나라하게 밝혀 적어보세요.*

What are the regression coefficients?
*그리고 이 악의 소굴에 숨어있는 조물주의 진짜배기 회귀 계수(진짜 $\beta$) 숫자는 까놓고 몇인지 수사해 내십시오.*

- (b) What is the correlation between `x1` and `x2` ?
*(b) 이 빌런 변수 듀오 `x1`과 `x2` 사이에서 도대체 얼마나 더러운 결탁(상관관계) 숫자가 도출될까요? 계산해 보세요.*

Create a scatterplot displaying the relationship between the variables.
*그 두 놈이 얼마나 서로를 탐욕스럽게 쫓아다니는지(결탁했는지) 눈으로 까발릴 수 있도록 잔잔한 산점도로 관계를 폭로해 주십쇼.*

- (c) Using this data, fit a least squares regression to predict `y` using `x1` and `x2` .
*(c) 자, 이제 경찰차 번쩍! 아까 이 썩은 데이터로 `x1`, `x2`를 공동 범죄자로 몰아 지지고 볶고 추궁해서 무고한 `y`를 밝혀내는 최소 제곱 회귀 모델을 풀가동 시키십시오.*

Describe the results obtained.
*경찰(모델) 수사 결과표를 쭉 들이밀며 어떤 미친 숫자들이 튀어나왔는지 보고해 보십시오.*

What are $\hat{\beta}_0$, $\hat{\beta}_1$, and $\hat{\beta}_2$?
*범퍼인간 경찰 모델이 어설프게 지레짐작으로 찍어낸 $\hat{\beta}_0$, $\hat{\beta}_1$, $\hat{\beta}_2$ 숫자들은 과연 무엇입니까?*

How do these relate to the true $\beta_0$, $\beta_1$, and $\beta_2$?
*아까 (a) 파트에서 조물주 모드로 내려다본 진짜 정답 $\beta_0$, $\beta_1$, $\beta_2$랑 비교했을 때... 이 결과들이 얼마나 웃음거리가 되는 헛스윙을 날렸는지 낭만적으로 묘사해 보시죠.*

Can you reject the null hypothesis $H_0 : \beta_1 = 0$?
*모델의 허접한 수사력으로 이 난장판에서 귀무 가설 $H_0 : \beta_1 = 0$을 찍어 누르고(기각하고) 유의미하다 우길 수 있는 깡다구가 생겼습니까?*

How about the null hypothesis $H_0 : \beta_2 = 0$?
*그 똑똑하던 모델이 귀무 가설 $H_0 : \beta_2 = 0$ 놈한텐 어떻게 벌벌 떨든지 상황을 고발해보세요.*

- (d) Now fit a least squares regression to predict `y` using only `x1` .
*(d) 짜증 나서 특단의 수사 조치! 이번엔 불쌍한 `x2`를 방출해 버리고, 철저하게 독불장군 `x1` 혼자만 불러서 `y`를 심문하는 단순 최소 제곱 회귀 독대 심문을 때려보십시오.*

Comment on your results.
*홀딱 벗은 `x1`의 진술 결과에 대해 당신만의 맵고 짠 논평을 퍼부으십시오.*

Can you reject the null hypothesis $H_0 : \beta_1 = 0$?
*이번 심문에서는 과연 당당하게 귀무 가설 $H_0 : \beta_1 = 0$ 카드를 가뿐히 씹어먹고(기각하고) 유의미를 선포할 수 있었습니까?*

- (e) Now fit a least squares regression to predict `y` using only `x2` .
*(e) 이번엔 이판사판, `x1`을 골방에 처박아 빼버리고 오롯이 `x2` 혼자만을 심문실에 던져 넣어 `y`를 취조하는 최소 제곱 심문을 굴려보십시오.*

Comment on your results.
*이 녀석 혼자 있을 때는 판세가 또 어떻게 미쳐 돌아가는지 어이없는 결과를 맛깔나게 묘사해 보세요.*

Can you reject the null hypothesis $H_0 : \beta_1 = 0$?
*이 녀석은 과연 귀무 가설을 통쾌하게 부숴버리고(기각하고) "나 유의미해!"라고 당당하게 빼액 소리칠 수 있게 되었습니까? (참고 원문에선 오타로 $\beta_1$이라 적혀있지만 여기선 사실 $\beta_2$에 대한 검정입니다)*

- (f) Do the results obtained in (c)–(e) contradict each other?
*(f) 파트 (c)에서 두 놈을 같이 심문했을 때의 완전 거지 같은 헛발질 결과랑, 파트 (d), (e)에서 각각 독립 심문했을 때의 결과가 서로 모순되고 충돌하면서 상식 밥 말아 먹은 논리 역설이 폭발합니까?*

Explain your answer.
*도대체 왜 이런 기가 막힌 블랙 코미디 모순 사태가 통계 모델을 덮쳐버린 것인지, 공선성의 저주 관점에서 그 속사정을 확 파헤쳐 조리 있게 설명하십시오.*

- (g) Suppose we obtain one additional observation, which was unfortunately mismeasured.
*(g) 자, 수사 현장에 초짜 형사가 아주 개판으로 잘못 재어 온 거지 같은 단 1개의 '쓰레기 짝퉁 추가 데이터 측정치' 난입 사고가 벌어졌다고 상상합시다.*

We use the function `np.concatenate()` to add this additional observation to each of `x1` , `x2` and `y` .
*그 쓰레기 한 조각을 파이썬의 접착제 함수 `np.concatenate()` 우왁스러운 손길로 우리 안방 데이터 목록인 `x1`, `x2`, 그리고 `y` 꼬리에 무식하게 덕지덕지 붙여버리겠습니다.*

```python
x1 = np.concatenate([x1, [0.1]])
x2 = np.concatenate([x2, [0.8]])
y = np.concatenate([y, [6]])
```

Re-fit the linear models from (c) to (e) using this new data.
*오물이 한 방울 떨어진 이 치명타 데이터 웅덩이를 다시 박박 긁어모아, 아까 전 (c)부터 (e)까지 빙빙 돌려본 눈물겨운 선형 모델들을 처음부터 다시 학습(적합) 시켜보십시오.*

What effect does this new observation have on the each of the models?
*과연 이 미꾸라지 한 마리 관측치가 연못(각 모델)의 수질을 어떻게 구정물로 확 오염시켜 망쳐버렸는지 그 파급 효과를 고발하십시오.*

In each model, is this observation an outlier?
*각 모델이 바라보는 입장에서, 이 추가 관측치가 위아래로 동떨어진 미친 궤도의 이상치(outlier) 판정을 받습니까?*

A high-leverage point?
*아니면 모델 예측선을 멱살 잡고 꺾어버리는 고위험 무법자 레버리지 포인트(고도 뻥튀기 지점)로 악명을 떨칩니까?*

Both?
*어차피 수사 개판인데 아예 쌍방울로 두 뱃지를 훈장처럼 동시에 달아버리는 괴물입니까?*

Explain your answers.
*도대체 왜 오염된 데이터 한 톨에 그 난리가 나는지 진단 플롯을 그려보고 당당하게 당신의 논거를 변호하십시오.*

15. This problem involves the `Boston` data set, which we saw in the lab for this chapter.
**15번 문제.** 긴 여정의 피날레! 이번 장 랩 실습의 맛집이었던, 아련한 `Boston` 부동산 데이터셋으로 우리의 마지막 탐정 놀이를 시작합니다.

We will now try to predict per capita crime rate using the other variables in this data set.
*여기서 우리는, 이 방대한 동네 데이터셋 골목골목 지천에 널린 다른 모든 변수에 기대어 동네의 뒷골목 1인당 범죄율(per capita crime rate)을 점쟁이처럼 예언하는 무리수에 도전하겠습니다.*

In other words, per capita crime rate is the response, and the other variables are the predictors.
*다시 말해 타겟 과녁판(반응 변수)은 1인당 범죄율이고, 다른 남아도는 곁가지 정보들이 기출 문제집(예측 변수) 역할을 하는 판다.*

- (a) For each predictor, fit a simple linear regression model to predict the response.
*(a) 일단 장인 스피릿! 저 모든 예측 변조 예언자 후보들을 일일이 줄 세워서 1:1로 범죄율과 엮어 단물만 빼먹는 소박한 '단순 선형 회귀 모델' 수십 통을 아주 지독하게 따로따로 하나씩 돌려 맞춰보십시오.*

Describe your results.
*그렇게 노가다를 돌린 전체 결과의 흥망성쇠를 짧게 브리핑하십시오.*

In which of the models is there a statistically significant association between the predictor and the response?
*그 수많은 단순 모델 잡탕 중에, 과연 어느 예측 변수들만이 범죄율과 통계의 신성한 P-값 인증을 받은 유의미한 결탁(연관성)을 드러냈습니까?*

Create some plots to back up your assertions.
*입으로만 털지 말고 당신의 그 강력한 주장을 찍어 누를 수 있게 증명하는 뽀대나는 차트 플롯 몇 장을 만들어 무기처럼 뒤에 세워두십시오.*

- (b) Fit a multiple regression model to predict the response using all of the predictors.
*(b) 이제 진정한 패싸움! 저 곁가지 예측 변수들을 하나도 남김없이 통째로 아구창에 쓸어 담아넣고, 이 동네 범죄율을 집단 다굴로 예측하는 거대한 괴물 다변 회귀 모델 하나를 통렬하게 가동해 보십시오.*

Describe your results.
*이 어벤져스급 단체 폭행 다중 예측 모델에서 나온 기겁할 만한 결과 보고서를 읊어 보시죠.*

For which predictors can we reject the null hypothesis $H_0 : \beta_j = 0$?
*단체로 심문했더니, 도대체 저 잘난 척하는 예측 변수 용의자들 중 과연 누구누구만이 결백을 주장하던 쓸모없단 핑계(귀무 가설 $H_0$)를 강제로 부숴버리고, 집단 내 진정한 에이스로 살아남았습니까?*

- (c) How do your results from (a) compare to your results from (b)?
*(c) (a) 파트의 1:1 뒷골목 예선전 싸움에서 거둔 성적과 (b) 파트의 통짜 본선 집단 패싸움 성적을 나란히 한 책상에 올려놓고 둘 사이의 배신과 모순을 비교 분석해 보십시오.*

Create a plot displaying the univariate regression coefficients from (a) on the _x_ -axis, and the multiple regression coefficients from (b) on the _y_ -axis.
*그 둘의 엇갈림을 한 방에 시각화해 봅시다! 가로 _x_ 축에는 (a)에서 뽑힌 1:1 단독 출전 회귀 계수(단순 모델 계수) 성적을 나열하고, 세로 _y_ 축에는 (b)에서 뽑힌 단체 출전 회귀 계수(다중 모델 계수) 성적을 크로스로 매칭 시키는 앙증맞은 산점도를 엮어내 보세요.*

That is, each predictor is displayed as a single point in the plot.
*즉, 요 녀석들은 화면 상에서 저마다의 매력을 품은 점 하나하나로 영광스럽게 빛날 것입니다.*

Its coefficient in a simple linear regression model is shown on the _x_ -axis, and its coefficient estimate in the multiple linear regression model is shown on the _y_ -axis.
*(다시 말해 점의 좌우 위치는 단독 캐리 할 때의 힘이고, 위아래 위치는 단체로 팀플 할 때의 조화로운 기여도를 낱낱이 고해바친다는 뉘앙스입니다!)*

- (d) Is there evidence of non-linear association between any of the predictors and the response?
*(d) 잠깐, 우리는 왜 세상사가 무조건 일직선(선형)으로 흘러간다고 순진하게 믿고 있었죠? 혹시 저 예측 변수들 사이에 뭔가 꾸불텅 우동 사리 굴러가듯 곡선을 띠는 비선형적인 짬짜미가 존재한다는 증후군 결산의 신호가 있었습니까?*

To answer this question, for each predictor X , fit a model of the form
*이 뼈를 때리는 철학적 질문에 답하기 위해, 각 용의자 예측 변수 $X$에 관해 아래 수식과도 같이 능글맞게 꺾이는 이차항, 삼차항 모델 형태를 직접 뒤집어씌워서 통렬히 돌려보며 진실을 심문해 보세요!*

**==> picture [154 x 11] intentionally omitted <==**
**==> picture [154 x 11] intentionally omitted <==**

---

## Sub-Chapters (하위 목차)

[< 3.7.1 Conceptual](../3_7_1_conceptual/trans2.html)
