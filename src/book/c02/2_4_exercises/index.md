---
layout: default
title: "index"
---

# 2.4 Exercises

# 2.4 연습문제들

## _Conceptual_

## _개념적 문제_

1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

1. (a) 부터 (d) 까지의 각 부분에 대해, 유연한 통계적 학습 기법의 성능이 유연하지 않은 기법보다 일반적으로 더 좋을지 나쁠지 명시하십시오. 당신의 답변을 정당화하십시오.
   - (a) The sample size $n$ is extremely large, and the number of predictors $p$ is small.
   - (a) 표본 크기 $n$ 이 매우 크고, 예측변수들의 개수 $p$ 가 작은 경우.
   - (b) The number of predictors $p$ is extremely large, and the number of observations $n$ is small.
   - (b) 예측변수들의 개수 $p$ 가 매우 크고, 관측치들의 개수 $n$ 이 작은 경우.
   - (c) The relationship between the predictors and response is highly non-linear.
   - (c) 예측변수들과 반응변수 간의 관계가 고도로 비선형적인 경우.
   - (d) The variance of the error terms, i.e. $\sigma^2 = \text{Var}(\epsilon)$, is extremely high.
   - (d) 오차 항들의 분산, 즉 $\sigma^2 = \text{Var}(\epsilon)$ 이 매우 높은 경우.

2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide $n$ and $p$.

2. 각 시나리오가 분류 문제인지 회귀 문제인지 설명하고, 우리가 추론과 예측 중 어느 것에 가장 관심 있는지 명시하십시오. 마지막으로 $n$ 과 $p$ 를 제공하십시오.
   - (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.
   - (a) 우리는 미국의 상위 500개 기업들에 관한 하나의 데이터 세트를 수집합니다. 각 기업별로 우리는 이윤, 직원 수, 산업 그리고 CEO 급여를 기록합니다. 우리는 어느 요인들이 CEO 급여에 영향을 미치는지 이해하기에 관심이 있습니다.
   - (b) We are considering launching a new product and wish to know whether it will be a _success_ or a _failure_. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.
   - (b) 우리는 하나의 새로운 상품 론칭을 고려 중이며 이것이 _성공_ 일지 _실패_ 일지 알기를 희망합니다. 우리는 이전에 출시되었던 20개의 유사 상품들에 대한 데이터를 수집합니다. 각각의 제품에 대하여 우리는 그것이 성공인지 혹은 실패였는지, 해당 제품에 부과된 가격, 마케팅 예산, 경쟁사 가격, 그리고 기타 열 개의 변수들을 기록했습니다.
   - (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.
   - (c) 우리는 세계 주식 시장들 안의 주간 변동률과 연관하여 USD/Euro 환율의 % 변동을 예측하는 것에 관심이 있습니다. 그리하여 우리는 2012년 한 해의 주간 데이터를 수집합니다. 매 주마다 우리는 USD/Euro 환율의 % 변동, 미국 시장의 % 변동, 영국 시장의 % 변동, 그리고 독일 시장의 % 변동을 기록합니다.

3. We now revisit the bias-variance decomposition.

3. 우리는 이제 편향-분산 분해를 조명합니다.
   - (a) Provide a sketch of typical (squared) bias, variance, training error, test error, and Bayes (or irreducible) error curves, on a single plot, as we go from less flexible statistical learning methods towards more flexible approaches. The $x$-axis should represent the amount of flexibility in the method, and the $y$-axis should represent the values for each curve. There should be five curves. Make sure to label each one.
   - (a) 우리가 덜 유연한 통계적 학습 기법들에서 더욱 유연한 기법들로 나아갈 때의, 전형적인 (제곱된) 편향, 분산, 훈련 오차, 테스트 오차, 그리고 베이즈(혹은 피할 수 없는) 오차 곡선들의 스케치를 하나의 단일 플롯 위에 보여주십시오. 그 $x$-축은 방법 안의 유연성의 양을 나타내어야 하며, 그리고 $y$-축은 각 곡선들을 위한 값을 나타내어야 합니다. 거기에는 다섯 개의 곡선들이 있어야 합니다. 각 곡선에 라벨을 확인하여 붙이십시오.
   - (b) Explain why each of the five curves has the shape displayed in part (a).
   - (b) 왜 그 다섯 개 곡선들 각각이 (a) 부분에서 보여진 형상들을 가지는지 설명하십시오.

4. You will now think of some real-life applications for statistical learning.

4. 당신은 이제 통계적 학습을 위한 실생활 응용 분야들을 생각할 것입니다.
   - (a) Describe three real-life applications in which _classification_ might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.
   - (a) _분류_ 가 유용할지 모를 세 가지 실생활 응용 분야를 기술하십시오. 예측변수뿐만 아니라, 반응변수 역시 기술하십시오. 각 활용의 목표가 추론입니까 아니면 예측입니까? 당신의 답변을 설명하십시오.
   - (b) Describe three real-life applications in which _regression_ might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.
   - (b) _회귀_ 가 유용할지 모를 세 가지 실생활 응용 분야를 기술하십시오. 예측변수뿐만 아니라, 반응변수 역시 기술하십시오. 각 응용 분야의 목표가 추론입니까 아니면 예측입니까? 당신의 답변을 설명하십시오.
   - (c) Describe three real-life applications in which _cluster analysis_ might be useful.
   - (c) _군집 분석_ 이 유용할지 모를 세 가지 실생활 응용 분야를 기술하십시오.

5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

5. 회귀나 분류를 위한 매우 유연한 (덜 유연한 것에 비하여) 접근 방식의 이점들과 단점들은 무엇입니까? 어떤 환경 아래에서 더 유연한 접근 방식이 덜 유연한 접근 방식보다 선호될 수 있을까요? 언제 덜 유연한 접근 방식이 선호될 수 있을까요?

6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are its disadvantages?

6. 모수 및 비모수 통계적 학습 접근 방식들 간의 차이들을 기술하십시오. 회귀나 분류에 대한 (비모수 접근 방식과 반대되는) 모수 접근 방식의 이점들은 무엇입니까? 그것의 단점들은 무엇입니까?

7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

7. 아래의 표는 여섯 개의 관측치들, 세 개의 예측변수들, 그리고 하나의 질적 반응변수를 포함하는 훈련 데이터 세트를 제공합니다.

| Obs. | $X_1$ | $X_2$ | $X_3$ | $Y$ |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 3 | 0 | Red |
| 2 | 2 | 0 | 0 | Red |
| 3 | 0 | 1 | 3 | Red |
| 4 | 0 | 1 | 2 | Green |
| 5 | $-1$ | 0 | 1 | Green |
| 6 | 1 | 1 | 1 | Red |

Suppose we wish to use this data set to make a prediction for $Y$ when $X_1 = X_2 = X_3 = 0$ using $K$-nearest neighbors.

우리가 $K$-최근접 이웃들을 사용하여 $X_1 = X_2 = X_3 = 0$ 일 때 $Y$ 에 대한 예측을 생성하기 위해 이 데이터 세트를 사용하기를 원한다고 가정해 봅시다.

- (a) Compute the Euclidean distance between each observation and the test point, $X_1 = X_2 = X_3 = 0$.
- (a) 각 관측치와 테스트 포인트 $X_1 = X_2 = X_3 = 0$ 간의 유클리드 거리를 계산하십시오.
- (b) What is our prediction with $K = 1$? Why?
- (b) $K = 1$ 일 때 우리의 예측은 무엇입니까? 왜 그렇습니까?

- (c) What is our prediction with $K = 3$? Why?
- (c) $K = 3$ 일 때 우리의 예측은 무엇입니까? 왜 그렇습니까?
- (d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the _best_ value for $K$ to be large or small? Why?
- (d) 만약 이 문제의 베이즈 결정 경계가 고도로 비선형적이라면, 우리는 $K$ 를 위한 _가장 좋은_ 값이 클 것이라 생각합니까 작을 것이라 생각합니까? 왜 그렇습니까?

## _Applied_

## _응용적 문제_

8. This exercise relates to the `College` data set, which can be found in the file `College.csv` on the book website. It contains a number of variables for 777 different universities and colleges in the US. The variables are 

8. 이 연습문제는 책 웹사이트 안의 `College.csv` 파일에서 찾을 수 있는 `College` 데이터 세트와 관련됩니다. 그것은 미국의 777개 대학들에 대한 여러 변수들을 포함합니다. 변수들은 다음과 같습니다: 

   - `Private` : Public/private indicator
   - `Private` : 국공립 / 사립 지시자

   - `Apps` : Number of applications received
   - `Apps` : 접수된 지원서들의 개수

   - `Accept` : Number of applicants accepted
   - `Accept` : 합격된 지원자들의 개수

   - `Enroll` : Number of new students enrolled
   - `Enroll` : 등록된 신입생들의 개수

   - `Top10perc` : New students from top 10 % of high school class
   - `Top10perc` : 고등학교 상위 10% 출신의 신입생들

   - `Top25perc` : New students from top 25 % of high school class
   - `Top25perc` : 고등학교 상위 25% 출신의 신입생들

   - `F.Undergrad` : Number of full-time undergraduates
   - `F.Undergrad` : 규정 시간(full-time) 학부생들의 개수

   - `P.Undergrad` : Number of part-time undergraduates
   - `P.Undergrad` : 시간제(part-time) 학부생들의 개수

   - `Outstate` : Out-of-state tuition
   - `Outstate` : 타주 출신 학생의 수업료

   - `Room.Board` : Room and board costs
   - `Room.Board` : 기숙사비 및 식비

   - `Books` : Estimated book costs
   - `Books` : 추정 도서 비용

   - `Personal` : Estimated personal spending
   - `Personal` : 추정 개인 경비

   - `PhD` : Percent of faculty with Ph.D.s
   - `PhD` : Ph.D. 학위를 가진 교수진의 퍼센트

   - `Terminal` : Percent of faculty with terminal degree
   - `Terminal` : 최종 학위를 가진 교수진의 퍼센트

   - `S.F.Ratio` : Student/faculty ratio
   - `S.F.Ratio` : 학생/교수 비율

   - `perc.alumni` : Percent of alumni who donate
   - `perc.alumni` : 기부하는 동문의 퍼센트

   - `Expend` : Instructional expenditure per student
   - `Expend` : 학생 1인당 교육 지출

   - `Grad.Rate` : Graduation rate
   - `Grad.Rate` : 졸업률

Before reading the data into `Python`, it can be viewed in Excel or a text editor.

데이터를 `Python` 으로 읽어 들이기 전에, 그것은 엑셀이나 텍스트 에디터 안에서 보아질 수 있습니다.

- (a) Use the `pd.read_csv()` function to read the data into `Python`. Call the loaded data `college`. Make sure that you have the directory set to the correct location for the data.
- (a) 데이터를 `Python` 으로 읽어 들이기 위해 `pd.read_csv()` 함수를 사용하십시오. 적재된 데이터를 `college` 라 부르십시오. 당신이 데이터를 위해 그 디렉터리를 정확한 위치로 설정해 두었음을 확인하십시오.
- (b) Look at the data used in the notebook by creating and running a new cell with just the code `college` in it. You should notice that the first column is just the name of each university in a column named something like `Unnamed: 0`. We don’t really want `pandas` to treat this as data. However, it may be handy to have these names for later. Try the following commands and similarly look at the resulting data frames:
- (b) 오직 코드 `college` 한 줄만 들어 있는 새로운 셀 하나를 생성하고 실행함을 통하여 노트북에 사용된 해당 데이터를 살펴보십시오. 여러분은 첫 번째 열이 단지 `Unnamed: 0` 등과 같이 명명된 열들 내부의 각 대학 이름이라는 것을 알아야 합니다. 우리는 `pandas` 가 이것을 데이터로 취급하기를 진짜로 원하지 않습니다. 하지만, 추후를 위하여 이 이름들을 가지는 것은 유용할 수 있습니다. 다음의 명령을 시도해 보고 유사하게 결과 데이터 프레임들을 살펴보십시오:

```python
college2 = pd.read_csv('College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college3.set_index('College')
```

This has used the first column in the file as an `index` for the data frame. This means that `pandas` has given each row a name corresponding to the appropriate university. Now you should see that the first data column is `Private`. Note that the names of the colleges appear on the left of the table. We also introduced a new python object above: a _dictionary_, which is specified by `(key, value)` pairs. Keep your modified version of the data with the following:

이것은 데이터 프레임을 위한 인덱스로서 그 파일 안의 첫 번째 열을 사용했습니다. 이것은 `pandas` 가 각각의 행에 적절한 대학에 대응하는 이름을 주었음을 의미합니다. 여러분은 이제 첫 번째 데이터 열이 `Private` 임을 보아야 합니다. 그 대학교 이름들이 표의 왼쪽에 나타난 것에 주목하십시오. 우리는 또한 위에서 새로운 파이썬 객체를 하나 소개했습니다: 그것은 `(key, value)` 쌍들에 의해 표기되는 특정 _딕셔너리(dictionary)_ 입니다. 다음의 것들과 함께 여러분의 수정된 버전의 데이터를 유지하십시오:

```python
college = college3
```

- (c) Use the `describe()` method to produce a numerical summary of the variables in the data set.
- (c) 데이터 세트 안의 변수들의 수치적인 요약을 생성하기 위해 `describe()` 메서드를 사용하십시오.

- (d) Use the `pd.plotting.scatter_matrix()` function to produce a scatterplot matrix of the first columns `[Top10perc, Apps, Enroll]`. Recall that you can reference a list `C` of columns of a data frame `A` using `A[C]`.
- (d) 첫 번째 열들인 `[Top10perc, Apps, Enroll]` 의 산점도 매트릭스를 생성하기 위해 `pd.plotting.scatter_matrix()` 함수를 사용하십시오. 당신이 `A[C]` 를 사용하여 데이터 프레임 `A` 의 열들의 리스트 `C` 를 참조할 수 있음을 기억하십시오.

- (e) Use the `boxplot()` method of `college` to produce side-by-side boxplots of `Outstate` versus `Private`.
- (e) `Private` 에 대한 `Outstate` 의 병렬형 박스 플롯을 생성하기 위해 `college` 의 `boxplot()` 메서드를 사용하십시오.

- (f) Create a new qualitative variable, called `Elite`, by _binning_ the `Top10perc` variable into two groups based on whether or not the proportion of students coming from the top 10% of their high school classes exceeds 50%.
- (f) 출신 학생들이 고등학교 학급의 상위 10% 과반수인 50% 를 초과하는지 여부에 기반하여 `Top10perc` 변수를 두 개의 그룹으로 분할함으로써 `Elite` 라 불리는 새로운 질적 변수를 생성하십시오.

```python
college['Elite'] = pd.cut(college['Top10perc'],
                          [0, 50, 100],
                          labels=['No', 'Yes'])
```
*(Note: the threshold logic typically uses 50 for the 50% marker, since Top10perc stores values up to 100 rather than ratios up to 1, adjust as necessary per dataset).*

  Use the `value_counts()` method of `college['Elite']` to see how many elite universities there are. Finally, use the `boxplot()` method again to produce side-by-side boxplots of `Outstate` versus `Elite`.
  얼마나 많은 엘리트 대학교들이 있는지 보기 위해 `college['Elite']` 의 `value_counts()` 메서드를 사용하십시오. 마지막으로, `Elite` 에 대한 `Outstate` 의 병렬형 박스 플롯을 생성하기 위해 `boxplot()` 메서드를 다시 사용하십시오.

- (g) Use the `plot.hist()` method of `college` to produce some histograms with differing numbers of bins for a few of the quantitative variables. The command `plt.subplots(2, 2)` may be useful: it will divide the plot window into four regions so that four plots can be made simultaneously. By changing the arguments you can divide the screen up in other combinations.
- (g) 약간의 양적 변수들을 위해 상이한 수의 빈(bin)을 가진 몇몇의 히스토그램들을 생성하기 위해 `college` 의 `plot.hist()` 메서드를 사용하십시오. 명령 `plt.subplots(2, 2)` 는 유용할 수 있습니다: 그것은 4개의 플롯들이 동시에 만들어질 수 있도록 플롯 창을 4개의 영역들로 분할합니다. 그 인수들을 변경함으로써 여러분은 다른 조합들로 화면을 분할할 수 있습니다.

- (h) Continue exploring the data, and provide a brief summary of what you discover.
- (h) 데이터 탐색을 계속하십시오, 그리고 당신이 발견한 것의 간략한 요약을 제공하십시오.

9. This exercise involves the `Auto` data set studied in the lab. Make sure that the missing values have been removed from the data.

9. 이 연습문제는 실습에서 연구된 `Auto` 데이터를 수반합니다. 누락된 값들이 그 데이터로부터 지워졌음을 확실시 하십시오.

   - (a) Which of the predictors are quantitative, and which are qualitative?
   - (a) 예측 변수들 중 어느 것이 양적입니까, 그리고 어느 것이 질적입니까?
   - (b) What is the _range_ of each quantitative predictor? You can answer this using the `min()` and `max()` methods in `numpy`.
   - (b) 각각의 양적 예측 변수의 _범위(range)_ 는 무엇입니까? 당신은 `numpy` 의 `min()` 과 `max()` 메서드들을 사용하여 이것에 답변할 수 있습니다.
   - (c) What is the mean and standard deviation of each quantitative predictor?
   - (c) 각 양적 예측 변수의 평균과 표준 편차는 무엇입니까?

   - (d) Now remove the 10th through 85th observations. What is the range, mean, and standard deviation of each predictor in the subset of the data that remains?
   - (d) 이제 10 번째에서 85 번째의 관측치들을 지우십시오. 남은 데이터의 부분집합 안의 각 예측 변수들의 범위, 평균, 그리고 표준 편차는 무엇입니까?
   - (e) Using the full data set, investigate the predictors graphically, using scatterplots or other tools of your choice. Create some plots highlighting the relationships among the predictors. Comment on your findings.
   - (e) 산점도들 혹은 여러분이 선택한 기타 도구들을 사용하여 전체 데이터 세트를 그래픽적으로 조사하십시오. 예측 변수들 상호 간의 관계들을 강조하는 몇몇 플롯들을 만드십시오. 발견한 결과에 논평하십시오.
   - (f) Suppose that we wish to predict gas mileage (`mpg`) on the basis of the other variables. Do your plots suggest that any of the other variables might be useful in predicting `mpg`? Justify your answer.
   - (f) 우리가 여타의 변수들을 바탕으로 가스 주행거리(`mpg`) 를 예측하기 바란다고 가정해 봅시다. 여러분의 플롯들은 다른 변수들 중 어느 것이라도 `mpg` 를 예측하는 것에 유용할지도 모른다고 제안합니까? 당신의 대답을 정당화 하십시오.

10. This exercise involves the `Boston` housing data set.

10. 이 연습문제는 `Boston` 주택 데이터 세트를 포함합니다.
    - (a) To begin, load in the `Boston` data set, which is part of the `ISLP` library.
    - (a) 시작을 위해, `ISLP` 라이브러리의 일부인 `Boston` 데이터 세트를 로드하십시오.
    - (b) How many rows are in this data set? How many columns? What do the rows and columns represent?
    - (b) 이 데이터 세트에는 몇 개의 행들이 있습니까? 몇 개의 열들이 있습니까? 행들과 열들은 무엇을 나타냅니까?
    - (c) Make some pairwise scatterplots of the predictors (columns) in this data set. Describe your findings.
    - (c) 이 데이터 안의 예측 변수들(열들) 의 한쌍형 산점도들을 일부 만드십시오. 발견한 결과를 기술하십시오.
    - (d) Are any of the predictors associated with per capita crime rate? If so, explain the relationship.
    - (d) 어떠한 예측 변수라도 1인당 범죄율과 연관됩니까? 만약 그렇다면, 역학 관계를 설명하십시오.
    - (e) Do any of the suburbs of Boston appear to have particularly high crime rates? Tax rates? Pupil-teacher ratios? Comment on the range of each predictor.
    - (e) 보스턴의 교외들 중 어떤 곳은 특별히 높은 범죄율을 가진 것으로 나타납니까? 혹은 세금 이율을? 학생-강사 비율을? 지정 각 예측 변수의 범위에 대하여 논평하십시오.
    - (f) How many of the suburbs in this data set bound the Charles river?
    - (f) 이 데이터 세트의 교외들 중 얼마나 많은 것들이 찰스 강(Charles river)에 접해 있습니까?
    - (g) What is the median pupil-teacher ratio among the towns in this data set?
    - (g) 이 데이터 세트에 속한 타운들 간에 중앙값 학생-강사 비율은 무엇입니까?
    - (h) Which suburb of Boston has lowest median value of owneroccupied homes? What are the values of the other predictors for that suburb, and how do those values compare to the overall ranges for those predictors? Comment on your findings.
    - (h) 어느 보스턴 교외가 소유자-거주 주택의 가장 낮은 중앙값을 갖습니까? 그 교외를 위한 다른 예측 변수들의 값은 무엇이며, 그러한 값들은 해당 예측 변수들을 위한 전체 범위들과 비교하여 어떤가요? 발견한 결과들에 대해 논평하십시오.
    - (i) In this data set, how many of the suburbs average more than seven rooms per dwelling? More than eight rooms per dwelling? Comment on the suburbs that average more than eight rooms per dwelling.
    - (i) 이 데이터 세트 안에서 주거당 평균 구역 일곱 개보다 더 많은 평균 방들을 가지는 교외 지역이 몇 개나 있습니까? 여덟 개의 방들 보다 더 큽니까? 거주지 주택 당 평균 여덟 실 이상을 가지는 타운 요소 교외 지역들에 대해 논평하십시오.