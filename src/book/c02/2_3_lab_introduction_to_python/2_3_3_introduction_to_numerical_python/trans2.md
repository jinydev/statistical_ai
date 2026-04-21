---
layout: default
title: "trans2"
---

[< 2.3.2 Basic Commands](../2_3_2_basic_commands/trans2.html) | [2.3.4 Graphics >](../2_3_4_graphics/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.3 Introduction to Numerical Python
# 2.3.3 숫자 마법사 'NumPy' 소개

As mentioned earlier, this book makes use of functionality that is contained in the `numpy` _library_, or _package_.
아까 위에서도 스포일러 했듯이, 이 책의 모든 뼈대 연산은 결국 `numpy`라 불리는 기가 막힌 데이터 마법 _라이브러리(library)_, 즉 _패키지(package)_ 배낭에 담긴 막강한 수학 기능성들을 쏙쏙 빼다 씁니다.

A package is a collection of modules that are not necessarily included in the base `Python` distribution.
패키지가 뭐냐구요? 파이썬을 막 처음 샀을 때 기본 옵션(base Python)으론 주지 않는, 나중에 필요할 때마다 다운로드성 DLC처럼 추가로 낑겨 넣어야 하는 강력한 마법 모듈들의 모음집 팩을 뜻합니다.

The name `numpy` is an abbreviation for _numerical Python_.
그 위대한 이름 `numpy`(넘파이)는 _수치적 파이썬(numerical Python)_ 의 앞 글자를 재치 있게 줄여 지은 이름이죠.

To access `numpy`, we must first `import` it.
이 넘파이 마법 보따리에 접근하려면, 일단 우리 메모리로 짐을 싸서 스튜디오로 들여오는 탑승 수속, 즉 `import` 주문을 먼저 걸어줘야 합니다.

```python
In [7]: import numpy as np
```

In the previous line, we named the `numpy` _module_ `np`; an abbreviation for easier referencing.
바로 윗줄 타건에서 `import numpy as np` 라고 친 이유요? 매번 'numpy'라고 5글자나 타자 치는 건 현대 프로그래머들에겐 사치스럽기 그지 없는 극악의 중노동입니다! 그래서 앞으로 언제든 부르기 쉽게(easier referencing) 애칭 `np`라는 두 글자의 깜찍한 약칭을 지어준 겁니다.

In `numpy`, an _array_ is a generic term for a multidimensional set of numbers.
이 넘파이 마법계에서 가장 최고 존엄으로 취급되는 **_배열(array)_** 이란 존재는, 쉽게 말해 아파트(다차원) 구조로 층층이 숫자들이 나열된 거대한 숫자 집합 주차장을 일컫는 범용 용어입니다.

We use the `np.array()` function to define `x` and `y`, which are one-dimensional arrays, i.e. vectors.
가장 먼저 우리는 `np.array()`라는 아파트 건설 함수를 호출해, 1층짜리 단독 주택 배열(1차원 배열) 즉 **벡터(vectors)** 라고 불리는 숫자 덩어리 변수 `x`와 `y`를 예쁘게 정의해 보겠습니다.

```python
In [8]: x = np.array([3, 4, 5])
        y = np.array([4, 9, 7])
```

Note that if you forgot to run the `import numpy as np` command earlier, then you will encounter an error in calling the `np.array()` function in the previous line.
조심하세요! 혹시 깜빡하고 아까 위에서 `import numpy as np` 탑승 수속 주문을 켜두지 않았다면, 파이썬이 "np가 도대체 누군데?!" 하며 시뻘건 에러탄을 맞게 될 거란 사실을 가슴에 새깁시다.

The syntax `np.array()` indicates that the function being called is part of the `numpy` package, which we have abbreviated as `np`.
코드를 읽을 때 `np.array()` 란 구문은 그냥 "내가 부른 `array()` 함수는 넘파이 패키지(`np`) 가문 소속의 함수다!" 라고 가문의 문장에 출처를 정정당당히 밝히고 호출하는 행위입니다.

Since `x` and `y` have been defined using `np.array()`, we get a sensible result when we add them together.
어쨌건 이제 변수 `x`와 `y`는 바보 같은 순수 파이썬 리스트가 아닌 천재적인 `np.array()` 행렬로 재탄생해 단단히 구축되었습니다! 이제 둘을 더하면 아주 모범적이고 상식적인 벡터 덧셈 결과가 나올 겁니다.

Compare this to our results in the previous section, when we tried to add two lists without using `numpy`.
이전 섹션 단락에서 넘파이(`numpy`) 없이 쌩으로 바보같이 `x + y`를 했을 때 "3, 4, 5, 4, 9, 7"로 기차놀이 풀칠을 해버렸던 참사 결과와 이 기막힌 덧셈을 지금 당장 비교해보세요!

```python
In [9]: x + y
Out[9]: array([ 7, 13, 12])
```

In `numpy`, matrices are typically represented as two-dimensional arrays, and vectors as one-dimensional arrays.[1]
이 `numpy` 동네 안에서, 행과 열이 살아 숨 쉬는 진짜배기 수학 **행렬(matrices)** 들은 전형적으로 가로세로 바둑판 같은 **2차원 배열**들로, 한 줄로 쭉 선 **벡터(vectors)** 들은 단출한 **1차원 배열**들로 묘사되어 돌아갑니다.[1]

We can create a two-dimensional array as follows.
우리는 다음과 같이 바둑판 같은 멋진 2차원 배열 아파트를 간단히 지을 수 있습니다.

```python
In [10]: x = np.array([[1, 2], [3, 4]])
         x
Out[10]: array([[1, 2],
                [3, 4]])
```

The object `x` has several _attributes_, or associated objects.
이렇게 멋지게 지어진 2차원 객체 고층 아파트 `x` 는 겉모습만 번지르르한 게 아니라, 아파트 설계도 같은 자아 정보, 이른바 여러 개의 **_속성들(attributes)_** 을 꼬리표처럼 달고 다닙니다.

To access an attribute of `x`, we type `x.attribute`, where we replace `attribute` with the name of the attribute.
내가 만든 아파트 `x`의 스펙(속성)이 궁금하다면? 그냥 스위치 누르듯 `x.알고싶은_속성이름` 식으로 점을 찍고 타건해 물어보면 됩니다.

For instance, we can access the `ndim` attribute of `x` as follows.
예를 들어, "얘야 너 도대체 몇 층짜리 차원(dimension) 아파트니?" 라고 묻고 싶을 땐 냅다 `ndim` 속성을 갖다 대면 다음과 같이 스펙을 탁 뱉어냅니다.

```python
In [11]: x.ndim
Out[11]: 2
```

The output indicates that `x` is a two-dimensional array.
결과창에 달랑 '2'라고 나온 출력본은 `x`가 자랑스럽게 2차원(two-dimensional) 배열 건축물임을 증명합니다.

Similarly, `x.dtype` is the _data type_ attribute of the object `x`.
비슷한 이치로, 질문을 바꿔 `x.dtype` 스위치를 넣으면 아파트 `x`의 벽면 내부 자재가 어떤 타입인지 알려주는 **_데이터 타입(data type)_** 스펙이 술술 튀어나옵니다.

This indicates that `x` is comprised of 64-bit integers:
벽면을 열어봤더니, 이 건축물이 크고 단단한 64-비트 정수(integers) 블록들로 옹골차게 구성됐음을 알려주네요:

> 1 While it is also possible to create matrices using `np.matrix()`, we will use `np.array()` throughout the labs in this book.
> 1 번외로 팁을 주자면, 낡은 기술인 `np.matrix()` 구형 주문을 써서 억지로 행렬을 만들 수도 있긴 하지만, 이 책의 모든 실습(labs) 훈련 과정 통틀어 우리는 무조건 모던하고 세련된 만능키 `np.array()` 주문만을 내내 고집할 겁니다!

```python
In [12]: x.dtype
Out[12]: dtype('int64')
```

Why is `x` comprised of integers?
잠깐, 근데 왜 `x`가 소수점 하나 없는 퍽퍽한 정수들 블록으로만 지어졌을까요?

This is because we created `x` by passing in exclusively integers to the `np.array()` function.
그야 당연히 우리가 애초에 `x`를 설계할 때 `np.array()` 건설함수 입구에다가 소수점 없는 "1, 2, 3, 4" 같은 순혈 정수들만 독점적으로 꽉꽉 욱여넣었기 때문입니다! 뿌린 대로 거두는 법이죠.

If we had passed in any decimals, then we would have obtained an array of _floating point numbers_ (i.e. real-valued numbers).
만일 자재 창고에 소수점(decimals)이 단 0.1이라도 하나 섞여 들어갔다면? 파이썬은 눈치 빠르게 전체 아파트 벽면을 오차 없이 정밀하게 짜기 위해, 부유하는 소수점 즉 **_부동 소수점 수치(floating point numbers)_** (실수 값) 블록의 형태 배열 구조로 몽땅 업그레이드 체인지 했을 겁니다.

```python
In [13]: np.array([[1, 2], [3.0, 4]]).dtype
Out[13]: dtype('float64')
```

Typing `fun?` will cause `Python` to display documentation associated with the function `fun`, if it exists.
또 하나 엄청난 꿀팁! 여러분이 `fun?` 처럼 함수명 뒤에 물음표를 딱 붙이고 실행하면? 만약 그 함수가 세상에 존재하는 놈이라면 `Python`은 즉시 그 함수 설명서(documentation)를 무슨 사용 설명서 브로슈어 펼치듯 화면에 짠! 하고 꺼내 전시해 줍니다. 

We can try this for `np.array()`.
바로 이 신기한 기술을 `np.array()` 아파트 건설 주문에도 당장 똑같이 시도해 찔러볼 수 있죠!

```python
In [14]: np.array?
```

This documentation indicates that we could create a floating point array by passing a `dtype` argument into `np.array()`.
브로슈어 설명서를 잘 들여다보면 깨알 같은 단서가 나옵니다. 굳이 3.0 처럼 소수점을 주입하지 않더라도, 옵션값으로 `dtype=float` 인자 꼬리표를 강제로 달아 던져주는 꼼수만으로도 멋진 부동 소수점 실수 배열을 강제 생성이 가능하다는 깨달음을 줍니다! 

```python
In [15]: np.array([[1, 2], [3, 4]], float).dtype
Out[15]: dtype('float64')
```

The array `x` is two-dimensional.
다시 우리의 귀여운 2차원 바둑판 아파트 `x` 로 돌아가 볼까요. 

We can find out the number of rows and columns by looking at its `shape` attribute.
우리는 `x`가 총 몇 층(행)짜리인지, 한 층당 몇 호수(열)가 뚫려 있는지 그 몸매 사이즈를 `shape` 이라는 체형 속성 단면 스위치를 한 번 눌러 열람함으로써 단박에 발견해 낼 수 있습니다.

```python
In [16]: x.shape
Out[16]: (2, 2)
```

A _method_ is a function that is associated with an object.
프로그래머들이 밥 먹듯 쓰는 **_메서드(method)_** 란 놈이 도대체 뭘까요? 간단합니다. 아파트(객체, object) 구내에 전용으로 딱 달라붙어 설치된 붙박이 부대시설(내장 함수, function)을 멋지게 부르는 말입니다.

For instance, given an array `x`, the expression `x.sum()` sums all of its elements, using the `sum()` method for arrays.
예를 하나 들어보죠! 배열 `x` 가 주워졌을 때 우리가 냅다 쓴 `x.sum()` 이라는 코드는, 이 배열 아파트가 전용으로 소유한 자체 `sum()` 합계 계산기(메서드) 부대시설을 작동시켜 전 호수의 입주민 숫자 요소들을 모조리 싹 다 더해버리는 무시무시한 기능입니다.

The call `x.sum()` automatically provides `x` as the first argument to its `sum()` method.
이게 엄청 편한 이유요? 내가 `x.sum()` 스위치를 딸깍! 하고 누르는 순간, 보이지 않는 곳에선 `x` 스스로가 자신의 데이터를 첫 번째 제물(인수)로 바쳐 계산기에 셀프로 집어넣고 합계를 내는 마법을 부리기 때문이죠.

```python
In [17]: x = np.array([1, 2, 3, 4])
         x.sum()
Out[17]: 10
```

We could also sum the elements of `x` by passing in `x` as an argument to the `np.sum()` function.
물론, 내장 계산기 부대시설을 안 쓰고 거꾸로 메인 중앙 기압실 함수인 `np.sum()` 에 `x` 를 통째로 도시락 주듯 인수로 집어던져(passing in) 똑같이 원소들의 총합 연산을 우려낼 수조차 있습니다! (결과는 똑같습니다!)

```python
In [18]: x = np.array([1, 2, 3, 4])
         np.sum(x)
Out[18]: 10
```

As another example, the `reshape()` method returns a new array with the same elements as `x`, but a different shape.
메서드 뽕맛을 본 김에 또 다른 예시 들어갑니다! 마법의 `reshape()` 트랜스포머 메서드를 부르면, 원래 아파트 `x` 와 똑같은 주민(원소) 구성은 한 명도 빠짐없이 지독히 살리면서, 건물의 외곽 체형(모습) 구조만 찰흙 주무르듯 요리조리 다르게 주물러 개조시킨 전혀 새로운 배열을 눈앞에 반환해 딱 줍니다!

We do this by passing in a `tuple` in our call to `reshape()`, in this case `(2, 3)`.
이렇게 형태를 성형 개조하려면, 의사에게 구체적인 요구사항이 적힌 `tuple` 견적서(이 경우엔 즉 `(2, 3)`)를 거론되는 `reshape()` 메서드 내부에다 수술비 넣듯 슬쩍 찔러 넣어주면 그만입니다.

This tuple specifies that we would like to create a two-dimensional array with 2 rows and 3 columns.[2]
이 `(2, 3)` 튜플 주문서가 무슨 뜻이냐고요? "원장님! 2층 건물(행)에 층당 3호실(열)이 있는 날렵한 2차원 배열 쌍커풀 건물로 확 뜯어고쳐 주십시오!" 라고 당당히 요구(specifies)하는 것과 같습니다.[2]

In what follows, the `\n` character creates a _new line_.
이제 뒤따라오는 코드 구경할 때 주의! 뜬금없이 끼어드는 저 `\n` 요괴 문자는 프로그래머들이 몰래 숨겨둔 엑스칼리버입니다. 저 녀석을 치면 그 자리에서 다음 줄로 무조건 강제 엔터(_new line_)를 치며 줄바꿈을 시전합니다!

```python
In [19]: x = np.array([1, 2, 3, 4, 5, 6])
         print('beginning x:\n', x)
         x_reshape = x.reshape((2, 3))
         print('reshaped x:\n', x_reshape)
beginning x:
 [1 2 3 4 5 6]
reshaped x:
 [[1 2 3]
  [4 5 6]]
```

The previous output reveals that `numpy` arrays are specified as a sequence of _rows_.
방금 본 기가 막힌 트랜스포머 결과를 뜯어보면, 넘파이(`numpy`) 아파트 건설사들이 데이터를 어떻게 차곡차곡 쌓는지 알 수 있습니다. 바로 층 단위 즉 **_행들(rows)_** 이 연속으로 포근하게 차례차례 쌓여 올라가는 시퀀스 기반 설계도를 따랐음을 만천하에 드러내죠!

This is called _row-major ordering_, as opposed to _column-major ordering_.
기둥(열)부터 무식하게 세우고 보는 _열-우선(column-major)_ 방식 세계와는 180도 정반대로, 이렇게 가로로 길게 층(행)부터 벽돌 쌓듯 지어 올리는 방식을 고상하게 **_행-우선 순서(row-major ordering)_** 라고 칭합니다.

`Python` (and hence `numpy`) uses 0-based indexing.
파이썬(그리고 그 피를 이어받은 넘파이)의 가장 엽기적인 룰 한 가지! 얘네는 숫자를 셀 때 1, 2, 3 순서가 아니라 항상 지하 주차장 0층(0-based indexing)부터 악착같이 세는 끔찍한 습관을 지니고 있습니다.

This means that to access the top left element of `x_reshape`, we type in `x_reshape[0,0]`.
자, 이 말인즉슨 성형수술 끝난 아파트 `x_reshape` 의 가장 왼쪽 옥탑방 꼭대기 부자 입주민(첫 번째 요소) 집 문을 부수고 접근하려면, 1층 1호가 아니라 [0층, 0호] 번지수인 `x_reshape[0,0]` 을 쳐넣어야 열린다는 살벌한 뜻입니다!

```python
In [20]: x_reshape[0,0]
Out[20]: 1
```

Similarly, `x_reshape[1,2]` yields the element in the second row and the third column of `x_reshape`.
같은 오싹한 논리로, `x_reshape[1,2]` 도어벨을 누르면 1층이 아니라 **두 번째 층(행)** 에 있고, 2호가 아니라 **세 번째 위치(열)** 에 몸을 숨긴 숨둥이 원소를 단숨에 색출해 끌고 나옵니다. 헷갈리죠? 1을 더해 생각하세요!

```python
In [21]: x_reshape[1,2]
Out[21]: 6
```

Similarly, `x[2]` yields the third entry of `x`.
또 똑같이, 그냥 일렬 기차 형태 `x[2]` 를 호출해 버리면 2번 칸이 아니라 여지없이 **세 번째 기입 항목**에 지정된 원소 녀석을 토해내게 됩니다!

Now, let’s modify the top left element of `x_reshape`.
이런! 이제 슬쩍 장난기를 발동해서 새롭게 만든 저 `x_reshape` 아파트의 최상단 왼쪽 VVIP 원소 놈(1번)을 5번으로 몰래 암살하고 조작 수정해 바꿔치기해 보겠습니다!

To our surprise, we discover that the first element of `x` has been modified as well!
근데 웬걸! 까무러치게 놀라운 등골 오싹 호러 쇼가 벌어집니다! 방금 조작한 건 새 아파트였는데, 멀쩡히 놔뒀던 원래 구형 기차 배열 `x` 의 첫 원소 놈까지 쌍둥이 텔레파시처럼 같이 5로 암살당해 변경되어 버렸단 사실을 기겁하며 목격하게 됩니다! 이게 어찌 된 영문일까요?

```python
In [22]: print('x before we modify x_reshape:\n', x)
         print('x_reshape before we modify x_reshape:\n', x_reshape)
         x_reshape[0,0] = 5
         print('x_reshape after we modify its top left element:\n', x_reshape)
         print('x after we modify top left element of x_reshape:\n', x)
x before we modify x_reshape:
 [1 2 3 4 5 6]
x_reshape before we modify x_reshape:
 [[1 2 3]
  [4 5 6]]
x_reshape after we modify its top left element:
 [[5 2 3]
  [4 5 6]]
x after we modify top left element of x_reshape:
 [5 2 3 4 5 6]
```

> 2 Like lists, tuples represent a sequence of objects. Why do we need more than one way to create a sequence? There are a few differences between tuples and lists, but perhaps the most important is that elements of a tuple cannot be modified, whereas elements of a list can be.
> 2 아까 리스트 말고 튜플이란 놈도 일렬 기차 무리(시퀀스)라고 했죠. 도대체 튜플은 뭐가 아쉬워서 왜 따로 태어난 걸까요? 기기묘묘한 차이점들이 많지만 가장 치명적인 차이는 딱 하나겁니다! 튜플 요소 놈들은 한 번 태어나면 **절대, 네버, 목에 칼이 들어와도 암살(수정)을 안 당하는 강철 멘탈**을 가졌다는 치명적 점이죠. 반면 리스트 놈들은 원하면 얼마든지 쏙쏙 수정할 수 있는 허술한 종이 멘탈 종족입니다!

Modifying `x_reshape` also modified `x` because the two objects occupy the same space in memory.
다시 쌍둥이 암살 스릴러 사건으로 돌아와 보죠. 아까 `x_reshape` 수정한 게 왜 오리지널 `x`한테 전이됐냐? 사실 이 두 배열은 눈에 보이는 옷(shape)만 트랜스포머처럼 다르게 입었을 뿐 컴퓨터 메모리상에선 **완벽히 한 몸의 영혼(동일한 메모리 공간)** 을 배를 갈라 공유하며 차지한 존재였기 때문입니다! 무섭죠?

We just saw that we can modify an element of an array.
어쨌든 방금 엄청난 짓을 한 겁니다. 우린 파이썬에서 배열 속 입주민을 내 마음대로 쏙쏙 수정 개조할 수 있다는 무서운 사실을 알았죠.

Can we also modify a tuple?
그렇담 강철 멘탈인 '튜플(tuple)' 입주민 놈들도 암살(수정) 해버릴 수 있을까요?

It turns out that we cannot — and trying to do so introduces an _exception_, or error.
해봤더니! 절대 불가능합니다! 튜플 건드리려고 시도하는 순간 파이썬 경호원이 "이 바보야!" 하며 그 유명한 무서운 **_예외(오류, error)_** 딱지를 이마에 냅다 붙여버립니다! 건들지 마세요!

```python
In [23]: my_tuple = (3, 4, 5)
         my_tuple[0] = 2
```

```
TypeError: 'tuple' object does not support item assignment
```

We now briefly mention some attributes of arrays that will come in handy.
자, 이제 분위기 바꿔서 앞으로 실무에서 평생 우려먹을 배열계의 초단골 옵션 스펙, **속성들(attributes)** 3인방을 간략히 소개해 줍니다.

An array’s `shape` attribute contains its dimension; this is always a tuple.
첫째 파워! 배열에다 점 찍고 `shape`를 외치면 녀석의 구체적인 신체 사이즈(차원, 배열 행/열)를 고스란히 바쳐옵니다. 아, 이 사이즈 스펙은 절대 수정 못 하는 강철 멘탈 **튜플** 형식으로 토해낸다는 사실! 메모장에 적으세요.

The `ndim` attribute yields the number of dimensions, and `T` provides its transpose.
둘째 파워 `ndim`을 부르면 걍 무식하게 "2차원이요!" 하고 층수만 깔끔히 숫자 리턴하고요! 셋째 꿀파워 `T` 단추를 누르면 아파트를 **세로 모공으로 눕히는 트랜스포메이션(전치 행렬)** 결과를 눈앞에 산출해 보여줍니다. 눕방이 편해지죠!

```python
In [24]: x_reshape.shape, x_reshape.ndim, x_reshape.T
```

```python
Out[24]: ((2, 3),
          2,
          array([[5, 4],
                 [2, 5],
                 [3, 6]]))
```

Notice that the three individual outputs `(2,3)`, `2`, and `array([[5, 4],[2, 5], [3,6]])` are themselves output as a tuple.
여기서 잠깐, 화면 위에서 튀어나온 결과창을 잘 보세요! 세 개의 각기 다른 출력 결과물들이 모여 하나의 큰 강철 괄호 튜플 `(결과1, 결과2, 결과3)` 구조로 묶여서 우리에게 배달되었다는 놀라운 디테일에 주의 집중하십시오!

We will often want to apply functions to arrays.
때때로 우리는 이 무식한 배열 덩어리에 온갖 기기묘묘한 수학 함수 연산을 비 올 듯 사정없이 적용해 융단 폭격을 갈기고 싶어 손목이 근질거리게 될 겁니다.

For instance, we can compute the square root of the entries using the `np.sqrt()` function:
예를 들면, 내친김에 모든 입주민 원소들을 도마 위에 올려놓고 마법의 **`np.sqrt()`** 함수 칼을 휘둘러 싹 다 공평하게 그 무시무시한 수학의 **'제곱근(루트)'** 값을 일괄 재계산해 버릴 수 있습니다!

```python
In [25]: np.sqrt(x)
Out[25]: array([ 2.24,  1.41,  1.73,  2.  ,  2.24,  2.45])
```

We can also square the elements:
칼질뿐일까요? 모든 원소 덩치들을 체육관에 넣고 각각 사이드 근육을 두 배로 펌핑시켜 깡그리 덩어리를 뻥튀기하는 **'제곱'** 훈련도 시킬 수 있죠!

```python
In [26]: x**2
Out[26]: array([25,  4,  9, 16, 25, 36])
```

We can compute the square roots using the same notation, raising to the power of $1/2$ instead of 2.
제곱근(루트) 함수가 기억 안 난다고요? 괜찮습니다! 방금 제곱한 별 2개(`**`) 펌핑 표기법을 그대로 응용해, 숫자 2를 주는 대신에 살짝 비틀어 $1/2$ 즉 `0.5` 거듭제곱 파워를 줘버려도 결과는 마법의 루트와 소름 차게 똑같이 산출되니까요!

```python
In [27]: x**0.5
Out[27]: array([ 2.24,  1.41,  1.73,  2.  ,  2.24,  2.45])
```

Throughout this book, we will often want to generate random data.
이 책으로 험난한 통계 전장을 누비는 내내, 우리는 신의 주사위 놀이처럼 허구한 날 미친 랜덤 무작위 더미 데이터들을 양산하고 창조하고 싶어서 안달이 날 겁니다.

The `np.random.normal()` function generates a vector of random normal variables.
그럴 때마다 등장하는 구원투수! `np.random.normal()` 이라는 주문 함수는 마술처럼 정규 분포의 마법 속에 뛰노는 변수 무리들을 하나의 멋진 랜덤 백터 덩이군으로 쑥쑥 숨풍 뽑아 형성해 냅니다.

We can learn more about this function by looking at the help page, via a call to `np.random.normal?`.
이 대단한 함수의 속내가 궁금하다고요? 아까 꿀팁 줬죠? `np.random.normal?` 을 치며 긴박한 한 통의 호출 구조 명령을 넘기면 만병통치약 같은 도움말 페이지가 튀어나오니 열람하며 더 배울 게 한 다발입니다!

The first line of the help page reads `normal(loc=0.0, scale=1.0, size=None)`.
그 거룩한 도움말 메뉴얼 지면 첫 줄거리를 눈 크게 뜨고 직시해 보면, 마치 암호 문건 같은 `normal(loc=0.0, scale=1.0, size=None)` 이라는 무언의 규칙 구조가 기저 표기 구문으로 읽혀 들어올 겁니다.

This _signature_ line tells us that the function’s arguments are `loc`, `scale`, and `size`.
이 폼나는 서명 _시그니처(signature)_ 라인은, 이 위대한 조물주 함수 안에는 세 가지 필수 영양소 투입 인자, 즉 **`loc`(평균), `scale`(표준편차), `size`(개수)** 가 필요함을 은밀히 찌르고 알려주죠.

These are _keyword_ arguments, which means that when they are passed into the function, they can be referred to by name (in any order).[3]
더 놀라운 건 이 세트는 그냥 인자도 아니고 **_키워드(keyword) 인자_** 들이라는 사실! 즉, 믹서기에 짬뽕으로 처넣을 때 "scale=1, loc=0" 이렇게 이름을 딱 명시해 주면 내 맘대로 뒤죽박죽 어떤 빌어먹을 순서로 던져도 함수가 찰떡같이 자리를 찾아 삼켜준다는 은혜로운 뜻이 숨어있습니다![3]

By default, this function will generate random normal variable(s) with mean (`loc`) 0 and standard deviation (`scale`) 1; furthermore, a single random variable will be generated unless the argument to `size` is changed.
이것도 귀찮다? 그냥 빈 괄호로 부르면, 넘파이님은 기본 옵션(default)값으로 "평균(`loc`)은 0, 퍼진 정도(`scale`)는 1"로 잡힌, 소위 통계학의 근본 스탠다드 녀석 하나만 뚝딱 만들어줍니다. 게다가 `size` 값을 강제로 안 바꾸는 한 짠돌이처럼 딱 **한 놈의 단일 난수**만 주니까 명심하세요!

We now generate 50 independent random variables from a $N(0, 1)$ distribution.
이제 말 나온 김에, $N(0, 1)$ (평균 0, 표준편차 1) 스펙의 삐까뻔쩍한 통 안에 손을 넣어, 50마리의 눈치 안 보는 독립적인 랜덤 주사위 몬스터들을 생성해 보겠습니다!

```python
In [28]: x = np.random.normal(size=50)
         x
Out[28]: array([-1.19,  0.41,  0.9 , -0.44, -0.9 , -0.38,  0.13,  1.87,
                -0.35,  1.16,  0.79, -0.97, -1.21,  0.06, -1.62, -0.6 ,
                -0.77, -2.12,  0.38, -1.22, -0.06, -1.97, -1.74, -0.56,
                 1.7 , -0.95,  0.56,  0.35,  0.87,  0.88, -1.66, -0.32,
                -0.3 , -1.36,  0.92, -0.31,  1.28, -1.94,  1.07,  0.07,
                 0.79, -0.46,  2.19, -0.27, -0.64,  0.85,  0.13,  0.46,
                -0.09,  0.7 ])
```

We create an array `y` by adding an independent $N(50, 1)$ random variable to each element of `x`.
장난 좀 더 칠까요? 방금 만든 그 50칸짜리 배열 아파트 `x`의 각 호수별 입주민에다 추가로 $N(50, 1)$ 구역에서 따로 태어난 무작위 변수 몬스터 값들을 강제로 들러붙어 더해 버려서, 덩치를 불린 새로운 `y` 아파트 배열을 무단 생성해 보겠습니다.

```python
In [29]: y = x + np.random.normal(loc=50, scale=1, size=50)
```

The `np.corrcoef()` function computes the correlation matrix between `x` and `y`.
자, 그럼 여기서 의문! 방금 태어난 뚱뚱보 `y`놈은 원본 오리지널 `x`랑 얼마나 빼닮고 쌍둥이처럼 움직일까요? 파이썬 탐정 사무소 전용 상관관계(Corr) 스캐너 기술 함수인 **`np.corrcoef()`** 가 그 둘 사이의 밀접 끈적한 유착 관계(행렬)를 도출해 계산해 줄 겁니다! 

The off-diagonal elements give the correlation between `x` and `y`.
스캐너 분석 결과 창에서 딱 정중앙 대각선(나와 나의 사랑=1) 부분을 빗겨나간 외곽 여분 요소값들을 째려보면? 빙고! `x`와 `y` 녀석이 얼마나 사이좋게 붙어 다니는지(상관관계) 알려주는 섹시한 상관계수 스코어가 우리 눈앞에 떡 하니 주어집니다.

```python
In [30]: np.np.corrcoef(x, y)
Out[30]: array([[1.  , 0.69],
                [0.69, 1.  ]])
```

If you’re following along in your own `Jupyter` notebook, then you probably noticed that you got a different set of results when you ran the past few commands.
잠깐, 지금 여러분만의 노트북 창에 제 코드를 뚝딱뚝딱 복사하며 따라오고 계시는 당신! 눈치가 조금이라도 있다면, 본인이 아까 방금 실행했던 명령 결괏값 창에 떠오른 무작위 숫자 라인업 더미가 제 교재에 찍힌 스크린샷과 머리카락부터 발끝까지 딴판으로 다르다는 사실을 이미 뼈저리게 알아채셨겠군요! 

In particular, each time we call `np.random.normal()`, we will get a different answer, as shown in the following example.
이거 기계 고장 아닙니다! 말 그대로 "랜덤(무작위)" 함수이기 때문에, 다음 짧은 예시에 나오듯 우리가 `np.random.normal()` 부름 버튼을 딸깍 눌러 제낄 찰나의 때마다 사정없이 요동치며 상이하고 새로운 도출 답변 정답만을 툭툭 내던지는 게 당연한 겁니다!

```python
In [31]: print(np.random.normal(scale=5, size=2))
         print(np.random.normal(scale=5, size=2))
[ 4.28  2.59]
[ 4.62 -2.54]
```

In order to ensure that our code provides exactly the same results each time it is run, we can set a _random seed_ using the `np.random.default_rng()` function.
하지만, "아놔! 강좌랑 숫자가 다르면 공부할 때 헷갈리잖아요! 매번 똑같은 번호표 좀 달라고!!" 라고 절규할 여러분의 멘탈을 지키기 위하여, 파이썬엔 기막힌 자물쇠가 하나 존재하죠! `np.random.default_rng()` 란 방안 함수를 사용해 우주의 비밀 번호 같은 **_랜덤 시드(random seed)_** 씨앗 코드를 설정해 틀어막아 버림으로써 1,000번을 돌려도 토씨 하나 안 틀리게 같은 운명의 숫자를 양산시키는 보장 방안 장치를 확보해 놓을 수 있습니다.

This function takes an arbitrary, user-specified integer argument.
설정법은 단순합니다. 사용자가 자기 생일, 군번, 아니면 로또 번호든 뭐든 임의적인 정수 숫자 덩어리 인수를 이 함수의 뱃속에 저당 잡히듯 박아 넣기만 하면 됩니다.

If we set a random seed before generating random data, then re-running our code will yield the same results.
그렇게 무작위 몬스터를 뽑아내기 직전 제단에 시드 마법진을 한 번 딱 설정해 놓으면? 이 코드를 천년만년 재실행하며 돌리더라도 컴퓨터 기계는 마치 기시감, 데자뷰에 빠진 양 완전히 예고된 판이한 무결 오차의 같은 운명을 지닌 쌍둥이 결과 숫자물 복제본만을 여지없이 거두어냅니다.

The object `rng` has essentially all the random number generating methods found in `np.random`.
게다가 저 시드를 품은 강력한 객체 덩어리 일원 `rng` 는 엄청난 잠재력을 과시합니다. 본질적으로 기존 `np.random` 오리지널 공장에서 보유하고 돌아가던 그 모든 종류의 무수한 랜덤 수 도출 메서드 기계들을 이 놈이 다 흡수해 보유 상속해 지니고 있거든요!

Hence, to generate normal data we use `rng.normal()`.
그러니 논리적으로 깔끔하게, 우리는 기껏 배운 정규 분포 몬스터를 뽑아낼 땐 더 이상 구형 공장이 아닌 이 시드가 장전된 `rng.normal()` 신형 총을 꺼내 단번 일격에 난사를 때려 거둔단 이야기죠!

```python
In [32]: rng = np.random.default_rng(1303)
         print(rng.normal(scale=5, size=2))
         rng2 = np.random.default_rng(1303)
         print(rng2.normal(scale=5, size=2))
[ 4.09 -1.07]
[ 4.09 -1.07]
```

Throughout the labs in this book, we use `np.random.default_rng()` whenever we perform calculations involving random quantities within `numpy`.
바로 이게 비법입니다. 이 교재 실습의 수만 개 전방 구간 속을 헤집으며 다닐 무렵, 우리 강사진은 여러분이 `numpy` 랜덤 주사위를 던지며 헷갈리지 않게 배려하고자 제반 단위 연산이 나타나는 시기마다 언제나 저 `np.random.default_rng()` 강철 닻을 사용해 시공간을 동일 포맷으로 확정시킵니다.

In principle, this should enable the reader to exactly reproduce the stated results.
이렇게 지독하게 자물쇠를 거는 심산과 원칙적 목표는, 바로 컴퓨터 앞 저 멀리서 코드를 치는 불특정 다수의 우리 독자 여러분 누구라도 강좌 모니터에 딱 찍힌 수치 결과 그대로를 소수점 이하까지 100% 한 치 오차 없게 모방 재생산하고 도출시켜 "아, 나도 잘하고 있구나"라는 가능 구조와 여분 안심감을 선사하기 위함입니다. 

However, as new versions of `numpy` become available, it is possible that some small discrepancies may occur between the output in the labs and the output from `numpy`.
그런데, 최악의 경우를 대비해 스포 하나 날립니다! 세상만사가 항상 기계처럼 풀리지 않듯 추후 출시될 첨단 `numpy` 다음 세대 신규 버전 모듈들이 나오게 되면요, 제가 옛날 버전에 맞춰 써놓은 이 책의 실습 결과 출력값과 여러분 최신 파이썬 버전의 결괏값 사이에 "에잉? 끝자리 소수점 하나가 다르네?" 같은 몇몇 국소적이고 좁쌀만 한 조잡 오차 균열 차이가 도출되는 귀여운 비양심적 일탈 불일치 정도는 소폭 일어날 가능성이 있으니 너무 기함하지 마십시오!

The `np.mean()`, `np.var()`, and `np.std()` functions can be used to compute the mean, variance, and standard deviation of arrays.
숫자 마법을 마무리할 통계의 3신기 트리오! 바로 `np.mean()`(평균 내기), `np.var()`(분산 흩어짐 재기), 그리고 마지막 보스 `np.std()`(표준 편차 요동치기)! 이 세 함수들은 무수한 배열의 뼈대 수치 통계 분석을 가늠해 뽑아내고 척척 연산해 내기 조치 목적으로 다분하게 두루 사용 채택 구동되는 만능 칼잡이 트리오입니다.

These functions are also available as methods on the arrays.
이 강력 트리오는 따로 함수 공구함에서 안 꺼내고 편하게, 지어둔 배열 아파트 구조물 그 자체 위편 단면에 내재된 전속 부대시설 메서드 점 스위치 조작 도구(예: `x.mean()`)만으로도 무결하고 깔끔하게 여전히 이행 사용이 가능한 면모를 부쩍 띄고 있죠!

> 3 `Python` also uses _positional_ arguments. Positional arguments do not need to use a keyword. To see an example, type in `np.sum?`. We see that `a` is a positional argument, i.e. this function assumes that the first unnamed argument that it receives is the array to be summed. By contrast, `axis` and `dtype` are keyword arguments: the position in which these arguments are entered into `np.sum()` does not matter.
> 3 아까 인자(목재 재료)를 짬뽕으로 넣어도 된다 했는데 조건이 있어요! 파이썬은 이름표 없는 맹독성 _위치 지정(positional)_ 인자라는 룰도 공존시킵니다. 위치 지정 녀석들은 이름표(키워드) 따위 무시하고 "오직 순서가 법이다"라고 우깁니다! 예컨대 `np.sum?` 에 설명 뜬 `a` 같은 놈은요, 우리가 `np.sum(x)` 할 때 굳이 이름 명시 안 해도 가장 먼저 들어온 미 기명 첫 번째 녀석 `x`를 "아, 이놈이 바로 덧셈 당할 통계 배열 타깃물이구나!" 라고 건방지게 자동 가정해 버리는 무시무시한 지표 위치 룰 구조를 갖추고 있죠. 반면 `axis=0` 처럼 이름 찍힌 키워드 인자들은? 얘네는 배열을 맨 앞, 맨 옆, 어디다 냅다 던져넣든 순서는 모조리 상관 않는 무질서 개방성을 증명 보여주는 속성입니다.

```python
In [33]: rng = np.random.default_rng(3)
         y = rng.standard_normal(10)
         np.mean(y), y.mean()
Out[33]: (-0.11, -0.11)
```

```python
In [34]: np.var(y), y.var(), np.mean((y - y.mean())**2)
Out[34]: (2.72, 2.72, 2.72)
```

Notice that by default `np.var()` divides by the sample size _n_ rather than $n - 1$; see the `ddof` argument in `np.var?`.
단 이 분산 구하는 `np.var()` 함수에서 주의할 통계학의 뒤통수 꿀팁 하나! 기본 옵션 상으론 분모를 계산할 때 학계 무수분파 분산 룰인 $n - 1$ 구조 공식을 철저히 파괴하고 시크하게 그 데이터 총 표본수 대가리 덩치 숫자인 통 단위규모 _n_ 으로 가려움 없이 즉각 제수 삼아 나눈다는(자유도 무시) 살벌한 사실 점을 유념하십시오! "어? 분산은 n-1 아닌가요?" 하고 이 옵션을 손질 여부 점검하고 싶다 가령 한다면 단락 부근의 `np.var?` 설명서에 숨은 옵션 인자 조절 구역 부분의 `ddof` 항을 샅샅이 뒤져 검토해 조정해 부디 써 보시길 바랍니다!

```python
In [35]: np.sqrt(np.var(y)), np.std(y)
Out[35]: (1.65, 1.65)
```

The `np.mean()`, `np.var()`, and `np.std()` functions can also be applied to the rows and columns of a matrix.
우리의 이 믿음직한 삼신기 통계 함수 트리오(`np.mean()`, `np.var()`, `np.std()`) 세트 요소 객체 무리는 한낱 단출한 1차원 줄뿐만 아니라, 웅장한 행렬 아파트 전체 단원에 포진한 구조 내부의 특정 구역 다수 층수 "행들" 방면으로, 단면 뾰족한 동 구획 "열들" 단위를 겨냥 세로 꼬집어 통제하여 단전 조작 적용 역시 가능 가용 될 부가 사기 스킬 기능을 보유합니다! (특정 층, 특정 라인 통계 따로 빼기 가능)

To see this, we construct a $10 \times 3$ matrix of $N(0, 1)$ random variables, and consider computing its row sums.
과연 그게 진짜일지 이 엄청난 기능을 직접 목격 두 눈 가늠하려고, 우리는 잽싸게 저 $N(0, 1)$ 속성의 몬스터들을 잔뜩 욱여넣어 자그마치 "행 10칸 넓이 3칸" 짜리의 거대 $10 \times 3$ 규모 싹쓸이 행렬 아파트를 건축 생성 구조 지어 올리고, 각 방 단락마다 행별로 층층이 통 단면 합 요소를 시도해 쫘아악 추출해 뽑아 계산하는 도출 작용 플랜을 수립해 보겠습니다.

```python
In [36]: X = rng.standard_normal((10, 3))
         X
Out[36]: array([[ 0.23, -0.35, -0.28],
                [-0.67, -1.06, -0.39],
                [ 0.48, -0.24,  0.96],
                [-0.2 ,  0.02,  1.55],
                [ 0.55, -0.51, -0.18],
                [ 0.54,  1.94, -0.27],
                [-0.24,  1.  , -0.89],
                [-0.29,  0.88,  0.58],
                [ 0.09,  0.67, -2.83],
                [ 1.02, -0.96, -1.67]])
```

Since arrays are row-major ordered, the first axis, i.e. `axis=0`, refers to its rows.
아까 제가 살짝 경고했죠? 파이썬 배열 건축물 짓는 구조 질서 속성은 필시 기본적으로 바닥 1층 위에 2층을 까는 "행-우선(row-major) 정렬" 성질 주효 기틀을 깐다고요. 그렇기 때문에 이 넘파이에서 첫째 기조 지칭 중심 파워 축 즉 `axis=0` 딱지는 컴퓨터 입장에서 바로 그 기준 단락인 **행 단위 조각**들을 단독 지정해 가리키고 아우르며 포위한다는 기명 사실이 됩니다.

We pass this argument into the `mean()` method for the object `X`.
우리가 이 사실을 교묘히 이용해 `axis=0` 라는 조작 스위치 매개 뼈대 인자를 거대 객체 본원 건물 `X` 에 종속된 `mean()` 함수 입구 내부 속으로 살짝 던져 주입 단언 투여하면? (마법이 풀리죠!)

```python
In [37]: X.mean(axis=0)
Out[37]: array([ 0.15,  0.14, -0.34])
```

The following yields the same result.
귀찮은 그대들을 위한 보너스 코드! 이름표 안 달고 쿨하게 숫자 `0` 만 딱 집어넣은 아래 등장 구문 조치 역시 한 줌 부끄럼 없이 앞의 결과 출력 양태와 다분 일치하게 모조리 똑같은 단연 결괏값을 뽑아 산출 내어 우리 단전에 사르르 던져 줄 겁니다!

```python
In [38]: X.mean(0)
Out[38]: array([ 0.15,  0.14, -0.34])
```

---

## Sub-Chapters

[< 2.3.2 Basic Commands](../2_3_2_basic_commands/trans2.html) | [2.3.4 Graphics >](../2_3_4_graphics/trans2.html)
