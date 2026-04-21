---
layout: default
title: "trans2"
---

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../trans2.html) | [4.7.7.2 Poisson Regression >](../4_7_7_1_poisson_regression/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.7.1 Out69 1.53E-20

The sum of squared differences is zero.
방금 보신 것처럼 뺄셈 결과를 다 제곱해서 더해봐도 결론은 완벽한 0(zero)! 즉, 옛날 방식 무식한 모델이 뱉어낸 결괏값이나, 억지로 평균 0점을 꼬아서 만든 힙스런 신형 모델 도출 수치 결괏값이나 **기계가 바라보는 정답 자체는 100% 동일하다**는 반전 없는 싱거운 타점 결론(sum of squared differences) 이 코딩으로 증명됩니다.

We can also see this using the `np.allclose()` function:
눈이 아프시다면 굳이 저렇게 뺄셈 곱셈 안 하고 파이썬의 아주 영리한 통계 단골 팩트 체크 스위치 무기인 `np.allclose()`(야! 두 배열 스탯 완전히 오차 없이 다 똑같아? 하고 기계에게 묻는 기능 검증 함수) 를 전면 타격 작동 시켜서(using) 도출 팩트 일치 결론을 바로 깔끔하게 두 눈으로 도출 폭로 목격(see) 할 수도 있습니다!

```python
In [70]: np.allclose(M_lm.fittedvalues, M2_lm.fittedvalues) # "첫 번째 모델 예측 덩어리랑 두 번째 모델 예측 덩어리, 둘 다 100% 완전 똑같은지 기계가 채점해라!!"
```

```python
Out[70]: True # 시스템 왈: "네 주인님! 오차 단 1도 없이 아주 소름 돋게 100% 똑같습니다! (True)"
```

To reproduce the left-hand side of Figure 4.13 we must first obtain the coefficient estimates associated with `mnth`.
이제 본문 공부할 때 봤던 교재 도표 Figure 4.13의 기막힌 시각 지표 좌측 편 그림(left-hand side) 덩어리를 우리가 직접 해커처럼 프로그래밍 코딩으로 자가 복제 재생산 기동 생성 도출(reproduce) 해 볼 겁니다! 그러기 위해서는 반드시 선결 스텝으로, 그 숨겨져 꼬여 있는 월(`mnth`) 정보 파편과 연계된 부품들만 쏙쏙 타점 저격해 통계 계수 산점 추정치 배열들(coefficient estimates) 을 개별 독립 핀포인트로 표에서 온전하게 획득 단독 추출 뽀려와야만(obtain) 합니다.

The coefficients for January through November can be obtained directly from the `M2_lm` object.
그런데 딜레마가 있습니다. 추출 시 1월(January) 부터 11월(November) 지표 단락까지의 계수 점수 정보들은 아주 쉽고 착하게 기판 변수 파편 `M2_lm` 결과 객체 배열(object) 표면에 다 대놓고 기재되어 있어서 그냥 아무 추가 연산 왜곡 작동 장난 없이 곧바로 단독 직접 완전 획득 쏙 뽑아서 분리 도출(obtained directly) 추출 복사해 버리면 끝입니다.

The coefficient for December must be explicitly computed as the negative sum of all the other months.
하지만 문제는 아까 말했듯이 표에서 증발해버린 누락된 12월(December)! 이 숨어버린 단절 누락 은닉 계수 단일 수치는 당황하지 말고 우리가 아까 배운 마법의 규칙! 즉 논리적으로 **나머지 모든 1~11월의 도출된 총합 점수 부분(sum) 을 다 합친 다음에, 맨 마지막에 마이너스 역전 부호 일격(-) 을 빵! 먹여서(negative)** 논리적 산점 역산 기법 조작 절차로 명시적으로 프로그래머가 손수 단절 직접 수동 스크래치 계산 도출 연산 억지 조작 편입 작전(explicitly computed) 을 가해서 강제 부활 산출 도출 복원 회수 수리를 해내야만 합니다.

We first extract all the coefficients for month from the coefficients of `M2_lm`.
자, 작전 개시! 통계 연산 과정에서 제일 통계 먼저 조작 `M2_lm` 결과 기판의 15개나 되는 복잡한 산재 표 배열 파편 혼합 계수들 무더기 더미 속에서, 다른 이상한 평일, 기온 점수 다 쳐내고 오직 통계 월별(`mnth` 라는 텍스트 단어가 붙은) 기간 한정 계수 표상 파편 들만 을 쏙쏙 텍스트 필터링 조건 지정 조작하여 개별 단독 우선 부분 스캔 추출 단절 분열 흡수(extract) 처리 해냅니다.

```python
In [71]: coef_month = S2[S2.index.str.contains('mnth')]['coef'] # "야 S2 표! 너 안에 'mnth' 글자 들어간 놈들 점수만 싹 다 긁어와!"
         coef_month
```

```python
Out[71]: mnth[Jan]    -46.0871 # (오! 1월부터 11월까지 점수만 깔끔하게 빼돌림 성공!)
         mnth[Feb]    -39.2419
         mnth[March]  -29.5357
         mnth[April]   -4.6622
         mnth[May]     26.4700
         mnth[June]    21.7317
         mnth[July]    -0.7626
         mnth[Aug]      7.1560
         mnth[Sept]    20.5912
         mnth[Oct]     29.7472
         mnth[Nov]     14.2229
         Name: coef, dtype: float64
```

Next, we append `Dec` as the negative of the sum of all other months.
다음 은닉 조각 12월 점수 살리기 연산 융합 단계(Next)! 우리는 방금 빼돌린 나머지 산출 모든 타 1~11월들(all other months) 계수 추출 결과 도출 배열 점수들을 `sum` 명령어로 다 통으로 합산한 뒤, 그 산술 결과 수치 표면에 일격으로 마이너스 역전 부호 음수 기점 일격(-) 조작타(negative)를 가한 강제 산술 확증 값(이게 바로 12월 점수죠!)을 단절 은닉된 타점 `Dec`(12월) 지표 명칭 꼬리표 네임택을 달아 배열 기판의 맨 하단 끝에 전격 수동 뽄드 덧대기 병합 결합 꼬리 추가 결합(append) 구조 억지 조작 봉합 접합을 감행합니다!

```python
In [72]: months = Bike['mnth'].dtype.categories
         coef_month = pd.concat([
             coef_month, # 좀 전에 빼돌린 1~11월 덩어리 밑에...
             pd.Series([-coef_month.sum()], # 12월 점수(-sum)를 억지로 계산해서 만든 덩어리를...
                       index=['mnth[Dec]']) # 이름표는 12월로 붙여서 강제 수동 접합(concat) 시켜버린다!!
         ])
         coef_month
```

```python
Out[72]: mnth[Jan]    -46.0871
         mnth[Feb]    -39.2419
         mnth[March]  -29.5357
         mnth[April]   -4.6622
         mnth[May]     26.4700
         mnth[June]    21.7317
         mnth[July]    -0.7626
         mnth[Aug]      7.1560
         mnth[Sept]    20.5912
         mnth[Oct]     29.7472
         mnth[Nov]     14.2229
         mnth[Dec]      0.3705 # 짜잔! 마법처럼 사라졌던 12월 점수(0.3705)가 맨 밑바닥에 부활 장착 환생 완료!
         Name: coef, dtype: float64
```

Finally, to make the plot neater, we’ll just use the first letter of each month, which is the 6th entry of each of the labels in the index.
마지막 피날레! 코딩 시각 데이터 조작 절차 발동(Finally)! 최종 복원된 점수를 가지고 그래프(plot) 패널 판을 그릴 건데, 엑스축 밑에 `mnth[Jan]`, `mnth[Feb]` 이런 식으로 글자 다 적으면 길어서 촌스럽고 화면상 지저분하니까 좀 더 단절 산뜻하고 이쁘고 외형 미관상 더 개성 있게 축약 생성 깔끔 구성(make neater) 하기 임의 지시를 위해서 꼼수를 부립니다. 우리는 표기상 각 분리 개별 파편 월 글자의 스펠링 영단어 중에 제일 앞에 위치한 기점 첫 번째 개별 문자 낱단 항목 스펠링 기호(first letter) 마킹 알파벳 요소 (예: Jan 이면 'J' 하나!)만 을 단독 분리 선택 조작 발취해 라벨로 박아 사용(use) 할 것입니다.

```python
In [73]: 
fig_month, ax_month = subplots(figsize=(8, 8)) # "8x8 사이즈 빈 캔버스 도화지 쫙 펴라!"
x_month = np.arange(coef_month.shape[0])
ax_month.plot(x_month, coef_month, marker='o', ms=10) # 1~12월 점수(coef_month)를 들이붓고 굵은 왕 점('o')으로 그려!!
ax_month.set_xticks(x_month)
# 밑에 꼼수 발동! mnth[Jan] 낱말에서 파이썬 서열 인덱스([5], 즉 6번째인 J, F, M...)만 뜯어서 이쁘게 라벨링 박아 넣어라!! 
ax_month.set_xticklabels([l[5] for l in coef_month.index], fontsize=20) 
ax_month.set_xlabel('Month', fontsize=20)   # 엑스축 이름은 Month!
ax_month.set_ylabel('Coefficient', fontsize=20); # 와이 축 이름은 거창하게 Coefficient!
```

Reproducing the right-hand plot in Figure 4.13 follows a similar process.
자, 아까 본문 도표 Figure 4.13 의 우측 편 조작 도출 연개 시간에 따른 그래프(right-hand plot) 영역을 다시 우리 손으로 시각 프로그래밍 복제 재생산 단절 생성 작전(reproducing) 코드로 카피 구현해 내는 지시 작동 방식 역시! 방금 우리가 미친 듯이 전개한 월별 점수 복원 방식과 완벽하게 데칼코마니 상응하는 상호 유사한 코딩 복원 공정 패턴 체제 파이프라인 절차들(similar process) 조작 논리 매뉴얼을 100% 동일 수반 추적(follows) 병용 복붙 전개합니다.

```python
In [74]: 
coef_hr = S2[S2.index.str.contains('hr')]['coef'] # 시간(hr)들만 모조리 뜯어!!
coef_hr = coef_hr.reindex(['hr[{0}]'.format(h) for h in range(23)])
coef_hr = pd.concat([
    coef_hr,
    pd.Series([-coef_hr.sum()], index=['hr[23]']) # 안 보이는 맨 막판 시간(23시) 놈을 마이너스 타격(-sum) 연산으로 복구해서 꼬리에 접합 수술!!
])
```

We now make the hour plot.
부품은 완벽히 복구 조립 장전 완료됐다! 이제 우리는 모든 시간이 융합 확정 복구된 통합 시간 데이터 점수 장부 도출 스펙 치로 이제 최종 그래프 시각화 타깃 목적인 **시간 도출 연계 그래프(hour plot)** 도표 마스터 패널 캔버스를 전면 웅장하게 단독 생성 확립 드로잉 구축 단절(make) 산점 도출합니다! 쏴라!!

```python
In [75]: 
fig_hr, ax_hr = subplots(figsize=(8, 8)) # 또 8x8 사이즈 빈 캔버스 도화지 펴!! 세팅!
x_hr = np.arange(coef_hr.shape[0])
ax_hr.plot(x_hr, coef_hr, marker='o', ms=10) # 0시부터 23시까지 복구한 점수를 들이붓고 타격해 그려!!
ax_hr.set_xticks(x_hr[::2])
ax_hr.set_xticklabels(range(24)[::2], fontsize=20) # 글씨 너무 많으니까 이쁘게 [::2] 2칸씩 짝수 시간만 점프 띄어쓰기해서 하단 라벨에 박아! 
ax_hr.set_xlabel('Hour', fontsize=20) # 엑스축 이름표 세팅! Hour!
ax_hr.set_ylabel('Coefficient', fontsize=20); # 와이 축 이름표 세팅! 점수 지표!! 축하합니다!
```

---

## Sub-Chapters

[< 4.7.7 Linear And Poisson Regression On The Bikeshare Data](../trans2.html) | [4.7.7.2 Poisson Regression >](../4_7_7_1_poisson_regression/trans2.html)
