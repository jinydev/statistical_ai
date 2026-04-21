---
layout: default
title: "trans2"
---

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/trans2.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.5.2 An Empirical Comparison
# 4.5.2 경험적 비교 (직접 데이터를 굴려보자!)

We now compare the _empirical_ (practical) performance of logistic regression, LDA, QDA, naive Bayes, and KNN.
자, 수학 공식으로만 떠드는 입배틀은 여기까지! 우리는 이제 로지스틱 회귀, LDA, QDA, 나이브 베이즈, 그리고 투박한 깡패 KNN 기계들을 실제 판에 올려놓고 멱살 잡히고 뒹구는 **경험적(empirical)** 인 실전 타율(성능)을 팩트로 비교해보겠습니다.

We generated data from six different scenarios, each of which involves a binary (two-class) classification problem.
우리는 이 기계 장치들을 가혹하게 테스트하기 위해, 마치 실험실의 마루타처럼 성격이 완전히 구별되는 6가지의 지독한 시나리오 데이터를 인공적으로 뽑아냈습니다. 이 판들은 모두 "적군이냐 아군이냐"를 가르는 이진(두 클래스) 분류 미션 방입니다.

In three of the scenarios, the Bayes decision boundary is linear, and in the remaining scenarios it is non-linear. The results are summarized below:
그 6개의 방 중 3개의 방은 진짜 참 정답의 결정 라인(베이즈 결정 경계)이 예쁘고 길쭉한 선형(linear)으로 곧게 뻗어 있고, 나머지 3개의 방은 뒤틀리고 꼬인 비선형(non-linear) 형태를 취합니다. 이 피 튀기는 콜로세움의 전투 결과표는 아래와 같이 화려하게 요약됩니다:

- **Scenario 1 (Linear boundary, independent normal variables):** LDA performed well as expected. Logistic regression also performed well. KNN performed poorly because it suffered from variance. QDA performed worse than LDA since it was more flexible than necessary. Naive Bayes was slightly better than QDA because the assumption of independent predictors was correct.
- **시나리오 1 (선형 경계 + 착한 독립 정규 변수들):** "가장 얌전하고 교과서적인 맵!" LDA는 입꼬리를 올리며 예상대로 아주 날아다녔습니다. 눈치 빠른 로지스틱 회귀 역시 무난하게 훌륭한 타율을 뽑았죠. 반면 무식한 무투파 KNN은 이 예쁜 판에서 괜히 예민하게 요동치는 분산(variance) 발작을 겪느라 헛발질하며 죽을 쑤었습니다. 뚱땡이 QDA는 선 하나면 끝날 판에 쓰잘데기 없이 구부러진 무기를 들고 설쳐대는 바람에(과잉 유연성) 오히려 LDA보다 성적이 저조했죠. 나이브 베이즈 꼼수 장치는 "변수는 다 독립이야!" 라는 억지 가정이 이 맵에서는 우연히 진짜 사실로 맞아떨어진 덕에 QDA보단 오히려 낫다는 흡족한 성적표를 받았습니다.

- **Scenario 2 (Linear boundary, correlated variables):** Similar to Scenario 1, except naive Bayes performed very poorly because its independence assumption was completely violated by the correlated predictors.
- **시나리오 2 (선형 경계 + 뒤에서 짝짜꿍하는 연관 변수들):** "시나리오 1과 비슷해! 근데 함정이 있다?" 판 자체는 여전히 얌전한 직선 맵이지만, 이번엔 단서들이 서로 뒤에서 찰떡같이 엮여 내통합니다! 이 바람에 "변수들은 무조건 독립이야 짱짱!"을 외치던 마법 장치 나이브 베이즈의 행복 회로 가설이 처참하게 박살 나며 폭망하고 최하위 바닥 수준으로 곤두박질치고 말았습니다.

- **Scenario 3 (Linear boundary, t-distribution):** Outliers were present. Logistic regression outperformed LDA since the data departed from the strict normal assumption. QDA deteriorated considerably. Naive Bayes performed very poorly again due to violated assumptions.
- **시나리오 3 (선형 경계 + 미친 이상치 깽판, t-분포):** "얌전한 맵에 미친 또라이(이상치)들이 난입했다!" 판이 시작되자 곳곳에서 통계를 무시하는 과격한 이상치 데이터들이 날뜁니다. 엄격한 정규 분포 성적표만 믿었던 모범생 LDA는 이상치에 뺨을 맞고 뻗었지만, 현실 적응력 강한 로지스틱 회귀 깡패는 이 난장판에서도 침착하게 대처하며 LDA를 크게 눌러 이겼습니다(outperformed). QDA는 아예 멘탈이 나갔고 크게 저하됐으며, 나이브 베이즈 꼼수 장치는 여전히 가정 파괴의 늪에서 헤어 나오지 못하고 연달아 바닥을 쳤습니다.

- **Scenario 4 (Quadratic boundary, normal distribution with different correlations):** The decision boundary is non-linear. QDA outperformed all the other methods. Naive Bayes performed poorly due to independence violation.
- **시나리오 4 (구부러진 2차 경계 + 얽히고설킨 정규 분포):** "드디어 지형이 구부러졌다!" 직선 맵이 붕괴되고 결정 라인이 비선형(non-linear)으로 요동칩니다. 물 만난 고기처럼 이때를 기다린 유연한 전차 QDA가 모든 경쟁 기계들을 압도적으로 씹어먹으며 패왕으로 등극합니다. 반면 나이브 베이즈는 또다시 연관성의 벽을 못 넘고 꼼수 가정이 들통나 부진을 겪었죠.

- **Scenario 5 (Highly non-linear boundary):** Both QDA and naive Bayes gave better results than the linear methods (LDA/Logistic). However, the highly flexible KNN-CV method gave the best overall results. Interestingly, KNN with $K=1$ gave the worst results, highlighting the importance of tuning smoothness.
- **시나리오 5 (미친 듯이 꼬이고 뒤틀린 초 비선형 경계):** "도면이 스파게티 꽈배기가 되었다!" 이 괴랄한 판에선 선 긋기 원툴인 LDA와 로지스틱 회귀가 맥을 못 추고, 그나마 구부릴 줄 아는 QDA와 나이브 베이즈가 선방을 칩니다. 하지만, 마침내!! 뼈대 따위 쌩까고 무식하게 현장 바닥에 딱 달라붙어 구르는 끝판왕 장비, 매우 유연한 세팅을 거친 **KNN-CV** 녀석이 전체 대전에서 최종 최상 성능 스코어를 따내는 무적의 모습을 보여줍니다! 하지만 웃기게도, 같은 KNN이라도 $K=1$ 이라는 극단적 세팅을 건 녀석은 오히려 판에서 꼴찌 최악을 기록했는데요. 이는 무식한 기계라도 부드러움(smoothness)을 조율 튜닝(tuning)해 주는 작업이 생존에 얼마나 절대적인지를 매섭게 보여주는 교훈입니다.

- **Scenario 6 (Non-linear boundary due to unequal variance, extremely small sample size n=6):** Naive Bayes performed phenomenally well because its assumptions held and its variance is low. LDA/Logistic regression performed poorly due to the non-linear true boundary. QDA struggled heavily because it lacked the data size to estimate its high number of parameters, suffering from intense variance. KNN also failed completely due to the lack of training data.
- **시나리오 6 (분산 불균형 비선형 경계 + 달랑 6개뿐인 초 빈곤 자원 데이터):** "총알이 모자라도 너무 모자란 극한의 굶주림 서바이벌(n=6)!" 식량이 없어 다 굶어 죽는 이 극한 환경에서 희대의 꼼수 장치 **나이브 베이즈**가 미라클 같은 대박(phenomenally well) 성과를 터뜨리며 세상을 놀라게 합니다! "억지 독립 가정 발동!" 이게 기적처럼 맞아떨어졌을 뿐만 아니라, 부품 고장이 없는 '극저 분산(low variance)' 특성이 이 굶주린 척박한 땅에서 생물적 우위로 폭발한 겁니다. 반면 참 지형이 비선형인 탓에 선형 기계들(LDA/로지스틱)은 피를 토했고, 무기 부품에 기름(파라미터 추정 데이터)을 쏟아부어야만 굴릴 수 있는 뚱땡이 거함 QDA는 굶어 죽어 극심한 요동 발작에 몹시 고통받으며 완전 망했습니다(struggled heavily). 거기에 무투파 KNN? 데이터 쪽수로 밀어붙이는 놈이 훈련 총알이 없으니 시동조차 못 걸고 완전히 아사해 참패(failed completely)하고 말았죠!

These six examples illustrate that no one method will dominate the others in every situation.
눈물 없인 볼 수 없는 이 6번의 피 말리는 전투 결과표는, 결국 우리에게 아주 시크한 진리를 못 박아 줍니다: "어떤 천하무적 무기 기계 모델 장치라도, 모든 상황 우주 세팅 무대에서 혼자만 영원히 왕관을 쓰고 영구 짱을 먹으며 지배(dominate) 할 수 있는 놈은 이 바닥에 절대로 존재하지 않는다!"

When the true decision boundaries are linear, then the LDA and logistic regression approaches will tend to perform well.
만약 판이 얌전하게 쭉쭉 뻗은 선형적(linear)인 교과서 꽃길이라면, 똑똑한 엘리트 **LDA** 모델이나 현실 깡패 **로지스틱 회귀** 기계가 아주 믿음직하게 가성비 좋게 잘만 굴러갑니다.

When the boundaries are moderately non-linear, QDA or naive Bayes may give better results.
판 지형 라인이 살살 요동치며 어느 정도 완만한 비선형 곡선을 그린다 싶으면, 덩치 큰 **QDA** 전차를 몰거나, 기적의 돌연변이 **나이브 베이즈** 꼼수가 훨씬 더 통쾌한 결과를 쏟아냅니다.

Finally, for much more complicated decision boundaries, a non-parametric approach such as KNN can be superior.
마지막으로, 지형이 앞도 안 보일 정도로 꼬이고 뒤틀려 규칙 따위 갖다 버린 복잡 시궁창 막장 경계 선이라면? 골치 아픈 뼈대 이론 따위 집어치운 비모수적(non-parametric) 잡초 싸움꾼, 뚝심 최강 **KNN**이 역전의 무기로 모두를 압살하고 가장 예리하게 제패(superior) 할 수 있는 최후의 보스 병기 카드로 남게 됩니다!

---

## Sub-Chapters

[< 4.5.1 An Analytical Comparison](../4_5_1_an_analytical_comparison/trans2.html) | [4.6 Generalized Linear Models >](../../4_6_generalized_linear_models/trans2.html)
