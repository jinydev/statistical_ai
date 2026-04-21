---
layout: default
title: "index"
---

[< 4.8.1 Conceptual](../4_8_1_conceptual/index.html)

# _Applied_ 
# _응용_

13. This question should be answered using the `Weekly` data set, which is part of the `ISLP` package. This data is similar in nature to the `Smarket` data from this chapter’s lab, except that it contains 1,089 weekly returns for 21 years, from the beginning of 1990 to the end of 2010. 
13. 이 질문은 `ISLP` 패키지의 일부인 `Weekly` 데이터 세트를 사용하여 답변해야 한다. 이 데이터는 1990년 초부터 2010년 말까지 21년 동안의 1,089개의 주간 수익률을 포함한다는 점을 제외하면, 성격상 이 장의 랩에 있는 `Smarket` 데이터와 유사하다.
   - (a) Produce some numerical and graphical summaries of the `Weekly` data. Do there appear to be any patterns? 
   - (a) `Weekly` 데이터의 수치적 및 그래픽 요약을 일부 생성하라. 어떤 패턴이 나타나는가?
   - (b) Use the full data set to perform a logistic regression with `Direction` as the response and the five lag variables plus `Volume` as predictors. Use the summary function to print the results. Do any of the predictors appear to be statistically significant? If so, which ones? 
   - (b) 전체 데이터 세트를 사용하여 `Direction`을 반응 변수로, 그리고 5개의 시차(lag) 변수와 `Volume`을 예측 변수로 하여 로지스틱 회귀를 수행하라. 요약 함수를 사용하여 결과를 출력하라. 통계적으로 유의미해 보이는 예측 변수가 있는가? 그렇다면 어느 것인가?
   - (c) Compute the confusion matrix and overall fraction of correct predictions. Explain what the confusion matrix is telling you about the types of mistakes made by logistic regression. 
   - (c) 혼동 행렬(confusion matrix)과 전체 올바른 예측의 비율을 계산하라. 혼동 행렬이 로지스틱 회귀에 의해 만들어진 실수의 유형에 대해 무엇을 알려주는지 설명하라.
   - (d) Now fit the logistic regression model using a training data period from 1990 to 2008, with `Lag2` as the only predictor. Compute the confusion matrix and the overall fraction of correct predictions for the held out data (that is, the data from 2009 and 2010). 
   - (d) 이제 `Lag2`만을 예측 변수로 사용하여, 1990년부터 2008년까지의 훈련 데이터 기간을 사용해 로지스틱 회귀 모델을 적합하라. 남겨둔 데이터(즉, 2009년 및 2010년 데이터)에 대해 혼동 행렬과 전체 올바른 예측의 비율을 계산하라.
   - (e) Repeat (d) using LDA. 
   - (e) LDA를 사용하여 (d)를 반복하라.
   - (f) Repeat (d) using QDA. 
   - (f) QDA를 사용하여 (d)를 반복하라.
   - (g) Repeat (d) using KNN with $K = 1$. 
   - (g) $K = 1$인 KNN을 사용하여 (d)를 반복하라.
   - (h) Repeat (d) using naive Bayes. 
   - (h) 나이브 베이즈를 사용하여 (d)를 반복하라.
   - (i) Which of these methods appears to provide the best results on this data? 
   - (i) 이 방법들 중 어느 것이 이 데이터에서 가장 좋은 결과를 제공하는 것으로 보이는가?
   - (j) Experiment with different combinations of predictors, including possible transformations and interactions, for each of the methods. Report the variables, method, and associated confusion matrix that appears to provide the best results on the held out data. Note that you should also experiment with values for $K$ in the KNN classifier. 
   - (j) 각각의 방법에 대해, 가능한 변환 및 상호작용을 포함하여 여러 예측 변수 조합으로 실험하라. 남겨둔 데이터에 대해 가장 좋은 결과를 제공하는 것으로 보이는 변수, 방법, 그리고 연관된 혼동 행렬을 보고하라. KNN 분류기에서 $K$ 값으로도 실험해야 한다는 점에 유의하라.

14. In this problem, you will develop a model to predict whether a given car gets high or low gas mileage based on the `Auto` data set. 
14. 이 문제에서는 `Auto` 데이터 세트에 근거하여 주어진 자동차가 높거나 낮은 연비(gas mileage)를 내는지 예측하는 모델을 개발할 것이다.
   - (a) Create a binary variable, `mpg01`, that contains a 1 if `mpg` contains a value above its median, and a 0 if `mpg` contains a value below its median. You can compute the median using the `median()` method of the data frame. Note you may find it helpful to add a column `mpg01` to the data frame by assignment. Assuming you have stored the data frame as `Auto`, this can be done as follows: 
   - (a) 만약 `mpg`가 중앙값 이상의 값을 포함하면 1을 포함하고, `mpg`가 중앙값 미만의 값을 포함하면 0을 포함하는 이진 변수 `mpg01`을 생성하라. 데이터 프레임의 `median()` 메서드를 사용하여 중앙값을 계산할 수 있다. 할당을 통해 데이터 프레임에 `mpg01` 열을 추가하는 것이 도움이 될 수 있다는 점에 유의하라. 데이터 프레임을 `Auto`로 저장했다고 가정할 때, 이는 다음과 같이 수행할 수 있다.

```python
Auto['mpg01'] = mpg01
```

   - (b) Explore the data graphically in order to investigate the association between `mpg01` and the other features. Which of the other features seem most likely to be useful in predicting `mpg01`? Scatterplots and boxplots may be useful tools to answer this question. Describe your findings. 
   - (b) `mpg01`과 다른 피처 간의 연관성을 조사하기 위해 그래픽으로 데이터를 탐색하라. 다른 피처 중 어느 것이 `mpg01`을 예측하는 데 가장 유용할 가능성이 높아 보이는가? 산점도 및 상자 그림(boxplot)은 이 질문에 답하는 데 유용한 도구일 수 있다. 당신의 발견을 설명하라.
   - (c) Split the data into a training set and a test set. 
   - (c) 데이터를 훈련 세트와 테스트 세트로 분할하라.
   - (d) Perform LDA on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (d) (b)에서 `mpg01`과 가장 연관성이 높아 보였던 변수를 사용하여 `mpg01`을 예측하기 위해 훈련 데이터에 LDA를 수행하라. 구한 모델의 테스트 오류는 얼마인가?
   - (e) Perform QDA on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (e) (b)에서 `mpg01`과 가장 연관성이 높아 보였던 변수를 사용하여 `mpg01`을 예측하기 위해 훈련 데이터에 QDA를 수행하라. 구한 모델의 테스트 오류는 얼마인가?
   - (f) Perform logistic regression on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (f) (b)에서 `mpg01`과 가장 연관성이 높아 보였던 변수를 사용하여 `mpg01`을 예측하기 위해 훈련 데이터에 로지스틱 회귀를 수행하라. 구한 모델의 테스트 오류는 얼마인가?
   - (g) Perform naive Bayes on the training data in order to predict `mpg01` using the variables that seemed most associated with `mpg01` in (b). What is the test error of the model obtained? 
   - (g) (b)에서 `mpg01`과 가장 연관성이 높아 보였던 변수를 사용하여 `mpg01`을 예측하기 위해 훈련 데이터에 나이브 베이즈를 수행하라. 구한 모델의 테스트 오류는 얼마인가?
   - (h) Perform KNN on the training data, with several values of $K$, in order to predict `mpg01`. Use only the variables that seemed most associated with `mpg01` in (b). What test errors do you obtain? Which value of $K$ seems to perform the best on this data set? 
   - (h) 훈련 데이터상에서 여러 $K$ 값으로 KNN을 수행하여 `mpg01`을 예측하라. (b)에서 `mpg01`과 가장 연관성이 높아 보였던 변수만을 사용하라. 어떠한 테스트 오류들을 얻는가? 어떠한 $K$ 값이 이 데이터 세트에서 가장 잘 수행되는 것으로 보이는가?

15. This problem involves writing functions. 
15. 이 문제는 함수 작성을 수반한다.
   - (a) Write a function, `Power()`, that prints out the result of raising 2 to the 3rd power. In other words, your function should compute $2^3$ and print out the results. 
   - (a) 2의 3제곱에 해당하는 결과를 출력하는 함수 `Power()`를 작성하라. 즉, 당신의 함수는 $2^3$을 계산하고 그 결과를 출력해야 한다.
      - _Hint: Recall that_ `x**a` _raises_ `x` _to the power_ `a`. _Use the_ `print()` _function to display the result._ 
      - _힌트:_ `x**a`_는_ `x`_를_ `a`_승으로 만든다는 것을 상기하라. 결과를 표시하려면_ `print()` _함수를 사용하라._
   - (b) Create a new function, `Power2()`, that allows you to pass _any_ two numbers, `x` and `a`, and prints out the value of `x**a`. You can do this by beginning your function with the line 
   - (b) _임의의_ 두 숫자 `x` 및 `a`를 전달할 수 있게 허용하고 `x**a`의 값을 출력하는 새로운 함수 `Power2()`를 생성하라. 당신은 함수를 다음 줄로 시작하여 이 작업을 수행할 수 있다.

```python
def Power2(x, a):
```

   You should be able to call your function by entering, for instance, 
   예를 들어 다음과 같이 입력함으로써 당신의 함수를 호출할 수 있어야 한다.

```python
Power2(3, 8)
```

   on the command line. This should output the value of $3^8$, namely, $6,561$. 
   명령줄(command line)에 입력한다. 이것은 $3^8$의 값, 즉 $6,561$을 출력해야 정답이다.

   - (c) Using the `Power2()` function that you just wrote, compute $10^3, 8^{17}$, and $131^3$. 
   - (c) 방금 작성한 `Power2()` 함수를 사용하여 $10^3, 8^{17}$, 및 $131^3$을 계산하라.
   - (d) Now create a new function, `Power3()`, that actually _returns_ the result `x**a` as a `Python` object, rather than simply printing it to the screen. That is, if you store the value `x**a` in an object called `result` within your function, then you can simply `return` this result, using the following line: 
   - (d) 이제 화면에 단순히 출력하는 대신, 결과 `x**a`를 `Python` 객체로서 실제로 _반환(return)하는_ 새로운 함수 `Power3()`를 생성하라. 즉, 함수 내에서 `result`라는 객체에 값 `x**a`를 저장한다면, 다음 줄을 사용하여 단지 이 결과를 `return`할 수 있다.

```python
return result
```

   Note that the line above should be the last line in your function, and it should be indented 4 spaces. 
   위의 줄이 당신 함수의 마지막 줄이어야 하며, 4칸 인덴트(들여쓰기)되어야 함에 유의하라.
   - (e) Now using the `Power3()` function, create a plot of $f(x) = x^2$. The $x$-axis should display a range of integers from 1 to 10, and the $y$-axis should display $x^2$. Label the axes appropriately, and use an appropriate title for the figure. Consider displaying either the $x$-axis, the $y$-axis, or both on the log-scale. You can do this by using the `ax.set_xscale()` and `ax.set_yscale()` methods of the axes you are plotting to. 
   - (e) 이제 `Power3()` 함수를 사용하여 $f(x) = x^2$의 그림(plot)을 생성하라. $x$축은 1에서 10까지의 정수 범위를 표시해야 하고, $y$축은 $x^2$를 표시해야 한다. 축에 적절하게 레이블을 지정하고 도면(figure)에 적합한 제목을 사용하라. $x$축, $y$축, 또는 둘 다 로그 스케일(log-scale)로 표시하는 것을 고려하라. 플로팅 중인 축의 `ax.set_xscale()` 및 `ax.set_yscale()` 메서드를 사용하여 이 작업을 수행할 수 있다.
   - (f) Create a function, `PlotPower()`, that allows you to create a plot of `x` against `x**a` for a fixed `a` and a sequence of values of x. For instance, if you call 
   - (f) 고정된 `a`와 `x`의 값들의 시퀀스에 대해 `x` 대 `x**a`의 그림(plot)을 생성할 수 있게 허용하는 함수 `PlotPower()`를 생성하라. 예를 들어, 당신이 다음을 호출하면

```python
PlotPower(np.arange(1, 11), 3)
```

   then a plot should be created with an $x$-axis taking on values $1, 2, \dots, 10$, and a $y$-axis taking on values $1^3, 2^3, \dots, 10^3$. 
   그러면 1, 2, \dots, 10 값을 취하는 $x$축과 $1^3, 2^3, \dots, 10^3$ 값을 취하는 $y$축을 가진 그림이 생성되어야 한다.

16. Using the `Boston` data set, fit classification models in order to predict whether a given suburb has a crime rate above or below the median. Explore logistic regression, LDA, naive Bayes, and KNN models using various subsets of the predictors. Describe your findings. 
16. `Boston` 데이터 세트를 사용하여 주어진 교외의 범죄율이 중앙값보다 높은지 낮은지를 예측하기 위해 분류 모델을 적합하라. 여러 다양한 예측 변수들의 부분 집합을 사용하여 로지스틱 회귀, LDA, 나이브 베이즈 및 KNN 모델을 탐색하라. 당신의 발견을 설명하라.
_Hint: You will have to create the response variable yourself, using the variables that are contained in the_ `Boston` _data set._
_힌트:_ `Boston` _데이터 세트에 포함된 변수를 사용하여 반응 변수를 당신 스스로 구축(생성)해야 할 것이다._

---

## Sub-Chapters


[< 4.8.1 Conceptual](../4_8_1_conceptual/index.html)
