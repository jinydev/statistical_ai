---
layout: default
title: "index"
---

# 11.7 Additional Topics 

---

## Sub-Chapters (하위 목차)

### 11.7.1 Area Under the Curve for Survival Analysis (생존 모델의 AUC와 C-인덱스 평가지표 척도)
* [문서로 이동하기](./11_7_1_area_under_the_curve_for_survival_analysis/)

분류 모델의 흔한 지표인 ROC 유사도처럼, 생존율 기대 수치가 높은 대상자가 실제 생존 시간이 더 길게 맵핑되었는가를 재는 일치도 켤레(Harrell's C-index) 지표를 소개합니다.

### 11.7.2 Choice of Time Scale (시간 축 척도의 결정과 제약 한계치)
* [문서로 이동하기](./11_7_2_choice_of_time_scale/)

연구 시작 시간 기준일지, 사람 나이 기준일지, 혹은 절대 연도 기준일지에 따라 생존 모델 그래프 전개가 상이함을 보여주며, 적절한 T 설정 철학을 안내합니다.

### 11.7.3 Time-Dependent Covariates (시간 의존적 공변량 투입 요소 확장망)
* [문서로 이동하기](./11_7_3_time-dependent_covariates/)

관측 기간 도중에 혈압이나 약물 복용량 같은 속성(변수값)이 바뀔 경우 시간 의존성 변수로 세팅하여 위험률 함수에 유동성을 전파시키는 콕스 모형 패치 기법입니다.

### 11.7.4 Checking the Proportional Hazards Assumption (비례 위험 가정 엄격도 위배 추적 검토)
* [문서로 이동하기](./11_7_4_checking_the_proportional_hazards_assumption/)

모든 시점에 걸쳐 그룹 간 위험비가 일정한 배율이어야 한다는 콕스 방식의 유일한 전제(PH)가 맞는지 스코엔펠드 한계 잔차(Schoenfeld Residuals) 도표로 감지합니다.

### 11.7.5 Survival Trees (생존 숲 및 트리 분기 분석 혼합 모델)
* [문서로 이동하기](./11_7_5_survival_trees/)

이전 트리 장에서 단일 로그 분류 기준이 쓰인 걸 생존 로그 랭크 기준값으로 대체하여 의사결정 나무를 키우는 논파라메트릭 섭스텐스 분리 방식들을 살펴봅니다.
