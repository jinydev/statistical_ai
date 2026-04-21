---
layout: default
title: "trans2"
---

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/trans2.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.4 Quadratic Discriminant Analysis
# 4.7.4 전투기 발진: 곡선의 지배자 이차 판별 분석(QDA) 가동

We will now fit a QDA model to the `Smarket` data.
자, 직선은 이제 지겹죠! 뻔한 1차 방정식 몽둥이를 내려놓고, 이제 부드럽게 휘어지는 곡선의 예술 타격 장비! **이차 판별 분석(QDA)** 이라는 웅장한 무기를 이 야생의 `Smarket` (주식장) 도박판에 꽂아 넣어 전장을 휘저어 보겠습니다.

QDA is implemented via `QuadraticDiscriminantAnalysis()` in the `sklearn` package, which we abbreviate to `QDA()`.
QDA 무기는 `sklearn` 패키지 무기고 안쪽 가장 깊숙한 진열장에 박혀있는 `QuadraticDiscriminantAnalysis()` 라는 엄청나게 길고 숨찬 스펠링의 도구를 통해 시스템적으로 꺼내와 세팅 가동되며, 우리 같은 실전 꾼들은 바쁘니까 보통 앞통수만 따서 초 간단하게 `QDA()` 라고 별명 지어 축약해 부릅니다.

The syntax is very similar to `LDA()`.
게다가 핵이득! 이 무기 녀석의 사용법 조작 매뉴얼(syntax)은 직전 판에서 신나게 썰어댔던 `LDA()` 기계의 버튼 조작 방식과 완전 쌍둥이처럼 소름 돋게 매우 똑같아서, 우리는 그냥 거의 거저먹기로 돌릴 수 있습니다.

```python
In [33]: qda = QDA(store_covariance=True) # 공분산(covariance) 기록 장치 스위치까지 꽉 켜서 곡선기 발진!
qda.fit(X_train, L_train) # 2004년 과거 훈련 식량 던져주고 피 터지는 스파링 돌입!
```

```python
Out[33]: QuadraticDiscriminantAnalysis(store_covariance=True) # "예, 훈련 무사히 다 마쳤습니다 주인님! 곡선 궤도 준비 완료!"
```

The `QDA()` function will again compute `means_` and `priors_`.
`QDA()` 총통 함수 기계 역시 기본기가 아주 튼실해서, 이전 직선 기계들처럼 데이터 부대를 신나게 때려서 훈련시키면서 동시에 내부 뇌 속에 각 클래스들의 기본 타점인 `means_`(본진 평균 좌표들) 스탯 속성과, 야생 기본 도박 확률인 `priors_`(사전 배당 확률 몫) 고유 정보 수치들을 알아서 철저하게 내부 몰래 척척 전부 계산(compute) 백업해 저장해 둡니다.

```python
In [34]: qda.means_, qda.priors_ # 야! 뇌 속에 저장해 둔 본진 좌표랑 도박 확률 다 토해내 봐!
```

```python
Out[34]: (array([[ 0.04279022,  0.03389409], # 하락팀(Down) Lag1, Lag2 타깃 좌표 세팅
                 [-0.03954635, -0.03132544]]), # 상승팀(Up) Lag1, Lag2 타깃 좌표 세팅
          array([0.49198397, 0.50801603])) # Down 찍을 확률 49%, Up 찍을 확률 50.8%! (아까 LDA랑 똑같음!)
```

The `QDA()` classifier will estimate one covariance per class.
여기서 LDA 기계와 이 곡선 장비 QDA 간의 가장 극명하고 치명타 적인 작동 철학 격차 차이가 벌어집니다! 이 유연한 `QDA()` 분류 시스템 장비는 집단 전체를 무식하게 묶어 한 치수로 다루지 않고, 아주 예민하고 섬세하게 **관할 지역 각 파벌 클래스당 한 개씩 각각 따로따로** 분리하여 독립된 그룹 고유 공간 덩치를 재는 분산 통계인 공분산(covariance) 타점을 내부적으로 차별화 지어 개별 분산 추정(estimate) 판단해 버릴 것입니다. 아주 민감하고 맞춤형(유연한 곡선형 덩치 설정) 포지션 세팅이죠!

Here is the estimated covariance in the first class:
아래 추출 출력 산출된 결과 데이터 수치 파편 값은 그렇게 철저히 그룹별로 따로 분리된 산출물 중, 그 첫 번째 지목 팀 (즉, Down 하락 팀) 진영 속 클래스 내의 개별 덩치를 나타내는 찐 추정 고유 공분산 측정 결괏값의 모습입니다:

```python
In [35]: qda.covariance_[0] # 야! 첫 번째 팀(Down팀) 공분산(덩치 사이즈) 까봐!
```

```python
Out[35]: array([[ 1.50662277, -0.03924806],
                [-0.03924806,  1.53559498]])
```

The output contains the group means.
이 속성 결괏값 해킹 도출 출력물 콘솔 로그 창은 여전히 우리가 예측한 대로 세력 분류된 각 통계 군단 그룹 본진 좌표인 도출 평균 좌표들(group means) 요약본 백업 데이터 파편 덩어리를 아주 굳건하게 오롯이 포괄 포함 보존 보유 출력해 줍니다. 

But it does not contain the coefficients of the linear discriminants, because the QDA classifier involves a quadratic, rather than a linear, function of the predictors.
**그런데 잠깐!** 이상한 점! 아무리 털어도 눈 씻고 찾아봐도 출력 체계 정보 기판 결과 내에서는, 이전 LDA 직선 기계 때는 분명히 떴고 자랑스럽게 여겼던 무기 공식 단서! 즉 **직선 예측 도출 판별식들의 단원 가중치 계수 부속들(coefficients of the linear discriminants)** 이 전혀 일절 관측 포함 발견 나타나지가 않습니다! 기계 고장인가요? 아뇨! 그 근본 주된 기전 원인은 바로 이 특수한 유연 마스터 QDA 단독 분류 장치가 기동 작동하며 투입될 때 쓰는 무기가, 이전에 썼던 단순한 무식 몽둥이인 '1차원 직선적 선형 기반 수식' 뼈대가 아니라, 오히려 훨씬 더 유연하고 복잡하게 휘어지는 '다변량 분류 예측 거대 구조 변수들의 거대 **이차 곡선형(quadratic)** 구조 함수' 라는 곡선 수식 기폭 공식을 자기 몸속 머릿속 내부 뇌리에 필수 채택하여 전극 포함 연산 작용 수반(involves) 작동시켜 버리기 때문입니다. 즉, "하나의 단순한 1차 직선 곱셈 가중치" 따위로 요약 묘사 설명해 줄 수가 없다는 깊은 스펙의 뜻이죠. 무기가 다른 겁니다!

The `predict()` function works in exactly the same fashion as for LDA.
하지만 내부 무기 속 사정 복잡한 공식 조립 스탯이 어찌 된 판국이든 간에 상관없이, 겉보기 조작 방식인 실전 막타 사격 스위치! **`predict()` 예측 구동 함수 조작 격발 버튼 구조 절차 작동**은 그저 사용자에겐 아주 편안하게, 기존 직선 기계 LDA를 다룰 때 매뉴얼 사용 방식에서와 구문 글자 단 하나 안 틀리고 정확히 100% 똑같은 익숙하고도 편안한 동일 조작 타격 방식(fashion) 절차로 무력 기동 작동합니다. 쏘세요!

```python
In [36]: qda_pred = qda.predict(X_test) # 미래를 쏜다! 2005년도 시험 답안지를 채워라! 예측 발사!
confusion_table(qda_pred, L_test) # 채점!!!
```

```python
Out[36]: Truth      Down   Up
Predicted            
Down         30   20
Up           81  121 # 빙고!!!!! 눈을 씻고 다시 보자!!!
```

Interestingly, the QDA predictions are accurate almost 60% of the time, even though the 2005 data was not used to fit the model.
와우! 매우 가슴 벅차게 흥미로운 통쾌한 극적 반전 쾌거 결과(Interestingly)! 비록 이번에도 이 기계의 훈련 적응 스파링 조립 적합 시, 단 한 번도 사전 미래 유출 정보 용도 검정용 타겟 인 2005년 미래 정답 예언 예측 데이터 지식을 기계가 단 0.1% 도 슬쩍 컨닝해 본 적이 없음에도 불구하고, 최종 실전 야생에 투입된 치열한 모의 결과 이 부드럽게 휘는 곡선의 QDA 암살 모델 장치의 도출 실전 적중 예측 정확도 영광의 타점은 1년 시간의 전체 도박 기간 중 거의 소름 돋게 무려 **대거 60% 에 육박하며 상승 도달 명중** 전개를 이룹니다(accurate)! (아까 50따리 원숭이 찍기에 비하면 이 정도면 환골탈태 갓 급 기계 진화죠!)

```python
In [37]: np.mean(qda_pred == L_test) # 정답 맞춘 정확도 채점해라!!
```

```python
Out[37]: 0.5992063492063492 # 무려 59.9% !!! 대박이다!!!
```

This level of accuracy is quite impressive for stock market data, which is known to be quite hard to model accurately.
기계가 기어이 도출 산출해 낸 이러한 성능 수준급 의 엄청난 파괴적 분류 체계 측정 적중률 60% 라는 정확도(accuracy) 결과 팩트는, 본래 통계 분석상 결코 개미들이 수식으로 정확하게 모델링 패턴을 꼽고 모의 기계로 정답을 판별 파악 달성 하기란 도저히 불가능하고 극악무도하게 매우 어려운(hard) 죽음의 늪 변수 영역인 것으로 널리 악명 높게 알려진 변동성 거대 주식 증권 헬 판 시장 도박 데이터 관측 기반 실체에 대해서는, 사실상 꽤 엄청난 상위 랭커 급의 상당히 매우 이례적이고 놀라울 만큼 통계적 스포트라이트를 받는 화려한 성과 스탯, 아주 성과 인상적인(impressive) 기념비적 수치 영광 타점 도출 결과물입니다.

This suggests that the quadratic form assumed by QDA may capture the true relationship more accurately than the linear forms assumed by LDA and logistic regression.
이 거대한 무력 적중 달성 결과 팩트 파편이 강하게 시사하는 바는 이겁니다. 이 변화무쌍한 주식판을 재단하는 덴, 바로 저렇게 똑똑하고 아주 유연하게 곡선으로 휘어 작동하며 감싸 안는 이 QDA 기계 시스템 모형 장비가 조립 설계 시 선택 채택한 곡선의 유려한 **'이차 곡선 단층 공식 허용 형태(quadratic form)'** 조립 통계 구조 판별 구동 방식 논리 자체 가, 도리어 이전에 고집 부렸던 직선밖에 모르는 뼈대 경직된 아재 스타일 선형화 옛 구도 무식한 LDA 모형이나 조작 방식도 단조롭고 무식하기 짝이 없던 로직 조작 일차원 로지스틱 회귀 기계 꼰대들의 구형 스펙에 의해 오직 선이라 착각하여 확고히 강압 일괄적으로 융합 가정 채택되었던 평면 스키마의 뻣뻣한 **'직선 선형 예측 형태들(linear forms)'** 도구들 보다도, 어쩌면 내부 비밀 패턴 진동 진리의 치열한 참된 무구 주가 변동 예측 연관 인과 변수들의 교묘하게 얽히고설킨 꼬인 진짜 연동 관계(true relationship) 지표 흐름 통계 팩트 실체를 한층 더 월등하게 기막히게 정밀 파악하고 미세 구조 늪에서 훨씬 더 섬세하게 정확하게(accurately) 통계적 미세 진동 패턴 포착 탐지(capture) 해서 맞춤으로 산출해 낼 수 있는 위력을 지녔을 수도 있다는 유력한 분석 기조 맹점을 아주 극도로 강하게 시사합니다(suggests). 주식은 역시 직선이 아니라 예측 불가 곡선 춤이었던 거죠!

However, we recommend evaluating this method’s performance on a larger test set before betting that this approach will consistently beat the market!
**자, 여기서 잠깐! 진정합시다. 60% 맞췄다고 전재산 팔아서 주식 풀 매수 하러 갈 생각인가요?** 그러나 우리 차디찬 이성 통계학도들이여, 섣부르게 흥분해서 우리는 여러분이 당장 주식 도박판 시장에서 이 알량한 통계 기계 하나의 투기 기법 접근법 단일 모델 조작 예측 방식을 믿고, 이놈이 향후 미래에도 영원토록 시종일관 지속적으로 끊임없이(consistently) 통계 시장 변동 장세를 완전히 다 통달하고 판돈을 싹쓸이하여 확실하게 다 박살 상회해 이기고 절대 괴물 주식 하우스를 붕괴 물리칠(beat the market) 절대 마법의 지팡이 성배 법칙일 것이라고 코딩 뽕에 취해 맹신하여 현실 전재산 투입 확신 풀 매수 베팅(betting) 조작 거래라는 매우 극단적이고 위함 천만한 한강행 편도 큰 도박을 섣부르게 맹목 구동 전개 걸어버리기 이전에! 반드시 이론적 스키마 검증 차원에서 앞으로 이와 같은 파생 동류의 환경에서 모조리, 지금 당장 써먹은 도박장 보다 훨씬 엄청나게 수백 배 더 크고 방대한 크기 제원, 폭발적 데이터의 다른 초대량 실전 모의 실전 테스트 예비 검정 시뮬레이터 세트(test set) 장치상 구동 환경 파도 기반 속에서 이 통계 수학적 파생 예측 작동 메서드의 통계적 진짜 우연 배제 확실성 있는 실전 모의 생존 강도 실성능(performance) 도출 결과 생존율 구동 전개를 냉정하고 피도 눈물도 없이 거듭 통계 재차 모의 반복 평가 검증(evaluating) 해 보는 매우 깐깐한 사전 필수 주의 조치 및 탐욕 자제력 검토 단계 이행 결단 을 여러분의 생존을 위해 가장 최우선 강력히 필수로 제안하고 뼛속 깊이 권장 단언(recommend) 및 경고 합니다! 언제나 도박장에선 기계보다 당신의 이성이 위대해야 합니다!

---

## Sub-Chapters

[< 4.7.3.1 Out31 True](../4_7_3_linear_discriminant_analysis/4_7_3_1_out31_true/trans2.html) | [4.7.5 Naive Bayes >](../4_7_5_naive_bayes/trans2.html)
