---
layout: default
title: "index"
---

# 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability 
# 2.1.3 예측 정확도와 모델 해석 가능성 사이의 트레이드오프 관계

Of the many methods that we examine in this book, some are less flexible, or more restrictive, in the sense that they can produce just a relatively small range of shapes to estimate _f_ .

앞으로 이 책 전체 내용에서 우리가 광범위하게 검토할 아주 수많은 기법들 중에서, 적지 않은 일부 방식들은 단지 _f_ 를 추정(estimate)하고 표현해 내기 위해 상대적으로 매우 한정되고 작은 제약된 범위의 모양 형태만을 제한적으로 생산해 낼 수 있다는 측면성에 비추어, 덜 유연하거나(less flexible) 심하게 구조적으로 더 제한적(more restrictive)입니다.

For example, linear regression is a relatively inflexible approach, because it can only generate linear functions such as the lines shown in Figure 2.1 or the plane shown in Figure 2.4.

그 한 가지 대표 예시로, 선형 회귀(linear regression)는 통계 측정 기법 중에서도 아주 비교적 극히 유연하지 않은 단단한 형태의 접근 방식에 속하게 되는데, 이는 애당초에 모델 수립이 이전 그림 2.1에 명확히 제시된 다이렉트 직선이나 그림 2.4에서 도출된 평편한 패널 평면체와 같은 아주 판에 박힌듯한 수평적 구조의 선형 함수 형태만을 오직 단조롭게 생성하고 도출해 낼 수 있기 때문입니다.

Other methods, such as the thin plate splines shown in Figures 2.5 and 2.6, are considerably more flexible because they can generate a much wider range of possible shapes to estimate _f_ . 

이러한 제한적 단일 표면 모델과는 아주 극명하게 대조적으로, 선행 예시인 그림 2.5와 그림 2.6에 여실히 제대로 제시되어 나타난 구부러지는 얇은 판 스플라인(thin plate splines)과 같은 다른 모델들 차원의 기법들은 대상 구조 _f_ 형태를 자유자재로 예측 추정하고 적합하기 위해 기존보다 훨씬 더 폭넓고 방대하며 무수히 넓은 범위의 발생 가능한 다채로운 모든 꺾임 형상(shapes)을 스스로 유기적으로 생성해 낼 수 있기 때문에 훨씬 더 그 속성이 유연하게 고려됩니다.

<p align="center">
  <img src="./img/Image_021.png" alt="Figure 2.7">
</p>

**FIGURE 2.7.** _A representation of the tradeoff between flexibility and interpretability, using different statistical learning methods. In general, as the flexibility of a method increases, its interpretability decreases._

**그림 2.7.** _전체적으로 각기 아주 다른 다양한 특성의 수많은 통계적 학습 기법들을 도표 상에 직접 사용하여 표시한 유연성(flexibility)과 해석 가능성(interpretability) 사이의 반비례적인 트레이드오프(tradeoff) 지표 관계성에 대한 명확한 그래픽적 표현 구조입니다. 통계적 현상의 시사점으로 일반적으로 어떤 시도 기법이 지니는 곡률의 유연성이 무한하게 증가할수록, 반작용으로 그 복잡해진 구조 이면에 따르는 분석 해석의 가능성은 한없이 추락하여 필연적으로 감소함을 직관적으로 보여줍니다._

One might reasonably ask the following question: _why would we ever choose to use a more restrictive method instead of a very flexible approach?_

이러한 특성 속에서 분석자는 무척이나 합리적인 맥락으로 다음과 같은 정당항 날카로운 학술적 질문을 도출하여 던질 수 있을 것입니다: _그렇다면 그 이유가 도대체 무엇이관대, 어찌하여 우리는 측정 가능성을 활짝 열어둔 매우 유연하고 좋은 최신의 접근 방식을 버리고 굳이 옛것의 더 제한적인 성질의 단순 기법 모델을 계속해서 우선적으로 고집스레 선택하고 더 애용하여 사용하는 건가요?_

There are several reasons that we might prefer a more restrictive model.

이 난제에 대한 해답으로 우리가 더 제한적인 구조의 모델 기법을 훨씬 더 선호할 수밖에 없는 아주 합당하고 뚜렷함을 가지는 여러 복합 이유들이 명백히 존재합니다.

If we are mainly interested in inference, then restrictive models are much more interpretable.

가장 대표적인 일례로 만약 수행하는 현재 분석가인 우리의 예측 과제 관심사가 오직 인과 관계 추론(inference)을 달성하는 데 온전히 치중되어 있다면, 상대적으로 제한적인 구조의 선형적 축의 모델들이 모형 파악 해석의 가능성(interpretable) 측면에서 훨씬 더 탁월하여 훌륭합니다.

For instance, when inference is the goal, the linear model may be a good choice since it will be quite easy to understand the relationship between _Y_ and $X_1, X_2, . . . , X_p$ .

정리하자면, 이와 같이 통계 측정의 인과 추론 자체가 통계의 주된 뚜렷한 목표(goal)가 되는 이러한 현황에서는, 출력 변수인 요인 _Y_ 와 입력 예측 변수인 요소 $X_1, X_2, . . . , X_p$ 사이의 얽힌 직관적인 함수적 기능 관계를 인간의 직관으로 너무도 아주 쉽게 파악하여 이해할 수 있게 해 주는 장점을 지닌 직선 축의 선형 모델이 아주 훌륭한 이상적인 측정 채택 방법 선택이 될 수 있습니다.

In contrast, very flexible approaches, such as the splines discussed in Chapter 7 and displayed in Figures 2.5 and 2.6, and the boosting methods discussed in Chapter 8, can lead to such complicated estimates of _f_ that it is difficult to understand how any individual predictor is associated with the response. 

이러한 단순 모델의 편의성과 극명하게 대조적으로, 곧 앞선 그림 2.5 및 2.6에 예시로 강렬히 표시되고 향후 7장에서 심도 있게 다뤄질 정교한 스플라인들(splines) 접근이나 8장에서 추가로 깊이 논의할 기계 학습인 부스팅(boosting) 방법 기법과 같이 매우 복잡하게 유연한 형태들의 모델 접근법 방식들은 한 가지 치명적 요소로 함수 모형 _f_ 에 대한 너무나 복잡하고 일그러져 꼬인 추정치 형태를 복잡하게 시도하여 도출할 수 있으며, 이로 인하여 최종적으로는 도대체 어떠한 지표의 개별적인 개별 예측 변수 요인들이 전체 결과 응답 변수 체계와 무슨 구조로 어떻게 함수적으로 얽혀 연관되어 발생된 예측 인과 관계인지 도무지 인간의 논리로 이해하기가 극한으로 매우 힘들어지는 블랙박스의 부작용을 일으킬 수 있습니다.

Figure 2.7 provides an illustration of the trade-off between flexibility and interpretability for some of the methods that we cover in this book.

방금 제시된 도표인 그림 2.7은 우리가 이 두터운 책의 전반 구성에 걸쳐 앞으로 포괄적으로 직접 다루게 될 무수히 많은 현존 방법론들 중 일부 모델들에 대하여 이 치명적인 모델 유연성과 예측 해석 가능성 여부 사이의 서로 엇갈리는 트레이드오프 양상 지표를 뚜렷한 도표 일러스트레이션으로 명쾌하게 제공합니다.

Least squares linear regression, discussed in Chapter 3, is relatively inflexible but is quite interpretable.

앞선 챕터 중 3단원에서 크게 중점적으로 다룰 가장 기본적인 최소 제곱 선형 회귀(Least squares linear regression)는 전체 구조 양상이 상대적으로 전혀 유연하지 못하지만 모델 구성의 해석 여부 관점에서는 오히려 꽤나 아주 쉽게 직관적으로 이해할 수 있을 만큼 해석 가능성이 뚜렷합니다.

The _lasso_ , discussed in Chapter 6, relies upon the linear model (2.4) but uses an alternative fitting procedure for estimating the coefficients $\beta_0, \beta_1, . . . , \beta_p$ .

뒤에 이어질 제6장에서 거론 논의하게 될 특수한 _라쏘(lasso)_ 기법은 초기에 선형 모델식 구조 (2.4) 양상에 아주 강력히 의존하기는 하나, 정작 세부적인 매개 변수인 각 파라마터 계수들 $\beta_0, \beta_1, . . . , \beta_p$ 형태를 각기 새롭게 예측하고 온전히 도출해 추정하기 위해 기존과는 색다른 대안적인 회귀 적합 처리 절차 프로세스를 거쳐 전격적으로 이를 사용합니다.

The new procedure is more restrictive in estimating the coefficients, and sets a number of them to exactly zero.

이 과정에 도입된 이러한 라쏘의 새로운 도출 절차는 계수 매개 변수를 일일이 추정하고 도출하는 단계에 있어 훨씬 구조적으로 더 엄격한 제한적인 제약 규칙(restrictive)을 강제로 부여하며, 더불어 심지어 그 파라미터 변수들 중 일부 선택된 다수의 요인 파라미터 계수들이 아예 정확하게 0(zero)의 결괏값으로 완전히 삭제 소거되도록 강제로 소멸 설정하기도 합니다.

Hence in this sense the lasso is a less flexible approach than linear regression.

이러한 라쏘의 고유 구조 형태를 유지한 이런 특정 강제 제약적인 의미에 측면에 비추어 논의를 확장하자면, 오히려 라쏘 기법 방식은 통상의 일반적인 뻣뻣한 선형 회귀보다도 훨씬 더 고정된 적은 요소의 유연하지 못한 축소 접근 방식(less flexible approach)에 직면한 모양을 띠게 됩니다.

It is also more interpretable than linear regression, because in the final model the response variable will only be related to a small subset of the predictors—namely, those with nonzero coefficient estimates.

그럼에도 이러한 큰 단점적 요소 제약은 오히려 기이하게도 역으로, 최종적으로 수립된 궁극적인 완성 회귀 모델 내부에서 도출 결과 중심 응답 변수가 오직 0이 아닌 유의미한 비영(nonzero) 계수 도출 값의 추정치들을 살아남아 보유한 아주 소수 그룹의 한정된 중요 예측 변수 일부의 하위 집합(subset) 등과만 단출하고 간략하게 남겨져 연관될 명백한 예측 구조 성질을 100% 띠기 때문에, 결과론적 시점에서는 일반 기본적 선형 회귀 모드 등 보다도 도리어 파악의 과정이 무지막지하게 훨씬 더 해석 가능하고 뛰어나다는 역설적 강점 해석을 띠게 만들기도 합니다.

_Generalized additive models_ (GAMs), discussed in Chapter 7, instead extend the linear model (2.4) to allow for certain non-linear relationships.

이어 향후 전개될 7장에서 상세히 깊게 다룰 _일반화 가법 모델(Generalized additive models, GAMs)_ 기조는 그 발상의 측면에서 라쏘처럼 요소를 감소 및 축소하는 노선 선택 방식 대신 정반대로 특정 구역 단위의 고차원 비선형적 관계의 모델 수립을 가능하게끔 그 기존 선형 모델 형식 구조 (2.4) 틀을 외부로 뻗어 훨씬 크게 광범위하게 확장(extend)하게 만듭니다.

Consequently, GAMs are more flexible than linear regression.

이렇게 하여 도출된 직접적인 구조의 한 가지 논리 결과로서, 이 GAM 기법은 모형 형태 도출 결과적으로 기존 한계에 닫힌 일반 선형 회귀식 모델 수립보다 압도적으로 훨씬 더 엄청난 곡률의 유연한 모델 선 구축 결과를 창출합니다.

They are also somewhat less interpretable than linear regression, because the relationship between each predictor and the response is now modeled using a curve.

하지만 이런 엄청난 장점 뒤에는 또 다른 치명적인 그림자 트레이드오프가 존재하여, 그렇게 도입 사용한 막강한 곡률 덕에 이제 각각의 파편적 예측 개입 변수와 출력되는 결과 응답 변수들 사이의 관계 구조가 직선이 아닌 훨씬 복잡하게 구부러지는 굴곡 곡선(curve)을 사용하여 이리저리 다방면으로 마구 모델링 예측 형성되기 때문에 이들은 예측 변수 구조와의 인과를 추론해낼 기존 모델의 해석 가능성 여부가 기초 단위 선형 회귀식보다는 불가피하게 다소 더 떨어지게 되고 기피됩니다.

Finally, fully non-linear methods such as _bagging_ , _boosting_ , _support vector machines_ with non-linear kernels, and _neural networks_ (deep learning), discussed in Chapters 8, 9, and 10, are highly flexible approaches that are harder to interpret. 

결과론적으로 정리해 보면 마지막으로 이어지는 이 책의 극후반기 목차인 8, 9, 10단원에서 장대하게 광역시로 논의할 방대하고 혁신적이고 극에 달한 기술, 이를테면 _배깅(bagging)_, _부스팅(boosting)_, 아주 고차원 복잡성 비선형 커널 방식을 철저히 의존해 사용하는 _서포트 벡터 머신(support vector machines)_, 그리고 극강의 블랙박스 기원 자체인 딥러닝 기반의 혁신 기법인 _신경망학습(neural networks, deep learning)_ 등과 같은 완벽히(fully) 구부러진 엄청난 고차원 비선형 극에 달한 방법론의 집합체들은 모델 스스로 데이터 구조의 곡률 유연성을 지독하게 복사하듯 만들어 낼 수 있는 등, 그 유연성의 수치가 상상을 초월하도록 매우 유연하지만(highly flexible approaches) 정작 너무나 높은 도출 모델 함수 차원의 해석 구조 복잡성으로 인해 우리 인간의 상식 논리로는 그 도출 예측 결과 수립을 해체하여 함수 이면의 도출 과정을 완전히 이해하며 인과를 명쾌하고 논리적으로 추론하여 전부 추정해 해석하기(interpret)가 아주 고되고 힘들고 훨씬 더 난해한 극악의 한계 극에 도달해 있습니다.

We have established that when inference is the goal, there are clear advantages to using simple and relatively inflexible statistical learning methods.

우리는 지금까지의 이러한 양측면의 다양한 기술 논의와 구조들을 통해 전체 모델의 궁극적 도출 방향과 목표지가 온전한 데이터 간 상관 인과 추론 관계(inference)인 환경에서는 도리어 구조 수립 체계가 너무너무 명확하고 단순하며, 따라서 곡률이 훨씬 덜 유연하고 기계적인 뻣뻣한 형태(inflexible)를 보이는 통계적 학습의 단순 방법론 기법을 전략 모델로서 선택 사용하는 것이 오히려 막강하고 다분히 분명하며 수없이 놀라운 큰 강점 이점을 우리에게 안겨 준다는 점을 지금까지 학술적으로 견고히 하여 명백히 증명해 확립했습니다.

In some settings, however, we are only interested in prediction, and the interpretability of the predictive model is simply not of interest.

그럼에도 불구하고 어떤 매우 특수한 목표 상황적 요구 환경 설정의 맥락 지표에서는 인과 추론은 전부 폐기한 체 오직 결과 산출 예측값에 대한 정밀한 절대 수리 '예측(prediction)' 그 자체에만 굳건한 관심이 온통 모두 깊게 쏠려 있고 포커싱(focusing)이 맞춰지게 되어, 예측 모델 자체가 구성되어 얽힌 과정 이면에 관한 해석의 가능성 유무 여부 등에는 당연히 절대 티끌만치도 전혀 단 한 점의 관심조차 동요가 있지 않은 극단적 도출 경우 상황들도 엄연히 빈번하게 많이 존재하여 나타나곤 합니다.

For instance, if we seek to develop an algorithm to predict the price of a stock, our sole requirement for the algorithm is that it predict accurately— interpretability is not a concern.

예를 들어 단적으로 말해, 어느 투자 기표 관측자가 만약 증시상의 복잡다단한 향후 주가의 미래 시세 추이 가격 흐름을 예측하여 수치로 제시하는 막강한 예측 도출 알고리즘 시스템 구조를 정교하게 개발하려고 목표를 삼아 모색하는 이러한 특수한 상황에 처한 경우라면, 이러한 도출 모델 알고리즘에서 가장 시급히 요구하는 절대 불변의 필수 단 하나뿐인 목표 요구 사항 조건은 오로지 이 도출 시스템이 향후 주가를 100% 얼마나 정확하게 일치시켜 예상 예측해 내는가, 바로 그것뿐입니다 — 이 지표 모델이 왜 그런 값이 나왔는지 등, 그 내면 모델 예측 지표 이면에 달린 해석의 여부는 절대 어떠한 관심 요소나 필수 제약사 안건의 중대한 고려 사항(concern)이조차 될 수도 없습니다.

In this setting, we might expect that it will be best to use the most flexible model available.

그렇기에 방금 제기된 이와 같은 구조 설정 안에서라면 직관적으로 판단되어 우리는 십중팔구 사용할 수 있는 가장 성능 고차적의 수없이 복잡하여 가장 구부러지고 유연하게 얽힌(highly flexible) 최고 복잡도 형태를 지닌 복합 모델 구조를 강력히 끌어다 사용하는 등 활용하는 편이 가장 우수할 것이며 절대적인 모델 구축의 최선이자 최상책일 것이라고 그저 단순히 쉽사리 추측하고 기대할 수도 있을 것입니다.

Surprisingly, this is not always the case!

그러나 아주 놀랍게도(Surprisingly), 이러한 일차원적이고 단순무식한 접근의 판단 생각은 언제나, 항시 항상 모든 환경에서 언제나 무조건 전부 성립되는 불변의 진리가 곧장 전혀 아닙니다!

We will often obtain more accurate predictions using a less flexible method.

과적합 상황들에 의해 필연적으로 일그러져 역으로 우리는 아주 묘하게도 종종 훨씬 더 딱딱하고 유연성이 형편없이 떨어지는 기법 등의 덜 유연한 원시적인 방법으로 다듬어진 덜 복잡한 모델 구축에서 도리어 더 실질적이고 더 정확히 신뢰성 높은 결과의 예측 수치를 성공적으로 훌륭히 얻게 도출해 내는 특별한 경험 과정을 이따금씩 거치게 될 것입니다.

This phenomenon, which may seem counterintuitive at first glance, has to do with the potential for overfitting in highly flexible methods.

단순하게 생각하면 이러한 언뜻 첫눈에 보기엔 전혀 이치에 부합되지 않아 이해 불가로 아주 상반되고 직관에 반하여 보이는 이런 복합적인 현상의 요인은 사실 고도로 극한을 향해 얽히고 비틀리며 치달은 고성능의 매우 유연한 방법론의 함수 모형 구조 속 그 이면에 아주 조용히 잠식해 잠재되어 무수하게 숨겨져 자리 잡고 존재하는 모델 도출의 치명적인 가장 큰 장애물 중 하나인, 이 과적합(overfitting) 문제의 그 무시무시한 파급 가능성 파장 능력과 아주 심도 깊이 직접적으로 밀접 연관된 관련이 서로 있습니다.

We saw an example of overfitting in Figure 2.6.

이 지독한 과적합 현상이 불러올 수 있는 심각성 실패 파장 오류 참사의 한 가지 대표 사례는 곧 직전에 우리에게 익히 보여졌던 전시 그림 2.6의 모형 패널의 일그러진 요동 지표에서 이미 잘 목격해 확인된 바 있습니다.

We will discuss this very important concept further in Section 2.2 and throughout this book. 

우리는 앞으로 이어질 맹렬한 주제인 다음 파트 섹션 2.2를 비롯하여 향후 전개되는 이 두터운 방대한 정보의 책 장장 기조 전반 단원에 이르기까지 널리 걸쳐서 이러한 너무도 아주 중요하고 심장히 통계 분석에서 핵심으로 다뤄지는 이러한 필수적인 중요한 요소 기반 지식 개념 관해 한층 더 방대하게 고도화시켜 더 심도 깊게 거론하며 논의할 전개를 수립할 예정입니다.
