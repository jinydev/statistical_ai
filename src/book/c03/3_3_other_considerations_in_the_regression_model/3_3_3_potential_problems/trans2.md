---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.3.2.1 Non-Linear Relationships](../3_3_2_extensions_of_the_linear_model/3_3_2_1_non-linear_relationships/trans2.html) | [2. Correlation Of Error Terms >](2_2._correlation_of_error_terms/trans2.html)

# 3.3.3 Potential Problems

# 3.3.3 잠재적 골칫거리들 (선형 회귀의 6대 고질병)

When we fit a linear regression model to a particular data set, many problems may occur. Most common among these are the following:
우리가 특정 장부(데이터 세트)를 가져다 놓고 선형 회귀 모델이라는 틀에 강제로 구겨 넣어 맞출 때, 실전에서는 참으로 속 터지는 수많은 골칫거리 버그들이 터져 나오기 일쑤입니다. 그중에서도 통계쟁이들이 가장 지겹게 마주치는 최악의 6가지 흔한 고질병 리스트는 다음과 같습니다.

1. _Non-linearity of the response-predictor relationships._ (정답과 힌트가 일직선이 아닌 삐딱선 곡선일 때)
2. _Correlation of error terms._ (오차 찌꺼기들끼리 뒷거래로 서로 눈치 보며 짜고 칠 때)
3. _Non-constant variance of error terms._ (오차 찌꺼기들의 널뛰기 폭발력이 갈수록 걷잡을 수 없이 커질 때)
4. _Outliers._ (혼자 튀는 미친 돌연변이 또라이 점들)
5. _High-leverage points._ (영향력 갑질하는 목소리 큰 깡패 점들)
6. _Collinearity._ (힌트 변수들끼리 캐릭터가 겹쳐서 도플갱어 짓거리를 할 때)

In practice, identifying and overcoming these problems is as much an art as a science. Many pages in countless books have been written on this topic. Since the linear regression model is not our primary focus here, we will provide only a brief summary of some key points.
실전 현장에서 이 더러운 6가지 역병들을 귀신같이 캐내고 치유하는 과정은 투박한 공학이라기보단 차라리 무당의 감에 가까운 예술의 경지에 속합니다. 이미 시중의 수많은 통계학 두꺼운 벽돌 책들이 이 역병 퇴치법에 지면을 수백 페이지씩 할애하며 떠들어댔죠. 하지만 이 교재의 최종 목적지는 구닥다리 '선형 회귀'를 마스터하는 게 아니기 때문에, 여기서는 그냥 핵심 엑기스만 핥아보고 빠르게 넘어가겠습니다.

---

## 1. Non-linearity of the Data (데이터가 삐딱선 탈 때: 잔차도 돋보기로 숨은 곡선 찾기)

**==> picture [318 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
Residual Plot for Linear Fit(1차 꼬챙이 적합의 쓰레기장) Residual Plot for Quadratic Fit(2차 포물선 적합의 쓰레기장)<br>323 334<br>330 323<br>334<br>155<br>5 10 15 20 25 30 15 20 25 30 35<br>Fitted values Fitted values<br>20<br>15<br>15<br>10<br>10<br>5<br>5<br>0<br>0<br>Residuals Residuals<br>−5<br>−5<br>−10<br>−10<br>−15<br>−15<br>**----- End of picture text -----**<br>

**FIGURE 3.9.** _Plots of residuals versus predicted (or fitted) values for the_ `Auto` _data set. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend. Left: A linear regression of_ `mpg` _on_ `horsepower`. _A strong pattern in the residuals indicates non-linearity in the data. Right: A linear regression of_ `mpg` _on_ `horsepower` _and_ `horsepower`$^2$. _There is little pattern in the residuals._
**FIGURE 3.9.** `Auto` _장부를 털어 만든 '예측 적중값' 대비 '잔차(예측 실패 찌꺼기)' 쓰레기장 투시도. (빨간 선은 쓰레기들이 어디로 흘러가는지 추세를 억지로 부드럽게 그려준 심봉사 지팡이입니다.) (왼쪽) 융통성 없는 일자 직선 모델로 밀어붙였더니, 찌꺼기들이 강렬한 U자 밥그릇 모양으로 뭉쳐서 "우리 사실 곡선이야 바보야!" 라고 비웃는 패턴이 적나라하게 폭로됨. (오른쪽) 마력을 제곱한 2차 항을 넣고 적합했더니, 찌꺼기 패턴이 산산조각 나며 잡동사니 무작위 구름처럼 깨끗해짐._

The linear regression model assumes that there is a straight-line relationship between the predictors and the response.
멍청한 선형 회귀 모델의 치명적 결함! 이 녀석은 힌트와 정답 사이가 무조건 자를 대고 그은 듯 '일직선 철로(straight-line)'로 곧게 뻗어 있을 거라는 미친 망상(가정)에 빠져 산다는 겁니다.

If the true relationship is far from linear, then virtually all of the conclusions that we draw from the fit are suspect. In addition, the prediction accuracy of the model can be significantly reduced.
만약 야생의 실제 데이터 진실 관계가 그 따위 일직선과 담쌓고 저세상 곡선으로 꼬여 있다면 어떨까요? 그 멍청한 일직선 철로 모델 위에서 신나서 뽑아낸 온갖 예측과 통찰과 결론들은 모조리 구라, 사기, 망상으로 판명될 위기에 처합니다. 게다가 이 깡통 모델이 뱉어내는 타겟 정답 예측 적중률마저 처참히 바닥을 뚫고 곤두박질치게 되겠죠.

_Residual plots_ are a useful graphical tool for identifying non-linearity.
자, 이럴 때 우리 모델이 일직선 강박증에 취해 야생의 곡선 데이터를 억지로 짓누르고 착각한 건 아닌지 잽싸게 뽀록을 캐내는 아주 맛깔스러운 시각적 진단 돋보기 도구가 있습니다. 바로 **_잔차도(Residual plots)_**라는 쓰레기장 투시경입니다!

Given a simple linear regression model, we can plot the residuals, $e_i = y_i - \hat{y}_i$, versus the predictor $x_i$. In the case of a multiple regression model, since there are multiple predictors, we instead plot the residuals versus the predicted (or _fitted_) values $\hat{y}_i$.
이 돋보기를 쓰는 법은 간단해요. 힌트 변수가 1개뿐인 단순 회귀 모델이라면 힌트 변수 $x_i$ 스펙 대비 잔차 쓰레기들($e_i$, 내 예측치와 실제 정답 간의 오차 찌꺼기)을 흩뿌려 차트 점박이로 점을 찍어보면 됩니다. 반면 힌트가 여러 개인 복잡한 다중 회귀 판에서는 힌트가 너무 많아 좌표가 꼬이니까, 깔끔하게 최종적으로 도출된 '예측 결괏값($\hat{y}_i$)'을 가로축 기준 삼아 그에 따른 해당 찌꺼기 투기장 양태를 흩뿌려 투사해 그립니다.

Ideally, the residual plot will show no discernible pattern. The presence of a pattern may indicate a problem with some aspect of the linear model.
바라건대 가장 이상적이고 마음 편한 건강한 쓰레기장(잔차도)의 꼴은 무엇일까요? 예측 찌꺼기들이 어떤 음흉한 물결이나 일정한 S자 진영 세력 뭉침 같은 식별 가능한 '패턴' 따위는 1도 없이 아주 개판 무작위 혼돈 카오스 구름처럼 흩뿌려진 상태가 최고의 정상 상태입니다. 반대로 만일 찌꺼기들이 무슨 기하학적 형이상학 기호 패턴으로 뭉치며 조직적인 파동 그림을 그리고 있다면? 그건 명백히 "네 일직선 회귀 모델 설계의 어딘가가 단단히 썩어 문드러졌다!"라는 끔찍한 치명적 결함 발작 경고등을 울리는 셈입니다.

The left panel of Figure 3.9 displays a residual plot from the linear regression of `mpg` onto `horsepower` on the `Auto` data set that was illustrated in Figure 3.8.
아까 봤던 그림 3.8 창문을 다시 소환해 그림 3.9의 왼쪽 단면 패널을 째려봅시다. 저 그림은 아까 그 `Auto(자동차)` 데이터에서 일자 꼬챙이 직선 모델로 연비(`mpg`)를 마력(`horsepower`)으로 찍어 누르고 나서 남은 패배의 찌꺼기 분비물들을 모아놓은 쓰레기장 단면입니다.

The red line is a smooth fit to the residuals, which is displayed in order to make it easier to identify any trends. The residuals exhibit a clear U-shape, which provides a strong indication of non-linearity in the data.
저 빨간 밧줄 선 보이시나요? 늙은 통계학자들이 침침한 눈으로 찌꺼기 패턴을 더 쉽게 읽으려고 쓰레기 흐름의 잔상을 억지로 부드럽게 이어 그려놓은 친절한 형광펜 추세선입니다. 세상에. 저 찌꺼기 점들과 빨간 밧줄이 완전히 조직적으로 모여서 노골적인 U자 형태의 밑 빠진 밥그릇 곡면 진동의 결탁 자태를 보여주고 있어요! 이건 이 장부 데이터 본판 바탕에 일직선이 아닌 음흉한 곡선 변동 결(비선형성)이 강렬하게 살아 숨 쉬는데, 멍청한 일자 모델이 그걸 다 놓치고 찌꺼기로 토해냈다는 초강력 경고 알리바이입니다.

In contrast, the right-hand panel of Figure 3.9 displays the residual plot that results from the model (3.36), which contains a quadratic term. There appears to be little pattern in the residuals, suggesting that the quadratic term improves the fit to the data.
그와 정반대로 이번엔 화면 오른쪽 패널을 보세요. 이건 아까 꼼수로 마력을 제곱한 2차 돌연변이 곡률 항($\text{horsepower}^2$)을 욱여넣어 돌린 신형 (3.36) 짬뽕 모델의 투기장입니다. 보세요! 아까 그 기만적인 U자 물결 카르텔 패턴이 흔적도 없이 박살이 나서, 그저 잡동사니 노이즈 파편들만이 무작위 우주 먼지 구름처럼 맥락 없이 흩뿌려져(little pattern) 있습니다. 이 말인즉슨, 우리가 쑤셔 넣은 2차 곡면 제곱 마법 항이 이 판의 구불구불한 심층 야생 정보 트렌드를 성공적으로 다 흡수 소화 해독해 버려서, 배설물(찌꺼기)에는 더 이상 남겨진 미지의 정보 패턴이 통째 사라지는 대성공 적합 향상의 치유 기적을 일궈냈다는 소름 돋는 증거 반증 도박판 인증서입니다.

If the residual plot indicates that there are non-linear associations in the data, then a simple approach is to use non-linear transformations of the predictors, such as $\log X$, $\sqrt{X}$, and $X^2$, in the regression model.
결론적으로 잔차 돋보기를 까봤는데 저런 불길한 비선형 곡선 찌꺼기 패거리 패턴 경고등이 번쩍이며 깜빡인다면 처방전은 뭘까요? 아주 심플한 야매 우회 치유법이 있죠 아까처럼! 그냥 힌트 변수 X의 몸뚱아리를 칼로 째서 $\log X$(로그 변환), $\sqrt{X}$(루트 변환), 혹은 앞서 써먹은 $X^2$(제곱 변환) 같은 잔인한 마개조 다변화 변형 조각 포맷으로 강제 환골탈태시킨 뒤 회귀 공장 컨베이어 벨트에 억지 쑤셔 넣고 굴리면 직빵 해결입니다.

In the later chapters of this book, we will discuss other more advanced non-linear approaches for addressing this issue.
이딴 허접하고 단순 무식한 야매 변환 꼼수 말고도, 저 머나먼 뒤쪽 후반부 챕터 교재로 넘어가면 이 지긋지긋한 비선형 굴레 마를 해소 치유하기 위한 훨씬 더 극강의 진보된 고차원 오버테크놀로지 고급 마법 기법들을 무수히 마주 잡고 썰어 해체해 볼 예정입니다.

---

### 2. Correlation of Error Terms (오차 항의 상관관계)
* [📖 쉬운 해설판으로 이동하기](./2_2._correlation_of_error_terms/trans2.html)

오차 항들은 서로 독립이어야 한다는 기본 전제가 깨졌을 때 발생하는 표준 오차 산정의 치명적인 오류를 다룹니다.
이로 인해 발생하는 가설 검정 결함 및 p-value의 신뢰성 하락을 설명합니다.

### 3. Non-constant Variance of Error Terms (오차 항의 비일관적 분산)

데이터의 반응 변수 값이 커짐에 따라 오차의 편차가 커지는 이분산성(Heteroscedasticity) 문제를 분석합니다.
로그 함수와 같은 반응 변수 변환(Transformation)으로 오차 분산을 안정화하는 기법을 배웁니다.

### 4. Outliers (이상치)

일반 예측치를 크게 벗어난 관측값인 이상치가 잔차 표준 오차 및 모델 적합도(R²)에 어떤 치명적인 영향을 끼치는지 파악합니다.
스튜던트화 잔차(Studentized Residual)를 사용한 진단과 대응을 다룹니다.

### 6. Collinearity (다중공선성)

입력 변수들이 서로 높은 상관성을 띠어 각 계수 추정의 분산을 팽창시키는 다중공선성의 위험 패턴을 분석합니다.
분산 팽창 인수(VIF)를 계산하여 문제를 감지하고 대응책을 세우는 법을 안내합니다.

---

[< 3.3.2.1 Non-Linear Relationships](../3_3_2_extensions_of_the_linear_model/3_3_2_1_non-linear_relationships/trans2.html) | [2. Correlation Of Error Terms >](2_2._correlation_of_error_terms/trans2.html)
