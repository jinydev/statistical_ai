---
layout: default
title: "trans1"
---

# _5.3.2 Cross-Validation_ 
# _5.3.2 교차 검증_

In theory, the cross-validation estimate can be computed for any generalized linear model.
이론상으로 따져볼 때, 앞서 배운 교차 검증 추정치는 사실 그 어떠한 일반화 선형 모델(generalized linear model, GLM) 무기 라인업을 상대로도 언제든 연산 계산 산출될 수 있다.

In practice, however, the simplest way to cross-validate in Python is to use `sklearn` , which has a different interface or API than `statsmodels` , the code we have been using to fit GLMs. 
그러나 실무 현장 속 실질 구조상으로, 파이썬(Python) 환경 구역 내에서 교차 검증을 가동시키는 가장 직관적이고 심플한 방안책은 다름 아닌 머신러닝 라이브러리인 `sklearn` 을 활용 기용해 써먹는 것인데; 다만 이는 그간 우리가 GLM 기반 모델들을 장착 적합해 오던 익숙한 기본 코드 패키지 묶음인 `statsmodels` 툴의 체제와는 그 구조나 인터페이스, 혹은 API 취급 기조가 완전히 이질적으로 판이하게 다르다는 애로사항이 존재한다.

This is a problem which often confronts data scientists: “I have a function to do task _A_ , and need to feed it into something that performs task _B_ , so that I can compute _B_ ( _A_ ( _D_ )), where _D_ is my data.”
이 괴리 양상은 필드 전선 위에서 데이터 과학자들이 유독 왕왕 마주치며 씨름 대면 충돌하게(confronts) 되는 매우 전형적인 호환성 고충 문제 중 하나이다: “즉, 나한테 _A_ 란 임무 과제를 처리하는 함수 장치가 하나 수중에 있고, 이를 억지로 _B_ 란 과제를 물고 처리하는 다른 요건 장치 기계 부속 아가리 속으로 집어넣어 먹여야만, 그걸 통해 마침내 _B_ ( _A_ ( _D_ )) 구조의 연산 결괏값을 뽑아 계산해 낼 수 있다 치자 (물론 여기서 _D_ 는 내가 쥐고 있는 기본 데이터 덩어리다).”

When _A_ and _B_ don’t naturally speak to each other, this requires the use of a _wrapper_ .
만약 저 장치 부품인 _A_ 와 무기 부속 _B_ 녀석들 둘 시스템끼리 유기적으로 매끄럽게 자연스러운 언어 소통(speak to each other) 을 도통 인식해 내지 못할 적이면, 이는 필연적으로 중간 매개 어댑터 통역사 역할을 해줄 이른바 _래퍼(wrapper)_ 클래수 함수의 필수 도입을 요구하게 이른다.

In the `ISLP` package, we provide a wrapper, `sklearn_sm()` , that enables us to easily use the cross-validation tools of `sklearn` with models fit by `statsmodels` .
본 저서에 편입된 자체 학습 지원 모듈인 `ISLP` 패키지 군단 내에서, 우리는 학습자들에게 `sklearn_sm()` 이라는 이름의 이 래퍼(wrapper) 모듈을 무상 제공하고 있는데, 이는 우리로 하여금 고전적인 `statsmodels` 툴로 적합된 모델 무형 자산들에도 곧장 최신 `sklearn` 체제의 막강한 교차 검증 도구들을 아주 유들유들 손쉽게 연동 혼용 사용(use) 하도록 매끄럽게 지원 허가 가능(enables) 케 해준다.

The class `sklearn_sm()` has as its first argument a model from `statsmodels` .
이 `sklearn_sm()` 래퍼 클래스는 그 가장 앞선 첫 번째 도입 인자(argument) 파라미터 값으로 다름 아닌 고전 `statsmodels` 진영 출신의 분류 모델 객체를 직접 취해 넘겨받는다.

It can take two additional optional arguments: `model_str` which can be used to specify a formula, and `model_args` which should be a dictionary of additional arguments used when fitting the model.
나아가 이는 자의적 부수적으로 두 가지 옵셔널 추가 인자 성분을 임의 편입 취할(take) 수 있는데: 하나는 특정 함수 방정식 형태(formula) 를 기재 지정 세팅 지시해 서술할 당시 기용될 수 있는 속성인 `model_str` 이고, 다른 하나는 필시 응당 당해 해당 모델 무기를 훈련 적합 적재(fitting) 시킬 타이밍에 요구되는 부수적인 추가 인자 스펙 세팅 옵션들을 지닌 딕셔너리(dictionary) 맵 매개체 집합 속성 인자 `model_args` 이다.

For example, to fit a logistic regression model we have to specify a `family` argument.
가령 예시 격으로, 우리가 혹간 로지스틱 회귀 모델을 구동 적합시켜 보고자 할 요량이라면 우리는 무조건적으로 고정 함수 옵션 장치인 `family` 인자 지정 잣대를 어김없이 기입 세팅 지시(specify) 해 주어야 마땅하다.

This is passed as `model_args={'family':sm.families.Binomial()}` . 
이러한 부가적 파라미터 옵션 스펙은 곧장 파이썬 매핑 구조인 `model_args={'family':sm.families.Binomial()}` 딕셔너리 지시 사항 체제 수식으로서 매끄럽게 위임 하달 통과(passed) 입력된다.

Here is our wrapper in action: 
아래 코드는 이 래퍼 장치가 실제 현장에서 어떻게 호환 연동 기동 작전 수행(in action) 도무되는지를 시연한다:

```python
In [9]: hp_model = sklearn_sm(sm.OLS,
                              MS(['horsepower']))
        X, Y = Auto.drop(columns=['mpg']), Auto['mpg']
        cv_results = cross_validate(hp_model,
                                    X,
                                    Y,
                                    cv=Auto.shape[0])
        cv_err = np.mean(cv_results['test_score'])
        cv_err
```

---

## Sub-Chapters (하위 목차)

### 다중 분석 결과 지표 (Jupyter Notebook Output)
* [문서로 이동하기](./5_3_2_1_out14_23.8022_1.4218/)

각각의 쪼개진 폴드 조각별로 반환되는 로스 에러 값 배열들을 확인하고, 왜 편차가 존재하고 어떻게 평균내는 코드가 짜이는지 체감합니다.
