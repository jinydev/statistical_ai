---
layout: default
title: "trans2"
---

# _5.3.2 Cross-Validation_ 
# _5.3.2 사이킷런의 은총: 파이썬 K-Fold 교차 검증 실습_

In theory, the cross-validation estimate can be computed for any generalized linear model.
머릿속 이론 빙빙 도는 소리만 따지자면, 그 무시무시한 '교차 검증 파편 에러 스코어 추정'은 사실 여러분이 맘에 드는 아무 GLM(일반화 선형 모델) 깡통 무기 하나를 쥐고서도 죄다 계산해 낼 수 있는 기본 이론 스킬이긴 합니다.

In practice, however, the simplest way to cross-validate in Python is to use `sklearn` , which has a different interface or API than `statsmodels` , the code we have been using to fit GLMs. 
하지만 구질구질한 실무 데이터 판에서, 특히 파이썬 키보드를 두들기며 이 미친 교차 뺑뺑이 검증을 가장 편하고 숨막히지 않게 조질 수 있는 치트키 툴은 다름 아닌 머신러닝계의 양대 산맥 **'사이킷런(`sklearn`)'** 패키지를 갖다 쓰는 겁니다. 근데 여기서 하나 거지 같은 에로사항이 하나 터지죠. 이 `sklearn` 플랫폼 툴은, 이때까지 우리가 주야장천 선형 회귀 배울 때 써먹던 기성품 도구 상자인 **`statsmodels`** 랑은 서로 API 설계도 언어도 달라서 "야, 니 무기 나한테 안 맞아!" 하며 부품(인터페이스) 아다리가 안 맞고 튕겨버린다는 비극입니다.

This is a problem which often confronts data scientists: “I have a function to do task _A_ , and need to feed it into something that performs task _B_ , so that I can compute _B_ ( _A_ ( _D_ )), where _D_ is my data.”
마치 애플 충전기를 갤럭시폰 똥구멍에 쑤셔 넣으려는 이 빡치는 상황! 현업 데이터 과학자들이 맨날 밤새며 쌍욕 하는 단골 멘트죠: **"아 씨, 내가 A 패키지 무기를 가져왔는데, 이걸로 굴러가는 B패키지의 최신 엔진 아가리 속에 데이터 D를 먹여서 $B(A(D))$ 미친 연산을 돌리고 싶어 미치겠는데 둘이 코드가 안 맞잖아!!!"**

When _A_ and _B_ don’t naturally speak to each other, this requires the use of a _wrapper_ .
저 A 툴과 B 공장 툴이 서로 외계어 시전을 하며 소통(speak to each other) 거부를 할 땐, 해답은 하나뿐입니다. 이 둘의 입과 귀 사이에 통역사 돼지코 변환 젠더를 끼워 넣는 것, 즉 이른바 **'래퍼(wrapper)'** 클래스를 소환해 덧씌워 써먹어야만 합니다.

In the `ISLP` package, we provide a wrapper, `sklearn_sm()` , that enables us to easily use the cross-validation tools of `sklearn` with models fit by `statsmodels` .
그래서 자비로운 이 책의 저자들이 자체 배포 패키지인 `ISLP` 창고 안에다가, 아주 달달한 돼지코 통역사 래퍼 함수인 **`sklearn_sm()`** 이란 치트 무기를 선사해 두었습니다. 이 요술 젠더만 꽂으면, 우리가 그간 익숙하게 써왔던 구형 `statsmodels` 무기 부품들로도 저 최첨단 `sklearn` 용병 기지들의 꿀 기능(교차 검증 스킬) 을 아주 매끄럽고 찰지게 편히 빨아(enables) 써먹을 수 있게 구원받습니다.

The class `sklearn_sm()` has as its first argument a model from `statsmodels` .
이 `sklearn_sm()` 통역사 모델 통구이 클래스의 작동법은 심플합니다. 맨 첫 번째 매개변수 입구에다가 그냥 아까 쓰던 그 구형 `statsmodels` 무기 깡통 녀석을 턱 하니 던져 주면 됩니다.

It can take two additional optional arguments: `model_str` which can be used to specify a formula, and `model_args` which should be a dictionary of additional arguments used when fitting the model.
심지어 이 통역사는 두 개의 추가 뽀찌 옵션도 받아주는데: "무기 부품에 공식 좀 달아줘!" 할 때 덧대는 `model_str` 끈이나, 아니면 이 무기 장전할 때 같이 들어갈 잡다한 특수 세팅 스펙들을 주머니 단위(dictionary) 로 몰아넣어 먹이는 `model_args` 들이 바로 그것입니다.

For example, to fit a logistic regression model we have to specify a `family` argument.
가령 예전에 배웠죠? 로지스틱 단검으로 스왑해서 적합을 빙빙 돌리고플 땐, 야생의 무기에 `family` 라는 세팅값을 무조건 이마에 써붙히고 돌려야 한다고 말입니다.

This is passed as `model_args={'family':sm.families.Binomial()}` . 
이 복잡한 룰은 통역사 돼지코를 탈 땐 딱 이렇게 포장해 건네주면 됩니다: `model_args={'family':sm.families.Binomial()}`. 참 쉽죠?

Here is our wrapper in action: 
자, 그럼 통역사 래퍼를 씌워 짝퉁 엔진을 구동하는(in action) 현장 씬을 보여드리죠:

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

## Sub-Chapters (하위 퀘스트 목차)

### 다중 분석 결과 지표 (Jupyter Notebook Output)
* [문서로 이동하기](./5_3_2_1_out14_23.8022_1.4218/)

데이터를 칼질해 나온 각각의 폴드(fold) 조각들마다 어떻게 널뛰는 에러 핏물 값들이 토해져 나오는지 배열로 뜯어보고, 이걸 피눈물 흘리며 하나의 평균으로 뭉뚱그려 최종 K-폴드 전투 진단 방어 에러 스코어로 매조지하는 눈물겨운 실황 코드를 엿봅니다.
