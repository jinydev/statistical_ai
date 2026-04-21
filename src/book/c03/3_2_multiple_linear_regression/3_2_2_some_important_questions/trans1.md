---
layout: default
title: "trans1"
---

[< 3.2.1 Estimating The Regression Coefficients](../3_2_1_estimating_the_regression_coefficients/trans1.html) | [3.2.2.1 Two Deciding On Important Variables >](3_2_2_1_two_deciding_on_important_variables/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 3.2.2 Some Important Questions

# 3.2.2 몇 가지 중요한 질문들 (Some Important Questions)

When we perform multiple linear regression, we usually are interested in answering a few important questions.

우리가 다중 선형 회귀를 수행할 때, 일반적으로 몇 가지 중요한 질문에 답하는 데 관심을 갖습니다.

1. _Is at least one of the predictors $X_1, X_2, \dots, X_p$ useful in predicting the response?_

1. _예측 변수 $X_1, X_2, \dots, X_p$ 중에서 적어도 하나는 응답을 예측하는 데 유용한가?_

2. _Do all the predictors help to explain $Y$, or is only a subset of the predictors useful?_

2. _모든 예측 변수들이 $Y$ 를 설명하는 데 도움이 되는가, 아니면 특정한 예측 변수들의 부분 집합만이 유용한가?_

3. _How well does the model fit the data?_

3. _모델이 데이터에 얼마나 잘 적합되는가?_

4. _Given a set of predictor values, what response value should we predict, and how accurate is our prediction?_

4. _주어진 예측 변수 값의 집합에 대해 우리는 어떤 응답 값을 예측해야 하며, 우리의 예측은 얼마나 정확한가?_

We now address each of these questions in turn.

이제 이 질문들을 차례대로 다루어 보겠습니다.

## One: Is There a Relationship Between the Response and Predictors?

## 질문 1: 반응 변수와 예측 변수들 사이에 관계가 있는가?

Recall that in the simple linear regression setting, in order to determine whether there is a relationship between the response and the predictor we can simply check whether $\beta_1 = 0$.

단순 선형 회귀 설정에서는 응답과 예측 변수 사이에 관계가 있는지 판단하기 위해 단순히 $\beta_1 = 0$ 인지만 확인하면 된다는 점을 상기하십시오.

In the multiple regression setting with $p$ predictors, we need to ask whether all of the regression coefficients are zero, i.e. whether $\beta_1 = \beta_2 = \dots = \beta_p = 0$.

$p$ 개의 예측 변수가 있는 다중 회귀 설정에서는 모든 회귀 계수가 0인지, 즉 $\beta_1 = \beta_2 = \dots = \beta_p = 0$ 인지를 질문해야 합니다.

As in the simple linear regression setting, we use a hypothesis test to answer this question.

단순 선형 회귀 설정에서와 마찬가지로 우리는 이 질문에 대답하기 위해 가설 검정을 사용합니다.

We test the null hypothesis,

우리는 다음 귀무 가설을 검정합니다.

$$
H_0 : \beta_1 = \beta_2 = \dots = \beta_p = 0 \quad (3.23)
$$

versus the alternative

대립 가설은 다음과 같습니다.

$$
H_a : \text{at least one } \beta_j \text{ is non-zero.}
$$

This hypothesis test is performed by computing the _F -statistic_ ,

이 가설 검정은 _F-통계량(F-statistic)_ 을 계산하여 수행됩니다.

$F$-statistic ($F$-통계량)

$$
F = \frac{(\text{TSS} - \text{RSS}) / p}{\text{RSS} / (n - p - 1)} \quad (3.24)
$$

where, as with simple linear regression, $\text{TSS} = \sum (y_i - \bar{y})^2$ and $\text{RSS} = \sum (y_i - \hat{y}_i)^2$.

단순 선형 회귀에서와 마찬가지로, 여기서 $\text{TSS} = \sum (y_i - \bar{y})^2$ 이고 $\text{RSS} = \sum (y_i - \hat{y}_i)^2$ 입니다.

If the linear model assumptions are correct, one can show that

만약 선형 모델의 여러 가정들이 올바르다면, 다음을 보여줄 수 있습니다.

$$
E\{\text{RSS} / (n - p - 1)\} = \sigma^2
$$

and that, provided $H_0$ is true,

그리고 만약 $H_0$ 가 참이라면, 다음이 성립합니다.

$$
E\{(\text{TSS} - \text{RSS}) / p\} = \sigma^2
$$

Hence, when there is no relationship between the response and predictors, one would expect the $F$-statistic to take on a value close to 1.

그러므로 응답과 예측 변수들 사이에 아무런 관계가 없을 때, $F$-통계량이 1에 가까운 값을 가질 것이라 기대할 수 있습니다.

On the other hand, if $H_a$ is true, then $E\{(\text{TSS} - \text{RSS}) / p\} > \sigma^2$, so we expect $F$ to be greater than 1.

반대로 만약 $H_a$ 가 참이라면 $E\{(\text{TSS} - \text{RSS}) / p\} > \sigma^2$ 이 성립하므로, 우리는 $F$ 가 1보다 클 것이라 기대합니다.

The $F$-statistic for the multiple linear regression model obtained by regressing `sales` onto `radio`, `TV`, and `newspaper` is shown in Table 3.6.

`sales` 를 `radio`, `TV`, 그리고 `newspaper` 에 회귀시켜 얻은 다중 선형 회귀 모델의 $F$-통계량은 표 3.6 에 나타나 있습니다.

In this example the $F$-statistic is 570.

이 예제에서 $F$-통계량은 570 입니다.

Since this is far larger than 1, it provides compelling evidence against the null hypothesis $H_0$.

이 값은 1보다 훨씬 크기 때문에, 귀무가설 $H_0$ 에 반하는 매우 강력한 증거를 제공합니다.

In other words, the large $F$-statistic suggests that at least one of the advertising media must be related to `sales`.

다시 말해, 큰 $F$-통계량은 최소한 하나의 광고 매체가 반드시 `sales` 와 연관되어 있음을 시사합니다.

However, what if the $F$-statistic had been closer to 1?

하지만 만일 $F$-통계량이 1에 훨씬 더 가까웠다면 어땠을까요?

| Quantity | Value |

| :--- | :--- |

| Residual standard error | 1.69 |

| $$R^2$$ | 0.897 |

| $F$-statistic | 570 |

**TABLE 3.6.** _More information about the least squares model for the regression of number of units sold on TV, newspaper, and radio advertising budgets in the_ `Advertising` _data. Other information about this model was displayed in Table 3.4._

**TABLE 3.6.** `Advertising` _데이터에서 TV, 신문, 라디오 광고 예산에 따른 판매량의 최소 제곱 회귀 모델에 대한 추가 정보입니다. 이 모델에 대한 기타 정보는 표 3.4 에 표시되었습니다._

How large does the $F$-statistic need to be before we can reject $H_0$ and conclude that there is a relationship?

$H_0$ 를 기각하고 관계가 있다고 결론 내리기까지 $F$-통계량은 무릇 얼마나 커야 할까요?

It turns out that the answer depends on the values of $n$ and $p$.

결과적으로 그 해답은 $n$ 과 $p$ 의 값에 달려 있습니다.

When $n$ is large, an $F$-statistic that is just a little larger than 1 might still provide evidence against $H_0$.

$n$ 이 클 때에는 단지 1보다 약간만 더 큰 $F$-통계량이라도 여전히 $H_0$ 에 반하는 증거를 제공할 수 있습니다.

In contrast, a larger $F$-statistic is needed to reject $H_0$ if $n$ is small.

반대로 $n$ 이 작다면 $H_0$ 를 기각하기 위해 더 덩치가 큰 $F$-통계량이 요구됩니다.

When $H_0$ is true and the errors $\epsilon_i$ have a normal distribution, the $F$-statistic follows an $F$-distribution.$^6$

$H_0$ 가 참이고 오차 $\epsilon_i$ 가 정규 분포를 가질 때, $F$-통계량은 $F$-분포를 따릅니다.$^6$

For any given value of $n$ and $p$, any statistical software package can be used to compute the $p$-value associated with the $F$-statistic using this distribution.

$n$ 과 $p$ 의 임의의 주어진 값에 대해, 어떠한 통계 소프트웨어 패키지든 이 분포를 이용하여 $F$-통계량과 연관된 $p$-값을 계산하는 데 사용할 수 있습니다.

Based on this $p$-value, we can determine whether or not to reject $H_0$.

계산된 $p$-값을 토대로 우리는 $H_0$ 의 기각 여부를 결정할 수 있습니다.

For the advertising data, the $p$-value associated with the $F$-statistic in Table 3.6 is essentially zero, so we have extremely strong evidence that at least one of the media is associated with increased `sales`.

광고 데이터의 경우, 표 3.6 의 $F$-통계량과 묶인 $p$-값은 사실상 거의 0 에 수렴하므로, 우리는 매체들 중 적어도 하나는 증가된 `sales` 와 강한 인과 연관성이 있다는 극도로 확고한 증거를 가집니다.

In (3.23) we are testing $H_0$ that all the coefficients are zero.

수식 (3.23) 에서 우리는 모든 계수들이 모조리 0 인가라는 $H_0$ 척도를 검정하고 있습니다.

Sometimes we want to test that a particular subset of $q$ of the coefficients are zero.

때때로 우리는 계수들 중 특정 $q$ 개의 부분 집합이 0 인가를 검정하길 원할 수 있습니다.

This corresponds to a null hypothesis

이는 다음의 귀무 가설과 부합합니다.

$$
H_0 : \beta_{p-q+1} = \beta_{p-q+2} = \dots = \beta_p = 0
$$

where for convenience we have put the variables chosen for omission at the end of the list. In this case we fit a second model that uses all the variables _except_ those last $q$. Suppose that the residual sum of squares for that model is $\text{RSS}_0$. Then the appropriate $F$-statistic is

편의를 도모하기 위해 우리는 목록의 가장 마지막 순서에 배제할 목적으로 선택된 변수들을 위치시켰습니다. 이 경우 우리는 제일 마지막 그룹인 $q$ 개 항목만들을 _제외시킨_ 나머지 모든 변수들을 사용하는 두 번째 모델을 적합 적용합니다. 해당 파생 모델의 잔차 제곱For instance, consider an example in which $p$ = 100 and $H_0$ : $\beta_1 = \beta_2 = \dots = \beta_p = 0$ is true, so no variable is truly associated with the response. In this situation, about 5 % of the $p$-values associated with each variable (of the type shown in Table 3.4) will be below 0.05 by chance. In other words, we expect to see approximately five small $p$-values even in the absence of any true association between the predictors and the response. In fact, it is likely that we will observe at least one $p$-value below 0.05 by chance! Hence, if we use the individual $t$-statistics and associated $p$-values in order to decide whether or not there is any association between the variables and the response, there is a very high chance that we will incorrectly conclude that there is a relationship. However, the $F$-statistic does not suffer from this problem because it adjusts for the number of predictors. Hence, if $H_0$ is true, there is only a 5 % chance that the $F$-statistic will result in a $p$-value below 0.05, regardless of the number of predictors or the number of observations.

예를 들어, 예측 변수의 개수가 $p = 100$ 이고 $H_0 : \beta_1 = \beta_2 = \dots = \beta_p = 0$ 이 참이어서 어떤 변수도 반응 변수와 실질적으로 연관되지 않은 예제를 생각해 보십시오. 이 상황에서 각 변수와 연관된 $p$-값(표 3.4에 표시된 유형)의 약 5%는 우연히 0.05 미만이 될 것입니다. 다시 말해, 예측 변수와 반응 변수 사이에 아무런 실제 연관성이 없더라도 우리는 약 5개의 작은 $p$-값을 예상할 수 있습니다. 사실 우리는 우연히 0.05 미만의 $p$-값을 최소한 하나 이상 관찰할 가능성이 매우 높습니다! 따라서 만약 우리가 변수와 응답 사이에 연관성이 있는지 여부를 결정하기 위해 개별 $t$-통계량과 연관된 $p$-값을 사용한다면 관계가 존재한다고 잘못 결론 내릴 가능성이 매우 높습니다. 하지만 전체 $F$-통계량은 예측 변수의 개수에 맞게 조정되므로 이 문제점을 겪지 않습니다. 따라서 $H_0$ 가 참이라면, 예측 변수의 개수나 관측치의 개수와 관계없이 $F$-통계량이 0.05 미만의 $p$-값을 가져올 확률은 오직 5% 에 불과합니다.

The approach of using an $F$-statistic to test for any association between the predictors and the response works when $p$ is relatively small, and certainly small compared to $n$ . However, sometimes we have a very large number of variables. If $p > n$ then there are more coefficients $\beta_j$ to estimate than observations from which to estimate them. In this case we cannot even fit the multiple linear regression model using least squares, so the _F_ - statistic cannot be used, and neither can most of the other concepts that we have seen so far in this chapter. When $p$ is large, some of the approaches discussed in the next section, such as _forward selection_ , can be used. This _high-dimensional_ setting is discussed in greater detail in Chapter 6.

예측 변수와 응답 변수 간의 그 어떤 연관성을 검정하기 위해 별도 분산 $F$-통계량을 사용하는 이 접근법은 $p$ 가 상대적으로 작을 때 효과적이며, 확실히 $n$ 에 비해 수적 밀리고 작을 때 잘 성립합니다. 하지만 때때로 우리는 대단히 많은 개수에 달하는 변수를 보유할 때가 있습니다. 만약 $p > n$ 이라면 추정해야 할 대상 계수 모수 측정 $\beta_j$ 지표들이 그것들을 산출 추정하는 뿌리 기초 관측 표본 데이터량보다 되려 더 방만하게 과잉 존재하게 됩니다. 이 거동 불가 조건 상황에선 차라리 전통적인 최소 제곱 수학 접근을 사용하여 다중 선형 회귀 모델을 적합시키는 조치마저 아예 원천적인 도달 실패 불능에 이르므로, 고로 저 _F_-통계량 도구 역시 사용될 수 전무할뿐더러 우리가 현 챕터 과정에서 여태껏 지나와 살펴본 여타 다른 주요 통계 원리 개념의 상당수 역시 모두 사용할 제원이 무용지물 없어집니다. 하지만 만약 대상 크기 지수에 $p$ 척도가 상당량 클 경우, 다음 섹션 도합 구간에서 집중 논의하게 될 _전진 선택법(forward selection)_ 조율 등의 일부 통계 접근 방식을 선택 채용 사용할 수 있습니다. 이 고도 _고차원(high-dimensional)_ 통계 설정 세팅 환경 국면 테마는 통과 이후 맞이할 뒷장 챕터 6 편에서 필시 더 치밀하게 심층 조달 상세 논의될 전망입니다.e, if $H_0$ is true, there is only a 5 % chance that the $F$-statistic will result in a $p$-value below 0.05, regardless of the number of predictors or the number of observations.

일례로, 예측 투입 변수 단위 개수만 무려 $p = 100$ 개에 달하며 더구나 모든 통계 계수들이 빈틈없이 모조리 0 인 상태 즉 가설 $H_0 : \beta_1 = \beta_2 = \dots = \beta_p = 0$ 자체가 순수한 진실 참값이라고 설정해 봅시다. 이는 과연 그 어떤 다수 변수도 타깃 반응값과는 실질적 연관성이 전혀 무의미함을 뜻합니다. 하지만 이 삭막한 조건 국면에서조차 (가령 표 3.4 사례처럼 도출된) 각 개별 변수에 엮인 부수 전체 단위 $p$-값들의 약 5% 에 달하는 파편들은 오직 순전한 통계 무작위성에 기인한 요행 우연발로 인해 기준 0.05 스코어 하단 밑으로 슬쩍 파고들어 걸릴 것입니다. 다시 말해 우리는 예측 요인과 반응 지표 사이 찐한 참된 연관성이 일절 전무한 상태 하에서도 돌연 약 다섯 개의 수상쩍게 작은 $p$-값 덩어리들이 발현되는 착시를 기대해 볼 수 있습니다. 실제 실무에서는 아무 관계가 없음에도 우연으로 말미암은 0.05 미만 언더의 $p$-값을 적어도 단 한 개 이상 볼 확률 비중이 실로 굉장히 치명적으로 높은 양상입니다! 결론적으로 우리가 변수들과 타깃 반응 간 사이의 어떠한 유대가 진짜 존재하는지 안 하는지 그 분수령을 분간 결단 짓고자 여타 다른 거시 지표 없이 그저 개별 부품 단위의 쪼가리 $t$-통계량과 소속 $p$-값 조각들에게만 오롯이 맹목 의존해 판결을 단언 내린다면, 기저엔 암것도 없는 공실 데이터 속에 억지 가짜 거짓 결부 관계망이 떡하니 성립 구축되어 버렸다는 크나큰 오판 도장을 그릇되이 찍어낼 위험 확률 빈도에 아주 다분히 노출 부과됩니다. 그러나 이와는 본원적으로 대조되게 거시 관망 형태의 총 지휘 통계 지표 $F$-통계량 접근 모드는 투입된 예측 인자 요소들의 빈량 단위 개수를 인지해 합당하게 알아서 자동 튜닝 조율하므로 꼬리뼈 같은 이러한 억울한 편향 오차 판결 문제 고충 불균형 파형으로 인해 절대 고통받지 않습니다. 그러므로 만일 애당초 우리의 잣대 가설 $H_0$ 가 진짜 실재하는 퓨어한 진실 참이라면, 투입 변수의 난입 수나 추출된 관측치 총 볼륨 규모의 덩치 차이 변수 따위 얽매임과는 철저히 독립 무관하게 종합 전체 산출 검토 모형을 거친 최후 단락판 $F$-통계량이 종국엔 저 혼자 통계 수치 0.05 등급점 미만의 찌그러진 오판 $p$-값을 덜렁 초래 생성해 버릴 거짓 오판 착시 비율 빈도는 고작 단 5% 천장 확률의 통계 여유 한계 수준 범위 미만에서 굳건히 안전봉쇄 통제 차단될 뿐입니다.

The approach of using an $F$-statistic to test for any association between the predictors and the response works when $p$ is relatively small, and certainly small compared to $n$ . However, sometimes we have a very large number of variables. If $p > n$ then there are more coefficients $\beta_j$ to estimate than observations from which to estimate them. In this case we cannot even fit the multiple linear regression model using least squares, so the _F_ - statistic cannot be used, and neither can most of the other concepts that we have seen so far in this chapter. When $p$ is large, some of the approaches discussed in the next section, such as _forward selection_ , can be used. This _high-dimensional_ setting is discussed in greater detail in Chapter 6.

다중 예측 변수 부문들과 결과 타깃 반응점 사이의 상관관계 여부 꼬투리를 조사 검정 체계로 세워 파고들고자 투입되는 이 대규모 전역 검증 $F$-통계량 분석 방식 접근은, 모쪼록 파라미터 계수 요소인 $p$ 집적이 상대적으로 다소 적은 무난한 덩치를 아우르고 유지할 경우 매우 부드럽게 잘 들어맞아 작동합니다. 더불어 데이터 체급 표본 크기인 분량 조각 $n$ 과 견주어 본 상대 비교 척도면에서도 당연히 적정 숫자로 가짓수가 명확히 적을 때 꽤나 원활하게 성립 기동합니다. 그렇지만 우리의 분석 일선 전장에선 간혹 아주 막막하게 셀 수도 없이 과도하게 매우 거대한 방대한 수의 예측 투입 계수 변인들이 쓰나미처럼 덜컥 손에 주어질 때가 있습니다. 가령 최악으로 만만찮게 예측 요소인 $p > n$ 관측 표본 사이즈를 상회 돌파하는 역오버플로 기현상처럼, 척도 계수 $p$ 가 외려 표본 관측 데이터 분량 $n$ 보다 무작정 더 비대하게 웃돌아 커져 버리는 기현상 장벽 시나리오라면 상황은 사뭇 돌변합니다. 예측 추계 계수 산출에 뼈대 토대가 될 소스 기반의 한정 원천 관측치들 데이터 총합 분량 수보다도 외려 도출해 찾아 떠나야 할 정답 구적 계수 측량 수치 $\beta_j$ 잔당 분기 지표들이 더 터무니없이 무분별하게 난립 우후죽순 과잉 존재해야만 한다는 논리 모순 오류율 불가 조건의 수학 파탄 수순으로 내몰립니다. 이런 맹목적으로 무자비한 하드 스파르타의 가혹한 불능 오염 수위 난해 상황 구간에선, 기존 우리가 달달 외운 전통적인 최소 제곱 연산 접근 산식을 이용 활용하여 다중 선형 분석 회귀 모델 기본 체계를 한 땀 적합 대입 시뮬레이션 돌리려던 모든 통상적 도출 시도 과정마저 아예 본원적 도무지 불능 먹통 상태에 처참히 이르게 됩니다. 따라서 상기 거국 전역의 만능 열쇠라 칭송되던 _F_-통계량 무기 역시 이런 아수라장 판국 환경에선 단연코 사용 불가 무용지물 폐기 조각이 될뿐더러, 사실상 본 챕터 단락 한가운데 지점까지 줄곧 마르고 닳도록 우리가 내리 주의 깊게 천착 주시해 목도하며 관통해 왔던 대다수 기타 다른 주요 통계 제어 공식 여타 핵심 개념 구조 도구들조차 모조리 전부다 허공 속 무력화 마비 꼼짝 못 한 채 한낱 아무 응용의 쓸모 여지 파문조차 남기지 못한 무형의 백지상태 고철 동력이 되고 맙니다. 허지만 행여 속단하긴 이릅니다! 만일 이렇듯 예측 변수의 광활한 단위 부피 크기 $p$ 구적 척도가 어마 무시하게 드넓게 방대하고 뻥튀기될 극한 불량 경우라 할지 언정, 챕터 맥락 바로 다음 단락 페이지 분의 부문 섹션 편에서 속속들이 하나하나 정밀 해부해 세부 파헤쳐 공개 설명될 **_전진 선택법(forward selection)_** 같은 또 다른 모종의 극적 기상천외한 다차원 탈출 방안 여러 다양한 신형 대체 파생 통계 접근 타파 계단 모델링 기술 우회 수단 기법들을 긴급 처방 구호로 대거 역동원해 무리 없이 투입 접목 사용할 순 있으니 크게 절망할 사안은 지레 아닙니다. 이처럼 기묘기괴하고 까다로운 골칫거리 속성 타입의 광대 폭주형 매스컴 **_고차원(high-dimensional)_** 난해 고강도 설정 세팅 통계 척력 기조 환경 극한 체제 장벽 이슈 테마는, 통과 이후 이어질 본 교재 대망의 뒷장 챕터 6 분량 편 구역에서 기필코 한층 대폭 더 깊고 치밀하게 정밀 메스 들이밀어 상세 심층 공략 통계 분석 대토론 화제로 해부 집중 논의될 예정임을 필히 아울러 사전 통지 전언 고지하여 드립니다.

---


### Two: Deciding on Important Variables (질문 2: 중요한 변수 결정)

다수의 변수 중 반응 변수와 실제로 유의미한 관계가 있는 변수 조합들을 선택(Variable Selection)하는 방법을 배웁니다.
전진 선택법(Forward), 후진 제거법(Backward) 및 혼합 선택법의 개념을 간단히 다룹니다.

### Three: Model Fit (질문 3: 모델 적합도)

선택된 다중 회귀 모델이 주어진 훈련 데이터에 얼마나 잘 적합되었는지 다중 R² 지표 및 RSE를 통해 살펴봅니다.
변수가 추가될 때마다 R²가 증가하는 성질에 대비한 평가를 소개합니다.

### Four: Predictions (질문 4: 예측)

적합된 모델을 바탕으로 새로운 관측치에 대한 반응 변수 스코어를 예측할 때 수반되는 세 가지 큰 불확실성을 검토합니다.
신뢰 구간 및 예측 구간(Prediction Interval)의 차이를 명확히 살펴봅니다.

---

## Sub-Chapters (하위 목차)


[< 3.2.1 Estimating The Regression Coefficients](../3_2_1_estimating_the_regression_coefficients/trans1.html) | [3.2.2.1 Two Deciding On Important Variables >](3_2_2_1_two_deciding_on_important_variables/trans1.html)
