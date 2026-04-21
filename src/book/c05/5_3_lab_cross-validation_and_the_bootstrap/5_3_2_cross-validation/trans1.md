---
layout: default
title: "trans1"
---

# 5.3.2 Cross-Validation
# 5.3.2 교차 검증

In theory, the cross-validation estimate can be computed for any generalized linear model. In practice, however, the simplest way to cross-validate in Python is to use `sklearn`, which has a different interface or API than `statsmodels`, the code we have been using to fit GLMs. 
이론론적으론(In theory) 교차 검증의 예측 지표는 일반화 선형 모델(generalized linear model, GLM) 범주의 그 어떤 포맷에 대해서든 무리 없이 셈 연산이 수행 계산될 수 있습니다. 그러나 현실 실무 진영(In practice)에서 파이썬을 기반으로 삼아 교차 테스트를 진행하는 가장 단순 명쾌한 수단은 `sklearn` 을 가져다 채용하는 일인데, 이 소프트웨어는 우리가 그동안 GLMs 체계를 끼워 맞추기(fit) 위해 통상 사용 고수해오던 `statsmodels` 패키지와는 상이한 이질적 인터페이스 체계, 즉 별도의 API를 보유 내재하고 있습니다.

This is a problem which often confronts data scientists: “I have a function to do task _A_, and need to feed it into something that performs task _B_, so that I can compute $B(A(D))$, where _D_ is my data.” When _A_ and _B_ don’t naturally speak to each other, this requires the use of a _wrapper_ . In the `ISLP` package, we provide a wrapper, `sklearn_sm()`, that enables us to easily use the cross-validation tools of `sklearn` with models fit by `statsmodels`. The class `sklearn_sm()` has as its first argument a model from `statsmodels`. It can take two additional optional arguments: `model_str` which can be used to specify a formula, and `model_args` which should be a dictionary of additional arguments used when fitting the model. For example, to fit a logistic regression model we have to specify a `family` argument. This is passed as `model_args={'family':sm.families.Binomial()}` . 
이 지점이 곧 예로부터 숱한 데이터 과학자 실무진이 흔히 마주 직면하는(confronts) 딜레마성 문제입니다: "나는 우선 미션 _A_ 를 도맡아 구동 처리하는 기능 함수를 보유 중이고, 이걸 이내 또 다른 선행 분리 미션 _A_ 를 수행 구동시킨 파생 물질 안에 부어 넣어 투입(feed)해야 하는 상황인데, 이는 최종적으로 본인의 기초 소재 데이터 _D_ 를 기반으로 궁극의 연쇄 함수상 $B(A(D))$ 의 셈 결과값을 뽑아 계산(compute) 할 목적 때문이라네." 여기서 막상 도구 _A_ 진영과 도구 _B_ 양 진영 체계가 서로 맞물려 자연스런 상호 통신 회화(speak to each other) 호환 기작을 못 일으키고 엇박자를 낼 때, 이는 결국 우리에게 껍데기 외장 연결 코드인 이른바 래퍼(_wrapper_) 의 조달 사용을 종용 요구(requires)하게 만듭니다. 우리는 `ISLP` 패키지 구성 안무의 일환으로 한 가지 자체 래퍼 도구인 `sklearn_sm()` 을 제공 지급(provide)하고 있으며, 이것의 작동 능률 체계는 우리가 `statsmodels` 으로 피팅시켜 짠 회귀 모델들을 별 무리 없이 `sklearn` 내부 교차 검증 검사 도구들과 부드럽게 병합 연계시켜 운용(use)하는 걸 손쉽게 가능 토록 지원(enables)합니다. 이 부류 식별 클래스 객체 단위인 `sklearn_sm()` 은 내부의 첫 관문적 인자(first argument) 요소로서 통상 `statsmodels` 출신의 모델 코어를 지명 접수합니다. 추가적으로 이것은 보조 편의 선택 조율 인자 2개를 선택 수용(take)할 능역이 존재하는데: 곧 전개 형성 수식(formula)을 콕 집어 명시 지목할(specify) 때 등용 활용되는 `model_str` 과, 또 한편으론 타깃 모델의 훈련 구동 적합화를 시도 단행할 요량 시에만 임시적 편의 도모차 요구 투입되는 추가(additional) 보충성 인수들의 사전 묶음 자료형(dictionary) 기구여야만 하는, 저 이른바 `model_args` 가 바로 그것입니다. 일례를 들자면(For example), 한 로지스틱 예측함 모델 계통을 온전히 구동 피팅 맞추기 위해, 우리들은 불가피하게 `family` 라는 이름의 세부 지정항 단위체를 반드시 고정해 명시해야(specify) 할 처절한 소요성이 제기됩니다. 이 현안 처리는 코드상에서 `model_args={'family':sm.families.Binomial()}` 패키지 구성을 투과 관통(passed)시키는 방식 문법으로 성사 도달됩니다.

Here is our wrapper in action: 
아래 보이는 시뮬레이션 장면이 해당 우리 래퍼의 구체적 운용 작용(in action) 현장입니다:

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
* [문서로 이동하기](./5_3_2_1_out14_23.8022_1.4218/trans1.html)
