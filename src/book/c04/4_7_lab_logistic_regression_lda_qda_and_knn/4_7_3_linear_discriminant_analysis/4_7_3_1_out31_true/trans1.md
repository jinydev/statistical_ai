---
layout: default
title: "trans1"
---

[< 4.7.3 Linear Discriminant Analysis](../index.html) | [4.7.4 Quadratic Discriminant Analysis >](../../4_7_4_quadratic_discriminant_analysis/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# **`Out[31]:`** `True` 

If we wanted to use a posterior probability threshold other than 50% in order to make predictions, then we could easily do so.
우리가 모델 판별 예측을 내리기 위해 기존의 보편적인 50% 가 아닌 다른 변형된 기점 값의 사후 확률 스코어 임계치(threshold) 기준선을 사용하기를 절실히 원했다면, 우리는 아주 쉽게 그렇게 수행 구현할 수 있었습니다.

For instance, suppose that we wish to predict a market decrease only if we are very certain that the market will indeed decrease on that day — say, if the posterior probability is at least 90%.
예를 들어 특정 조건하에, 만약 다루는 대상 주식 시장 장세가 특정한 그날 정말로 명백히 필연적으로 하락 예측 방향성(decrease) 으로 접어들 것이라고 우리가 아주 맹목적으로 확신(very certain)하는 특정 경우에만 극히 한정 지어서 — 말하자면 즉 가설로, 산술 계산된 사후 확률(posterior probability) 퍼센트 점수가 최소 발동 조건 90% 이상인 특수 발동 전제 상황 — 확정적인 시장 예측 하락 변동(market decrease) 배팅을 무수히 제한적 통제 한정하여 선별적으로 예측 통보하기를 원한다고 실험 가정해 봅시다.

We know that the first column of `lda_prob` corresponds to the label `Down` after having checked the `classes_` attribute, hence we use the column index 0 rather than 1 as we did above.
우리는 앞에서 데이터 분류 구조 속성체계 모형 지표인 `.classes_` 부품 지표를 추출 확인해 파악해 본 선행 전적이 앞서 있은 후라 이제 변수 `lda_prob` 확률 도출 데이터 덩어리 지표의 그 첫 번째 배열 데이터 축 열(column) 공간 영역이 타깃 예측 판별 지시 라벨인 `Down` 결과 변통 정답 레이블에 논리 상응 대응한다는 것을 이미 파악하여 확실히 압니다. 따라서 우리는 그러한 추출 조작을 위해 위의 이전 상황 기동에서 우리가 앞서 적용 지향 구축했던 대로 타겟 지정 시 1 의 범위 수치가 아닌 또 역전된 다른 배열 인덱스 컬럼 도출 축 번호 인덱스 0을 추출 적용 사용하여 첫 배열의 하위 1번 열 타겟의 통계 지시 값을 추출 지향 타겟으로 사용합니다.

```python
In [32]: np.sum(lda_prob[:,0] > 0.9)
```

```python
Out[32]: 0
```

No days in 2005 meet that threshold!
분석이 판별 산정 결과 2005년의 전수 전체 날들 관측 분석 표본 중에 그 설정한 가혹한 통계 제한 조건인 해당 임계치(threshold) 확률 타점 조작 조건을 충족하는(meet) 해당 날은 1년 중 단 하루 단위조차 기록 존재하지 않습니다(No days)!

In fact, the greatest posterior probability of decrease in all of 2005 was 52.02%.
실제 사실 팩트 통계 지표에 기반을 두면, 2005년 전체 파편 표본 내내 관측 발동된 하락 변동장 (decrease) 예견의 통계 점수 기준 가장 압도적으로 큰 단위인 최대 확률을 보유 점유한 가장 거대한 최고 상위 1등 최대 등극 사후 확률 최댓값은 고작 수치 점유율의 52.02%에 불과했습니다.

The LDA classifier above is the first classifier from the `sklearn` library.
기동 예시 위에서 소개되었던 기본 장착용 저 LDA 분류기(classifier) 장비는 파이썬 전용 부속 모듈 종합 세트인 `sklearn` 라이브러리 연장 패키지 덤불에서 추출 채택하여 선보인 가장 선점 첫 번째 개별 단일 기능 판별 단위 통계 분류기 무기 개체 인공물 표본입니다.

We will use several other objects from this library.
우리는 당분간 향후 이 공구 패키징 라이브러리 부속 세트에서 수많은 그 밖의 다른 수 종류의 이질적 다양한 응용 통계 객체들(objects) 패키징 무기들을 함께 계속해서 발동 기동 추려낼 사용할 것입니다.

The objects follow a common structure that simplifies tasks such as cross-validation, which we will see in Chapter 5.
도출 투입 사용된 해당 개체 통계 객체 구조물 들은 차후 미래의 챕터 5 이론 단원 안에서 우리가 직접 대규모 대면하여 마주하게 될 고차원 응용 전산 과정인 교차 검증(cross-validation) 분석 응용 테크닉과 같은 매우 복잡 귀찮은 반복 통계 수고 전산 연산 프로세스 작업들(tasks) 단위 공정 을 유독 매우 상당하게 무지 아주 간소화(simplifies) 단축시켜 처리 구현해 주는 아주 굳건하고 확고한 그들만의 단일 획일적인 통합 공통 조립 구동 배열 작동 뼈대 구조(common structure) 로직 전제를 똑같이 전부 모조리 부품 불문 예외 없이 다 공유해서 추종 연산 따릅니다(follow).

Specifically, the methods first create a generic classifier without referring to any data.
디테일하게 원리를 파고들자면 콕 집어 명확히 통계 구체적으로(Specifically) 설명해서, 이 통일된 통합 시스템 구동 동작 분석 메서드 파편 규칙들은 코딩 선언 과정에서, 프로그램 구동 외부의 그 어떤 관측 참조 자료 현물 데이터들에도 애초에 연관 짓거나 어떠한 관련 참조(referring) 의존조차 구동 투입 하지 않는 완전히 공허 깡통인 채로 머물고 있는 빈 껍데기 기저 속성의 포괄적이고 전면적 형태인 이른바 제네릭 일반 속성 장비 통계 분류기(generic classifier) 프로그래밍 실체 기틀 을 제일 먼저 프로그래밍 생성 선별 객체로써 출산 프로그래밍 조립합니다.

This classifier is then fit to data with the `fit()` method and predictions are always produced with the `predict()` method.
이 프로그래밍 깡통 객체 생성 빈 껍데기 분류기 통계 기계는 전산 지시 그런 다음에 이어서 비로소 프로그래밍 기저 파편 `fit()` 탑재 반복 조립 훈련 학습 기능 탑재 메서드 기능 스위치 조작과 함께 한정된 지정 외부의 통계 데이터 파편을 구동 투입 받아 거기에 비로소 형태를 조작 강제로 체계 기계 구동 적립 신경망 구조를 기계적으로 강제 학습 강제 형질 적합(fit) 강요 구체화 시킵니다. 그리고 차례대로 궁극적인 신경 작동의 핵심 결괏값 판별 투척 타겟 산출 타점 점수 산출 예측들(predictions) 궤적 지표는 결코 통계 예외 없이 아주 일관되게 모두 무조건 전적으로 기계 표본 발동 `predict()` 연사 작동 사격 예측 발진 사격 조준 메서드 도구 하나 만을 유일 사용하여 결연 확고히 발사 쏘아 올려 기계적으로 최종 일정히 찍어 형태 도출 변환 산출 출력(produced) 산술 결판 생산 되어 도출 표기 됩니다.

This pattern of first instantiating the classifier, followed by fitting it, and then producing predictions is an explicit design choice of `sklearn`.
이러한 아주 극단적으로 일률적이고 획일적인 전형적인 작동 이 아주 정교한 프로그래밍 조립 체계 규칙 시스템 기계적 프로그램 동작 절차 이행 패턴 전제 구조, 즉 논리 연산 제일 첫 시작 먼저 제일 빈껍데기 깡통 모양 뇌 인 통계 형태 분류기 클래스 빈 형틀 껍데기 그 자체를 프로그램 메모리상 기동에 인스턴스화 표본 붕어빵 활성(instantiating) 실질 개체 소환시키고, 그 뒤를 징검다리 적으로 다음 절차에 맞춰 연계 기점 조작해서 거기에 강박적으로 특수한 도출 변형용 외부 타깃 분석 데이터를 투입 쑤셔 부어 넣어 목적 형태 모형을 타점 최적 방향 적합(fitting)하게 집중 훈련 시킨 작동 구동 완료 한 뒤에, 훈련 종료 완료 단절 뒤 마침내 결론을 이행 따라 거기에서 이어서 마지막 도출 산출 결괏값 도출 파편 판별 예측치 통계 점수 최종 채점 결괏값들 을 전면 일정히 사격 발동 기계 생산(producing) 획득 조작 추출 기능 수행 뽑아 수확해 연산 내는 이 기고만장하고 정교한 파이썬 코딩 순차 절차적 동작 연계 작동 구동 작동 체계 패턴 구조 아키텍처 야말로 저 거대 프로그래밍 통계 조작 집단인 `sklearn` 팀의 패키지의 아주 확고부동하고 프로그래밍 내부 체계의 극명한 명시적이고 확정적인(explicit) 전면적 철학 반영 시스템 디자인 설계 구조 기능 확정 선택(design choice) 철학 채택 의도 기술 뼈대 논리 결과물 기저 조작 자체의 핵심 정수입니다.

This uniformity makes it possible to cleanly copy the classifier so that it can be fit on different data; e.g. different training sets arising in cross-validation.
이 아주 극단적인 통계 획일 통일성 기조 잣대의 엄격 고정 구조 일관성(uniformity) 규칙 강압 적용 기능은 그 비어있는 그 빈 속 빈 껍데기에 불과한 기존 최초 빈 깡통 형태 기계 분류기 클래스 프로그래밍 형태 자체 구조 만을 그 통계 성질 오롯이 조작 복사 그 자체로 아주 복사 잔여 오류 티 하나도 없이 전혀 완벽 투명 깔끔하게 통째 도식 그대로 수월히 단순 단조롭게 복제 단일 복사 복사기 무한 복제(copy) 해서 붕어빵처럼 기계적으로 한 없이 이식해 계속 찍어내는 것을 전개 전산적으로 아주 완벽히 문제 없이 수월하게 무구 보장 가능하도록 매끄럽게 통일 기초 바탕 가능성 기틀 만들어 제공 조작 지원 해 줍니다. 그래서 그 성질의 우위 결과적 역산 보장 성립 구조 전개 로서 논리 그것이 예를 들어 향후 초 고난도 교차 검증(cross-validation) 분석 데이터 분기 무한 테스트 시나리오 분산 작동 환경 내에서 불가피하게 시계열 적으로 필수 필연적 발현 끊임없이 창출 연산 분기 무관 발생(arising) 하게 되는 무수히 결 갈래 속성이 완전히 제각각 다르고 쪼개지는 무수한 이질적인 파편 특성 각각 다른 분리 훈련 데이터 배당 세트들(different training sets) 환경 데이터 같은 온전히 태생 형태 속성 기원이 기형 다른 변칙적인 파편화된 여러 개별 다른 독립 테스트 데이터들(different data) 에 조차 무조건 대해서도 일일이 그 뼈대 속 껍데기 기계들을 복제 대량 이식하여 재차 반복적 무한정 치명적 논리 통계 오류 충돌 없이 안전 정률 무결성 으로 그 파편들에 전격 다 적합(fit) 고강도 구동 수치 반복 연계 이식 훈련 무한정 시킬 수 있도록 작동 무한 확장에 특화 완전 작동 보장하도록 아주 안정성 있게 안전하게 통계 설계 기능 구조 기반 을 강제 만들어 지원 줍니다.

This standard pattern also allows for a predictable formation of workflows.
이 아주 단단하게 확립되고 아주 굳건하게 엄수 정립된 파이썬 모듈 데이터 기저 코딩 구조 기반 통일 단일 기능 표준화 기기 조작 뼈대 패턴 아주 명확한 룰 기점 규격 패턴(standard pattern) 시스템 공고 조직 그물 철칙 체계는 데이터 지시 또한, 그에 부수 파생되어 광대한 통계 전산의 거대한 투기 코딩 예측 데이터 조립 및 전체 거시 통계 데이터 파이프라인 개발 공학 코딩 무구 분석 프로그래밍 공정의 총체적 큰 숲 그림상 전체 작업 설계 프로그래밍 기동 단원 조립 복합 과정 구간 전반 에서의 아주 구조가 일목요연하게 확실하고 데이터 통계 연산 논리상 구조 절차 설계 흐름이 예측 보장 투명하게 확연 설계 가능한 치밀 무결성 통계 설계의 일관되고 깔끔 단결된 무한 확장 단일 복합 파이프라인 연계 워크플로(workflows) 시스템 들의 거대 구조 데이터 파이프라인 배열 조립 연계 형성 및 기획 구술 배열 창조(formation) 파판 체계 구축 기획 자체 구조 도 구조적으로 아주 단번에 치명적 충돌 문제 오작동 없이 한 개체 통일 지점 연산 시스템 체제 유지 보장 전개 허용(allows) 개척 창출 이득 해 내장 구현 지원하는 파이썬 고유 프로그래밍 의 아주 결정적인 부가가치 시스템 이점 부가 이점을 마지막 덤 보너스로 부상 달성시켜 창출 조작 선사 제시합니다.
