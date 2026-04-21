---
layout: default
title: "trans1"
---

# `ax.set_ylim([50000, 250000]);`

Notice the expression `None` in `Y[:, None]` above. This adds an axis (dimension) to the one-dimensional array `Y` , which allows it to be recycled when subtracted from the two-dimensional `Yhat_in` .
방금 사용했던 앞선 코드 수식 `Y[:, None]` 내부에 기재된 `None` 키워드 표현식을 눈여겨보십시오. 이 조작은 1차원 형태 배열에 불과했던 기존 `Y` 객체에 새로운 결합 축(차원, dimension) 하나를 몰래 끼워 추가해 주는 역할을 수행하며, 이로 인해 우리는 2차원 매트릭스 형태인 `Yhat_in` 배열에서 수치 감산을 연산할 때 오류 없이 차원 재활용 연산이 가능해지게 됩니다.

We are now ready to use cross-validation to estimate test error along the model path. We must use _only the training observations_ to perform all aspects of model-fitting — including variable selection. Therefore, the determination of which model of a given size is best must be made using _only the training observations_ in each training fold. This point is subtle but important. If the full data set is used to select the best subset at each step, then the validation set errors and cross-validation errors that we obtain will not be accurate estimates of the test error.
자, 이제 우리는 앞선 전진 선택 모델 궤도를 훑고 지나가며 테스트 단면의 오차 예측을 연산해 내기 위해 십자 교차 검증(cross-validation) 기법을 들이댈 준비가 되었습니다. 여기서 대전제가 하나 있습니다. 우리는 변수 선택(variable selection) 과정마저 포함한 모든 모형 적합 단계 절차의 모든 측면을 반드시 _오직 훈련된 독립 관측치들로만(only the training observations)_ 단독 수행해야 한다는 점입니다. 따라서 특정 크기로 주어진 한계 모델 중 도대체 어떤 녀석이 가장 최고 실적의 모델인지 평가 결정을 내리는 일도 오로지 각 독립 훈련 폴드(training fold) 단계 내부에 갇힌 _순수 훈련용 종속 관측치들만을 이용해_ 평가 내려져야만 합니다. 이 주의사항은 미묘해 보이지만 굉장히 중요합니다. 만약 전체 투입 데이터 세트 묶음 그 자체가 오염되어, 각 선택별 단계에서 최고의 독립 부분집합을 뽑아내는 과정에 슬쩍 투입 쓰였다면, 그렇게 도출해 얻은 검증용 세트 차원의 오차율 결과나 십자 교차 검증 오차율 점수 지표들 따위는 실전 테스트 단 오차를 예측해 내는 무결한 정확 신뢰 통계 지표가 되지 못할 것입니다.

We now compute the cross-validated predicted values using 5-fold crossvalidation.
그러므로 우리는 엄격하게 5-겹(5-fold) 교차 검사 절차를 통해 연산 도출된 순수 교차-예측 결괏값 도출 연산을 지금 수행하겠습니다.

```python
In [14]: K = 5
kfold = skm.KFold(K,
                  random_state=0,
                  shuffle=True)
Yhat_cv = skm.cross_val_predict(full_path,
                                Hitters,
                                Y,
                                cv=kfold)
Yhat_cv.shape
```

```
Out[14]: (263, 20)
```

The prediction matrix `Yhat_cv` is the same shape as `Yhat_in` ; the difference is that the predictions in each row, corresponding to a particular sample index, were made from models fit on a training fold that did not include that row.
예측치 배열 매트릭스 `Yhat_cv`는 모델 궤적 결괏값인 `Yhat_in`의 형상(shape)과 완전히 동일합니다 ; 그러나 이 둘의 핵심적 차이는 이 배열의 각 특정 행렬 단면(row), 즉 특정 샘플 인덱스 좌표에 대치 상응하는 예측 결과치 결괏값들의 경우, 절대적으로 그 해당 연산 표본 행을 배합 포함하지 않은 채 오직 훈련(training) 독립 폴드(fold)에만 맞춰 따로 적합 구축 파생된 모델들을 이용해서 뱉어낸 순수 별개 결괏값이라는 사실입니다.

At each model along the path, we compute the $\text{MSE}$ in each of the crossvalidation folds. These we will average to get the mean MSE, and can also use the individual values to compute a crude estimate of the standard error of the mean.[^9] Hence we must know the test indices for each cross-validation split. This can be found by using the `split()` method of `kfold`. Because we fixed the random state above, whenever we split any array with the same number of rows as Y we recover the same training and test indices, though we simply ignore the training indices below.
우리는 이 도출 궤도를 통과하는 각 단계 모델들에서 각자의 교차 검증 폴드 단 $\text{MSE}$를 도출 일일 계산합니다. 우리는 이 개별 평가 점수 결괏값을 평균으로 통계 수합해 '평균 통계 MSE' 수치를 무사히 얻어낼 것이며, 또한 이렇게 쌓인 각각의 개별 연산 결괏값을 '평균 수치의 표준 오차'를 미루어 예측 짐작하는 다소 거친 방식의 추론[9]에 써먹을 수도 있습니다. 따라서, 우린 이 모든 과정 세팅을 위해 반드시 각각의 교차-검토 분할(cross-validation split)에 할당 맵핑될 테스트 묶음 인덱스 위치를 알아야만 합니다. 이는 조금 전 써먹었던 저 파이썬 내장 `kfold` 객체의 강력한 `split()` 메서드를 구동 사용하면 가볍게 찾아 나눌 수 있습니다. 위 연산 구역에서 난수 발생 스드(random state) 값을 의도적으로 0으로 고정해 두었으므로, Y 변수 매트릭스와 동일한 열 길이 크기를 가진 배열을 쪼개 돌릴 때마다 항상 늘 정확히 동일한 훈련 및 테스트 인덱스 위치 좌표를 일관 복구(recover) 반복 도출하게 됩니다 (물론 여기서 우린 기껏 얻은 훈련 인덱스 좌표 번호 배열은 아래 코드에서 그냥 편히 버려 무시하겠지만 말입니다).

[^9]: The estimate is crude because the five error estimates are based on overlapping training sets, and hence are not independent.
[^9]: 5개의 에러 오차 추정치 통계 단면이 상호 중복되어 겹쳐진 훈련용 세트 기반 하에 산출 기반되었으므로 이 추정 연산 방식은 결코 상호 완전 독립적이지 않으며, 그로 인해 본 추산치 평가 방식은 거친 측면이 있습니다.

We now add the cross-validation error estimates to our $\text{MSE}$ plot. We include the mean error across the five folds, and the estimate of the standard error of the mean.
이제 우리는 갓 얻어낸 이 십자 교차 분할 검증용 오류 추정치 그래프 도표를 앞선 표본 도출 $\text{MSE}$ 차트 데이터 라인에 당당히 덧그려 포갭니다. 이렇게 갱신된 그래프엔 5개의 개별 폴드를 가로지르는 평균 전체 오차율 추정선과 평균 분포상 추산 표준 오차 수치 곡선 범위 또한 한데 포함될 것입니다.

```python
In [15]: cv_mse = []
for train_idx, test_idx in kfold.split(Y):
    errors = (Yhat_cv[test_idx] - Y[test_idx, None])**2
    cv_mse.append(errors.mean(0)) # column means
cv_mse = np.array(cv_mse).T
cv_mse.shape
```

```
Out[15]: (20, 5)
```

```python
In [16]: ax.errorbar(np.arange(n_steps),
                     cv_mse.mean(1),
                     cv_mse.std(1) / np.sqrt(K),
                     label='Cross-validated',
                     c='r') # color red
ax.set_ylim([50000, 250000])
ax.legend()
mse_fig
```

To repeat the above using the validation set approach, we simply change our `cv` argument to a validation set: one random split of the data into a test and training. We choose a test size of 20%, similar to the size of each test set in 5-fold cross-validation.
검증 세트 접근법 규칙 잣대를 대입 응용하여 이 과정을 수식 반복하기 위해, 우리는 그저 기존 사용된 `cv` 파라미터 매개 변수를, 검증 세트 환경 (단 한 번, 데이터를 훈련 세트와 시험 세트로 기립 무작위 분할하는 작업 처리) 모델 구조로 똑 잘라 바꿔 교체만 해주면 됩니다. 한 번의 지정에서 저희는 5-폴드 교차 세팅 평가 구조 검증 환경에 속해 있는 각 개별 분할 테스트 블록 세트 객체의 규격 사이즈와 똑같이 아주 흡사하게 통일 대응토록, 지정 테스트 세트 크기를 20% 규격으로 단일 채택 고정하겠습니다.

```python
In [17]: validation = skm.ShuffleSplit(n_splits=1,
                                       test_size=0.2,
                                       random_state=0)
for train_idx, test_idx in validation.split(Y):
    full_path.fit(Hitters.iloc[train_idx],
                  Y[train_idx])
    Yhat_val = full_path.predict(Hitters.iloc[test_idx])
    errors = (Yhat_val - Y[test_idx, None])**2
    validation_mse = errors.mean(0)
```

As for the in-sample $\text{MSE}$ case, the validation set approach does not provide standard errors.
앞선 표본 내 오류 $\text{MSE}$ 산출 경우 사례와 동일 무사하게, 이처럼 외부 별도 단일 검증 진단 세트 무대를 이용한 접근 계산 연산법 방식에서는 딱히 별도의 계산 결괏값 표준 오차(standard errors) 추산 정보 자체를 제공하지 않습니다.

```python
In [18]: ax.plot(np.arange(n_steps),
                 validation_mse,
                 'b--', # color blue, broken line
                 label='Validation')
ax.set_xticks(np.arange(n_steps)[::2])
ax.set_ylim([50000, 250000])
ax.legend()
mse_fig
```

## Best Subset Selection
## 최적 부분집합 탐색 자동 선택 (Best Subset Selection)

Forward stepwise is a _greedy_ selection procedure; at each step it augments the current set by including one additional variable. We now apply best subset selection to the `Hitters` data, which for every subset size, searches for the best set of predictors.
조금 전 써먹은 전진식 단계 예측 선택법은 아주 탐욕적(greedy) 알고리즘 성향 절차입니다 ; 매 작동 스텝마다 기존 데이터 세트 뭉치에 단 하나의 한 가지 변수식을 더 우겨 결합 포함시켜서 모델을 점점 거대하게 증강시켜버립니다. 우리는 이제 이에 반발 대응해 `Hitters` 데이터셋 실험 무대에 이른바 '최적 부분집합 선택법(best subset selection)'을 시도 적용 가동해 보겠습니다. 이 방식은 구획된 모든 한계 부분 집합 사이즈 한도 내에서 가장 최상의 예측 적합 변수 무리 세트 조합만을 핀셋으로 탐색 선별해 냅니다.

We will use a package called `l0bnb` to perform best subset selection. Instead of constraining the subset to be a given size, this package produces a path of solutions using the subset size as a penalty rather than a constraint. Although the distinction is subtle, the difference comes when we crossvalidate.
이 훌륭한 최선 부분 객체 선별 절차를 무사 완수하기 위해 저희는 외부에서 `l0bnb`라고 불리는 호출 패키지 모듈을 수입해 응용 접목 사용할 것입니다. 무작정 부분 분할 집합 세트의 사이즈 한계 크기를 억지로 제약 고정시켜 지정 부여하는 일반적 무식한 방식 대신, 이 훌륭한 구조 패키지 객체 모듈은 평가 도출될 부분 분할 집합 체계 사이즈 수치를 단순 '강제 한도 제약(constraint)' 기법보단 성과 점수에 감점 벌금을 부여해 찍어누르는 일종의 '패널티(penalty) 보상 장치'로 모델 평가 점수에 활용하여 정답 판별 모델 결괏값이 진행되는 일련의 이행 궤적 패스 결괏값을 무사 생성해 파생 산출해 줍니다. 이 차이 조건은 무척 미묘하지만, 우리가 이 결과 모델의 단계를 교차검열(crossvalidate)할 때만큼은 비로소 그 결정적 차이가 확연히 벌어지며 드러나게 됩니다.

```python
In [19]: D = design.fit_transform(Hitters)
D = D.drop('intercept', axis=1)
X = np.asarray(D)
```

Here we excluded the first column corresponding to the intercept, as `l0bnb` will fit the intercept separately. We can find a path using the `fit_path()` function.
여기서 저희는 편향 상숫값 기점인 절편(intercept)에 상응하며 대응하는 1번 첫 번째 열 기둥 세로열을 데이터 프레임 체계에서 강제 삭제 배제시켜 도출했습니다. 이는 `l0bnb` 패키지 모듈 함수가 그 자신의 평가 적합 절차 수행 시, 절편 위치는 독자 모의 무대에서 따로 계산 적합시키며 챙길 기능이 내장되어 있기 때문입니다. 이제 준비가 끝났으니 우린 아주 무난히 파생 함수인 `fit_path()` 명령 모듈 객체를 응용 호출함으로써 이 모델의 변화 궤적 패스를 가동해 도출해 낼 수 있습니다.

```python
In [20]: path = fit_path(X,
                         Y,
                         max_nonzeros=X.shape[1])
```

The function `fit_path()` returns a list whose values include the fitted coefficients as `B` , an intercept as `B0` , as well as a few other attributes related to the particular path algorithm used. Such details are beyond the scope of this book.
이 훌륭 연산 패키지 함수인 `fit_path()` 모듈 툴은 그저 단순히 배열이 아니라, 일종의 리스트 묶음 세트를 산출 결과값으로 반환 복귀시킵니다. 그리고 이 무단 도출된 종합 세트 결괏값 안에는 `B`라는 꼬리표 키값 명찰을 달고 도출된 최종 모델의 모델 적합 계수 값 산출치들과 함께, `B0`라고 딱지가 붙어 파생된 모델 절편 계산 수치 정보, 그리고 나아가 조금 더 추가된 특정 연산 파생 모델 알고리즘 작동 궤도 계산식에 결부 연관된 알 수 없는 몇몇 특성 데이터 조각 단면들이 속해 산출되어 기재 포트폴리오로 나옵니다. 덧붙여 그러한 내부 연산 작동 부속품들의 세세한 논리 사항 이치들을 꿰뚫어 해석하는 작업은 이 통계 예측 기법 책이 다루고자 했던 교육 과정 기본 소화 범주(scope) 영역을 벗어나므로 과감히 무시하셔도 됩니다.

```python
In [21]: path[3]
```

```python
Out[21]: {'B': array([0., 3.254844, 0., 0., 0.,
                      0., 0., 0., 0., 0.,
                      0., 0.677753, 0., 0., 0.,
                      0., 0., 0., 0.]),
 'B0': -38.98216739555494,
 'lambda_0': 0.011416248027450194,
 'M': 0.5829861733382011,
 'Time_exceeded': False}
```

In the example above, we see that at the fourth step in the path, we have two nonzero coefficients in `'B'` , corresponding to the value 0.114 for the penalty parameter `lambda_0` . We could make predictions using this sequence of fits on a validation set as a function of `lambda_0` , or with more work using cross-validation.
방금 출력된 위 실질 결과 아웃풋 실습 관측 예시 단락 무대를 통해, 모형 작동 궤도 경로의 네 번째 (4th step) 통과 단계 시점 컷 결과에서 산출 결괏값 `'B'` 배열 기호 안에 속한 총 스무 개의 예측 수치 요소 객체 중 오직 숫자 0이 아닌 유의미한 변수 객체 계수 생존 결과가 단 2개만 살아 도출 잔존해 있음을 확인할 수 있습니다. 그리고 이 결과 도출 상태는 평가 점수를 찍어 누를 당시 투입 적용된 모의 패널티 통제 파라미터 매개 변수 `lambda_0`의 0.114 수치 값에 정확히 대응 반응해 나타난 결과치 파생 현상입니다. 우리는 도출된 이 파라미터 함수 척도 `lambda_0` 변수를 기준 통제 함수 잣대로 삼아 단일 검증 진단 데이터 세트 모의 무대 위에서 이 기가 막히게 적합된 회귀 계수들의 연결고리 순환 과정 궤도를 이용 예측 도출을 연산 단행할 수 있으며, 더 나아가 여기에 수고를 약간 더 가미하고 교차-진동 검수 점검 기법인 교차 검증을 응용 동원함으로써 한층 고도화된 정답 예측 결과를 시도 산출 도출 얻어낼 수도 있을 것입니다.
