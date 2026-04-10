---
layout: default
title: "index"
---

# 8.3 Lab: Tree-Based Methods 

We import some of our usual libraries at this top level. 

```
In [1]:importnumpyasnp
importpandasaspd
frommatplotlib.pyplotimportsubplots
fromstatsmodels.datasetsimportget_rdataset
importsklearn.model_selectionasskm
fromISLPimportload_data,confusion_table
fromISLP.modelsimportModelSpecasMS
```

We also collect the new imports needed for this lab. 

```
In [2]:fromsklearn.treeimport(DecisionTreeClassifierasDTC,
DecisionTreeRegressorasDTR,
plot_tree,
export_text)
fromsklearn.metricsimport(accuracy_score ,
log_loss)
fromsklearn.ensembleimport\
(RandomForestRegressorasRF,
GradientBoostingRegressorasGBR)
fromISLP.bartimportBART
```

8.3 Lab: Tree-Based Methods 355 

---

## Sub-Chapters (하위 목차)

### 8.3.1 Fitting Classification Trees (분류 트리 적합 및 시각화 실습)
* [문서로 이동하기](./8_3_1_fitting_classification_trees/)

`DecisionTreeClassifier` 알고리즘을 소환하고, 데이터를 쪼개는 계층 구조망을 파이썬 `plot_tree` 함수로 시각화하여 화면에 그려봅니다.

### 8.3.3 Bagging and Random Forests (랜덤포레스트 앙상블 파이썬 피팅 실습)
* [문서로 이동하기](./8_3_3_bagging_and_random_forests/)

`RandomForestRegressor` 객체를 불러온 상태에서 노드 변수 개수(Max features)를 조절하는 방식으로 배깅과 포레스트를 번갈아 구동하는 법을 익힙니다.

### 8.3.4 Boosting (그라디언트 부스팅 파이썬 실습)
* [문서로 이동하기](./8_3_4_boosting/)

`GradientBoostingRegressor`를 탑재하여 트리 갯수 및 학습률(Learning Rate)를 인자로 넣으면서 과적합 없이 손실을 낮추는 부스팅 조작을 다룹니다.

### 8.3.5 Bayesian Additive Regression Trees (BART 패키지 운용 실습)
* [문서로 이동하기](./8_3_5_bayesian_additive_regression_trees/)

BART 전용 통계 패키지를 로드하여 MCMC 깁스 샘플링 기반의 트리를 파이썬 워크플로우에 통합 적용해 보는 경험적 코딩입니다.
