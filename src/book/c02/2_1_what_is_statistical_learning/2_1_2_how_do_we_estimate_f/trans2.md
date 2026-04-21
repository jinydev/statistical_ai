---
layout: default
title: "trans2"
---

[< 2.1.1.1 Prediction](../2_1_1_why_estimate_f/2_1_1_1_prediction/trans2.html) | [2.1.2.1 Parametric Methods >](2_1_2_1_parametric_methods/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# 2.1.2 How Do We Estimate _f_?
# 2.1.2 우리는 어떻게 _f_ 를 유추해 내는가? (기계에게 과외시키기)

Throughout this book, we explore many linear and non-linear approaches for estimating _f_.
이 징글징글한 책을 끝까지 보시다 보면, 이 미지의 돗자리 함수 _f_ 를 베껴 그리기 위한 수많은 '직선(선형)' 방식들과 꼬불꼬불한 '곡선(비선형)' 방식들을 지겹도록 탐험하게 될 겁니다.

However, these methods generally share certain characteristics. We provide an overview of these shared characteristics in this section.
하지만 방법이 달라도 이 녀석들은 모델을 만드는 똑같은 '공통된 성질(습성)'을 하나 공유하고 있습니다. 이번 섹션에선 그 공통점의 뼈대를 살짝 보여드리겠습니다.

We will always assume that we have observed a set of _n_ different data points.
모든 통계 이야기의 시작은 언제나 똑같습니다. "자, 우리가 영혼을 끌어모아 만든 _n_ 명 분의 엑셀 데이터 파일(관측치)이 있다고 칩시다"라는 거죠.

For example in Figure 2.2 we observed _n_ = 30 data points.
예를 들어 아까 봤던 그림 2.2에서는, 동네 아저씨 _n_ = 30 명을 붙들고 억지로 얻어낸 데이터 점들이 있었죠.

These observations are called the _training data_ because we will use these training observations to train, or teach, our method how to estimate _f_.
이 _n_ 개의 데이터(과거의 정답지)들을 좀 멋있게 **'훈련 데이터(Training data)'** 라고 부릅니다. 왜냐고요? 이걸 컴퓨터 기계한테 "옛다, 오답 노트 가져다 풀어봐라!" 하고 반복적으로 던져주며, 어떻게든 기계가 짝퉁 함수 _f_ 를 빚어내도록 피 튀기게 가르치고(훈련하고) 굴릴 거니까요.

Let $x_{ij}$ represent the value of the _j_ th predictor, or input, for observation _i_, where $i = 1, 2, \dots, n$ and $j = 1, 2, \dots, p$. Correspondingly, let $y_i$ represent the response variable for the _i_ th observation.
복습 한번 해볼까요? $x_{ij}$ 는 엑셀 표에서 "$i$ 번째 아저씨의 $j$ 번째 힌트(예: 나이)" 칸에 적힌 숫자입니다. (당연히 아저씨는 1번부터 $n$ 번까지, 힌트 칸은 1번부터 $p$ 번까지 있죠). 그 줄 맨 끝에 적힌 진짜 정답(예: 월급)은 짝꿍처럼 $y_i$ 라고 부릅니다.

Then our training data consist of $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$ where $x_i = (x_{i1}, x_{i2}, \dots, x_{ip})^T$.
그러면 우리의 피 같은 훈련 데이터(오답 노트)는 결국엔 **{(1번 아저씨 힌트 뭉치, 1번 정답), (2번 아저씨 힌트 뭉치, 2번 정답), ...}** 이렇게 짝지어진 세트 메뉴 $n$ 그릇의 거대한 뷔페가 됩니다.

Our goal is to apply a statistical learning method to the training data in order to estimate the unknown function _f_.
우리가 해야 할 짓은 명확합니다. 이 거대한 오답 노트 뷔페(훈련 데이터)에 통계적 학습이라는 미친듯한 수학 믹서기를 들이대서 갈아버리고, 아직 아무도 본 적 없는 진리의 마법 공식 _f_ 의 복사본을 찍어내는(추정하는) 겁니다.

In other words, we want to find a function $\hat{f}$ such that $Y  pprox \hat{f}(X)$ for any observation $(X, Y)$.
다시 말해 우리 손으로 빚어 만든 짝퉁 함수 식(모자를 쓴 $\hat{f}$)에다가 미래의 새로운 힌트 $X$ 를 쑥 집어넣으면, 기가 막히게도 진짜 정답 $Y$ 랑 "거진 비슷하게($\approx$)" 숫자가 튀어나올 정도로 똑똑한 $\hat{f}$ 를 찾는 게 지상 목표입니다!

Broadly speaking, most statistical learning methods for this task can be characterized as either _parametric_ or _non-parametric_.
자, 이 짝퉁 함수를 찍어내는 통계 공장(수학적 기법들)은 크게 두 파벌로 갈라져서 싸웁니다. 한쪽은 뼈대를 세우고 시작하는 **모수적(parametric) 파벌**이고, 다른 한쪽은 자유영혼 인 **비모수적(non-parametric) 파벌**입니다. 

We now briefly discuss these two types of approaches.
이제 이 두 앙숙 파벌이 일하는 방식을 아주 짧게 썰을 풀어드리겠습니다.

---

### Parametric Methods (모수적 방법론: 틀에 박힌 옹고집)
처음부터 답을 정해놓고 시작합니다! "이 공식은 무조건 일직선일 거야!(형태 가정)" 라고 선을 긋고, 그 직선의 기울기 숫자(파라미터) 몇 개만 덜렁 찾아내는 식입니다.
그래서 계산은 엄청나게 빠르고 직관적이지만, 애초에 데이터가 일직선이 아니라 꼬불꼬불한 모양이었다면 완전히 똥볼을 차게 되는 치명적인 단점이 있습니다.

### Non-Parametric Methods (비모수적 방법론: 자유방임주의)
이 녀석들은 절대 형태를 미리 정하지 않습니다. "진짜 정답 _f_ 가 네모든 동그라미든 내가 알 바 아님!" 하고 쿨하게 데이터 점들을 따라 그냥 물 흐르듯 선을 미친 듯이 구불구불 이어버립니다(형태 가정 없음).
정말 정교하게 모양을 본뜰 순 있지만, 이 짓을 제대로 하려면 데이터가 몇 배로 엄청나게 무식하게 많이 필요하다는 게 함정입니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.1.1 Prediction](../2_1_1_why_estimate_f/2_1_1_1_prediction/trans2.html) | [2.1.2.1 Parametric Methods >](2_1_2_1_parametric_methods/trans2.html)
