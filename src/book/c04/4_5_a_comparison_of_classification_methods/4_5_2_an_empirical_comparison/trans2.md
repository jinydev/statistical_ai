---
layout: default
title: "trans2"
---

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/trans2.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.5.2 An Empirical Comparison
# 4.5.2 경험적 비교: 실전 데이터 필드에서의 피 튀기는 모의 전투

We now compare the _empirical_ (practical) performance of logistic regression, LDA, QDA, naive Bayes, and KNN. We generated data from six different scenarios, each of which involves a binary (two-class) classification problem. In three of the scenarios, the Bayes decision boundary is linear, and in the remaining scenarios it is non-linear. The results are summarized below:
방금 전의 딱딱한 탁상 수학 토론을 끝내고, 이제 로지스틱 회귀, LDA, QDA, 나이브 베이즈, 그리고 돌격대 KNN의 **_경험적_ (실전 야생에서의 전투) 타격 성능**을 진짜 모의 훈련장에서 까놓고 승부를 가려 비교해 볼 시간입니다! 우리는 철저한 검증을 위해 아주 악랄하게 세팅된 **여섯 가지 극단적 훈련 시나리오 맵**에서 가짜 난수 데이터 군단을 생성해 흩뿌렸습니다. 각 실험 맵은 얄짤없는 이분법 데스매치 (이진 분류) 전쟁터 모드입니다. 이 여섯 개의 전장 맵 가운데, 딱 절반인 세 개의 맵은 적과 아군 구역을 가르는 심판의 '베이즈 절대 방어선'이 반듯하고 단순한 **'직선(1차 선형)' 장벽 구조**를 띠고 있고, 나머지 절반 세 개의 맵은 끔찍하게 구불거리는 뱀 꼬리 지그재그 **'비선형 커브' 장벽 구조**를 지니고 있습니다. 이 여섯 차례 피 튀기는 모의 전투 배틀 로얄의 랭킹 결과 스코어를 아래에 요약 발제 보고합니다!

- **Scenario 1 (Linear boundary, independent normal variables):** LDA performed well as expected. Logistic regression also performed well. KNN performed poorly because it suffered from variance. QDA performed worse than LDA since it was more flexible than necessary. Naive Bayes was slightly better than QDA because the assumption of independent predictors was correct.
- **[전투 맵 1] (단순 직선 경계, 애들이 다 정규 분포에 독립적임):** 이 전투판은 선형 판별기의 고향 그 자체입니다. 예상대로 뻣뻣한 **LDA** 특수 부대가 압도적인 승전보를 울리며 대활약했습니다. 쌍둥이인 **로지스틱 회귀** 역시 어김없이 발군의 실력으로 선방했죠. 반면 머리에 먹물이 텅 빈 **KNN 돌격대**는 미쳐 날뛰는 변동성 파동 현상(Variance) 에 시달리며 눈먼 총알을 쏴대다 개죽음 참패를 당했습니다. 곡선 뱀 **QDA** 녀석은 하필 전장이 단순 직선 싸움터인데도 혼자 너무 유연하게 흐느적거리다 몸이 꼬여서(과적합) 오히려 딱딱한 LDA보다 저조한 헛발질을 보였고, 순진무구 **나이브 베이즈**는 "얘네들 다 독립이잖아!" 라는 지들의 단순 멍청한 가정이 우연히도 적중해버린 운 좋은 로또를 맞은 덕분에 QDA보다 살짝 우위의 타격 성적을 구사하는 이변 선방을 보였습니다!
- **Scenario 2 (Linear boundary, correlated variables):** Similar to Scenario 1, except naive Bayes performed very poorly because its independence assumption was completely violated by the correlated predictors.
- **[전투 맵 2] (단순 직선 경계인데, 변수들끼리 연관성 사슬로 더러움):** 첫 번째 전투 맵과 양상은 비슷하지만 딱 한 놈의 운명이 확 달라졌습니다. 바로 **나이브 베이즈** 입니다! ఈ 맵에선 변수병사 놈들이 치사하게 뒤로 얽혀 상관관계 유착 사슬(correlated)을 짜고 노는 판국인데, 나이브 베이즈가 "어림없다 늬들 다 독립 전사야!" 라고 눈감고 우기던 망상이 처참하게 짓밟혀 산산조각 났기 때문에, 허공에 헛발질하며 구제 불능 수준의 **바닥 치는 꼴찌 최악의 랭킹 성적**으로 폭격을 맞아 침몰했습니다.
- **Scenario 3 (Linear boundary, t-distribution):** Outliers were present. Logistic regression outperformed LDA since the data departed from the strict normal assumption. QDA deteriorated considerably. Naive Bayes performed very poorly again due to violated assumptions.
- **[전투 맵 3] (단순 직선 경계, 근데 괴물 특이치가 난무하는 t-분포 늪지대):** 변태적 뚱보 괴물 극단값(Outliers 특이치) 이 난무하는 오염된 전투 지형입니다. 이 진창에선 데이터들이 LDA가 그토록 굳게 믿던 얌전한 교과서 '정규 분포' 형태의 성역을 깡그리 이탈 파괴해 버렸기 때문에! 실전 야생 노가다에 강한 통계 깡패 **로지스틱 회귀 군단**이 혈통 귀족파 LDA 녀석들을 발아래 압도해버리고 성능 승리를 쟁취합니다. 한편 **QDA**는 그 유연한 몸집 통제력을 아예 잃고 뇌졸중 걸리듯 상당한 폭삭 악화를 면치 못했고, 빙충이 **나이브 베이즈** 역시 지들만의 허무 맹랑 독립 맹신이 산산조각 위반 나면서 또다시 연달아 폭망 참패를 조기 당했습니다.
- **Scenario 4 (Quadratic boundary, normal distribution with different correlations):** The decision boundary is non-linear. QDA outperformed all the other methods. Naive Bayes performed poorly due to independence violation.
- **[전투 맵 4] (2차 포물선 비선형 구부러진 방어성벽 경계, 다양한 유착 관계를 띤 정규 분포 숲):** 드디어 진검승부! 방패 장벽이 더 이상 단순 직선이 아니라 곡률 요동 비선형 굴곡 요새입니다! 물 만난 물고기, 곡선 뱀의 제왕 **QDA 유격대**가 다른 모든 선형 경쟁 진영 녀석들을 싹 다 압도적으로 찍어 누르며 황제로 왕좌에 군림했습니다. 불쌍한 빙구 **나이브 베이즈**는 여전히 파벌들 간의 연관 유착 속성을 절대 부인하는 치명적인 "지 혼자 남남" 망상 위반 질병으로 인해 또 참패의 쓴맛을 삼켰습니다.
- **Scenario 5 (Highly non-linear boundary):** Both QDA and naive Bayes gave better results than the linear methods (LDA/Logistic). However, the highly flexible KNN-CV method gave the best overall results. Interestingly, KNN with $K=1$ gave the worst results, highlighting the importance of tuning smoothness.
- **[전투 맵 5] (극강의 꼬불꼬불 초-비선형 지그재그 난해 방어벽):** 방어막이 미친년 널뛰듯 지그재그 늪입니다! 일단 뻣뻣한 나무 직진 통나무들(LDA / 로지스틱 대원들)은 전멸. 그래도 휜 각에선 조금 유연하게 휘어주는 곡선 **QDA**와 독립 타격 몽상 **나이브 베이즈**가 그들보단 선방 나은 성적을 터뜨렸습니다. 허나! 진짜배기 최종 보스 승리 왕관은 아예 수식 뼈대 따위 처음부터 버려두고 데이터의 점 굴곡 곡률 모양에 맞춰 무한 변신 장착 타격을 가하는 극강 유연 **비모수 무적 머신 KNN (교차 검증 세팅빨)** 돌격 부대놈이 압권으로 휩쓸어 최강자 등극 타결을 거머쥐었습니다! 근데 개그는 여기서도 **단 1명의 동료만 쳐다보는 (K=1) 외골수 세팅의 KNN 찌라시 녀석**은 너무 요동치는 변덕 징조 예민성 파편화 공포 탓에 제일 최악 꼴찌 바닥을 치는 망신 삽질을 당했다는 사실입니다. 이는 우리가 파라미터를 곡률 조절해 튜닝 평활 공구(tuning smoothness)로 깎고 다듬는 작업이 얼마나 목숨처럼 귀중한 치명 생존 기술인 지 무 척 절실 압 도 통 지 입 증 해 주는 역사의 증거 교훈 파편 입 니 다!
- **Scenario 6 (Non-linear boundary due to unequal variance, extremely small sample size n=6):** Naive Bayes performed phenomenally well because its assumptions held and its variance is low. LDA/Logistic regression performed poorly due to the non-linear true boundary. QDA struggled heavily because it lacked the data size to estimate its high number of parameters, suffering from intense variance. KNN also failed completely due to the lack of training data.
- **[전투 맵 6] (애들끼리 뱃살 두께가 파괴적으로 불균등 꼬여 생긴 기괴 비선형 장막, 거기다 데이터 쪽수 n=6 이란 처참한 극한 빈곤 가난 지형):** 기적의 반전! 빙충이 등신 소리 듣던 멍청 **나이브 베이즈 군단**이 미쳐 날뛰며 이 척박한 무대판을 평정하고 역사에 남을 극강 우승 성능 타격 제왕 홈런 타자 진압 퍼포먼스(phenomenally well)를 때려 박았습니다! 왜냐? 진짜 우연찮게도 놈이 세워둔 그 오지랖 망상 가정들이 이 지형 환경이랑 딱 기막히게 맞아떨어졌을 뿐더러, 데이터가 겨우 6개밖에 안 되는 이 처참한 극빈 거지 소규모 환경에서조차 변동 파괴 진동 에러(Variance)가 전혀 없이 안정적인 맷집 방어막이 무적 급으로 작동했기 때문입니다. 당연히 뻣뻣 통나무 **LDA/ 로지스틱 형제**는 기괴한 비선형 벽 구조에 대가리를 박고 폭망했고, 유연한 우승자 후보 괴물 **QDA 곡선** 녀석은 연산 파라미터가 드럽게 많이 필요해서 기름 더 많이 먹는 하마 병에 걸려 있는데 사료 고작 n=6개밖에 안 주니 고열 굶주림(intense variance 폭탄) 발작으로 쇼크 사망을 선고받으며 쓰러졌습니다. 그 아무 뼈대도 없는 데이터 거지 본능 돌격대 **KNN 조차도** 주워 먹을 훈련 파편이 전무 부족한 사막 허허벌판 결핍 상태라 총 한 번 못 쏴보고 굶어 즉사 전원 참수 실패 폭망 부도 결단을 맞이 통 렬 구 현 당했습니다.

These six examples illustrate that no one method will dominate the others in every situation. When the true decision boundaries are linear, then the LDA and logistic regression approaches will tend to perform well. When the boundaries are moderately non-linear, QDA or naive Bayes may give better results. Finally, for much more complicated decision boundaries, a non-parametric approach such as KNN can be superior.
방금 펼쳐본 이 피 튀기는 6대 전투 랭킹 시나리오는 우리에게 뼈아픈 실전 교훈 하나를 명언처럼 각인시켜 줍니다: **이 통계 야생 바닥에 모든 상황을 다 호령하는 단 하나의 무적 지배자 모델 따위는 절대 존재하지 않는다!** 당신의 치고받는 문제 구역 진짜배기 장벽 모양이 어림잡아 선형 직선 형태다 싶으면 주저 없이 **LDA나 로지스틱 회귀** 전술을 투입해야 승산이 큽니다. 만약 그 적진 구역 뼈대가 은근슬쩍 구불구불 곡선 뱀처럼 휘어있다면, 그땐 **QDA나 혹은 무식 맹신충 나이브 베이즈**를 투척해야 최고의 점수를 챙깁니다. 마지막으로! 장벽 꼬라지가 아주 거미줄 지뢰밭 미로 수준으로 미치게 뒤엉킨 난해한 복잡 곡률 상태라면, **아예 수학 뼈대 따위 전부 걷어차 버리고 맨 땅 야생 돌진하는 KNN** 같은 비모수 폭격기 방식이 승자 독식의 압도적 결과를 가져올 수 있습니다!

---

## Sub-Chapters

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/trans2.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/trans2.html)
