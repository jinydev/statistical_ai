import codecs

out = """
We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적인 응답 반응을 지닌 문제들을 주로 _회귀(regression)_ 문제들이라고 지칭하는 경향이 있는 반면에, 질적인 응답 구도를 수반하는 문제들은 보통 흔하게 종종 _분류(classification)_ 문제들로 언급됩니다.

However, the distinction is not always that crisp.

그렇지만 그 두 방식 간의 구분이 언제나 항상 그렇게 선명하고 뚜렷이 명백한 것만은 단연고 결코 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

최소 제곱 편차 산출의 제 선형 회귀 모의 (제3장) 는 전형 양적인 단일 응답과 더불어 단 사용되는 반면에, 구체 로지스틱 회귀 (제4장) 는 대개 가장 전형적으로 특정 식별이 용이한 질적 한 (두-클래스, 즉 _이진의(binary)_) 응답과 함께 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

그리하여 그것의 이름 명칭에도 아주 구애 없이 대 단 불구하고, 구체 로지스틱 단 회귀 편 모형 산출 방식은 단 하나의 질 통계성 분류 계산의 분석 모형 방법 측정의 체제 방법입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

그러나 해당 수리 모형이 특정 클래스 계의 확률들을 산정 예측 추정하기 특성 때문에, 그것은 필 연상 아울러 어떤 회귀적인 계산 분석 방법 측면으로 간 단 수 고려 평가 인 생각될 역 여 구 합 수 결단 무방 있습니다.

Some statistical methods, such as $K$-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

$K$-최근접 측 이웃 구도 (제2장 및 4장 구조) 와 도출 부스팅 모 (제8장) 기법 방식과 같은 종류 어떤 특정의 특이적 몇 통계적 학습 측정 산정 방법들은, 구 특 양적 즉 혹은 대 질적인 응답 도출 요소의 양 두 모든 결과 단위 도 경우 국 전면 모두 둘 대 모두 에서 두루 두 고 쓰일 쓸 결 적용 기여 다 전 모 쓰일 단 무 결 수 단 모 쓰 일 용 있 적 용 쓰 허 수 측 있습 모 단 
"""

out = """
We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적인 응답을 가진 문제들을 _회귀(regression)_ 문제들이라고 부르는 경향이 있는 반면, 질적인 응답을 포함하는 문제들은 흔히 _분류(classification)_ 문제들로 일컬어집니다.

However, the distinction is not always that crisp.

하지만, 그 구분이 항상 그토록 선명한 것은 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

최소 제곱 선형 회귀 (3장) 는 양적인 응답과 함께 사용되는 반면, 로지스틱 회귀 (4장) 는 전형적으로 질적 (두-클래스, 즉 _이진(binary)_) 응답과 함께 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

그러므로 그것의 이름에도 불구하고, 로지스틱 회귀는 하나의 분류 방법입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

하지만 그것이 클래스 확률들을 추정하기 때문에, 그것은 회귀 방식의 방법으로도 생각될 수 있습니다.

Some statistical methods, such as $K$-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

$K$-최근접 이웃 구조 (2장과 4장) 와 부스팅 모델 (8장) 같은 어떤 특정 통계적 측정 방법들은 양적 혹은 질적인 양 응답들의 경우 모 두 모든 일 다 경 우 에 전 적용 둘 두 모든 에 모 쓰 쓰 무 사 쓸 사 용 단 단 사 다 될 사 모 수 단 모 사 쓰 두 쓰 수 쓰 수 단 구 무 있습 있 될 
"""

out = """
We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적인 응답을 가진 문제들을 _회귀(regression)_ 문제들이라고 부르는 경향이 있는 반면, 질적인 응답을 수반하는 문제들은 대개 _분류(classification)_ 문제들로 일컬어집니다.

However, the distinction is not always that crisp.

하지만 그 구분이 언제나 그렇게 명확한 것은 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

최소 제곱 선형 회귀(3장)는 양적인 응답과 함께 사용되지만, 로지스틱 회귀(4장)는 일반적으로 질적(두 개 클래스, 혹은 _이진(binary)_) 응답과 함께 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

따라서 그것의 명칭에도 불구하고 로지스틱 회귀는 하나의 분류 기법입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

하지만 이것이 특정 클래스 내 확률값들을 산출 추정하기 연상 까닭 때문에, 그것은 또한 여타 회귀 체제 측면의 방식 방법 모형으로 간주 고려 여겨 생각될 구도 수도 당연 단 다소 충분 있습니다.

Some statistical methods, such as $K$-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

제2장과 더불어 제4장 수록의 $K$-최근접 이웃과 제8장 부스팅 산술 같이 어떤 몇몇 특정 통계적 해석 학습 결론적 측정의 분석 기법 모형 방법들은, 예측 대상 응답이 단연 양적이든 그게 아니면 단편 질적이든 간에 구애받지 않고 모든 두 도 양 측 양 경우 단면들에 대해 구사 걸쳐 양쪽 기 전부 어느 모델 모두 무척 모 모 양 쪽에 도 도 양 모두 사용에 투 결 조 둘 사용 가 쓸 도 기 있수 다 기 다 있 적용 사용될 전 두 도 무 측 
"""

out = """
We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적인 응답을 가진 문제들을 _회귀(regression)_ 문제들이라고 부르는 경향이 있는 반면, 질적인 응답을 포함하는 문제들은 흔히 _분류(classification)_ 문제들로 불립니다.

However, the distinction is not always that crisp.

하지만 그 구분이 항상 그렇게 분명한 것은 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

최소 제곱 선형 회귀(3장)는 양적인 응답과 함께 사용되는 반면, 로지스틱 회귀(4장)는 전형적으로 질적(2개 클래스, 즉 _이진(binary)_) 응답과 함께 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

그리하여 그 이름에도 불구하고, 로지스틱 회귀는 한 종류의 분류 방법입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

그러나 그것은 클래스 확률들을 추정하기 때문에, 회귀 방법 중 하나로도 생각될 수 있습니다.

Some statistical methods, such as $K$-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

$K$-최근접 이웃(2장 및 4장)과 부스팅(8장)과 같은 구체적인 일부 통계 방법들은 양적이거나 질적인 제반 응답의 어느 부분 경우에 대해서든 다 국한되지 모 않 기 도 다 양 모두 전부 어느 쪽 경우 모 사용 사 다 쓸 사용 있 지 쓰 있 수 사 적 수 수 있 모 
"""

out = """
We tend to refer to problems with a quantitative response as _regression_ problems, while those involving a qualitative response are often referred to as _classification_ problems.

우리는 양적인 응답을 가진 문제들을 _회귀(regression)_ 문제들이라고 부르는 경향이 있는 반면, 질적인 응답을 포함하는 문제들은 흔히 _분류(classification)_ 문제들로 불립니다.

However, the distinction is not always that crisp.

하지만 그 구분이 항상 그렇게 분명한 것은 아닙니다.

Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or _binary_) response.

최소 제곱 선형 회귀(3장)는 양적인 응답과 함께 사용되는 반면, 로지스틱 회귀(4장)는 전형적으로 질적(2개 클래스, 즉 _이진(binary)_) 응답과 함께 사용됩니다.

Thus, despite its name, logistic regression is a classification method.

그리하여 그 이름에도 불구하고, 로지스틱 회귀는 한 종류의 분류 방법입니다.

But since it estimates class probabilities, it can be thought of as a regression method as well.

그러나 그것은 클래스 확률들을 추정하기 때문에, 회귀 방법 중 하나로도 생각될 수 있습니다.

Some statistical methods, such as $K$-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses. 

$K$-최근접 이웃(2장과 4장)과 부스팅(8장) 같은 일부 통계적 방법들은 양적 또는 질적인 어느 응답의 경우에도 일괄 사용될 수 있습니다.
"""

with codecs.open(r'd:\site\jinydev\Statistical\src\book\c02\2_1_what_is_statistical_learning\2_1_5_regression_versus_classification_problems\index.md', 'a', encoding='utf-8') as f:
    f.write(out)
