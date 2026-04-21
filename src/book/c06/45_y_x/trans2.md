---
layout: default
title: "trans2"
---

# $Y = X\beta + \epsilon$, 
# $Y = X\beta + \epsilon$ (가짜 변수 암살 작전), 

where $\beta$ has some elements that are exactly equal to zero. 
여기서 명심할 점은, $\beta$ 계수 요원들 중 다수는 위장 취업한 무능력자라서 실제 스펙 수치가 정확히 '0' (exactly equal to zero)으로 증발해버리는 깡통 변수들이라는 사실입니다.

- (b) Split your data set into a training set containing 100 observations and a test set containing 900 observations. 
- (b) 당신이 쥐고 있는 전체 데이터 병력을 무자비하게 반으로 쪼개십시오(Split). 고작 100명의 소수 정예 관측치 병력만 남겨 가혹한 훈련소(training set)에 밀어 넣고, 나머지 방대한 900명의 관측치 병력은 실전 피바람이 불어닥칠 테스트 세트(test set) 전장으로 보내 대기시킵니다.

- (c) Perform best subset selection on the training set, and plot the training set $\text{MSE}$ associated with the best model of each size. 
- (c) 이제 그 100명의 훈련소 세트(training set) 내부에서 무식할 정도로 모든 변수 조합을 닥치는 대로 쏴보는 **최적 부분집합 선택(best subset selection)** 알고리즘을 강제로 돌리십시오(Perform). 그리고 모델 사이즈(투입 변수 개수) 체급별로 가장 타점 좋은 챔피언 모델이 기록한 훈련소 $\text{MSE}$ (평균 제곱 오차) 에러율 지표를 우상향 차원 플롯(plot) 레이더망에 쫙 점찍어 도식화합니다.

- (d) Plot the test set $\text{MSE}$ associated with the best model of each size. 
- (d) 훈련소의 달콤한 환상을 깰 차례입니다. 아까 뽑아둔 체급별 챔피언 모델들을 아까 격리해 둔 900명의 무자비한 실전 테스트 세트에 던져 넣고, 거기서 처참하게 깨지고 깎인 실전 $\text{MSE}$ 지표들을 다시 한번 플롯 차트(Plot)로 냉혹하게 그려냅니다.

- (e) For which model size does the test set $\text{MSE}$ take on its minimum value? Comment on your results. If it takes on its minimum value for a model containing only an intercept or a model containing all of the features, then play around with the way that you are generating the data in (a) until you come up with a scenario in which the test set $\text{MSE}$ is minimized for an intermediate model size. 
- (e) 자, 심판의 시간이 왔습니다. 도대체 몇 명의 변수를 기용한 체급 사이즈 파츠(model size)에서 우리의 실전 테스트 $\text{MSE}$ 지표가 가장 낮고 예리한 바닥 최저치(minimum value)를 찍으면서 안착(take on) 합니까? 여러분이 육안으로 확인한 이 살벌한 스코어 결과(results)에 대해 입을 열어 진단 논평(Comment on)을 내려보십시오. 만약 운명의 장난처럼 그 최저 $\text{MSE}$ 바닥점이 **고작 빈 껍데기 절편 상수항 하나만 덜렁 가진 모델**이나 반대로 **모든 피처를 무식하게 다 때려 박은 과적합 모델** 언저리에서 엉뚱하게 발생해버렸다면? 그렇다면 여러분은 테스트 세트의 $\text{MSE}$ 그래프 포물선이 중간쯤 되는 합리적 타협 중간 사이즈(an intermediate model size) 하에서 가장 낮고 이쁜 최저점 앵글(minimized)을 만들어주는 이상적인 시나리오 셋업 국면 장치(scenario)가 얻어걸릴 때까지, 맨 처음 문항 (a)번에서 데이터를 조작 생성(generating) 하던 파이썬 공식 설정 방식(way) 세팅을 이리저리 가지고 놀며(play around with) 리셋과 노가다를 반복하십시오.

- (f) How does the model at which the test set $\text{MSE}$ is minimized compare to the true model used to generate the data? Comment on the coefficient values. 
- (f) 드디어 $\text{MSE}$ 과녁을 가장 낮게 예리하게 명중시킨(minimized) 여러분의 최고 에이스 모델! 이 녀석의 변수 배치구조는, 애초에 조물주인 여러분이 맨 처음 신의 손으로 모의 데이터를 빚어낼(generate) 때 설정했던 그 오리지널 정답 모델(true model) 뼈대와 견주어 보았을 때 과연 어떤 판도로 비교 대칭 일치 모순(compare) 되는 기믹을 띱니까? 파라미터가 입고 있는 실제 계수 전투력 스코어 타점 수치값(coefficient values)들 하나하나에 돋보기를 들이대며 논평(Comment on) 하십시오.

- (g) Create a plot displaying $\sqrt{\sum_{j=1}^p (\beta_j - \hat{\beta}_j^r)^2}$ for a range of values of $r$, where $\hat{\beta}_j^r$ is the $j$th coefficient estimate for the best model containing $r$ coefficients. Comment on what you observe. How does this compare to the test $\text{MSE}$ plot from (d)? 
- (g) 튜닝 사거리 $r$ 이라는 여러 제약 변수 구간들(a range of values)에 대응하여, $\sqrt{\sum_{j=1}^p (\beta_j - \hat{\beta}_j^r)^2}$ 라는 이 기괴하고 파괴적인 오차율 모니터 공식을 디스플레이 화면 위 차트 지표(a plot) 상에 시원하게 렌더링 작도 구현 생성(Create)해 그리십시오. 팁을 주자면 여기서 얽힌 암호 $\hat{\beta}_j^r$ 는, 정확히 $r$ 개의 한정된 무기(계수) 개수들만 짊어진(containing) 당시 부문 최고 챔피언 모델(best model)의 예측 추정 스코어인 $j$ 번째(the $j$th) 전투력 타점 계수력(coefficient estimate)을 온전히 뜻합니다. 이 플롯을 그리고 난 뒤 육안으로 타격 식별 관측파악(observe)한 그로테스크한 현상(what)에 대해 일갈의 부연 코딩 조명 해석(Comment on)을 내뱉으십시오. 특히, 지금 여기서 본 이 요동치는 현상이 앞선 번호 (d)번 스테이지에서 뽑아냈던 오리지널 테스트 $\text{MSE}$ 플롯 구조 형태와 비교(compare)하여 무슨 소름 돋는 평행 이론 우위 대조 모순 매칭 판도 연결 고리 반응을 보이고 있습니까?

11. We will now try to predict per capita crime rate in the `Boston` data set. 
11. 자, 탄창을 갈아 끼웁니다. 이번엔 우리가 그 악명 높은 `Boston` 부동산 데이터 판도에 무작정 투입되어, 마을 동네의 1인당 범죄 발생률(per capita crime rate) 게이지 스코어를 향해 예측 총구를 과감히 겨누어 조준 훈련 시도해 볼 액션 차례(try to predict) 입니다!

- (a) Try out some of the regression 회귀 methods explored in this chapter, such as best subset selection, the lasso, ridge regression, and PCR. Present and discuss results for the approaches that you consider. 
- (a) 이번 6장 전장에서 우리가 땀 범벅으로 다루고 핏빛으로 익혀 해부 섭렵 탐색 강탈(explored) 했던 강력한 회귀 머신건(regression methods) 세트 중 몇 자루(some of)를 골라 거침없이 방아쇠를 당겨 실전 시도(Try out) 해보십시오. 가령 무식한 전수 탐색인 최적 부분집합 선택(best subset selection), 무자비한 계수 암살자 라쏘(lasso), 계수 수축 압축기 릿지 돌격소총(ridge regression), 데이터 차원 용광로인 PCR 저격총 등(such as)이 있겠군요. 무기를 고르고 조작 고려 세팅(consider) 해 본 그 툴 방식 접근 병기(approaches) 전략 타원 별로 실전 예측 보고서 결과(results)들을 멋지게 브리핑 패널에 제시(Present) 올려두고, 서로 뭐가 낫네 구리네 치열하게 토론 검증 논파(discuss)의 장을 전개하십시오.

- (b) Propose a model (or set of models) that seem to perform well on this data set, and justify your answer. Make sure that you are evaluating model performance using validation set error, crossvalidation, or some other reasonable alternative, as opposed to using training error. 
- (b) 이 피 마르는 보스턴 데이터 세트 전장 위에서 가장 폼 미친(seem to perform well) 활약 킬 수를 쓸어 담아줄 단 하나의 원픽 에이스 모델, 혹여는 모델 최정예 군단 그룹 덩어리(or set of models)를 딱 찍어 단언 결론 상정 추천(Propose) 제시하십시오! 그리고 도대체 왜 그런 결론 타점(answer)이 나왔는지에 대한 타당한 논거 방패와 철통같은 입증 논리(justify) 를 전개 변론하십시오. 다시 한번 귓가에 경고 명심 못을 박건대(Make sure), 당신이 그 모델의 순수 잠재 전투력 타점 수치(model performance) 척도를 뽑아낼 때만큼은, 저열한 허수아비 훈련 오류율 숫자(using training error) 따위에 절대 현혹 모순 부합 맹신 의존 침묵 빙자 기대(as opposed to)지 말고! 반드시 뼈 때리는 검증 세트 환경 오차 확인망(validation set error), 혹은 치밀하게 교차로 겹쳐 검증하는 크로스 밸리데이션(crossvalidation), 그것도 아니면 무언가 다른 그 어떤 지당 합리 논리 타당한(reasonable) 훌륭한 대체 루트 대안책 잣대 기저 진영(alternative)들을 적극 활용 도용 차용 의존 병행 도입 기용(using) 해서만 실전 스펙 평가 검정을 치러내야 한다는 사실을 잊으시면 안 됩니다.

- (c) Does your chosen model involve all of the features in the data set? Why or why not? 
- (c) 마지막 질문입니다. 치열한 접전 끝에 당신이 최종 왕관을 씌워 간택 픽업(chosen)한 그 괴물 에이스 모델의 설계 내부 뼈대 장바구니 안에는, 처음 주어졌던 저 전역 데이터 피처 파편 덩어리들(features) 전체 몽땅 모조리 온통(all of) 이 예외 하나 없이 싹 다 탑승 징집 개입 연루 포함 합세 수렴 수용 소지 합류(involve) 되어 존재 합니까? 그렇다면 대체 왜 그렇다고 봅니까(Why)? 안 그럼 무참히 썰려 탈락 거부 제거 축소 되었다면 그 이유(why not)는 도대체 뭐라고 변명하시겠습니까?
