---
layout: default
title: "trans2"
---

[< 4.7.3 Linear Discriminant Analysis](../index.html) | [4.7.4 Quadratic Discriminant Analysis >](../../4_7_4_quadratic_discriminant_analysis/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# **`Out[31]:`** `True` 

If we wanted to use a posterior probability threshold other than 50% in order to make predictions, then we could easily do so.
도박의 룰을 바꿔볼까요? 아까는 동전 던지기 판처럼 50%를 커트라인 임계치(threshold)로 삼아서 50.1%만 넘어도 주식이 떡상(Up)할 거라고 냅다 베팅해 버리는 야수의 심장 플레이를 했습니다. 하지만 만약 우리가 쫄보라서 "난 도박이 싫어! 무조건 100번에 90번은 기계가 확실하다고 할 때만 돈을 걸고 싶어!"라고 이 확률 커스텀 룰을 아주 쉽고 쪼잔하게 마음대로 변경 조작(easily do so)할 수도 있습니다. 

For instance, suppose that we wish to predict a market decrease only if we are very certain that the market will indeed decrease on that day — say, if the posterior probability is at least 90%.
예를 들어서 개미 타겟 시나리오로, 우린 피 같은 돈을 지키기 위해 오직 기계 녀석이 "이건 미쳤다. 이 코인, 90% 사후 확률 스코어(posterior probability) 수치 퍼센트로 무조건 오늘 개같이 나락 하락(market decrease) 해서 박살 난다!"라고 완전히 침 튀기며 거의 확신(very certain)에 차 부르짖을 때만 그 확신 범죄 예측 하락 배팅을 확정 발동 짓기를 원한다고 가설을 세워봅시다. 안전제일 구간이죠!

We know that the first column of `lda_prob` corresponds to the label `Down` after having checked the `classes_` attribute, hence we use the column index 0 rather than 1 as we did above.
아까 우리가 `.classes_` 부품 기계 출석부를 털어 확인해 봤으니 이제 우린 통계 표의 비밀을 정확히 꿰차고 꼼수로 압니다. `lda_prob` 객체 확률 명부표의 그 첫 번째 세로 기둥 줄(열) 성적이 바로 '떡락(Down)' 진영의 계산 도출 확률표 점수 배당이란 걸 말이죠. 그래서 우리는 파이썬의 번호 표기 규칙에 따라 아까 상승팀 1번 열을 파밍 타격했던 것과 반대로 이번엔 '0' 번 배당 번째 열(Down 타겟 열) 칼날 추출 타겟 지점을 콕 집어 타격 파밍 필터링 지시를 내려 추출을 겨냥합니다!

```python
In [32]: np.sum(lda_prob[:,0] > 0.9) # 기계야, 확실히 떡락(Down) 할 확률이 90% 가 '넘는' 엄청난 폭락 예견 징후 날짜 데이터 개수 합계(sum) 찾아 카운트해 봐!!!
```

```python
Out[32]: 0 # 에효, 단 한 개도 0건 없음! 
```

No days in 2005 meet that threshold!
보이시나요? 충격적 결괏값 도출 출력. 2005년 미래 예측 테스트 관측 구간의 일일 전장 데이터 그 어떤 특정 단 하루의 거대 날들(No days)도, 그 철벽의 굳건한 90% 이상 떡락 확률 도달이라는 저 안전 신봉 깐깐한 타점 확률 임계치(threshold) 기준선을 뚫고 만족 달성 한 (meet) 날은 통계상 1건도 0번, 절대 도출 존재하지 않습니다! 기계도 90% 신내림을 받을 순 없다는 거죠!

In fact, the greatest posterior probability of decrease in all of 2005 was 52.02%.
충격적인 통계 사실 팩트 체크 폭로 시간! 까놓고 까발려보니 2005년 전체 내내 기간 구간 중에서, 떡락한다고 가장 미친 듯이 확신에 차 핏대 세운 1등 예측 달성 사후 확률 최고조 최댓값 은 겨우 간신히 50 반타작을 넘은 기껏해야 도달 수치 52.02%에 불과했습니다. 시장 방향성은 이놈 기계 따위가 함부로 90% 운운하며 100% 장담 예측 확신할 수 있는 만만한 야생 도박판 호구 속성이 절대 아닙니다.

The LDA classifier above is the first classifier from the `sklearn` library.
기능 기동 소개 알림! 방금 위에서 뼈 빠지게 다뤘던 돌격용 저격 기관총 'LDA 분류기(classifier)' 장비는 파이썬 바닥의 최고 유명 전산 공구 전투 모음 장비 가방인 `sklearn` 라이브러리 부대 패키지 군수품 보급소에서 우리가 소개 차 처음으로 시험 테스트 발동 꺼내 쏴본 가장 첫 번째 기동 판별 무기 모델 소총이었습니다. (무기 체험판 1번)

We will use several other objects from this library.
우리는 당분간 이 험난한 통계 도박 코딩 분류 여정 내내 이 무궁무진한 `sklearn` 라이브러리 가방 안에서 온갖 종류의 엄청나게 수많은 수치 무기 분류 병기 개체 통계 무기 객체들(objects) 타점 총기 및 미사일 도구들을 잔뜩 꺼내 계속 난사 타격 발동 사용할 것입니다.

The objects follow a common structure that simplifies tasks such as cross-validation, which we will see in Chapter 5.
여기서 알아두면 수명 길어지는 코딩 꿀팁 하나! 이 무기 장비들 개체들은 차후 지옥의 심화 훈련 단원인 챕터 5 이론에서 피 튀기게 무한대로 써먹게 될 '교차 검증(cross-validation)' 이라는 살인적인 무한 노가다 타격 반복 모의 훈련 테크닉 전산 조립 공정 작업 단원(tasks) 과정을 파이썬 구조상 말도 안 되게 딸깍 마술처럼 쉽게 단축 조립 단축형 간소화(simplifies) 시켜주는 엄청난 마스터키, 이른바 무기 부품 모듈화 **'규격 통일 장비 조립 공통 장착 뼈대 구조(common structure)'** 설계 철학의 획일성 제식을 똑같이 모조리 추종(follow) 채택하며 따르고 조립 사용됩니다. 일체형 배터리 시스템 같은 거죠!

Specifically, the methods first create a generic classifier without referring to any data.
디테일한 무기 장착 원리 작전 교범! 콕 집어 설명해 명명하자면 (Specifically), 이 최첨단 기동 무기 모듈 메서드 규범 시스템 사용법은 구동 개시 첫 단계에서, 일단 주변에 도구 과녁 훈련용 참 그 어떤 일체의 총알 데이터 관측 참조 자료들 에도 아직은 아무 연관 참견(referring) 의존 연결 따위 접속 간섭을 절대 넣지 말고 깨끗하고 영롱한, 말 그대로 총알 0발 탄창 0개 깡통 상태인 텅 빈 제네릭 무의 백지 베이스 거대 속성 빈 속 껍데기 포괄 속성 초기화 틀 분류기(generic classifier) 프로그래밍 코딩 틀 부품 실체 개체를 모의 컴퓨터 세상 배열에 1차로 제일 선 조립 생성 발진 소환시킵니다. 

This classifier is then fit to data with the `fit()` method and predictions are always produced with the `predict()` method.
이 깡통 무기 분류기 개체는 기동 지시 그 다음에야 비로소 무기 개체 내부 훈련 학습 스위치인 `fit()` 총구 톱니바퀴 조작 스위치 메서드 작동 명령과 버무려져 한정 외부 타겟 훈련 데이터를 전극 데이터 식량으로 투입 수혈 수급 받아 거기에 최적 조준 조작 자신 내부 기계적 형태 뇌 속 신경망 구조를 기계적으로 딥러닝 기조 강제 형질 기계 적합(fit) 스파링 숙달 훈련시킵니다. 그리고 이어서 이 총기의 본질 실전 사격인 궁극의 단말 출력 결정 결괏값 판별 타겟 단서 투척 적중 타점 사격 예측 표적 예측 사격 도출 행동 결과(predictions) 결괏값 통계 수치 표 분출은 결코 다른 꼼수 도구 메서드 구동의 절대 하등 예외 허용 따위 없이 지시 일관되게 항상 오직 전격 `predict()` 결전 발사 작동 타점 사격 발진 추론 조준 전용 메서드 도구 스위치 격발 한 장치만을 유일 사용하여 거사 격발 쏘아 도출 형태로 산출 반환 출력(produced) 생산 도출 표기 뽑혀 나옵니다! 장전(fit) 후 무조건 사격 격발(predict) 이라는 단순 무식 2단 진리죠!

This pattern of first instantiating the classifier, followed by fitting it, and then producing predictions is an explicit design choice of `sklearn`.
이러한 군대 제식 훈련처럼 극단적으로 반복 일률적이고 통일 획일적인 기동 절차 파이썬 작동 정교 프로그래밍 동작 설계 템플릿 연산 구조 구동 패턴 룰, 즉 1번! 묻지도 따지지도 말고 무책임 빈껍데기 깡통 모델 통계 속 껍데기 분류기 설계도 객체 클래스 그 자체 개체를 메모리에 인스턴스화 표본 붕어빵 현실 강제 활성 창조(instantiating) 실질 스폰 소환시키고, 2번! 그 뒤를 차례 징검다리 스텝 밟듯이 절차에 맞춰 연계 콤보 기동 조작해서 구멍에다가 사정없이 실전 외부 훈련 데이터를 쳐 박아 최적 적합(fitting)하게 진단 훈련 뺑기를 돌려 장착 조립 스파링 완료 시킨 뒤, 3번! 그 훈련 종료 스탯 조율 완료 확인 직후 연계 콤보 타격 거기에서 이어서 마지막 실전 타격 결과물 통계 판별 점수 산출 결괏값들 을 전면 사격 기계 생산(producing) 조작 격발 수확 추출해 뽑아 사살해 내는 이 파이썬 무기 기계 스캐줄 3단계 불변 작동 순차 절차적 타격 연계 구동 루틴 패턴 로직 설계야말로 저 천재들 코딩 설계 집단인 파이썬의 `sklearn` 모듈 연합 팀 내부 패키지가 미친 듯이 맹신 고집하는 가장 확고 부동 강력 규칙이자 의도된 설계의 명시적인 지시와 확정 극명(explicit)한 고의적 전면 배포 개발 철학 시스템 뼈대 구조 기반 아키텍처 디자인 디자인 선택 및 맹신 결실(design choice) 조립 메커니즘 의 극치 본질 근간 그 핵심 철학 팩트 자체입니다.

This uniformity makes it possible to cleanly copy the classifier so that it can be fit on different data; e.g. different training sets arising in cross-validation.
이 아주 극단적 고집 수준의 무기 스펙 통계 부품 규격화 표준 통일성 기조 일체 형 구조 제식 일관성(uniformity) 규칙 강압 모듈 설계의 궁극적 미친 장점은 그 초기 기원 틀 속 빈 깡통 도면 그 자체에 불과한 초기 빈 장비 형태 속성 기계 설계 분류기 도면 프로그래밍 형태 자체 모듈 만을 프로그래밍상 오류 버그 하나도 없이 아주 티끌 없이 오롯이 깔끔 깨끗하게 통째 파일로 코드 그대로 한 무제한 수월 조작 단순하게 도면 무한 복제 단일 복사 복제 이식 복사(copy) 배열 생성 해서 복사 붕어빵을 다수로 마구 찍어 이식해 계속 찍어 생성하는 것을 프로그래밍 적으로 구조상 한 치 제약 무구 문제없이 무구 완벽하게 매끄럽게 통일 기초 보장 제공 작동하도록 조작 지원 만들어 가능 허용 이룩해 줍니다! 그래서 모의 그 성질 단순 이식 장착 구조 전개 파급 팩트로서 로직이 활용되어 예를 들어 훗날 최고급 난도 무한정 딥 훈련인 미친 노가다 판 교차 검증(cross-validation) 분석 데이터 시뮬레이터 분기 무한 테스트 시뮬레이션 시나리오 작동 환경 전쟁 통 속에서 훈련 상 불가피하게 무진장 분열 시계열상 필연 코 폭풍 분열 발생 창출 빈발(arising) 하게 되는 훈련 분기 수 천 가지 무수히 결 파편 갈래 속성이 완전히 제각각 다르게 쪼개지는 무수한 이질적인 파편 훈련 적군 특성의 각각 파편 단위 완전히 태생 형태 다른 분리 신생 모델 훈련 데이터 배당 세트들(different training sets) 과 같은 온전히 타겟 속성 환경이 기형 다른 기괴 변칙적인 파편 표본 여러 개별 다른 실전 독립 환경 다른 파편 테스트 데이터들(different data) 환경 전제에 일일히 대해서 조차 도 모조리 한계 불문 문제없이 일일이 그 뼈대 속 껍데기 규격 기계 도면들을 코딩 한 줄로 무한 복제 이식하여 재차 반복적으로 거대 한정 치명적 루틴 논리 통계 오류 충돌 없이 매우 미친 이식 호환성 안전 정률 안정 구조로 무결성 으로 그 모든 미세 파편 전극에 전격 다 오류 없이 모조리 적합 적응 시켜 구동 장착(fit) 고강도 구동 수치 반복 일치 호환성 연계 훈련 대량 반복 공정 시킬 수 있도록 작동 무한 확정 호환성 에 무척 특화되어 완전 무한 호환 작동 가동 보장하도록 아주 안정성 있게 시스템 통계 대량 호환 기원 설계 기반 코드를 무상 강제 만들어 조작 쾌적 자동 지원 줍니다. 이거 진짜 미친 듯이 편한 꿀템 전설 지원 시스템입니다!

This standard pattern also allows for a predictable formation of workflows.
이 아주 사골 국물 단단하게 기초가 확립되고 굳건하게 엄수 조판 정립 표준 제식화된 파이썬 모듈 `sklearn` 라이브러리 만의 특유 데이터 기저 통합 규격 뼈대 단위 조립 기능 통일 표준 작동 패턴 아주 단단한 시스템 기준 룰 기점 제식 규격 패턴(standard pattern) 프로그래밍 시스템 설계 구성 공고 조직 파이프라인 배열 체계는 데이터 지시 또한, 그에 연쇄 파생 부가 콤비네이션 무기 이점 스탯으로서 거대 데이터 세상을 주무르는 통계 전산의 거대한 데이터 자동 코딩 예측 공정 장치 조립 및 전체 거시 통계 복합 자동 공정 데이터 자동 파이프라인 인프라 개발 공학 프로그래밍 공정의 총체적 큰 숲 인프라 단위 숲 거시 그림상 전체 분석 설계 프로그램 프로그래밍 복합 자동 파이프 구축 과정 구간 전반 통계 에서의 아주 코드 작동 구조가 일목요연하게 눈에 보듯 확실하고 기저 연결 데이터 체계 통계 연산 논리상 자동화 구조 작동 흐름 절차가 투명하고 예측 보장 확실히 앞뒤가 설계 파악 연계 전사 가능한 설계 조립 일관 팩트 단결된 무한 자동 반복 연계 단일 복합 파이프라인 연보 복합 체계 워크플로(workflows) 시스템 들의 시스템 연쇄 설계 디자인 공장 자동화 형성 구성 체인 시스템 배열 연계 직렬 창조 개척(formation) 기능 구술 기획 데이터 설계 구축 기획 자동 기저 구조 자체 도 논리적으로 오류 구조적 충돌 오작동 파괴 없이 단번에 치명 타격 한 개체 분열 통일 지점 단일 일련 고속 연산 단일 관통 시스템 자동 전개로 작동 보장 체제 연동 보장 허용(allows) 대량 파이프라인 무구 창출 이득 구현 성취 편의 확장 허용 해 창조 내는 아주 놀라운 코딩 무한 편의 생산성 향상 확장성이라는 파이썬 통계 코딩 분석 시스템 스텝 특유의 아주 결정적인 최종 거대 부가가치 시스템 이점 부가 이점을 마지막 끝판왕 보너스 추가 버프 로 도출 달성시켜 프로그래머 코딩 작업자에게 위대한 결실 로 조작 선사 편익 제공 안내합니다.
