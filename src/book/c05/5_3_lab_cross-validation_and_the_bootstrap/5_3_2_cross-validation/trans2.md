---
layout: default
title: "trans2"
---

# 5.3.2 Cross-Validation
# 5.3.2 래퍼(Wrapper)의 마법: 패키지 대통합 작전! (교차 검증)

In theory, the cross-validation estimate can be computed for any generalized linear model. In practice, however, the simplest way to cross-validate in Python is to use `sklearn` , which has a different interface or API than `statsmodels` , the code we have been using to fit GLMs. 
입 아프게 떠들었던 이론(In theory) 에선, 선형이든 커브든 어떤 모델을 가져와도 교차 검증 점수를 척척 계산해야 정상이죠? 하지만 실전 코딩 판(In practice) 의 현실은 시궁창입니다. 파이썬에서 교차 검증을 가장 편하게 돌리려면 싸이킷런 `sklearn` 패키지 형님을 모셔 와야 하는데, 정작 우리가 방금 전까지 회귀 모델 뼈대를 깎던 공구는 `statsmodels` 패키지였습니다. 문제는 이 두 회사의 장비 규격, 즉 버튼 조작법(API) 이 달라서 호환이 안 된다는 거죠. 애플 충전기로 갤럭시 충전하려는 꼴입니다!

This is a problem which often confronts data scientists: “I have a function to do task _A_ , and need to feed it into something that performs task _B_ , so that I can compute $B(A(D))$, where _D_ is my data.” When _A_ and _B_ don’t naturally speak to each other, this requires the use of a _wrapper_ . In the `ISLP` package, we provide a wrapper, `sklearn_sm()` , that enables us to easily use the cross-validation tools of `sklearn` with models fit by `statsmodels` . The class `sklearn_sm()` has as its first argument a model from `statsmodels` . It can take two additional optional arguments: `model_str` which can be used to specify a formula, and `model_args` which should be a dictionary of additional arguments used when fitting the model. For example, to fit a logistic regression model we have to specify a `family` argument. This is passed as `model_args={'family':sm.families.Binomial()}` . 
이게 바로 툭하면 해커들을 야근하게 만드는 코딩계의 망할 고질병(confronts) 입니다. "난 A 작업을 하는 믹서기를 갖고 있는데, 여기서 나온 주스를 B라는 빵 기계에 넣어야 돼. 내 피 같은 데이터 D로 $B(A(D))$ 케이크를 만들고 싶다고!" 근데 A와 B 기계가 서로 언어가 달라서 대화를 안 하네(don’t naturally speak)? 이때 구세주처럼 등장하는 게 바로 통역사 젠더, 즉 **래퍼(_wrapper_)** 기술입니다. 저자 형님들이 우리 불쌍한 학생들을 위해 `ISLP` 패키지 안에 `sklearn_sm()` 이라는 통역사 젠더를 미리 깎아서 넣어놨습니다(provide). 이 통역사 하나면 `statsmodels` 에서 만든 모델을 `sklearn` 의 교차 검증 기계에 쏙 꽂아서 돌릴 수(easily use) 있죠! 이 꿀템 `sklearn_sm()` 젠더의 앞구멍(첫 번째 인자) 에 `statsmodels` 모델을 물려주고 나면, 뒤에 추가로 조절할 수 있는 스위치(optional arguments) 2개가 더 있습니다. 모델의 뼈대 수식을 꽂아줄 `model_str` 구멍과, "이 모델 돌릴 땐 이런 옵션도 꼭 켜주세요~" 하고 잡다한 환경설정 파우치(딕셔너리) 를 달아줄 `model_args` 구멍이죠. 예를 들어(For example) 까다로운 로지스틱 회귀 모델을 구동할 땐 족보(`family`) 세팅이 필수적인데, 이때 통역사에게 `model_args={'family':sm.families.Binomial()}` 모양의 파우치를 슬쩍 건네주면 끝입니다. 참 쉽죠?

Here is our wrapper in action: 
자, 백문이 불여일타! 우리 통역사 래퍼 형님의 실전 접지(in action) 현장을 구경하시죠:

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
* [문서로 이동하기](./5_3_2_1_out14_23.8022_1.4218/trans2.html)
