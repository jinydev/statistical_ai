---
layout: default
title: "index"
---

# 2.1.4 Supervised Versus Unsupervised Learning 
# 2.1.4 지도 학습 대 비지도 학습 (Supervised Versus Unsupervised Learning)

Most statistical learning problems fall into one of two categories: _supervised_ or _unsupervised_ .

세상의 아주 수많은 대다수의 통계적 기계 학습 문제들은 크게 성질에 따라 _지도 학습(supervised)_ 또는 _비지도 학습(unsupervised)_ 이라는 두 가지 범주 체계 중 하나에 거의 완벽하게 분류되어 떨어집니다.

The examples that we have discussed so far in this chapter all fall into the supervised learning domain.

우리가 지금까지 앞선 목차 이 장에서 심도 있게 거론하고 논의했던 모든 수많은 단편적 사례들은 전부 다 예외 없이 완벽하게 이 지도 학습(supervised learning)의 명백한 도메인 영역에 포함되어 속합니다.

For each observation of the predictor measurement(s) $x_i$ , _i_ = 1 _, . . . , n_ there is an associated response measurement $y_i$ .

이 도메인 체계에서는 각각 관측된 _i_ = 1 _, . . . , n_ 번까지의 입력 예측 변수 측정치 관측치인 $x_i$ 마다, 항상 그에 짝을 이루어 응답하는 종속 결과 측정치 결괏값 요소 데이터인 $y_i$ 가 쌍기둥처럼 하나씩 확실하게 연관되어 함께 필수 수집되어 존재합니다.

We wish to fit a model that relates the response to the predictors, with the aim of accurately predicting the response for future observations (prediction) or better understanding the relationship between the response and the predictors (inference).

이를 바탕으로 우리는 훗날 미지의 미래 시점에 수집될 다른 미래 관측치에 대해 발생될 예상 결과 응답들을 아주 정확하게 정답처럼 예측(prediction)해내거나, 혹은 반대로 결과 응답과 투입 원인 예측 변수들 사이의 깊게 얽힌 본질적 역학 상관관계를 훨씬 더 심도 있게 분석 원인 구조를 이해(inference)하려는 그러한 뚜렷한 목표(aim)를 가지고서, 그 기저의 요소 응답과 예측 변수들을 유기적으로 잘 연결시켜 연관 짓는(relates) 가장 훌륭한 최적 모형 모델을 찾아 구축하고 적합시키고자(fit) 매우 열망합니다.

Many classical statistical learning methods such as linear regression and _logistic regression_ (Chapter 4), as well as more modern approaches such as GAM, boosting, and support vector machines, operate in the supervised learning domain.

앞으로 이어질 4장에서 논의할 기초적인 선형 회귀(linear regression) 모델 및 _로지스틱 회귀(logistic regression)_ 분석의 방법론과 같은 전통적이고 무수한 수많은 고전적 고전 통계 학습 방법론들을 비롯하여, 그뿐 아니라 GAM, 복잡한 부스팅, 정밀한 서포트 벡터 머신 등과 같은 엄청나게 복잡한 최신식의 고해상도 최신 현대 접근 방법들은 모두 모조리 이 지도 학습 도메인 환경의 토대 위에서 강력하게 작동합니다.

The vast majority of this book is devoted to this setting. 

앞으로 펼쳐질 이 두껍고 방대한 책 전체 내용의 아주 대다수(vast majority) 엄청난 분량이 바로 이러한 뚜렷한 지도 학습 설정 환경에 대해 전적으로 다루어지며 상당수 할애됩니다.

By contrast, unsupervised learning describes the somewhat more challenging situation in which for every observation _i_ = 1 _, . . . , n_ , we observe a vector of measurements $x_i$ but no associated response $y_i$ .

이와 아예 근본 축부터 극명하게 대조적으로, 그 반대편 비지도 학습(unsupervised learning) 패러다임은 모든 각각의 관측치 _i_ = 1 _, . . . , n_ 에 대하여 다수의 입력 측정치 변수 요인 세트 벡터 값들인 $x_i$ 만은 어찌저찌 수집하여 관찰할 수 있지만, 정작 그에 단단히 결합되어 종속으로 함께 상응하여 도출되었어야 할 정답 결과인 연관 응답 데이터 $y_i$ 요소는 완전히 누락되어 전혀 수집되지 않은 관찰 불가의 조금 더 난해하고 훨씬 더 까다롭고 도전적인(challenging) 아주 특수한 정보 부재의 상황 환경을 기술합니다.

It is not possible to fit a linear regression model, since there is no response variable to predict.

이러한 수집 부재의 상황에서는 예측의 목표 자체가 될 기준 종속 응답 변수인 정답(y) 데이터의 존재가 아예 없기 때문에, 우리는 앞서 배운 선형 회귀 모형과 같은 고전적 축의 단순 모델조차 전혀 시도하여 수립하고 적합시키는 것이 근본적으로 수학적으로 불가능합니다.

In this setting, we are in some sense working blind; the situation is referred to as _unsupervised_ because we lack a response variable that can supervise our analysis.

따라서 이러한 지표가 없는 설정 환경에서, 비유하자면 우리는 어떤 의미인지 도통 방향을 알기 힘들게 마치 한 치 앞도 보이지 않는 맹인(blind)의 어두운 상태로 맹목적으로 분석 작엄 현황을 수행하는 것과 진배없이 놓여 있습니다; 또한 이러한 환경을 가리켜서 방향 지표 정답을 알려주어 우리들의 분석 향방을 제대로 분석하여 감독해주고(supervise) 교정 지도해 줄 목표 응답 변수가 원천 부족하므로 이러한 환경 상황 상태를 통계학에서는 흔히 일컬어서 특별하게 _비지도(unsupervised)_ 기법 분류 상황이라고 공식 지칭합니다.

What sort of statistical analysis is possible?

그렇다면 과연 정답이 누락된 이런 불모의 환경에서는 도대체 대체 어떤 유형의 불완전한 통계 조작 분석 시도가 그나마 과연 가능성으로나마 남아 있을까요?

We can seek to understand the relationships between the variables or between the observations.

우리는 이러한 비지도 분석 시도를 활용하여, 비록 정답(y)은 없지만 가지고 있는 입력 변수 쌍들 간의 서로의 깊은 유의미한 상관관계 체계나, 심지어 혹은 개별 훈련 표본 그 관측치 덩어리 자체 집단 분포 군집들 사이의 얽힌 구조적 유사성 상관관계 구조를 그 자체로 독립적으로 파악해 이해하려고 강력히 모색해 볼 수는 있습니다.

One statistical learning tool that we may use in this setting is _cluster analysis_ , or clustering.

이러한 정답이 배제된 환경에서 우리가 그나마 통계적 지표를 찾고자 능동적으로 크게 기대하여 전격 기용해 사용해 볼 수 있는 썩 훌륭한 비지도 통계적 기계 학습 도구들 중 두드러지는 아주 대표적인 하나는 바로 _군집 분석(cluster analysis)_ , 또는 흔히 영어로 통칭하여 거론되는 군집화(clustering) 기법입니다.

The goal of cluster analysis is to ascertain, on the basis of $x_1, . . . , x_n$ , whether the observations fall into relatively distinct groups.

이러한 군집 분석 통계 기법 활용의 궁극적인 존재의 근본 목표는, 철저히 정답 없는 무작위로 살포된 $x_1, . . . , x_n$ 표본 지표의 기초 정보만을 철저한 바탕으로 하여, 데이터상 분포된 아주 무수한 이런 개별 개개의 모든 조사 관측치들이 어떠한 자기들만의 특별한 연관성으로 인해 내부적으로 형성된 상대적으로 성질이 완전히 뚜렷이 구별되는 상이한 몇 개의 소수 독립 군집 이면 그룹(distinct groups)들 중 하나로 자연스레 갈라져 분류되어 속할 수 있는가의 숨겨진 데이터 구조 관계성 이면 지표를 도출해 내고 확실히 찾아 규명(ascertain)하는 것입니다.

For example, in a market segmentation study we might observe multiple characteristics (variables) for potential customers, such as zip code, family income, and shopping habits.

가장 피부에 쉽고 와닿는 현장 실사례를 예로 들어, 어떤 상업적 목적의 시장 세분화 마케팅 조사 분과 연구 파트에 직면하여서, 우리가 막연하지만 회사에 잠재적으로 유리한 신규 타겟 고객을 규명하기 위한 목적으로 그들을 파악고자 표본 고객 개별 개개인들에 대해 거주 지역 우편 번호(zip code), 각 가구의 월평균 경제적 가구 총수입(family income), 평소 주기 편의점 방문 횟수 등의 개인 쇼핑 소비 습관 빈도(shopping habits) 등과 같은 아주 복잡하고 다양한 여러 다중 특성 요소(변수) 항목들을 수집하고 대량 관찰했다고 가정해 추측해 봅시다.

We might believe that the customers fall into different groups, such as big spenders versus low spenders.

우리는 이러한 파편적인 데이터 특성 요소가 결국 개별 표본 고객들을 '씀씀이가 아주 큰 주요 지출 성향 고객(big spenders)' 대(versus) '짠돌이 같은 적은 절약 지출 성항 고객(low spenders)' 등과 같이 매우 극명하고 뚜렷하게 상이한 차이를 보이는 특수 속성의 완전히 서로 다른 개별 그룹 집단들로 결국 각기 분리되어 나뉘어 떨어질 것이라고 아주 강하게 직관적인 합리적 믿음을 가질 수 있습니다.

If the information about each customer’s spending patterns were available, then a supervised analysis would be possible.

만약 그렇게 분류하는 확실한 판단 근거 도출을 위해 이미 기수집된 조사 단계에서부터 각각의 모든 개별 조사 고객 표본 개체마다 실제로 각자가 도대체 어느 범위의 정답 카테고리 지출 성향 패턴(spending patterns) 정답에 속하는지에 대한 명확한 참 명제 지표 결괏값 정보 정답(y)이 아주 친절하게 모두 이용 가능하게 온전히 함께 수집된 상태로 제공되어 주어져 있었다면, 이때는 아주 간단히 그냥 지도 학습 분석(supervised analysis)을 깔끔히 실행 처리하는 것이 그저 너무도 아주 쉽게 충분히 그냥 가능했을 것입니다.

However, this information is not available—that is, we do not know whether each potential customer is a big spender or not.

그러나 슬프게도, 대부분의 현실 세계에서 우리들의 지표 현황을 반영하듯 결코 이 귀중한 정답 결과 판단 확증 정보 데이터 결괏값은 좀처럼 절대 보통 수집되어 잘 이용할 수 있는 상태로 주어지지 않습니다 — 요약하자면, 즉 우리의 현재 도출 과제는 현재 파악 중인 파편적 데이터만 가진 각 익명의 가상 잠재 표본 고객이 실제로 미래에 대형 고액 지출을 일으키는 아주 씀씀이가 큰 초거대 가치 중요 지출자 고객 정답일지(y) 아니면 소액 지출자에 불과할지 그 명백한 정답 분류 자체를 우리는 전혀 아직 알지 못합니다(do not know).

In this setting, we can try to cluster the customers on the basis of the variables measured, in order to identify distinct groups of potential customers.

이렇게 정답이 완전히 가려져 배제된 이 답답한 불투명 상황 설정 한도에서도, 우리는 숨겨져 잠식되어 있는 완전하게 독립적으로 상이하게 분명히 구별되는 특별하고 독특한 이면의 파편적 잠재 중요 고객 덩어리 그룹 무리를 식별해 찾아내기 위한 특수한 목적으로, 그저 단순하게 그나마 우리가 수집하여 알 수 있는 관측 측정된 개별 $x_i$ 변수들만을 그 기초로 철저하게 의존 사용하여 산발적으로 뿌려진 개별 잠재 고객들을 어떻게든 그룹화하여 군집화(cluster)시켜 묶어보고자 훌륭하고 의미 있게 그나마 고군분투 시도할 수 있습니다.

Identifying such groups can be of interest because it might be that the groups differ with respect to some property of interest, such as spending habits. 

이러한 기이하고 독특한 비지도 분류 무리 그룹들을 통계적으로 직접 식별해 도출해 내는 이러한 시도 과정 경험은 종종 꽤 많은 주요 관점 흥미(interest)를 우리에게 이끌어 엄청난 유용함을 선사하여 유발할 수 있는데, 이는 그 기저 분석으로 분리된 각 개별 통계 그룹 결과들이 아마도 소비 지출 패턴 습관 등과 같아 우리가 도달 지표로 간절히 알고자 관심을 가졌던 특정 목표 속성 도출 요인 측면 속에서 그룹 간의 꽤 극명하고 확실한 차이 구조를 은연중에 제대로 잘 분화하여 극명하게 파악해 보여줄 아주 높은 가능성을 지녔을 수 있기 때문입니다.

<p align="center">
  <img src="./img/Image_022.png" alt="Figure 2.8">
</p>

**FIGURE 2.8.** _A clustering data set involving three groups. Each group is shown using a different colored symbol._ Left: _The three groups are well-separated. In this setting, a clustering approach should successfully identify the three groups._ Right: _There is some overlap among the groups. Now the clustering task is more challenging._ 

**그림 2.8.** _본질적으로 세 개의 이질적인 독립 무리 그룹을 지닌 임의 발생된 군집화 시도 데이터 세트의 모습입니다. 분산된 각 개별 지표 표본점 무리 그룹은 관찰의 직관적 구분을 돕기 위해 데이터의 공간 분포 위에서 각기 서로 전혀 다른 색상의 상이한 특유 기호를 사용하여 색칠 표시되어 직관적으로 나타나 있습니다._ (좌측 패널 표면): _왼쪽 도표 상에서는, 이 기저 형성된 세 개의 무리 군집 분산 파편 그룹들이 상호 침범 없이 아주 공간적으로 뚜렷하게 멀리 벌어져 분리(well-separated)되어 명확히 동떨어진 군락을 이루며 존재합니다. 이렇게 그룹 구분이 뚜렷하고 이상적인 지표 환경 설정 구조 내에서라면, 군집화(clustering) 시도 분석 도구 접근법 기능 하나만으로도 그저 아주 쉽게 이 세 개의 그룹 덩어리 존재들을 별 오차의 고난 없이도 수학적으로 아주 명쾌하게 모조리 성공적으로(successfully) 식별해 나누어 훌륭하게 분해 분류해 낼 것입니다._ (우측 패널 표면): _그러나 반대로, 오른쪽 도표 환경 상황을 보면 세 그룹의 기저 형성 경계가 한데 마구 뭉쳐 심하게 흐려져 무리 사이에 공간이 아주 겹쳐 중첩되는 구간(overlap) 혼재 부분이 상당히 아주 많이 발생되어 복잡하게 어우러져 있는 혼잡한 다소 지저분한 분포 불량 구조가 명백하게 존재합니다. 이제 이러한 복합 중첩의 어려운 요소가 가미된 구조 환경 탓에 이 무리들을 순수 군집화만으로 모조리 완벽히 구분시켜 도출해 내는 무작위 분류 작업 과제는 방금 앞전의 시도 때보다 그 난이도가 훨씬 더 까다롭고 도전적인(more challenging) 고난의 극한 극한 난관 과업 분석 한계로 아주 크게 격상 상승하게 됩니다._

Figure 2.8 provides a simple illustration of the clustering problem.

우리 앞에 마주한 이 그림 2.8은 방금 다루었던 이런 심각한 난이도를 가져오는 군집화 분석 문제 구조적 어려움의 명확한 실상을 단적으로 대변해 보여주는 아주 훌륭하고 단순 명쾌한 기하학적 패널 지표 일러스트레이션을 제공합니다.

We have plotted 150 observations with measurements on two variables, $X_1$ and $X_2$.

우리는 흩뿌린 전체 데이터 세트 구조상의 수평 가로축 수직 세로축 역할을 하는 핵심 2개 요인 차원 변수, 즉 요소 $X_1$ 과 또 다른 $X_2$ 의 수직 수평 측정 위치 결괏값을 바탕으로 총합 개수 150개의 무수한 무작위 분포 관측치 점 표본들을 도표 위에 전격적으로 점을 무작위 찍어 살포하여 직접 모두 분포시켜 플롯팅(plotted) 했습니다.

Each observation corresponds to one of three distinct groups.

이렇게 공간상 널브러져 분포된 패널 상의 모든 개별 관측치 각 점들은 본질 그 이면 통계 구조에서 분명히 상호 간 완전히 차별되어 구별되는 은밀한 세 개의 독립 기저 분류 그룹 진영 파벌 중 정확히 어느 한 곳(one of three)에 반드시 포함되어 해당하고 상응하여 속하게 됩니다.

For illustrative purposes, we have plotted the members of each group using different colors and symbols.

시각적인 이해의 편의 도출의 이해 목적을 강력히 달성하기 위해, 공간상 흩뿌려진 각 통계 그룹 분류 파벌군에 속하는 모든 소속 점 멤버 구성원들의 본질 소속 파악이 가능토록 점 개체를 그들끼리 일부러 서로 전혀 다른 확연한 구별의 색상톤과 다채로운 모형 기호를 임의 지정 사용토록 하여 일부러 구별지어 플롯 해 표시했습니다.

However, in practice the group memberships are unknown, and the goal is to determine the group to which each observation belongs.

그러나 이 시각 모형은 편의상 조작 가미된 것이고, 엄격한 현실 통계(in practice) 데이터 원뿔 상황에서는, 이렇게 모든 개별 점 그룹의 어느 뚜렷한 표본이 대체 어느 특정 분포 소속 멤버인지의 그런 해답 지표 명찰 그룹 멤버십 소속 데이터 결과 분류 자체는 언제나 철저하게 아주 정답 없는 무참한 완전한 영구 미지의 영역(unknown)으로 주어지며, 우리의 군집 기법 분석 구조의 궁극적 최종 결과적 도달 목표는, 이런 전혀 모르는 수많은 각각의 암흑 개별 관측치 점 표본 데이터들이 개별상 도대체 근원적으로 어떤 그룹에 각자 결속되어 파편화되어 속하는 결정 결과 구조 형태를 가장 정확히 분류 판별해 도출 분석하여 내어 결정(determine)하는 것입니다.

In the left-hand panel of Figure 2.8, this is a relatively easy task because the groups are well-separated.

이러한 지독한 난제 파악 시도 구조 임무조차 그림 2.8의 왼쪽에 전시된 좌측 비교적 분화되어 얌전한 모습의 패널 도표 분면 분포 환경 현상 속에서는, 각 분포 기표 그룹들이 분포 공간상 상호 충돌 한계 없이 매우 아주 뚜렷하게 멀찍이 떨어져서 이상적으로 분리된 형태기이(well-separated) 때문에 이 분류 목표 달성 작업 모색 정도의 과업은 오히려 몹시 단순 산출될 매우 훌륭하고 상대적으로 놀랍게 쉬운 한결 편안한 작업 분류 수행(relatively easy task)에 불과합니다.

By contrast, the right-hand panel illustrates a more challenging setting in which there is some overlap between the groups.

그렇지만 다시 그에 아주 극명히 정면 대치하여 대조적으로 옆을 살피면, 이 오른쪽 패널 도표 겉면 일러스트레이션은 그룹들과 무리군집 분포 경계 지표 사이에 서로가 공간을 빼앗고 이리저리 혼재 침범 침투하는 모호하고 비대한 일부 지표 중첩 공간 현상(overlap) 혼재 부분이 무수하게 무작위 발생하여 존재하는 훨씬 복잡한 훨씬 심도 있고 무덤덤한 까다로운 복합 모델 설정 현상을 극한으로 보여주고 있습니다.

A clustering method could not be expected to assign all of the overlapping points to their correct group (blue, green, or orange). 

이러한 중첩의 복조 극한 상황을 이겨내고 일반 군집화 한정 기법(clustering method) 수준 모형이 저 혼재 분면에서 겹쳐 혼재된 모든 구역들의 모호하고 지저분한 중첩 측정 혼동 점 요인(points)들을 전부 단 한 점의 오차 오류나 혼동조차 전혀 일절 없이 그들의 진짜 본래 소속인 올바른 100% 정답 분류 그룹 분류(파란색, 초록색, 혹은 주황색) 소속으로 모조리 다 수치 정확하게 분류 할당해 내어 판별 기적 분류할 것이라고는 도저히 그 누구라도 일절 절대 기대할 수조차 결코 없을 것입니다.

In the examples shown in Figure 2.8, there are only two variables, and so one can simply visually inspect the scatterplots of the observations in order to identify clusters.

그림 2.8에 간단히 축약되어 제시된 모형 예시 구조들에서는 공간 분석 차원의 지표 구조가 불과 단 두 개의 단순한 변수(X1, X2)만으로 국한되어 존재하고, 그래서 사람이 육안으로 분석 도표 구조에서 단순히 인간의 지표 시각 기능으로 그 개별 개체 관측치들의 투영된 2차원 산점도(scatterplots) 패널을 훑어 시각적 직관 검사(visually inspect)하는 행위만으로도 어느 정도의 그나마 아주 단순 직관적인 은연중 파악 군집(clusters) 구별 식별들을 1차적으로 훌륭히 해낼 수조차 있습니다.

However, in practice, we often encounter data sets that contain many more than two variables.

하지만 이와 전혀 현실 세계(in practice)는 완전하게 판이하게, 우리는 종종 그 분석 지표 차원이 겨우 두 개의 변수가 아니라 기하급수적으로 이보다 아득히 어마어마하게 훨씬 더 많은 대규모 기표 차수 변수 요소 요인들을 내부에 집약시켜 포함하는 훨씬 덩치가 큰 대조 지표 거대 데이터 세트 정보(data sets)들과 끊임없이 마주치며 현장에서 자주 실질적 조우하게 됩니다.

In this case, we cannot easily plot the observations.

이런 다차원 무한 거대 규모 변수 사례들의 상황 요소 발생 직면 시, 우리는 그저 단순 관측 변수를 도화지나 공간상에 간단히 도표로 패널처럼 시각화하여 플롯팅 선점해 전부 뚜렷하게 도식화하는 행위조차 너무너무 구조적으로 불가능하게 쉽지 않고 결코 그럴 수조차 전혀 없습니다(cannot easily plot).

For instance, if there are _p_ variables in our data set, then $p(p - 1) / 2$ distinct scatterplots can be made, and visual inspection is simply not a viable way to identify clusters.

단적으로 기표해 예를 들어 산정하자면, 만약 우리의 현재 분석 수집 조사 데이터 세트 집약체 안에 기표 수 _p_ 개의 수많은 다중 방대 차수 변수가 존재한다고 감히 가정한다면, 수학적 계산 논리 도출에 의해 그 결과로만 총 $p(p - 1) / 2$ 개라는 무수하고 끔찍하게 많은 종류의 각기 모두 다른 차원 쌍의 기하학적 산점도 도표들을 방대하게 모조리 교차해 만들어 내야만 그 공간을 표시 및 비교 생성할 수 있으며, 당연히 이처럼 무지 막대한 차원 숫자의 도표를 사람이 전부 하나하나 맨눈으로 직접 시각 검사(visual inspection)를 실행 수동 시도하여 군집을 사람 눈으로 식별하려 해내는 것은 도저히 시간과 절차상 감당할 수 없을 정도로 불가능하여 단순히 생각해도 결코 실행 가능한 실현 가능 타당한(viable) 효율적인 정상적 대안 방법 시도조차 될 수조차 절대 없습니다.

For this reason, automated clustering methods are important.

바로 이러한 너무나 뚜렷하고도 압도적인 명백한 데이터 차원 한도적인 절대 이유 때문이라도, 기계를 훈련시켜 정답 없이 분류할 자동화된 군집 기법 방식 모형 기법 수단(automated clustering methods) 기능론이 이 분야에서 엄청나게 중요하고 절실한 필수 요소 구조로 강력한 학문의 중요한(important) 기초로 급부상합니다.

We discuss clustering and other unsupervised learning approaches in Chapter 12. 

우리는 다가오는 12장에 이르러 이런 광범위한 방식 등 비지표 기반인 군집화(clustering) 기법은 물론 그 외의 놀라운 여러 다양한 타 비지도 학습(unsupervised learning) 기법 방법론 접근 방식 전반 형태 요소들에 대해서 마침내 비로소 깊고 심도 있게 모두 포괄 광범위 논의를 다루게 될 것입니다.

Many problems fall naturally into the supervised or unsupervised learning paradigms.

물론 현존 세상의 다양한 여러 수없이 많은 통계 문제 분포 과제들은 아주 자연스럽게도 애초에 앞서 논의 지표에 설정한 기준의 가장 큰 두 축인 지도(supervised) 혹은 비지도(unsupervised) 기계 학습 패러다임 이론 범주 무리 중 하나로 단숨에 손쉽게 뚝 절반 체계 안으로 떨어지며 이분법 분류될 수 있습니다.

However, sometimes the question of whether an analysis should be considered supervised or unsupervised is less clear-cut.

그러나 간혹 아주 혼재되고 특수 결합된 기이한 일부 복합 상황 환경 모델 데이터 구조의 과제에 한해서, 이 과제물 시도 분석이 과연 한 방향인 지도 학습 축으로 무조건 여겨져 파악되어야 하는지 아니면 결여된 수치로 비지도 학습 축으로 강제로 취급 분류되어야 하는지에 대한 경계성 분할 질문 문제 파악 자체가, 결코 이분법처럼 무 자르듯이 이리 단순히 뚜렷하지 않고 경계가 서로 흐릿하게 뒤섞여 오히려 명확한 구분 분류 체계 자체가 무색해질 정도로 아주 덜 명백하게 훨씬 다소 많이 덜 명확한 꼬인 난제 현황(less clear-cut)에 봉착하는 지경도 분명 종종 존재하여 일어납니다.

For instance, suppose that we have a set of _n_ observations.

그 특수한 예시로 난해한 환경의 단편을 한 가지 극명히 꼽고 들어, 만일 우리 조직이 일정 한도로 고정된 숫자 개수인 총 _n_ 개의 수많은 관측된 묶음의 대량 수집 관측치 표본 데이터를 확보해 가졌다고 한 번 예시로 가정해 봅시다.

For _m_ of the observations, where _m < n_ , we have both predictor measurements and a response measurement.

전체 _n_ 개 관측 수집치 묶음 집단 모델 풀 중에서 개수 한도 _m_ 값 표본의 숫자가 전체 _n_ 보다 작은 범주 설정 _m < n_ 내에서 이 _m_ 개의 무리 집단 관측치들에 한해서만, 우리는 이들 한정된 표본들로부터 운이 좋게 입력 예측 변수 정보 측정치와 더불어 정답 도출 결과 종속 변수인 응답 측정치(response measurement) 지표 데이터(y) 측면 결괏값 두 가지 정보 무기 쌍들을 한 세트로 이 그룹에 한해서 모두 다 확보하여 운 좋게 가졌습니다.

For the remaining $n - m$ observations, we have predictor measurements but no response measurement.

그러나 그런 특수한 소수 표본들을 제외하고 전체 수량에서 남겨진 나머지 다수 $n - m$ 집단의 잔여 표본 덩어리 거대 관측치 무리 집단 모델에서는, 아쉽게도 오직 우리는 겉보기 지표 데이터인 원인 지수 입력 예측 변수(predictor measurements) 정보만 간신히 확보 측정수집해 지녔을 뿐 정작 중요한 그 결과 응답 지표 정답의 핵심 데이터 성질 응답 측정 결괏값(no response measurement) 지표는 이 절대다수 표본들에게는 철저히 부재하여 전혀 얻어 채울 수 없었습니다.

Such a scenario can arise if the predictors can be measured relatively cheaply but the corresponding responses are much more expensive to collect.

이러한 무작위적이고 반쪽짜리 정보 혼합 분포된 통계 정보 데이터의 끔찍하고 기형적 파편화 형태의 시나리오 불량 사태 구조 체계는, 만일 조사의 대상에서 개체 겉면의 원인 예측 변수 요소들만의 조사는 매우 상대적으로 큰 비용의 제약이 거의 없어 쉽고 무척 저렴하게 손쉽게 조사 수집 수량 관측될 수 있지만, 반면 그에 꼭 상응하여 결과 수반되는 진정한 도출 지표 정답 응답 데이터값 등의 지표 도출 성적 요인들의 수집 분석 획득 비용 등은 이를 모두 철저히 수집하려 분석하기에는 그 필요 수집 및 소요 수량 조달 비용 및 처리 절차 요구 비용 등 파급 소요 비용이 경제적으로 몹시 지독하게 무지막지하게 비싸고 막대하여 무수하게 엄청난 비용(expensive to collect)을 필연적으로 엄청 수반 요구해야만 하는 특수 정보 비대칭형 산업 환경 조건 속성의 수집 분석 환경 상황 체계상 구조 등에서 매우 심심찮고 은근하게 놀랍게 아주 자연스러운 발생으로 자주 흔하게 실현하여 도출돼 일어날 소지가 대단히 다분합니다.

We refer to this setting as a _semi-supervised learning_ problem.

우리는 이처럼 혼선되어 발생되고 기형적으로 정보 부족 요소가 융합 파편화되어 엉킨 돌연변이 환경의 통계 모델 설정(setting) 상황 현상을 우리 전문 용어로 흔히 지칭하여 _준지도 학습(semi-supervised learning, 반지도 기계 학습)_ 이라는 형태라는 통상적인 이분법 중간 경계선 용어의 난제로 지칭하여 일컫습니다.

In this setting, we wish to use a statistical learning method that can incorporate the _m_ observations for which response measurements are available as 정답 데이터가 주어진 묶음 무리 well as the $n - m$ observations for which they are not.

이러한 극단 복합 난해 설정 체제 상황의 난관 환경에서는, 당연하게도 우리는 분석 시스템 구조가 귀중한 정답 핵심 정보 지표인 응답(y값) 측정치를 지녀 그것이 도출 활용이 아주 원활히 가능하여 훌륭히 사용할 수 있도록 보장된 특급 표본 집단들인 이 소수 _m_ 개 관측치들의 분석 훈련 이점을 포함하여 최대한 유통 응용 이용하며 통합(incorporate)하는 것은 물론, 게다가 추가로 그것조차 가지지 못한 온통 지표 암흑 상태 불모지의 대다수 그룹 다수를 차지하는 덩어리인 나머지 정답 부재 결여의 남겨진 절대다수 $n - m$ 개 무리의 수많은 관측치 측정치 표본 덩어리 지표들조차도 통계 산입에 하나도 버림없이 모조리 융합하여 적합하게 분석 처리에 관여 가능토록 기획 반영하는 아주 초보 등 복잡 고도화된 한층 상위 차원의 우수한 복합 고성능 통계적 복합 모델 학습 통계 방법 수단을 기필코 전격 사용하고자 간절히 고대하며 바라고 크게 원하게(wish to use) 시도하게 됩니다.

Although this is an interesting topic, it is beyond the scope of this book. 

비록 이것이 장래 시대에 아주 엄청나게 무지 흥미롭고 거대하며 아주 주목받는 고도의 대규모 분석 주된 난제 초점 기법 주제(interesting topic)임에는 틀림없는 사실이겠지만, 이런 고도의 혼합형 분석은 아쉽게도 이 기초 입문 과정을 다루는 우리 이 책 교재 모델이 주로 목표하여 다루고자 의도 형성했던 이 교재 교과 과정 내용 자체의 포괄 한계 수준 역량 범주 목표 설정의 경계 사정권 심도(scope of this book)를 아득하게 그 이상으로 훨씬 넘어선 지점의 지나친 심화 난제의 범위(beyond)의 훨씬 윗급 단계를 띠고 형성하고 있습니다.
