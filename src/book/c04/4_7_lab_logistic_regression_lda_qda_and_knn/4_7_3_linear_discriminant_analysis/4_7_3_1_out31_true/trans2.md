---
layout: default
title: "trans2"
---

[< 4.7.3 Linear Discriminant Analysis](../trans2.html) | [4.7.4 Quadratic Discriminant Analysis >](../../4_7_4_quadratic_discriminant_analysis/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# **`Out[31]:`** `True` 

If we wanted to use a posterior probability threshold other than 50% in order to make predictions, then we could easily do so. For instance, suppose that we wish to predict a market decrease only if we are very certain that the market will indeed decrease on that day — say, if the posterior probability is at least 90%. We know that the first column of `lda_prob` corresponds to the label `Down` after having checked the `classes_` attribute, hence we use the column index 0 rather than 1 as we did above. 
만약 우리가 무식하게 50% 반반 무 많이 자르기 찍기 칼날 통제 임계값(threshold) 방식 말고 아주 극단적이고 치졸 치밀한 깐 깐 한 조건 커 트 라인 장 벽 을 쳐서 예측 판결을 내리고 싶다면? 이 역시 껌값처럼 파이썬에서 세팅할 수 있습니다. 예를 들어 상상해 보십시오. 우린 개미 털기 지옥장인 하락장(decrease) 베팅 예측에 엄청난 쫄보 공포증 환자라서, "나 진짜 오늘 무조건 100% 떡락할 거 같아!" 라고 덜덜 떨며 극강의 확신(확률 최소 90% 이상) 이 터질 때만 구차하게 하락 팻말(Down) 판정을 들고 싶습니다. 아까 우리가 스파이짓으로 몰래 까본 `classes_` 이름표 속성에서 확률판 `lda_prob` 뭉치의 파이썬 배열판 **첫 번째 왼쪽 기둥(0번째 방렬 열, index 0) 이 구렁텅이 나락(`Down`)의 호적 족보 라인**임을 깨우쳤으니, 이번엔 위 파이썬 라인에서 엉뚱하게 1번 찍지 말고 왼쪽 0번 첫 열 인덱스를 호출 정조준해 검열 검사식 파이썬 코드를 쏩니다.

```python
In [32]: np.sum(lda_prob[:,0] > 0.9)
```

```python
Out[32]: 0
```

No days in 2005 meet that threshold! In fact, the greatest posterior probability of decrease in all of 2005 was 52.02%. 
와우 기가 막히게 허무한 반전 팩트 폭격 결과! 야생 테스트 무대였던 2005년도 365일 거대 테스트 시험 달력 그 어느 개뿔 단 하루 치의 날짜 쪼가리도 감히 이 '90% 확률 떡락 공포 커트라인 벽' 조건에 걸리고 뚫린 적이 요단강 건너 죽을 때까지 아예 단 한 번도 없었습니다! 팩트 체크를 파볼까요? 사실 2005년 저 테스트해 판 통틀어서 이 LDA 기계 놈이 가장 덜덜 떨며 내 뿜었던 최대(가장 확률이 컸던) 맥시멈 최악의 폭락 떡락 사후 예언 공포 지표 스코어가 고작해야 소수점 찔끔 비참한 도토리 확률치인 **52.02%** 가 고작 최대치(greatest) 최고 신기록 폭락 확률이었단 말입니다. (장난합니까?) 

The LDA classifier above is the first classifier from the `sklearn` library. We will use several other objects from this library. The objects follow a common structure that simplifies tasks such as cross-validation, which we will see in Chapter 5. Specifically, the methods first create a generic classifier without referring to any data. This classifier is then fit to data with the `fit()` method and predictions are always produced with the `predict()` method. This pattern of first instantiating the classifier, followed by fitting it, and then producing predictions is an explicit design choice of `sklearn`. This uniformity makes it possible to cleanly copy the classifier so that it can be fit on different data; e.g. different training sets arising in cross-validation. This standard pattern also allows for a predictable formation of workflows.
참고로 방금 여러분이 숨 막히게 만지고 씹고 뜯고 피팅 구동했던 이 LDA 분류 용병 기계 놈이, 여러분이 이 책에서 통계 코딩 거대 병기 무기고인 **전설의 `sklearn` (사이킷런) 라이브러리** 조직에서 맨 처음 조우하게 된 첫 번째 대장급 돌격 분류기 멤버 용사 녀석입니다. 앞으로 우린 이 무기고 패밀리에 속한 수많은 외계인 병기(objects 객체 도구들) 들을 소환할 텐데, 참 다행스럽게도 이 녀석들은 모조리 머리부터 발끝까지 뼛속 부품이 **판박이 공장 라인 일관된 복제 부품 공통 뼈대 패턴 구조물(common structure)** 체제 지배율 아래 도배돼 있습니다. 이게 왜 다행이냐고요? 나중에 피 말리는 5장 가서 배울 지옥의 훈련 '교차 검증(cross-validation)' 무한 뺑뺑이 노가다 코딩 삽질의 미친 난이도를 획기적으로 날로 먹어 단순화 시켜주는 기적의 레시피기 때문이죠. 이 깡패 집단 `sklearn` 용병 체제의 공장 기조는 딱 이렇습니다:
1. 일단 데이터 안 주고 그냥 공껍데기 빈 깡통 거푸집 "Generic 분류기 로봇 껍데기 기기(인스턴스화)" 를 쌩으로 찍어 소환 창조합니다. 
2. 그 빈 로봇 배때지에다가 `.fit()` 이라는 밥주걱 메서드로 훈련용 데이터 생살밥을 강제로 쑤셔 먹이고 퍼먹여 피 튀기게 피팅 훈련 세팅 체질을 갈궈 만듭니다.
3. 배가 빵빵해져 학습 훈련 졸업한 로봇의 뇌 신경 코어 스위치에 항상 한 치 오차 엇나감 없이 절 대 똑같이 영원 불변 `.predict()` 라는 무적 미래 예언 사격 지시 메서드 버 튼 버튼 스펠 주문 펀치로 결과를 영점 사격 발포 사출 예측(predictions) 축 복 배 설 시 킵니다. 
어떻습니까? **장비 창조 소환(인스턴스) -> 훈련 먹방 타격(fit) -> 미래 예언 사격(predict)!** 이 너무나 기계적으로 일관되고 투명한 복붙 공장화 공정 사이클! 이게 바로 `sklearn` 설계자 천재들의 미친듯한 뼛속 강박 명시적 철학 미학 설계도(explicit design choice) 의 위엄입니다. 이렇게 기조가 영구 통일 복붙되어(uniformity) 있으면, 나중에 데이터가 100만 개로 쪼개지는 교차 검증 전장에서도 그냥 로봇 껍데기를 컨트롤+C/V 로 깔끔 산뜻하게 다발성 붕어빵 무한 복제 세공 창조해서 제각기 다른 반찬의 데이터 무한 루프 훈련소에 투항 처넣고 돌리기가 미치도록 수월해지는 마법 극강 효율 편의 전술 폭발 축복 설계입니다. (결론: 얜 이 워크플로우 콤보 장치 하나로 프로그래머 구원자입니다.)

---

## Sub-Chapters

[< 4.7.3 Linear Discriminant Analysis](../trans2.html) | [4.7.4 Quadratic Discriminant Analysis >](../../4_7_4_quadratic_discriminant_analysis/trans2.html)
