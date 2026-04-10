---
layout: default
title: "index"
---

# 2.1.5 Regression Versus Classification Problems 
# 2.1.5 회귀 문제 대 분류 문제 (Regression Versus Classification Problems)

Variables can be characterized as either _quantitative_ or _qualitative_ (also known as _categorical_ ).

분석되는 변수의 형태 성질은 그 기반 속성에 지표에 따라 크게 수치를 갖는 _양적(quantitative)_ 변수 형태이거나 혹은 (흔히 종종 _범주형(categorical)_ 으로도 더 유명하게 널리 잘 알려진) 특성을 구분하는 _질적(qualitative)_ 변수로 양극화되어 크게 둘 중 하나의 성향으로 반드시 특정 지어 분류 특징지어질 수 있습니다.

Quantitative variables take on numerical values.

이러한 분포 중 양적 변수(quantitative variables) 모델은 항상 뚜렷한 수리적 높낮이가 존재하는 실수 등과 같이 비교 가능한 성질의 수치적 결괏값(numerical values) 형태를 측정치의 결과로 직접 취합니다.

Examples include a person’s age, height, or income, the value of a house, and the price of a stock.

단편적인 구체적인 주변 실체적 예시 지표로는 특정인 사람의 물리적 측정 나이나 신장 키 수치, 또는 측정 경제적 수입치(income), 혹은 부동산 주택의 측정 현물 가치, 그리고 유가 증권 주식의 지표 가격 수치 거래치 등이 아주 자연스럽게 이 양적 분포 범주 체계의 전형적인 포함 모델 예시로 포함됩니다.

In contrast, qualitative variables take on values in one of _K_ different _classes_ , or categories.

이와 정면으로 아주 뚜렷이 대비되게 대조적으로, 질적 변수(qualitative variables) 형태는 결코 크기를 지닌 수치 체계를 갖지 않는 대신 상호 각기 전혀 다른 형태를 띠어 독립된 _K_ 개의 고정된 _클래스(classes)_ , 혹은 고정 항목인 범주(categories) 소속 분류 카테고리 중 단지 하나의 항목만을 관측치로 지칭하여 취합니다.

Examples of qualitative variables include a person’s marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia).

이렇게 비수치적인 이 질적 분석 변수의 대표적인 모델 예시로는 어떤 임의 특정 개인의 혼인 기혼 유무 등의 법적 결혼 상태 분포(결혼함 또는 결혼 아직 안 함), 혹은 구매자가 구입한 상업용 제품의 로고 브랜드 소속(A 브랜드, B 브랜드, 또는 C 브랜드 등), 혹은 채무자가 향후 미래에 대출된 빚에 대해 체납 파산하여 채무 불이행을 일으킬지 파산 여부 상태 예측(예 혹은 아니오 발생 여부), 혹은 의료적 암 선고 진단명 분류의 결과치 상황(급성 골수성 백혈병 발생 여부 판별 혹은 급성 림프모구성 백혈병 발현 혹은 암 종양 세포 부재로 정상인 백혈병 아님으로 분류) 등이 극명하게 이에 해당하는 범주의 형태 예시들로 직접적으로 모두 포괄 포함됩니다.

We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 이렇게 결과물 종속 형태 정답이 수치적 지표의 양적(quantitative) 등락의 응답 지표 결과를 동반해 지닌 예측 문제의 분류 상황을 흔히 주로 통상 _회귀(regression)_ 문제라고 자주 지칭하여 부르는 모델 경향이 있는 반면, 이에 반대편 대비되어 전혀 비수치적이고 수치적 크기 연관이 아예 없는 질적(qualitative) 항목 선택형 응답 결과를 예측 목표로 삼는 상황의 예측 분석 결과 문제 상황은 통상적으로 이를 집단 구별 문제인 _분류(classification)_ 문제 형태라 자주 흔히 지칭하여 이분화합니다.

However, the distinction is not always that crisp.

그러나 언제나 그렇듯 통계학 세계에서 두 가지 대립 차원 사이의 이런 무 자르듯 한 명쾌한 이분법적 개념 구별 선 긋기 체계가 항시 늘 그렇게 언제나 늘 명확히 칼같이(crisp) 나누어져 떨어지며 자명한 것은 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_ ) response.

예를 들어 앞서 향후 제3장 파트에서 심도 있게 깊이 다룰 고전적인 최소 제곱 선형 회귀의 기법 모드는 가장 전형적인 수치 체계 모델인 만큼 무조건 수량적인 양적 예측 응답 데이터 반응 결괏값을 목표로 사용되지만 예측 도출하지만, 그에 비하여 이름은 동일 회귀임에도 제4장 단원에서 엮여 논의될 _로지스틱 회귀(logistic regression)_ 의 경우는 이 기법이 사실 수치가 아니라, 뚜렷하게 아주 양극화되어 판별되는 질적 항목 범주 구분(좀 더 정확히 좁혀 말하자면 이분법적으로 정확히 오직 단 두 개의 상이한 구분 클래스 항목만을 양자택일하는 _이진(binary)_ 형태 응답 구조)의 특수한 정답 결과 요소를 분류하는 데에 아주 특징적으로 전형적 예측 기법으로 주로 널리 채택되어 통용되어 자주 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

그렇기 때문에 이처럼 로지스틱 회귀 현상 분석 구조의 특성은 그 표면적인 통계학 전문 공식 명칭 명명(이름상 '회귀')에도 정작 완전히 정반대되게 무색하게스리, 이 분석 방식은 본질 통계 구조 역학 체계론적으로 볼 때 틀림없는 완벽한 범주 예측 분석 기법인 분류(classification) 방식의 하나입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

하지만 여기서 또 한 번 반전이 일어나는데 통상적으로 이 분류 기법이 예측을 내놓을 때 단순히 항목 자체를 무턱대고 바로 내뱉지 않고 각 항목 클래스에 직접 속할 확률 가능성 비율적인 퍼센트의 수치 통계적 '확률(probabilities)' 자체를 1차로 수리적 추정해 구하여 산출해 내기 때문에, 그 연산 과정을 고려하면 어떤 의미 기능 관점에서는 이것이 충분히 아주 훌륭한 산술 회귀 분석 산출(regression method) 방법의 일부 지위인 기능 구조 절차로도 함께 다분히 간주되어 널리 광범위하게 함께 생각될(thought of) 수도 있습니다.

Some statistical methods, such as _K_ -nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

나아가 이러한 불분명한 경계를 더욱 관통하는 유연한 도태적 모델 기법들, 예를 들면 _K-최근접 이웃(K-nearest neighbors)_ 기법(제2장 및 4장에서 논의 통찰 예정)이나 고차원 기법인 부스팅 모델(boosting)(제8장에서 상세 설명 예정) 등과 같은 일부 강력하고 현대적인 유연한 융합 통계 모델 분석 방법론들의 경우 등은, 도출하는 목표 반응치 응답 요인인 종속 변수(y) 결과 목표 데이터 묶음이 수치의 양적 속성이든 아니면 집단 소속의 질적 형태 속성이든 아예 조금도 종류 무관하게 전혀 구애받지 않고 아예 양측 예측 분류 도출 상황 모든 경우에 전천후로 두루두루 모조리 다 자유자재로 함께 겸용되어 아주 빈번히 활발하게 전격 모두 다 널리 채택되어 무궁무진하게 활용 사용될 수 있습니다.

We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.

이처럼 우리는 일차적인 통계적 학습의 초석 접근 방법론 방향의 전개 기틀을 도출 선택할 때 최우선적으로, 가장 먼저 고려될 척도는 최종 관측 정답 응답의 그 뼈대 형태가 양적 수치 체계가 될 것인지 아니면 질적 분류 체계가 되는지 등의 지표 기준 여부를 철저한 기초 바탕 정보 기준으로 아주 강하게 일차적으로 삼아 예측 방향 체계를 결정하고 전격적으로 선택하는 가장 초기 설계의 강렬한 경향성을 지닙니다; 즉 달리 직관적으로 풀어 부연 설명하자면, 만일 분석 결괏값 대상이 명백히 수치적인 양적 지표 상태라면 망설임 없이 기계적으로 선형 회귀 같은 분석 예측 체계를 모델로 일차적으로 채택하여 아주 쉽게 사용할 것이며 반대로 만약 정답 예상 출력 변수 체계가 속성 그룹 등의 범주 질적 상황이라면 이때는 망설임 없이 분류 측면 모델 기법인 로지스틱 회귀 기법 모델 등을 최우선 검토하여 사용하는 것이 아주 가장 일반적인 가장 통상의 통계 논리 접근 기본 단계의 판단 도출 경향 지표입니다.

However, whether the _predictors_ are qualitative or quantitative is generally considered less important.

하지만 정작 이러한 결론 도출 출력 항목과 완전히 별개로 반대편 진입 입력 정보들, 즉 원인 투입 정보인 _예측 변수들(predictors, x의 투입 요소들)_ 무리가 정작 자신들이 내부적으로 질적 요소 항목이든 혹은 양적 인자 요소를 지녔든간에 그 입력 변수의 체계 자체 그들의 기저의 데이터 속성 진영 여부는 정작 일반적인 모델 구성 관점 지표에서는 그리 엄청난 파급 제약 등을 일으키거나 하지 않아 도리어 대수롭지 않게 아예 훨씬 그 도출 여부 분석 중요도가 매우 상대적으로 더 적게, 거의 신경 쓰지 않게(less important) 종종 별일 아니오 간주됩니다.

Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly _coded_ before the analysis is performed.

이 놀랍게 두꺼운 이 책 전반 단원에 이르러 우리가 끝없이 분석 다루어 논의하게 될 거의 극 대다수의 웬만한 통계적 기계 주요 파급 학습 방법론 기법 분석 기술 체계 구조 등은, 그 어떤 유형 체계의 질적 항목 형태의 소속 진영 예측 입력 데이터 변수일지라도 그것들 형태가 실제 분석 계산 작업 환경 과정 시스템 내부로 최초 도입 시 구동 투입 수행 처리되기 사전에(before the analysis is performed), 기계가 알아들을 수 있는 분석 가능한 아주 적절하고도 합당한 규칙 변환 절차에 입각하여 정확히 기호 등으로 잘 변환 _코딩(coded)_ 되거나 숫자 형태 더미 변수 등으로 아주 올바르고 정확하게 적절한 숫자 변환 코딩 수치화 과정 규칙 처리 절차만이 무사히 온전하게 구조적으로 변환 전제되어 보장되어만 충분히 준다면, 예측 입력 투입 원인 변수(x) 무리들 자체의 데이터 고유 유형 속성 체계 유형 성질 따위에는 완전히 상관없이 그것과 아예 무관하게 거의 모조리 자유롭게 모조리 어디에나 다 두루 활발하게 별 지장 없이 예측 산출 전격 투입 적용될 수 있습니다.

This is discussed in Chapter 3. 

이러한 범주 질적 데이터 입력 형태와 변수들의 적절한 처리 규칙 변환 코딩 치환 방법에 관한 흥미롭고 구체적 통계 지표 정보의 매우 자세한 논의는 바로 이어질 3장 항목 전면 파트에서 더욱 광범위하고 심도 있게 제대로 펼쳐지며 맹렬하게 토의 다루어질 것입니다.
