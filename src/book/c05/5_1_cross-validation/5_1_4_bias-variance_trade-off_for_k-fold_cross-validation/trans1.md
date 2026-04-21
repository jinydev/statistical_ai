---
layout: default
title: "trans1"
---

# _5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation_ 
# _5.1.4 k-폴드 교차 검증을 위한 편향-분산 트레이드오프_

We mentioned in Section 5.1.3 that _k_ -fold CV with _k < n_ has a computational advantage to LOOCV.
우리는 앞선 5.1.3 절에서 _k < n_ 조건을 지닌 _k_ -폴드 CV가 LOOCV에 대비해 무척 강력한 연산적 이점을 갖는다고 언급한 바 있다.

But putting computational issues aside, a less obvious but potentially more important advantage of _k_ -fold CV is that it often gives more accurate estimates of the test error rate than does LOOCV.
하지만 이러한 연산 비용 이슈를 잠시 제쳐둔다 하더라도, 비록 겉으로 덜 명백하게 보이지만 잠재적으로는 훨씬 더 중대할 수 있는 _k_ -폴드 CV의 이점은 바로 이것이 LOOCV가 해내는 것보다 오히려 테스트 오차율에 대해 더 정확한 추정치들을 종종 제공해 준다는 사실이다.

This has to do with a bias-variance trade-off. 
이것은 편향-분산 트레이드오프(bias-variance trade-off) 원리와 직결되어 있다.

It was mentioned in Section 5.1.1 that the validation set approach can lead to overestimates of the test error rate, since in this approach the training set used to fit the statistical learning method contains only half the observations of the entire data set.
이전 5.1.1 절에서는, 통계적 학습 방법에 적합시키는 데 쓰인 훈련 세트가 명백히 전체 데이터 세트 관측치의 절반 수준밖에 포함하지 못하기 때문에, 검증 세트 접근법이 테스트 오차율을 과대평가(overestimates) 하는 결과를 초래할 수 있다고 지적된 바 있다.

Using this logic, it is not hard to see that LOOCV will give approximately unbiased estimates of the test error, since each training set contains _n −_ 1 observations, which is almost as many as the number of observations in the full data set.
이러한 논리를 적용해 본다면, LOOCV 구동 시 각각의 거듭되는 훈련 세트가 전체 데이터 세트의 관측치 수량과 거의 맘먹는 무려 _n −_ 1 개의 관측치들을 꾸준히 포함하게 되므로, 필경 LOOCV가 시험 오차에 대해 대략적으로 편향이 벗겨진 무편향(unbiased) 추정치를 뱉어낼 것임을 알아차리기는 결코 어렵지 않다.

And performing _k_ -fold CV for, say, _k_ = 5 or _k_ = 10 will lead to an intermediate level of bias, since each training set contains approximately ( _k −_ 1) _n/k_ observations— fewer than in the LOOCV approach, but substantially more than in the validation set approach.
그리고 이어서, 가령 _k_ = 5 나 _k_ = 10 설정으로 _k_ -폴드 CV를 수행하게 된다면 이는 결과적으로 중간 수준 단계의 편향(bias) 수위를 낳게 되는데, 왜냐하면 이때 각 훈련 세트가 대략적으로 ( _k −_ 1) _n/k_ 개의 관측치—단연 LOOCV 체제보다는 적지만, 오히려 고전적인 검증 세트 접근법보다는 확연히 실질적으로 훨씬 더 많은 물량—를 포용하여 모기 때문이다.

Therefore, from the perspective of bias reduction, it is clear that LOOCV is to be preferred to _k_ -fold CV. 
그러므로, 전적인 편향 감소(bias reduction) 관점의 렌즈로만 바라본다면, 의심의 여지 없이 LOOCV가 _k_ -폴드 CV보다 더욱 선호되어야 마땅함이 분명하다.

However, we know that bias is not the only source for concern in an estimating procedure; we must also consider the procedure’s variance.
그러나, 임의의 추정 절차를 가동할 때 우리가 근심해야 할 유일무이한 출처가 비단 편향(bias) 하나뿐만은 결코 아니라는 점을 우리는 잘 알고 있다; 즉 우리는 통계 절차가 낳는 예측 분산(variance) 지표 역시 반드시 함께 숙고하고 고려해야만 하는 것이다.

It turns out that LOOCV has higher variance than does _k_ -fold CV with _k < n_ .
결과적으로 따져보면 흥미롭게도 LOOCV가 오히려 _k < n_ 조건의 _k_ -폴드 CV가 가지는 분산보다 한층 더 높은 고수위 분산을 나타낸다는 사실이 밝혀진다.

Why is this the case?
도대체 왜 이런 현상이 발생하는가?

When we perform LOOCV, we are in effect averaging the outputs of _n_ fitted models, each of which is trained on an almost identical set of observations; therefore, these outputs are highly (positively) correlated with each other.
우리가 LOOCV를 돌릴 때, 우리는 사실상 실질적으로 고스란히 _n_ 개의 적합된 모델 도출량들을 통째로 합산 평균 내는 작위를 하는 셈인데, 이 모델들 낱개 수량 각각은 거의 완벽에 가깝도록 판박이처럼 동일한 관측치 세트를 돌려받으면서 훈련에 임한 녀석들이다; 따라서, 이 모델들이 내뿜은 결괏값들은 상호 간에 지극히 강한 (양의) 상관관계(correlated) 로 결박되어 있을 수밖에 없다.

In contrast, when we perform _k_ -fold CV with _k < n_ , we are averaging the outputs of _k_ fitted models that are somewhat less correlated with each other, since the overlap between the training sets in each model is smaller.
대조적으로, 우리가 만약 _k < n_ 규격의 _k_ -폴드 CV를 가동하게 된다면, 훈련 세트들끼리의 상호 일치 중복(overlap)되는 파이 비중이 조금 더 작기 때문에, 상호 간에 이들 각 기기가 맺는 상관관계성 수위가 상대적으로 다소 느슨해진 덜한 _k_ 개 분량의 적합 모델 결괏값 도출물들을 우리가 평균 내게 됨을 뜻한다.

Since the mean of many highly correlated quantities has higher variance than does the mean of many quantities that are not as highly correlated, the test error estimate resulting from LOOCV tends to have higher variance than does the test error estimate resulting from _k_ -fold CV. 
서로 간 상관성이 유독 지독히도 높고 강하게 묶인 다수 양(quantities) 들의 평균값은 그렇지 않고 상관관계가 덜한 녀석들의 뭉친 평균값에 비해서 한결같이 더 높은 고공 분산을 띠는 경향이 필연 존재하므로, 기실 LOOCV로부터 도출 방출된 테스트 에러 추정치는 응당 _k_ -폴드 CV가 내뿜는 시험 오차 추정치가 감당할 수준보다 필시 더 높은 분산(higher variance) 변동성 요동 파장을 앓는 경향을 보일 수밖에 없다.

To summarize, there is a bias-variance trade-off associated with the choice of _k_ in _k_ -fold cross-validation.
전체적으로 요약 시사하자면, _k_ -폴드 교차 검증 국면에서 _k_ 라는 수치를 어떤 값으로 택하느냐 하는 제반 선택에는 필연 편향-분산 트레이드오프 딜레마가 숙명처럼 동전의 양면 수반되어 작동한다.

Typically, given these considerations, one performs _k_ -fold cross-validation using _k_ = 5 or _k_ = 10, as these values have been shown empirically to yield test error rate estimates that suffer neither from excessively high bias nor from very high variance. 
통상, 이러한 깊은 일련의 숙고 타진 여건 통찰을 모두 복합 고려해 볼 때 사람들은 주로 _k_ = 5 혹은 _k_ = 10 수식을 써서 _k_ -폴드 교차 검증을 전개 이행 수행하길 즐기는데, 그 이유는 다름 아닌 바로 저 5와 10이란 묘한 두 십 단위 수치가 그동안 지나치게 높지도 않은 적정 압도 편향치 그리고 너무 널뛰지 않는 고공 분산치 모두로부터 괴롭힘을 덜 받으면서 가장 영리하게 살아남는 황금 비율의 실전 예측 에러 시험 오차 추정치들을 낳는다고 지난 과거 실증적인 현장 경험 측면에서 증명되어왔기 때문이다.
