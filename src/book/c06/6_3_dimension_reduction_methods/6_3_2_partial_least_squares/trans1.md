---
layout: default
title: "trans1"
---

# 6.3.2 부분 최소 제곱법 (Partial Least Squares)

The PCR approach that we just described involves identifying linear combinations, or _directions_, that best represent the predictors $X_1, \ldots, X_p$. These directions are identified in an _unsupervised_ way, since the response $Y$ is not used to help determine the principal component directions. That is, the response does not _supervise_ the identification of the principal components. Consequently, PCR suffers from a drawback: there is no guarantee 
우리가 방금 설명한 PCR 접근법은 예측 변수 $X_1, \ldots, X_p$를 가장 잘 나타내는 선형 결합, 즉 _방향(directions)_ 을 식별하는 과정을 수반합니다. 이러한 방향들은 주성분 방향을 결정하는 데 반응 변수 $Y$가 사용되지 않기 때문에 _비지도(unsupervised)_ 방식으로 식별됩니다. 즉, 반응 변수는 주성분 식별 과정을 _지도(supervise)_ 하지 않습니다. 결과적으로 PCR은 한 가지 단점을 갖게 됩니다. 

> ^8 More details can be found in Section 3.5 of _The Elements of Statistical Learning_ by Hastie, Tibshirani, and Friedman.
> ^8 더 자세한 내용은 Hastie, Tibshirani, Friedman 저, _The Elements of Statistical Learning_ 의 3.5 절에서 찾을 수 있습니다.

![Figure 6.21](./img/6_21.png)

**FIGURE 6.21.** _For the advertising data, the first PLS direction (solid line) and first PCR direction (dotted line) are shown._ 
**그림 6.21.** _광고 데이터에 대해 첫 번째 PLS 방향(실선)과 첫 번째 PCR 방향(점선)이 표시되어 있습니다._

that the directions that best explain the predictors will also be the best directions to use for predicting the response. Unsupervised methods are discussed further in Chapter 12. 
그 단점은 예측 변수를 가장 잘 설명하는 방향이 반응 변수를 예측하는 데 동등하게 가장 좋은 방향일 것이라는 보장이 없다는 것입니다. 비지도 학습 방법론에 대해서는 12장에서 더 자세히 논의합니다.

We now present _partial least squares_ (PLS), a _supervised_ alternative to PCR. Like PCR, PLS is a dimension reduction method, which first identifies a new set of features $Z_1, \ldots, Z_M$ that are linear combinations of the original features, and then fits a linear model via least squares using these $M$ new features. But unlike PCR, PLS identifies these new features in a supervised way—that is, it makes use of the response $Y$ in order to identify new features that not only approximate the old features well, but also that _are related to the response_. Roughly speaking, the PLS approach attempts to find directions that help explain both the response and the predictors. 
이제 우리는 PCR에 대한 _지도(supervised)_ 대안인 _부분 최소 제곱법(partial least squares, PLS)_ 을 소개합니다. PCR과 마찬가지로 PLS는 원래 원본 특성들의 선형 결합인 새로운 특성 세트 $Z_1, \ldots, Z_M$을 먼저 식별한 다음, 이 새로운 $M$개의 특성들을 사용하여 최소 제곱법을 통해 선형 모델을 적합시키는 차원 축소 방법입니다. 그러나 PCR과 달리, PLS는 반응 변수 $Y$를 활용하여 기존 예측 특성들을 잘 근사할 뿐만 아니라 _반응 변수와 관련된(related to the response)_ 새로운 특성들을 식별해 내는 지도적 방식으로 이루어집니다. 대략적으로 말하면, PLS 접근법은 반응 변수와 예측 변수 쌍방을 모두 잘 설명하는 데 도움이 되는 방향을 찾으려 시도합니다.

We now describe how the first PLS direction is computed. After standardizing the $p$ predictors, PLS computes the first direction $Z_1$ by setting each $\phi_{j1}$ in (6.16) equal to the coefficient from the simple linear regression of $Y$ onto $X_j$. One can show that this coefficient is proportional to the correlation between $Y$ and $X_j$. Hence, in computing $Z_1 = \sum_{j=1}^p \phi_{j1} X_j$, PLS places the highest weight on the variables that are most strongly related to the response. 
이제 첫 번째 PLS 방향이 어떻게 계산되는지 설명합니다. $p$개의 예측 변수를 모두 표준화한 후, PLS는 $Y$를 $X_j$ 상에 맞춘 단순 선형 회귀에서 도출된 계수와, 방정식 (6.16)에서의 각 $\phi_{j1}$ 값을 일치하게 설정함으로써 첫 번째 방향인 $Z_1$을 계산합니다. 이 계수가 $Y$와 $X_j$ 사이의 상관관계에 비례한다는 것을 증명할 수 있습니다. 따라서 $Z_1 = \sum_{j=1}^p \phi_{j1} X_j$를 계산할 때, PLS는 반응 변수와 가장 강하게 연관된 변수들에게 가장 높은 지표 가중치를 부여하게 됩니다.

Figure 6.21 displays an example of PLS on a synthetic dataset with Sales in each of 100 regions as the response, and two predictors; Population Size and Advertising Spending. The solid green line indicates the first PLS direction, while the dotted line shows the first principal component direction. PLS has chosen a direction that has less change in the `ad` dimension per unit change in the `pop` dimension, relative to PCA. This suggests that `pop` is more highly correlated with the response than is `ad`. The PLS direction does not fit the predictors as closely as does PCA, but it does a better job explaining the response. 
그림 6.21은 100개 지역 각각의 판매량(Sales)을 반응 변수로, 인구 규모(Population Size) 및 광고 지출(Advertising Spending)을 두 예측 변수로 구성한 합성 데이터 세트에서의 PLS 예시를 보여줍니다. 진한 녹색 실선은 첫 번째 PLS 방향을 나타내며, 점선은 첫 번째 주성분 방향을 보여줍니다. PLS는, PCA에 비해 `pop` 차원이 한 단위 변화할 때 `ad` 차원에서 나타나는 변화가 적은 방향을 선택했습니다. 이는 `pop` 변수가 `ad`보다 반응 변수와 더 높은 상관관계를 지니고 있음을 시사합니다. PLS 방향은 PCA가 그랬던 것만큼 예측 변수를 밀접하게 적합시키지는 못하지만, 반응 변수를 설명하는 데에는 더 뛰어난 성과를 보여줍니다.

To identify the second PLS direction we first _adjust_ each of the variables for $Z_1$, by regressing each variable on $Z_1$ and taking _residuals_. These residuals can be interpreted as the remaining information that has not been explained by the first PLS direction. We then compute $Z_2$ using this _orthogonalized_ data in exactly the same fashion as $Z_1$ was computed based on the original data. This iterative approach can be repeated $M$ times to identify multiple PLS components $Z_1, \ldots, Z_M$. Finally, at the end of this procedure, we use least squares to fit a linear model to predict $Y$ using $Z_1, \ldots, Z_M$ in exactly the same fashion as for PCR. 
두 번째 PLS 방향을 식별하기 위해, 먼저 각 변수를 $Z_1$에 회귀시키고 _잔차(residuals)_ 를 얻음으로써 $Z_1$에 대해 각 변수를 _조절(adjust)_ 합니다. 이 잔차들은 첫 번째 PLS 방향에 의해 아직 설명되지 않고 남아 있는 정보로 해석될 수 있습니다. 그런 다음, 원본 데이터를 기반으로 $Z_1$을 계산했던 것과 정확히 동일한 방식(exactly the same fashion)으로 이 _직교화된(orthogonalized)_ 데이터를 사용하여 $Z_2$를 계산합니다. 이러한 반복적인 접근법은 다수의 PLS 구성 요소 $Z_1, \ldots, Z_M$을 식별하기 위해 총 $M$회 반복하여 수행될 수 있습니다. 마지막으로 이 절차가 끝난 시점에서, 우리는 선형 모델에 $Z_1, \ldots, Z_M$을 이용해 목표 변수 $Y$를 예측할 수 있도록, PCR에서 수행했던 것과 정확히 똑같은 방식 기반으로 최소 제곱법을 사용해 모델을 적합시킵니다.

As with PCR, the number $M$ of partial least squares directions used in PLS is a tuning parameter that is typically chosen by cross-validation. We generally standardize the predictors and response before performing PLS. 
PCR의 경우와 마찬가지로, PLS에서 사용되는 부분 오차 단면의 부분 최소 제곱 방향선 개수 파라미터인 단일 $M$ 지수는 전적으로 **교차 검증(cross-validation)** 평가 수치를 기준으로 통상 최종 결정되는 단면 튜닝 매개변수 통제입니다. 우리는 PLS를 기동 실행 분석 수행하기 이전에 예측 변수와 반응 응답 변수를 먼저 일반적으로 사전에 몽땅 **표준화(standardize)** 시켜 줍니다.

PLS is popular in the field of chemometrics, where many variables arise from digitized spectrometry signals. In practice it often performs no better than ridge regression or PCR. While the supervised dimension reduction of PLS can reduce bias, it also has the potential to increase variance, so that the overall benefit of PLS relative to PCR is a wash. 
PLS는 계량화학(chemometrics) 통계 도메인 분야 분석상에서 인기가 많은 수리 기법입니다. 해당 도메인에선 디지털화된 분광계 신호상에서 기인되어 발생 분포하는 수많은 다중 무한 변수 데이터 신호가 무수 존재하기 연유입니다. 하지만 정작 산업 실무상 실전 무대에서의 운용에서 PLS 모델은, 종종 기존의 능선 회귀 모델 방식 혹은 일반 분석 PCR 보편 단면적 방법들보다 단일 눈에 띄게 더 우월 뛰어나 성과 결과치 단면 측정 도출을 보이지 못하며 기대 성능에 단결 못 미치는 실질적인 수행 결괏값 도출 한계를 현장 측에서 대변해 주곤 합니다. 그 단면의 도출 이면에는 지도 측 학습 단결 방면의 PLS 차원 압축 조작 감응이 시스템 진영 기저 오리지날 헛발질 단면 오차 편향(bias) 비율을 낮추고 단축 제재하여 낮출 수는 척결 진정 있겠으나, 동시에 잡음에 동조하는 단일 지수 무계 분산(variance) 산포 규모 체계치를 기하학 차원 동시 키워 오히려 통제 밖으로 높이고 늘려 버릴 위험 잠재 배반 부작용 증가 현상이 수반 도출 잠복 발현 동반 잠복되어 커질 동결 우려 이면이 도사리기 때문입니다. 결과적으로 PCR 모델과 비교해 볼 때 PLS 기법이 가지는 전체적인 성과 이점은 사실상 상쇄되어 별 의미가 없어집니다.
