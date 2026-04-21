---
layout: default
title: "trans2"
---

[< 4.8.1 Conceptual](../4_8_1_conceptual/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.8.2 Applied
# 4.8.2 실전 코딩 미션: 키보드 폭격 시간!

13. This question should be answered using the `Weekly` data set, which is part of the `ISLP` package. This data is similar in nature to the `Smarket` data from this chapter’s lab, except that it contains 1,089 weekly returns for 21 years, from the beginning of 1990 to the end of 2010. 
13. 이번 미션은 든든한 무기고 `ISLP` 패키지에서 야심 차게 꺼내든 `Weekly`(주간 수익률) 데이터 세트를 도마 위에 올려놓고 썰어야 합니다. 이 데이터는 우리가 랩장(lab)에서 지겹게 우려먹었던 `Smarket` 잡주 데이터랑 뼛속까지 닮은 쌍둥이 형제격인데, 스케일이 좀 더 큽니다. 1990년 응답하라 시절부터 2010년 연말까지, 장장 21년이란 세월 동안 처맞은 1,089개의 피 튀기는 주간 수익률 파편들을 통째로 담고 있거든요.
   - (a) Produce some numerical and graphical summaries of the `Weekly` data. Do there appear to be any patterns? 
   - (a) `Weekly` 데이터에 요약 마법(`describe()`) 이랑 그래프 수채화 수치 그림(graphical summaries)을 사정없이 갈겨보세요. 차트에서 뭔가 음흉하게 꿈틀거리는 패턴(patterns)이 포착됩니까?
   - (b) Use the full data set to perform a logistic regression with `Direction` as the response and the five lag variables plus `Volume` as predictors. Use the summary function to print the results. Do any of the predictors appear to be statistically significant? If so, which ones? 
   - (b) 아끼지 말고 데이터셋 원기옥 100%를 다 갈아 넣어 로지스틱 회귀 전투를 벌입니다. 무조건 맞춰야 할 타겟 과녁(반응 변수) 은 떡락/떡상을 맞추는 `Direction` 이고, 우리가 쓸 힌트 무기(예측 변수) 들은 5개의 낡은 지연 변수(Lag 1~5) 에 덤으로 거래량 `Volume` 몽둥이까지 총출동시킵니다. 전투가 끝나면 요약(`summary()`) 결과창을 쫙 뽑아 올리세요. 힌트 무기들 중에 통계계의 엄격한 커트라인(p-value)을 통과한 **유의미한(statistically significant)** 찐 실세가 단 하나라도 보이나요? 만약 있다면 도대체 어떤 놈입니까?
   - (c) Compute the confusion matrix and overall fraction of correct predictions. Explain what the confusion matrix is telling you about the types of mistakes made by logistic regression. 
   - (c) 이 모델이 얼마나 삽질을 했는지 뼈 때리는 오차 일기장(confusion matrix) 과 전체 타율 스코어(올바른 예측 비율) 를 계산대에서 뽑으세요. 그리고 이 오차 일기장이 로지스틱 기계 녀석의 고질적인 '바보짓(mistakes의 유형)' 에 대해 당신 귀에 무슨 험담을 속삭이고 있는지 논리적으로 까발리세요.
   - (d) Now fit the logistic regression model using a training data period from 1990 to 2008, with `Lag2` as the only predictor. Compute the confusion matrix and the overall fraction of correct predictions for the held out data (that is, the data from 2009 and 2010). 
   - (d) 힌지가 고장 났으니 가지치기 들어갑니다! 이번엔 오로지 `Lag2` 달랑 하나만 궁극의 스나이퍼 무기로 쥐어주고, 타임 소드 스킬을 써서 1990년부터 2008년 구간까지만 피 튀기게 훈련(fit) 시킵니다. 그리고 고이 짱박아둔 미래 타겟(held out data, 즉 2009~2010년 데이터) 에 대해 이 스나이퍼 모델이 터뜨린 새로운 오차 일기장과 최종 명중률 점수를 다시 계산판에 띄우세요.
   - (e) Repeat (d) using LDA. 
   - (e) 뻣뻣한 선형 충성도 100%의 LDA 머신을 출격시켜 방금 (d) 짓거리를 똑같이 반복하세요.
   - (f) Repeat (d) using QDA. 
   - (f) 이번엔 부드러운 곡선 폭격기 QDA 머신을 띄워 (d) 짓거리를 똑같이 반복하세요.
   - (g) Repeat (d) using KNN with $K = 1$. 
   - (g) 내 앞의 1명만 믿고 가는 극단주의 용병 KNN ($K=1$) 을 용병으로 사들여 (d)를 또 재탕하십시오.
   - (h) Repeat (d) using naive Bayes. 
   - (h) "난 다 독립이야!" 라고 우기는 맹신도 나이브 베이즈(naive Bayes) 를 풀어 (d)를 재탕하세요.
   - (i) Which of these methods appears to provide the best results on this data? 
   - (i) 자, 이 피 터지는 로봇 격투기 중에서, 이 요상한 주식 데이터 판때기에 가장 어울리는 **최강의 무공 스코어(best results) 1인자**는 대체 누구로 보입니까?
   - (j) Experiment with different combinations of predictors, including possible transformations and interactions, for each of the methods. Report the variables, method, and associated confusion matrix that appears to provide the best results on the held out data. Note that you should also experiment with values for $K$ in the KNN classifier. 
   - (j) 당신의 끼를 마음껏 발휘해 볼 자유 튜닝 시간입니다! 각 무기(방법론) 에 온갖 잡동사니 힌트 변수들을 이리저리 끼워보고, 지지고 볶는 변환(transformations) 부터 섞어치기 상호작용(interactions) 시너지까지 별의별 짓을 다 실험해 보세요. 이 숨겨둔 미래 데이터(held out data) 전장에서 가장 미친 타율(best results) 을 터뜨린 전설의 변수 조합, 모델 이름, 그리고 그때의 훈장(오차 행렬) 을 당당하게 보고서로 제출하세요. (참고: 무지성 KNN 용병의 $K$ 인원수 조정 튜닝 노가다도 꼭 뛰셔야 합니다!)

14. In this problem, you will develop a model to predict whether a given car gets high or low gas mileage based on the `Auto` data set. 
14. 이 문제에서 당신은 기름 먹는 하마 자동차들이 뒹구는 `Auto` 데이터 세트에 뛰어듭니다. 자동차 엔진 속을 꿰뚫어 보고 그 차의 **기름 연비(gas mileage)** 가 미친 혜자인지 개똥망 급인지 예언하는 초특급 감정 모델을 개발해야 합니다.
   - (a) Create a binary variable, `mpg01`, that contains a 1 if `mpg` contains a value above its median, and a 0 if `mpg` contains a value below its median. You can compute the median using the `median()` method of the data frame. Note you may find it helpful to add a column `mpg01` to the data frame by assignment. Assuming you have stored the data frame as `Auto`, this can be done as follows: 
   - (a) 일단 흑백 논리로 선을 그어버리죠. `mpg` (연비) 스코어가 전체 놈들 중간 등수(중앙값 median) 를 간지나게 뚫어버린 '우등생' 차들에겐 `1` 딱지를, 중간 밑으로 밑바닥을 깔아주는 '열등생' 차들에겐 `0` 딱지를 붙여버리는 잔인한 이분법적 신분 변수 `mpg01` 을 창조하세요. 전체의 중간 지점은 데이터 프레임에 달린 `median()` 칼날 메서드를 쓰면 아주 쉽게 썰 수 있습니다. 만든 `mpg01` 딱지는 원래 주차장인 `Auto` 데이터 프레임 우측에 새 기둥(열) 으로 쑤셔 박아(add a column) 주는 센스를 발휘하세요. 친절히 코드를 알려주자면 이런 식입니다:

```python
Auto['mpg01'] = mpg01
```

   - (b) Explore the data graphically in order to investigate the association between `mpg01` and the other features. Which of the other features seem most likely to be useful in predicting `mpg01`? Scatterplots and boxplots may be useful tools to answer this question. Describe your findings. 
   - (b) `mpg01` 합격 목걸이와 나머지 스펙 변수들 사이에 어떤 끈적한 로맨스(연관성) 가 흐르는지 수사하기 위해, 데이터에 대고 그래프 폭격을 가하십시오. 시각화의 정점인 산점도(Scatterplots) 구슬 흩뿌리기나, 상자 수염 그림(boxplots) 박스 포장하기 같은 장비들이 꽤 쏠쏠하게 먹힐 겁니다. 과연 어떤 자동차 스펙들이 `mpg01` 의 운명을 맞추는 데 가장 신기 들린 무당(가장 유용한 변수) 처럼 보이나요? 당신이 탐정처럼 캐낸 팩트 결과(findings) 를 서술하세요.
   - (c) Split the data into a training set and a test set. 
   - (c) 자, 데이터를 무자비한 도끼질로 찢으세요! 땀수건 두른 '훈련 캠프장(training set)' 과, 피 튀기는 '실전 수능 모의고사장(test set)' 으로 공평하게 두 동강 냅니다.
   - (d) Perform LDA on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (d) 아까 (b)번에서 눈여겨봐 둔 그 무당급 연관성 깡패 변수들만 골라다가, 훈련 캠프장 데이터에 빳빳한 LDA 다림질을 갈겨서 `mpg01` 과녁을 저격하십시오. 그렇게 빚어낸 무기가 실전 테스트장에선 과연 몇 퍼센트 타율(test error) 도 폭망했습니까?
   - (e) Perform QDA on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (e) 자, 이번엔 유연한 허리를 자랑하는 곡선 폭격기 QDA를 출격시켜 훈련 캠프장에 똑같이 세팅해 보세요. 이차 곡선으로 춤췄을 때의 실전 오답 스코어는 어떻게 뜹니까?
   - (f) Perform logistic regression on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (f) 고전파 등판! 이번엔 S자 스프링 넥을 가진 로지스틱 회귀 기계에 그 스펙들을 꽂아 훈련 데이터 풀을 돌리세요. 이번 모델의 실전 자폭률(test error) 점퍼는 수치가 어찌 나옵니까?
   - (g) Perform naive Bayes on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (g) 남의 눈치 안 보는 아웃사이더, 나이브 베이즈 모델을 소환해서 훈련 데이터판을 휩쓸어 보시죠. 이 독불장군 모델의 모의고사 폭망 스코어는 얼마로 찍히나요?
   - (h) Perform KNN on the training data, with several values of $K$, in order to predict `mpg01`. Use only the variables that seemed most associated with `mpg01` in (b). What test errors do you obtain? Which value of $K$ seems to perform the best on this data set? 
   - (h) 다수결의 투표깡패 KNN 용병 부대를 훈련 캠프에 풀되, 동원할 이웃 숫자 깡패단 패거리 $K$ 볼륨을 이것저것 펌핑시키고 줄여가면서(several values) 튜닝 실험을 뺑뺑이 돌려보세요. 힌트 변수는 (b)번에서 고른 단골 무당 스펙들로 고정! 각 투표 패거리 수 $K$ 마다 터져 나오는 오답률 스코어가 어떻게 요동칩니까? 이 무자비한 실험에서 최종 우주 최강 무공을 보여준 최적의 깡패 규모 **$K$ (가장 성능 쩌는 픽)** 은 도대체 몇 명이었습니까?

15. This problem involves writing functions. 
15. 파이썬의 꽃, 내 맘대로 찍어내는 나만의 도구 상자! 함수(Functions) 작명 시간입니다.
   - (a) Write a function, `Power()`, that prints out the result of raising 2 to the 3rd power. In other words, your function should compute $2^3$ and print out the results. 
   - (a) 당신만의 마법 주문 `Power()` 라는 이름의 함수 상자를 하나 조립하십시오. 이 상자를 두드리면, 곧바로 안에서 무식하게 "2의 3제곱(거듭제곱 raising)" 불꽃을 튀겨서 $2^3$ 즉 8 이란 결괏값을 화면 밖으로 프린트(토사) 해 버려야 합니다.
      - _Hint: Recall that_ `x**a` _raises_ `x` _to the power_ `a`. _Use the_ `print()` _function to display the result._ 
      - _힌트: 잊지 마세요 파이썬 엔진에서 거듭제곱 점프는 쌍별표_ `x**a` _로 때리면_ `x` _를 허공_ `a` _높이만큼 띄워 올려버립니다. 그리고 그걸 사람 눈에 쏘려면_ `print()` _스피커폰을 쓰면 됩니다._
   - (b) Create a new function, `Power2()`, that allows you to pass _any_ two numbers, `x` and `a`, and prints out the value of `x**a`. You can do this by beginning your function with the line 
   - (b) 이번 도구 상자는 업그레이드 버전! 아무 숫자나 맘대로 동전 투입구에 넣을 수 있는 `Power2()` 란 진화형 함수를 만드세요. 동전구멍 2개(`x` 와 `a`) 에 _무슨_ 미지의 숫자 쌍을 구겨 넣든, 녀석은 자동으로 `x**a` 거듭제곱 데미지를 폭발시켜 토해내야 합니다. 당신의 코딩 도해는 요런 우아한 스타트 라인으로 삽질을 시작할 수 있죠.

```python
def Power2(x, a):
```

   You should be able to call your function by entering, for instance, 
   이 상자를 완성하고 나면, 밖에서 파이썬 명령 줄(command line) 칠판 창에 대고 간지나게 돌격 스킬을 외쳐 호출(call) 할 수 있게 됩니다. 예를 들어:

```python
Power2(3, 8)
```

   on the command line. This should output the value of $3^8$, namely, $6,561$. 
   요렇게 때려 넣으면 기계가 덜컹 화답하며 $3^8$ 파워 데미지 계산치, 즉 눈 돌아가는 수치 $6,561$ 을 냅다 뱉어내 주어야 합격입니다.

   - (c) Using the `Power2()` function that you just wrote, compute $10^3, 8^{17}$, and $131^3$. 
   - (c) 방금 당신이 목수처럼 손수 조립해 낸 그 갓벽한 `Power2()` 대포 함수를 조준해서, 미친 과녁들인 $10^3, 8^{17}$, 그리고 $131^3$ 에 포탄 발사 계산을 타격해 보세요.
   - (d) Now create a new function, `Power3()`, that actually _returns_ the result `x**a` as a `Python` object, rather than simply printing it to the screen. That is, if you store the value `x**a` in an object called `result` within your function, then you can simply `return` this result, using the following line: 
   - (d) 또 레벨 업! 이번엔 그냥 바보처럼 화면에 허송세월 글씨만 찍 싸버리고 마는 게 아니라, 똑똑하게 그 연산 데미지 결과 `x**a` 덩어리를 온전한 `Python` 객체(물건) 로 포장해서 뒤로 _반환(returns) 토스_ 시켜주는 `Power3()` 란 완전체 함수 창고를 하나 더 짓습니다. 만약 당신이 연산 불덩이 `x**a` 를 함수창고 내부의 `result` 란 이름표 박스 안에 곱게 모셔놨다면, 그걸 바깥세상으로 다시 `return(반환 발송)` 패스 찔러주기 위해 이런 한 줄을 박아 넣으면 끝장입니다:

```python
return result
```

   Note that the line above should be the last line in your function, and it should be indented 4 spaces. 
   눈치 챙겨야 할 포인트: 파이썬은 띄어쓰기 결벽증이 있습니다! 저 반환 패스 발송 문장은 반드시 함수 공간의 가장 맨 바닥 밑줄에 있어야 하고, 무조건 깔끔하게 "스페이스바 4번(들여쓰기)" 의 군기를 맞춰야 톱니가 굴러갑니다.
   - (e) Now using the `Power3()` function, create a plot of $f(x) = x^2$. The $x$-axis should display a range of integers from 1 to 10, and the $y$-axis should display $x^2$. Label the axes appropriately, and use an appropriate title for the figure. Consider displaying either the $x$-axis, the $y$-axis, or both on the log-scale. You can do this by using the `ax.set_xscale()` and `ax.set_yscale()` methods of the axes you are plotting to. 
   - (e) 방금 완성된 영혼 토스 기법 `Power3()` 대포를 장착했으니, 이차방정식 궤도포 $f(x) = x^2$ 의 예술적인 붓질(plot) 그림을 캔버스에 박아 넣읍시다. 가로선 $x$-축 바닥 모래사장엔 1부터 10까지 징검다리 정수를 알뜰히 깔아주고, 수직 기둥 $y$-축엔 그 타격 데미지 $x^2$ 수치 눈금을 그립니다. 축 팻말엔 폼나는 이름표(Label) 도 달고, 전시회 그림답게 위압감 쩌는 제목(title) 도 걸어주세요. 뽀너스! 일반 도화지가 심심하다면 $x$ 축이든 $y$ 축이든 아니면 둘 다 양쪽으로 잡아끌어 시공간을 휘어버리는 **로그 스케일(log-scale) 압축 모드** 발동을 도발적으로 고려해 보세요. (파이썬 캔버스 조종간인 `ax.set_xscale()` 과 `ax.set_yscale()` 버튼을 누르면 쉽게 맵핵을 켤 수 있습니다).
   - (f) Create a function, `PlotPower()`, that allows you to create a plot of `x` against `x**a` for a fixed `a` and a sequence of values of x. For instance, if you call 
   - (f) 아티스트의 끝판왕 도전! 이참에 그림 그리는 붓질마저 한방에 자동 빵구워내는 전지전능 매크로 함수 `PlotPower()` 를 공장 창립하세요. 이 공장은 거듭제곱 승수 `a` 를 딱 자물쇠로 고정(fixed) 시켜 둔 채, 변화무쌍한 `x` 포탄 연속 줄기 시퀀스를 밀어 넣으면 곧장 `x` 와 그놈이 맞고 터진 $x**a$ 사이의 불꽃 튀는 전투 그래프를 쫙 찍어냅니다. (예를 들어, 당신이 이렇게 외치면):

```python
PlotPower(np.arange(1, 11), 3)
```

   then a plot should be created with an $x$-axis taking on values $1, 2, \dots, 10$, and a $y$-axis taking on values $1^3, 2^3, \dots, 10^3$. 
   삐용~ 하고 도화지가 튀어나오면서 $x$ 가로축엔 1, 2, ... 10 까지 징검다리 스텝이 나열되고, 세로 $y$ 축엔 곧장 $1^3, 2^3, \dots, 10^3$ 불지옥 데미지 곡선이 스마일처럼 쫙 세팅되어 렌더링 되어야 정상 판정입니다.

16. Using the `Boston` data set, fit classification models in order to predict whether a given suburb has a crime rate above or below the median. Explore logistic regression, LDA, naive Bayes, and KNN models using various subsets of the predictors. Describe your findings. 
16. 범죄의 도시, 그 유명한 `Boston` 주택가 스펙 데이터 사냥을 떠나봅시다! 특정 동네의 범죄율이 전체 보스턴 바닥의 중간 등수(중앙값 median) 를 뚫고 올라갔는지 치안이 좋은지 예언해 내는 무자비한 분류 예측 모델을 조립해야 합니다. 스펙 무기(예측 변수들) 를 이렇게 저렇게 부분 조합(subsets) 해 가며 끼워 맞춰보고, **로지스틱 회귀, 선형 잣대 LDA, 극단주의 나이브 베이즈, 그리고 다수결 깡패 KNN** 까지 모조리 뺑뺑이 난투극을 돌려보세요. 그 처절한 생존 싸움 속에서 당신이 발견한 소름 돋는 진리(findings) 를 심층 보고서로 서술해 내시길 바랍니다.
_Hint: You will have to create the response variable yourself, using the variables that are contained in the_ `Boston` _data set._
_힌트 팩폭: 이번엔 밥 떠먹여 주는 타겟 채점 과녁이 없습니다! 당신이 친히 `Boston` 도구 상자 안의 톱니바퀴 변수들을 가지고, 범죄율 상/하위 권을 가르는 심판의 '정답 꼬리표(반응 변수)' 객체를 니 손으로 직접 뚝딱뚝딱 조립(create) 해 내야만 싸움이 시작될 겁니다!_

---

## Sub-Chapters

[< 4.8.1 Conceptual](../4_8_1_conceptual/trans2.html)
