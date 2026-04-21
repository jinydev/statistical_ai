---
layout: default
title: "trans2"
---

[< 4.5.2 An Empirical Comparison](../4_5_a_comparison_of_classification_methods/4_5_2_an_empirical_comparison/trans2.html) | [4.6.1 Linear Regression On The Bikeshare Data >](4_6_1_linear_regression_on_the_bikeshare_data/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.6 Generalized Linear Models
# 4.6 일반화 선형 모델 (GLM) : 뼈의 한계를 넘는 괴물 병기!

In Chapter 3, we assumed that the response $Y$ is quantitative, and explored the use of least squares linear regression to predict $Y$.
저 까마득한 옛날 3장 시절, 우리는 타깃 정답지인 반응 변수 $Y$ 가 키나 몸무게처럼 매끄럽게 끊기지 않고 쭈욱 이어지는 **연속적인 양적 수치(quantitative)** 일 거라고 굳게 믿고, 이 녀석을 때려잡기 위해 평범하고 길다란 '최소 제곱 선형 회귀' 라는 직선 몽둥이 하나를 사용해 예측하는 법을 배웠습니다. 

Thus far in this chapter, we have instead assumed that $Y$ is qualitative.
그리고 판이 바뀌어 이번 4장에 들어와서는 지금까지 줄곧, 타깃 $Y$ 가 사과냐 배냐를 가르듯 딱딱 끊어지는 **문자 꼬리표 범주(qualitative)** 일 거라고 가정하고 치고받아왔죠.

However, we may sometimes be faced with situations in which $Y$ is neither qualitative nor quantitative, and so neither linear regression from Chapter 3 nor the classification approaches covered in this chapter is applicable.
그런데 말입니다! 실전 지옥에 나가보면 황당하게도 우리가 맞춰야 할 $Y$ 결과값이 저 연속 수치도 아니고 끊기는 문자 꼬리표도 아닌, **이도 저도 아닌 제3의 돌연변이 괴물 형태**를 띠는 기막힌 딜레마 구역에 맞닥뜨리는 수가 허다합니다. 당연히 이런 괴상한 늪지대 무대에서는 애증의 3장 선형 회귀 통나무 방망이도 전혀 안 먹히고, 지금 4장에서 피 터지게 배웠던 그 어떤 화려한 분류기 기법들도 몽땅 먹통 폐기물이 되고 맙니다!

As a concrete example, we consider the `Bikeshare` data set.
그 지저분하고 끔찍한 돌연변이의 구체적 실사례로, 통계 바닥에서 아주 유명한 **`Bikeshare(자전거 대여)` 쌍끌이 데이터 세트**를 도마에 올려 까봅시다.

The response is `bikers`, the number of hourly users of a bike sharing program in Washington, DC.
이 바닥에서 우리가 맞춰야 할 타깃 반응 변수는 무려 `bikers` 인데, 미국의 워싱턴 DC라는 동네에서 한 시간마다 따릉이를 빌려가는 **'사람들의 렌탈 머릿수'** 입니다. 

This response value is neither qualitative nor quantitative: instead, it takes on non-negative integer values, or _counts_.
사람의 머릿수를 반으로 쪼갤 순 없으니 이 정답 값은 몸무게처럼 유연한 연속 수치 숫자(정량적)도 아니고, "성공이냐 실패냐"를 가르는 단순 문자(정성적) 팻말도 아닙니다. 이 변태 녀석의 정체는 바로! 절대 마이너스가 나올 수 없는 양수의 눈금 덩어리이자 뚝뚝 끊기는 정수 칸, 단 하나, 1번, 2번, 즉 **_카운트 개수(counts)_** 라는 아주 특이한 성질을 지니고 태어났습니다!

We will consider predicting `bikers` using the covariates `mnth` (month of the year), `hr` (hour of the day, from 0 to 23), `workingday` (an indicator variable that equals 1 if it is neither a weekend nor a holiday), `temp` (the normalized temperature, in Celsius), and `weathersit` (a qualitative variable that takes on one of four possible values: clear; misty or cloudy; light rain or light snow; or heavy rain or heavy snow.)
우리는 야생에서 이 괴상한 `bikers` 횟수 타깃을 정확히 때려 맞추기 위해, 아주 짭짤하게 긁어모은 힌트 단서(공변량) 무기들을 총동원 투입할 겁니다: `mnth` (1~12월 달별 꼬리표), `hr` (하루 0시~23시의 시간차 꼬리표), `workingday` (주말이나 편히 노는 공휴일이 아니면 무조건 1을 도장 박아주는 일개미 지시 변수), `temp` (섭씨온도를 예쁘게 가공 튜닝한 정규화 수치), 그리고 피날레 장비인 `weathersit` (하늘이 무너지느냐 맑느냐를 4가지 단계: 맑음 / 옅은 안개나 흐림 / 가벼운 비나 눈 / 무참한 폭우나 폭설 따위로 쪼개서 팻말을 붙인 정성적 날씨 변수) 따위가 그 주인공입니다.

In the analyses that follow, we will treat `mnth`, `hr`, and `weathersit` as qualitative variables.
이 야생 전장에서 피 튀길 후속 분석 전투부터, 우리 사령부는 선제 타격으로 저 `mnth(월)`, `hr(시간)`, 그리고 `weathersit(날씨)` 이 세 녀석 아이템들만큼은 절대 수학적 연속 숫자가 아니라고 규정하고, 아주 철저하고 냉정하게 끊어지는 **문자 범주형(qualitative) 꼬리표 변수** 계급으로 취급해 굴릴 것입니다.

---

### 4.6.1 Linear Regression on the Bikeshare Data
### 4.6.1 자전거 대여 데이터 패기에 잘못 들이댄 선형 회귀 몽둥이질

### 4.6.2 Poisson Regression on the Bikeshare Data
### 4.6.2 본 게임 시작! 자전거 대여 카운트 데이터 전용 무기, 특수 '포아송 회귀' 출격!

### 4.6.3 Generalized Linear Models in Greater Generality
### 4.6.3 더 넓은 세계로의 확장: 우주 융합 끝판왕 '일반화 선형 모델 (GLM)'의 진짜 정체

---

## Sub-Chapters

[< 4.5.2 An Empirical Comparison](../4_5_a_comparison_of_classification_methods/4_5_2_an_empirical_comparison/trans2.html) | [4.6.1 Linear Regression On The Bikeshare Data >](4_6_1_linear_regression_on_the_bikeshare_data/trans2.html)
