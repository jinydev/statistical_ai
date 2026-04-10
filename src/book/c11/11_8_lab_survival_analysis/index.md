---
layout: default
title: "index"
---

# 11.8 Lab: Survival Analysis 

In this lab, we perform survival analyses on three separate data sets. In Section 11.8.1 we analyze the `BrainCancer` data that was first described in Section 11.3. In Section 11.8.2, we examine the `Publication` data from Section 11.5.4. Finally, Section 11.8.3 explores a simulated call-center data set. 

We begin by importing some of our libraries at this top level. This makes the code more readable, as scanning the first few lines of the notebook tell us what libraries are used in this notebook. 

```
In [1]:frommatplotlib.pyplotimportsubplots
importnumpyasnp
importpandasaspd
fromISLP.modelsimportModelSpecasMS
fromISLPimportload_data
```

We also collect the new imports needed for this lab. 

```
In [2]:fromlifelinesimport\
(KaplanMeierFitter ,
CoxPHFitter)
fromlifelines.statisticsimport\
(logrank_test ,
multivariate_logrank_test)
fromISLP.survivalimportsim_time
```

---

## Sub-Chapters (하위 목차)

### 11.8.1 Brain Cancer Data (뇌종양 생존 모델링 파이썬 분석 파이프라인 수행 과정망)
* [문서로 이동하기](./11_8_1_brain_cancer_data/)

Lifelines 패키지의 카플란 피터 인스턴스 구축과 콕스 회귀 패키지를 활용해 그룹별 뇌종양 환자들의 치료 효과 플롯을 브라우저에 투영합니다.

### 11.8.2 Publication Data (의학 논문 출판 소요 시일 지연 중도절단 콕스 분석 랩 구현)
* [문서로 이동하기](./11_8_2_publication_data/)

긍정 논문/부정 논문으로 갈리는 연구 범주형 요인이 언제 사건(저널 채택)을 촉발시키는지 관측치를 적합하며 p-value를 파이썬 터미널에서 점검합니다.

### 11.8.3 Call Center Data (콜센터 대기고객 중도 이탈 포기 생존 기간 관측 데이터망 랩 테스트)
* [문서로 이동하기](./11_8_3_call_center_data/)

고객들이 상담원 통화가 될 때를 기다리다 일시 중단(censored event)한 대기 시간 데이터를 통계 파레토 모형 플롯과 묶어 분석해보는 재미난 응용 관측 연습을 합니다.
