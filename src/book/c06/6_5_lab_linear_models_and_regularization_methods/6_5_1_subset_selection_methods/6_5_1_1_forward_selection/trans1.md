---
layout: default
title: "trans1"
---

# 전진 선택법 (Forward Selection)

We will apply the forward-selection approach to the `Hitters` data. We wish to predict a baseball player’s `Salary` on the basis of various statistics associated with performance in the previous year.
우리는 전진 선택(forward-selection) 접근법을 `Hitters` 데이터 세트에 적용해 볼 것입니다. 이 분석의 목표는 지난 시즌 다방면의 성적 실적과 관련된 다양한 통계 지표를 바탕으로 메이저리그 야구 선수의 현재 `연봉(Salary)`을 예측하는 것입니다.

First of all, we note that the `Salary` variable is missing for some of the players. The `np.isnan()` function can be used to identify the missing observations. It returns an array of the same shape as the input vector, with a `True` for any elements that are missing, and a `False` for non-missing elements. The `sum()` method can then be used to count all of the missing elements.
무엇보다도 먼저, 데이터 세트 내 일부 선수들의 `Salary` 변수 관측값이 누락되어 사라져 있음을 인지하게 됩니다. 결측치(missing observations)를 식별해 내기 위해 파이썬의 `np.isnan()` 함수를 사용할 수 있습니다. 이 함수는 입력 벡터와 동일한 형태의 배열을 반환하며, 누락된 요소에 대해서는 `True`를, 정상적으로 존재하는 데이터에 대해서는 `False`를 결과로 내보냅니다. 그런 다음 결측 요소의 총계 개수를 파악하기 위해 `sum()` 메서드를 연달아 사용할 수 있습니다.

```python
In [3]: Hitters = load_data('Hitters')
np.isnan(Hitters['Salary']).sum()
```

```
Out[3]: 59
```

We see that `Salary` is missing for 59 players. The `dropna()` method of data frames removes all of the rows that have missing values in any variable (by default — see `Hitters.dropna?` ).
결괏값 출력에 따르면 총 59명의 선수들에 대한 `Salary` 지표가 누락되어 비어 있음을 알 수 있습니다. 데이터 프레임 모듈의 `dropna()` 메서드는, 어떠한 변수 필드에서든 이렇게 누락된 결측값이 포함된 객체의 행(row)을 모조리 완전히 제거합니다 (기본 설정 시 - 자세한 사항은 `Hitters.dropna?` 구문 도움말을 참조하세요).

```python
In [4]: Hitters = Hitters.dropna()
Hitters.shape
```
