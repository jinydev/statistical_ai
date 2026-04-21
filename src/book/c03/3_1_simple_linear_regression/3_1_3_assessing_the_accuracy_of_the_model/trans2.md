---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.1.2 Assessing the Accuracy of the Coefficient Estimates](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans2.html) | [3.2 Multiple Linear Regression >](../../3_2_multiple_linear_regression/trans2.html)

# 3.1.3 Assessing the Accuracy of the Model

# 3.1.3 모델의 정확도 평가 (우리 식당의 임시 매출 예측기, 성적표 받는 날!)

Once we have rejected the null hypothesis (3.12) in favor of the alternative hypothesis (3.13), it is natural to want to quantify _the extent to which the model fits the data_. The quality of a linear regression fit is typically assessed using two related quantities: the _residual standard error_ (RSE) and the $R^2$ statistic.
만약 우리가 통계 법정에서 지루한 '무의미하다'는 주장(귀무가설)을 기각하고 인공지능 모델이 찾아낸 '의미 있다'는 주장(대립가설)을 승소로 이끌어 냈다면, 이제 궁금해지는 건 "그래서 이 녀석의 실력이 도대체 몇 점짜리인데?" 하고 _우리 모델이 데이터의 진실에 얼마나 찰떡처럼 맞아떨어지는지_ 를 성적표 수치로 매겨보고 싶을 겁니다. 우리가 억지로 그어놓은 선형 회귀 직선의 품질(퀄리티)을 채점할 때, 통계학의 세계에서는 보통 **잔차 표준 오차(Residual Standard Error, RSE)** 선생님과 **$R^2$(설명력 점수)** 선생님이라는 두 분의 까다로운 면접관을 모셔옵니다.

> $^4$ In Table 3.1, a small $p$-value for the intercept indicates that we can reject the null hypothesis that $\beta_0 = 0$, and a small $p$-value for `TV` indicates that we can reject the null hypothesis that $\beta_1 = 0$. Rejecting the latter null hypothesis allows us to conclude that there is a relationship between `TV` and `sales`. Rejecting the former allows us to conclude that in the absence of `TV` expenditure, `sales` are non-zero.
> $^4$ 표 3.1에서 절편이 받은 쥐꼬리만 한 $p$-값 성적은 "기본 매출 따윈 없어($\beta_0=0$)" 라는 우울한 귀무가설의 어리광을 기각할 수 있다는 증거이며, `TV` 항목의 작은 $p$-값은 "TV 광고 해봤자 돈 낭비야($\beta_1=0$)" 라는 꼰대 같은 귀무가설을 시원하게 후려칠 수 있다는 선언입니다. 후자(TV)의 헛소리를 기각함으로써 우리는 "광고비를 태우면 분명 매상이 오르는 관계가 있다!"고 확신할 수 있고, 전자(절편)를 기각함으로써 "설령 이번 달 광고를 하나도 안 때리더라도 기특하게도 기본 매상($\beta_0$)은 쏠쏠하게 찍힌다"는 달콤한 결론을 내릴 수 있습니다.

| Quantity | Value |
| :--- | :--- |
| Residual standard error | 3.26 |
| $R^2$ | 0.612 |
| $F$-statistic | 312.1 |

**TABLE 3.2.** _For the_ `Advertising` _data, more information about the least squares model for the regression of number of units sold on TV advertising budget._
**TABLE 3.2.** `Advertising` _데이터를 기반으로, TV 광고비(X) 투입 대비 얼마나 많은 제품이 팔려나갔는지(Y) 최소 제곱법으로 구워낸 모델의 최종 성적표(추가 스펙 정보)입니다._

Table 3.2 displays the RSE, the $R^2$ statistic, and the $F$-statistic (to be described in Section 3.2.2) for the linear regression of number of units sold on TV advertising budget.
표 3.2는 우리가 만든 'TV 광고비에 따른 제품 단위 판매량' 예측 선형 회귀 모델이 받아든 최종 등급표로서, RSE 와 $R^2$ 통계수치, 그리고 훗날 3.2.2절에서 다룰 무시무시한 군단장 격인 $F$-통계량 수치를 박제해 보여주고 있습니다.

## Residual Standard Error

## 잔차 표준 오차 (RSE: 과녁을 얼마나 빗나갔는지 재는 줄자)

Recall from the model (3.5) that associated with each observation is an error term $\epsilon$. Due to the presence of these error terms, even if we knew the true regression line (i.e. even if $\beta_0$ and $\beta_1$ were known), we would not be able to perfectly predict $Y$ from $X$. The RSE is an estimate of the standard deviation of $\epsilon$. Roughly speaking, it is the average amount that the response will deviate from the true regression line. It is computed using the formula
이전 (3.5) 공식에서 모든 데이터 점들 옆에는 항상 불완전한 소음 찌꺼기인 오차 항 $\epsilon$(입실론) 요정들이 더덕더덕 붙어있었다는 사실을 기억하시나요? 현실 세계에 만연한 이 짓궂은 오차 요정들의 농간 때문에, 만약 신이 강림하여 우주의 진리인 진짜 회귀선($\beta_0$와 $\beta_1$의 정답)을 우리 귀에 속삭여 준다 한들, 애초에 $X$ 힌트만으로 $Y$ 값을 오차 0.0001도 없이 신들린 듯 완벽히 예언하는 것은 물리적으로 불가능합니다! RSE(잔차 표준 오차)는 바로 이 불규칙하게 퍼진 요정($\epsilon$)들이 얼마나 요란하게 날뛰는지 그 분포(표준 편차)를 간접적으로 짐작해본 수치표입니다. 아주 무식하고 직관적으로 퉁쳐서 비유하자면, 모델 예측값 과녁의 화살들이 진짜 정답 십자선에서 벗어나 **평균적으로 빗나가는 거리의 오차 단위량**을 의미하며, 이는 다음과 같은 통계 공식 체인소로 계산됩니다.

$$
\text{RSE} = \sqrt{\frac{1}{n-2}\text{RSS}} = \sqrt{\frac{1}{n-2}\sum_{i=1}^n(y_i-\hat{y}_i)^2} \quad (3.15)
$$

Note that RSS was defined in Section 3.1.1, and is given by the formula
여기서 괄호 안의 심장이 되는 RSS 파트는 이미 3.1.1 단원에서 우리가 지독하게 줄이려고 애썼던 찌꺼기들의 제곱합 덩어리이며, 공식은 이랬습니다.

$$
\text{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 \quad (3.16)
$$

In the case of the advertising data, we see from the linear regression output in Table 3.2 that the RSE is 3.26. In other words, actual sales in each market deviate from the true regression line by approximately 3,260 units, on average. Another way to think about this is that even if the model were correct and the true values of the unknown coefficients $\beta_0$ and $\beta_1$ were known exactly, any prediction of sales on the basis of TV advertising would still be off by about 3,260 units on average. Of course, whether or not 3,260 units is an acceptable prediction error depends on the problem context. In the advertising data set, the mean value of `sales` over all markets is approximately 14,000 units, and so the percentage error is $3,260 / 14,000 = 23\%$.
우리의 귀여운 장부 데이터 예제로 돌아와서, 아까 본 표 3.2 성적표를 슬쩍 커닝해 보면 RSE 오차 덩어리가 3.26으로 큼지막하게 쓰여있습니다. 곱백을 해보면, 각각의 지역 동네 시장에서 실제로 팔아 치운 매출 물량은 "신의 정답 선" 기준에서조차 평균적으로 대략 3,260 박스 정도가 엇나가고 있다는 쓰라린 뜻입니다. 이 절망적인 상황을 조금 더 비참하게 상상해 보자면, "아무리 우리 AI 뇌가 정밀하고 신의 절대 진리 무기($\beta_0, \beta_1$)를 탑재했다고 자만하더라도, TV 변수만 갖고서 매출을 읊어대면 여전히 한 번 찍을 때마다 매번 3,260개씩은 얼버무리며 틀려먹을 운명이다!"라는 뜻입니다. 물론, 3,260개라는 헛스윙이 "아 뭐 그럴 수도 있지" 하고 사장님이 용서해 줄 오차일지, 아니면 당장 "잘라버려!" 할 재앙일지는 파는 물건에 따라 다릅니다. 이 예제의 경우 전체 동네의 평균 매출이 14,000개 정도니까, 이걸 백분율 에러로 때려보면 $3,260 / 14,000 = 23\%$ 의 허점이 구멍으로 뚫려있다는 결론이 나옵니다.

The RSE is considered a measure of the _lack of fit_ of the model (3.5) to the data. If the predictions obtained using the model are very close to the true outcome values—that is, if $y_i \approx \hat{y}_i$ for $i = 1, \dots, n$—then (3.15) will be small, and we can conclude that the model fits the data very well. On the other hand, if $\hat{y}_i$ is very far from $y_i$ for one or more observations, then the RSE may be quite large, indicating that the model doesn’t fit the data well.
그래서 사람들은 এই RSE 점수를 가리켜 우리 장난감 모델이 실제 세계 도화지에 얼마나 **헛돌고 안 맞는지(_적합 결여도 lack of fit_)**를 보여주는 고발장으로 씁니다. 만약 모델이 찍은 정답 예측(알파고 수)이 진짜 성적표인 관측치랑 소름 돋게 들어맞아 소수점까지 찰떡($y_i \approx \hat{y}_i$)이라면, 공식 3.15 덩어리 값은 0에 수렴할 것이고 우린 "야! 이거 데이터랑 미친 듯이 쫙쫙 달라붙네!" 하고 찬양할 수 있습니다. 반면에 우리 알바생 모델($\hat{y}_i$)이 부른 숫자가 사장님 금고($y_i$) 랑 하나둘 기하급수적으로 차이가 벌어져 버리면 RSE 에러 값은 하늘을 뚫고 치솟으며 "이 쓰레기 모델 당장 폐기해, 현실이랑 1도 안 맞아!" 라는 불호령을 내리게 됩니다.

## $R^2$ Statistic

## $R^2$ 통계량 (결정 계수: 내 힌트가 우주를 설명하는 지분율)

The RSE provides an absolute measure of lack of fit of the model (3.5) to the data. But since it is measured in the units of $Y$, it is not always clear what constitutes a good RSE. The $R^2$ statistic provides an alternative measure of fit. It takes the form of a _proportion_—the proportion of variance explained—and so it always takes on a value between 0 and 1, and is independent of the scale of $Y$.
RSE 수치는 앞서 말했듯 모델이 얼마나 빗나가는지를 가리키는 '절대 거리 단위'의 적합 결도 척도입니다. 하지만 애꿎게도 이 녀석의 체급(단위)은 항상 타겟 뱃살($Y$) 무게를 기어이 따라가다 보니, RSE가 가령 50이라는 숫자가 떴을 때 이게 훌륭한 건지 완전 망한 건지 한눈에 감별하기가 여간 까다로운 게 아닙니다. 이때 혜성처럼 나타나는 구원 투수가 바로 **$R^2$(설명력 점수)** 통계량입니다! 이 친절한 녀석은 "자, 전체 혼돈 중에 내가 멱살 잡고 캐리한 분산(변동성)의 _비율(퍼센트 지분)_ 이 몇 프로나 되냐면~" 하는 지분 증서 형태를 취하기 때문에, 무조건 깔끔하게 **0(0%) ~ 1(100%)** 사이의 아름답게 코팅된 숫자만을 돌려주며, 결과적으로 타겟 과녁 $Y$ 가 달러든 파운드든 원화 단위든 그 치사한 스케일 장난질에 눈을 깜짝하지 않고 독립적입니다!

To calculate $R^2$, we use the formula
자, 이 심플하고 멋진 비율 지분표인 $R^2$ 를 매기는 공식은 다음과 같습니다.

$$
R^2 = \frac{\text{TSS} - \text{RSS}}{\text{TSS}} = 1 - \frac{\text{RSS}}{\text{TSS}} \quad (3.17)
$$

where $\text{TSS} = \sum (y_i - \bar{y})^2$ is the _total sum of squares_, and $\text{RSS}$ is defined in (3.16). $\text{TSS}$ measures the total variance in the response $Y$, and can be thought of as the amount of variability inherent in the response before the regression is performed. In contrast, $\text{RSS}$ measures the amount of variability that is left unexplained after performing the regression. Hence, $\text{TSS} - \text{RSS}$ measures the amount of variability in the response that is explained (or removed) by performing the regression, and $R^2$ measures the _proportion of variability in $Y$ that can be explained using $X$_. An $R^2$ statistic that is close to 1 indicates that a large proportion of the variability in the response is explained by the regression. A number near 0 indicates that the regression does not explain much of the variability in the response; this might occur because the linear model is wrong, or the error variance $\sigma^2$ is high, or both. In Table 3.2, the $R^2$ was 0.61, and so just under two-thirds of the variability in `sales` is explained by a linear regression on `TV`.
이 신비의 공식 속 분모인 $\text{TSS} = \sum (y_i - \bar{y})^2$ 는 고상한 말로 _총 제곱합(Total Sum of Squares)_ 이라고 부릅니다. 아주 쉽게 말하면, 우리가 어떤 예측 짓거리도 시작하기 전 백지상태에서 측정해 본 "원래 타겟 $Y$ 의 널뛰기하는 총 혼돈(분산)의 양" 입니다. 그리고 $\text{RSS}$ 는 아까 죽어라 계산했던 "직선을 긋고 어쩌고 난리를 다 쳤음에도 기어이 설명 못 하고 구질구질하게 남아버린 찌꺼기 널뛰기 양"이죠. 
그렇다면 $\text{TSS}$ 에서 이 쓰레기 $\text{RSS}$ 를 무자비하게 빼버린 분자($\text{TSS} - \text{RSS}$)의 정체는? 바로 "내가 회귀 모델을 영리하게 때려 맞혀서 완벽하게 제거하고 설명해 낸 순수한 예측 성공 업적" 이 됩니다! 따라서 $R^2$ 파이 조각은 **"전체 타겟 $Y$ 가 미친 듯이 오르락내리락하는 이유 중에 도대체 내 힌트 $X$ 덕분이라고 설명할 수 있는 지분(비율)이 얼마나 되는가?"** 를 아주 정확히 콕 집어 계산해 냅니다. 이 $R^2$ 성적표가 만점인 1에 가깝게 찍혔다면, 타겟이 이리저리 요동치는 현상의 막대한 원인을 내 모델 하나가 기가 막히게 다 헐뜯어 설명해 내고 있다는 영광의 훈장입니다. 하지만 이 숫자가 바닥인 0 근처에서 구르고 있다면, 안타깝게도 내 예측이 똥 촉(선형 제약 모델이 아예 틀렸거나)이거나, 아니면 원래 세상만사가 오차 변동성($\sigma^2$)으로 뒤범벅된 카오스이거나 두 가지 참사 중 하나겠죠. 방금 전 표 3.2를 슬며시 보면, 우리 $R^2$ 점수는 0.61이었습니다. 즉 `sales(매출)`이 오르락내리락하는 우주의 미스터리 중 **무려 약 $3분의 2$(약 61%) 가량의 원인 지분이 철저하게 내가 뿌린 다이아몬드 지분 `TV(광고)` 변동 하나 덕분** 임을 위풍당당하게 설명해 내는 겁니다!

The $R^2$ statistic (3.17) has an interpretational advantage over the RSE (3.15), since unlike the RSE, it always lies between 0 and 1. However, it can still be challenging to determine what is a _good $R^2$_ value, and in general, this will depend on the application. For instance, in certain problems in physics, we may know that the data truly comes from a linear model with a small residual error. In this case, we would expect to see an $R^2$ value that is extremely close to 1, and a substantially smaller $R^2$ value might indicate a serious problem with the experiment in which the data were generated. On the other hand, in typical applications in biology, psychology, marketing, and other domains, the linear model (3.5) is at best an extremely rough approximation to the data, and residual errors due to other unmeasured factors are often very large. In this setting, we would expect only a very small proportion of the variance in the response to be explained by the predictor, and an $R^2$ value well below 0.1 might be more realistic!
물론 100점 만점 시험지처럼 항상 0.0과 1.0(0% ~ 100%) 사이에 예쁘게 코팅되어 나오는 이 지분 지표 $R^2$ 점수는 그 지독하고 스케일 자비 없는 RSE 거대 단위 수치보다는 훠어얼~씬 이해관계자들의 마음을 편안하고 해석하기 우월하게 이끌어줍니다. 허나 방심은 금물! 도대체 $R^2$ 값이 얼마나 찍혀야 사장님께 결재받고 "성공적인 프로젝트입니다!" 라 할 든든한 _착한 등급선_ 인지에 대한 기준을 명확하게 딱 자르기는 무진장 곤란합니다. 분야마다 눈높이가 하늘과 땅 차이거든요! 예를 한 번 볼까요? 고정밀 계기판을 깎아 쓰는 순수 이학 물리학 세계에선 원래 질량 보존처럼 숨 쉬듯 딱 떨어지는 100% 진리 정답이 예측되는 동네라, $R^2$ 점수가 0.99 1.0 에 무진장 육박하며 바짝 들러붙어야 정상 궤도라 취급받고 오히려 $R^2$ 점수가 미달 나면 실험실 대학원생이 엉뚱한 노이즈 폭탄 데이터를 만들어 냈다고 싸울지도 모릅니다. 반면에 이와 정반대인 생물, 생태 자연현상, 혹은 심리학이나 깐깐하기 그지없는 소비재 마케팅 실무 도메인 바닥에서는 어떨까요? 인간의 복잡한 뇌구조나 날씨처럼 도무지 우리 직각 냄비 선형 (3.5) 무기가 극히 허술하고 매우 난립한 조잡한 수준의 요행 같은 추정일 경우가 비일비재하며, 미처 우리가 알지도 채 못하는 또 다른 엄청난 돌발 요인 변수들 탓에 발생하는 무지막지한 덩어리 잔류 오차 벽이 그저 태산만 하게 앞을 압도하곤 합니다. 이런 살벌한 실전 야생 환경 속이라면, 솔직히 우리 조잡한 변수 힌트 몇 개 따위가 타겟의 방대한 변량을 뜯어먹고 설명할 비율 지분 자리가 겨우 한 줌의 소량이길 그저 염원하고 기대해야 하며, 진짜 **$R^2$ 수치가 0.1(고작 10% 지분 파이) 밑으로 처참히 곤두박질치는 것이 외려 눈물 나게 현실적인 현주소** 일지도 모른다는 뜻입니다!

The $R^2$ statistic is a measure of the linear relationship between $X$ and $Y$. Recall that _correlation_, defined as
방금 배운 $R^2$ 점수 채점표 녀석은 사실 따지고 보면 $X$ 와 $Y$ 둘이 얼마나 쿵짝쿵짝 일직선 성향으로 발을 맞춰 걷는지를 캐내는 직선 로맨스 지수라 볼 수 있습니다. 혹시 고등학교 때 둘의 짝짜꿍 끈끈함을 수치로 증명하던 은밀한 밀회 점수, _상관 계수(Correlation)_ 를 배운 적 있으신가요?

$$
r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}} \quad (3.18)
$$

is also a measure of the linear relationship between $X$ and $Y$.$^5$ This suggests that we might be able to use $r = \text{Cor}(X, Y)$ instead of $R^2$ in order to assess the fit of the linear model. In fact, it can be shown that in the simple
오호라! 이 $r$(상관 계수) 마법의 척도 역시 $X$ 와 $Y$ 두 변수가 직선 궤적 위에서 얼마나 강력히 사슬처럼 엮여 나아가는지를 나타내는 선형 친밀도 척도 지표입니다.$^5$ 이런 찰떡같은 등식 성질은 결국 우리에게 "구태여 귀찮게 $R^2$를 구하지 말고 그냥 이 익숙한 상관 계수 $r = \text{Cor}(X, Y)$ 를 대타로 내보내 회귀 선형 퀄리티 도구를 대신해 적합성 성적을 메겨버려도 일맥상통 무방하겠는걸?" 하는 짜릿한 제안을 던져줍니다. 사실 알고 보면 이런 초보적인 1차원 단순 회귀

> $^5$ We note that in fact, the right-hand side of (3.18) is the sample correlation; thus, it would be more correct to write $\widehat{\text{Cor}}(X, Y)$; however, we omit the "hat" for ease of notation.
> $^5$ 깐깐한 통계 학자들을 위해 살짝 부연하자면, (3.18) 공식의 오른쪽 팔꿈치 수식은 사실 모집단의 진짜 신의 숫자가 아니라 우리가 긁어모은 표본 데이터 나부랭이를 통한 '표본 상관(Sample Correlation)' 찌꺼기에 불과합니다. 따라서 엄격히 규율을 따지자면 가짜 복제품 티를 팍팍 내는 꼬깔모자 기호 $\widehat{\text{Cor}}(X, Y)$ 라 적는 게 통계 법정에서 무죄를 선고받을 정답이겠지만; 지면 낭비와 여러분의 안구 보호를 위해 여기서 복잡한 "햇(hat)" 따위 장식품 기호는 과감하게 던져버리고 생략하기로 묵계합시다.

80 3. Linear Regression
(3장 선형 회귀 80페이지)

<br>
**Simple regression of `sales` on `radio`**
<p align="center"><b>`radio(라디오 예산)` 지출 방어력 대비 `sales` 의 단순 직선 예측 회귀 스코어표</b></p>
<br>
| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 9.312 | 0.563 | 16.54 | $< 0.0001$ |
| `radio` | 0.203 | 0.020 | 9.92 | $< 0.0001$ |
**Simple regression of `sales` on `newspaper`**
<p align="center"><b>`newspaper(신문 예산)` 지출을 밀어 넣은 `sales` 의 단순 다트 게임 회귀표</b></p>
<br>
| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 12.351 | 0.621 | 19.88 | $< 0.0001$ |
| `newspaper` | 0.055 | 0.017 | 3.30 | $0.00115$ |

**TABLE 3.3.** _More simple linear regression models for the_ `Advertising` _data. Coefficients of the simple linear regression model for number of units sold on_ Top: _radio advertising budget and_ Bottom: _newspaper advertising budget. A $\$1,000$ increase in spending on radio advertising is associated with an average increase in sales by around 203 units, while the same increase in spending on newspaper advertising is associated with an average increase in sales by around 55 units. (Note that the_ `sales` _variable is in thousands of units, and the_ `radio` _and_ `newspaper` _variables are in thousands of dollars.)_
**TABLE 3.3.** 여러분의 통계 시력을 높여줄 `Advertising` _광고 수익 장부의 추가적인 단순 직선 회귀 스펙 모델 성적표 파노라마입니다. 아래는 순수히 단일 매체에만 기대어 팔아 재낀 물류 단위 수에 맞춘 직관적인 단선 회귀 추정 계수들 모음집입니다._ 위 테이블 라운드: _오직 라디오(`radio`) 라인 예산금 편성에 치중한 경우,_ 아래 등판 선수: _종이 신문(`newspaper`) 홍보 광고판에 올인했을 경우입니다. 재밌게도 라디오 매체에 짤랑짤랑 $\$1,000$ (약 130만 원) 가량 잔돈의 돈줄을 풀면 평균적으로 203 묶음의 대단한 물류 판매 급증 펌핑 리턴을 받아먹는 놀라운 시너지를 보입니다! 반면, 똑같은 $\$1,000$ 뭉칫돈을 죽어가는 신문지에 풀 먹일 때는 고작 55 박스의 애처로운 평균 판매 반등과 아주 약소하게만 연결되어 있다는 게 발각 났습니다. (이 동네 통계 단위가 심장이 크기에 유념하세요, 예측 결과인_ `sales(매출)` _박스는 수천 개 단위 묶음 그로스 기준이고, 원인 부스터 모터들인_ `radio` _및_ `newspaper` _쪽 오일 등유 치유 숫자판 규격도 다 수천 달러짜리 헤비급 덩어리로 잘려 있다는 점을 절대 잊으시면 안 됩니다.)_

linear regression setting, $R^2 = r^2$. In other words, the squared correlation and the $R^2$ statistic are identical. However, in the next section we will discuss the multiple linear regression problem, in which we use several predictors simultaneously to predict the response. The concept of correlation between the predictors and the response does not extend automatically to this setting, since correlation quantifies the association between a single pair of variables rather than between a larger number of variables. We will see that $R^2$ fills this role.
(방금 문장에서 이어짐) 환경 구조 속에서는 무려, **$R^2 = r^2$** 라는 마법 같은 일치 귀결 공식이 툭 떨어집니다. 한마디로 귀찮은 거 다 떼고, 그냥 단순무식하게 구려먹던 두 엇박자 사이의 '상관 계수를 통째로 제곱'한 덩어리가 기적처럼 $R^2$ 통계 지분 점수랑 토씨 하나 안 틀리고 쌍둥이처럼 완벽히 합치한다는 통쾌한 진리가 밝혀집니다. 하지만 잠깐! 바로 이어지는 넥스트 매직 스테이지(다중 통계) 구역에서는, 이 단세포적인 짝짜꿍 게임을 넘어 **"동시에 여러 개의 수많은 힌트 족집게들($X_1, X_2...$)을 무더기로 때려 박아 하나의 결과 스코어 방어율을 맞추는 거대한 다중 선형 회귀의 굴레"** 속 딜레마를 마주치게 됩니다. 문제는 우리가 알던 그 소꿉장난 같던 상관 계수($r$)의 우정 게임 척도가 이런 문어발 양다리 체계로는 자동으로 레벨업 확장 전이가 안 된다는 겁니다! 애초에 상관 마법($r$)은 단둘 사이 1대1 데이트 밀당 감도만을 집중 조명할 뿐 다수의 양반들을 한 지붕 아래 엮고 측정하는 다인큐 스킬 따위는 전혀 할 줄 모르기 때문입니다. 그래서 우린 바로 이 공백의 구원 타석 영웅 자리를 대신해, $R^2$ 이 녀석이 그 거대한 다인다발 파이를 집어삼키는 측정 왕좌 역할을 늠름하게 꿰차고 채워주게 되는 가슴 벅찬 명장면을 다음 섹션부터 목격하게 될 것입니다. 

## Sub-Chapters

[< 3.1.2 Assessing the Accuracy of the Coefficient Estimates](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/trans2.html) | [3.2 Multiple Linear Regression >](../../3_2_multiple_linear_regression/trans2.html)
