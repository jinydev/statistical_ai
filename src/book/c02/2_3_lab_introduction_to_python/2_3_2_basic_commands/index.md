---
layout: default
title: "index"
---

# 2.3.2 Basic Commands
# 2.3.2 기본 명령어(Basic Commands)

In this lab, we will introduce some simple `Python` commands. For more resources about `Python` in general, readers may want to consult the tutorial at `docs.python.org/3/tutorial/`.

이번 실습에서는 몇 가지 단순한 `Python` 명령어를 다룹니다. `Python` 언어 전반에 대한 자세한 정보가 필요한 독자는 `docs.python.org/3/tutorial/` 경로의 튜토리얼을 참고하십시오.

Like most programming languages, `Python` uses _functions_ to perform operations. To run a function called `fun`, we type `fun(input1, input2)`, where the inputs (or _arguments_) `input1` and `input2` tell `Python` how to run the function. A function can have any number of inputs. For example, the `print()` function outputs a text representation of all of its arguments to the console.

여느 대다수 프로그래밍 언어와 마찬가지로, `Python` 은 연산을 수행하기 위해 _함수(function)_ 를 사용합니다. 만약 `fun` 이라는 함수를 실행하려면 `fun(input1, input2)` 라고 입력합니다. 여기서 입력값(또는 _인수(argument)_)인 `input1` 과 `input2` 는 `Python` 에게 함수를 실행하는 방법을 알려주는 역할을 합니다. 함수는 여러 개의 입력 인수를 얼마든지 받을 수 있습니다. 예를 들어, `print()` 함수는 함수에 전달된 모든 인수들의 텍스트 표현을 묶어 화면 콘솔에 출력해 보여 줍니다.

```python
In [1]: print('fit a model with', 11, 'variables')
fit a model with 11 variables
```

The following command will provide information about the `print()` function.

다음에 제시하는 명령을 실행하면 `print()` 함수에 대한 정보를 제공합니다.

```python
In [2]: print?
``` 

Adding two integers in `Python` is pretty intuitive.

`Python`에서 두 정수를 더하는 것은 꽤 직관적입니다.

```python
In [3]: 3 + 5
Out[3]: 8
```

In `Python`, textual data is handled using _strings_. For instance, `"hello"` and `'hello'` are strings. We can concatenate them using the addition `+` symbol.

`Python`에서 텍스트 데이터는 _문자열(strings)_ 을 사용하여 처리됩니다. 예를 들어, `"hello"` 와 `'hello'` 기표는 모두 문자열입니다. 덧셈 기호인 `+` 를 사용하여 이들을 하나로 결합할 수 있습니다.

```python
In [4]: "hello" + " " + "world"
Out[4]: 'hello world'
```

A string is actually a type of _sequence_: this is a generic term for an ordered list. The three most important types of sequences are lists, tuples, and strings. We introduce lists now.

문자열은 사실 _시퀀스(sequence)_ 의 한 종류입니다. 시퀀스란 순서가 있는 목록을 뜻하는 포괄적인 용어입니다. 시퀀스의 가장 중요한 세 가지 유형은 리스트(list), 튜플(tuple), 그리고 문자열(string)입니다. 우리는 여기서 곧바로 리스트 형태를 먼저 소개합니다.

The following command instructs `Python` to join together the numbers 3, 4, and 5, and to save them as a _list_ named `x`. When we type `x`, it gives us back the list.

다음 명령어는 `Python` 에게 숫자 3, 4, 5를 하나로 결합하고, 이어진 결괏값을 `x` 라는 이름의 _리스트(list)_ 구조 안에 저장하라고 지시합니다. 이후 단순히 `x` 를 입력하면, 해당 리스트 내부를 다시 돌려줍니다.

```python
In [5]: x = [3, 4, 5]
        x
Out[5]: [3, 4, 5]
```

Note that we used the brackets `[]` to construct this list.

이러한 리스트를 작성 구축할 때 우리가 시스템 대괄호 기호인 `[]` 를 사용했음에 주목하십시오.

We will often want to add two sets of numbers together. It is reasonable to try the following code, though it will not produce the desired results.

우리는 종종 각기 다른 두 수치 집합의 무리를 하나의 숫자로 더하고 싶을 때가 있습니다. 아래의 코드를 시도해 보는 건 꽤 논리적이고 합리적인 시도지만, 안타깝게도 우리가 바라던 덧셈 산술 결과를 이끌지는 않습니다.

```python
In [6]: y = [4, 9, 7]
        x + y
Out[6]: [3, 4, 5, 4, 9, 7]
``` 

The result may appear slightly counterintuitive: why did `Python` not add the entries of the lists element-by-element? In `Python`, lists hold _arbitrary_ objects, and are added using _concatenation_. In fact, concatenation is the behavior that we saw earlier when we entered `"hello" + " " + "world"`.

이 결과 화면은 사람의 직관과 약간 어긋나는 반직관적인 모습으로 보일 수 있습니다: 어째서 `Python` 은 이 리스트 요소 항목들을 서로 각 위치에 맞춰 원소 대 원소 더하기 산술로 처리하지 않았을까요? 그 이유는 `Python` 체제 내에서 리스트 변수가 매우 광범위한 _임의의(arbitrary)_ 객체들까지 자유롭게 담을 수 있도록 설계되었으며, 이에 따라 덧셈 기호가 단순 숫자 덧셈이 아니라 구조적 나열인 _연결 병합(concatenation)_ 양식으로 사용되기 때문입니다. 사실, 이러한 병합 연결 원리 기반의 동작은 우리가 이전에 앞서 타이핑했던 `"hello" + " " + "world"` 문자열 코드 구문에서도 이미 동일하게 관찰했던 것과 같습니다.

This example reflects the fact that `Python` is a general-purpose programming language. Much of `Python`’s data-specific functionality comes from other packages, notably `numpy` and `pandas`. In the next section, we will introduce the `numpy` package. See `docs.scipy.org/doc/numpy/user/quickstart.html` for more information about `numpy`.

이러한 단편적인 한 가지 예시는 `Python` 이 단지 수학 연산에만 국한되지 않는 범용성 일반 목적 프로세스 언어라는 사실을 그대로 반영합니다. 그러므로 `Python` 체계가 갖는 대다수 깊은 데이터 분석 중심의 특화 기능들은 별도의 다른 외부 시스템 패키지, 그 가운데서도 특히 양대 산맥인 `numpy` 그리고 `pandas` 모듈을 통해 전폭적으로 지원 조달됩니다. 이어질 다음 실습 섹션에서는 이 분석 도구 중 하나인 `numpy` 패키지를 도입해 소개할 것입니다. `numpy` 패키지에 대한 더 풍성한 상세 정보와 기초 훈련 지표는 관련 웹 경로인 `docs.scipy.org/doc/numpy/user/quickstart.html` 문서를 참조해 주십시오.

---

## Sub-Chapters (하위 목차)

현재 2.3.2 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)
