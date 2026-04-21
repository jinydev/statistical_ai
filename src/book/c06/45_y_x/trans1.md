---
layout: default
title: "trans1"
---

# $Y = X\beta + \epsilon$, 
# $Y = X\beta + \epsilon$, 

where $\beta$ has some elements that are exactly equal to zero. 
여기서 파라미터 계수 $\beta$ 는 그 성분 요소 수치들(elements) 중 일부가 완벽하고 정확하게 완전한 '0' 제로 수치와 부합 일치(exactly equal to zero)하는 부분 공간들을 보유 가지고(has) 있습니다.

- (b) Split your data set into a training set containing 100 observations and a test set containing 900 observations. 
- (b) 여러분의 전체 관측 데이터 세트를 100개의 관측치 개수를 소유 포괄 수반하는(containing) 훈련 데이터 세트(training set)와, 900개의 넉넉한 관측치 수량을 통째 포괄 포함 담지하는(containing) 나머지 테스트 데이터 세트(test set) 두 그룹으로 물리적 분할 분리 조치(Split) 하십시오.

- (c) Perform best subset selection on the training set, and plot the training set $\text{MSE}$ associated with the best model of each size. 
- (c) 분리해 둔 당해 훈련 데이터 세트 풀 안쪽(on the training set) 국면 속에서 고전 절차인 최적 부분집합 선택(best subset selection) 알고리즘 방식들을 온전히 단행 구동 발동 수행(Perform) 시키고, 그런 다음 산출된 각 변수 모형의 치수 크기 사이즈 체급(each size) 갈래별로 각각 산출 매칭 연결된(associated with) 최고 으뜸 최적의 우수 예측 모델을 기반으로 삼아, 앞선 훈련 세트 생태의 결과 $\text{MSE}$ (평균 제곱 오차 지표) 추이를 점철 도면 차트로 도식 구현 출력(plot) 해보십시오.

- (d) Plot the test set $\text{MSE}$ associated with the best model of each size. 
- (d) 마찬가지로, 이번에는 동일 각 모델 치수별 크기별 최고 우수 등급 모델 지표에 전격 매칭 고정 부여 부합 결합 연동(associated with) 지어진, 그 거대 테스트 잔류 세트 환경의 예측 $\text{MSE}$ 결괏값 추이 플롯 표면을 렌더링 시각 도식화(Plot) 하십시오.

- (e) For which model size does the test set $\text{MSE}$ take on its minimum value? Comment on your results. If it takes on its minimum value for a model containing only an intercept or a model containing all of the features, then play around with the way that you are generating the data in (a) until you come up with a scenario in which the test set $\text{MSE}$ is minimized for an intermediate model size. 
- (e) 어느 정도 규모와 덩치 갯수의 모델 크기(model size) 세팅에서 그 테스트 세트 예측 검증 $\text{MSE}$ 지표가 가장 낮고 작디 작은 최소 절대 최저 에러 바닥 임계 수치값 결론(minimum value) 단계 국면을 이끌어 취하며(take on) 돌파 도달합니까? 여러분이 도출해 낸 이 결괏값 결과 추이 양상(results)들에 대해 의견 코멘트 해석을 논평 부연 기재(Comment on) 하십시오. 혹여라도 만약, 고작 절편 변수 상수항 껍데기 하나 만을 부실히 단독 대동 포함하거나(containing only an intercept) 반대로 앞선 모델 속 전체 모든 특징 군집 피처(all of the features)들을 깡그리 몽땅 다 무식하게 쓸어 포함 흡수시켜 버린 극단적인 모델 뼈대 진영 자체에서 상기 그 최저 에러 예측 최솟값(minimum value) 스코어 실적을 산출 취하게(takes on) 되는 발생 에러 역전 현상이 벌어진다면, 그렇다면 그 후단 테스트 검증 세트의 결과 $\text{MSE}$ 값이 비로소 극단이 아닌 다소 중립적인 중간 매개 수준 합리적 크기의 체급 모델 단위 구조(an intermediate model size) 하에서 가장 타당하고 절제 축소된 최소 효율 스코어(minimized)를 내는 이상적 합당 시나리오 포맷 설정 국면 형태(scenario)에 여러분들이 다행히 마침내 도달 착수 부합 봉착(come up with) 할 수 있을 그때 시점(until)까지, 초기 문제 문항 (a)번 영역에서 여러분이 애초 관측치 데이터를 이끌어 생산 제조 발현 조립(generating) 했었던 그 내부 생성 데이터 공식 메커니즘 방식 패턴 장치 계수 수식 과정 양상(way)들을 여러 방면으로 요리조리 주물러 다르게 실험 시도 변형 세팅 조작 이행(play around with) 재 조정해 보십시오.

- (f) How does the model at which the test set $\text{MSE}$ is minimized compare to the true model used to generate the data? Comment on the coefficient values. 
- (f) 테스트 세트 결과 검증 $\text{MSE}$ 에러 지점을 가장 낮게 바닥으로 최저 최소화 탕감(minimized) 해주었던(at which) 최적 산출 모델의 자태는, 앞서 초기 원래 데이터군을 인위적으로 탄생 배태 발현 생성 조립 생산(generate) 해내기 위해 여러분들이 애초 사용 매설(used to) 이입했던 저 진실 진성 뼈대 정답 참 본연 원래 기본 모델(true model) 구조체와 견주어 비교(compare) 해 보았을 때 과연 어떠한 유사 부합 양태로 매칭 대조 진단 평가 판단(How does) 됩니까? 각 계수 $\beta$ 파라미터 배정 산정 수치 척도 타점 스펙값(coefficient values)들 성분에 관해 여러분들의 정밀 심층 코멘트 해설을 표명 논평 부가(Comment on) 기입 제시하십시오.

- (g) Create a plot displaying $\sqrt{\sum_{j=1}^p (\beta_j - \hat{\beta}_j^r)^2}$ for a range of values of $r$, where $\hat{\beta}_j^r$ is the $j$th coefficient estimate for the best model containing $r$ coefficients. Comment on what you observe. How does this compare to the test $\text{MSE}$ plot from (d)? 
- (g) 단일 범위 국면이 아닌 여러 일련의 튜닝 범위 나열 나열된 궤도 범위 폭의 이행 편차 변수(a range of values) $r$ 요소들에 대하여, 해당 $\sqrt{\sum_{j=1}^p (\beta_j - \hat{\beta}_j^r)^2}$ 산식 포맷 공식 산출 에러 지표값을 모니터 시각 지면에 디스플레이 도식 시연 표시 표출 묘사(displaying)해 주는 하나의 플롯 차트(a plot) 지계를 직접 작도 설계 구축 생성 조립 구현 생성(Create) 하십시오. 단, 이 조건문 수식에서 통용되는 국지적 기호 명명 $\hat{\beta}_j^r$ 수치 포맷체는, 정.확.히 $r$ 개의 유효 계수 부피 수량들을 대거 통괄 보유 개입 포함(containing) 하는 각 당해 최고 부문 성능 우수 등급 모델 포맷(for the best model)을 위해 산정 도출 도달 식별 환산된 $j$번째 (the $j$th) 개별 계수 추정 타점 척도 예측 수치값(coefficient estimate)을 정확히 지칭 뜻합니다. 출력된 표면상에서 여러분 모니터 상 통과 관찰 목도 식별 식별 진단 확인(observe) 하신 바 내용 징후 사실(what)에 대해 상세 부연 지적 부기 논평 조명 서술 코멘트 설명 해설을 추가 기명(Comment on) 하십시오. 상기 현상들의 진단 조짐 자태는 앞선 문항 (d) 블록 상에서 출력 도출 묘사 건져 잉태 얻어낸 바 있는 테스트 $\text{MSE}$ 추세 플롯과 어떤 역학 구조 구도 양상 비교 대조 우위 진단 여부 판도(How does this compare) 양상을 띠며 직조 대응 매칭 대비(compare) 됩니까?

11. We will now try to predict per capita crime rate in the `Boston` data set. 
11. 자, 우리들은 이제 드디어 매우 유명한 `Boston` 주택가 데이터 관측 세트 환경 내부에서 일 인당 범죄 발생률 게이지 지표 점수 척도 표면(per capita crime rate) 수치를 진정 표적 예측 조준 타진 가늠 도출 탐색(predict) 코자 과감히 전진 시도 돌입 전개 착수 감행 이행(try to)을 펼칠 것입니다.

- (a) Try out some of the regression methods explored in this chapter, such as best subset selection, the lasso, ridge regression, and PCR. Present and discuss results for the approaches that you consider. 
- (a) 이 당해 6장 챕터 궤적 영역 내에서 깊이 심도 있게 전역 고찰 탐구 진단 정밀 도출 섭렵 파헤 살펴 탐색 모색(explored) 해본 역사가 있는 주요 중요 핵심 주력 회귀 해결 단면 모델 방법 기전 작전 접근 채널 수리 기법 방식 툴 장치(regression methods) 녀석들 중 그 주요 일부분 소수 선택 발탁 녀석들(some of), 즉 예를 들어 가령 예컨대 비견 참작 들어보자면(such as) 최적 부분집합 선택(best subset selection) 파트라던가, 라쏘 페널티 장치(the lasso), 릿지 통제 회귀선법(ridge regression), 그리고 주성분 투과 회귀 기반(PCR) 등등의 일부 부류 모델 부대원들을 적극 시범 검증 기동 시험 가용 실험 트라이 테스트 사용 발휘 감행 타진 투사 확인 적용 타진(Try out) 시도해 구동해 보십시오. 여러분들 측에서 이리저리 다각적 고찰 신중 판단 설계 사료 안목 취사 조작 고려 감안 검토 선별 픽업 결정 구상 투입 고려 검토(consider) 해본 그 개별 매개 방법 접근 툴 방법론 수단 절차 공조 엔진 전략 체계 파벌(approaches) 들과 연계된 개별 매칭 후단 성능 예측 실적 통계값 결과 실체물 평가 결괏값들(results)을 일일이 제안 지면 제시 돌출 보고 표방 진설 공개 노출 표명 제시(Present) 할 것이며, 나아가 이 결과를 토대로 심오한 논평 논파 쟁점 담론 논의 해석 부연 비교 검토 토론 담의 토의 담화 서술(discuss) 단계를 추가 전개 하십시오.

- (b) Propose a model (or set of models) that seem to perform well on this data set, and justify your answer. Make sure that you are evaluating model performance using validation set error, crossvalidation, or some other reasonable alternative, as opposed to using training error. 
- (b) 상기 이 특정 난해 실전 데이터 세트(on this data set) 환경 판도 상에서 유독 매우 견고 영리 출중 뛰어 무난 우수 매끄 강력 탁월 월등 훌륭 유능 기특 온건히도 뛰어난 발군의 예측 성능 타점 발휘 진도 결과 기능 성과 구사(perform well) 퍼포먼스를 내며 제대로 먹혀 들어가는 양상 기조 단면 동향 사태 여력 짐작 가망 양태 국면 현상 기조 현상(seem to)을 띠는 한 단일 강력 최우수 모델, 혹은 여러 묶음 병합 군단 세트 다수의 강력 모델 진영 조합체 그룹 진영 단락 등(or set of models)이라도 전면 진단 제시 추천 발의 투척 제안 단언 제의 제안(Propose) 제시해 부르십시오. 그리곤 왜 그런 선택 지정 발탁 지목 결론(answer) 타점에 도달 안착하게 되었는지에 대한 타당한 본연 당위 합리 정당 논리 근거 입증 해명 변호 사유를 조명 변호 이유 논거 제시 입증 타당 증빙 조명 정당화(justify) 하십시오. 반드시 명심 필히 유념 단호 결단 기필 자각 이행 명심 유념 자각 필히 확인 확실 당부 확고히 명심(Make sure) 해야 할 대전제 율법 조건 한계(that)로는, 섣부르게도 저급한 훈련 전용 모델 에러 오차율(using training error) 스펙만을 맹신 추종 활용 단일 지목 의존 융합 탑재(using) 하는 그 어리석고 멍청 위험한 단방향 단순 구식 지표 방식 편향 굴곡 의존 조작과는 참으로 매우 상이 극단 모순 전복 철두 전면 반대 상존 대치 정반대 대조 배치 정반대의(as opposed to) 기조 철칙 방면으로써, 여러분들의 모델 객체 타석 평가 잣대는 철두철미한 독립 검증 세트 환경상의 예측 오차 결과(validation set error), 혹은 기민한 다각 크로스 교차 검증 통과 수치망(cross-validation), 나아가 아니면 혹은 또 다른 어떤 그 무엇이든 간에 논리 기반 합리 이치 지당 타당 상응 건실 합당 상응 지당 합당한(reasonable) 강력 대체 우회 방편 교체 체체 우회 노선 채널 대안 지표 진영 결단 방법 대안책 수단 평가 방식(alternative) 채널들을 적극 구동 병합 활용 의존 동원 도용 기용 채용 지득 부려 사용(using) 부림으로써, 모델 본연의 궁극 예측 잠재 퍼포먼스 기력 능력 타진 실력 성과 성능 위용 역량 성능 지표(model performance) 체급들을 객관 평가 검증 계산 타협 계측 평가 측정 판정(evaluating) 해내고 매겨 도출하고 있어야만 한다는 중요한 룰을 지켜야만 합니다.

- (c) Does your chosen model involve all of the features in the data set? Why or why not? 
- (c) 결국 최종장 국면에 이르러 위풍 등극 여러분이 직접 지목 픽업 채택 간택 발탁 지정(chosen) 추려낸 그 최후 막강 우수 모델(your chosen model)의 내부 구조 생태계 뼈대 안에는, 과연 저 초기 오리지널 전역 데이터 세트 그룹 전장에 흩어져 나열 기입 존재했던 전체 일체 깡그리 일동 전부 모든 온통 모두 각양 전부 전역 모든(all of) 특징 세력 정보 컬럼 특성 피처 변수 대상물 관측 컬럼 예측 변수 인자 특징들(features)의 파편 개체수 모두가 일체 잔류 전부 온전히 대동 편입 삽입 동반 결부 포용 포함 관통 소지 결탁 내포 유지 전부 동반 함유 보유 내장 망라 결속 합류 수반 포함(involve) 합류되어 수렴 이주 정착 포진해 담겨 안착해 존재합니까? 만일 전면 포함되었다면 왜 그렇다고(Why) 보십니까? 혹은 반대로 일부가 유실 삭감 배제 증발 탈락 수축 제거 제외 삭제 축출 단락 축소되어 그렇지 못하게 차단 거부 축출(why not) 도달 결정 삭감 되었다면 대체 또 그 연유 발로 이유는 무엇입니까?
