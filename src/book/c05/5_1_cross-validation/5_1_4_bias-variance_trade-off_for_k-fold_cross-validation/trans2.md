---
layout: default
title: "trans2"
---

# _5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation_ 
# _5.1.4 통계학 최강의 딜레마: k-폴드를 지배하는 편향-분산 트레이드오프_

We mentioned in Section 5.1.3 that _k_ -fold CV with _k < n_ has a computational advantage to LOOCV.
바로 앞 5.1.3절에서 우리는 이 타협안(_k_ -폴드 CV)이 "무식하게 인원수 _n_ 번만큼 짬을 때리는" LOOCV 기법보다 컴퓨터 쿨러를 지켜주는 엄청나게 자비로운 '연산 속도의 이점'이 있다고 입이 닳도록 칭찬했습니다.

But putting computational issues aside, a less obvious but potentially more important advantage of _k_ -fold CV is that it often gives more accurate estimates of the test error rate than does LOOCV.
그런데 말입니다. 컴퓨터 전기세가 얼마 나오든 속도 문제를 아예 머릿속에서 치워버린다고 가정해 봅시다. 겉보기엔 안 띄지만 무서울 정도로 소름 돋는 _k_ -폴드 CV의 진짜 위력은 따로 있습니다. 이 녀석이 대단한 척하는 LOOCV보다 **실전 에러 정답률을 훨씬 더 예리하고 날카롭게(더 정확하게) 때려 맞춘다는 충격적인 사실**입니다.

This has to do with a bias-variance trade-off. 
이 얄궂은 반전의 역학은 바로 그 악명 높은 **방패(편향)와 창(분산)의 딜레마, 즉 편향-분산 트레이드오프**라는 우주의 섭리와 직결되어 있습니다.

It was mentioned in Section 5.1.1 that the validation set approach can lead to overestimates of the test error rate, since in this approach the training set used to fit the statistical learning method contains only half the observations of the entire data set.
기억을 되살려 봅시다. 초반 5.1.1 절의 구닥다리 반반 쪼개기(검증 세트 접근법) 시절, 모델에게 고작 데이터 절반만 먹이니까 훈련이 부족해서 "내 머리로는 도저히 ㅠㅠ 실제 에러율은 엉망일 거야"라고 지레 겁먹고 오차율을 허풍 쳐서 **과대평가(overestimates)** 하는 멍청한 짓벌임을 벌였다고 했죠?

Using this logic, it is not hard to see that LOOCV will give approximately unbiased estimates of the test error, since each training set contains _n −_ 1 observations, which is almost as many as the number of observations in the full data set.
자 그 논리를 그대로 가져와 보죠! 그 극단인 LOOCV는 어땠습니까? 이건 훈련시킬 때마다 "전체 인원 - 단 1명"이라는, 사실상 오리지널 전체 덩치와 거의 싱크로율 100%에 육박하는 병력을 몽땅 먹여 훈련시킵니다. 즉 짬밥을 충분히 거하게 먹인 덕에 **과대평가의 겁쟁이 편향(bias)을 거의 완벽하게 0으로 날려버린 무적의 편향(unbiased)** 상태로 실전 에러 점수를 가늠해 낼 거라고 짐작하긴 아주 쉽습니다.

And performing _k_ -fold CV for, say, _k_ = 5 or _k_ = 10 will lead to an intermediate level of bias, since each training set contains approximately ( _k −_ 1) _n/k_ observations— fewer than in the LOOCV approach, but substantially more than in the validation set approach.
그리고 이어 등장한 우리들의 타협안, _k_ = 5조 혹은 10조로 쪼갠 뺑뺑이를 돌리면 어떻게 될까요? 여기선 훈련 덩치가 대락 ( _k −_ 1) _n/k_ 개가 됩니다. 이건 LOOCV급의 막강 물량보단 열세지만, 그래도 옛적 반반 무 많이 쪼개기 방식보다는 어마어마하게 물량이 두툼하죠! 그리하여 요 녀석은 이쪽저쪽의 눈치를 보며 **"적당히 중립 기어를 박은 쏠쏠한 중간 수준의 편향(bias) 수위"** 에 착륙하게 됩니다.

Therefore, from the perspective of bias reduction, it is clear that LOOCV is to be preferred to _k_ -fold CV. 
자! 그렇다면 여기서 결론!! 만약 이 세상 통계 전투가 오로지 **"어떻게든 편향(에러의 거품) 찌꺼기를 단 하나라도 더 죽여 남기지 않는가(bias reduction)"** 만이 목적이라면, 그야말로 무조건 두말할 나위 없이 LOOCV가 _k_ -폴드 CV 녀석보다 절대 우위로 추앙받아야 마땅할 것입니다!!

However, we know that bias is not the only source for concern in an estimating procedure; we must also consider the procedure’s variance.
**하지만... 세상은 그렇게 호락호락하지 않습니다.** 이 망할 통계 바닥에서 우리가 공포에 떨어야 할 유일한 악마가 오직 저 '편향(bias)' 한 놈뿐은 아니라는 걸 우린 이미 처절하게 배웠으니까요; 우리는 모델이 널뛰는 불안정성의 그림자, 바로 **통계 절차의 미친 분산(variance)** 이라는 거대 폭탄 스탯도 같이 감시하고 두려워해야만 합니다.

It turns out that LOOCV has higher variance than does _k_ -fold CV with _k < n_ .
뚜껑을 열고 진실을 까보니 충격적이게도 다름 아닌 저 어리석은 극단 LOOCV가, 오히려 중간 타협안을 택한 적당한 _k_ -폴드 CV보다 **훨씬 더 무식하게 미쳐 날뛰는 고공 분산(higher variance) 수치를 내뿜는다**는 사실이 탄로 납니다.

Why is this the case?
도대체 저 완벽해 보였던 LOOCV 녀석한테 왜 이런 널뛰는 재앙(높은 분산)이 강림한 걸까요?

When we perform LOOCV, we are in effect averaging the outputs of _n_ fitted models, each of which is trained on an almost identical set of observations; therefore, these outputs are highly (positively) correlated with each other.
LOOCV가 고통스럽게 밤새 돌려 뽑은 n개의 에러 스코어 결괏값 도출물들을 곰곰이 뜯어보십쇼. 이 녀석들은 각기 1명씩만 다르지, 훈련병 구성의 무려 99% 이상이 전부가 서로 **복사 붙여넣기 한 듯이 소름 돋게 거의 똑같은 애들끼리 판박이 훈련**을 돌려버린 결과입니다. 그러니까 이 n개의 모델 결산 결과물은 전부 "야 우리 한두 명 빼고 어차피 다 아는 식구잖아?" 라면서 **서로끼리 미치도록 강력한 파벌과 패거리(고도로 얽힌 양의 상관관계, Highly Correlated) 카르텔**을 극악하게 강렬히 형성하게 됩니다.

In contrast, when we perform _k_ -fold CV with _k < n_ , we are averaging the outputs of _k_ fitted models that are somewhat less correlated with each other, since the overlap between the training sets in each model is smaller.
반면 우리가 타협안인 중도 매운맛 _k_ -폴드 CV를 돌릴 땐 어떨까요? 애초에 그룹 자체를 큼직한 뭉텅이 조각으로 박살 내버렸으니, 모델을 돌릴 때마다 서로 겹치는 훈련 멤버들의 교집합(overlap) 비스킷 덩어리가 상대적으로 훨씬 더 적습니다. 그 말은 즉, _k_ 번 나온 모델 점수들이 상대적으로 "와 나 쟤네랑 별로 안 친한데?" 라면서 **서로 덜 끈적하게 묶이는(덜한 상관관계) 적당한 개별적 독립성을 보유한 점수들**로 분산 투자가 되어 도출된다는 의미입니다.

Since the mean of many highly correlated quantities has higher variance than does the mean of many quantities that are not as highly correlated, the test error estimate resulting from LOOCV tends to have higher variance than does the test error estimate resulting from _k_ -fold CV. 
수학의 잔혹한 정리를 떠올려볼까요. **"서로 패거리처럼 미치도록 끈끈하게 상관성이 높은 녀석들을 싹 다 더해서 평균을 낸 집단 덩어리는, 서로 조금 무관심하게 거리를 둔 덜 친한 녀석들의 덩어리들을 평균 낸 것보다, 외부 자극 한 방에 오들오들 훨씬 더 심하게 멘탈이 흔들려 무너지는 치명적 분산(variance)을 가지게 된다."** 고로 LOOCV가 뽑아낸 그 패거리 카르텔 테스트 에러 점수 요약본 지표는, 결국 _k_ -폴드 CV가 내어준 타협안 에러 추정치 방어력보다 한결같이 "작은 변화에도 무섭게 널뛰며 요동치는 훨씬 더 막강하고 끔찍한 분산(higher variance)"이라는 불안감 요동을 품는 저주에 걸리는 겁니다.

To summarize, there is a bias-variance trade-off associated with the choice of _k_ in _k_ -fold cross-validation.
자, 기나긴 여정을 요약하자면 결국 세상에 공짜는 없습니다. 우리가 교차 검증 게임판에서 그룹의 조각 수인 변수 _k_ 값을 몇 명 단위로 지목해 설정할 것이냐는, 결국 통계학의 그 무서운 절대 숙명인 저 방패(편향)와 창(분산) 비율 교환, **편향-분산 트레이드오프 딜레마 폭탄 스위치**를 어느 눈금 선에 갖다 놓을지를 결정하는 생사결 조율 결단과 직결됩니다.

Typically, given these considerations, one performs _k_ -fold cross-validation using _k_ = 5 or _k_ = 10, as these values have been shown empirically to yield test error rate estimates that suffer neither from excessively high bias nor from very high variance. 
현업에서 살아 숨 쉬는 통계 전문가들이 이런 뼈저린 양날의 검 딜레마 철학을 모조리 피 흘리며 다 검토 숙고해 본 끝에 터득한 게 있습니다. 결국 저 **_k_ = 5** 나 **_k_ = 10** 등수를 들이밀고 게임을 뛰는 것이, 편향이 높아 오차를 과장해버리는 멍청함(high bias) 에도 안 당하고 + 조금 달라졌다고 미친 듯 널뛰는 분산 공포의 저주(high variance) 에도 뻗지 않으며 살아남을 수 있는 **전설의 꿀통이자 가장 영리한 진정한 황금 밸런스 비율 치트키**라는 사실을요. 이것이 지난 세월 수많은 경험적 삽질 전투(empirically) 를 통해 모두 증명된 짠내 나는 필드 진리이기 때문에, 우리는 늘 입버릇처럼 **5와 10**이라는 폴드 개수를 신줏단지 모시듯 쓰는 겁니다!
