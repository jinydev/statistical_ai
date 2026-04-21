---
layout: default
title: "trans2"
---

[< 2.3.7 Loading Data](../2_3_7_loading_data/trans2.html) | [2.3.9 Additional Graphical And Numerical Summaries >](../2_3_9_additional_graphical_and_numerical_summaries/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.8 For Loops
# 2.3.8 For 루프 (챗바퀴 돌리기)

A `for` loop is a standard tool in many languages that repeatedly evaluates some chunk of code while varying different values inside the code.
끝을 모르는 쳇바퀴 햄스터처럼 파이썬에서 코드를 무한 반복하게 만드는 녀석! 바로 `for` 루프(loop)입니다. 이 녀석은 배열 보따리 안의 값들을 하나씩 차례로 바꿔가면서, 네모난 코드 블록 조각(chunk)을 숨 넘어가게 반복적으로 쥐어짜며 실행(평가)시키는 파이썬 생태계의 가장 위대한 표준 노가다 도구입니다.

For example, suppose we loop over elements of a list and compute their sum.
가령 예를 들어 볼까요? 우리가 숫자 3개가 든 리스트 바구니의 원소들을 쳇바퀴(`loop` 위에 올려놓고 하나하나 꺼내가며 덧셈기(`sum`)로 총합을 낸다고 가정해 봅시다.

```python
In [96]: total = 0
         for value in [3, 2, 19]:
             total += value
         print('Total is: {0}'.format(total))
Total is: 24
```

The indented code beneath the line with the `for` statement is run for each value in the sequence specified in the `for` statement.
윗 코드를 해부해 보죠. `for` 구문 지휘자가 있는 줄 바로 아래에, 들여쓰기(indented, 탭으로 밀어 넣은 여백) 포격을 당해 움푹 파인 코드 덩어리(`total += value`)가 보일 겁니다. 요 녀석은 선언 구문 머리통에 명시된 리스트 시퀀스(`[3, 2, 19]`) 안의 각 숫자가 불려 나올 때마다 한 번씩 처맞듯 실행(run)됩니다. (총 3번 실행되겠죠!)

The loop ends either when the cell ends or when code is indented at the same level as the original `for` statement.
언제 이 잔혹한 노가다가 끝날까요? 더 이상 꺼낼 숫자가 사라져 주피터 셀 장막이 끝나 버리거나, 아니면 우연히 바깥 코드가 다시 제일 첫 줄 구문인 `for` 지휘자와 똑같은 줄 위치(레벨)로 들여쓰기가 풀린 채 원위치 등판하게 되면 그 쳇바퀴는 즉시 작동 종료됩니다.

We see that the final line above which prints the total is executed only once after the for loop has terminated.
그래서 아까 위 코드를 잘 관찰해 보면, 오직 합계 결과물을 딱 출력 프린트하는 맨 밑바닥 마지막 줄 코드(`print(...)`)는 저 3번의 `for` 루프 지옥고가 전부 완전히 종료되고 난 이후에야 들여쓰기가 풀린 채로 유유히 딱 1번만 단연 오롯이 실행되었음을 우리는 단박 알아챌 수 있습니다.

Loops can be nested by additional indentation.
이 루프 지옥은 한 번만 쓸 수 있을까요? 천만에요. 또 들여쓰기 공간을 파고 들어가면 그 쳇바퀴 안에 또 작은 쳇바퀴를 까는 엽기적인 루프 중첩(nested) 지옥 건물도 손쉽게 지어 올릴 수 있습니다.

```python
In [97]: total = 0
         for value in [2, 3, 19]:
             for weight in [3, 2, 1]:
                 total += value * weight
         print('Total is: {0}'.format(total))
Total is: 144
```

Above, we summed over each combination of `value` and `weight`.
보셨나요? 위에서 큰 루프가 `value` 바구니를 돌고, 각 value가 잡힐 때마다 그 안쪽 지하에서 또다시 작은 루프가 `weight` 바구니를 3번 더 도는 미세 컨트롤 노가다 십자포화를 펼쳐, 모든 행렬 조합(combination)에 대한 교차 합산을 깡그리 계산해냈습니다! (총 3 x 3 = 9번의 덧셈 연산!)

We also took advantage of the _increment_ notation in `Python`: the expression `a += b` is equivalent to `a = a + b`.
그리고 아까 루프 돌 때 쓴 단어! 파이썬 짬바가 느껴지는 유용한 축약 _증가(increment)_ 부호 무기를 우리가 적극 차용 활용했는데요. 무식하게 `a = a + b` 라고 치지 않고 멋있게 약어로 `a += b` 라고 치는 기술, 둘은 토씨 하나 안 틀리고 완전히 동일 동등(equivalent)한 작동을 이룹니다.

Besides being a convenient notation, this can save time in computationally heavy tasks in which the intermediate value of `a + b` need not be explicitly created.
이 마법의 `+=` 기호는 단지 타자 치기 편리성뿐만이 아닙니다. 수십억 번 돌아가는 무거운 연산 고통 작업 중에 파이썬이 `a+b` 결괏값을 저장하느라 불필요한 중간 임시 메모리 공간을 어리바리하게 명시적으로 만들고 부수는 막대한 처리 시간 비용까지도 세이브 절약해 줄 수 있는 극강 효율템이란 점을 명심하십시오.

Perhaps a more common task would be to sum over `(value, weight)` pairs.
자, 현실 현장으로 가볼까요? 실무에선 아까처럼 모든 바구니를 십자 교차하는 엽기 짓거리는 잘 안 하고, 두 바구니에서 첫째 놈끼리 짝 맞추고, 둘째 놈끼리 짝을 맞추는 이른바 1:1 `(value, weight) 짝지어 쌍` 동시 더하기(일차원 가중합)가 훨씬 더 평범하게 흔히 벌어지는(common) 노가다 양상일 겁니다. 

For instance, to compute the average value of a random variable that takes on possible values 2, 3 or 19 with probability 0.2, 0.3, 0.5 respectively we would compute the weighted sum.
예를 들면, 주사위를 던졌는데 숫자가 나올 확률이 공평한 게 아니라 2가 나올 확률(0.2), 3이 나올 확률(0.3), 19 복권이 터질 확률(0.5) 이렇게 각기 가중 확률이 걸린 어지러운 통계 난수 변수의 '기대 평균값' 하나를 깔끔하게 연산하고자 쳐볼 때, 우린 당연스레 값과 가중치를 1:1로 맞바꿔 부딪히게 곱해서 더하는 가중치 덧셈(weighted sum) 룰을 필히 강구하게 될 터입니다.

Tasks such as this can often be accomplished using the `zip()` function that loops over a sequence of tuples.
이럴 때 2번 중첩 쳇바퀴 돌리지 말고! 양손에 두 바구니를 쥐고 동시에 하나씩 꺼내 짝지어 주는 파이썬의 중매쟁이 함수인 옷 지퍼 올리기 도구 **`zip()` 함수**를 쓰면 진짜 허탈할 정도로 이런 동시 타격 과정(루프) 작업이 가뿐하게 1타로 성취될 수 있습니다.

```python
In [98]: total = 0
         for value, weight in zip([2, 3, 19],
                                  [0.2, 0.3, 0.5]):
             total += weight * value
         print('Weighted average is: {0}'.format(total))
Weighted average is: 10.8
```
(이 예술을 보세요! 지퍼 `zip()` 가 양쪽에서 2와 0.2를 짝지어서 내보내고, 3과 0.3을 짝지어 내보냅니다! 완벽하죠!)

## String Formatting
## 문자열 틀 폼 깎아 맞추기 포매팅 (Formatting)

In the code chunk above we also printed a string displaying the total.
아까 쳇바퀴 예제 코드의 대미를 장식할 때 보셨겠지만, 우린 무미건조한 숫자만 뽑은 게 아니라 "Total is:" 라는 고상한 텍스트 문자열 간판까지 하나 붙여서 화면에 최종 합산결과(total)를 전시듯 출력했습니다. 

However, the object `total` is an integer and not a string.
하지만 상식적으로 부딪히는 문제! 컴퓨터 세상에선 `total(결과 24)` 은 엄연한 숫자로 된 정수일 뿐, 결코 글자로 된 문자 속성이 아니거든요! 이질적인 놈들끼리 더하면 원래 터집니다!

Inserting the value of something into a string is a common task, made simple using some of the powerful string formatting tools in `Python`.
이처럼 숫자 같은 다른 종족값을 글자 텍스트 문자열 속 빵구 뚫린 빈칸에다 교묘히 구겨 끼워 삽입하는 스킬은 코더들의 밥벌이 스킬입니다. 파이썬에선 이것을 쌈박하게 한 방에 해결해 단조 처리해 주는 무시무시한 힘을 지닌 강력 조립 문자열 포매팅(formatting) 도구들을 보유하고 있어 무척 간단 이롭게 구성됩니다.

Many data cleaning tasks involve manipulating and programmatically producing strings.
나중에 더러운 데이터 청소부(Data cleaning) 노가다 알바를 뛸 때면, 엑셀 텍스트들을 요리조리 칼로 깎아 조작하고 이처럼 프로그래밍 주문을 때려 휙휙 대량 생산 문구 문자열로 뿜어내게 만드는 짓거리가 아주 지독하게 잔뜩 수반되거든요.

For example we may want to loop over the columns of a data frame and print the percent missing in each column.
가령 쏠쏠한 예제를 들어볼까요? 여러분이 어떤 데이터 프레임 컨테이너 속 수십 개의 기둥(열)들을 루프 반복 순회하며 돌아다니면서, 각 기둥 바닥마다 구멍 난 '누락(missing) 결측치 퍼센티지(%) 오염도' 상태 보고서 문구를 줄지어 촥촥 화면에 출력하길 극렬 원할 수도 있습니다.

Let’s create a data frame `D` with columns in which 20% of the entries are missing i.e. set to `np.nan`.
연습 삼아, 안에 든 내용물 항목들 중 정확히 무작위 20% 구획이 처참히 치아 빠지듯 누락 빵구난, 다시 말해 일찍 썩어서 `np.nan` 으로 독점 빵구가 세팅 지정된 임시 연습용 썩은 데이터 프레임 컨테이너 체제 **`D`** 구조망을 하나 이내 생성 창조해 봅시다.

We’ll create the values in `D` from a normal distribution with mean 0 and variance 1 using `rng.standard_normal()` and then overwrite some random entries using `rng.choice()`.
우리는 아까 배운 마법의 지팡이 `rng.standard_normal()` 을 소환해 평균 0과 퍼짐(분산) 1이라는 예쁜 기준의 정규 분포 공장에서 썩지 않은 `D` 내부의 청정 숫자값들을 우선 뽑아 깔아 놓을 겁니다. 그러곤 곧장 확률 조작기 `rng.choice()` 도구를 써서 배열 단 구역에 무작위 테러 타깃 항목을 골라 잡고 블랙홀 결측치 투하를 감행해 무참히 지독한 덮어씌움 폭파 갈이를 단연코 시전해 벌일 겁니다!

```python
In [99]: rng = np.random.default_rng(1)
         A = rng.standard_normal((127, 5))
         M = rng.choice([0, np.nan], p=[0.8, 0.2], size=A.shape)
         A += M
         D = pd.DataFrame(A, columns=['food',
                                      'bar',
                                      'pickle',
                                      'snack',
                                      'popcorn'])
         D[:3]
Out[99]:        food       bar    pickle     snack   popcorn
         0  0.345584  0.821618  0.330437 -1.303157       NaN
         1       NaN -0.536953  0.581118  0.364572  0.294132
         2       NaN  0.546713       NaN -0.162910 -0.482119

In [100]: for col in D.columns:
              template = 'Column "{0}" has {1:.2%} missing values'
              print(template.format(col,
                                    np.isnan(D[col]).mean()))
Column "food" has 16.54% missing values
Column "bar" has 25.98% missing values
Column "pickle" has 29.13% missing values
Column "snack" has 21.26% missing values
Column "popcorn" has 22.83% missing values
```

We see that the `template.format()` method expects two arguments `{0}` and `{1:.2%}`, and the latter includes some formatting information.
위의 이 기막힌 양산 출력 코드를 뜯어보면, `template.format()` 붕어빵 기계 메서드가 자기 입구로 들어올 2명 분의 인자 짝꿍, 즉 변수명 박아 넣을 문자용 `{0}` 빈칸 자리 하나랑 결측률 통계치가 들어갈 숫자 빵꾸 `{1:.2%}` 까지 총 두 개의 대기석을 기대하며 벌리고 입맛을 다심을 봅니다. 여기서 뒤쪽 놈은 덧붙여 모양을 깎을 약간의 장식용 포매팅 설계도 정보 구조까지 앙큼하게 포함하고 장착했네요!

In particular, it specifies that the second argument should be expressed as a percent with two decimal digits.
틀리기 쉬운 저 뒤쪽의 미세 팁! `{1:.2%}` 란 저 얄미운 구조는 딱 "입구로 건네지는 내가 그 두 번째 인수 숫자를 받긴 받을 건데, 그냥 받지 말고 끝에 % 부호를 예쁘게 달고 꼭 소수점 이하 두 자리(.2)까지만 단연코 가위로 잘라서 표출 표현해라!"라고 까다로운 주문 지시를 정밀 지정해 지목하는 구조입니다.

The reference `docs.python.org/3/library/string.html` includes many helpful and more complex examples.
더 변태같이 복잡하고 화려한 문자열 양철통 서식 예제들이 궁금증을 자아낸다면 파이썬 성지 공식 도피처 문서인 `docs.python.org/3/library/string.html` 링크로 순례를 떠가보길 바랍니다. 그곳이 정말 도움이 되고 살벌하게 얽히고 조립된 훨씬 더 많은 복잡 예제 문건 단락들을 단연 수록 모조리 포함하고 있을 참입니다!

---

## Sub-Chapters

[< 2.3.7 Loading Data](../2_3_7_loading_data/trans2.html) | [2.3.9 Additional Graphical And Numerical Summaries >](../2_3_9_additional_graphical_and_numerical_summaries/trans2.html)
