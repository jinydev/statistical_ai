---
layout: default
title: "trans1"
---

[< 4.8.1 Conceptual](../4_8_1_conceptual/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.8.2 Applied
# 4.8.2 응용 문제

13. This question should be answered using the `Weekly` data set, which is part of the `ISLP` package. This data is similar in nature to the `Smarket` data from this chapter’s lab, except that it contains 1,089 weekly returns for 21 years, from the beginning of 1990 to the end of 2010. 
13. 이 질문은 `ISLP` 패키지의 일부인 `Weekly` 데이터 세트를 사용하여 답변해야 합니다. 이 데이터는 1990년 초부터 2010년 말까지 21년 동안의 1,089개 주간 수익률을 포함하고 있다는 점을 제외하면, 본 장의 랩(lab) 에 있는 `Smarket` 데이터와 본질적으로 유사합니다.
   - (a) Produce some numerical and graphical summaries of the `Weekly` data. Do there appear to be any patterns? 
   - (a) `Weekly` 데이터의 몇 가지 수치적 및 그래픽 요약을 생성하십시오. 패턴(patterns)이 나타나는 것 같습니까?
   - (b) Use the full data set to perform a logistic regression with `Direction` as the response and the five lag variables plus `Volume` as predictors. Use the summary function to print the results. Do any of the predictors appear to be statistically significant? If so, which ones? 
   - (b) 전체 데이터 세트를 사용하여 `Direction` 을 반응 변수로 하고 5개의 지연 변수(lag variables) 와 `Volume` 을 예측 변수로 하는 로지스틱 회귀를 수행하십시오. 요약(summary) 함수를 사용하여 결과를 출력하십시오. 예측 변수 중 통계적으로 유의미한(statistically significant) 것이 있습니까? 그렇다면 어떤 것입니까?
   - (c) Compute the confusion matrix and overall fraction of correct predictions. Explain what the confusion matrix is telling you about the types of mistakes made by logistic regression. 
   - (c) 오차 행렬(confusion matrix)과 올바른 예측의 전체 비율을 계산하십시오. 오차 행렬이 로지스틱 회귀로 인해 발생하는 실수의 유형에 대해 무엇을 말해주고 있는지 설명하십시오.
   - (d) Now fit the logistic regression model using a training data period from 1990 to 2008, with `Lag2` as the only predictor. Compute the confusion matrix and the overall fraction of correct predictions for the held out data (that is, the data from 2009 and 2010). 
   - (d) 이제 `Lag2` 만을 유일한 예측 변수로 사용하여, 1990년부터 2008년까지의 훈련 데이터 기간 동안 로지스틱 회귀 모델을 피팅하십시오. 남겨진 데이터(held out data, 즉 2009년과 2010년 데이터) 에 대한 오차 행렬과 올바른 예측의 전체 비율을 계산하십시오.
   - (e) Repeat (d) using LDA. 
   - (e) LDA를 사용하여 (d)를 반복하십시오.
   - (f) Repeat (d) using QDA. 
   - (f) QDA를 사용하여 (d)를 반복하십시오.
   - (g) Repeat (d) using KNN with $K = 1$. 
   - (g) $K=1$ 로 KNN을 사용하여 (d)를 반복하십시오.
   - (h) Repeat (d) using naive Bayes. 
   - (h) 나이브 베이즈를 사용하여 (d)를 반복하십시오.
   - (i) Which of these methods appears to provide the best results on this data? 
   - (i) 이러한 방법들 중 어느 것이 이 데이터에서 가장 좋은 결과(best results)를 제공하는 것으로 보입니까?
   - (j) Experiment with different combinations of predictors, including possible transformations and interactions, for each of the methods. Report the variables, method, and associated confusion matrix that appears to provide the best results on the held out data. Note that you should also experiment with values for $K$ in the KNN classifier. 
   - (j) 각 방법론에 대하여 가능한 변환(transformations)과 상호작용(interactions)을 포함하여 예측 변수들의 여러 다른 조합(combinations)으로 실험해 보십시오. 남겨진 데이터에서 가장 좋은 결과를 제공하는 것으로 보이는 변수, 방법, 상응하는 오차 행렬을 보고하십시오. 또한 KNN 분류기에서 $K$ 값을 다양하게 실험해 보아야 함을 유의하십시오.

14. In this problem, you will develop a model to predict whether a given car gets high or low gas mileage based on the `Auto` data set. 
14. 이 문제에서는 `Auto` 데이터 세트를 기반으로 특정 차량이 높은 연비(gas mileage)를 갖는지 낮은 연비를 갖는지를 예측하는 모델을 개발할 것입니다.
   - (a) Create a binary variable, `mpg01`, that contains a 1 if `mpg` contains a value above its median, and a 0 if `mpg` contains a value below its median. You can compute the median using the `median()` method of the data frame. Note you may find it helpful to add a column `mpg01` to the data frame by assignment. Assuming you have stored the data frame as `Auto`, this can be done as follows: 
   - (a) `mpg` 값이 중앙값(median)을 초과하는 경우는 1을, 중앙값 미만인 경우는 0을 포함하는 이진 변수(binary variable) `mpg01` 을 생성하십시오. 데이터 프레임의 `median()` 메서드를 사용하여 중앙값을 계산할 수 있습니다. 할당(assignment)을 통해 데이터 프레임에 `mpg01` 열을 추가하는 것이 도움이 될 수 있습니다. 데이터 프레임을 `Auto` 로 저장했다고 가정하면, 다음과 같이 수행할 수 있습니다.

```python
Auto['mpg01'] = mpg01
```

   - (b) Explore the data graphically in order to investigate the association between `mpg01` and the other features. Which of the other features seem most likely to be useful in predicting `mpg01`? Scatterplots and boxplots may be useful tools to answer this question. Describe your findings. 
   - (b) `mpg01` 과 다른 특성들 간의 연관성(association)을 인베스티게이션하기 위해 그래프로 데이터를 탐색하십시오. 다른 어느 특성이 `mpg01` 을 예측하는 데 통상적으로 가장 유용할 것 같습니까? 산점도(Scatterplots)와 상자 수염 그림(boxplots)이 이 질문에 답하기 위한 유용한 도구가 될 수 있습니다. 여러분의 발견(findings)을 설명하십시오.
   - (c) Split the data into a training set and a test set. 
   - (c) 데이터를 훈련 세트(training set) 와 테스트 세트(test set) 로 분할하십시오.
   - (d) Perform LDA on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (d) (b)에서 `mpg01` 과 가장 연관성이 있어 보였던 변수를 사용하여 `mpg01` 을 예측하기 위해 훈련 데이터에 LDA를 수행하십시오. 획득한 모델의 테스트 에러(test error) 는 얼마입니까?
   - (e) Perform QDA on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (e) (b)에서 `mpg01` 과 가장 관련성이 높아진 변수들을 활용, 훈련 데이터에 대해 QDA를 수행하십시오. 얻어낸 모델이 가진 테스트 에러율은?
   - (f) Perform logistic regression on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (f) (b)에서 `mpg01` 항목과 함께 유의미한 변수들을 발췌하여 로지스틱 회귀 분석을 훈련 데이터 상에서 수행하십시오. 이 모델의 테스트 오류 스코어는 어떻게 나옵니까?
   - (g) Perform naive Bayes on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (g) `mpg01` 데이터와 맞닿은 여러 항목으로 구성된 나이브 베이즈 분석을 훈련 데이터에서 수행하세요. 모델에서 관측된 테스트 스코어는?
   - (h) Perform KNN on the training data, with several values of $K$, in order to predict `mpg01`. Use only the variables that seemed most associated with `mpg01` in (b). What test errors do you obtain? Which value of $K$ seems to perform the best on this data set? 
   - (h) `mpg01` 항목 예측을 돕기 위해 여러 $K$ 값을 대입하여 훈련 데이터에 대해 KNN을 반복 수행하십시오. (b)에서 가장 깊게 연관된 변수들만 집어넣어야 합니다. 테스트 에러율 타율이 얼마나 나왔습니까? 그리고 어떤 $K$ 값이 가장 높은 최상의 결과를 자랑합니까?

15. This problem involves writing functions. 
15. 이 문제는 함수를 작성(writing functions)하는 것과 관련이 있습니다.
   - (a) Write a function, `Power()`, that prints out the result of raising 2 to the 3rd power. In other words, your function should compute $2^3$ and print out the results. 
   - (a) 2를 3승(power)으로 올린 값을 출력하는 `Power()` 함수를 작성하십시오. 즉, 함수는 $2^3$ 을 연산하여 결과를 프린트 아웃 해야 합니다.
      - _Hint: Recall that_ `x**a` _raises_ `x` _to the power_ `a`. _Use the_ `print()` _function to display the result._ 
      - _힌트:_ `x**a` _가_ `x` _의_ `a` _승을 계산한다는 것을 상기하십시오. 결과를 표시하려면_ `print()` _함수를 사용하십시오._
   - (b) Create a new function, `Power2()`, that allows you to pass _any_ two numbers, `x` and `a`, and prints out the value of `x**a`. You can do this by beginning your function with the line 
   - (b) _임의의_ 두 숫자 `x` 와 `a` 를 전달하고 `x**a` 값을 출력할 수 있는 새 함수 `Power2()` 를 생성하십시오. 당신은 다음 줄로 함수 작성을 시작함으로써 수행할 수 있습니다.

```python
def Power2(x, a):
```

   You should be able to call your function by entering, for instance, 
   당신은 예를 들어 다음과 같이 입력함으로써 함수를 호출할 수 있어야 합니다.

```python
Power2(3, 8)
```

   on the command line. This should output the value of $3^8$, namely, $6,561$. 
   명령 줄(command line) 에 말입니다. 이것은 $3^8$ 의 값, 즉 $6,561$ 을 출력해야 합니다.

   - (c) Using the `Power2()` function that you just wrote, compute $10^3, 8^{17}$, and $131^3$. 
   - (c) 방금 작성한 `Power2()` 함수를 사용하여 $10^3, 8^{17}$, 및 $131^3$ 을 계산하십시오.
   - (d) Now create a new function, `Power3()`, that actually _returns_ the result `x**a` as a `Python` object, rather than simply printing it to the screen. That is, if you store the value `x**a` in an object called `result` within your function, then you can simply `return` this result, using the following line: 
   - (d) 이제 단순히 화면에 출력하는 것이 아니라 실제로 `x**a` 결과를 `Python` 객체로 _반환(returns)_ 하는 새 함수 `Power3()` 을 생성하십시오. 즉, 함수 내의 `result` 라는 객체에 `x**a` 값을 저장하면 다음 줄을 사용하여 이 결과를 간단히 `return` 할 수 있습니다:

```python
return result
```

   Note that the line above should be the last line in your function, and it should be indented 4 spaces. 
   위의 줄은 함수의 마지막 줄이어야 하며, 4칸 들여쓰기(indented) 되어야 함을 유의하십시오.
   - (e) Now using the `Power3()` function, create a plot of $f(x) = x^2$. The $x$-axis should display a range of integers from 1 to 10, and the $y$-axis should display $x^2$. Label the axes appropriately, and use an appropriate title for the figure. Consider displaying either the $x$-axis, the $y$-axis, or both on the log-scale. You can do this by using the `ax.set_xscale()` and `ax.set_yscale()` methods of the axes you are plotting to. 
   - (e) 이제 `Power3()` 함수를 사용하여 $f(x) = x^2$ 의 도표를 작성하십시오. $x$-축은 1부터 10까지의 정수 범위를 표시해야 하고, $y$-축은 $x^2$ 을 표시해야 합니다. 축에 적절하게 레이블을 지정하고 그림에 적절한 제목을 사용하십시오. $x$ 축이나 $y$ 축 혹은 양축 모두에 로그 척도(log-scale)를 표시하는 것을 고려하십시오. 도표를 그리는 Axes의 `ax.set_xscale()` 및 `ax.set_yscale()` 메서드를 사용하여 이를 수행할 수 있습니다.
   - (f) Create a function, `PlotPower()`, that allows you to create a plot of `x` against `x**a` for a fixed `a` and a sequence of values of x. For instance, if you call 
   - (f) 고정된 `a` 값과 `x` 인자 값 시퀀스(sequence)에 대하여 `x` 대비 `x**a` 도표를 만들 수 있는 함수 `PlotPower()` 를 생성하십시오. 예를 들어 다음과 같이 호출하면:

```python
PlotPower(np.arange(1, 11), 3)
```

   then a plot should be created with an $x$-axis taking on values $1, 2, \dots, 10$, and a $y$-axis taking on values $1^3, 2^3, \dots, 10^3$. 
   그러면 $x$ 축은 $1, 2, \dots, 10$ 값을 갖고 $y$ 축은 $1^3, 2^3, \dots, 10^3$ 값을 갖는 도표가 생성되어야 합니다.

16. Using the `Boston` data set, fit classification models in order to predict whether a given suburb has a crime rate above or below the median. Explore logistic regression, LDA, naive Bayes, and KNN models using various subsets of the predictors. Describe your findings. 
16. `Boston` 데이터 세트를 사용하여 주어진 교외 지역의 범죄율이 중앙값(median) 보다 높은지 낮은지 여부를 예측하기 위해 분류 모델을 피팅하십시오. 예측 변수의 다양한 부분 집합(subsets)을 사용하여 로지스틱 회귀, LDA, 나이브 베이즈 및 KNN 모델들을 탐색하십시오. 결과를 설명하십시오.
_Hint: You will have to create the response variable yourself, using the variables that are contained in the_ `Boston` _data set._
_힌트:_ `Boston` _데이터 세트에 포함된 변수들을 사용하여 여러분 자신이 직접 반응 변수를 생성해야 할 것입니다._

---

## Sub-Chapters

[< 4.8.1 Conceptual](../4_8_1_conceptual/trans1.html)
