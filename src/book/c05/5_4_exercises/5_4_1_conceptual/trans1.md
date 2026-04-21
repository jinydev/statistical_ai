---
layout: default
title: "trans1"
---

# Conceptual
# 개념 문제

1. Using basic statistical properties of the variance, as well as singlevariable calculus, derive (5.6). In other words, prove that $\alpha$ given by (5.6) does indeed minimize $\text{Var}(\alpha X + (1 - \alpha) Y)$. 
1. 단일 변수 미적으로 비롯되는 연산 작용법과 더불어, 분산 지표의 가장 기초적 통계 속성(properties)을 기반으로 삼고 운용(using)하여 앞의 식 (5.6)을 파생 도출(derive) 해보십시오. 이를 다시 달리 표현하자면(In other words), 식 (5.6)을 통해 주어지는 $\alpha$ 계수가 과연 진정으로 $\text{Var}(\alpha X + (1 - \alpha) Y)$ 식을 극소치로 최소화(minimize) 하는 구조인지 그 사실 여부를 직접 방증 증명(prove) 하라는 뜻입니다.

2. We will now derive the probability that a given observation is part of a bootstrap sample. Suppose that we obtain a bootstrap sample from a set of $n$ observations. 
2. 이제 우리들은 어느 하나의 소관 관측 표본 지정물이 임의의 어느 부트스트랩 관측 샘플 표본 세트 집단 목록 장부 내부의 어엿한 일원 구성원(part of) 자격으로 몸담게 되는(is) 진입 합류 확률값을 거슬러 파생 도출(derive)해 연산해 낼 것입니다. 우리가 전체 $n$ 개의 관측치 표본 요건들로 구성 결성 결집된 하나의 거대 집합 세트체(set)로부터, 한 무리의 부트스트랩 무작위 검증 모집단 표본 무리를 신규 확보 획득(obtain) 도출하게 됐다는 특정 상황을 관측 상정(Suppose) 가정해 두십시오. 

   - (a) What is the probability that the first bootstrap observation is _not_ the $j$th observation from the original sample? Justify your answer. 
   - (a) 제일 으뜸타자 선두 선발 격인 1순위 첫 번째 부트스트랩 추출 관측 표본 단일 요소물이 애당초 원천 발생 기저인 원본 태생 샘플 모집단 출신 명부 지표상의 제 $j$ 번째 순위 대상 관측 요건 개체물이 결단코 **아니게(not) 될** 엇갈림의 불일치 확률은 과연 어느 지수 분율로 수렴합니까? 여러분이 도출 발굴 산출해 고안해 낸 당해 지침 정답치 근원 이면의 타당성을 입증 소명(Justify) 논증하십시오.

   - (b) What is the probability that the second bootstrap observation is _not_ the $j$th observation from the original sample? 
   - (b) 이번에는 서열 두 번째 차례로 지목 발탁 선발된 부트스트랩 대상 관측 표본 단일 계체물이 원본 태생 근원 샘플 군집 명부상 내에 적시 기록된 제 $j$ 번째 기명 대상 관측 개체 주체가 아닐(not) 엇갈림의 회피 어긋남 불일치 탈락 확률 산출 계수율 치수는 얼마입니까?

   - (c) Argue that the probability that the $j$th observation is _not_ in the bootstrap sample is $(1 - 1/n)^n$. 
   - (c) 당해 원천 모집단 제 $j$ 번째 서열 지정 관측 표본 단일 주체가 부트스트랩 생성 결성 편제 샘플 군집 진영 지표 체제 내부권 안에 결코 **포착 흡수 유입(in) 소환 발탁 합류 소속 진입되지 않은 채** 낙마 외곽 여분 미아 이탈 누락 잔류 패스 누락 될 확률이 거듭 $(1 - 1/n)^n$ 수준 치수로 수렴 안착함을 이치 방증 논증 입증(Argue) 하십시오.

   - (d) When $n = 5$, what is the probability that the $j$th observation is in the bootstrap sample? 
   - (d) 만일 $n = 5$ 란 조건 지표가 가동될 때, 저 당해 제 $j$ 번째 발탁 관측 대상 주체 개체가 새로 생성 포집된 부트스트랩 군집 샘플 장부 묶음 속 내부로 전입 유입 침투 등재 포함 귀속 흡수 발탁 선발 소속 포섭 전입 적재 합류 진입 수록 소속 침투 투입 편입 귀속 잔류 머물게 결합 잔류 포션 병합 융합 포속 결성 위치 자리(in)할 진입 귀착 확률 수치는 얼마입니까?

   - (e) When $n = 100$, what is the probability that the $j$th observation is in the bootstrap sample? 
   - (e) 만일 조건이 $n = 100$ 단위 규모일 때, 저 해당 특정의 제 $j$ 번째 명기 관측 개체 대상물이 발탁 생성 결산 조치 도출된 부트스트랩 샘플 군중 묶음 표본 진영(bootstrap sample) 안에 함께 투입 포함 체류 내포 자리 잡고 내재 합류 내장 속해 있을(is in) 결합 편입 소환 흡수 수록 확률은 얼마입니까?

   - (f) When $n = 10,000$, what is the probability that the $j$th observation is in the bootstrap sample? 
   - (f) 이번엔 확장하여 $n = 10,000$ 범위 규모일 때, 저 제 $j$ 번째 대상 지정 관측 개체가 당대 조율 파생 분비 기획 생성 조성 결집된 부트스트랩 풀 샘플 모집 훈련 진영 세트 체제 안에 투과 유입 결합 합류 귀속 흡수 장착 속하여 침투 편입 내포 내재 결치 정착 포함될(in) 귀속 확률 점유 이행 도달 수치는 얼마입니까?

   - (g) Create a plot that displays, for each integer value of $n$ from 1 to 100,000, the probability that the $j$th observation is in the bootstrap sample. Comment on what you observe. 
   - (g) 매차 각 1부터 점진 팽창하여 무려 한도 100,000 컷 수위에 이르는(from 1 to 100,000) 각 층위 연속 궤도 각 단계별 등급 단위의 정수 단위값 규모의 저 $n$ 변인 스펙 규격 조건들 각각에 연계 호응 상응 대응(for each integer value) 관찰 반응하여, 그 매 단계 당시마다 저 제 $j$ 번째 타겟 관측 대상물이 무작위 선발 부트스트랩 진영군 샘플 울타리 바운더리 안쪽에 거뜬 당당히 투입 진입 합류 흡인 선발 귀속 발탁 포섭 소속 합류 진입 당도 체류 편입 무사 안착 포함될(in the bootstrap sample) 확률 예측 전이 상승 낙폭 수치를 세부 구간별 파편별 전시 나열 표출 조명 시각 투사 방영 시연(displays) 도식 차트화 반영 구성해 내는 시각 도면 점 도표 커어브 그래프 플롯 투시 차트 구성 모형(plot)을 단독 형상 일관 제작 가공 생성 축조 도식 도출 설계 구축 작성 고안 창출(Create)해 내십시오. 뒤이어 그 결과 투영 도출 산물 차트 지면 모형에서 스스로 방금껏 귀하가 파악 관측 체감 적발 직시 목도 분석 캐치 포착 발견 관찰 통찰 판독 감별 식별 직관 감지 인지 엿보게(observe) 된 사안 쟁점 맥락 본질 양태 기조 작태 면모 본연 추이 징후 소회 직관 사항 부분 지적 맥락 요결 귀결 대목 단면 형국 사태 소견 감상 느낌 측면에 관해 낱낱이 소회 평론 언급 평가 촌평 논평 지적 기술 의견 부연 첨언 해설(Comment on) 하십시오.

   - (h) We will now investigate numerically the probability that a bootstrap sample of size $n = 100$ contains the $j$th observation. Here $j = 4$. We first create an array `store` with values that will subsequently be overwritten using the function `np.empty()`. We then repeatedly create bootstrap samples, and each time we record whether or not the fifth observation is contained in the bootstrap sample. 
   - (h) 우리는 지금 이 차제 순간(now)부터 규격 규모 사이즈 크기 한도가 도합 $n = 100$ 대 단위인 어떤 한 묶음 개체군 부트스트랩 풀 모집 세트 진영 집단 샘플 묶음 세트장(bootstrap sample) 속에 저 문제적 타깃 기명 제 $j$ 번째 순번 관측 대원 객체물이 기필코 수용 내포 함유 품어짐 포함(contains) 편입 결구 흡입 소속될 단일 개별 관측 주체의 귀속 가능 여부 소속 확률율 빈도 수치를 한 차례 심도 철저 정량적 코드 연산 수리 전산 수치적 단위(numerically) 계측 잣대로서 조사 점검 캐치 판별 수조 사찰 가늠 검증 탐구 역추적 검사 측량 역행 정산 규명 추측 진단 파악 연산 분석(investigate) 기조 추궁 감식 실사 착수해 볼 것입니다. 이 시뮬레이션 지점 구역 위치(Here) 하에서는 고속 $j = 4$ 기준 설정점을 잡습니다. 이를 시도하고자 우리는 최우선(first) 기조로 함수 명령어 수단 `np.empty()` 를 채택 차용 동원 운용(using)하여 그 껍데기만 빈깡통 껍질 임시 공간 잉여 가변 더미 변수로 채워 남개 두었다 향후 추이 후단(subsequently)의 속행 단계를 밟아가며 지속 매 갱신 덮어씌움 순환 반복 수용 재할당 덮어쓰기 기록(overwritten)을 연쇄 속행할 심산 의도를 담아낸 임시 그릇 용기 벡터 껍데기 여분 빈 공극 체제 매개 장치 저장소 공간 명칭 배열 객체물인 `store` 룸 진영 공간을 미리 마련 수리 조잡 조형 준비 할당 생성 개통 창조 확보(create)합니다. 그런 차후 종단 국면 이면 과정 수순으로(then) 지속 끝없이 수만 번 1만 회 차수 반복 뺑뺑 강행 사이클 체제 재모집 부트스트랩군 훈련 추출 샘플 모집 병합 단상 군단들을 끝없이 산출 방조 도출 구성 획득 포집 발굴 포획 취합 모의 연성 추출 생산 창조 모집 유도 복원 맹장 창출(create)해 내며, 매회 돌릴 때(each time) 당시 해당 순환 고리 기점 발자취 파편 회차 순간마다(time) 우리는 저 (0번 1번 2번 3번 다음 인덱스 순열로서의) 제5열 순서 인물 표집인 다섯 번째 타자 관측 요원물 객체가 기적처럼 해당 랜덤 난수 주사위 가동 파생된 당대 부트스트랩 발탁 훈련 픽업 모집 샘플 군단 합류 진입 병합 포섭 세트상에 포함 흡수 함유 머묾 채용(contained) 되었는지 배척 탈락 낙오 배제 버려짐 면제 되었는지 유무 여부 합불 당락 포함 당락 생사(whether or not) 자취 기조 사실 명제 여건 이면 흔적 단서 상황 이치 결말 소출 적중 결과를 꼬박꼬박 꼼꼼히 일일이 수리 누적 파악 기입 수집 누계 전표 보존 추적 결착 기재 검사 집계 기입 저장 입력 기록(record)할 것입니다.

```python
rng = np.random.default_rng(10)
store = np.empty(10000)
for i in range(10000):
    store[i] = np.sum(rng.choice(100, replace=True) == 4) > 0
np.mean(store)
```

Comment on the results obtained. 
방금 귀하가 획득 도출 달성 갈취 수거 산출 연성 분출 확보 환수 입수 취득 발견 적중 달성 채굴 적출 건져 거머쥔 수득 수확(obtained) 계산 환원 결착 산출 연산 종점 결론 도출 결과물(results) 단서 점수 증거 지표 수치 흔적 결과 성과물 현황 파편 결과들에 대해 나름대로 고찰 지적 단평 평가 일갈 코멘트 논평 참견 요약 토로 거론 서술 참견 평설 비평 첨언 해설 단평 촌평 평론 설명 해석 풀이 언급 기술 한마디 평가(Comment on) 하십시오.

3. We now review $k$-fold cross-validation. 
3. 우리들은 이제 분위기 톤을 바꿔 $k$-폴드 분할 교차 검증의 세계를 복습 되짚어 복기 재조명 상기 점검 재검토 회고 고찰 점검 리뷰 반추 시찰(review) 해봅니다.

   - (a) Explain how $k$-fold cross-validation is implemented. 
   - (a) 저 해당 $k$-폴드 분할 갈래 쪼개기 단위 교차 뺑뺑 테스트 검증 시스템 방식 기조가 어떤 메커니즘 구동 원리 연산 절차 방식 기계 이치 과정 절차 원리 수순(how)으로 시현 가동 작동 수행 접합 전개 체현 조립 발현 전사 발달 달성 도입 구사 동원 구동 마련 설계 구현 가동 편성(is implemented) 되는지 그 전개 방식상을 차근 묘사 해설 부연 풀이 논증 논술 서술 진술 표방 설명(Explain)해 보십시오.

   - (b) What are the advantages and disadvantages of $k$-fold crossvalidation relative to: 
   - (b) 아래 열거 지목된 대상 요소 진영 방식들 각각에 나란히 견주어 맞서 대비 대조 비견 상충 빗대 종속 대안 우열 비교할 적에(relative to), 당신이 느끼고 아는 참된 진정한 저 $k$-폴드 쪼개기 조각 검증술 검사 장치 기법의 숨겨진 장점 혜택 메리트 꿀팁 이점 특강 매력 강점 위용(advantages) 과 치명적인 한계 리스크 모순 취약 약점 단점 흠집 제약 굴레 패널티 결함 결점 기피 단점(disadvantages) 사항들은 과연 각각 무엇(What are) 무엇입니까?

      - i. The validation set approach? 
      - (i) 예스러운 고전 단칼 반토막 쪼개기 방식의 반반 무작위 검증 세트 분리 평가 방식 기조(validation set approach)?

      - ii. LOOCV? 
      - (ii) 무식 철저 극한 뺑뺑 지옥 훈련 방식 단 1개만 제외 뺑뺑 척결 무한 반복 (LOOCV)?

4. Suppose that we use some statistical learning method to make a prediction for the response $Y$ for a particular value of the predictor $X$. Carefully describe how we might estimate the standard deviation of our prediction. 
4. 만약에 우리 연구가 모종의 여타 특정 통계상 기계적 학습 가동 공법 수단 모듈(statistical learning method) 장벽 기술들을 한껏 착취 도입 가동 부려 써먹고 응용 차용 발탁 접목(use) 활용 수용함으로써, 오직 딱 하나로 설정 제한 고정된 특정한 입력 스펙 특징 척결 성향 변인 피처 $X$ 값 수치(a particular value of the predictor $X$) 조건에 부응 매칭 적응 대응 결부 화합 종속 조준되어 산출 튀어나올 목표 타겟 조준 환수 성과 판독 결과물 응답 표적치 $Y$ (the response $Y$) 도출에 관대한 어떤 하나의 수치적 예언 가늠 환측 예측치 전망 사출 판별 추세 산출 추단 점수 예견 타진 예언 기대 예측 도출(a prediction) 성과 조성을 빚어 창출해 달성 생성 발발 양산 생성 이룩 성취 확보 조성 유도 도모 창출 수행 가동 구축 해내려(to make) 한다고 치자고 한번 일시적 상황 관측 가정 포장 단언 상정 전제 추측 상상 기획 착안 의심 설계 가설 짐작 예상 간주(Suppose) 해 보십시다. 우리 모델 주체가 이 같은 궤도 하에서 도출 생성해낸 저 당해 타깃 예측 달성 산출 결과치 스코어($our prediction$) 자체가 품고 내재 발산 발동 기인 야기 파생하는 오차 편의 진폭 변위 편향 이격 수준 범위 변동 한계 표준 오차 굴레 척도 오차 편의율 표준 엇나감 펌핑 표준 이격 스코어 찌꺼기 널뛰기 이탈 변위 스펙 표준 이격 변동 요동 편차 오차 흔들림 표준 편차(standard deviation) 위력을 장차 우리가 향후 차례 어떤 작전 원리 방식으로 가늠 측량 수리 계상 타산 짐작 예언 기대 조망 예상 예측 진단 타진 가늠 파악 척도 포착 단측 환측 환산 도출 지적 점검 추측 역산 가늠 예측 타산 진단 추산 가치 예측 추단 추정 연산 계량 측량 추계 예측 추측(estimate) 수리해 낼 방도 가능 역량 심산 길목 가망 전망 타계 가능성 소양 여력 소지 기단 여지 징수 여력 확률 공산 조짐 잠재 한도 방향 위상 도리 구도 여부 방안 싹수 도리 길목 여력 기회 차제 공산 기조 진위 향상 해법 도리 역량(might)이 남아 통용 개척 수립 존재할 수 있는지 체제 방향 과정 순서 척도 방법 과정 경로 여부(how)를 아주 각별히 세심 극도 철저 주의 깊고 깊숙하게(Carefully) 관철 고발 관찰 토로 서술 기명 열거 해설 진술 식별 분해 적시 규명 나열 조명 모사 증명 브리핑 시연 상술 시사 조명 지적 소회 표명 설명 피력 입증 읊어 나열 타진 묘사 상세 서술 해설 설명 증명 묘사(describe) 기술해 보십시오.
