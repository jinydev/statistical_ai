---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6.3 Multiple Linear Regression](../3_6_3_multiple_linear_regression/trans2.html) | [3.6.4.1 List Comprehension >](3_6_4_1_list_comprehension/trans2.html)

# _3.6.4 Multivariate Goodness of Fit_

# 3.6.4 다변량 적합도 살펴보기: 내 요리는 얼마나 맛있을까?

We can access the individual components of `results` by name (`dir(results)` shows us what is available).
아까 우리가 `.summary()`라는 거대한 통계 성적표 전체 창을 띄워봤죠? 하지만 코딩으로 자동화를 하려면 그중 특정 점수 항목만 쏙 뽑아내야 할 때가 있습니다. 이럴 땐 반환받았던 `results` 봇따리 객체 변수 안에 내포된 자잘한 각 개별 하부 구성 요소들(components 파편들)을, 마치 서랍장 견출지 이름(by name) 부르듯 톡톡 건드려 곧장 개별 접근(access)해 빼내 차용해 올 수가 있습니다. (만약 서랍장에 무슨 이름들이 붙어 있는지 기억 안 나면? 파이썬 만능 탐색기 손전등 구문인 **`dir(results)`** 를 타건 실행해 보세요. 당장 어떤 이름표의 하위 가용 항목 서랍들이 도사리고 있는지 일목요연하게 그 목록들을 쫘악 펼쳐 보여(shows us) 줍니다!)

Hence `results.rsquared` gives us the $R^2$, and `np.sqrt(results.scale)` gives us the RSE.
그런 은혜로운 객체지향 원리를 살려 `results.rsquared` 라고 멤버 변수 구문을 대입해 주면 목표하던 우리 모델의 설명력 점수인 **$R^2$** 지수값만 달랑 단숨에 획득해 쥐여주며, 더불어 `np.sqrt(results.scale)` 수식 공식을 덧입혀 기용하면 우리가 바라고 바라던 잔차 표준 오차(오차가 평균적으로 얼마나 벌어져 있는지 알려주는) **RSE** 척도 결괏값 또한 척척 계산 도출해 우리 손에 기꺼이 제공(gives us)해 줍니다. 

Variance inflation factors (section 3.3.3) are sometimes useful to assess the effect of collinearity in the model matrix of a regression model.
한편, 아까 앞에서 귀가 닿도록 배웠던 일명 **'분산 팽창 계수(Variance inflation factors, VIF)'** (앞선 본문 3.3.3절 이론 참조) 지표 녀석은, 여러 변수들이 잔뜩 투입된 다중 회귀 모델(model matrix) 체제 내부에서 자기들끼리 너무 비슷해 똬리를 틀고 엉켜버린 **'다중 공선성(collinearity, 겹치는 재료 버그)'**의 몹쓸 여파와 악영향(effect) 추이를 이리저리 감별 진단 타진해 평가(assess)하고자 할 때 꽤나 매우 요긴하고 유용한(useful) 실무 잣대 도구로 애용되곤 합니다. (주무대의 쌍둥이 방해꾼을 찾아내는 일이죠.)

We will compute the VIFs in our multiple regression fit, and use the opportunity to introduce the idea of __.
나아가 바로 다음 실습 대목에서 우리는 방금 갓 산출해 낸 이 다중 회귀 적합(multiple regression fit) 국면 잣대를 도마 위에 올린 채로, 이들 문제의 제반 VIF 점수들을 일괄 파이썬 코드로 냅다 타건해 직접 연산 도출(compute)해 낼 터입니다! 게다가! 이 유익한 코드 구현 수행 과정의 특별 보너스 기회를 십분 틈타 차용함으로써 파이썬 문법 고유의 최고 사기 강력 스킬인 이른바 **'리스트 컴프리헨션(List Comprehension)'** 이라는 막강 개념 기조 역시 아주 덤으로 간략 친숙하게 소개(introduce)해 드릴까 합니다. (이거 모르면 파이썬 초보 티 팍팍 납니다!)

---


### List Comprehension (리스트 컴프리헨션)

분석 과정에서 여러 변수 명칭을 동적으로 조작할 때 쓰이는 강력한 리스트 반복문(List Comprehension) 문법 팁을 배웁니다.
이 기술 하나면 판다스 데이터프레임 내 칼럼들을 내 맘대로 손쉽게 척척 필터링할 때 두고두고 평생 써먹습니다!

---

## Sub-Chapters (하위 목차)


[< 3.6.3 Multiple Linear Regression](../3_6_3_multiple_linear_regression/trans2.html) | [3.6.4.1 List Comprehension >](3_6_4_1_list_comprehension/trans2.html)
