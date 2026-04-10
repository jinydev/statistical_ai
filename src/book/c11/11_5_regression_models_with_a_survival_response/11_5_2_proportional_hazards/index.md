---
layout: default
title: "index"
---

# _11.5.2 Proportional Hazards_ 

The Proportional Hazards Assumption 

The _proportional hazards assumption_ states that 

$$
h(t | x_i) = h_0(t) \exp \left( \sum_{j=1}^p x_{ij} \beta_j \right) \quad (11.14)
$$

proportional hazards assumption 

where _h_ 0( _t_ ) _≥_ 0 is an unspecified function, known as the _baseline hazard_ . baseline It is the hazard function for an individual with features _xi_ 1 = _· · ·_ = _xip_ = hazard 0. The name “proportional hazards” arises from the fact that the hazard function for an individual with feature vector _xi_ is some unknown function 

> 9See Exercise 9. 

> 10Given the close relationship between the hazard function _h_ ( _t_ ) and the density function _f_ ( _t_ ) explored in Exercise 8, posing an assumption about the form of the hazard function is closely related to posing an assumption about the form of the density function, as was done in the previous paragraph. 

> 11The notation _h_ ( _t|xi_ ) indicates that we are now considering the hazard function for the _i_ th observation conditional on the values of the covariates, _xi_ . 

11.5 Regression Models With a Survival Response 479 

![Figure 11.4](./img/11_4.png)

**FIGURE 11.4.** Top: _In a simple example with p_ = 1 _and a binary covariate xi ∈{_ 0 _,_ 1 _}, the log hazard and the survival function under the model_ (11.14) _are shown (green for xi_ = 0 _and black for xi_ = 1 _). Because of the proportional hazards assumption_ (11.14) _, the log hazard functions differ by a constant, and the survival functions do not cross._ Bottom: _Again we have a single binary covariate xi ∈{_ 0 _,_ 1 _}. However, the proportional hazards assumption_ (11.14) _does not hold. The log hazard functions cross, as do the survival functions._ 

_p p h_ 0( _t_ ) times the factor exp �� _j_ =1 _[x][ij][β][j]_ �. The quantity exp �� _j_ =1 _[x][ij][β][j]_ � is called the _relative risk_ for the feature vector _xi_ = ( _xi_ 1 _, . . . , xip_ ) _[T]_ , relative to that for the feature vector _xi_ = (0 _, . . . ,_ 0) _[T]_ . 

What does it mean that the baseline hazard function _h_ 0( _t_ ) in (11.14) is unspecified? Basically, we make no assumptions about its functional form. We allow the instantaneous probability of death at time _t_ , given that one has survived at least until time _t_ , to take any form. This means that the hazard function is very flexible and can model a wide range of relationships between the covariates and survival time. Our only assumption is that a one-unit increase in _xij_ corresponds to an increase in _h_ ( _t|xi_ ) by a factor of exp( _βj_ ). 

An illustration of the proportional hazards assumption (11.14) is given in Figure 11.4, in a simple setting with a single binary covariate _xi ∈{_ 0 _,_ 1 _}_ (so that _p_ = 1). In the top row, the proportional hazards assumption (11.14) holds. Thus, the hazard functions of the two groups are a constant multiple of each other, so that on the log scale, the gap between them is constant. Furthermore, the survival curves never cross, and in fact the gap between the survival curves tends to (initially) increase over time. By contrast, in the bottom row, (11.14) does not hold. We see that the log hazard functions for the two groups cross, as do the survival curves. 

480 11. Survival Analysis and Censored Data 

---

## Sub-Chapters (하위 목차)

### Cox’s Proportional Hazards Model (콕스 비례 위험 모형)
* [문서로 이동하기](./11_5_2_1_coxs_proportional_hazards_model/)

시간 중심의 기본 위험 함수 $h_0(t)$ 형태를 굳이 추정하지 않고 오직 변수 계수에만 집중하여 부분 최대 우도법으로 모델링하는 이 분야 최고의 베스트셀러 모델입니다.

### Connection With The Log-Rank Test (로그 랭크 검정과의 수학적 관계망)
* [문서로 이동하기](./11_5_2_2_connection_with_the_log-rank_test/)

단일 범주 변수로 이분류된 데이터를 콕스 모형의 독립변수에 넣었을 때 도출되는 스코어 검정 통계량이 신기하게도 로그 랭크의 원리와 본질적으로 일치함을 유도해 냅니다.

### Which one should we prefer? (어떤 방식을 선호해야 하는가?)
* [문서로 이동하기](./11_5_2_3_which_one_should_we_prefer/)

단순 2집단 분기라면 카플란 마이어+로그랭크 통계량이 편리하고 가시적이나, 여럿 변수를 통제한 개별 요인 기여도를 알기 원할 땐 콕스 모델을 택하는 게 옳음을 정리합니다.

### Additional Details (콕스 모형의 추가 수학적 논의 및 부분 우도 함수 유도 절차)
* [문서로 이동하기](./11_5_2_4_additional_details/)

콕스 모형 최적화 과정에서 왜 오직 타겟 사건들이 일어나는 찰나의 순간값들 세팅만 분모로 모여 계수($\beta$) 부분 검정에 영향을 미치는지 편미분 연산을 심층 점검합니다.
