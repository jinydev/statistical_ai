---
layout: default
title: "trans2"
---

[< 1.1 An Overview Of Statistical Learning](../1_1_an_overview_of_statistical_learning/trans2.html) | [1.3 This Book >](../1_3_this_book/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# A Brief History of Statistical Learning
# 통계적 학습의 간략한 역사 (고인물들의 처절한 노가다 연대기)

Though the term statistical learning is fairly new, many of the concepts that underlie the field were developed long ago.
'통계적 기계 학습'이라는 단어 자체는 요즘 유튜브에서나 떠드는 꽤나 신상 트렌드 단어 냄새가 나지만, 사실 그 바닥을 지탱하는 뼈대 수학 공식들은 이미 호랑이 담배 피우던 옛날 옛적부터 고인물 할아버지들이 닦아놓은 낡은 유산들입니다.

At the beginning of the nineteenth century, the method of *least squares* was developed, implementing the earliest form of what is now known as *linear regression*.
시간을 거슬러 19세기 완전 초반(1800년대)으로 가봅시다. 이때 이미 위대한 수학자들이 점들 사이로 선 하나를 쫙 긋는 마법, 바로 **'최소 제곱법'** 이라는 걸 발명해 냈습니다. 이게 바로 오늘날 우리가 지겹도록 쓰는 자막대기, **'선형 회귀'** 모형의 가장 시조새가 되는 형태였죠.

The approach was first successfully applied to problems in astronomy.
재밌는 건 이 수학적 마술 선 긋기가 처음 빙의해서 대박을 친 분야가 동네 장부가 아니라 밤하늘의 행성 궤도를 때려 맞추는 '천문학' 동네 문제였다는 겁니다. 스케일 장난 아니죠?

Linear regression is used for predicting quantitative values, such as an individual's salary.
현대판에서 이 '선형 회귀'라는 무기는 주로 그 사람의 직급을 보고 "너 이번 달 급여 얼마지?" 하고 숫자의 크기 자체(정량적 값)를 점쟁이처럼 때려 맞추는 데 쓰이고 있습니다.

In order to predict qualitative values, such as whether a patient survives or dies, or whether the stock market increases or decreases, *linear discriminant analysis* was proposed in 1936.
하지만 "살까 죽을까?", "주식이 떡상할까 떡락할까?" 같은 숫자가 아닌 무자비한 이지선다 팀 고르기(정성적 값, 분류) 상황이 오면 선형 회귀는 멍청해집니다. 이 사태를 구원하고자 1936년 할아버지들이 **'선형 판별 분석'** 이란 새로운 진영 가르기 무기를 세상에 투척했습니다.

In the 1940s, various authors put forth an alternative approach, *logistic regression*.
시간이 흘러 1940년대엔 세상의 똑똑한 학자들이 입을 모아 또 다른 팀 고르기의 전설, **'로지스틱 회귀'** 라는 대안적인 무기를 만들어 내며 O/X 퀴즈판의 강자로 등극시켰죠.

In the early 1970s, the term *generalized linear model* was developed to describe an entire class of statistical learning methods that include both linear and logistic regression as special cases.
그러다 1970년대 초반, 학자들이 귀찮으니 킹받게 쪼개져 있는 걸 하나로 묶어버립니다. 선형 회귀 할아버지랑 로지스틱 회귀 아저씨를 전부 자기들 밑에 두고 부하로 거느리는 왕좌의 단어, 바로 **'일반화 선형 모델(GLM)'** 이라는 폼나는 단어를 뽑아내어 통계판을 평정했습니다.

By the end of the 1970s, many more techniques for learning from data were available.
그리고 1970년대 말쯤엔, 기계가 데이터를 씹어 먹고 배우는 꽤나 그럴싸하고 다양한 기술들이 넘쳐나며 전성기를 맞기 시작했습니다.

However, they were almost exclusively linear methods because fitting non-linear relationships was computationally difficult at the time.
하지만 완전 치명적인 약점이 있었습니다! 당시 기법들은 거의 99% 뻣뻣한 '선형(직선)' 기법뿐이었습니다. 왜냐고요? 당시에는 저주받은 계산기 성능 때문에 뱀처럼 구불구불한 뼈대(비선형 관계)의 꼬인 데이터를 계산하려면 학자들이 늙어 죽을 만큼 미치도록 빡셌기(계산상 어려움) 때문입니다.

By the 1980s, computing technology had finally improved sufficiently that non-linear methods were no longer computationally prohibitive.
그러다 드디어 1980년대! 갓 컴퓨터 기술이 미친 듯이 점프업하면서 연산 능력이 향상되자, 그 구불구불한 뱀 뼈대(비선형 방법)를 계산하는 게 더 이상 "안 해! 못 해! 밥상 엎어!" 수준의 미친 불가능 성역이 아니게 되었습니다!

In the mid 1980s, *classification and regression trees* were developed, followed shortly by *generalized additive models*.
이 컴퓨팅 파워를 등에 업고 1980년대 중반, 나뭇가지 치둣 답을 고르는 잔머리의 대가 **'분류 및 회귀 트리'** 가 발명되었고, 곧이어 꼬인 선들의 종합 예술인 **'일반화 가법 모델(GAM)'** 이 세상의 빛을 보게 됩니다.

*Neural networks* gained popularity in the 1980s, and *support vector machines* arose in the 1990s.
거기다 지금도 유명한 알파고의 조상 격인 **'신경망(Neural networks)'** 이 1980년대에 아이돌급 인기를 누리며 떡상했고, 1990년대엔 수학의 끝판왕으로 불리는 선 긋기의 마술사 **'서포트 벡터 머신(SVM)'** 이 간지나게 등장했습니다.

Since that time, statistical learning has emerged as a new subfield in statistics, focused on supervised and unsupervised modeling and prediction.
이 르네상스 폭발 시기를 기점으로, 마침내 '통계적 기계 학습'은 단순히 옛날 통계의 끄나풀 정도가 아니라, 선생님 있는 지도 학습과 선생님 없는 비지도 학습을 아우르며 미래를 맞추는 통계학의 가장 핫한 신도시(새로운 하위 분야)로 대대적인 독립을 선언하게 됩니다. 

In recent years, progress in statistical learning has been marked by the increasing availability of powerful and relatively user-friendly software, such as the popular and freely available Python system.
바야흐로 지금! 최근 이 통계 판이 우주 대폭발을 겪고 있는 진짜 이유는 천재적인 공식 때문이 아닙니다. 바로 여러분도 공짜로 깔아서 남들 다 쓴다는 '파이썬(Python)'처럼 눈물 나게 강력하면서도 마우스 딸깍이면 돌아가는 미친 친절한 소프트웨어들이 개나 소나 쓸 수 있게 동네방네 풀렸기 때문이죠!

This has the potential to continue the transformation of the field from a set of techniques used and developed by statisticians and computer scientists to an essential toolkit for a much broader community.
이게 왜 쩌는 거냐고요? 아주 먼 옛날 눈알 빠지게 수식만 풀던 통계학자나 골방의 코딩 변태 컴퓨터 공학자들만의 그들만의 전유물(비밀 무기 세트)에서, 이제는 주식쟁이, 마케터, 의사 할 거 없이 온 동네 사람(더 넓은 커뮤니티)들이 당장 꺼내 써먹는 '필수 생존 도구 망치 세트'로 이 판을 영원히 뒤집어엎을 아주 강력한 폭탄(잠재력)을 품고 있다는 뜻입니다!

---

## Sub-Chapters (하위 목차)

[< 1.1 An Overview Of Statistical Learning](../1_1_an_overview_of_statistical_learning/trans2.html) | [1.3 This Book >](../1_3_this_book/trans2.html)
