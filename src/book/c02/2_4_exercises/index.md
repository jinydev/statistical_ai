---
layout: default
title: "index"
---

# 2.4 Exercises
# 2.4 연습문제

## _Conceptual_
## 개념 문제

1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

1. (a)부터 (d)까지의 각 항목에 대하여, 유연한(flexible) 통계 학습 방법의 성능이 유연하지 않은(inflexible) 방법보다 일반적으로 더 나을 것으로 기대되는지 아니면 더 나쁠 것으로 기대되는지 명시하십시오. 그리고 그 이유를 정당화하십시오.

   - (a) The sample size $n$ is extremely large, and the number of predictors $p$ is small.

   - (a) 표본 크기 $n$ 이 매우 크고, 예측 변수의 수 $p$ 가 적은 경우.

   - (b) The number of predictors $p$ is extremely large, and the number of observations $n$ is small.

   - (b) 예측 변수의 수 $p$ 가 매우 크고, 관측치의 수 $n$ 이 적은 경우.

   - (c) The relationship between the predictors and response is highly non-linear.

   - (c) 예측 변수와 응답 사이의 관계가 매우 비선형적인 경우.

   - (d) The variance of the error terms, i.e. $\sigma^2 = \text{Var}(\epsilon)$, is extremely high.

   - (d) 오차항의 분산, 즉 $\sigma^2 = \text{Var}(\epsilon)$ 이 매우 높은 경우.

2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide $n$ and $p$.

2. 다음의 각 시나리오가 분류(classification) 문제인지 회귀(regression) 문제인지 설명하고, 우리가 추론(inference)과 예측(prediction) 중 어느 것에 더 관심이 있는지 명시하십시오. 마지막으로 $n$ 과 $p$ 를 제공하십시오.

   - (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.

   - (a) 우리는 미국 상위 500대 기업에 대한 데이터를 수집합니다. 각 기업에 대해 우리는 이익, 직원 수, 산업, 그리고 CEO 급여를 기록합니다. 우리는 어떤 요인들이 CEO 급여에 영향을 미치는지 이해하고자 합니다.

   - (b) We are considering launching a new product and wish to know whether it will be a _success_ or a _failure_. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

   - (b) 우리는 신제품 출시를 고려 중이며 그것이 _성공_ 할지 아니면 _실패_ 할지 알고 싶습니다. 우리는 이전에 출시되었던 유사한 제품 20개에 대한 데이터를 수집합니다. 각 제품에 대해 우리는 성공 여부, 제품에 책정된 가격, 마케팅 예산, 경쟁사 가격, 그리고 10개의 다른 변수들을 기록했습니다.

   - (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

   - (c) 우리는 세계 주식 시장의 주간 변동성에 비례하여 USD/유로 환율의 % 변동을 예측하는 데 관심이 있습니다. 따라서 우리는 2012년 한 해 동안의 주간 데이터를 수집합니다. 매주 우리는 USD/유로의 % 변동, 미국 시장의 % 변동, 영국 시장의 % 변동, 그리고 독일 시장의 % 변동을 기록합니다.

3. We now revisit the bias-variance decomposition.

3. 이제 우리는 편향-분산(bias-variance) 분해를 다시 살펴봅니다.

   - (a) Provide a sketch of typical (squared) bias, variance, training error, test error, and Bayes (or irreducible) error curves, on a single plot, as we go from less flexible statistical learning methods towards more flexible approaches. The $x$-axis should represent the amount of flexibility in the method, and the $y$-axis should represent the values for each curve. There should be five curves. Make sure to label each one.

   - (a) 덜 유연한 통계 학습 방법에서 더 유연한 접근 방식으로 넘어감에 따라 그려지는 전형적인 편향 제곱, 분산, 훈련 오차, 테스트 오차, 그리고 베이즈 (또는 줄일 수 없는) 오차 곡선의 스케치를 하나의 도면에 제공하십시오. $x$ 축은 방법론에 존재하는 유연성의 양을 나타내고, $y$ 축은 각 곡선의 값을 나타내야 합니다. 여기엔 다섯 개의 곡선이 있어야 합니다. 각 곡선의 라벨을 명확히 표시하십시오.

   - (b) Explain why each of the five curves has the shape displayed in part (a).

   - (b) 다섯 개의 곡선들이 왜 각각 (a)에서 표시된 모양을 갖는지 설명하십시오.

4. You will now think of some real-life applications for statistical learning.

4. 이제 당신은 통계적 학습을 위한 실제 적용 사례들을 구상하게 될 것입니다.

   - (a) Describe three real-life applications in which _classification_ might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.

   - (a) _분류_ 가 유용할 수 있는 일상 속의 응용 사례 세 가지를 서술하십시오. 예측 변수들과 더불어 예상되는 응답을 기재하십시오. 각 적용 사례의 목표가 추론입니까, 아니면 예측입니까? 답변을 설명하십시오.

   - (b) Describe three real-life applications in which _regression_ might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.

   - (b) _회귀_ 가 유용할 수 있는 일상 속의 응용 사례 세 가지를 서술하십시오. 예측 변수들과 더불어 예상되는 응답을 기재하십시오. 각 적용 사례의 목표가 추론입니까, 아니면 예측입니까? 답변을 설명하십시오.

   - (c) Describe three real-life applications in which _cluster analysis_ might be useful.

   - (c) _군집 분석(cluster analysis)_ 이 유용할 수 있는 일상 속의 응용 사례 세 가지를 서술하십시오.

5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

5. 회귀나 분류 문제를 풀 때, 매우 유연한 접근 방식의 장점과 단점은 (덜 유연한 접근법에 비해) 무엇입니까? 어떤 상황에서 덜 유연한 접근법보다 더 유연한 접근법이 선호될 수 있습니까? 덜 유연한 접근법이 더 선호될 수 있는 상황은 언제입니까?

6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are its disadvantages?

6. 모수적(parametric) 통계 학습 방식과 비모수적(non-parametric) 학습 방식의 차이점을 설명하십시오. (비모수적 접근법과는 대조적으로) 회귀나 분류 문제에 있어 모수적 접근법이 지니는 고유 장점은 무엇입니까? 단점은 무엇입니까?

7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

7. 아래의 표는 총 6개의 관측치, 3개의 예측 변수, 그리고 1개의 질적 응답 변수를 포함하는 훈련 데이터 세트를 보여줍니다.

| Obs. | $X_1$ | $X_2$ | $X_3$ | $Y$ |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 3 | 0 | Red |
| 2 | 2 | 0 | 0 | Red |
| 3 | 0 | 1 | 3 | Red |
| 4 | 0 | 1 | 2 | Green |
| 5 | $-1$ | 0 | 1 | Green |
| 6 | 1 | 1 | 1 | Red |

Suppose we wish to use this data set to make a prediction for $Y$ when $X_1 = X_2 = X_3 = 0$ using $K$-nearest neighbors.

우리가 만약 $K$-최근접 이웃(K-nearest neighbors) 알고리즘을 구동해 $X_1 = X_2 = X_3 = 0$ 지점의 $Y$ 클래스를 예측하고자 할 때 이 특정 데이터 세트를 활용한다고 가정해 봅시다.

- (a) Compute the Euclidean distance between each observation and the test point, $X_1 = X_2 = X_3 = 0$.

- (a) 각 관측치와 이 테스트 지점 $X_1 = X_2 = X_3 = 0$ 그룹 간의 유클리드 거리(Euclidean distance)를 계산하십시오.

- (b) What is our prediction with $K = 1$? Why?

- (b) 알고리즘에서 $K = 1$ 일 때 우리의 최종 예측은 무엇으로 판명됩니까? 왜 그렇습니까?

- (c) What is our prediction with $K = 3$? Why?

- (c) 이번엔 $K = 3$ 일 때를 가정해 보십시오. 우리의 예측은 무엇이 됩니까? 이유는 무엇입니까?

- (d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the _best_ value for $K$ to be large or small? Why?

- (d) 만약 본 문제에서 이상적 진단 구획인 베이즈 결정 경계(Bayes decision boundary) 자체가 극도로 비선형적 굴곡을 그릴 경우, 우리는 제원상 최적의 _가장 타당한(best)_ $K$ 값이 커야 한다고 예측하게 됩니까 혹은 작아야 한다고 여기게 됩니까? 사유를 밝히십시오.

## _Applied_
## 응용 문제

8. This exercise relates to the `College` data set, which can be found in the file `College.csv` on the book website. It contains a number of variables for 777 different universities and colleges in the US. The variables are 

8. 이 연습문제는 책 웹사이트의 `College.csv` 파일에서 찾을 수 있는 `College` 데이터 세트와 관련이 있습니다. 여기에는 미국의 777개 대학 및 대학교들에 대한 여러 변수들이 포함되어 있습니다. 변수들은 다음과 같습니다:

   - `Private` : Public/private indicator 

   - `Private` : 공립/사립을 나타내는 지표

   - `Apps` : Number of applications received 

   - `Apps` : 접수된 지원서의 수

   - `Accept` : Number of applicants accepted 

   - `Accept` : 합격된 지원자의 수

   - `Enroll` : Number of new students enrolled 

   - `Enroll` : 새로 등록한 학생의 수

   - `Top10perc` : New students from top 10 % of high school class 

   - `Top10perc` : 고등학교 내신 상위 10% 이내인 신입생의 등급

   - `Top25perc` : New students from top 25 % of high school class 

   - `Top25perc` : 고등학교 내신 상위 25% 이내인 신입생의 등급

   - `F.Undergrad` : Number of full-time undergraduates 

   - `F.Undergrad` : 정규직 (전일제) 학부생의 수

   - `P.Undergrad` : Number of part-time undergraduates 

   - `P.Undergrad` : 비정규직 (시간제) 학부생의 수

   - `Outstate` : Out-of-state tuition 

   - `Outstate` : 타주 출신 학생의 등록금

   - `Room.Board` : Room and board costs 

   - `Room.Board` : 기숙사 및 식비

   - `Books` : Estimated book costs 

   - `Books` : 예상되는 교재비

   - `Personal` : Estimated personal spending 

   - `Personal` : 예상되는 개인 지출 비용

   - `PhD` : Percent of faculty with Ph.D.s 

   - `PhD` : 박사 학위(Ph.D.) 소지 교수진의 비율(%)

   - `Terminal` : Percent of faculty with terminal degree 

   - `Terminal` : 최종 학위(Terminal degree) 소지 교수진의 비율(%)

   - `S.F.Ratio` : Student/faculty ratio 

   - `S.F.Ratio` : 학생 대 교수 비율

   - `perc.alumni` : Percent of alumni who donate 

   - `perc.alumni` : 기부하는 동문의 비율(%)

   - `Expend` : Instructional expenditure per student 

   - `Expend` : 학생 1인당 교육 지출 비용

   - `Grad.Rate` : Graduation rate 

   - `Grad.Rate` : 졸업률

Before reading the data into `Python`, it can be viewed in Excel or a text editor.

데이터를 `Python` 으로 읽어들이기 전에, 엑셀이나 텍스트 편집기에서 미리 볼 수 있습니다.

- (a) Use the `pd.read_csv()` function to read the data into `Python`. Call the loaded data `college`. Make sure that you have the directory set to the correct location for the data.

- (a) `pd.read_csv()` 함수를 사용하여 데이터를 `Python` 으로 읽어들이십시오. 로드된 데이터 변수를 `college` 라고 부르십시오. 데이터가 위치한 올바른 경로로 디렉토리가 설정되어 있는지 확인하십시오.

- (b) Look at the data used in the notebook by creating and running a new cell with just the code `college` in it. You should notice that the first column is just the name of each university in a column named something like `Unnamed: 0`. We don’t really want `pandas` to treat this as data. However, it may be handy to have these names for later. Try the following commands and similarly look at the resulting data frames:

- (b) 노트북에 `college` 코드만 포함된 새 셀을 만들고 실행하여 사용 중인 데이터를 살펴보십시오. 첫 번째 열은 단지 대학 이름들이 나열된, `Unnamed: 0` 처럼 명명된 이름뿐임을 알아차려야 합니다. 우리는 `pandas` 가 이것을 실제 데이터로 취급하는 것을 원치 않습니다. 하지만 나중을 위해 이 이름들을 보존하는 것은 유용할 수 있습니다. 다음 명령어들을 시도해 보고 결과 데이터 프레임들을 비슷하게 살펴보십시오:

```python
college2 = pd.read_csv('College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college3.set_index('College')
```

This has used the first column in the file as an `index` for the data frame. This means that `pandas` has given each row a name corresponding to the appropriate university. Now you should see that the first data column is `Private`. Note that the names of the colleges appear on the left of the table. We also introduced a new python object above: a _dictionary_, which is specified by `(key, value)` pairs. Keep your modified version of the data with the following:

이 단계는 파일의 첫 번째 열을 데이터 프레임의 고유 `index` (인덱스)로 사용하게 한 것입니다. 이는 곧 `pandas` 가 각 행마다 해당 대학에 일치하는 이름을 부여했음을 의미합니다. 이제 여러분은 첫 번째 데이터 열이 자연스레 `Private` 로 변경되었음을 확인해야 합니다. 대학들의 이름은 표의 가장 왼쪽에 따로 나타남에 유의하십시오. 이 과정에서 우리는 위 코드에 새로운 파이썬 객체인 _딕셔너리(dictionary)_ 도 도입했는데, 이는 `(키, 값)` 쌍으로 지정됩니다. 여러분이 변경한 버전의 데이터를 보존하기 위해 다음 코드를 유지하십시오:

```python
college = college3
```

- (c) Use the `describe()` method to produce a numerical summary of the variables in the data set.

- (c) `describe()` 메서드를 사용하여 데이터 세트 내 변수들의 수치적 요약을 생성하십시오.

- (d) Use the `pd.plotting.scatter_matrix()` function to produce a scatterplot matrix of the first columns `[Top10perc, Apps, Enroll]`. Recall that you can reference a list `C` of columns of a data frame `A` using `A[C]`.

- (d) `pd.plotting.scatter_matrix()` 함수를 사용하여 열 `[Top10perc, Apps, Enroll]` 로 구성된 요소의 산점도 행렬을 생성하십시오. 데이터 프레임 `A` 에 속한 특정 열들의 목록인 `C` 를 참조할 때 `A[C]` 문법을 사용할 수 있음을 상기하십시오.

- (e) Use the `boxplot()` method of `college` to produce side-by-side boxplots of `Outstate` versus `Private`.

- (e) `college` 의 `boxplot()` 메서드를 사용하여 `Private` 구분에 따른 `Outstate` 의 나란한 박스플롯(상자 수염 그림)을 생성하십시오.

- (f) Create a new qualitative variable, called `Elite`, by _binning_ the `Top10perc` variable into two groups based on whether or not the proportion of students coming from the top 10% of their high school classes exceeds 50%.

- (f) 고등학교 내신 최상위 10% 출신 학생들이 차지하는 비율이 과연 50%를 초과하는지 여부에 따라 `Top10perc` 변수를 _구간화(binning)_ 함으로써 두 그룹으로 나눈 새로운 질적 변수 `Elite` 를 새로 생성하십시오.

```python
college['Elite'] = pd.cut(college['Top10perc'],
                          [0, 50, 100],
                          labels=['No', 'Yes'])
```
*(Note: the threshold logic typically uses 50 for the 50% marker, since Top10perc stores values up to 100 rather than ratios up to 1, adjust as necessary per dataset).*
*(참고: Top10perc 변수는 비율을 나타내는 1 대신 100까지의 숫자를 저장하므로, 임계값 분기 논리에서 50% 의 기준으로 보통 50 을 사용합니다. 필요 시 데이터 세트에 맞게 값을 조정하십시오).*

  Use the `value_counts()` method of `college['Elite']` to see how many elite universities there are. Finally, use the `boxplot()` method again to produce side-by-side boxplots of `Outstate` versus `Elite`.

  본 데이터에서 `college['Elite']` 의 `value_counts()` 내부 메서드를 사용하여 엘리트 대학이 몇 개나 존재하는지 확인하십시오. 마지막으로 `boxplot()` 통합 메서드를 다시 한 번 더 사용하여 `Elite` 구분에 따른 `Outstate` 의 나란한 박스플롯을 생성하십시오.

- (g) Use the `plot.hist()` method of `college` to produce some histograms with differing numbers of bins for a few of the quantitative variables. The command `plt.subplots(2, 2)` may be useful: it will divide the plot window into four regions so that four plots can be made simultaneously. By changing the arguments you can divide the screen up in other combinations.

- (g) `college` 의 내부 함수 `plot.hist()` 메서드를 사용하여, 서로 다른 구간 막대 수(bins)를 부여 지닌 몇 가지 양적 변수에 대한 일련의 히스토그램을 생성 출력하십시오. 이때 `plt.subplots(2, 2)` 지정 명령어가 꽤 유용하게 쓰일 수 있습니다: 이 코드는 사용자의 플롯 창을 4개의 영역으로 균등 분할하므로 총 4개의 플롯 그림을 동시에 그릴 수 있게 통제합니다. 내부 인수를 변경함으로써 창 화면을 다른 여러 조합 비율로 분할할 수도 있습니다.

- (h) Continue exploring the data, and provide a brief summary of what you discover.

- (h) 스스로 데이터를 다각도로 더 집중 탐색해 보고, 새롭게 발견한 사실에 대해 간략한 요약을 제공하십시오.

9. This exercise involves the `Auto` data set studied in the lab. Make sure that the missing values have been removed from the data.

9. 이 연습문제는 실습에서 집중 연구했던 대상인 `Auto` 데이터 세트 표본을 수반합니다. 데이터에서 결측값이 모두 확실히 제거되었는지 확인하십시오.

   - (a) Which of the predictors are quantitative, and which are qualitative?

   - (a) 이 변수들 중에서 어느 것이 양적 변수이며, 어느 것이 질적입니까?

   - (b) What is the _range_ of each quantitative predictor? You can answer this using the `min()` and `max()` methods in `numpy`.

   - (b) 각 양적 예측 변수의 _범위(range)_ 수치폭은 어떻게 됩니까? 여러분은 이에 답하기 위해 `numpy` 모듈의 `min()` 함수 및 `max()` 메서드 기능을 사용할 수 있습니다.

   - (c) What is the mean and standard deviation of each quantitative predictor?

   - (c) 각 양적 판단 예측 변수의 평균값(mean)과 표준 편차(standard deviation)는 무엇입니까?

   - (d) Now remove the 10th through 85th observations. What is the range, mean, and standard deviation of each predictor in the subset of the data that remains?

   - (d) 이번엔 데이터 표본의 10번째부터 85번째까지의 관측치를 제거하십시오. అలా 삭제를 마친 후 남은 데이터 부분 집합(subset) 안에서, 각 개별 예측 변수들의 범위와 평균, 그리고 표준 편차는 어떻게 도출됩니까?

   - (e) Using the full data set, investigate the predictors graphically, using scatterplots or other tools of your choice. Create some plots highlighting the relationships among the predictors. Comment on your findings.

   - (e) 전체 원본 데이터 세트를 온전히 사용하여 산점도 창이나 스스로 선택한 툴 기능들을 통해 해당 예측 변수들을 시각적으로 조사하십시오. 예측 매개 변수들 간의 관계를 강조하는 몇 가지 플롯들을 만들어 보십시오. 찾아낸 결과물에 논평을 남기십시오.

   - (f) Suppose that we wish to predict gas mileage (`mpg`) on the basis of the other variables. Do your plots suggest that any of the other variables might be useful in predicting `mpg`? Justify your answer.

   - (f) 이번엔 우리가 다른 변수들을 토대로 차량의 가스 연비인 (`mpg`) 를 예측해 내고자 한다고 가정합시다. 여러분의 플롯 그래프들은 다른 변수들이 이 `mpg` 변수를 예측하는 데 유용할지 구체적으로 조언합니까? 왜 그렇게 단정한 것인지 명확한 논거로 답변을 정당화하십시오.

10. This exercise involves the `Boston` housing data set.

10. 이 연습문제는 `Boston` 보스턴 주택 데이터 세트를 수반합니다.

    - (a) To begin, load in the `Boston` data set, which is part of the `ISLP` library.

    - (a) 처음으로, `ISLP` 라이브러리의 일부분인 `Boston` 데이터 세트를 로드하십시오.

    - (b) How many rows are in this data set? How many columns? What do the rows and columns represent?

    - (b) 이 데이터 세트에는 총 몇 개의 행이 존재합니까? 열은 몇 개입니까? 행과 열들은 각각 무엇을 나타냅니까?

    - (c) Make some pairwise scatterplots of the predictors (columns) in this data set. Describe your findings.

    - (c) 이 데이터 안에서 예측 변수(columns) 상호 쌍들에 대해 산점도 쌍을 몇 개 생성해 보십시오. 그리고 발견해 낸 점들을 설명하십시오.

    - (d) Are any of the predictors associated with per capita crime rate? If so, explain the relationship.

    - (d) 예측 변수들 중에서 1인당 범죄율과 깊이 상호 연관된 것이 하나라도 있습니까? 만약 존재한다면 그 관계를 설명하십시오.

    - (e) Do any of the suburbs of Boston appear to have particularly high crime rates? Tax rates? Pupil-teacher ratios? Comment on the range of each predictor.

    - (e) 보스턴 외곽 지역 중에서 특히 범죄율이 현저히 높은 지역이 존재합니까? 세금 비율이 높은 지역은요? 학생 대 교사 비율이 높은 지역은 있습니까? 이들 각 기준 변수들의 범위에 대해 논평 커멘트를 남기십시오.

    - (f) How many of the suburbs in this data set bound the Charles river?

    - (f) 세트 내 몇 개의 교외 외곽 지역이 찰스(Charles) 강에 연접해 있습니까?

    - (g) What is the median pupil-teacher ratio among the towns in this data set?

    - (g) 이 데이터에 포함된 타운 지역들의 학생-교사 비율의 중앙값(median) 수치는 정확히 무엇입니까?

    - (h) Which suburb of Boston has lowest median value of owneroccupied homes? What are the values of the other predictors for that suburb, and how do those values compare to the overall ranges for those predictors? Comment on your findings.

    - (h) 보스턴 교외 지역 중에서 자가 소유 주택들의 자산 중앙값이 가장 낮은 곳은 어느 지역입니까? 그 특정 지역이 가진 다른 예측 변수 지표들의 값은 무엇입니까? 그리고 그런 해당 값들은 전체 집합 범위들과 과연 어떻게 서로 비교됩니까? 여러분이 발견한 결과 내용에 논평하십시오.

    - (i) In this data set, how many of the suburbs average more than seven rooms per dwelling? More than eight rooms per dwelling? Comment on the suburbs that average more than eight rooms per dwelling.

    - (i) 본 시스템 데이터상, 주거지 1채당 평균적으로 무려 방이 7개 이상 존재하는 교외 지역구는 총 몇 개 지정되어 부합합니까? 그렇다면 평단 8개 이상의 다중 방을 보유한 곳은 몇 곳입니까? 방이 8개 이상인 교외 지역의 내원에 대해 별도 논평을 해 보십시오.

---

## Sub-Chapters (하위 목차)

현재 2.4 연습문제 소속 문서입니다.
[목차로 돌아가기](../../)