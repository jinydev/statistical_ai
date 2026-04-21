---
layout: default
title: "trans1"
---

[< 3.6.6 Non-Linear Transformations Of The Predictors](../trans1.html) | [3.6.7 Qualitative Predictors >](../../3_6_7_qualitative_predictors/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# **`In [33]:`** `anova_lm(results1, results3)`

# 분산분석(ANOVA) 처리 결과

|**`Out[33]:`**|`df_resid`|`ssr`|`df_diff`|`ss_diff`|`F`|`Pr(>F)`|
|---|---|---|---|---|---|---|
|`0`|`503.0`|`19168.13`|`0.0`|`NaN`|`NaN`|`NaN`|
|`1`|`502.0`|`14165.61`|`1.0`|`5002.52`|`177.28`|`7.47e-35`|

Here `results1` represents the linear submodel containing predictors `lstat` and `age`, while `results3` corresponds to the larger model above with a quadratic term in `lstat`.

작금의 위 도출 수치 분석표에서 첫 번째 `results1` 지표는 변수 `lstat` 와 `age` 두 가지만을 엮어 조립된 단순 선형 기본 하위 모델(submodel) 객체를 대변(represents)하는 반면, 그에 견주는 후순위 `results3` 항목은 앞서 방금 `lstat` 의 파생 2차항(quadratic term) 변환 지수를 부가 접목해 세운 한 차원 더 조밀하고 덩치가 큰(larger model) 쇄신 모델 객체에 정확히 부합 상응(corresponds)합니다. The `anova_lm()` function performs a hypothesis test comparing the two models.

이때 `anova_lm()` 구동 함수 체제는 방금 이 두 대비 비교 모델 결괏값 군을 서로 나란히 견주어 맞대어 놓고 모종의 가설 검정(hypothesis test) 단계를 본격 수행(performs)하게 됩니다. The null hypothesis is that the quadratic term in the bigger model is not needed, and the alternative hypothesis is that the bigger model is superior.

여기서 설정된 귀무 가설(null hypothesis)의 요체는, 비대해진 저 거대 신규 모델 속 파생 2차항이 도출에 하등 쓰잘머리 없는 불필요한 군더더기 성분(not needed)이란 논지에 서며, 이에 맞서는 대립 가설(alternative hypothesis)의 축은 뭇 항목이 대거 추가된 거대 모델 쪽 성능이 필연 이전보다 단연 우월(superior)하다는 쪽을 지지합니다. Here the $F$-statistic is 177.28 and the associated $p$-value is zero.

도출표 판별 결과 이곳에서 산출된 고유 $F$-통계량(F-statistic) 점수는 177.28점을 가리키며, 그에 얽혀 파생 결부된(associated) 오차 한계 $p$-값(p-value) 수치는 문자 그대로 소수점 이하 거의 제로(zero) 형태를 찍고 있습니다. In this case the $F$-statistic is the square of the $t$-statistic for the quadratic term in the linear model summary for `results3` — a consequence of the fact that these nested models differ by one degree of

> 13Actually, `poly()` is a wrapper for the workhorse and standalone function `Poly()` that does the work in building the model matrix.

126 3. Linear Regression

freedom. This provides very clear evidence that the quadratic polynomial in `lstat` improves the linear model.

결론적으로 이러한 제반 지표와 현상들은, `lstat` 변수 차원에 기용 도입시켜 넣은 이차 다항식 항구 변환 조작이 분명 기존 1차 선형 모델 체계의 성능 기조를 유의미하게 쇄신 개선 끌어올려 주었음(improves)을 강력히 입증해 주는 몹시 농후하고 또렷하며 명확한(very clear) 시사 증거물(evidence)을 뒷받침 제공해(provides) 줍니다. This is not surprising, since earlier we saw evidence for non-linearity in the relationship between `medv` and `lstat`.

사실 이 결론 자체는 그리 유달리 새삼스럽거나 놀라운 대목(not surprising)조차 결코 될 수 없는데, 우린 이미 앞선 예제 탐구 행보 과정에서 진즉에 `medv` 변수와 `lstat` 두 기준 변수 사이 관계망 역학 축로에 모종의 비선형(non-linearity) 곡선 굴절 기류가 내포 동반 얽혀 있음을 입증하는 강력한 의도 징후 징후와 실측 증거(evidence)들을 뭇 발견해 목도 수집해 본 바(saw) 십분 있었기 때문입니다.

The function `anova_lm()` can take more than two nested models as input, in which case it compares every successive pair of models.

이 `anova_lm()` 함수 도구 규격은 단지 두 개의 한정된 상하 내포 중첩 모델(nested models) 쌍만을 투입물로 취합(take)하는 데 머물지 않고 능히 두 개 초과 가짓수 분량(more than two)을 무더기 일괄 투입 인자(input)로 밀어 넣어 거뜬히 받아들일 수 있으며, 이처럼 연쇄 가짓수가 늘어난 무더기 산입 사례의 국면(in which case)에선 함수 자체가 내부적으로 자체 배열 순서 계통에 편입된 모든 여느 일련의 연이은 단락 단짝 연달 모델 쌍(every successive pair)들 간의 성능 지표 우위 전선을 기계적으로 연속 낱낱이 줄지어 교차 비교 편차 비교 대조 연산(compares)해 냅니다. That also explains why their are `NaN`s in the first row above, since there is no previous model with which to compare the first.

또한 이 구조적 사실은 방금 전 위쪽 도출표 산출 결과상의 맨 꼭대기 첫 파생 행(first row) 부문에 지표 결괏값 대신 수치 공백 결측치 파편인 `NaN`(Not a Number) 덩어리들이 즐비하게 포진 채워진 이유마저도 명쾌히 뒷받침 설명해(explains why) 주는데, 맨 선두 0번 모델 입장에서는 당장 애당초 뒤돌아서 견주며 비교 진단 차출 대조해 볼(compare) 여느 그 어떠한 더 앞선 선행 기조 모델 지표가 도무지 앞 차례에 한 차원도 아예 전무하여 존재조차 하지(no previous model) 않기 기인한 연유(since)입니다.

```
In [34]: ax = subplots(figsize=(8, 8))[1]
ax.scatter(results3.fittedvalues, results3.resid)
ax.set_xlabel('Fitted value')
ax.set_ylabel('Residual')
ax.axhline(0, c='k', ls='--')
```

We see that when the quadratic term is included in the model, there is little discernible pattern in the residuals.

이처럼 모델 축 내에 2차항(quadratic term) 지수 변수를 고의로 산입 포진시켰을 요량일 땐(when included), 파생 결과 도출 잔차(residuals) 점들의 군집 궤적 분포 분포양상 내에서 눈에 띄게 식별 통찰 감지해 낼(discernible) 만한 도드라진 일련의 유의미한 편향 굴곡 패턴 기류가 사실상 거의 눈 씻고 찾아봐도 도출 발견되지 않음(little)을 우리 두 눈으로 똑똑히 확인할(see) 수 있습니다. In order to create a cubic or higher-degree polynomial fit, we can simply change the degree argument to `poly()`.

만약 향후에 우리 임의로 이 수준을 더 넘어서서, 아예 3차항(cubic) 도출을 필두로 더 복잡 다변 단조로운 고차 다항식(higher-degree polynomial) 도달 적합 국면을 시도 창설 구축 도출해 보고자(create) 한다면, 그땐 그저 별반 무리 없이 편히 함수 `poly()` 호출 투입부의 급수 차수(`degree`) 지정 인자(argument) 항목 지표만을 원하던 타깃 고차수 목표치로 살짝 변경 갱신 지정 교체 설정(change)해 차출 투입해 주면 그만입니다.

---

## Sub-Chapters (하위 목차)


[< 3.6.6 Non-Linear Transformations Of The Predictors](../trans1.html) | [3.6.7 Qualitative Predictors >](../../3_6_7_qualitative_predictors/trans1.html)
