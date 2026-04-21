---
layout: default
title: "trans2"
---

[< 2.1.1 Why Estimate F](../trans2.html) | [2.1.2 How Do We Estimate F >](../../2_1_2_how_do_we_estimate_f/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# Prediction
# 예측 (과격한 점쟁이 모드)

In many situations, a set of inputs _X_ are readily available, but the output _Y_ cannot be easily obtained.
현실에선 흔히 이런 빡치는 상황이 연출됩니다. 우리가 쥔 힌트 보따리 _X_ 들은 인터넷이나 서류 뭉치에 널리고 널렸는데, 정작 우리가 제일 알고 싶어 안달이 난 정답 _Y_ (예: 주가 변동, 환자의 병명)는 도무지 구하기 힘든 경우 말입니다.

In this setting, since the error term averages to zero, we can predict _Y_ using
이런 골치 아픈 세팅에서는 찌꺼기 운빨(오차 항)들의 깽판을 싹싹 모아 평균 내면 어차피 플러스마이너스 제로(0)로 녹아 없어진다고 믿고, 우린 대범하게 다음처럼 짝퉁 수식을 돌려 _Y_ 를 예측해 버립니다.

$$ \hat{Y} = \hat{f}(X) \tag{2.2} $$

where $\hat{f}$ represents our estimate for _f_, and $\hat{Y}$ represents the resulting prediction for _Y_.
여기서 모자(기호)를 뒤집어쓴 $\hat{f}$ 는 "우리가 대충 빚어낸 짝퉁 함수 $f$"라는 뜻이고, 모자를 쓴 $\hat{Y}$ 도 마찬가지로 "이 짝퉁 함수를 돌려 찍은 야매 정답(예측값) _Y_"라는 뜻입니다.

In this setting, $\hat{f}$ is often treated as a _black box_, in the sense that one is not typically concerned with the exact form of $\hat{f}$, provided that it yields accurate predictions for _Y_.
예측 모드에서 이 짝퉁 $\hat{f}$ 는 일명 수상한 **'블랙박스(black box)'** 라 불리며 까방권(까임 방지권)을 얻게 됩니다. 왜냐고요? 안에서 무슨 더러운 꼼수를 쓰든 겉으로 _Y_ 예측값 하나만 기가 막히게 잘 맞추면 그만이라, 굳이 속을 뜯어보고 싶어 하지 않거든요.

As an example, suppose that $X_1, \dots, X_p$ are characteristics of a patient’s blood sample that can be easily measured in a lab, and _Y_ is a variable encoding the patient’s risk for a severe adverse reaction to a particular drug.
예를 하나 들어보죠. 환자의 피를 뽑아서 동네 병원 기계에 휙 돌리면 나오는 온갖 수치 힌트들이 $X_1, \dots, X_p$ 라 칩시다. 반면에 _Y_ 는 이 환자에게 특정 약을 먹였을 때 쇼크사(부작용) 할 심각한 위험도를 뜻합니다.

It is natural to seek to predict _Y_ using _X_, since we can then avoid giving the drug in question to patients who are at high risk of an adverse reaction—that is, patients for whom the estimate of _Y_ is high.
그럼 당연하게도 피검사 힌트(_X_)만으로 쇼크사 위험도(_Y_)를 기가 막히게 미리 맞춰보고 싶지 않겠습니까? 이 예측 수치(우리가 만든 짝퉁 모자 $\hat{Y}$)가 높게 뜬 환자들에겐 무서워서 약을 처방 안 할 수 있으니까 사람을 살리는 겁니다!

The accuracy of $\hat{Y}$ as a prediction for _Y_ depends on two quantities, which we will call the _reducible error_ and the _irreducible error_.
그런데 이 야매 정답 $\hat{Y}$ 가 얼마나 진짜에 가까운지 그 '정확도'는, 우리가 줄일 수 있는 **'내 실력 탓(reducible error)'** 과 죽었다 깨어나도 못 잡는 **'우주의 운빨 탓(irreducible error)'** 이라는 두 가지 고질병에 시달리게 됩니다.

In general, $\hat{f}$ will not be a perfect estimate for _f_, and this inaccuracy will introduce some error.
당연한 말이지만, 우리가 아무리 머리를 굴려 $\hat{f}$ 를 찍어내도 그건 절대 신의 완벽한 돗자리 _f_ 가 될 수 없으므로 무조건 삐끗하는 오차가 발생하게 마련입니다.

This error is _reducible_ because we can potentially improve the accuracy of $\hat{f}$ by using the most appropriate statistical learning technique to estimate _f_.
하지만 이 오차는 우리의 피땀 눈물인 '개선 가능한 실력 탓(reducible error)'입니다. 왜냐하면 우리가 더 쩔어주는 통계 학습 기법을 밤새워 돌리면 $\hat{f}$ 가 진품 _f_ 랑 한 발짝 더 가까워질 수 있는 여지라도 남아있기 때문이죠.

However, even if it were possible to form a perfect estimate for _f_, so that our estimated response took the form $\hat{Y} = f(X)$, our prediction would still have some error in it!
그러나! 백번 양보해서 여러분이 노벨상을 받아 기적처럼 완벽한 신의 돗자리 함수 식 $\hat{Y} = f(X)$ 를 찾아냈다 쳐봅시다. 그래도 우리의 예측은 무조건 가끔 틀리는 개싸가지 없는 오차를 냅니다!

This is because _Y_ is also a function of $\epsilon$, which, by definition, cannot be predicted using _X_.
왜냐하면 진짜 정답 _Y_ 속에는 태생적으로 _X_ (우리가 가진 힌트들)랑은 전혀 무관하게 독립적으로 지멋대로 날뛰는 미친 찌꺼기 운빨 변수 $\epsilon$ 이 한 스푼 섞여 들어가서 작용하고 있기 때문이죠.

Therefore, variability associated with $\epsilon$ also affects the accuracy of our predictions.
고로 이 찌꺼기 $\epsilon$ 이 기분에 따라 변덕스럽게 털털거리는 그 진동(변동성) 때문에 예측 정확도에 알 수 없는 흠집이 새겨지게 됩니다.

This is known as the _irreducible_ error, because no matter how well we estimate _f_, we cannot reduce the error introduced by $\epsilon$.
이게 바로 그 악명 높은 **'줄일 수 없는 탓(irreducible error)'** 입니다. 우리가 _f_ 를 천재같이 찾아내도, 이 빌어먹을 운빨 찌꺼기가 일으키는 에러 파동은 절대로 통제하거나 뭉갤 수 없습니다.

Why is the irreducible error larger than zero?
아니 그럼 도대체 왜 이 운빨 에러는 0으로 싹 안 없어지고 남아있는 걸까요? 

The quantity $\epsilon$ may contain unmeasured variables that are useful in predicting _Y_: since we don't measure them, _f_ cannot use them for its prediction.
비밀을 까보자면, 이 거대한 우주의 찌꺼기 덩어리 $\epsilon$ 에는 사실 우리가 정답 _Y_ 를 맞추는 데 아주 요긴하지만 우리가 "귀찮아서, 몰라서" 측정하지 못하고 놓쳐버린 숨은 힌트들(unmeasured variables)이 버려져 있기 때문입니다. 내 장부에 안 쓰여 있으니 짝퉁 _f_ 가 그걸 볼 수조차 없는 거죠.

![Figure 2.3](./img/Image_017.png)

**FIGURE 2.3.** _The plot displays_ `income` _as a function of_ `years of education` _and_ `seniority` _in the_ `Income` _data set. The blue surface represents the true underlying relationship between_ `income` _and_ `years of education` _and_ `seniority`, _which is known since the data are simulated. The red dots indicate the observed values of these quantities for 30 individuals._

**그림 2.3.** _앞서 보았던 대형 `수입(Income)` 장부 그림입니다. '가방끈(교육)'과 '짬바(연공서열)' 두 가지 힌트가 들어오니 신의 함수 _f_ (파란색)가 2차원 돗자리 모양으로 펄럭입니다 이 펄럭이는 파란 돗자리는 조물주인 우리가 시뮬레이션으로 조작해서 모양을 아는 거지 현실에선 절대 안 보입니다. 빨간 점들은 그 도자리 근처에서 둥둥 떠다니는 현실의 30명 아저씨들 데이터입니다._

The quantity $\epsilon$ may also contain unmeasurable variation.
게다가 저 찌꺼기 $\epsilon$ 안에는 애초에 인간이 자(ruler)로 잴 수 없는 '도깨비 같은 변동성'도 숨어있습니다.

For example, the risk of an adverse reaction might vary for a given patient on a given day, depending on manufacturing variation in the drug itself or the patient’s general feeling of well-being on that day.
예를 들면 투약 전에 환자의 피를 뽑아서 멀쩡했어도, 그날 약 공장에서 유독 알약에 실수로 가루 하나를 덜 넣었을지, 아니면 그날 아침에 길 가다 환자가 개똥을 밟아서 기분이 잡치는 바람에 스트레스로 혈압이 뛰어 부작용 쇼크가 터질지... 이런 말도 안 되는 우주의 기운(변동)들이 얽혀 있다는 뜻입니다.

Consider a given estimate $\hat{f}$ and a set of predictors _X_, which yields the prediction $\hat{Y} = \hat{f}(X)$.
자, 이제 방금 설명한 걸 증명하기 위해, 우리의 작고 소중한 예측값 $\hat{Y} = \hat{f}(X)$ 하나를 꺼내봅시다.

Assume for a moment that both $\hat{f}$ and _X_ are fixed, so that the only variability comes from $\epsilon$.
우리가 천재라서 짝퉁 $\hat{f}$ 와 힌트 보따리 _X_ 를 아예 벽에 못 박아 고정(완벽하게 찾음)시켜버렸다고 아주 낙관적인 망상을 해봅시다. 이제 널뛰는 놈은 찌꺼기 $\epsilon$ 밖에 없습니다.

Then, it is easy to show that
그럼 예측이 얼마나 쓰레기같이 틀릴지 오차의 크기를 아주 쉽게 까볼 수 있습니다:

$$
\begin{align*}
E(Y - \hat{Y})^2 &= E[f(X) + \epsilon - \hat{f}(X)]^2 \\
&= [f(X) - \hat{f}(X)]^2 + \text{Var}(\epsilon)
\end{align*} \tag{2.3}
$$

where $E(Y - \hat{Y})^2$ represents the average, or _expected value_, of the squared difference between the predicted and actual value of _Y_, and $\text{Var}(\epsilon)$ represents the _variance_ associated with the error term $\epsilon$.
위 외계어 식에서 $E(Y - \hat{Y})^2$ 는 쉽게 말해 "(내 예측 - 찐 정답)을 제곱해서 넓힌 엄청난 차이의 오차 기댓값"이라는 뜻입니다. 그리고 뒤에 살포시 덤으로 더해져 있는 끈질긴 짐덩어리 $\text{Var}(\epsilon)$ 이 바로 찌꺼기 $\epsilon$ 의 잡음 정도(분산)를 의미하죠. 저 분산(운빨 오차)은 무조건 플러스 덤이기 때문에 에러가 0이 될 수가 없습니다!

The focus of this book is on techniques for estimating _f_ with the aim of minimizing the reducible error.
그러니 이제 포기할 건 통쾌하게 포기합시다! 이 두꺼운 책의 목표는 우주의 운빨에 대들려는 게 아니라, 그 수식 뒷부분의 덤을 뺀 앞부분, 즉 **내 실력 탓(reducible error) 부분의 오차 크기를 어떻게든 병적으로 깎아내서 최소화**시키는 통계적 꼼수들을 연마하는 것입니다!

It is important to keep in mind that the irreducible error will always provide an upper bound on the accuracy of our prediction for _Y_.
다만 겸손하게 마음속에 새겨둬야 할 씁쓸한 교훈 한 줄. 그 빌어먹을 '우주 운빨 오차(irreducible error)' 덕분에 우리가 세상에서 제일 비싼 슈퍼컴퓨터를 가져다 예측 모델을 짜더라도 뚫을 수 없는 **우주적 한계(천장)** 가 있다는 사실입니다.

This bound is almost always unknown in practice.
물론 가장 빡치는 건 현실 세계 어디를 뒤져봐도 저 운빨 찌꺼기가 과연 도대체 몇 퍼센트인지 한계선의 퍼센티지는 아무도 모른다는 사실이죠. 

# Inference
# 추론 (왜 그런가 따져 묻는 명탐정 모드)

We are often interested in understanding the association between _Y_ and $X_1, \dots, X_p$.
우린 그냥 눈 감고 정답 _Y_ 만 맞추면 시시하다고 느낄 때가 엄청 많습니다. 도대체 힌트 뭉치 $X$ 들이랑 결과 덩어리 _Y_ 사이에 무슨 더러운 커넥션(연관성)이 오가는 건지 깊숙이 들여다보고 싶어 안달이 날 때가 있죠.

In this situation we wish to estimate _f_, but our goal is not necessarily to make predictions for _Y_.
이럴 땐 $\hat{f}$ 를 추정하는 건 똑같지만, 당장 "내일 매출 얼마야?" 하고 찍어 맞추는 건 우리의 메인 퀘스트가 아닙니다. 

Now $\hat{f}$ cannot be treated as a black box, because we need to know its exact form.
아까처럼 $\hat{f}$ 를 더러운 블랙박스 방패 뒤에 숨길 수 없습니다! 이제 $\hat{f}$ 속의 톱니바퀴가 도대체 서로 어떻게 맞물려 돌아가는지 그 적나라한 해부도를 우리가 두 눈 뜨고 똑똑히 알아야 하거든요.

In this setting, one may be interested in answering the following questions:
이렇게 '명탐정 모드(추론)'로 설정하면, 우리는 이런 꼬투리를 잡고 취조실에서 물어보는 질문들에 답변하는 것에 열광하게 됩니다:

- _Which predictors are associated with the response?_
- _야, 니들(예측 변수들) 중에 도대체 누가 진짜 결과(응답)를 만들어낸 주범이냐?_

It is often the case that only a small fraction of the available predictors are substantially associated with _Y_.
놀랍게도, 우리가 끌어모은 수십, 수백 개의 힌트 변수들 중에서 진짜 정답 _Y_ 랑 끈끈한 관계를 맺은 실세 주범은 아주 극소수의 떨거지에 불과할 때가 수두룩합니다. 쓸데없는 힌트들이 잡범 노릇을 하고 있죠.

Identifying the few _important_ predictors among a large set of possible variables can be extremely useful, depending on the application.
이렇듯 쓰레기장마냥 널려있는 변수들 틈바구니에서 가장 심장같이 중요한 **'알짜 힌트 놈들'** 서너 개만 기가 막히게 지목해서 뽑아내는 건, 실무 현장에선 정말 미칠 듯이 소름 돋게 유용한 기술입니다.

- _What is the relationship between the response and each predictor?_
- _그래서, 그 결과(응답)랑 각 힌트들 사이가 무슨 원수지간이냐, 짱친이냐?_

Some predictors may have a positive relationship with _Y_, in the sense that larger values of the predictor are associated with larger values of _Y_.
어떤 힌트 놈들은 정답 _Y_ 와 '짱친(양의 방향)'일 수도 있습니다. 즉, 그 힌트 값이 하늘로 쭉 오르면 정답 _Y_ 값도 신나서 덩달아 하늘로 쭉 떡상하는 관계 말입니다.

Other predictors may have the opposite relationship.
반면 다른 어떤 힌트 놈들은 원수지간(음의 방향)이어서 반대로 쥐어패고 떨어지는 효과만 가져올 수도 있죠.

Depending on the complexity of _f_, the relationship between the response and a given predictor may also depend on the values of the other predictors.
심지어 신의 함수 _f_ 가 뒤틀리게 변태처럼 복잡해지면, 이 두 놈의 1:1 관계조차도, 제3자 힌트 놈이 눈치 없게 값이 끼어들 때마다 둘의 우정이 하루아침에 원수로 홱홱 변하기도 합니다 (전문 용어로 상호작용).

- _Can the relationship between Y and each predictor be adequately summarized using a linear equation, or is the relationship more complicated?_
- _결과 _Y_ 랑 힌트들 사이 관계를 걍 깔끔하게 일직선(선형)으로 칠보단장해버려도 될까, 아님 미친 듯이 복잡하게 구불거리는 진상 관계일까?_

Historically, most methods for estimating _f_ have taken a linear form.
역사적으로 통계학 할배들은 머리가 아파서 _f_ 를 추정할 때 그냥 아주 단순하고 무식한 '반듯한 일직선(linear)' 모양으로 때워버렸습니다.

In some situations, such an assumption is reasonable or even desirable.
가끔은 이런 반듯한 직선 가정이 아주 신의 한 수처럼 합리적일 때도 있고, 심지어 사장님한테 설명하고 결재받기가 편해서 더 환영받기도 합니다. 

But often the true relationship is more complicated, in which case a linear model may not provide an accurate representation of the relationship between the input and output variables.
하지만 애석하게도 현실의 진짜 관계란 건 미칠 듯이 구불거리는(복잡한) 경우가 다반사입니다. 그럴 때 직선같이 딱딱한 자를 들이밀면, 원인과 결과의 진짜 끈적함을 전혀 묘사하지 못하고 그냥 개소리가 될 뿐입니다.

In this book, we will see a number of examples that fall into the prediction setting, the inference setting, or a combination of the two.
이제 이 책에서 우리는 "오로지 결과만 맞춰라!" 하는 예측 모드, "원인을 캐물어라" 하는 추론 모드, 아니면 짬짜면처럼 둘을 섞어놓은 반반 무 많이 모드 등등 수많은 끔찍한 실전 사례들을 구경할 겁니다.

For instance, consider a company that is interested in conducting a direct-marketing campaign.
우선 어떤 화장품 회사가 주부들을 겨냥해 우편물 광고지(다이렉트 서신)를 막 뿌리는 이벤트를 한다고 쳐보죠.

The goal is to identify individuals who are likely to respond positively to a mailing, based on observations of demographic variables measured on each individual.
회사의 최대 목표는 아줌마들 호구조사 내역(인구통계 변수 힌트)들을 쓱 스캔해 본 다음, 우편을 보내면 덥석 낚여 돈을 쓸(긍정적으로 타오르는) 진상 호구 아줌마 리스트만 딱 식별해 찍어내는 겁니다.

In this case, the demographic variables serve as predictors, and response to the marketing campaign (either positive or negative) serves as the outcome.
이 세팅에선 그 아줌마들의 프로필 정보가 입력 힌트(예측 변수) 역할을 하고, 편지를 받아서 찢어버릴지 살지 그 물건 구매 여부(긍정/부정)가 최종 결괏값이 되는 겁니다.

The company is not interested in obtaining a deep understanding of the relationships between each individual predictor and the response; instead, the company simply wants to accurately predict the response using the predictors.
근데 회사 입장에서 "어느 동네 아줌마는 학력이 높아서 마케팅 심리가 블라블라..." 이딴 깊은 고찰의 원인(자세한 관계 이해)을 깨닫고 철학자가 되는 덴 1도 관심이 없습니다! 회사는 그저 힌트 변수들을 보고 "얘가 사? 안 사?" 이것만 오차 없이 미친 듯이 칼같이 뽑아내고(예측) 싶을 뿐입니다. 

This is an example of modeling for prediction.
이게 바로 앞뒤 안 재고 그냥 과녁만 무자비하게 맞추는 전형적인 **예측(Prediction)** 전용 모델링 사례입니다!

In contrast, consider the `Advertising` data illustrated in Figure 2.1.
분위기를 싹 바꿔서, 다른 회사의 이야기인 그림 2.1의 `Advertising(광고)` 회사 장부를 기억해 봅시다.

One may be interested in answering questions such as:
여기서 짱돌을 굴리는 깐깐한 어떤 분(대표님)은 이런 질문 폭탄을 던지고 싶어 미칠 겁니다:

- _Which media are associated with sales?_
- _야, (수많은 돈 먹는 하마들 중) 도대체 어느 매체(TV, 라디오 등)가 우리 매출을 끌어올린 은인이냐?_

- _Which media generate the biggest boost in sales?_ or
- _그 은인 매체들 중에서, 또 어느 매체에 돈을 태웠을 때 제일 미친듯한 매출 폭발(부스트 업)을 주냐?_ 혹은

- _How large of an increase in sales is associated with a given increase in TV advertising?_
- _만약 내가 너한테 TV 광고비로 천만 원을 딱 늘려주면(주어진 증가), 정확히 매출은 현금 얼마치 정도 벌어다 줄 건데?_

This situation falls into the inference paradigm.
이런 끔찍한 질문 공세가 나오는 깐깐한 회의실 풍경, 이게 바로 **추론(Inference)** 이라는 지독한 패러다임의 전쟁터입니다!

Another example involves modeling the brand of a product that a customer might purchase based on variables such as price, store location, discount levels, competition price, and so forth.
하나 더 해볼까요? 소비자가 슈퍼에 가서 어느 브랜드 과자를 고를지를 맞추기 위해, 과자 가격 힌트, 진열대 목 좋은 위치, 세일 할인율, 라이벌 과자의 경쟁 가격 등 잡다한 변수들을 모아 모델을 짠다고 상상해보죠.

In this situation one might really be most interested in the association between each variable and the probability of purchase.
이러면 회사는 단순히 결과를 맞추는 걸 넘어서, "오? 각 힌트 요소들 하나하나가 과연 그 지갑을 여는 '구매 확률 점수'를 얼마나 후벼 파고 흔드는지" 개별 연관성에 피가 끓도록 진짜 너무나 관심이 갈 겁니다.

For instance, _to what extent is the product’s price associated with sales?_
"과자값을 100원만 살짝 내려치면, 우리 판매량이 도대체 어느 한도 퍼센트까지 떡상하는가?" 이런 질문처럼 말이죠.

This is an example of modeling for inference.
자, 이런 집요한 원인 파헤치기 역시 아주 정석적인 **추론(Inference)** 목적의 모델 구축 사례입니다!

Finally, some modeling could be conducted both for prediction and inference.
마지막으로, 욕심 많은 어른들처럼 예측(찍어맞추기)과 추론(원인 묻기) 두 마리 토끼를 다 잡으려고(섞어 짬뽕) 발악하는 하이브리드 모델링도 할 수 있습니다.

For example, in a real estate setting, one may seek to relate values of homes to inputs such as crime rate, zoning, distance from a river, air quality, schools, income level of community, size of houses, and so forth.
부동산 판을 한번 볼까요? 집값을 맞추기 위해 우리는 범죄율, 구역 제한선, 예쁜 강 조망 거리, 미세먼지 수치, 8학군급 명문 학교, 앞집 아저씨의 돈 규모, 결국 아파트 평수 평형성 등 영끌할 수 있는 매물 힌트(입력 변수)를 총동원합니다.

In this case one might be interested in the association between each individual input variable and housing price—for instance, _how much extra will a house be worth if it has a view of the river?_
이때 "내가 집 거실창 구조 하나 딱 터서 강이 보이면 집값이 한 몇천만 원이나 더 오르냐?" 처럼 힌트 하나하나의 찰진 위력을 까발려보는 건 참 흥미롭죠.

This is an inference problem.
방금 말한 그건 다름 아닌 꼬치꼬치 따지는 **추론(Inference)** 문제입니다.

Alternatively, one may simply be interested in predicting the value of a home given its characteristics: _is this house under- or over-valued?_
반면에 옆에 있던 다른 사람은 다 귀찮고 그냥 우리 집 스펙만 전산에 쫙 밀어 넣었더니, "야! 이 아파트, 시세보다 5천만 원이나 저평가 돼 있네(under-valued)! 혹은 개거품 껴서 고평가 돼 있네!(over-valued)" 하고 가치만 딱 때려 맞춰서 시세 차익만 남기고 튀고 싶을 수도 있습니다.

This is a prediction problem.
결과만 맞춰서 사기 냄새 맡고 돈만 벌려는 이 전형적인 짓거리는 바로 **예측(Prediction)** 문제입니다.

Depending on whether our ultimate goal is prediction, inference, or a combination of the two, different methods for estimating _f_ may be appropriate.
여러분의 최종 보스 목적이 우승컵(예측)이냐, 심층 취재(추론)냐, 아님 짬뽕이냐에 따라, 이 짝퉁 함수 $\hat{f}$ 를 깎는 칼(방법론)의 도구 종류도 하늘과 땅 차이로 적절하게 바꿔 잡아야 합니다.

For example, _linear models_ allow for relatively simple and interpretable inference, but may not yield as accurate predictions as some other approaches.
대표적으로 무식하고 뻣뻣한 **_선형 모델(Linear models)_** 같은 놈들은 공식이 워낙 단순무식해서 추론의 인과관계를 설명해주기엔 아주 최적인 효자놈이지만, 나중에 배우겠지만 괴상한 다른 놈들만큼 칼같이 정답 스나이핑 적중률(정확한 예측)을 보장해주진 않습니다.

In contrast, some of the highly non-linear approaches that we discuss in the later chapters of this book can potentially provide quite accurate predictions for _Y_, but this comes at the expense of a less interpretable model for which inference is more challenging.
그와 대조적으로 이 책 뒤쪽에서 구부렁대는 **고오급 비선형 놈들**은 미친 듯이 정답 _Y_ 의 한가운데를 뚫어버리는 쾌감(엄청난 예측력)을 맛보게 해주지만, 빌어먹게도 속 안 구조가 지저분하게 꼬여서 사장님한테 왜 이런 예측이 나왔는지 입증(해석 및 추론)하기가 극혐으로 빡세진다는 눈물겨운 대가를 치러야만 합니다.

---

## Sub-Chapters (하위 목차)

[< 2.1.1 Why Estimate F](../trans2.html) | [2.1.2 How Do We Estimate F >](../../2_1_2_how_do_we_estimate_f/trans2.html)
