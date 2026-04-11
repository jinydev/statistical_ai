---
layout: default
title: "index"
---

# _2.3.2 Basic Commands_

# _2.3.2 기본 명령어_

In this lab, we will introduce some simple `Python` commands.

이 실습에서, 우리는 약간의 단순한 `Python` 명령어들을 도입해 소개할 것입니다.

For more resources about `Python` in general, readers may want to consult the tutorial at `docs.python.org/3/tutorial/`.

일반적인 `Python`에 관한 더 많은 자료 자원들을 살펴 확인하기 위해서, 독자 여러분은 `docs.python.org/3/tutorial/` 도달 위치에 제공 분포된 튜토리얼을 곁들여 참고하고자 원할지도 모릅니다.

Like most programming languages, `Python` uses _functions_ to perform operations.

대부분의 프로그래밍 언어들처럼, `Python`은 조작 연산들을 동작 수행하기 위해 여러 _함수들(functions)_ 을 기용 사용합니다.

To run a function called `fun`, we type `fun(input1, input2)`, where the inputs (or _arguments_) `input1` and `input2` tell `Python` how to run the function.

`fun`이라 호출 지정 명명된 함수 단위 하나를 실행 활성화 구동시키기 위해, 단연 우리는 키보드 텍스트 `fun(input1, input2)`를 조작하여 입력 결합 타이핑하며, 이곳에서 입력값들 (또는 부가적 명칭인 _인자들(arguments)_) 즉 이 `input1`과 `input2`는 어김없이 `Python`에게 어찌 당 함수를 단연 실행시킬지 지시 도출해 말해 줍니다.

A function can have any number of inputs.

하나의 함수 모델 구획 구조는 그 단연 임의의 개수의 입력값들을 항시 지녀 가질 수 있습니다.

For example, the `print()` function outputs a text representation of all of its arguments to the console.

예를 들어, 그 거론된 `print()` 생성 함수는 자신에게 배정된 모든 인자 속성들의 텍스트 기반 표현을 결과로써 콘솔 화면으로 출력해 내게 됩니다.

```python
In [1]: print('fit a model with', 11, 'variables')
fit a model with 11 variables
```

The following command will provide information about the `print()` function.

제시되어 따르는 다음 명령어 구역은 `print()` 함수 구조 단위에 연관된 부연 정보를 나타내 지원 제공할 것입니다.

```python
In [2]: print?
``` 

Adding two integers in `Python` is pretty intuitive.

단연 `Python` 언어 구조 내부에서 두 개의 숫자 정수들을 합해 더하는 과정은 아주 눈에 띄게 직관적입니다.

```python
In [3]: 3 + 5
Out[3]: 8
```

In `Python`, textual data is handled using _strings_.

해당 `Python` 구조 안에서, 다수 텍스트 기반 데이터 형질은 늘 _문자열들(strings)_ 단위 구획들을 사용하여 제어되고 조작 도달 다루어집니다.

For instance, `"hello"` and `'hello'` are strings.

예를 한 가지 들어 보자면, `"hello"` 형상과 `'hello'` 지문 쌍 구획은 모두 함께 문자열들입니다.

We can concatenate them using the addition `+` symbol.

우리는 이들을 더하기 합 연산용 `+` 심볼 기호를 동원 사용하여 함께 한 덩이로 이음 연쇄시킬 수 있습니다.

```python
In [4]: "hello" + " " + "world"
Out[4]: 'hello world'
```

A string is actually a type of _sequence_: this is a generic term for an ordered list.

결과적으로 하나의 문자열 덩이는 사실상 곧 한 유형적 부류의 _시퀀스(sequence)_ 에 단언 속합니다: 왜냐하면 이것은 배열된 질서 순서를 갖는 정렬된 리스트 목차를 위하여 존재하는 하나의 일반화된 포괄 지칭 용어이기 따름입니다.

The three most important types of sequences are lists, tuples, and strings.

전반적 구조 시퀀스의 세 가지 가장 두루 중요한 주력 속성 타입들은 곧 리스트들, 튜플들, 그리고 거론 문자열들입니다.

We introduce lists now.

우리는 이제 저 리스트 구조들를 소개에 올립니다.

The following command instructs `Python` to join together the numbers 3, 4, and 5, and to save them as a _list_ named `x`.

뒤 번에 따를 이 다음 명령어 조작 규칙은 단언 `Python` 콘솔로 하여금 숫자들 3, 4, 그리고 5를 함께 나란 결합시키도록, 그리고 나란한 그것들을 `x`라는 지명 이름 지어진 단독 _리스트(list)_ 구조체로 저장 확보시키도록 일동 지시 내립니다.

When we type `x`, it gives us back the list.

우리가 문자 구문 `x`를 조작 기입 타이핑할 때, 이것 조치 실행 본연은 우리에게 저 본원적 리스트 전체 배열을 획득 반환해 넘겨 돌려줍니다.

```python
In [5]: x = [3, 4, 5]
        x
Out[5]: [3, 4, 5]
```

Note that we used the brackets `[]` to construct this list.

이 도출 리스트를 구동 생성 형성 축 조립하기 위한 수단으로써 우리가 대괄호 형태들 조각 `[]` 을 이용해 일체 동반 사용했음에 주의로 유의하십시오.

We will often want to add two sets of numbers together.

우리들은 심심찮게 때때로 종종 숫자들로 수결 묶인 두 개의 결집 세트 집합들을 나란 고이 함께 도두 집결 더하기를 단연금 원할 시점이 오게 될 것입니다.

It is reasonable to try the following code, though it will not produce the desired results.

비록 그러한 행위 도출 결과 결실이 감히 기대 소망했던 온상 결과들을 일률 생산 구축해 내지 아예 않을지라도, 그래도 다음 제시 코드를 작히 직접 고스란히 시도 투사 해보는 행위는 일선 합리적 판단 행위에 속합니다.

```python
In [6]: y = [4, 9, 7]
        x + y
Out[6]: [3, 4, 5, 4, 9, 7]
``` 

The result may appear slightly counterintuitive: why did `Python` not add the entries of the lists element-by-element?

얻은 소산 결과는 아마도 단면 약간 직관적 상식 이면의 역상 구도로서 직관에 상당히 반하여 출현되어 보일지도 당면 모릅니다: 그 왜 어찌하여 `Python` 언어 지표 체계는 두 당 리스트들의 기입 요소 항목들을 항시 낱낱이 각 항목 상호 요소-대-요소로 합해 더하지 않았을까요?

In `Python`, lists hold _arbitrary_ objects, and are added using _concatenation_.

상기 언어 규약 `Python` 규칙상 안에서, 이 리스트 규합 덩이들은 온갖 다수 _임의의(arbitrary)_ 임의적 속성 객체들을 그 자체 무던히 쥐고 포함 지니며, 그러다 즉 나아가 이 이들은 _연립 연쇄 단위 구조(concatenation)_ 연산 규합 방법을 적용 동원 사용하여 결집 되어 부가 더해집니다.

In fact, concatenation is the behavior that we saw earlier when we entered `"hello" + " " + "world"`.

사실, 이 일컫는 단원 연쇄 연결은 일찍이 당초 우리가 `"hello" + " " + "world"` 거론 구문을 여실히 직접 타건 조작해 단면 입력했을 시기에 우리가 일전 시야 목격했던 바로 그 행위 구조 특성과 일치합니다.

This example reflects the fact that `Python` is a general-purpose programming language.

이 단일 한 실전 예제는 바로 거론되는 저 `Python` 자체가 통상 보편적 활용의 일반-목적적(general-purpose) 범주에 속한 다-방면 프로그래밍 언어 체제라는 기저의 진면 사실을 시사 투영 일격에 반영합니다.

Much of `Python`’s data-specific functionality comes from other packages, notably `numpy` and `pandas`.

대거 상기 `Python`의 다루는 일면 데이터-특정적 지향 기능성들의 다반수 수많은 여간 대부분은 필시 다른 외부 유입된 타 패키지들, 특히 그 가운데 눈에 무척 띄게 두드러지는 `numpy` 및 `pandas` 라이브러리들로부터 근거 추출되어 제공 옵니다.

In the next section, we will introduce the `numpy` package.

다음 이어 따라 도래할 섹션 단락에서, 우리는 주축인 `numpy` 패키지를 도입해 훌쩍 소개할 것입니다.

See `docs.scipy.org/doc/numpy/user/quickstart.html` for more information about `numpy`.

저 당면 `numpy` 기술에 관한 획득 가능한 부가 정보로서 한층 더 많은 여유 지식 차원 정보들을 소망 원하신다면 부디 `docs.scipy.org/doc/numpy/user/quickstart.html` 열람 위치를 관조 보십시오.
