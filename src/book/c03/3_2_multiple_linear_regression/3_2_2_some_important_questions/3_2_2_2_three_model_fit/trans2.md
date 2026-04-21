---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.2.2.1 Two Deciding On Important Variables](../3_2_2_1_two_deciding_on_important_variables/trans2.html) | [3.2.2.3 Four Predictions >](../3_2_2_3_four_predictions/trans2.html)

# Three: Model Fit

# 질문 3: 모델 적합도 (우리가 끓인 이 짬뽕 요리, 점수가 몇 점짜리야?)

Two of the most common numerical measures of model fit are the RSE and $R^2$, the fraction of variance explained.
우리가 완성한 이 거대한 짬뽕(다중 회귀 모델)이 얼마나 손님들 입맛(실제 데이터)에 잘 맞춰졌는지 냉정하게 평가하는 가장 흔하고 대중적인 두 가지 점수표가 있습니다. 바로 잔차들이 널뛰는 **RSE(잔차 표준 오차)**와, 모델이 우주의 혼돈을 얼마나 설명해 냈는지 지분을 따지는 **$R^2$(설명력 퍼센트)**입니다.

These quantities are computed and interpreted in the same fashion as for simple linear regression.
다행히도, 이 점수표들을 계산하고 해석하는 룰은 예전 기초반에서 배웠던 '단순 선형 회귀' 시절의 룰과 토씨 하나 안 틀리고 똑같이 통용됩니다.

Recall that in simple regression, $R^2$ is the square of the correlation of the response and the variable.
혹시 기억하시나요? 단순 1대1 회귀 시절에, 이 $R^2$ 점수의 정체는 그냥 원인 파라미터 1개와 타겟 정답 사이의 찰떡 친밀도인 '상관계수($r$)'를 무식하게 통째로 제곱한 녀석($r^2$)에 불과했습니다.

In multiple linear regression, it turns out that it equals $\text{Cor}(Y, \hat{Y})^2$, the square of the correlation between the response and the fitted linear model; in fact one property of the fitted linear model is that it maximizes this correlation among all possible linear models.
그런데 투입 변수가 수백수천 개로 늘어난 이 웅장한 다중 선형 회귀의 굴레에서는 $R^2$ 의 모습이 살짝 진화합니다. 여기서 $R^2$ 는 **"진짜 정답($Y$)과 우리 짬뽕 모델이 뱉어낸 예언 복제품($\hat{Y}$) 사이의 친밀도(상관계수)를 제곱한 값"**, 즉 $\text{Cor}(Y, \hat{Y})^2$ 과 완벽하게 동일한 숫자로 밝혀집니다! 소름 돋게도 우리 척척박사 모델은, 이 세상에 존재하는 그 어떤 선형 조합 모델들보다도 이 친밀도 점수가 1등으로 가장 높게 나오도록 세팅된 기적의 발명품(최대화 특성)이랍니다.

An $R^2$ value close to 1 indicates that the model explains a large portion of the variance in the response variable.
당연한 소리겠지만, 이 $R^2$ 퍼센트 점수가 100점 만점인 1.0에 바짝 다가갈수록, 우리 짬뽕 요리가 타겟 맛(응답 변수)이 맵고 짜게 요동치는 복잡한 이유(분산)의 상당 부분을 기가 막히게 잡아내고 설명충처럼 잘 묘사하고 있다는 훌륭한 뜻이 됩니다.

As an example, we saw in Table 3.6 that for the `Advertising` data, the model that uses all three advertising media to predict `sales` has an $R^2$ of $0.8972$.
예를 들어 볼까요? 꿀잼 `Advertising(광고)` 장부 데이터에서 TV, 라디오, 벼룩시장 신문까지 3종 세트 매체를 몽땅 갈아 넣은 우리 잡탕 모델이 표 3.6에서 받은 $R^2$ 성적표는 무려 **$0.8972$(약 90% 지분 파워)** 였습니다.

On the other hand, the model that uses only `TV` and `radio` to predict `sales` has an $R^2$ value of $0.89719$.
그런데 잠깐 놀라운 걸 보여드리죠. 저기서 그 쓸모없던 쓰레기 '신문'을 몰래 빼버리고, 순수하게 엑기스인 `TV` 와 `radio` 달랑 두 개만 사용해서 끓인 모델의 $R^2$ 성적은 어떨까요? **$0.89719$** 입니다.

In other words, there is a _small_ increase in $R^2$ if we include newspaper advertising in the model that already contains TV and radio advertising, even though we saw earlier that the $p$-value for newspaper advertising in Table 3.4 is not significant.
이게 무슨 뜻이냐고요? 우리가 조금 전 표 3.4에서 '신문' 따위는 매출과 아무 상관없는 폐급 나부랭이($p$-값 망함)라고 비웃었음에도 불구하고! 이미 TV와 라디오로 꽉 찬 훌륭한 엑기스 냄비에 굳이 그 쓰레기 같은 '신문' 항목을 꾸역꾸역 구겨 넣었을 때, $R^2$ 점수는 아주 눈곱만치라도 미친 듯이 미세하지만 **결과적으로 쥐꼬리만큼 올라갔다(증가했다)**는 충격적인 사실입니다!

It turns out that $R^2$ will always increase when more variables are added to the model, even if those variables are only weakly associated with the response.
통계학의 더러운 비밀 하나 폭로하겠습니다. **$R^2$ 이 얄팍한 성적표 점수는, 모델 냄비 안에 새로운 쓰레기 재료(변수)를 무지성으로 계속 쑤셔 넣으면 넣을수록, 설령 그 재료가 맹물 수준으로 쓸모가 없더라도 무조건 무지성으로 우상향하며 무조건 증가**해 버리는 허영심 가득한 멍청한 거품 성질을 갖고 있습니다!

This is due to the fact that adding another variable always results in a decrease in the residual sum of squares on the training data (though not necessarily the testing data).
왜 이런 코미디가 발생할까요? 우리가 모델이 이미 쥐고 있는 훈련용 문제집(학습 데이터)에 억지로 새로운 수식의 팔다리(변수)를 달아줄 때마다, 훈련용 잔차 찌꺼기(RSS)는 약간의 요행을 통해서라도 어떻게든 모델이 끼워 맞출 구석을 찾아내며 필연적으로 줄어드는 착시 꼼수를 부리기 때문입니다. (물론 나중에 아예 처음 보는 실전 수능 테스트 데이터가 던져지면 대참사가 벌어지겠지만요).

Thus, the $R^2$ statistic, which is also computed on the training data, must increase.
따라서, 이 훈련용 잔차 찌꺼기 성적표를 기반으로 반비례 계산되는 $R^2$ 통계 지분 점수는 재료가 많아질수록 억지로 올라갈 수밖에 없는 운명인 겁니다. 

The fact that adding newspaper advertising to the model containing only TV and radio advertising leads to just a tiny increase in $R^2$ provides additional evidence that `newspaper` can be dropped from the model.
고로, 훌륭한 TV-라디오 정예 냄비에 꾸역꾸역 신문 전단지 쪼가리를 떨어뜨렸을 때 $R^2$ 점수가 고작 '0.00001'밖에 찔끔 오르지 않았다는 이 처참한 사실은 뒷목을 잡아야 할 불행이 아니라, 오히려 "아, 신문 이 녀석 진짜 하등 쓸모없는 놈이구나. 당장 배에서 쫓아내 버려도 1도 아쉬울 게 없네!" 라고 확신할 수 있는 든든한 사형선고 추가 증거가 됩니다.

Essentially, `newspaper` provides no real improvement in the model fit to the training samples, and its inclusion will likely lead to poor results on independent test samples due to overfitting.
본질을 요약하자면, `newspaper(신문)` 이 불량 매체는 연습용 훈련 데이터 문제집에서조차 실질적인 짬뽕 맛 개선을 1도 주지 못하는 폐급이며, 이놈의 쓸모없는 부피를 억지로 끌어안고 가는 행위는 훗날 실전 모의고사(독립적인 테스트 표본)에 마주쳤을 때 이상한 노이즈 환각에만 집착하는 소위 **'과적합(Overfitting)'** 함정에 빠져서 훨씬 지저분하고 쓰레기 같은 실전 폭망 예측 결과를 도출할 위험성만 잔뜩 높이는 적폐가 됩니다.

By contrast, the model containing only `TV` as a predictor had an $R^2$ of $0.61$ (Table 3.2).
반대로 비교해 볼까요? 옛날에 오로지 `TV` 요원 단 한 명만 고독하게 투입시켰던 단순 회귀 모델의 $R^2$ 지분 점수는 그저 평범한 $0.61$ (61%) 에 불과했습니다. (표 3.2 참고)

Adding `radio` to the model leads to a substantial improvement in $R^2$.
그런데 여기에 든든한 진또배기 요원인 `radio`를 추가 영입하자, $R^2$ 점수가 무려 61점에서 90점(0.897) 부근으로 미친 듯이 퀀텀 점프하며 **파괴적인 수준의 압도적인 화력 개선(상승)**을 이루어 냈습니다!

This implies that a model that uses TV and radio expenditures to predict sales is substantially better than one that uses only TV advertising.
이 놀라운 점프 차이는 우리에게, 사장님이 매출 타겟을 저격할 때 'TV 단일 스나이퍼' 혼자 쓰는 것보다 'TV'와 '라디오' 혼성 듀오를 같이 등판시켜 쌍권총을 쏘는 편이 하늘과 땅 차이로 비교 불가하게 실질적으로 훨씬 갓벽한 성능을 자랑한다는 걸 가슴 웅장하게 암시해 줍니다. 

We could further quantify this improvement by looking at the $p$-value for the `radio` coefficient in a model that contains only `TV` and `radio` as predictors.
이 가슴 벅찬 상승분을 좀 더 수학 덕후처럼 정량적으로 증명하고 싶다면? 그냥 이 TV-라디오 쌍권총 모델 장부에 박혀있는 `radio` 녀석 전용의 개별 성적표, 요놈의 $p$-값을 흘깃 지켜보는 것만으로도 게임 끝입니다. (확실하게 유의미한 소수점 아래 무한대의 0 도장이 박혀있을 테니까요.)

The model that contains only `TV` and `radio` as predictors has an RSE of 1.681, and the model that also contains `newspaper` as a predictor has an RSE of 1.686 (Table 3.6).
자, 아까 우리가 RSE(잔차 오차)를 모델 평가 지표로 같이 쓴다고 했었죠? 흥미로운 사실! TV와 라디오만 담백하게 쓴 듀오 모델의 오차 덩어리 RSE는 '1.681'입니다. 그런데 여기에 그 망할 '신문'을 낑겨 넣은 3인조 삼총사 모델의 요란한 RSE 오차 수치는 '1.686'으로 (미세하지만) 올랐습니다! (표 3.6 참고)

In contrast, the model that contains only `TV` has an RSE of $3.26$ (Table 3.2).
이와 대조적으로 옛날에 TV 혼자 삽질하던 시절의 왕방울만 한 RSE 오차 크기는 자그마치 $3.26$ 이나 되는 대재앙 수준이었습니다. (표 3.2)

This corroborates our previous conclusion that a model that uses TV and radio expenditures to predict sales is much more accurate (on the training data) than one that only uses TV spending.
이 수치 비교가 뜻하는 바는 너무나 분명합니다! "TV랑 라디오를 둘 다 끌고 가야 매출 적중률 과녁이 (비록 연습장 문제집 데이터에서라도) 훨씬 바늘처럼 정밀해진다!" 라는 우리의 기존 확신 도장에 빼박 증거로 거대한 참 잘했어요 쌍도장을 쾅쾅! 찍어 사스콰치급 확증 코어(Corroborate)를 안겨준다는 말입니다.

Furthermore, given that TV and radio expenditures are used as predictors, there is no point in also using newspaper spending as a predictor in the model.
게다가 더불어 쐐기를 박자면, 이 기특하고 유능한 TV와 라디오 엘리트 듀오가 포진해 있는 진용 체제라면, 하등 쓸모없는 백수 같은 '신문비 찌라시' 종잇장 따위를 굳이 버스 태우듯 모델에 태우고 다닐 어떠한 일말의 명분이나 가치 따위 1도 존재치 않는다는 통쾌한 진리입니다.

The observant reader may wonder how RSE can increase when `newspaper` is added to the model given that RSS must decrease. In general RSE is defined as
여기서 머리가 아주 비상하게 잘 돌아가는 통계 덕후 꼬마 독자분이라면 하나 딴지를 걸고 싶을 겁니다. "아니 작가 양반, 아까 당신이 변수(쓰레기 신문이라도)를 추가하면 찌꺼기 조각(RSS)은 무조건 구조상 억지로라도 줄어든다며? 근데 방금 RSS로 계산한다는 RSE 오차놈(1.681 -> 1.686)은 신문을 넣었는데 왜 외려 늘어난 거냐? 앞뒤가 안 맞잖아!" 아주 훌륭한 관찰력입니다. 통상적으로 이 RSE 녀석은 다음과 같은 기막힌 공식 뱃속에서 튀어나옵니다.

$$
\text{RSE} = \sqrt{\frac{1}{n-p-1} \text{RSS}} \quad (3.26)
$$

**==> picture [230 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Sales(매출)<br>TV(티비 예산)<br>Radio(라디오 예산)<br>**----- End of picture text -----**<br>

**FIGURE 3.5.** _For the_ `Advertising` _data, a linear regression fit to_ `sales` _using_ `TV` _and_ `radio` _as predictors. From the pattern of the residuals, we can see that there is a pronounced non-linear relationship in the data. The positive residuals (those visible above the surface), tend to lie along the 45-degree line, where TV and Radio budgets are split evenly. The negative residuals (most not visible), tend to lie away from this line, where budgets are more lopsided._
**FIGURE 3.5.** `Advertising` _시장 장부를 입체로 부활시킨 요술입니다! 바닥축에_ `TV` _와_ `radio` _두 놈(예측 변수)을 깔고 타겟인_ `sales(매출)` _하늘 향해 뻗친 3D 산악 지대에 우리의 거대한 직선 철판('다중 선형 회귀 평면')을 사정없이 찍어 누른 모습입니다. 저 가시처럼 뻗어 나오는 빨간 핏대 줄기(잔차 에러)의 징그러운 패턴을 잘 째려보세요! 자연 데이터는 사실 철판때기로 깔끔히 덮이는 밋밋함이 아니라 꿀렁꿀렁 심장 뛰는 '비선형(Non-linear)' 호흡을 내뿜고 있다는 스릴 넘치는 현장 고발입니다. 평면 위로 빼꼼 고개를 내민 당돌한 양수(+) 잔차 녀석들은 예산이 TV와 라디오에 딱 반반(50:50) 황금 비율로 투자된 대각 45도 황금 능선을 밟을 때 극대화되고 집중된 경향을 뿜어냅니다! 반면 우리 눈을 피해 밑으로 처박힌 심해의 음수(-) 잔차 녀석들은 사장님이 'TV 몰빵 전략', 혹은 '라디오 몰빵 빙구짓'처럼 돈을 편식해 한쪽으로 심하게 몰아넣은 벼랑 끝 변방 지대에서 요란을 떠는 미운 오리 새끼 양상을 보입니다._

which simplifies to (3.15) for a simple linear regression.
머리 아픈 공식 이야기로 돌아가면, 저 (3.26) 뱃속 공식에서 변수가 하나만 있는 단순 회귀($p=1$) 때는 이게 쑥 단축돼서 이전에 본 공식 (3.15) 로 귀엽게 간소화됩니다.

Thus, models with more variables can have higher RSE if the decrease in RSS is small relative to the increase in $p$.
비밀 폭로가 시작합니다! 저 쪼개지는 분모 밑창에 자리 잡고 똬리를 튼 $p$(변수 머릿수)가 범인입니다! 신문 변수가 추가되면서 물론 분자 파트인 쓰레기 조각 통(RSS)이 요행으로 아주 찔끔 줄어들긴 했을 겁니다. 하지만 반대로 분모 쪽에선 변수 머릿수 $p$가 $2$에서 $3$으로 하나 커지는 바람에 **분모 전체 덩치($n - p - 1$) 몫은 되려 확 줄어들어 갉아 먹힙니다.** 즉, RSS 분자가 요행으로 티끌만큼 줄어든 구두쇠 이점 따위보다 $p$가 늘어나면서 분모가 작아져버려 발생하는 나눗셈 쇼크 마찰이 훨씬 막대하게 커버렸기 때문에, 공식이 요동치며 최종 덩어리인 RSE 뱃살 수치를 얄궂고 무정하게 도리어 위로 더 살찌워 올려버리는 패악질이 일어난 것입니다! 

In addition to looking at the RSE and $R^2$ statistics just discussed, it can be useful to plot the data.
지금까지 우리 뇌를 고문했던 골치 아픈 점수 계산기 타건질, 즉 RSE나 $R^2$ 같은 숨 막히는 텍스트 통계 숫자에만 너무 매달려 있을 필요가 있을까요? 때로는 그냥 아이들 그림책처럼 **데이터를 시원하게 시각 그림(Plot) 도화지에 흩뿌려 펼쳐보는 낭만 방식**이 예상치 못한 뒤통수를 때리는 번뜩이는 유용함을 선사하곤 합니다.

Graphical summaries can reveal problems with a model that are not visible from numerical statistics.
장담컨대, 이런 시원시원한 만화책 스타일 그래픽 요약본들은 차가운 종이 위 검은 활자로 타이핑된 뻣뻣한 수치 통계 성적표 따위에선 절대로 냄새조차 맡을 수 없는 기상천외한 모델의 고질적 질병이나 결함 맹점들을 소름 돋게 적나라하게 파헤치고 드러내 까발려줍니다.

For example, Figure 3.5 displays a three-dimensional plot of `TV` and `radio` versus `sales`.
예를 들어 볼까요? 앞서 방금 맛만 봤던 우리 화제작 **[그림 3.5]** 는 `TV` 와 `radio` 가 바닥에 깔리고 기둥으로 `sales` 매출 꼭대기가 하늘로 치솟은 웅장한 3차원 입체 게임 그래픽 무대를 뽐냅니다.

We see that some observations lie above and some observations lie below the least squares regression plane.
눈치채셨습니까? 우리가 억지로 누른 저 빳빳하고 평편한 회귀 철판(Plane) 모가지를 기준으로, 어떤 진짜 점 생명체 데이터들은 철판을 뚫고 하늘 위 양지쪽에 볼록 튀어나와서 웃고 앉았고, 또 어떤 왕따 녀석들은 철판 밑구덩이 바닥 그늘 쪽에 파묻혀서 불쌍하게 울고 있습니다.

In particular, the linear model seems to overestimate `sales` for instances in which most of the advertising money was spent exclusively on either `TV` or `radio`.
여기서 그래픽 탐정의 촉이 발동합니다. 가만히 째려보니, 이 무식한 빳빳 직선 철판 요괴(선형 모델)는 사장님이 극단적인 똥볼을 차서 '예산을 오로지 한쪽(TV 올인! 혹은 라디오 몰빵!)'으로만 치우치고 파편적으로 허탕 갈아부었을 극단 변두리 스팟 구석 사례에 대해, 혼자 김칫국을 원샷 때리며 `sales(매출)`가 꽤 많이 나올 거라 **지나치게 과대망상 오만(과대평가)**을 부리는 요망하고 오만한 현상을 보이고 있습니다.

It underestimates `sales` for instances where the budget was split between the two media.
반대로! 사장님이 통찰력이 빛나서 영리하게 예산을 두 매체(TV와 라디오)로 알뜰살뜰 반반 골고루 황금 밸런스로 양분해 쪼개 투자한 노른자 정중앙 분배 사례들에 있어서는, 실제론 장사가 미친 듯이 미어터지고 대박 났음에도 불구하고 이 구형 모델판때기는 상황파악 못 하고 `sales(매출)`를 너무 낮잡아 보며 **기죽어 무시(과소평가)**하는 비통한 참사 우스운 꼴을 빚어재끼고 있습니다. 

This pronounced non-linear pattern suggests a _synergy_ or _interaction_ effect between the advertising media, whereby combining the media together results in a bigger boost to sales than using any single medium.
무서운 진실입니다! 이렇게 철저하게 어긋나며 출렁이는 심장박동 같은 '비선형(Non-linear)' 현장의 패턴이 강력한 붉은 핏빛으로 시사하는 바는 무엇일까요? 바로 여러 광고 간판 녀석들을 섞었을 때 벌어지는 **폭발적인 화학 반응, _시너지(Synergy)_ 내지는 끈끈한 기적의 _상호작용(Interaction)_ 효과**가 도처에 만연해 살아 숨 쉬고 있다는 뜻입니다! 이 미친 시너지 세상에서는, 단순무식하게 어느 요원 요격 매체 한 녀석에게 뭉칫돈을 밀어줘서 풀 파워로 고독하게 조지는 짓거리보다는, 힘을 합쳐 둘을 교묘하게 한 냄비에 투하 배합해 짬짜면처럼 섞어 버리는 마법 콤보 스킬이 매출의 폭등 성장에 훨씬 거대한 슈퍼 부스터 광폭 버프를 선물한다는 짜릿한 이치입니다.

In Section 3.3.2, we will discuss extending the linear model to accommodate such synergistic effects through the use of interaction terms.
어떠신가요, 좀 억울하시죠? 이 빳빳한 철판 고무판 바보 모델로는 감당할 수 없는 진짜 세상의 달콤한 시너지 짜릿함을 낚아채고 싶어지셨나요? 걱정 마세요. 대망의 앞으로 맞이할 **섹션 3.3.2 파트 코너**에서, 우리는 '상호작용 항(동반 상승 시너지 부스터 변수)'이라는 금단의 치팅 파츠 아이템 부품을 달짝지근하게 결합 조명하여 추가 장착함으로써, 이런 시너지 효과의 마술까지도 다 씹어 먹고 보듬어 안을 수 있게 우리의 구형 선형 모델 로봇을 진화 업그레이드 폭발 확장 개조하는 미친 정비 작업 플랜을 즐겁고 신나게 토론해 볼 예정입니다!

---

[< 3.2.2.1 Two Deciding On Important Variables](../3_2_2_1_two_deciding_on_important_variables/trans2.html) | [3.2.2.3 Four Predictions >](../3_2_2_3_four_predictions/trans2.html)
