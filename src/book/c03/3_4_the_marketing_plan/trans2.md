---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 6. Collinearity](../3_3_other_considerations_in_the_regression_model/3_3_3_potential_problems/6_6._collinearity/trans2.html) | [3.5 Comparison Of Linear Regression With K Nearest Neighbors >](../3_5_comparison_of_linear_regression_with_k_nearest_neighbors/trans2.html)

# 3.4 The Marketing Plan

# 3.4. 마케팅 계획 - 회장님의 7가지 질문, 최종 보고서 작성하기!

We now briefly return to the seven questions about the `Advertising` data that we set out to answer at the beginning of this chapter.
드디어 올 것이 왔습니다! 우리 이 3장의 무시무시한 서두를 열었던 그때 그 시절 기억나시나요? 회장님이 던지셨던 피 말리는 `Advertising(광고)` 장부 데이터 관련 7가지 핵심 퀘스트 질문들! 길고 긴 선형 회귀 분석의 늪을 통과한 지금, 잠시 그때로 되돌아가 최종 요약 보고서를 결재판에 올려봅시다.

1. _Is there a relationship between sales and advertising budget?_
1. _가장 근본적인 질문이오. 대체 광고 예산 쏟아부은 거랑 매출(sales) 오르는 거랑 무슨 쥐뿔 연관은 있는 거요?_

This question can be answered by fitting a multiple regression model of `sales` onto `TV`, `radio`, and `newspaper`, as in (3.20), and testing the hypothesis $H_0 : \beta_\text{TV} = \beta_\text{radio} = \beta_\text{newspaper} = 0$.
이 서슬 퍼런 1번 질문에 대한 최종 해답은 간단합니다. 수식 (3.20)에서 배운 대로 우리의 결론 타겟인 매출(`sales`)을 도마 위에 올리고, 힌트로 `TV`, `Radio`, `Newspaper(신문)` 세 변수 패거리를 통째로 집어넣어 '다중 회귀 모델'이란 믹서기를 돌린 다음! 저승사자 같은 귀무가설 $H_0 : \beta_\text{TV} = \beta_\text{radio} = \beta_\text{newspaper} = 0$ (즉, "광고 효과는 전부 0이다. 돈 버렸다! 꽝이다!")란 잣대를 법정에 세워 기각(박살) 심판을 내려버리는 것으로 시원하게 해답을 얻을 수 있습니다.

In Section 3.2.2, we showed that the $F$-statistic can be used to determine whether or not we should reject this null hypothesis.
이전 통계 법정 섹션 3.2.2 파트에서 우리는 이 망할 '전부 다 꽝이다(귀무가설)'라는 헛소리를 시원하게 깨부수고 기각할 수 있을지 없을지 최종 사형 여부를 결정지어 줄 판사님 망치 지표로 **$F$-통계량(F-statistic)** 스탯을 꺼내 들 수 있음을 증명 실습해 보였습니다.

In this case the $p$-value corresponding to the $F$-statistic in Table 3.6 is very low, indicating clear evidence of a relationship between advertising and sales.
우리의 훌륭한 [표 3.6] 성적표 재판 결과! 이 예제 모델이 토해낸 $F$-통계치와 연좌되어 딸려 나온 그 $p$-값(확률 꼬리표) 척도가 세상에, 0에 수렴할 만큼 몹시 콩알만 하게 낮게 박혔습니다! 이는 곧, "회장님! 전반적인 광고 예산 활동과 매출(sales) 사이에는 아주 명백하고 확연한 찰떡 연관 관계가 필연 존재합니다!"라고 두말할 필요 없이 뚜렷이 증명하는 절대 무적 증거물인 셈입니다.

2. _How strong is the relationship?_
2. _연관이 있다는 건 알겠네. 그럼 그 효과가 도대체 얼마나 막강하게 강하단 말이오?_

We discussed two measures of model accuracy in Section 3.1.3.
우리는 앞선 섹션 3.1.3 단면에서 우리 모델이 얼마나 신궁처럼 잘 맞히는지 그 정확도를 채점하고 평가 단안 지표하는 두 가지 주요 척도의 방법론을 이미 깊숙이 논의했습니다.

First, the RSE estimates the standard deviation of the response from the population regression line.
첫째 채점관, **RSE(잔차 표준 오차)** 잣대입니다. 이놈은 모집단 회귀선(신의 정답선) 모델 기준에서 응답치(매출 결괏값)들이 빗나가며 뿜어내는 '오차 찌꺼기들의 널뛰기 표준 편차치'를 추산 가늠해 내는 패널티 빚더미 채점관입니다.

For the `Advertising` data, the RSE is $1.69$ units while the mean value for the response is $14.022$, indicating a percentage error of roughly $12\%$.
`Advertising` 데이터 예시 성적표 결과를 까보면, 이 산출된 빚더미 RSE 수치는 대략 $1.69$ (단위: 1,000대) 규모로 터져 나오는 반면, 우리 가게 전체 평균 매출(응답값) 볼륨 사이즈는 무려 $14.022$에 달합니다. 14 언저리 매출에 오차율이 1.69 정도면? 이를 비율상 따져보면 대략 고작 $12\%$ 수준의 미미한 소액 푼돈 상대적 오차율 타격만 존재함을 나타냅니다. (이 정도면 훌륭하죠!)

Second, the $R^2$ statistic records the percentage of variability in the response that is explained by the predictors.
둘째 채점관은 무적의 방어력 스탯, **$R^2$(결정 계수)** 통계 수치 지표입니다. 이 녀석은 우리가 욱여넣은 힌트 예측 변수들이 타겟 매출 응답 결과 쪽에서 발생하는 전체 변동성 흔들림의 파이를 도대체 몇 퍼센트(%)나 철권 통치해 커버 치며 입증(설명)해 내는지 지분을 방어 기록 산입하는 위대한 방패입니다.

The predictors explain almost $90\%$ of the variance in `sales`.
결과는 눈부십니다! 위 세 가지 광고 예측 변수들은 단연코 매출(`sales`) 타겟 에 발생한 전체 총 흔들림(분산)의 거의 대략 $90\%$ 상당이라는 압도적 무적 방어력 지분 파이를 말끔 통제 해명 방어해 냅니다.

The RSE and $R^2$ statistics are displayed in Table 3.6.
이 이뤄낸 위대한 두 성적, RSE와 $R^2$ 결과 통계 내역은 함께 묶여 [표 3.6] 전시 도표 성적표에 당당히 랭크 표시되어 있습니다.

3. _Which media are associated with sales?_
3. _우리 부서 3개 (TV, 라디오, 신문) 중에서 과연 어느 부서 매체가 실제 매출 떡상에 진짜 기여한 1등 공신 연관 부서들이오?_

To answer this question, we can examine the $p$-values associated with each predictor's $t$-statistic (Section 3.1.2).
이 살벌한 구조조정 질문의 물음에 명확히 핀셋으로 도려내 답하고자, 우리는 다시 법정을 열어 각 매체 부서 예측 변수 놈들 마빡에 핑 당 찍혀 부여된 $t$-통계량과, 그 옆에 질척하게 같이 맞물려 연관된 합격 꼬리표 $p$-값 지수들을 단편 살벌 개별 심사 검문 조사해 볼 수 있습니다(섹션 3.1.2 참조).

In the multiple linear regression displayed in Table 3.4, the $p$-values for `TV` and `radio` are low, but the $p$-value for `newspaper` is not.
[표 3.4]에 기재된 다중 결합 선형 회귀 재판 결과 측면을 보십쇼. 다대다 결투에서 살아남은 합격 꼬리표를 보면, 이중 `TV` 부서와 `Radio` 부서에 책정된 두 $p$-값 심사 수치는 바닥을 뚫을 만큼 눈에 띄게 현격히 낮습니다! 하지만 정작 우리의 혈세 낭비 `Newspaper(신문)` 부서의 $p$-값은? 안타깝게도 결코 그다지 낮지 않고 0.8 언저리 꼴통 오답 점수 합격선을 그립니다.

This suggests that only `TV` and `radio` are related to `sales`.
이러한 단편적 채점 결과 팩트는 기실 무대 뒤에서 묵묵히 밥값 하며 진짜 매출(`sales`) 쪽과 끈끈한 유의미 연관 관계에 놓인 건 뼈 빠지는 `TV` 팀과 `Radio` 팀 단 두 부서뿐이란 서글픈 사실을 노골적으로 시사합니다. (신문은 프리라이더였습니다!)

In Chapter 6 we explore this question in greater detail.
향후 머나먼 제 6장에서 이 서글픈 구조조정 후보군 선택 질문 장치를 다시금 소환해 한층 더 스마트하고 세부적인 방법으로 깊게 파헤쳐 가려 탐구해 볼 것입니다.

4. _How large is the association between each medium and sales?_
4. _좋아, TV랑 라디오가 잘한 건 알겠소. 그럼 각 매체별로 판매량 사이에 형성된 연관성의 진짜 파워! 영향력 규모는 정확히 어느 정도나 치솟소?_

We saw in Section 3.1.2 that the standard error of $\hat{\beta}_j$ can be used to construct confidence intervals for $\beta_j$.
우린 지난 섹션 3.1.2 부문 훈련소에서 배운 바 있습니다. 우리가 도출한 각 회귀 계수 타격력 덩어리 $\hat{\beta}_j$ 척도 요소가 지닌 약점인 '표준 오차' 값이, 실은 거꾸로 찐 계수 능력치 $\beta_j$ 의 든든한 방벽 '신뢰 구간(confidence interval)' 궤도를 설정 구성 구축하고 울타리 치는 데 널리 요긴히 쓰일 수 있음을 생생히 지켜보았습니다.

For the `Advertising` data, we can use the results in Table 3.4 to compute the $95\%$ confidence intervals for the coefficients in a multiple regression model using all three media budgets as predictors.
`Advertising` 데이터 예제판에 이걸 그대로 빗대어 비벼 봅니다. 우리 측은 앞서 구한 [표 3.4]에 기재된 통계 계수 결과 조각들을 재차 적극 줍줍 활용하여, 세 종류 미디어 예산 전부를 다 같이 욱여넣고 예측 변수로 삼아 수립한 다중 회귀 모델의 각 궤도별 계수 파워에 대한 영광의 **$95\%$ 신뢰 구간** 바운더리를 산입 계산 쪼개 도출해 낼 수 있습니다.

The confidence intervals are as follows: $(0.043, 0.049)$ for `TV`, $(0.172, 0.206)$ for `radio`, and $(-0.013, 0.011)$ for `newspaper`.
그 결과 산출된 각 항목 부서별 파워 보증 신뢰 구간은 다음과 같습니다: 
*   `TV` 팀 위력 궤도는 $(0.043, 0.049)$,
*   `Radio` 팀 위력 궤도는 $(0.172, 0.206)$,
*   그리고 문제의 잉여 `Newspaper` 팀 궤도는 $(-0.013, 0.011)$ 입니다.

The confidence intervals for `TV` and `radio` are narrow and far from zero, providing evidence that these media are related to `sales`.
보이십니까? `TV`며 `Radio` 부서가 획득한 신뢰 구간 대역폭 텐션 궤도는 양수(+) 구역에서 대단히 옹골하게 좁고 안정적이며 또 그 영토 위치조차 기준 하한선인 0(아무 타격 없음)에서 한참 멀리 하늘로 이격되어 있습니다! 이는 단연코 이들 둘 매체 녀석들만큼은 `sales` 매출 떡상 상승 측 지표와 확실히 쓸모 있게 견인 연관되어 있음을 보증하는 쐐기 증거를 철통같이 제공합니다.

But the interval for `newspaper` includes zero, indicating that the variable is not statistically significant given the values of `TV` and `radio`.
하지만!! 아까 그 프리라이더 `Newspaper(신문)` 부서가 띠고 걸터앉은 신뢰 구간 잣대 영토는요, 재수 없게도 그 가운데에 음수(-)와 양수(+)를 가로지르는 맹탕 무효 구역 **'0(zero)'** 수치가 재앙처럼 떠억 껴서 포함 속해 있습니다. 이는 이미 주어진 잘나가는 `TV` 및 `radio` 변수 잣대 일잘러 값들 여건하에서는, 정작 저 신문 변수 하나는 혼자 뒤로 마이너스 까먹을 수도, 아무 효과가 없을 수도 있는 그저 딱히 어떠한 별다른 통계적 유의성마저 확보 내지 지니지 못하는 폐급 낙제 변수임을 여실히 대변해 팩트 폭격합니다.

We saw in Section 3.3.3 that collinearity can result in very wide standard errors.
그런데 잠깐. 앞 챕터 섹션 3.3.3 다중공선성 빌런 파트에서 우리는 심각한 '공선성(짬짜미 병균)'이 모델에 끼어들면 때론 아주 극단적으로 방대한 허벌창 넓은 폭의 무쓸모 뻥튀기 표준 오차 텐션 수치를 초래할 소지 파멸이 다분함을 논의했죠.

Could collinearity be the reason that the confidence interval associated with `newspaper` is so wide?
그렇담 혹시, 저 병신 같은 `Newspaper(신문)` 부서에 연관된 신뢰 구간의 폭이 저리 넓게 쓸모없이(음수부터 양수까지) 벌어지고 형성된 주된 핑계 연유가, 다름 아닌 저놈 신문이 라디오랑 작당 범죄 모의를 꾸민 그런 공선성 역병 타격 탓은 아닐까요? (한 번 구제해 봅시다.)

The VIF scores are $1.005$, $1.145$, and $1.145$ for `TV`, `radio`, and `newspaper`, suggesting no evidence of collinearity.
자, 그래서 범인 탐지기 VIF(분산 팽창 인수) 판독기를 찍어봤습니다. 웬걸? 현재 각 `TV`, `radio`, 그리고 `newspaper` 항목별 VIF 계산 점수 판독 지표는 순서대로 각각 청정 구역 점수인 $1.005$, $1.145$, 그리고 $1.145$ 마진 수치에 꼴랑 불과합니다! (5점도 안 됩니다.) 즉, 이는 실상 어느 모델 국면 단면에도 변수끼리 공선성 결탁 폐해 짬짜미를 저질렀다는 핑계댈 시사 증거 따윈 도무지 일절 없다는 빼박 사실을 아주 철저히 부연해 제안 무마 설명합니다. (신문은 그냥 무능한 거였습니다!)

In order to assess the association of each medium individually on sales, we can perform three separate simple linear regressions.
번외로, 만일 3놈을 통째 결투 안 시키고 각 단일 미디어 부서 하나하나가 어떻게 독립 독고다이 개별적으로 전체 판매 타겟 부문에 1:1 영향을 미치는지 딜량을 정확히 개별 판가름 수사하고 평가 가늠코자 한다면? 우리는 세 차례의 별도 각방 분리된 '단순 선형 회귀 타격 모형' 측면을 각 1:1 개별 단독 전개 및 결투 수행해 볼 수도 있습니다.

Results are shown in Tables 3.1 and 3.3.
그렇게 1:1로 각개전투 분리해 돌려 도출된 단선 모의 결과들은 각각 무대 나누어 [표 3.1]이며 [표 3.3] 양 챔피언 측면에 분리 제시 전시되어 있습니다.

There is evidence of an extremely strong association between `TV` and `sales` and between `radio` and `sales`.
뭐 어떻게 1:1로 찢어 놔봐도, 여전히 `TV`며 `sales` 사이, 그리고 `radio` 및 `sales` 사이 이 두 부서 경우 양쪽 모두에선 단독이라도 대단 아주 짱짱하게 결부 융합된 극심한 강한 연관성 여부의 활약 단서 증거가 양쪽 모두 뚜렷 눈썹 튀게 나타나 보입니다.

There is evidence of a mild association between `newspaper` and `sales`, when the values of `TV` and `radio` are ignored.
놀라운 반전! 아까 다중 결투에선 폐급이었던 신문도... 다만 아주 애초 백지수표 기저에 널린 잘난 여타 경쟁자 `TV` 부서라거나 혹은 `radio` 따위 여타 천재 변수 인자 값들 동료를 통째 세상에서 아예 지워버려 무시해 덮고 고려 원천 배제했을 단신 무대 상황 시에 한하여!! 저기 초라한 `newspaper` 단면과 최종 `sales` 부문 타겟 사이에 겨우 그나마 얕고 온화 약소 짜잘한 미미한 잔기스 연관 기류가 일부 다행스레 좀 존재 구원된다는 어처구니 기막힌 증거 여부만이 극소수 관찰 도출될 따름입니다. (즉, TV/라디오가 없으면 신문도 꼴에 효과는 있다는 뜻이죠.)

5. _How accurately can we predict future sales?_
5. _이 모델 들고 나가서 실전 뛰면, 다가올 미래 향후의 총 판매량을 우리는 과연 얼마나 정밀하게 예측해 낼 수 있소?_

The response can be predicted using (3.21).
목표 향후 타겟 응답치 예언은 공식 (3.21) 예측 머신 단말기 형태를 전면 이용해서 모의 산입해 뽑아 낼 수 있습니다.

The accuracy associated with this estimate depends on whether we wish to predict an individual response, $Y = f(X) + \epsilon$, or the average response, $f(X)$ (Section 3.2.2).
그런데 여기서 주의! 이 산출된 추정치 예언 결과가 띠는 신뢰 타점 정확도는, 우리가 궁극적으로 점치고 예측하길 희망 지향하는 예언 방향의 바가... 
어느 **'특정 매장 단일 낱개 일개 응답치 측면' (즉, 변덕스러운 오차 $\epsilon$ 폭탄까지 감수해야 하는 $Y = f(X) + \epsilon$ 국면)**인지?
아니면 **'전국 체인망 전반적인 전체 평균 타점 지표 응답 대푯값 고정 요소 모의' (즉, 안정적인 $f(X)$ 중심 국면)**인지(섹션 3.2.2 구조 참조)에 전적으로 크게 좌우 기여 심각히 의존합니다!

If the former, we use a prediction interval, and if the latter, we use a confidence interval.
만일 우리의 이번 예언 목표 타겟 시선이 전자에 쏠려 있다면(한 매장의 험난한 오차 실전!), 널뛰기 방어용인 통상 헐렁헐렁 넓은 **예측 구간(Prediction Interval)** 그물 철조망 틀을 차용해야 치고! 후자에 안정적 뜻을 두었다면(전국 평균의 고요함!), 쫀쫀하고 좁쌀 탄탄한 **신뢰 구간(Confidence Interval)** 기조 잣대를 착 달라붙게 적용 동반 사용합니다.

Prediction intervals will always be wider than confidence intervals because they account for the uncertainty associated with $\epsilon$, the irreducible error.
주지하듯 '예측 구간' 방어 범위는 절대 빼거나 축소 축적 단축 불가결한 통계의 악마 궤도! 이른바 절대로 줄일 수 없는 태생 오차(irreducible error) 잡동사니 격인 $\epsilon$ 잡음 파동 속성 관련 기저 불확실성 소지 잔여 흔들림 여파 파동까지 구태여 모조리 다 총체 감안 포용 동반 넉넉 수치 계산 합산해야 하므로, 아주 십중팔구 예외 없이 늘 평온한 신뢰 구간보다 훨씬 더 무지막지 가로로 늘어져 넓게 팽창 벌어져 나타날 수밖에 없습니다.

6. _Is the relationship linear?_
6. _그렇담 질문. 걔네들 사이에 끈끈하게 형성된 변수 간 내재 관계 양상의 모양은 쭉 뻗은 '선형성(직선)' 기조를 띱니까?_

In Section 3.3.3, we saw that residual plots can be used in order to identify non-linearity.
저기 뒷장 섹션 3.3.3 파트 병동에서 우리는 이 빌어먹을 비틀린 병동 곡선! 비선형성 곡선 형태를 인지 단안 족집게 식별해 내는 최첨단 엑스레이 주요 목적 용도로 **잔차 플롯(Residual Plots, 찌꺼기 그래프)** 이 아주 죽여주게 요긴 적용 사용될 수 있음을 지켜보았습니다.

If the relationships are linear, then the residual plots should display no pattern.
만일 그들 구동 모델 장치 안의 잔존 관계 베이스가 거짓 없이 올곧게 쭉 뻗은 선형(직선) 관계가 맞다면? 이 엑스레이를 찍어 투영 산출된 잔차 플롯 점박이 하늘 표면 구역에는 일절 우주 쓰레기 먼지 마냥 아무 특징이나 패턴 U자 모양 형태 무늬 흔적 따위가 아예 랜덤 노이즈 구름처럼 아무런 특징치도 척도조차 나타나지 않아야 올곧은 정상 합격입니다.

In the case of the `Advertising` data, we observe a non-linear effect in Figure 3.5, though this effect could also be observed in a residual plot.
하지만 슬프게도 이 `Advertising` 광고 장부 데이터 사례 예시 국면 투사판에선, 설사 굳이 이 돌출 파급력을 잔차 플롯 엑스레이에서 직접 포착 진단 확인하지 않았을 수도 있겠으나... 여실히 위 그림 3.5 측면에 너무나 버젓이 구부러진 시너지 비선형 곡선 형태 굴곡 효과 지수 파급이 대놓고 노골 표출되어 곡면 나타남을 우리 두 육안으로 처참 관찰 확인할 수 있습니다.

In Section 3.3.2, we discussed the inclusion of transformations of the predictors in the linear regression model in order to accommodate non-linear relationships.
이렇게 선형이 아닌 걸로 판명 났을 땐 어쩌냐고요? 괜찮습니다. 섹션 3.3.2 수술실 파트에서 우리는 뻣뻣한 모델 내에 이렇듯 구부러지고 복잡다단한 비선형 성격 관련성을 타협 접목 수용코자, 통상 일선 쭉 뻗은 선형 회귀 모델 편제 틀 안에 여러 예측 변수에 대한 갖가지 루트(제곱근), 제곱승 따위 곡면 유연 치환 변환 도구 유가 요가 관절 이식 기능을 무리 산입 추가 포함해 두면서 극복하는 해결 돌파구를 둘러싸고 논의를 개진한 바 있습니다.

7. _Is there synergy among the advertising media?_
7. _마지막 질문! TV랑 라디오, 신문 광고 미디어 놈들 매체들 그 사이사이에 일말의 어떤 모종의 1+1=3 짬짜미 합체 폭발 마력 '시너지 효과'가 덤으로 껴 도사려 있소이까?_

The standard linear regression model assumes an additive relationship between the predictors and the response.
이봐요, 바닐라 완전 깡통 무옵션 단순 무결한 가장 보편 기초 표준 '선형 회귀 모의' 베이스는 본디 들어간 예측 변수 요인 무리 힌트들과 결론 응답 스코어 측 사이에 티끌의 이변 짬짜미 흔들림 없는 다소 지극 융통성 제로인 철저 1+1=2 일관 기조의 단순 **가산적(additive, 더하기)** 독립 측면 관계 체계만이 오직 성립하리라 깡통 임의 고정 가정합니다.

An additive model is easy to interpret because the association between each predictor and the response is unrelated to the values of the other predictors.
어차피 이런 기초적인 깡통 단순 가산 모델 덧셈 구조는 뭐, 개별 투사 예측 변수 낱개가 최종 결론 파견 응답과 찔리며 개별적으로 엮어 맺는 영향력 딜량 일련의 결부 연관성 자체가, 옆 부서 이웃인 '이렇다 할 다른 여타 나머지 예측 변숫값들' 놈들의 텐션 변동 동요량과 1도 전조 엮임이나 상관 간섭 없이 절대 남남 무관한 까닭 궤도 설계인지라... 나중에 향후 회가 수치를 풀어 나열 성적 결과물 리포트를 단순 일차원 해석하고 결재 올리기 참 유용하고 짱 쉽습니다.

However, the additive assumption may be unrealistic for certain data sets.
허나!! 빡센 현실 현장은 다르죠. 막상 역동적 미쳐가는 상권 몇몇 특정 콤플렉스 예외 소지 데이터 마케팅 세트 군집에서는 이러한 1+1=2 일방적 깡통 단순 무결 가산 기조 전제 가정 나이브 공식이, 그저 코웃음 나오는 책상물림 허상에 불과할 만치 자못 영 터무니없이 극 비현실적 막장 오류 결핍 국면 예측으로 돌변 나타날지 모릅니다!

In Section 3.3.2, we showed how to include an interaction term in the regression model in order to accommodate non-additive relationships.
이윽고 그래서! 우리 앞선 섹션 3.3.2 요가 기술 수술 절에서 우리는 이러한 현실의 폭풍 시너지! 다소 비가산적 측면 파동 짬뽕 관계 융합 기조를 보완 조달 접목해 유연하게 수용 타개하고자 회귀 산출 깡통 모델 진열 블록 안에 전혀 새로운 변이 합성 컴바인 마법 블록, 위대한 **상호작용 항(interaction term, 곱하기 교배 항)**을 인공 부가 무리 부착 조립 이식 포함 산입케 할 위대한 돌파구 연금 마법 방도를 통쾌 전개 소개했습니다.

A small $p$-value associated with the interaction term indicates the presence of such relationships.
통상 이러한 교배 이식 상호작용 측면 인공 항과 긴밀 연좌 재판에 넘겨진 평가 엮어진 아주 귀여운 콩알만 한 작은 $p$-값 크기 꼬리표 합격 스탯은? 게임 끝입니다. 막상 모델에 팩트 폭격 날리듯 그런 1+1=3 시너지 이질적 복합 관계 존재 파워가 실제 우리 장부 데이터 안에 실질 어마어마하게 파고 숨어 구동 작용 중이었음을 빼박 확증 뚜렷 지지 적시 만천하에 고발합니다.

Figure 3.5 suggested that the `Advertising` data may not be additive.
이러한 곡면 상승 연유로 이미 [그림 3.5] 도면 엑스레이는, 애당초 `Advertising` 타겟 관련 산입 투여 광고 예산 데이터가 실상 완전히 깡통처럼 더하기(가산적) 1차원 측면만 띠지 않을 수 있단 시너지 폭발 곡리 여력을 은연 시사 강하게 굴곡 그려 제안한 바 있습니다.

Including an interaction term in the model results in a substantial increase in $R^2$, from around $90\%$ to almost $97\%$.
기실 결론 축포! 야생 해당 투박한 모델 내부에 이 위대하고 거룩한 조화의 '상호작용 항(TV $\times$ Radio)' 짬뽕 변수를 1개 더해 꼽사리 함께 곱사등 부착 포함 산입시켜버리는 간단 추가 조치 튜닝 행위 한 번 만으로도!! 산출 방어력 반환 성적표 **$R^2$(설명력)** 수준 맷집 방어막은 기존 $90\%$ 안팎가량 치수 따위에서! 호러 미친 오버 수직 점프 폭발 상승!! 무려 자그마치 대규모 천상계 거의 **$97\%$** 근접 극한 영역 수준까지 대단 아주 비약 천장 뚫는 상당하고 막대 폭발 실질적인 극강 시너지 시프트 수직 상승 증가하는 퍼펙트 클리어 기적의 성과 지표 결과를 배출 표출해 증명 쐐기를 선언 냅니다!

---

## Sub-Chapters (하위 목차)


[< 6. Collinearity](../3_3_other_considerations_in_the_regression_model/3_3_3_potential_problems/6_6._collinearity/trans1.html) | [3.5 Comparison Of Linear Regression With K Nearest Neighbors >](../3_5_comparison_of_linear_regression_with_k_nearest_neighbors/trans1.html)
