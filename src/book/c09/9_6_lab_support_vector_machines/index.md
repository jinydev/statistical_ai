---
layout: default
title: "index"
---

# 9.6 Lab: Support Vector Machines 

In this lab, we use the `sklearn.svm` library to demonstrate the support vector classifier and the support vector machine. We import some of our usual libraries. 

```
In [1]:importnumpyasnp
frommatplotlib.pyplotimportsubplots,cm
importsklearn.model_selectionasskm
fromISLPimportload_data,confusion_table
```

We also collect the new imports needed for this lab. 

```
In [2]:fromsklearn.svmimportSVC
fromISLP.svmimportplotasplot_svm
fromsklearn.metricsimportRocCurveDisplay
```

We will use the function `RocCurveDisplay.from_estimator()` to produce `RocCurve` several ROC plots, using a shorthand `roc_curve` . 

```
Display.from_
estimator()
```

```
In [3]:roc_curve=RocCurveDisplay.from_estimator#shorthand
```

---

## Sub-Chapters (하위 목차)

### 9.6.1 Support Vector Classifier (선형 SVC 튜닝 파이썬 실습)
* [문서로 이동하기](./9_6_1_support_vector_classifier/)

선형 `kernel='linear'` 환경하에서 비용 C 패널티 속성 `cost` 파라미터의 그리드 서치(Grid Search CV)를 이용한 최적 마진 폭 튜닝 능력을 배양합니다.

### 9.6.2 Support Vector Machine (비선형 방사형/다항 커널 SVM 파이썬 테스트)
* [문서로 이동하기](./9_6_2_support_vector_machine/)

마름모나 구멍 난 데이터 군집 구조 등에 대해 가우시안 방사상 커널(`rbf`) 속성을 주입하고 동심원 기반의 경계를 렌더링하는 코드를 짜봅니다.

### 9.6.3 ROC Curves (ROC 분류 평가 곡면 직접 구현 실습)
* [문서로 이동하기](./9_6_3_roc_curves/)

훈련된 SVC 모델로부터 클래스 확신 예측 마진 값(`decision_function`)들을 추출해 파이썬에서 민감도 평가를 위한 2차원 성능 플롯 ROC 커브를 그립니다.

### 9.6.4 SVM with Multiple Classes (클래스 3개 이상 공간에 대한 파이썬 다중 SVM 지원 스크립트)
* [문서로 이동하기](./9_6_4_svm_with_multiple_classes/)

클래스 속성을 3종류 이상으로 변형한 관측치 구조를 라이브러리에 입력하여 파이썬 사이킷 툴이 어떻게 OVO 기능을 자가 소화해내는지 확인합니다.

### 9.6.5 Application to Gene Expression Data (생물 유전자 무제한 차원 발현 데이터 진단 랩)
* [문서로 이동하기](./9_6_5_application_to_gene_expression_data/)

관측치는 60개인데 유전 피처는 무려 수천 개단위인 초고차원 의료데이터를 로드해 선형 마진분류에 태워도 완벽 예측이 보장되는 SVM의 한계점과 유효 방해물을 관찰합니다.
