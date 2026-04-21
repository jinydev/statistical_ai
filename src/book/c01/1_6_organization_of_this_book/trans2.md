---
layout: default
title: "trans2"
---

[< 1.5 Notation And Simple Matrix Algebra](../1_5_notation_and_simple_matrix_algebra/trans2.html) | [1.7 Data Sets Used In Labs And Exercises >](../1_7_data_sets_used_in_labs_and_exercises/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# Organization of This Book
# 책의 구성 (이 두꺼운 책을 어떻게 씹어 먹을 것인가?)

Chapter 2 introduces the basic terminology and concepts behind statistical learning.
자, 2장으로 넘어가면 제일 먼저 뭐부터 하느냐? 이 바닥 사람들이 폼잡고 쓰는 외계어(기본 용어)들과 "로봇은 어떻게 배우는가?"에 대한 진짜 뼈대 개념들을 탈탈 털어드립니다.

This chapter also presents the $K$-nearest neighbor classifier, a very simple method that works surprisingly well on many problems.
여기서 덤으로 아까 구경했던 동네 친구 수 세는 다수결 무기! 그 멍청할 정도로 단순하지만 의외로 실전에서 개쩌는 성능력(놀랍도록 잘 작동함)을 발휘하는 **$K$-최근접 이웃 분류기(KNN)** 라는 기계도 살짝 공개합니다.

Chapters 3 and 4 cover classical linear methods for regression and classification.
본격적인 막노동의 시작, 3장과 4장에서는 할아버지 시대의 유물(고전적인 선형 방법)들을 몽땅 끌어와서, 어떻게 숫자를 때려 맞추는지(회귀)와 흑백 진영을 가르는지(분류)를 빡세게 배웁니다.

In particular, Chapter 3 reviews linear regression, the fundamental starting point for all regression methods.
특히 3장은 무조건 달달 외우셔야 합니다. 이 세상에 존재하는 모든 수치 맞추기(회귀 기법) 로봇들의 기원이자 할아버지 뻘인 **'선형 회귀'** 를 처음 뼈대부터 다시 발가벗기고 복습할 거니까요.

In Chapter 4 we discuss two of the most important classical classification methods, logistic regression and linear discriminant analysis.
그리고 4장에 넘어가면 이번엔 무자비한 이분법 팀 고르기(분류법) 동네의 고전 양대 산맥인 **'로지스틱 회귀'** 랑 **'선형 판별 분석'** 두 마리의 보스 몹을 까놓고 철저하게 해부(논의)해 봅니다.

A central problem in all statistical learning situations involves choosing the best method for a given application.
근데 여기까지 배우면 여러분 뇌정지가 올 겁니다. "아니, 무기가 이렇게 많은데 당장 내 회사 데이터에는 무슨 무기를 써야 (최상의 분석 기법을 선택) 제일 대박이 터지냐?" 바로 이게 평생 통계쟁이들 골을 울리게 하는 핵심 딜레마(가장 중요한 문제) 거든요.

Hence, in Chapter 5 we introduce cross-validation and the bootstrap, which can be used to estimate the accuracy of a number of different methods in order to choose the best one.
그래서 5장에서 우리는 기막힌 잔머리를 발동합니다! 여러 무기들을 돌아가며 써보고 "누가 젤 쎈가?"하고 모의 전투 성적을 미리 예습(정확도 추정)해서 단 하나의 엑스칼리버(최선)를 뽑아내는 마법의 신기술! **'교차 검증(Cross-validation)'** 과 이름부터 폼나는 **'붓스트랩(Bootstrap)'** 을 꺼내 듭니다!

Much of the recent research in statistical learning has concentrated on non-linear methods.
요즘 유튜브에서 떠드는 딥러닝 같은 최신 연구들은 죄다 뱀처럼 구불구불한 뼈대를 다루는(비선형) 간지나는 무기들에만 스포트라이트를 쏘아대고(집중하고) 있습니다.

However, linear methods often have advantages over their non-linear competitors in terms of interpretability and sometimes also accuracy.
근데 역설적이게도 팩폭을 날리자면, 저 구닥다리 뻣뻣한 작대기(선형 기법)들이 비선형 놈들과 맞짱 떴을 때 "내가 왜 이렇게 예측했는지 설명해 보라!"(해석 가능성)는 압박 면접에서는 압도적으로 말을 잘하고, 심지어 가끔은 쓸데없이 더 정확(정확도)하기까지 하다는 미친 반전(우위 이점)이 존재하죠! 

Hence, in Chapter 6 we consider a host of linear methods, both classical and more modern, which offer potential improvements over standard linear regression.
그래서 6장에선 이 구닥다리 선형 무기의 끝판왕 업그레이드 버전들을 싹 다 모아놓고 리뷰합니다. 옛날 꼰대 기술과 최신 장비들을 합쳐서, 오리지널 선형 회귀보다 딜이 훨씬 잘 박히는(잠재적 성능 개량) 온갖 무기 박람회를 열어볼 겁니다.

These include stepwise selection, ridge regression, principal components regression, and the lasso.
그 무기들의 찬란한 이름이 뭐냐고요? **'단계적 변수 선택법'**, 구불구불한 언덕을 타는 **'릿지 회귀'**, 가장 중요한 뼈대만 추리는 **'주성분 회귀'**, 그리고 서부의 올가미(Lasso)처럼 쓸데없는 변수를 목 졸라 죽이는 **'라쏘 회귀'** 등등의 멋진 라인업을 세워둡니다.

The remaining chapters move into the world of non-linear statistical learning.
자, 6장까지 버티신 분들 축하합니다! 이제 남은 챕터들부터는 어지럽고 미친 듯이 복잡하게 꼬인 뱀소굴, **'비선형 우주'** 로 진입하게 됩니다. 

We first introduce in Chapter 7 a number of non-linear methods that work well for problems with a single input variable.
일단 7장에서 그나마 순한 맛 비선형 기법부터 찍먹해 봅니다. 힌트(입력 변수)가 달랑 한 개인 단순한 문제 하나만 던져주고, 기계가 어떻게 뱀처럼 유연하게 선을 꼬아서 잘 맞추는지(잘 작동하는지) 여러 로봇들을 구경시켜 줍니다.

We then show how these methods can be used to fit non-linear additive models for which there is more than one input.
그러고 나서 "오케이 감 잡았어?" 싶으면 힌트를 여러 개(다중 입력)로 확 늘려버립니다. 그렇게 마구 들어오는 여러 힌트들을 어떻게 구불구불한 통구이 꼬챙이(비선형 가법 모델)로 하나하나 꿰어야 찰떡같이 척척 들어맞게 쌓는지(적합시킬 수 있는지) 그 신들린 컨트롤 과정을 생방송으로 보여드릴 겁니다.

In Chapter 8, we investigate tree-based methods, including bagging, boosting, and random forests.
8장에 가면 이제 선 긋는 건 포기하고 나뭇가지 치기(트리 기반) 놀이에 돌입합니다. 질문을 스무고개처럼 던져서 싹둑싹둑 쪼개 내려가는 기법들인데, 여기엔 나무를 여러 개 합쳐 힘을 합치는 **배깅(Bagging)** 부터 성능을 끝없이 쥐어짜 올리는 **부스팅(Boosting)**, 그리고 기계 학습의 국밥 같은 존재 **랜덤 포레스트(Random forests)** 까지 온갖 숲속의 괴물 체계들을 탈탈 털어봅니다.

Support vector machines, a set of approaches for performing both linear and non-linear classification, are discussed in Chapter 9.
9장은 선을 긋든 고함을 동그랗게 치든(선형 및 비선형) 팀 편 가르기(분류)에서만큼은 그 어떤 괴물도 다 두들겨 패버리는 세계관 넘버원 깡패! **'서포트 벡터 머신(SVM)'** 형님에 대해 아주 진지하게 영접(논의) 하는 시간을 가집니다.

We cover deep learning, an approach for non-linear regression and classification that has received a lot of attention in recent years, in Chapter 10.
그리고 10장! 드디어 뉴스에서 지겹도록 떠드는 바로 그 인공지능의 꽃, **'딥러닝(Deep Learning)'** 입니다. 그동안 세상을 들었다 놨다 하며 온갖 어그로와 찬사(막대한 관심)를 한 몸에 받았던, 숫자를 찍든 분류를 하든 미친듯한 퍼포먼스를 내는 이 끝판왕 괴물 로봇을 심도 있게 까발립니다.

Chapter 11 explores survival analysis, a regression approach that is specialized to the setting in which the output variable is censored, ie not fully observed.
11장에서는 병원 의사 선생님들이 제일 킹받아하는 변태 같은 상황(결과가 도중에 짤림, 검열, 안 보임)을 수리하기 위해 파생된 암울한 기술, 즉 사람이 언제 죽는지 도중에 관찰을 놓치거나(검열된 출력 변수) 튀어버린 경우에만 오타쿠처럼 특화된 기이한 통계 마법, **'생존 분석(Survival analysis)'** 이라는 기법을 탐험합니다.

In Chapter 12, we consider the unsupervised setting in which we have input variables but no output variable.
마침내 12장으로 가볼까요? 여기는 정답을 가르쳐주는 친절한 선생님(출력 변수) 따위는 통째로 증발해 버린 고아원(비지도 학습) 판입니다. 오로지 막막한 힌트(입력) 뭉치만 쥐여주고 기계 스스로 깨우쳐야 하는 극한의 방목 환경을 마주해 봅니다.

In particular, we present principal components analysis, $K$-means clustering, and hierarchical clustering.
선생님이 없으면 스스로 조폭 패거리(클러스터 파벌)라도 만들어야죠! 그래서 이런 개판 상황에서 빛을 발하는 차원 압축기 **'주성분 분석'**, 동네 아이들 패거리 묶는 대장 로봇 **'$K$-평균 군집화'**, 그리고 나무처럼 가지를 치며 올라가는 **'계층적 군집화'** 같은 멋진 패거리 형성 무기들을 꺼냅니다.

Finally, in Chapter 13 we cover the very important topic of multiple hypothesis testing.
그리고 이 장대한 서사시의 진짜 마지막 무대! 13장에서는 데이터 분석가들이 평생을 시달리며 삽질하게 되는 통계의 영원한 숙제, 수십 수백 개의 질문을 한꺼번에 던지고 뒷수습을 어찌할지(다중 가설 검정) 고민하는 골 때리는 훈련 과정을 치러낼 겁니다.

At the end of each chapter, we present one or more Python lab sections in which we systematically work through applications of the various methods discussed in that chapter.
자, 근데 입으로만 털면 노잼이잖아요? 각 챕터가 끝날 때마다 "야, 너 코딩 켜봐!" 하고 준비된 진짜배기 '파이썬(Python) 실습 놀이터(Lab)' 세션을 무조건 붙여 놨습니다. 배운 이론을 현실 데이터 샌드백에 꽂아 넣고 돌려보는 통쾌한 코딩 폭행 시스템(응용 작업)이 체계적으로 돌아갑니다.

These labs demonstrate the strengths and weaknesses of the various approaches, and also provide a useful reference for the syntax required to implement the various methods.
이 놀이터에서 직접 코드를 쳐보고 삽질해 보면 "아, 이 로봇은 여긴 개쩌는데 이 부분엔 약골이네(장단점 입증)!" 하는 팩트 폭행을 몸소 깨닫게 됩니다. 더불어 당장 회사 가서 그 로봇을 소환할 때 쓰는 마법 주문(필수 코드 문법 족보)까지 낭낭하게 챙겨드린다는 사실 잊지 마세요. 

The reader may choose to work through the labs at their own pace, or the labs may be the focus of group sessions as part of a classroom environment.
독자분들 맘입니다! 삘받을 때 혼자 안방에서 배 긁으며(자신의 속도로) 랩을 치며 돌리든, 아니면 스터디 부원들이랑 강의실에 모여 앉아서 "야 이 코드 왜 에러 나냐?" 하고 멱살 잡고 토론하는 피 튀기는 단체전 집중 과제로 써먹든, 알아서 푹 고아서 쓰십시오!

Within each Python lab, we present the results that we obtained when we performed the lab at the time of writing this book.
아, 그리고 그 놀이터 코드 바로 밑에는 저희가 이 책을 처음 쥐어짜면서 피땀 흘려 돌렸을 당시 컴퓨터 화면에 뿅 하고 떴던 '진짜 결괏값'들을 증거 사진 찍듯이 고스란히 박아놨습니다.

However, new versions of Python are continuously released, and over time, the packages called in the labs will be updated.
근데 여러분도 알다시피 코딩 바닥의 생태계는 미쳐 돌아가서(계속 출시됨), 세월이 지나면 파이썬 버전도 갈아 엎어지고 우리가 불러온 남의 집 족보(외부 패키지)들도 버전업하며 지 맘대로 막 업데이트가 될 겁니다.

Therefore, in the future, it is possible that the results shown in the lab sections may no longer correspond precisely to the results obtained by the reader who performs the labs.
그러다 보니 훗날 먼 미래의 여러분이 우리 코드를 똑같이 복붙해서 친다 한들, 책에 박힌 옛날 화석 결과물(표시된 결과값)이랑 여러분 모니터에 뜬 지금 결과가 "어? 소수점이 다른데?" 하면서 서로 엇나가고 배신을 때릴 무서운 가능성이 항상 도사리고 있습니다!

As necessary, we will post updates to the labs on the book website.
그래서 만약 그런 빡치는 코드 통수(에러 및 변화)가 터지면 수시로 패치 버전 만들어서 홈페이지에다 AS 공지사항 띄워 둘 테니 제발 욕하지 말고 홈페이지 좀 와주세요!

We use the * symbol to denote sections or exercises that contain more challenging concepts.
마지막 경고 기호! 책을 넘기다 가끔 징그럽게 생긴 **별표( * )** 딱지가 붙은 고약한 챕터나 무서운 문제들을 보게 될 겁니다. 조심하세요, 거긴 수학 귀신들이 득실거리는 미친 심연(더 도전적인 고난도)의 구역이라는 뜻입니다!

These can be easily skipped by readers who do not wish to delve as deeply into the material, or who lack the mathematical background.
수학 공포증이 있거나 "난 적당히 하고 꿀 빨래!" 하는 분들은 쫄지 마세요. 그 별표 밭은 그냥 개무시하고 가위로 오려내듯(가뿐하게 건너뛰어도) 쿨하게 스킵해도 다음 장 넘어가는데 아무도 수갑 안 채웁니다! 목숨 걸지 마세요!

---

## Sub-Chapters (하위 목차)

[< 1.5 Notation And Simple Matrix Algebra](../1_5_notation_and_simple_matrix_algebra/trans2.html) | [1.7 Data Sets Used In Labs And Exercises >](../1_7_data_sets_used_in_labs_and_exercises/trans2.html)
