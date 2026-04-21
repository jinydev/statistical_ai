---
layout: default
title: "trans1"
---

[< 3.3.1 Qualitative Predictors](../trans1.html) | [3.3.2 Extensions Of The Linear Model >](../../3_3_2_extensions_of_the_linear_model/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Predictors with Only Two Levels



Suppose that we wish to investigate differences in credit card balance between those who own a house and those who don’t, ignoring the other variables for the moment.

당분간 여타의 다른 변수들은 덮어두고, 단지 자가를 소유한 집단과 그렇지 않은 대조군 사이의 신용카드 잔고 내역 차이를 집중적으로 심층 조사해 탐구하고자 한다고 가정해 봅시다.

If a qualitative predictor (also known as a _factor_) only has two _levels_, or possible values, then incorporating it into a regression model is very simple.

어떤 정성적 예측 변수(때로는 _요인(factor)_ 이라 불리기도 함)가 오직 두 개의 단일 _수준(levels)_ 내지는 두 가닥의 발생 가능한 값을 가지는 경우라면, 이를 통계적 회귀 모델에 합병 편입시키는 일은 정말이지 매우 간단합니다.

We simply create an indicator or _dummy variable_ that takes on two possible numerical values.[10]

우리는 통상 두 가지 방향의 지수형 숫자형 값을 자체 취하는 모종의 지표 지시자 함수나 특수 _더미 변수(dummy variable)_ 체계를 신속히 고안해 창출해 내면 그만이기 때문입니다.[10]

For example, based on the `own` variable, we can create a new variable that takes the form

variable

$$
x_i = \begin{cases}
1 & \text{if } i\text{th person owns house} \\
0 & \text{if } i\text{th person does not own house}
\end{cases}
$$

and use this variable as a predictor in the regression equation.

그리고 이렇게 손수 고안해 창출한 특수 변수를 회귀 방정식 체제 하의 예측 인자로 사용합니다.

This results in the model

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i = \begin{cases}
\beta_0 + \beta_1 + \epsilon_i & \text{if } i\text{th person owns house} \\
\beta_0 + \epsilon_i & \text{if } i\text{th person does not own house}
\end{cases} \quad (3.27)
$$

Now \beta_0 can be interpreted as the average credit card balance among those who do not own, \beta_0 + \beta_1 as the average credit card balance among those who do own their house, and \beta_1 as the average difference in credit card balance between owners and non-owners.

Table 3.7 displays the coefficient estimates and other information associated with the model (3.27).

표 3.7 은 모델 체계 (3.27) 에 관련된 계수 추정치 및 여타 종류의 여분 정보 사항들을 직접적으로 알기 쉽도록 나타냅니다.

The average credit card debt for non-owners is estimated to be $\$509.80$, whereas owners are estimated to carry $\$19.73$ in additional debt for a total of $\$509.80 + \$19.73 = \$529.53$.

주택 미보유 계층군의 평균 집계 신용카드 부채 액수 단락은 대략 $\$509.80$ 로 추산되는 반면, 실제 유주택자층 소유 대상자들은 저마다 개별적으로 총계 비용 $\$509.80 + \$19.73 = \$529.53$ 수위에 육박하는, 다시 말해 무주택자에 비해 대략 $\$19.73$ 만큼의 채무를 평균치 구도로 더 부담하는 것으로 간주됩니다.

However, we

> [10] In the machine learning community, the creation of dummy variables to handle qualitative predictors is known as "one-hot encoding".

> [10] 기계 학습(machine learning) 관련 학계 내에서 이처럼 특정 정성적 구도 속성을 띤 예측 변수를 포섭하고 취급하고자 의도적으로 더미 변수 단위를 창출하는 제반 행위를 가리켜 통상 "원-핫 인코딩(one-hot encoding)" 이라 명명해 지칭합니다.

**==> picture [300 x 300] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 40 60 80 100 5 10 15 20 2000 8000 14000<br>Balance<br>Age<br>Cards<br>Education<br>Income<br>Limit<br>Rating<br>0 500 1500 2 4 6 8 50 100 150 200 600 1000<br>1500<br>500<br>0<br>100<br>80<br>60<br>40<br>20<br>8<br>6<br>4<br>2<br>20<br>15<br>10<br>5<br>150<br>100<br>50<br>14000<br>8000<br>2000<br>1000<br>600<br>200<br>**----- End of picture text -----**<br>


**FIGURE 3.6.** _The_ `Credit` _data set contains information about_ `balance` _,_ `age` _,_ `cards` _,_ `education` _,_ `income` _,_ `limit` _, and_ `rating` _for a number of potential customers._

notice that the $p$-value for the dummy variable is very high. This indicates that there is no statistical evidence of a difference in average credit card balance based on house ownership.
그런데 막상 더미 변수 척도에 해당하는 그 $p$-값은 매우 크다는 단편적 사실을 발견하게 됩니다. 이는 결국 자가 주택 소유 여부 판별에 따른 모종의 평균 신용카드 잔고 지표 간에 그 어떤 뚜렷한 실제 격차도 사실상 통계적으로 존재하지 않는다는 증거 부족의 실상을 시사합니다.

The decision to code owners as $1$ and non-owners as $0$ in (3.27) is arbitrary, and has no effect on the regression fit, but does alter the interpretation of the coefficients.
(3.27) 식 상에서 자택 소유자를 $1$ 로, 미소유자 군을 각각 $0$ 으로 암호 체계 부호화하여 할당한다는 식의 단순 결정 자체는 어디까지나 다분히 임의적이며, 그 때문에 이것이 회귀 적합 구성 전반에 미치는 실제 파급 효과란 사실상 아예 없지만 제반 계수의 통계적 의미를 풀이하는 체제 부분 관점에서는 다소 유의미한 해석 변동을 불러일으킬 뿐입니다.

If we had coded non-owners as $1$ and owners as $0$, then the estimates for $\beta_0$ and $\beta_1$ would have been $529.53$ and $-19.73$, respectively, leading once again to a prediction of credit card debt of $\$529.53 - \$19.73 = \$509.80$ for non-owners and a prediction of $\$529.53$ for owners.
만일 처음부터 우리가 반대로 주택 미보유층 집단 부호를 $1$ 로 지정하고 실소유주를 $0$ 부호로 코드화했더라면, 각각의 $\beta_0$ 와 $\beta_1$ 모수 추산치 단위값 구성은 지금과는 다른 별개의 $529.53$ 과 $-19.73$ 이 됨으로써, 결과론적으로 보아 다시 또 동일하게 주택 미소유자의 신용카드 부채 채무액 규모 추정치는 $\$529.53 - \$19.73 = \$509.80$ 이 될 테고 자가 보유층 집단이 갖게 될 예측치는 고스란히 예전 그대로의 형상인 $\$529.53$ 이 전개 도출될 것입니다.

Alternatively, instead of a $0 / 1$ coding scheme, we could create a dummy variable

$$
x_i = \begin{cases}
1 & \text{if } i\text{th person owns house} \\
-1 & \text{if } i\text{th person does not own house}
\end{cases}
$$

and use this variable in the regression equation.
그리고 이렇게 형성한 허구의 더미 변수 모델을 고스란히 회귀 방정식 구절로 채택하여 이용할 수도 있습니다.

This results in the model

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i = \begin{cases}
\beta_0 + \beta_1 + \epsilon_i & \text{if } i\text{th person owns house} \\
\beta_0 - \beta_1 + \epsilon_i & \text{if } i\text{th person does not own house}
\end{cases} \quad (3.28)
$$

3.3 Other Considerations in the Regression Model 93

|3.3 Other Considerations in the Regression Model|3.3 Other Considerations in the Regression Model|
|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>`own[Yes]`|509.80<br>33.13<br>15.389<br>_<_0_._0001<br>19.73<br>46.05<br>0.429<br>0.6690|



**TABLE 3.7.** _Least squares coefficient estimates associated with the regression of_ `balance` _onto_ `own` _in the_ `Credit` _data set. The linear model is given in (3.27). That is, ownership is encoded as a dummy variable, as in (3.26)._

Now $\beta_0$ can be interpreted as the overall average credit card balance (ignoring the house ownership effect), and $\beta_1$ is the amount by which house owners and non-owners have credit card balances that are above and below the average, respectively.[11]
이제 이 구도상 모수 $\beta_0$ 속성은 아예 주택의 실질 소유 유무별 부가 요인 후광 파급력을 배제 통제하고 간과한 채 지극히 포괄적인 형식의 전체적인 범주를 대변하여 나타내는 통계상 전반적 평균치 신용 잔고 자산 규모라 일일이 이해될 수 있으며, 그에 맞붙은 옆 부분 $\beta_1$ 은 주택 실소유자군 대조 패널과 또 미보유 계층별 집단들 각각의 총 신용 자산 잔금이 방금 언급한 그 포괄적 평균 기준 대비 실제 어느 수준만큼 위아래로 얹혀 오르내리는지 차감 액수 수준의 간격을 드러내는 구도 물량입니다.[11]

In this example, the estimate for $\beta_0$ is $\$519.665$, halfway between the non-owner and owner averages of $\$509.80$ and $\$529.53$.
이 사례 모델 형식상 $\beta_0$ 추정치는 거진 $\$519.665$ 정도로 도출되는데, 정확하게 이 값은 주택 미소유자의 평균대인 $\$509.80$ 와 보유군 평균 지표인 $\$529.53$ 그 두 극단의 한복판 정중앙치 구심점에 귀결되어 안착합니다.

The estimate for $\beta_1$ is $\$9.865$, which is half of $\$19.73$, the average difference between owners and non-owners.
또한 추가로 덧붙여 $\beta_1$ 항의 관련 모수 추정치 역시 어림잡아 $\$9.865$ 정도로 나타나는데, 이는 두 양단 집단 소유군 및 미소유자층 간의 실제 전체 평균 격차 척도로 관측된 액수 $\$19.73$ 량의 정확히 절반을 뚝 잘라 양분한 반토막 조각 치수와 판에 박은 듯 상동한 수준 액수 지표입니다.

It is important to note that the final predictions for the credit balances of owners and non-owners will be identical regardless of the coding scheme used.
여기서 우리가 놓치지 않고 눈여겨 주의 깊게 살펴 기약해야 할 주안점 특이 사항은, 궁극적으로 자택 보유 여력별 소유군 및 무소유 계층 각각 개체를 조준하여 실체가 도출된 끝맺음 귀결 예측 결과치 신용 잔고 산출 물량이 애초 사용자가 어떤 식으로 앞선 부호 인코딩 체계 척도를 차용해 지정 조작했건 상관하지 않고 끝에는 매양 동등하게 획일적 동일 양태 결과 치수로 전방위 수렴된다는 불변적 사실입니다.

The only difference is in the way that the coefficients are interpreted.
결국 발생하게 되는 이견 차이란 단지 개별 계수 요인 하나하나가 통계 관점으로 의미 도출 풀이 적용 및 해석 처리되는 세세한 방법론 그 체계 관점 노선 하나뿐이기 때문입니다.

Qualitative Predictors with More than Two Levels

When a qualitative predictor has more than two levels, a single dummy variable cannot represent all possible values.
만약 모종의 정성적인 예측 변수가 포섭해 지닌 등급 수준(levels) 값이 단순히 2개를 초과하여 형성된 다분화 구조일 경우라면, 일명 단일한 속성의 더미 변수 구조 체계 딱 하나만 가지고서는 현실적으로 이 모든 발생 가망 가능한 복잡 범주 지표 값을 다 망라할 수는 없습니다.

In this situation, we can create additional dummy variables.
바로 이러한 경우, 우리는 얼마든지 몇 배구 추가 여건 부수 더미 변수 부품 조각들을 거뜬히 잇달아 고안해 생성해 내면 그뿐입니다.

For example, for the `region` variable we create two dummy variables. The first could be
예컨대, 특정 구역 지표군을 관통해 가르지르는 `region(지역)` 예측 변수가 있다 치면, 당분간 우리는 이를 위해 가상의 더미 변수 표본 둘을 즉시 창안 축조해 둘 수 있습니다. 그중 첫 번째 변수 체제 형태는 필경 아래와 같을 것입니다.

**==> picture [268 x 31] intentionally omitted <==**

and the second could be
그리고 두 번째의 경우 이내 다음과 같은 형식 형체가 될 수 있을 것입니다.

**==> picture [267 x 31] intentionally omitted <==**

Then both of these variables can be used in the regression equation, in order to obtain the model
이후 이렇게 도출 준비된 이 두 여건 부수 변수 항목 전부를 한데 나란히 선형 체계 회귀 방정식 문맥 속에 묶어 투사 응용 활용할 수 있으며, 이내 그 수고 결과물로 차기 적합 모델 모형을 아래 구도로 온전히 취득하게 됩니다.

**==> picture [294 x 39] intentionally omitted <==**

(3.30)

Now $\beta_0$ can be interpreted as the average credit card balance for individuals from the East, $\beta_1$ can be interpreted as the difference in the average balance between people from the South versus the East, and $\beta_2$ can be interpreted as the difference in the average balance between those from the West versus the East.
이제 막 생성 적합 완료된 새 모형 전개 구조 내에서 거론된 중심 모수 $\beta_0$ 의미는 오로지 특정 지역권인 동부(East) 출신에 호적 영토를 두고 머무는 개별 표본 집단 체계의 전박적인 평균 보유율 신용카드 적립 잔고액 규모 단편 수준치로 꽤 명맥하게 풀이해 석명될 수 있고, $\beta_1$ 단락의 경우는 기실 동부(East)권 토박이 거주 층 대비 남부(South) 지역 체계 출신자 그룹의 평균 자산 잔고 수준이 상호 어느 일정 간극만큼 벌어져 있는지 양자 간 상충 격차 그 자체 지표를 꽤 투명히 가리킨 것으로 관점 해석되며, 끝으로 남은 항 $\beta_2$ 체계 또한 마찬가지 관점에서 남부 대신 서부(West) 거주 계층이 동부권 토박이들 대비 실제 벌려 양산해 내는 평균 잔고치 상대 전용 이견 격차 지수 폭으로 가시 분간해 풀이해 판단지을 수 있습니다.

There will always be one fewer dummy variable than the number of levels.
여기서 또 하나 눈겨겨볼 절대 규칙 중 진리 하나로 꼽자면 상시 구조적으로 투여될 전체의 가상 더미 변수 투입 개수 지표는 기저 태생부터 이미 변수가 거느릴 세부 특정 등급(levels) 구분 기준 총체적 범주 가짓수 부피에서 매번 매양 언제나 적확히 딱 '1' 이란 수치 만큼만 상시 체감 차감해 공제된 단편적 개수 비율로 제한 구성된다는 사실성입니다.

The level with no dummy variable — East in this example — is known as the __.
이렇듯 해당 사례 모델 구상 안에서 별반 여벌 더미 구도 변수를 고유로 따로 소유하지조차 않고 동떨어져 혼자 남겨진 저 외로운 속성의 동부(East) 거점 지역과 같은 해당 무소속 등급 수준 잣대를 통계상 일명 특정 기초 기준점 요소라는 의미 차원의 _기준선()_ 범주라 칭합니다.

> [11] Technically $\beta_0$ is half the sum of the average debt for house owners and the average debt for non-house owners. Hence, $\beta_0$ is exactly equal to the overall average only if the two groups have an equal number of members.
> [11] 기술적인 맥락 측면상 기저 $\beta_0$ 지표 수치는 앞서 다룬 자가 보유 주택 여력자 층의 평균 채무 단위와 반대되는 미보유 층 전체의 평균 부채 지표 총합산 값을 반절로 등분 나눈 값입니다. 그렇기에 해당 부문 $\beta_0$ 치수는 필연적으로 그 두 대조군 속성 그룹 양쪽 개체 지표 구성원 인원 숫자 비율 규모가 둘 다 완벽할 만치 철두철미 상호 동일한 극히 제약 균등 상태인 경우라는 일정한 제한 조건에서만 본디 오리지널 전체 획일적 포괄 평균 수치 단락에 정확무오하게 곧이 일치 귀결하여 떨어집니다.



94 3. Linear Regression


|---|---|
|||
||Coefcient<br>Std. error<br>_t_-statistic<br>p-value|
|`Intercept`<br>`region[South]`<br>`region[West]`|531.00<br>46.32<br>11.464<br>_<_0_._0001<br>_−_12.50<br>56.68<br>_−_0.221<br>0.8260<br>_−_18.69<br>65.02<br>_−_0.287<br>0.7740|



**TABLE 3.8.** _Least squares coefficient estimates associated with the regression of_ `balance` _onto_ `region` _in the_ `Credit` _data set. The linear model is given in (3.30). That is, region is encoded via two dummy variables (3.28) and (3.29)._

From Table 3.8, we see that the estimated `balance` for the , East, is $531 _._ 00. It is estimated that those in the South will have $18 _._ 69 less debt than those in the East, and that those in the West will have $12 _._ 50 less debt than those in the East. However, the $p$-values associated with the coefficient estimates for the two dummy variables are very large, suggesting no statistical evidence of a real difference in average credit card balance between South and East or between West and East.[12] Once again, the level selected as the  category is arbitrary, and the final predictions for each group will be the same regardless of this choice. However, the coefficients and their $p$-values do depend on the choice of dummy variable coding. Rather than rely on the individual coefficients, we can use an _F_ -test to test $H_0$ : \beta_1 = \beta_2 = 0; this does not depend on the coding. This _F_ -test has a $p$-value of 0 _._ 96, indicating that we cannot reject the null hypothesis that there is no relationship between `balance` and `region` .

Using this dummy variable approach presents no difficulties when incorporating both quantitative and qualitative predictors.
결과적으로 보건대, 이런 류의 더미 변수 채택 접근법 요소를 가미 활용 구사하는 작업 행위 자체는 여타 지성적 정량 형태의 예측 요인과 또 여타의 단면인 다른 한 축 정성적 속성의 예측 변수, 즉 서로 무척 판이하게 이질적인 양단 체계 둘을 교묘히 배합 상호 통합 절차 도모를 진행 구상하는 와중에서도 그리 딱히 애로 사항이나 어려움이란 문제 장애를 전혀 발현 야기시키지 않습니다.

For example, to regress `balance` on both a quantitative variable such as `income` and a qualitative variable such as `student`, we must simply create a dummy variable for `student` and then fit a multiple regression model using `income` and the dummy variable as predictors for credit card balance.
가령 그 한 예로, 정량 측정 단위 성향을 지닌 특정 `income` 물량 요소와 성격 측면이 전혀 대조되는 특수 정성 변수인 그 무어랄 것 없는 여타 요소 계열 `student` 분류 매개, 이들 둘 모두의 복합 쌍둥이 양대 자격 축을 구심 기반 기점으로 삼아 타깃 관할 지표 `balance` 요소가 걸친 방향성 각도로 한껏 기울여 통계 회귀 시키려 할 적엔, 그저 단순히 우리 쪽에서 우선 선 조치상 애당초 일찌감치 특정 `student` 파트 부분을 위해 무던히 더미 변수 틀 단면부터 재차 가볍게 가미 축조 조형시켜낸 뒤, 뒤이어 저마다 신용카드 실잔고 분별 예측 대상 후보 선상 표본 자격을 등에 업은 각 `income` 및 더미 변수 두 파트를 함께 써 다중 회귀 모델 모임 굿판에 제법 그럴싸하게 기계적 적합 투사시켜버리기만 하면 그 모든 수순 작업이 온전히 종결됩니다.

There are many different ways of coding qualitative variables besides the dummy variable approach taken here.
지금 당장 여기 단락서 우리 앞선 방식 기로상 쭉 전취 채택해 전개 진행했던 더미 변용 관련 인코딩 축조 접근 수법 요령안 이외에도 여럿 타 부가 형태의 무수한 세부 인코딩 부호 적용 수립 전개형 접근법 방식이 무성히 참 다채롭고 방대하게 더 많이 마련되어 있습니다.

All of these approaches lead to equivalent model fits, but the coefficients are different and have different interpretations, and are designed to measure particular _contrasts_.
허나 이 무수히 다른 형국 접근 갈래 기선 체재 방식들은 하나같이 매양 기저 결론 산출 관점에선 최종 종착지에 동등한 유사 수준 적합 모형 궤적 치수를 똑같이 보란 듯 야기 인도해 내려줄 뿐, 정작 개별 계수만큼은 외관 속성상 완전히 판이 다른 상이한 체제를 시현 잉태 야기하며 덩달아 도무지 닮지 않은 숱한 해석 논쟁 거리를 불러일으키곤 할 뿐더러 실은 그런 다수 관습적 행위 방식 전부가 다름 아닌 모종 수준 일각 단위 체계상 다소 여유 특이한 성현 기반 부문 관할 특정 _대조군(contrasts)_ 요인 구도를 예의 실측 계량 타점 삼기 위한 특정 복적 설계를 띠곤 합니다.

This topic is beyond the scope of the book.
물론 이 특유 부문의 대조 관련 세분화 주제 이슈 요소는 당초 본 서적 교재가 본디 목표 타협 기반 기조로 설정했던 다루기 지정 허용 주제 범위 수준 한계 척도를 한참 훌쩍 벗어나 넘어선 지대이므로 그 선망 도를 넘기게 됩니다.

---

## Sub-Chapters (하위 목차)


[< 3.3.1 Qualitative Predictors](../trans1.html) | [3.3.2 Extensions Of The Linear Model >](../../3_3_2_extensions_of_the_linear_model/trans1.html)
