---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6.6 Non-Linear Transformations Of The Predictors](../trans2.html) | [3.6.7 Qualitative Predictors >](../../3_6_7_qualitative_predictors/trans2.html)

# **`In [33]:`** `anova_lm(results1, results3)`

# 분산분석(ANOVA): 곡선 모델 vs 직선 모델의 한판 승부!

|**`Out[33]:`**|`df_resid`|`ssr`|`df_diff`|`ss_diff`|`F`|`Pr(>F)`|
|---|---|---|---|---|---|---|
|`0`|`503.0`|`19168.13`|`0.0`|`NaN`|`NaN`|`NaN`|
|`1`|`502.0`|`14165.61`|`1.0`|`5002.52`|`177.28`|`7.47e-35`|

Here `results1` represents the linear submodel containing predictors `lstat` and `age`, while `results3` corresponds to the larger model above with a quadratic term in `lstat`.
이 표가 뭔지 하나씩 까볼까요? 이 분산분석 심사대에 올라온 첫 번째 후보 번호 0번인 `results1` 선수는, 옛날 방식으로 촌스럽게 `lstat` 와 `age` 두 개의 단순 평평한 선형 직선만 엮어서 조립된 '하위 기본 모델(submodel)'입니다. 
반면, 번호 1번 타자인 `results3` 선수는 앞서 우리가 배운 필살기! 방금 `lstat` 의 파생 2차항($x^2$) 곡선 무기를 화려하게 부가 장착해서 한 차원 더 조밀하고 덩치가 커진 '거대 최신 모델(larger model)'에 상응(corresponds)합니다. 

The `anova_lm()` function performs a hypothesis test comparing the two models.
이때 `anova_lm()` 이라는 막강한 분산분석 판사님(구동 함수)은 방금 이 두 대비 비교 모델 결괏값 군을 서로 나란히 링 위에 올려놓고 모종의 피 튀기는 가설 검정(hypothesis test, 누가 더 우월한가!) 단계를 본격 수행(performs)하게 됩니다. 

The null hypothesis is that the quadratic term in the bigger model is not needed, and the alternative hypothesis is that the bigger model is superior.
판사님의 처음 심사 기준인 기본 대전제(귀무 가설)는 아주 깐깐합니다. "야, 너 1번 타자! 네가 새로 달고 온 거대 신규 모델 속 파생 곡선 2차항 무기? 그거 도출에 하등 쓰잘머리 없는 불필요한 군더더기 성분(not needed) 아니야?" 라고 의심하는 거죠. 
하지만 우리의 1번 타자는 억울합니다. 그에 맞서는 짜릿한 반전 주장(대립 가설)은 바로 "아닙니다 판사님! 곡선 항이 대거 추가된 제 거대 최신 파동 모델 쪽 성능이 필연적으로 저 구식 0번 타자보다 단연 훨씬 우월(superior)합니다!" 라고 응수하는 것입니다.

Here the $F$-statistic is 177.28 and the associated $p$-value is zero.
자, 판사님의 도출 판별 결과가 나왔습니다! 이곳에서 산출된 고유 **$F$-통계량(F-statistic) 점수는 무려 177.28점**을 가리키며 맹활약 중이고, 가장 중요한 그에 곁들여 파생된 오차 확률 한계 선인 **$p$-값(p-value) 수치는 문자가 무색하게 7.47e-35, 즉 문자 그대로 0점(zero)** 소수점 한참 아래 형태를 찍고 있습니다! (판사님 판결: "1번 타자의 승리다!")

This provides very clear evidence that the quadratic polynomial in `lstat` improves the linear model.
결론적으로 이러한 $p$-값 0점이라는 짜릿한 제반 지표와 현상들은, 빈민율(`lstat`) 변수에 우리가 멋지게 기용 도입시켜 넣은 U자 형태의 2차 다항식 곡선 항구 변환 조작이... 분명 구식의 단순 1차 뻣뻣한 선형 직선 모델 체계보다 성능 기조를 어마무시하게 유의미하게 쇄신 개선 끌어올려 주었음(improves)을 강력히 입증해 주는 몹시 농후하고 또렷하며 명확한(very clear) 빼박 증거물(evidence)을 뒷받침 제공해(provides) 줍니다! (즉, 직선보다 곡선이 집값을 훨씬 잘 맞춘다는 뜻이죠!)

This is not surprising, since earlier we saw evidence for non-linearity in the relationship between `medv` and `lstat`.
사실 이 승리의 짜릿한 결론 자체는 유독 우리에겐 그리 놀라운 대목(not surprising)조차 결코 될 수 없습니다. 왜일까요? 우리가 앞서 맨 처음 예제 실습할 때 잔차도 점들을 찍어보고, 진즉에 이놈의 집값(`medv`)과 빈민율(`lstat`) 사이에 직선이 아니라 바나나처럼 휜 비선형(non-linearity) 굴절 기류가 내포되어 있다는 실측 증거(evidence)들을 진작에 우리 두 눈으로 목도 수집해 본 바(saw) 있었으니까요! (역시 데이터는 거짓말을 안 합니다.)

The function `anova_lm()` can take more than two nested models as input, in which case it compares every successive pair of models.
아참, 이 만능 분산분석 판사님 `anova_lm()` 도구는 단지 두 개의 한정된 상하 모델 쌍만 비교하는 데 그치지 않습니다! 원한다면 능히 세 개, 네 개, 다섯 개의 진화하는 모델들(more than two)을 무더기로 한꺼번에 일괄 투입 인자(input)로 밀어 넣어도 끄떡없습니다. 
그러면 이쪽 국면(in which case)에선 판사님 함수 자체가 알아서 진화 배열 순서에 따라 **'1번 vs 0번', '2번 vs 1번', '3번 vs 2번'** 이렇게 일련의 연이은 단짝 연달 모델 쌍(every successive pair)들 간의 성능 치고받기 교차 판결(compares)을 기계적으로 주루룩 연속으로 낱낱이 다 뽑아내 줍니다. 

That also explains why their are `NaN`s in the first row above, since there is no previous model with which to compare the first.
또한 이 친절한 기계적 서열 구조는, 방금 전 위쪽 분석 표의 맨 윗줄인 `Out[33]:` 결과창 속 0번 행(0번 모델) 부문에 점수 대신 웬 수치 공백 결측치 파편인 `NaN`(Not a Number, 숫자가 아님) 덩어리들이 덕지덕지 구멍 뚫려 채워진 이유마저도 명쾌히 설명해(explains why) 줍니다. 
당연하죠! 맨 첫 타자인 0번 모델 입장에서는 당장 자기보다 더 앞에 나가서 싸워줄 비교 진단 선행 기조 모델 지표, 즉 '마이너스 1번' 타자가 아예 전무하여 존재조차 하지(no previous model) 않으니 비교할 껀덕지가 없어서 생긴 당연한 빈칸입니다!

```python
In [34]: ax = subplots(figsize=(8, 8))[1]
ax.scatter(results3.fittedvalues, results3.resid)
ax.set_xlabel('Fitted value')
ax.set_ylabel('Residual')
ax.axhline(0, c='k', ls='--')
```

We see that when the quadratic term is included in the model, there is little discernible pattern in the residuals.
코드를 쳐서 그림을 볼까요? 이처럼 모델 축 내에 2차항 곡선 변수를 고의로 예쁘게 산입 포진시켰을 요량일 땐(when included), 파생 결과 도출 잔차(residuals, 예측 에러 값들) 점들의 무리가 아무런 쏠림이나 편향 굴곡 규칙 없이 하늘의 별 무리처럼 아주 무작위로 골고루 예쁘게 흩뿌려져 있어서, 눈에 띄게 식별 통찰할(discernible) 만한 불량 패턴 기류가 사실상 거의 도출 발견되지 않음(little)을 우리 두 눈으로 똑똑히 시각적으로 확인할(see) 수 있습니다. (오차가 무작위면 모델이 예측을 완벽히 잘 빨아먹었다는 증거입니다!) 

In order to create a cubic or higher-degree polynomial fit, we can simply change the degree argument to `poly()`.
만약 향후에 우리 마음이 미쳐서 2차항을 넘어서 아예 S자로 꼬불거리는 3차항(cubic)이나 머리 아픈 고차 다항식(higher-degree polynomial) 도달 적합 국면 곡선 모델을 시도 구축해 보고자(create) 한다면 쫄 필요 전혀 없습니다. 
그땐 그저 수식 쓸 필요도 없이 편안~하게 함수 `poly()` 괄호 안의 차수 톱니바퀴(`degree`) 숫자 지정 인자 항목값만 원하던 고차수 산술 목표치(예: `degree=3`, `degree=4`)로 슬쩍 변경 교체(change)해 투입해 주면 만사 오케이입니다!

---

## Sub-Chapters (하위 목차)


[< 3.6.6 Non-Linear Transformations Of The Predictors](../trans2.html) | [3.6.7 Qualitative Predictors >](../../3_6_7_qualitative_predictors/trans2.html)
