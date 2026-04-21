---
layout: default
title: "trans1"
---

[< 3.7 Exercises](../trans1.html) | [3.7.2 Applied >](../3_7_2_applied/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# _Conceptual_

# 개념 문제

1. Describe the null hypotheses to which the $p$-values given in Table 3.4 correspond. Explain what conclusions you can draw based on these $p$-values. Your explanation should be phrased in terms of `sales`, `TV`, `radio`, and `newspaper`, rather than in terms of the coefficients of the linear model.

1. 앞선 표 3.4(Table 3.4)에 제시 기입된 제반 $p$-값(p-values) 차출 지표들이 각각 어떤 구체적 귀무 가설(null hypotheses) 기조 내용들에 상응 직결(correspond)해 부합하는지 낱낱이 묘사 서술(Describe)해 보십시오. 나아가 오로지 이들 $p$-값 지수들만을 단단한 근거 삼아(based on) 우리가 최종적으로 어떠한 결론 양상(conclusions)을 유추 도달해 끌어낼(draw) 수 있는지도 논리적으로 설명(Explain)해 보십시오. 단, 여러분의 답변 설명(explanation) 내역은 선형 모델상에 얽힌 단순 수학적 계수(coefficients) 용어 형태가 아닌, 오롯이 `sales`(판매량), `TV`, `radio`(라디오), 그리고 `newspaper`(신문)라는 실물 지표 맥락 용어(in terms of)들로 짜여 표현(phrased)되어야만 합니다.

2. Carefully explain the differences between the KNN classifier and KNN regression methods.

2. 기계 학습의 KNN 분류기(KNN classifier) 체제와 KNN 회귀(KNN regression) 접근 방법론 모델 간에 자리한 결정적 편차 차이점(differences)들을 세심히 짚어 꼼꼼히 설명(Carefully explain)해 보십시오.

3. Suppose we have a data set with five predictors, $X_1$ = GPA, $X_2$ = IQ, $X_3$ = Level (1 for College and 0 for High School), $X_4$ = Interaction between GPA and IQ, and $X_5$ = Interaction between GPA and Level. The response is starting salary after graduation (in thousands of dollars). Suppose we use least squares to fit the model, and get $\hat{\beta}_0 = 50$, $\hat{\beta}_1 = 20$, $\hat{\beta}_2 = 0.07$, $\hat{\beta}_3 = 35$, $\hat{\beta}_4 = 0.01$, $\hat{\beta}_5 = -10$.

3. 예컨대 우리가 총 5가지 다변 예측 변수(predictors)군, 즉 $X_1$ = GPA(학점 평균), $X_2$ = IQ(지능 지수), $X_3$ = Level(학력 수준, 대졸 College일 경우 1, 고졸 High School일 경우 0 부여), $X_4$ = GPA와 IQ 변수 간의 상호 작용(Interaction) 항, 그리고 $X_5$ = GPA와 Level(학력 수준) 변수 간의 통계적 상호 작용 지표 항들로 꽉 채워 설계된 일개 특정 데이터 세트 판을 앞선에 쥐고 지녔다 가정(Suppose)해 봅시다. 이때 목표 타깃 응답(response) 수치는 다름 아닌 졸업 직후 첫 초봉(starting salary after graduation, 단위: 천 달러, thousands of dollars)입니다. 이런 조건하에서 우리가 최소 제곱(least squares) 연산 잣대를 본격 기용해(use) 이 주어진 회귀 모델을 통계 적합(fit)시켰고, 그 파생 성과로 $\hat{\beta}_0 = 50$, $\hat{\beta}_1 = 20$, $\hat{\beta}_2 = 0.07$, $\hat{\beta}_3 = 35$, $\hat{\beta}_4 = 0.01$, $\hat{\beta}_5 = -10$ 이라는 부문별 계수치들을 일제히 도출 획득해 냈다(get) 가정해 봅니다.

- (a) Which answer is correct, and why?

- (a) 과연 하단에 제시 나열된 선택지 중 단연 어느 답변(Which answer) 항목 진출이 오롯이 옳은(correct) 팩트 결론일까요? 그리고 대체 그 근거 사유(why)는 무엇입니까?

- i. For a fixed value of IQ and GPA, high school graduates earn more, on average, than college graduates.

- i. IQ와 GPA 성적 수치가 매한가지 동일하게 고정된(fixed value) 통제 여건하에선, 줄곧 고졸(high school graduates) 학력자가 대졸(college graduates) 학위 소지자 무리보다 전체 수치상 평균적으로(on average) 더 많은(more) 초봉 급여를 벌어들여 챙깁니다(earn).

- ii. For a fixed value of IQ and GPA, college graduates earn more, on average, than high school graduates.

- ii. IQ와 GPA 성적 수치가 매한가지 동일하게 고정된 통제 위상 여건하에선, 늘 통상적으로 대졸 학위 소지자가 고졸 학력자 그룹보다 그 수치 평균 통계상으로 더 막대히 많은 급여를 벌어들입니다.

128 3. Linear Regression

- iii. For a fixed value of IQ and GPA, high school graduates earn more, on average, than college graduates provided that the GPA is high enough.

- iii. IQ와 GPA 성적 수치가 매한가지 동일 고정된 여건이라도 단, 단서 조항으로 그 특정 GPA(학점) 점수 축이 가히 단대히 유달리 충분히 드높이 우수하게만 랭크돼 뒷받침 제공(provided that.. is high enough)된다면, 그 쾌거 상한 국면에선 줄곧 고졸 학력자가 평균 통계상으로 대졸 학위 그룹보다 훨씬 더 막대히 많은 급여 보상을 벌어들여 챙깁니다.

- iv. For a fixed value of IQ and GPA, college graduates earn more, on average, than high school graduates provided that the GPA is high enough.

- iv. IQ와 GPA 성적이 똑같이 고정 통제 수치를 이룬 여건일지라도, 여하튼 그 GPA(학점) 학업 성취도 선상 점수치가 충분할 만치 상당히 월등히 눈부시게만 제공(provided that) 뒷받침되어 높다면, 그 수위 고점 국면에선 평균적으로 대졸 학위자가 고졸 학력자 무리보단 월등히 더 가파르게 많은 임금 첫 초봉을 벎이 확실시됩니다.

- (b) Predict the salary of a college graduate with IQ of 110 and a GPA of $4.0$.

- (b) 공인 IQ 수치 110 등급을 점유 지니고 동시에 대학 필적 학부 평점(GPA) 성과가 $4.0$ 만점인 어느 임의의 대졸자(college graduate) 한 명의 구체적 산정 예상 입사 초봉(salary) 지표를 한번 정밀 유추 산출 타진해 예측(Predict)해 보십시오.

- (c) True or false: Since the coefficient for the GPA/IQ interaction term is very small, there is very little evidence of an interaction effect. Justify your answer.

- (c) 참(True) 혹은 거짓(false) 여부를 밝혀 가리십시오: 도출된 GPA/IQ의 결부 매개 상호 작용 항(interaction term)에서 산출 파생된 고유 선형 회귀 계수치(coefficient) 덩어리 지수 척도가 애초 무척 수량 단위상으로 협소 미약하고 형편없이 몹시나 매우 작게(very small) 나온 고로(Since), 사실상 두 지표 간의 실체 얽힌 상호 작용 효과(interaction effect) 파급력은 거의 아예 전무하여 실질적 개입 연관 시사 증거(evidence) 자체가 도무지 무척이나 거의 없다고 볼 수 있습니다. 이 주장에 대한 본인의 최종 답변 판별 소견을 제반 근거 기반하에 논리적으로 명백히 변호 옹호 입증 정당화(Justify)해 보십시오.

4. I collect a set of data ($n = 100$ observations) containing a single predictor and a quantitative response. I then fit a linear regression model to the data, as well as a separate cubic regression, i.e. $Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3 + \epsilon$.

4. 지레 어느 연구자 본인(I)이 단 하나의 단일 예측 변수(single predictor) 성분과 또 그에 동반 호흡하는 양적 응답치(quantitative response) 결괏값만으로 아기자기 꽉 채워 구축 직조된 한 세트 무리의 관측 실측 데이터(총 관측치 양 $n = 100$ observations 점) 파편을 전격 모아 집대성 차출 수집(collect)했습니다. 그런 돌입 직후, 당장 마련된 이 데이터 집합 판에다 가장 흔한 1차 단순 선형 회귀 모델(linear regression model) 잣대를 일차로 전격 도출 적합(fit)시켰거니와, 그와 아울러 동시 궤도 부문에서 또 다른 별개의 동반 독립 3차 다항 회귀(cubic regression) 산입 교차 곡선 모델(즉, $Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3 + \epsilon$) 체제까지 추가 이중 연산 발탁해 이 역시 똑같이 맞물려 덧대어 적합시켰습니다(as well as).

- (a) Suppose that the true relationship between X and Y is linear, i.e. $Y = \beta_0 + \beta_1 X + \epsilon$. Consider the training residual sum of squares (RSS) for the linear regression, and also the training RSS for the cubic regression. Would we expect one to be lower than the other, would we expect them to be the same, or is there not enough information to tell? Justify your answer.

- (a) 예컨대 만일 $X$ 변수와 $Y$ 응답 결괏값 간의 실질적 근본 잠재 본 태생 관계가 이미 당초 완고하고 뚜렷한 확고부동 1차 선형 기조(linear, 즉 역학 관계 수식 $Y = \beta_0 + \beta_1 X + \epsilon$ 모형)를 단단히 띠고 형성 형성돼 있다 치고, 일단 먼저 그렇다고 애써 가정(Suppose)부터 해 봅시다. 이를 기반으로 우선 단순 1차 선형 회귀 도출망 모델이 산출 뱉어 낸 저 훈련(training) 단계 RSS(잔차 제곱합, residual sum of squares) 누적 지수 점수를 하나 염두 골똘히 고려(Consider)해 품고 띄워 본 데 이어, 이와 더불어 3차 다항 회귀(cubic regression) 변환망에서 매한가지 발생 조달 반환된 그 고유 훈련 RSS 수치 점수 궤적 파편까지도 거시상 함께 고려해(and also) 짚어 보십시오. 둘을 견줄 시 거시상 과연 우린 어느 모종의 한쪽 지표 RSS 성과치가 여타 편 쪽보다 한층 수치 폭으로 더 미약히 밑돌아 낮고 저조 구사(lower)될 거라 쉬이 기대 예상(expect)할 수 있을까요, 아니면 이 둘의 RSS 산입 결과 점수가 모두 거의 똑같고 하등 오차 없이 동일 완전 유사(the same)할 것으로 굳건히 기대 예측해야 할까요, 그것조차 혹 아니라면 당면 현 정황에 선 결론 판가름을 내기엔 우리 수중에 거머쥔 근거 정황 연루 정보(information) 단서량 자체가 영 턱없이 단편 부실 모자라 판별 시도조차 불가능한 한계 부족(not enough) 실정일까요? 당신이 이끄는 이 판단 소견의 뒷배경 옹호 근거 사유 논리망을 여실 명확히 조명 타진 강구해 정당화(Justify)해 보십시오.

- (b) Answer (a) using test rather than training RSS.

- (b) 바로 앞선 저 (a)번 항의 똑같은 맥락 질의에 대하여, 다만 이번엔 저 훈련(training) 단계의 한정 국면 파생 RSS 잣대 말고 이를 한사코 탈피 이관해 넘어선 오직 진짜 실전 국면 평가의 본산재인 시험(test) 과정 단계 고유 파생 RSS 지표 결괏값의 거시적 기대 양상 변차 전개 추이 판세를 기둥 잣대로 삼아 기용(using)해 고스란히 엇비슷이 답변(Answer)해 보십시오.

- (c) Suppose that the true relationship between $X$ and $Y$ is not linear, but we don't know how far it is from linear. Consider the training RSS for the linear regression, and also the training RSS for the cubic regression. Would we expect one to be lower than the other, would we expect them to be the same, or is there not enough information to tell? Justify your answer.

- (c) 이번엔 예컨대 변개 관점 역전선 발상으로 반대로 아예 변수 $X$ 와 $Y$ 간의 얽히고설킨 뭇 본 바탕 기저 체제 관계 역학이 본질상 극단 선형(linear) 기조가 애초 절대 아닌(not linear) 복잡 시야의 모종의 여건 양상을 띠고 있다고 지레 먼저 가정(Suppose)부터 내려 보기는 하되, 역으로 또 동시에 과연 그 굴절 진전 관계 양상이 애면글면 도대체 저 흔히 교과서적인 1차 직선(linear) 표준 기조 수위에서부터 얼마큼 아득 무구히 동떨어져 일탈 파생 왜곡 괴리 진행된 것인지(how far it is from linear) 그 수위 깊이나 규모 거리감 정도 정보 단서만큼은 우리가 아직 전혀 가다듬어 밝혀 속 시원히 파악 포착 알지 지레 짐작해 내진 못하는 그저 아득한 무지몽매(we don't know) 깜깜이 정황 상태라 지레 애써 상정해 봅시다. 이를 전제 기조로 깔고 우선 아까와 유사 맥락으로 단순 1차 선형 회귀 망이 산입 도출한 저 훈련(training) 국면의 RSS 거시 결과망 지수를 하나 염두에 띄워 깊이 고려(Consider)해 보시고, 거기 여봐란듯이 덧대어 3차 단편 회귀 변환망이 토핑 반환 도출해 낸 이면의 거시 훈련 RSS 결과 산입 점수상의 궤적까지도 함께 맞물려 면밀 포괄 고려 주시 비교해 오롯이 저울질해 보십시오. 둘을 견줄 시 거시상 과연 우린 어느 모종의 한쪽 지표 RSS 도출 성과치가 또 다른 반대쪽 역편보다 한층 수치 폭으로 더 미약히 밑돌아 낮고 현저히 구사 위태해질 거라 쉬이 기대 예상(expect one to be lower)할 수 있을까요, 아님 아까완 이색 양상으로 이 둘의 RSS 산입 결과 폭이 거의 한 묶음 획일 판으로 어금버금 치우침 굴곡 오차 없이 매한가지로 동일 완전히 유사 접목 평준(the same)할 것으로 진전 기대 예상해야 할까요, 행여나 그것조차 혹 아니라면 정황상 현 시점에서 뭇 모종 결론 판가름 단단히 내리치기(tell)엔 우리 수중 거머쥔 근거 정황 연루 정보 단서(information) 분량 자체가 영 턱없이 단편 빈약 모자라 시도 불가능 단절(not enough) 실정일런지요? 당신이 뭇 이끄는 이 같은 판단 전개 소견 이면의 세부 무수 뒷배경 옹호 근거 조달 사유들을 명쾌히 타진 방증 강구해 정당화 증명(Justify)해 보십시오.

- (d) Answer (c) using test rather than training RSS.

- (d) 바로 직전 상단 (c)번 항목에서 전격 차용 포진 질의된 무리 맥락과 똑같은 문제 지양 제시에 대하여, 단지 요번에도 한 단계 여정의 관점 도구 축을 탈바꿈시켜 여느 뻔한 애벌 훈련(training) 점수 국면의 낡은 파생 RSS 지표를 벗어던지고 그 대신 종단 진짜 막바지 실전 등판 본 국면 실력 측정의 평가 등뼈 무대인 본재 시험(test) 역량 판별 과정 단계에서야 얻어 도출된 고유 파생 모형 RSS 지수치의 기대 폭 등락 변동 진전 예상 양상을 단서 판별 축으로 기용(using)해 고스란히 엇비슷이 거시 답변 대응(Answer)해 보십시오.

5. Consider the fitted values that result from performing linear regression without an intercept. In this setting, the $i$th fitted value takes the form

5. 애써 도출 모델 방정식에서 절편 상수(intercept) 변수를 고의로 배제 추방해 쏙 아예 제외 삭제한 채 오로지 순수 선형 회귀(linear regression) 잣대 연산만을 강제 기용 구동 단행(performing)함으로써 산입 토핑되어 얻어져 나온 판별 결과 산출물 조각인 제반 적합 값치(fitted values) 도출 성분 덩어리들을 일제히 다 거시 염두에 두고 판별 가늠 고찰 고려(Consider)해 보십시오. 이처럼 다소 특수한 차단 제약 환경 구도(setting) 내에서는, 그 어떤 산재한 제 $i$ 번 째(the $i$th) 특정 임의 배정 적합 결괏값 성분(fitted value) 지표일지라도 무적권 으레 하단 기입 공식 조달(takes the form) 이면 양상의 구도 체제를 다분히 필연적으로 따르고 지니게 됩니다:

where

**==> picture [213 x 59] intentionally omitted <==**

Show that we can write
이때 이를 발판 지렛대 기틀 부차 근거 삼아, 우리 통계 역학 수학 도출식 조작으로선 능히 이 지수를 하위 공식 표기 진전 식처럼 단숨에 한결 다르게 꼬아 도출 축약 표기(can write)해 다시 기입 적어 낼 수 있음(Show)을 명료 수식상으로 입증 시사 증명해 보이십시오:

**==> picture [65 x 28] intentionally omitted <==**

What is $a_{ij}$?
이 도달 수식 방정식 배열 속에 도사리고 끼어든 기조 파생 $a_{ij}$ 란 단연 궁극적으로 대체 무엇(What is)을 상징 배정 구사 뜻하는 매개 항의 요체인 걸까요?

_Note: We interpret this result by saying that the fitted values from linear regression are_ linear combinations _of the response values._
_※ 부연 유념 주의 참고(Note): 사실 우린 종종 이런 단편 수학 결괏값 증명 지표 양상 결과(result)들을 예의 면밀 두루 종합 분석 판별해 해석(interpret)할 요량으로, “결국 선형 회귀 연산 체제의 구동 산입 결과로 뿜어 도출 형성 기인(from linear regression)되어 나온 저 모든 고유 속성 적합 값(fitted values) 지수 성분들은, 다름 아닌 그저 실 기틀 응답 타깃 목푯값(response values) 판별 성분 치수들을 일렬 통째로 늘어뜨려 각자 비중을 두어 곱하고 단순 일방 더해 지며 만든 무수 잡다 모종의 일개 선형 결합(linear combinations) 파생 덩어리에 지나지 않는다.” 고 단언 일컫어(by saying that) 말하며 사안을 거시 맥락 부연 정의하곤 합니다._

3.7 Exercises 129

6. Using (3.4), argue that in the case of simple linear regression, the least squares line always passes through the point (¯ _x,_ ¯ _y_ ).

7. It is claimed in the text that in the case of simple linear regression of $Y$ onto $X$, the $R^2$ statistic (3.17) is equal to the square of the correlation between $X$ and $Y$ (3.18). Prove that this is the case. For simplicity, you may assume that $\bar{x} = \bar{y} = 0$.
7. 앞선 정규 도서 교재 메인 서술 텍스트 본문(in the text) 내역에선 당장, 단편 목적 종속 타깃 변수 $Y$ 값을 뭇 입력 단면 예측 기저 기준축 $X$ 에 비스듬히 맞대어 얹어 구동 도출 연루 적합시키는 단순 1차 단일 선형 회귀 모의 도달 분석 체제로 점철된 사례 기반하(in the case of simple linear regression of $Y$ onto $X$)에서는, 도파 기인된 모델 설명력 핵심 평가 점유 성향치인 당면 $R^2$ 통계 지수상 결괏값 요체(교재 내 수식 3.17번 참조)가 곧장 고스란히 다름 아닌 입력 인덱스 $X$ 지표와 응답 타깃 $Y$ 지수 둘 사이의 근거 태생 표본 상관계수(correlation) 수치를 자기 스스로 오롯이 제곱 증폭(square)시켜 굽어 뽑아낸 결괏값 성분(교재 내 수식 3.18번 참조)과 숫제 수치상 소름 끼치리만치 완벽히 고스란히 딱 한 덩어리로 합치 동일 귀결(is equal to)된다고 대대 역설 주장 선언(claimed)된 바 있습니다. 진정 이 주창된 결론 사실 기조 양상(this is the case)이 거짓 없는 진실 팩트임을 여러분의 명징 수학 논증 공통 도출 과정을 빌미로 하나하나 속 시원히 증명 파헤쳐 논증(Prove)해 보십시오. 단, 연산 과정의 수고를 덜고 계산 수식을 가급적 손쉽게 간소화(For simplicity) 축약할 척도상 목적으로, 애초 이 증명 모본 데이터 세트 전체의 구심 X 및 Y 점수 평균 좌표 지수가 가뿐히 모두 0에 수렴하는 이른바 $\bar{x} = \bar{y} = 0$ 환경 상황이라고 내심 가정 전제(assume)한 채 돌입을 시작해도 전적으로 무방히 맘껏 허용됩니다.

---

## Sub-Chapters (하위 목차)


[< 3.7 Exercises](../trans1.html) | [3.7.2 Applied >](../3_7_2_applied/trans1.html)
