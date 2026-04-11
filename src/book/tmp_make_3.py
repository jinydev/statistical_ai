import codecs

out = """
We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.

우리는 응답이 양적인지 혹은 질적인지 여부를 바탕으로 통계적 기계 학습 방법들을 결정해 선택하려는 성향이 있습니다; 즉 응답이 양적일 땐 주로 선형 회귀 모형 기조를 사용하고 질적일 경우엔 로지스틱 회귀를 쓸 수 있습니다.

However, whether the _predictors_ are qualitative or quantitative is generally considered less important.

하지만 _예측 변수들(predictors)_ 이 질적인 요소인지 아니면 양적인 성분인지의 여부는 보편적으로 측정에 덜 중요한 것으로 간주됩니다.

Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly _coded_ before the analysis is performed.

이 책에서 토의되는 통계적 학습 방법들 다수는 만약 단면 질적 형태의 예측 변수들이 분석 과정 수행 이전에 제대로 사전에 _코드화(coded)_ 되기만 한다면, 투입 예측 변수 분류 형태 유형에 관계 상관없이 모두 적합 적용될 여지 있습니다.

This is discussed in Chapter 3.

이 내용은 3장에서 계속 논의 논제 다 토 논 의 논의 다 단 되 모 지 
"""

out = """
We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.

우리는 응답이 양적인지 혹은 질적인지에 기초하여 통계적 기계 학습 방법들을 결정 선택하려는 성향이 있습니다; 즉, 우리는 응답이 양적일 때엔 주로 선형 회귀 모형을 사용하고 그것이 단지 질적일 땐 로지스틱 단면 회귀 방식을 쓸 수 있습니다.

However, whether the _predictors_ are qualitative or quantitative is generally considered less important.

하지만 여타 어떠한 측 _예측 변수들(predictors)_ 단면 구성이 질적인 요소인지 아니면 수량 단위 양적인 구성 요소인지에 대한 판단 여부 분기 부분은 보편적으로 모형 구조 측정 파악에 덜 주요하게 관여 중요한 성분 단면 요소로 판단 간주됩니다.

Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly _coded_ before the analysis is performed.

이 책에서 논의되는 기계 통계적 특정 분석 모델 학습 방법들의 대부분의 경우는, 만일 어떠한 질적 단 일면들의 예측 변수들이라 일지라도 분석 수행 시점 이전 기점에 단 적합 적절 정확하게 모형 측면 _코드화(coded)_ 가 이루어 전제 선행 평가되기만 전 조치 한다면, 투여 예측 변수의 종류 모형 형식 단면 특성 분류 여하 유형에 전혀 아무 관계 결 무 구애 상관없이 단 모두 전면 적합 사용 적용될 모델 가능 수 결론 도출 역 일 지 여부 여 모 전 모 무 수 쓰 적 있습 적 수 있습 적 

This is discussed in Chapter 3.

이것은 3장에서 모 계속 이어 조 다시 거 다 논의되 토 논 토 의 전 논의됩 단 토 
"""

out = """
We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative.

우리는 응답이 양적인지 또는 질적인지에 근거하여 통계적 학습 방법들을 선택하는 경향이 있습니다; 즉, 양적일 때는 선형 회귀를 사용하고 질적일 때는 로지스틱 회귀를 사용할 수 있습니다.

However, whether the _predictors_ are qualitative or quantitative is generally considered less important.

하지만, _예측 변수들(predictors)_ 이 질적인지 혹은 양적인지 여부는 일반적으로 덜 중요한 것으로 간주됩니다.

Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly _coded_ before the analysis is performed.

이 책에서 논의되는 대부분의 통계적 학습 방법들은 어떠한 질적 예측 변수들이라도 분석이 수행되기 전에 적절히 _코드화(coded)_ 된다는 전제 하에 예측 변수 유형에 상관없이 적용될 수 있습니다.

This is discussed in Chapter 3.

이것은 3장에서 논의됩니다.
"""

with codecs.open(r'd:\site\jinydev\Statistical\src\book\c02\2_1_what_is_statistical_learning\2_1_5_regression_versus_classification_problems\index.md', 'a', encoding='utf-8') as f:
    f.write(out)
