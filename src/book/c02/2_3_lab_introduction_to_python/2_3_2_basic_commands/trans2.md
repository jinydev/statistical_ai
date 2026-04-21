---
layout: default
title: "trans2"
---

[< 2.3.1 Getting Started](../2_3_1_getting_started/trans2.html) | [2.3.3 Introduction To Numerical Python >](../2_3_3_introduction_to_numerical_python/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.2 Basic Commands

# 2.3.2 기본 명령어 (파이썬 옹알이 떼기)

In this lab, we will introduce some simple `Python` commands.
이번 훈련소에서, 우리는 파이썬의 가장 기초적인 몇 가지 애교만점 초간단 명령어(commands)들을 쓱~ 소개해 드립니다. 아따 맘마 옹알이 떼는 수준이니 너무 긴장 마세요!

For more resources about `Python` in general, readers may want to consult the tutorial at `docs.python.org/3/tutorial/`.
진짜 파이썬 기초만 수백 페이지 파보고 싶은 찐 문과생 독자 여러분은, 파이썬 공식 교과서인 `docs.python.org/3/tutorial/` 로 살짝 길을 틀어 그쪽 튜토리얼을 곁들여 참고(consult)하고 오셔도 좋습니다.

Like most programming languages, `Python` uses _functions_ to perform operations.
여느 콧대 높은 프로그래밍 언어들처럼, `Python` 역시 지저분한 노가다 작업을 깔끔하게 처리하기 위해 멋진 이름이 붙은 **_함수들(functions)_** 이라는 믹서기 테크닉을 애용합니다.

To run a function called `fun`, we type `fun(input1, input2)`, where the inputs (or _arguments_) `input1` and `input2` tell `Python` how to run the function.
예컨대 요술 상자 `fun`이라는 함수를 작동(run)시키고 싶다? 그럼 그냥 우리 키보드로 `fun(사과, 바나나)` 라고 치기만 하면 됩니다! 요 괄호 안에 던져 넣는 불쌍한 제물들(input1, input2), 그 이름하야 고상하게 부르는 **_인자(arguments)_** 가 바로 `Python`에게 "이 요술 상자를 어떻게, 무슨 재료로 돌려버릴까?" 라고 속사포 지시를 내리는 핵심 칩셋 역할을 합니다.

A function can have any number of inputs.
이 함수 요술 믹서기 구조는 고정된 틀이 없습니다. 그냥 인자를 1개만 넣어도 되고, 100개를 마구 쑤셔 넣어도 되는(any number of inputs) 자유 영혼입니다!

For example, the `print()` function outputs a text representation of all of its arguments to the console.
예컨대 앵무새 같은 `print()` 함수 믹서기에다 재료들을 다 우겨 넣으면, 그놈은 콘솔(검은 화면) 앞으로 모든 인자들의 목소리를 텍스트 글자로 예쁘게 토해내 줍니다(outputs).

```python
In [1]: print('fit a model with', 11, 'variables')
fit a model with 11 variables
```

The following command will provide information about the `print()` function.
뒤따르는 다음 신기한 명렁어 조작은 바로 저 `print()` 믹서기 함수에 대한 "제조사 고객센터 설명서" 같은 아주 쏠쏠한 꿀 정보(information)를 파이썬 화면 상에 친절히 띄워 줍니다.

```python
In [2]: print?
```

Adding two integers in `Python` is pretty intuitive.
단연코 `Python` 세계에서 두 개의 숫자(정수) 묶음을 더하는 계산은 스마트폰 계산기 치듯 눈 감고도 칠 만큼 초등학교 수학처럼 극강으로 친숙하고 직관적(intuitive)입니다!

```python
In [3]: 3 + 5
Out[3]: 8
```

In `Python`, textual data is handled using _strings_.
하지만 숫자가 아닌 글자 데이터를 다룰 땐 어떡하냐고요? `Python` 구조 안에서는 온갖 문자, 글귀 같은 텍스트 기반 데이터(textual data)는 늘 따옴표 목줄로 묶어둔 **_문자열(strings)_** 이라는 포장용 조작 수단을 사용해 제어합니다.

For instance, `"hello"` and `'hello'` are strings.
한 가지 꿀팁을 드리죠. 쌍따옴표 `"hello"` 형태든, 홑따옴표 `'hello'` 형태든 파이썬 눈에는 둘 다 차별 없는 평등한 문자열들입니다. 네, 쌍이든 홑이든 땡깡 부리지 않고 똑같이 읽어 들입니다.

We can concatenate them using the addition `+` symbol.
게다가 놀랍게도 문자열들끼리는 더하기 합 연산용 십자가 `+` 기호를 써서 기차 줄처럼 척척 한 덩어리로 붙여 이음 연쇄(concatenate)시켜버릴 수도 있습니다! (글자들도 더하기가 된다고요!)

```python
In [4]: "hello" + " " + "world"
Out[4]: 'hello world'
```

A string is actually a type of _sequence_: this is a generic term for an ordered list.
사실 문자열(string)이라는 놈의 숨은 정체는 알고 보면 **_시퀀스(sequence, 일렬 기차)_** 속성의 한 일원입니다. 시퀀스란? "순번표를 뽑고 줄을 서 있는 데이터 조각들의 집합체(ordered list)"를 뭉뚱그려 부르는 통계학자들의 고상한 포장 용어입니다.

The three most important types of sequences are lists, tuples, and strings.
파이썬 제국을 지배하는 이 순서 기차 삼형제의 가장 중요한 3대장 타입은 바로! 모양이 바뀔 수 있는 **리스트(lists)**, 단단한 바위 같은 **튜플(tuples)**, 그리고 방금 배운 글귀 무리 **문자열(strings)** 입니다.

We introduce lists now.
자, 그중에서도 최고 먹이사슬 위인 **리스트(lists)** 박스를 이제 화려하게 소개하겠습니다.

The following command instructs `Python` to join together the numbers 3, 4, and 5, and to save them as a _list_ named `x`.
아래에 등장할 기막힌 코드는 `Python` 노예에게 아주 구체적인 명령을 내립니다: "어이, 파이썬! 당장 숫자 3, 4, 5를 한데 모아 묶어서 챙기고, 그걸 통째로 널찍한 **_리스트(list)_** 바구니에 담은 뒤 겉면에 쓱쓱 `x`라는 이름표를 붙여 평생 저장해 둬!"

When we type `x`, it gives us back the list.
그리고 나서 우리가 명령창에 하찮게 그저 `x` 라고 치고 엔터를 딱 때리면(type), 이 똑똑한 비서는 보란 듯이 방금 포장 저장해 뒀던 그 리스트 통째 바구니 결괏값을 우리에게 획득 반환해 넘겨 돌려줍니다(gives us back).

```python
In [5]: x = [3, 4, 5]
        x
Out[5]: [3, 4, 5]
```

Note that we used the brackets `[]` to construct this list.
조심, 유의 꿀팁! 이 마법 바구니 리스트를 구동 생성 조립하기 위해서 우리는 반드시 저 각진 네모 대괄호 조각 `[]` 을 양옆 앞뒤로 철통같이 에어랩 포장해야 한단 사실에 주의(Note)하십시오! 

We will often want to add two sets of numbers together.
자, 이제 우리는 심심찮게 종종 숫자들로 묶인 두 개의 바구니 세트(집합)들끼리 통째로 덧셈 연산을 하고 싶어 미칠 지경이 될 겁니다. (수학 시간 벡터 더하기처럼 말이죠.)

It is reasonable to try the following code, though it will not produce the desired results.
비록 안타깝게도 그 계산 시도가 우리가 애초에 침 흘리며 내심 원했던 뭉친 합산 기댓값을 생산 구축해 내지 못할망정, 그래도 한 번쯤 다음 코드를 직접 용감하게 시도(try)해 보는 행위는 일선 합리적인 삽질에 속합니다!

```python
In [6]: y = [4, 9, 7]
        x + y
Out[6]: [3, 4, 5, 4, 9, 7]
```

The result may appear slightly counterintuitive: why did `Python` not add the entries of the lists element-by-element?
어라? 얻어터져 나온 소산 똥망 결과가 우리 직관에 살짝(slightly) 뒤틀려서 굉장히 이상하게(counterintuitive) 보일 수 있습니다! 어째서 멍청한 `Python` 언어 지표 체계는 두 리스트 바구니의 1번, 2번 배열 칸 항목끼리 나란히 (3+4), (4+9) 요소 대 요소로(element-by-element) 지능적으로 산술 덧셈 합산을 하지 않고 저 따위 기차 놀이를 한 걸까요?

In `Python`, lists hold _arbitrary_ objects, and are added using _concatenation_.
이게 바로 `Python` 리스트들의 무지막지한 융통성 때문입니다! 이 바구니들은 꼭 숫자뿐만이 아니라 온통 잡다하고 _임의적인(arbitrary)_ 속성 객체(글자, 그림, 사과 등)들마저 무던히 다 쓸어 담기 때문에, 더하기(+)를 써버리면 수학 덧셈이 아니라 그저 글자 잇기처럼 **_연립 연쇄 연결 기차놀이(concatenation)_** 로 뒤에다 풀칠해서 이어 붙여버리기 일쑤인 성질 탓입니다.

In fact, concatenation is the behavior that we saw earlier when we entered `"hello" + " " + "world"`.
아하! 사실 저 무식한 연단 연쇄 이어 붙이기 행동(behavior) 패턴은요, 초반에 우리가 `"hello" + " " + "world"` 구문을 타건 입력했을 때 신기하다며 눈으로 직접 목격하고 즐겼던 바로 그 행위 구조 특성과 토씨 하나 안 틀리고 똑바로 일치합니다!

This example reflects the fact that `Python` is a general-purpose programming language.
어찌 보면 이런 사소한 삽질 실전 예제 하나만 봐도, 기저에 깔린 저 `Python`이라는 놈 자체가 그저 숫자만 만지는 계산기가 아니라 온 세상을 아우르는 다용도 보편 일반-목적적(general-purpose) 범용 프로그래밍 언어 생태계라는 거시적인 진실을 오롯이 시사 반영(reflects)해 주는 겁니다.

Much of `Python`’s data-specific functionality comes from other packages, notably `numpy` and `pandas`.
그럼 우리는 평생 벡터 수학 개무시 덧셈도 못 쓰냐고요?! 아닙니다! 그 구멍 난 데이터 특화형 만능 수학 처리 기능성(data-specific functionality)들의 대부분은 착한 외부 조력자 패키지, 특히 데이터계의 양대 산맥인 **`numpy`** 와 **`pandas`** 모듈로부터 수혈받아 추출되어 멋지게 공급(comes from)됩니다! 

In the next section, we will introduce the `numpy` package.
결국 이어진 다음 대망의 섹션 단락에서, 우리는 이 숫자 연산계의 척척박사 주축 모듈인 파워 패키지 **`numpy`** 를 마침내 여러분께 소개 도입해 선사할 것입니다! 기대해 주세요!

See `docs.scipy.org/doc/numpy/user/quickstart.html` for more information about `numpy`.
당면 기초 수학 천재 패키지인 `numpy` 기술에 관한 매뉴얼 지식 차원의 깊은 정보들을 소망 원하신다면 묻지도 따지지도 말고 공식 문단 링크인 `docs.scipy.org/doc/numpy/user/quickstart.html` 주소를 웹 브라우저에 타건해 직접 탐독(See)해 보실 걸 권합니다!

---

## Sub-Chapters

[< 2.3.1 Getting Started](../2_3_1_getting_started/trans2.html) | [2.3.3 Introduction To Numerical Python >](../2_3_3_introduction_to_numerical_python/trans2.html)
