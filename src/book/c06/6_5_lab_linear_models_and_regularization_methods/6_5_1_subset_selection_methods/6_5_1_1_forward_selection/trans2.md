---
layout: default
title: "trans2"
---

# 전진 선택법 알고리즘 파이썬 실습 (Forward Selection)

We will apply the forward-selection approach to the `Hitters` data. We wish to predict a baseball player’s `Salary` on the basis of various statistics associated with performance in the previous year.
이번 실습에선 데이터 사이언스의 단골 손님인 메이저리그 야구 데이터 `Hitters` 세트를 콘솔 무대 위로 올려 전진 선택(forward-selection) 알고리즘 기법을 아주 매끄럽게 적용해 보는 코딩 실습을 진행합니다. 우리의 분석 미션 타겟은 지난 정규 시즌에 선수들이 그라운드에서 뿜어낸 다방면의 성적 실적과 관련된 각종 화려한 통계 지표 정보들을 머신러닝 모형에 쑥쑥 집어넣어, 해당 프로 야구 선수가 구단과 계약할 현재 알짜배기 진짜 `연봉(Salary)` 가치를 기가 막히게 족집게처럼 예측 관통해 내는 것입니다.

First of all, we note that the `Salary` variable is missing for some of the players. The `np.isnan()` function can be used to identify the missing observations. It returns an array of the same shape as the input vector, with a `True` for any elements that are missing, and a `False` for non-missing elements. The `sum()` method can then be used to count all of the missing elements.
무엇보다도 데이터 분석의 시작은 전처리(preprocessing) 청소 작업입니다. 판다스 프레임을 까보면 애석하게도 일부 타자 선수들의 수입 척도인 `Salary` 변수 관측값이 뻥 뚫려 누락되어 비어있는 결측치 빵꾸 상황을 단번에 인지하게 됩니다. 이 거슬리는 결측치(missing observations) 구멍 난 조각들을 체계적으로 추적해 솎아내기 위해 우리는 넘파이의 강력한 탐색 기능인 `np.isnan()` 함수 툴킷을 가동합니다. 모델이 이 녀석을 장착해 데이터 객체를 스캔하면, 배열(array) 내장 모듈의 객체 판독 엔진 메커니즘이 원본 인풋 벡터와 동일한 배열 복사판을 반환하면서 누락되어 사라진 문제아가 스캔된 오답 요소 객동 좌표 스팟엔 `True` 경고 알람을 울려 뱉고 은밀히 찾아내며, 반대로 멀쩡하게 수치가 존재 보존된 건강한 데이터 객체 좌표 위치엔 `False` 안정 사인 패스 결과값을 내보내어 안전 확인 스캔 판독 통과를 알려 줍니다. 그 탐지망 뒤에 연이어 간단하게 집계 파이프 명령어 기법인 `sum()` 메서드 계산 통계 함수 갈고리를 붙여 띄워 연결해주면, 저 `True` 경고가 울렸던 오류 발생 타겟 결측 요소 객체들의 총계 통계 합산 개수를 순식간에 싹쓸이 카운팅 검출 스캔 집계 파파악 해내는 기적의 편의를 발휘할 수 있습니다.

```python
In [3]: Hitters = load_data('Hitters')
np.isnan(Hitters['Salary']).sum()
```

```
Out[3]: 59
```

We see that `Salary` is missing for 59 players. The `dropna()` method of data frames removes all of the rows that have missing values in any variable (by default — see `Hitters.dropna?` ).
스캔 결과창 아웃풋을 살피니 무려 거금인 수입 연봉 지표 필드인 `Salary` 컬럼이 누락되어 뻥 뚫린 채 유실되어버린 황당한 선수가 자그마치 59명이나 무더기로 발생 포착 발견되었음을 알 수 있습니다. 이 상태론 원활한 회귀 분석 지표 도출 모델링 가동 진행 자체가 물리 체제상 불가하므로, 판다스 데이터 프레임 모듈의 청소 전문 필터 함수 체제인 `dropna()` 메서드를 호출 구동시켜 줍니다. 이 청소기는 작동을 개시하는 즉시 데이터가 속한 어떠한 척도 변수 필드에서든 이렇게 누락된 결측값 구멍이 하나라도 포함 발각 발견 확인된 객체의 가로열(row, 데이터 행) 전체를 아주 깔끔하게 일괄 모조리 가차 없이 날려 삭제 파쇄 제거해 줍니다 (기본 내장 설정 옵션 기준이므로 통제 파라미터 제원을 조정하고 싶다면 꼭 도움말 명령어 `Hitters.dropna?` 구문 쿼리를 타이핑 쳐서 상세 제어 문서를 참고하여 파악해 보세요).

```python
In [4]: Hitters = Hitters.dropna()
Hitters.shape
```
