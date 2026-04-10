---
layout: default
title: "index"
---

# _2.3.3 Introduction to Numerical Python_

As mentioned earlier, this book makes use of functionality that is contained in the `numpy` _library_, or _package_. A package is a collection of modules that are not necessarily included in the base `Python` distribution. The name `numpy` is an abbreviation for _numerical Python_. To access `numpy`, we must first `import` it.

앞서 언급했듯, 이 책은 `numpy` _라이브러리(library)_ 또는 _패키지(package)_ 에 포함된 기능들을 주로 사용합니다. 패키지란 기본 `Python` 배포판에 항상 기본적으로 포함되지는 않는 모듈 묶음을 뜻합니다. `numpy` 라는 이름은 _수치 파이썬(numerical Python)_ 의 약자입니다. `numpy` 패키지에 접근하기 위해 사용자는 가장 먼저 코드 `import` 를 사용해 패키지를 가져와야 합니다.

```python
In [7]: import numpy as np
```

In the previous line, we named the `numpy` _module_ `np`; an abbreviation for easier referencing. In `numpy`, an _array_ is a generic term for a multidimensional set of numbers. We use the `np.array()` function to define `x` and `y`, which are one-dimensional arrays, i.e. vectors.

바로 윗줄 명령어에서, 우리는 코드를 더 쉽게 참조하도록 단축 약어를 동원하여 `numpy` _모듈(module)_ 의 이름을 단편 `np` 로 새로 명명했습니다. `numpy` 환경에서 _배열(array)_ 은 특정 차원으로 된 다차원 숫자 집합체를 통치하는 일반적인 용어입니다. 우리는 앞으로 구문 `np.array()` 함수를 사용해 1차원 숫자 배열, 즉 숫자 벡터 구조인 변수 `x` 와 `y` 를 정의할 수 있습니다.

```python
In [8]: x = np.array([3, 4, 5])
        y = np.array([4, 9, 7])
```

Note that if you forgot to run the `import numpy as np` command earlier, then you will encounter an error in calling the `np.array()` function in the previous line. The syntax `np.array()` indicates that the function being called is part of the `numpy` package, which we have abbreviated as `np`. Since `x` and `y` have been defined using `np.array()`, we get a sensible result when we add them together. Compare this to our results in the previous section, when we tried to add two lists without using `numpy`.

만약 여러분이 앞 단계에서 `import numpy as np` 입력 명령어를 잊었다면, 앞 구문에서 `np.array()` 배열 함수를 호출할 즈음 에러를 마주하게 됩니다. 구문 구조인 `np.array()` 는 호출되는 이 함수 자체가 우리가 `np` 로 줄여 명명한 `numpy` 데이터 패키지의 일부분이라는 사실을 명시해 나타냅니다. 현재 기표된 변수 `x` 와 또 다른 `y` 가 이미 `np.array()` 모델을 활용해 성공적 정의되었으므로, 우리는 이들 둘을 더할 때 비로소 상식에 알맞은 논리적 덧셈 결과를 도출해 얻습니다. 우리가 방금 `numpy` 의 조력 없이 오직 순수 두 리스트를 나열해 합치려 애쌌던 앞 단원 섹션의 결괏값들과 직접 대조해 어떻게 다른지 비교 분석해 보십시오.

```python
In [9]: x + y
Out[9]: array([ 7, 13, 12])
```

In `numpy`, matrices are typically represented as two-dimensional arrays, and vectors as one-dimensional arrays.[1] We can create a two-dimensional array as follows.

보통 `numpy` 계산 분석 체제 안에서, 행렬 시스템은 일반적으로 2차원 공간 배열의 형태로 표기되며, 반면에 벡터는 1차원 공간 배열 표기로 구별됩니다.[1] 우리는 다음과 같은 파이썬 코드 문구로 직접 새로운 2차원 행렬 배열을 만들어 낼 수 있습니다.

```python
In [10]: x = np.array([[1, 2], [3, 4]])
         x
Out[10]: array([[1, 2],
                [3, 4]])
```

The object `x` has several _attributes_, or associated objects. To access an attribute of `x`, we type `x.attribute`, where we replace `attribute` with the name of the attribute. For instance, we can access the `ndim` attribute of `x` as follows.

파이썬 객체 `x` 에는 몇 가지 _속성(attributes)_, 일명 연관된 객체들이 포함되어 있습니다. `x` 의 어떤 속성에 접근하려면, `x.attribute` 와 같이 마침표를 찍고 `attribute` 부분을 내가 원하는 해당 속성의 명칭 이름으로 교체해 타이핑하면 됩니다. 예를 들어 우리는 다음과 같이 변수 `x` 의 차원을 뜻하는 `ndim` 속성에 직접 접근할 수 있습니다.

```python
In [11]: x.ndim
Out[11]: 2
```

The output indicates that `x` is a two-dimensional array. Similarly, `x.dtype` is the _data type_ attribute of the object `x`. This indicates that `x` is comprised of 64-bit integers:

이 출력 결괏값은 모형 `x` 본체가 2차원 공간 배열의 구조를 지님을 나타냅니다. 이것과 비슷하게 `x.dtype` 은 `x` 객체의 _자료형(data type)_ 속성 구조를 나타냅니다. 이 출력은 `x` 가 64비트 정수(64-bit integers) 공간으로 구성되었음을 짚어줍니다:

> 1 While it is also possible to create matrices using `np.matrix()`, we will use `np.array()` throughout the labs in this book.
> 
> 1 물론 별도의 `np.matrix()` 구문을 사용하여 데이터 행렬 시스템을 만들 수도 있겠지만, 본 도서의 모든 기표 실습 과정 전반에서는 우리는 예외 없이 오직 가장 범용적인 `np.array()` 만을 주로 사용할 예정입니다.

```python
In [12]: x.dtype
Out[12]: dtype('int64')
```

Why is `x` comprised of integers? This is because we created `x` by passing in exclusively integers to the `np.array()` function. If we had passed in any decimals, then we would have obtained an array of _floating point numbers_ (i.e. real-valued numbers).

왜 대상 `x` 배열은 오직 정수들로만 구성되었을까요? 그 이유는 처음 우리가 뼈대 결절인 `np.array()` 함수에 오로지 정수 숫자들만을 예외 없이 엄격히 직접 전달했기 때문입니다. 만일 거기에 우리가 단 하나의 소수 값이라도 산점 전달 포함했다면, 우리는 즉각 정수가 아닌 다른 _부동 소수점 수(floating point numbers)_ (즉, 실수값) 배열의 결과를 고스란히 획득 도출 받았을 겁니다.

```python
In [13]: np.array([[1, 2], [3.0, 4]]).dtype
Out[13]: dtype('float64')
```

Typing `fun?` will cause `Python` to display documentation associated with the function `fun`, if it exists. We can try this for `np.array()`.

터미널이나 콘솔 환경에서 `fun?` 과 같이 묻는 형식으로 기표 구동하게 되면, 만일 해당 대상 함수가 기표상 존재할 경우 파이썬 `Python` 이 시스템 함수 `fun` 과 연관된 도움말 도큐먼트 문서를 즉시 화면 단면에 출력해 줍니다. 이번에는 이 조회 기법을 우리가 방금 써먹은 `np.array()` 구문에도 똑같이 투사 시도해 봅시다.

```python
In [14]: np.array?
```

This documentation indicates that we could create a floating point array by passing a `dtype` argument into `np.array()`.

이 반환된 문서를 읽어보면, 우리가 `np.array()` 괄호 기둥 안에 `dtype` 속성 인자를 넣고 추가 전달하는 방식으로 내가 직접 부동 소수점 배열의 결과를 즉시 편히 생성 도출해 낼 수도 있음이 잘 나타납니다.

```python
In [15]: np.array([[1, 2], [3, 4]], float).dtype
Out[15]: dtype('float64')
```

The array `x` is two-dimensional. We can find out the number of rows and columns by looking at its `shape` attribute.

객체 배열 `x` 모델은 2차원 공간 형상을 가집니다. 사용자 우리는 배열 끝의 `shape` 속성에 접근 들여다봄으로써 데이터의 열 개수와 행 개수를 쉽게 파악하고 알아낼 수 있습니다.

```python
In [16]: x.shape
Out[16]: (2, 2)
```

A _method_ is a function that is associated with an object. For instance, given an array `x`, the expression `x.sum()` sums all of its elements, using the `sum()` method for arrays. The call `x.sum()` automatically provides `x` as the first argument to its `sum()` method.

프로세스에서 _메서드(method)_ 란 대상 특정 객체에 긴밀하게 연관 귀속된 함수를 말합니다. 예를 들어 변수 배열 `x` 가 하나 기표 주어졌을 때, 덧셈 수식 `x.sum()` 구문을 입력하면 배열 전용으로 귀속된 결별 `sum()` 메서드가 실행되어 자기 자신 안의 배열 원소 값을 모두 더해 총합 산술합니다. 즉 `x.sum()` 호출 구문은 자동으로 `x` 배열 자기 자신 본체를 `sum()` 메서드의 첫 번째 인수 자리로 주어 제공 조달합니다.

```python
In [17]: x = np.array([1, 2, 3, 4])
         x.sum()
Out[17]: 10
```

We could also sum the elements of `x` by passing in `x` as an argument to the `np.sum()` function.

또한 이뿐만 아니라, 독립적인 일반 패키지 함수 구문인 `np.sum()` 기둥 안에 명시적으로 내 변수 `x` 를 인수 덩어리로 전달 산술 투입하여 원소들의 통합 합계를 내게 할 수도 있습니다.

```python
In [18]: x = np.array([1, 2, 3, 4])
         np.sum(x)
Out[18]: 10
```

As another example, the `reshape()` method returns a new array with the same elements as `x`, but a different shape. We do this by passing in a `tuple` in our call to `reshape()`, in this case `(2, 3)`. This tuple specifies that we would like to create a two-dimensional array with 2 rows and 3 columns.[2] In what follows, the `\n` character creates a _new line_.

또 다른 예로써, 기본 내장된 `reshape()` 메서드는 대상 `x` 와 서로 완전히 똑같은 요소 데이터를 고스란히 담고 있으나 그 배열의 구조 형태만큼은 완전히 다른 새로운 배열 형상을 우리에게 결과 객체로 반환해 줍니다. 우리는 이를 위해 코드 `reshape()` 메서드 호출 구문 내부에 하나의 `튜플(tuple)` 단위 묶음을 인수로써 함께 조달 전달하는데, 지금의 경우엔 튜플 `(2, 3)` 이 그 대상입니다. 이 튜플 기표는 우리가 목표로 삼는 공간 배열이 거시적으로 2개의 선형 열과 3개의 개별 행으로 이루어진 2차원의 표면 배열이길 원한다는 것을 명시적으로 지적합니다.[2] 다음 도출될 코드 안에서, `\n` 입력 문자는 프로그램상 _줄바꿈(new line)_ 개행을 생성 조달합니다.

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

The previous output reveals that `numpy` arrays are specified as a sequence of _rows_. This is called _row-major ordering_, as opposed to _column-major ordering_.

앞선 결과 출력 코드는 구조상 `numpy` 배열이 기본적으로 _행(rows)_ 계열의 일련 시퀀스 순서로 나열되어 지정됨을 잘 보여줍니다. 데이터 구조상 이를 일컬어 행이 우선 기준이 되는 _행 우선 순서(row-major ordering)_ 규칙이라고 부르며, 이와 반대되는 성향 규칙이 바로 기표가 거꾸로 열이 기준이 되는 _열 우선 순서(column-major ordering)_ 입니다.

`Python` (and hence `numpy`) uses 0-based indexing. This means that to access the top left element of `x_reshape`, we type in `x_reshape[0,0]`.

시스템언어 `Python` (그리고 그에 귀속 파생된 `numpy` 도 당연히 포함해) 데이터는 모두 기저 0부터 숫자가 시작되는 제로 베이스(0-based) 인덱싱 번호 체계를 이용합니다. 이것의 의미는 배열 모형 기표 `x_reshape` 의 가장 왼쪽 맨 위 상단 원소 항목을 지적해 기표 접근하기 위해서는 위치 값을 1번이 아닌 0으로 간주해 `x_reshape[0,0]` 코드로 타이핑 입력해야 함을 뜻합니다.

```python
In [20]: x_reshape[0,0]
Out[20]: 1
```

Similarly, `x_reshape[1,2]` yields the element in the second row and the third column of `x_reshape`.

비슷한 맥락 논리로 접근하면, 코드 `x_reshape[1,2]` 는 당연 배열 변수 `x_reshape` 내부에서 두 번째 기준 열의 세 번째 행 요소에 기표 된 원소를 반환해 줍니다.

```python
In [21]: x_reshape[1,2]
Out[21]: 6
```

Similarly, `x[2]` yields the third entry of `x`.

마찬가지 논리에 따라 `x[2]` 는 배열군 `x` 의 세 번째 위치에 등재된 기표 원소를 반환 산출합니다.

Now, let’s modify the top left element of `x_reshape`. To our surprise, we discover that the first element of `x` has been modified as well!

자, 이제 기표된 배열 요소 `x_reshape` 의 맨 왼쪽 가장 위 상단 요소의 수치값을 한번 다른 값으로 직접 수정 변경해 봅시다. 그런데 우리 예상과 다르게 무척 놀랍게도, 원본이었던 진짜 구조 데이터 `x` 의 내부 첫 번째 요소 역시 덩달아 수치가 변경 조율되는 놀라운 사실을 발견할 수 조달 있습니다!

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
> 
> 2 리스트들과 비슷하게, 묶음 튜플 방식 또한 단면 객체들의 늘어선 구조 시퀀스 집합을 대변 모의합니다. 시스템은 왜 시퀀스 구조를 만드는 데 이렇게 두 가지 이상의 상이한 전혀 다른 방법을 굳이 만들어 필요로 할까요? 튜플과 리스트 양 구조 사이에는 몇 가지 소소한 작은 차이점들이 여러 존재하지만, 아마 그 어떤 것보다도 가장 두드러지게 중요한 핵심 분면 차이는 리스트 내부 원소들은 사용자가 아무 제약 없이 맘껏 자유롭게 사후에도 요소를 직접 수정이 가능한데 반해 튜플 시스템 내 원소들은 애초부터 구조적으로 요소를 일절 절대 나중에 변경 수정할 수 없다는 큰 제약 점입니다.

Modifying `x_reshape` also modified `x` because the two objects occupy the same space in memory.

분명 변수 `x_reshape` 요소만 단독 수정 조작했음에도 다른 대상 `x` 까지 덩달아 파편 수치 수정된 이유는 바로 이 각기 두 객체 데이터가 구조상 사실 내부 컴퓨터 메모리 공간상에서 완전히 서로 똑같은 지점의 동일 주소 영역을 물리적으로 나란히 같이 차지 사용하고 있기 때문입니다.

We just saw that we can modify an element of an array. Can we also modify a tuple? It turns out that we cannot — and trying to do so introduces an _exception_, or error.

방금 우리는 조달 수단으로 배열 수치 원소를 직접 수정 변경해 보았습니다. 그렇다면 과연 튜플 묶음 데이터도 똑같이 내부 속성 변경이 가능이나 할까요? 앞선 설명대로 그 작업은 결코 이루어질 수 없음이 도출 판명되며, 실제로 그렇게 어리석게 바꾸려고 코드 터미널 조작 시도하면 파이썬 시스템은 예의 없이 즉각 프로그래밍 _예외(exception)_ 즉 오작동 징후 에러를 곧장 표시 발생시킵니다.

```
In [23]:my_tuple=(3,4,5)
my_tuple[0]=2
```

```
TypeError:'tuple'objectdoesnotsupportitemassignment
```

We now briefly mention some attributes of arrays that will come in handy. An array’s `shape` attribute contains its dimension; this is always a tuple. The `ndim` attribute yields the number of dimensions, and `T` provides its transpose.

이제 실무에서 향후 요긴하게 계속 사용될 배열의 몇 가지 핵심 속성들을 잠시 짧게 짚어보겠습니다. 배열의 `shape` 속성은 객체 데이터의 공간적 차원을 담고 있으며 이 결괏값은 항상 시스템상 튜플로 반환됩니다. 한편 `ndim` 속성은 특정 차원들의 정량적 개수를 수치로 산출하며, `T` 지표는 기표 된 배열 행렬의 전치(transpose) 결과를 고스란히 제공합니다.

```
In [24]:x_reshape.shape,x_reshape.ndim,x_reshape.T
```

```
Out[24]:((2,3),
2,
array([[5,4],
[2,5],
[3,6]]))
```

Notice that the three individual outputs `(2,3)` , `2` , and `array([[5, 4],[2, 5], [3,6]])` are themselves output as a tuple.

또한 방금 출력된 세 가지 각기 다른 개별 산출 결괏값인 `(2,3)` 및 `2` , 그리고 배열 `array([[5, 4],[2, 5], [3,6]])` 은 사실상 이들 결과들 자체가 전체 표면적으로 하나의 큰 구조인 튜플로 묶여져 함께 출력된 것임을 명시히 주목하십시오.

We will often want to apply functions to arrays. For instance, we can compute the square root of the entries using the `np.sqrt()` function:

사용자는 다방면으로 종종 전체 배열 집단에 단일 함수들을 바로 적용시켜야 할 상황을 잦게 맞이합니다. 예를 들어 우리는 널리 쓰이는 기본 내장 함수 `np.sqrt()` 를 차용 사용해 항목 전체 원소들에 대한 통합 제곱근을 동시에 단박에 계산 도출할 수 있습니다:

```
np.sqrt()
```

```
In [25]:np.sqrt(x)
```

```
Out[25]:array([2.24,1.41,1.73,2.,2.24,2.45])
```

We can also square the elements:

이와 마찬가지로 항목 전체 요소들을 똑같이 제곱 산출할 수도 있습니다:

```
In [26]:x**2
```

```
Out[26]:array([25,4,9,16,25,36])
```

We can compute the square roots using the same notation, raising to the power of 1 _/_ 2 instead of 2.

또한 똑같은 시스템 코딩 표기법 방식을 써서 요소 전체에 일반 지수 2 대신 $1/2$ 분산 제곱 지수를 단번에 취해 올림으로써도 동일하게 편한 제곱근 산출 연산을 도출할 수 조달 있습니다.

```python
In [27]: x**0.5
Out[27]: array([ 2.24,  1.41,  1.73,  2.  ,  2.24,  2.45])
```

Throughout this book, we will often want to generate random data. The `np.random.normal()` function generates a vector of random normal variables. We can learn more about this function by looking at the help page, via a call to `np.random.normal?`. The first line of the help page reads `normal(loc=0.0, scale=1.0, size=None)`. This _signature_ line tells us that the function’s arguments are `loc`, `scale`, and `size`. These are _keyword_ arguments, which means that when they are passed into the function, they can be referred to by name (in any order).[3] By default, this function will generate random normal variable(s) with mean (`loc`) 0 and standard deviation (`scale`) 1; furthermore, a single random variable will be generated unless the argument to `size` is changed.

이 책을 처음부터 끝까지 살펴보는 동안 우리는 종종 무작위 분포 형태를 띠는 조달 난수 모의 데이터를 꽤 자주 직접 생성해야만 합니다. 특수 패키지 함수 구문인 `np.random.normal()` 은 이러한 시스템 난수 정규 변수들의 집합 벡터를 한 번에 생성 조달해 줍니다. 우리는 `np.random.normal?` 을 콘솔에 호출하여 구동되는 대상 도움말 페이지를 열람해 살핌으로써 이 구문 함수에 관련된 추가 조작 정보들을 손쉽게 심화 학습할 수 있습니다. 반환 표시된 해당 도움말 도큐먼트의 첫 줄을 보면 `normal(loc=0.0, scale=1.0, size=None)` 이라고 명시 적혀있습니다. 이 함수 모의의 _서명(signature)_ 양식으로 조달된 해당 첫 줄은 우리로 하여금 이 함수 구문이 받아들일 수 있는 인수 이름이 바로 `loc`, `scale`, 그리고 변수 `size` 란 것을 자세히 가리킵니다. 이것들을 가리켜 보통 _키워드(keyword)_ 매개 인자 방식이라 일컫는데, 곧 이 말뜻은 이들 단편 인수가 함수 내부로 전달될 때는 입력 위치의 순서 개념과는 무관히, 아무 순서 배열로든 상관없이 단지 고유 조작 대상의 이름 명칭만을 통해 특정 요소를 지시 명확히 참조 통제할 수 있다는 사실 단계를 뜻합니다.[3] 이 모델 함수를 설정값 변경 없이 호출하면 도출 기본값으로 그것은 중심 평균(`loc`)은 0이고 분산 편차(`scale`)는 1을 띠는 하나의 정규 난수 변수를 생성 산출하며; 게다가 변수 `size` 에 부여되는 항목 인수가 이외의 숫자로 변경 설정되지 않는다 치면 단지 1개의 단편 시스템 단일 난수 변수만 도출 반환해 생성할 것입니다.

We now generate 50 independent random variables from a $N(0, 1)$ distribution.

자, 그러면 이제 코드 입력을 통해 평균 0, 표준편차 1 구조 분포도 표면인 $N(0, 1)$ 기준에 맞춰 서로 완전히 무관한 독립 산술된 정규 난수 변수 50개를 전격 산출해 생성해 보겠습니다.

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

다음 코드를 따름으로써 기존에 기표 마련해 둔 객체 배열 변수 `x` 내부의 각 소속 모든 단편 원소에 서로 간섭 완전 별개의 새로운 $N(50, 1)$ 정규 난수 분포 변숫값들을 강제 합산시킴으로써 기표 `y` 라고 새로 명명된 전혀 이질 다른 새로운 변수 배열 무리를 산점 조합해 새롭게 생성합니다.

```python
In [29]: y = x + np.random.normal(loc=50, scale=1, size=50)
```

The `np.corrcoef()` function computes the correlation matrix between `x` and `y`. The off-diagonal elements give the correlation between `x` and `y`.

특수 함수 구문인 `np.corrcoef()` 는 주어진 변수 배열 `x` 와 대상군 `y` 시스템 간의 산술 상관관계에 대한 상관 행렬 구조를 연산해 산술 줍니다. 도출 기표 상 대각선 방면 기준 축에서 서로 완전히 동떨어져 배치 벗어난 구역의 요소 수치 기표들이야말로 바로 `x` 와 `y` 변수 배열군 양자 간의 산술 상관 치수 계수를 실질 반영 대변합니다.

```python
In [30]: np.corrcoef(x, y)
Out[30]: array([[1.  , 0.69],
                [0.69, 1.  ]])
```

If you’re following along in your own `Jupyter` notebook, then you probably noticed that you got a different set of results when you ran the past few commands. In particular, each time we call `np.random.normal()`, we will get a different answer, as shown in the following example.

만약 여러분이 각자의 독립적인 실습 전용의 `Jupyter` 노트북 환경 인터페이스 안에서 직접 코드를 입력 따라치면서 조달 실습하고 있다면, 방금 지난 단락의 이 몇 가지 코드 명령들을 손수 타이핑 실행했을 때 본 책 지표의 안내 시연 결과와는 서로 값이 전혀 맞지 않는 상이 다르고 파편적 다른 세트 모의 수치 결과 지표들을 도출해 돌려받게 되었단 구조 속성 사실을 아마 분명 체감 눈치챘을 겁니다. 그 원인은 특히나 함수 `np.random.normal()` 구문을 수단 호출할 때마다, 아래의 시연 구조 단편 코드가 단면 알려주듯 단번 매 실행 조작 순간 조건마다 전혀 낯설게 달라지는 완전히 새로운 기표 무작위 난수 답변 세트를 도달 도출해 결과 얻기 때문입니다.

```python
In [31]: print(np.random.normal(scale=5, size=2))
         print(np.random.normal(scale=5, size=2))
[ 4.28  2.59]
[ 4.62 -2.54]
```

In order to ensure that our code provides exactly the same results each time it is run, we can set a _random seed_ using the `np.random.default_rng()` function. This function takes an arbitrary, user-specified integer argument. If we set a random seed before generating random data, then re-running our code will yield the same results. The object `rng` has essentially all the random number generating methods found in `np.random`. Hence, to generate normal data we use `rng.normal()`.

따라서 우리의 스크립트 코드 모의 조작이 매 실행 조건마다 항상 예외 없이 무조건 처음과 도출 완전히 일치 같은 단일 결괏값만 기만 산출 하도록 방비 통제하기 위해, 우리는 사전 구문 `np.random.default_rng()` 함수를 사용하여 척도 상의 _무작위 시드(random seed)_ 고정값을 미리 설정 투사해 볼 수 있습니다. 이 투사 함수는 사용자가 구상 특명 임의로 직접 지정 결정한 시스템 정수 인수를 그 매개로 받아들여 산점 설정합니다. 무작위 난수 기반의 데이터를 조작 생성해내기 바로 그 직전 윗단에 척도 무작위 훈련 시드(seed)를 설정 적용하면, 차후에 본 시스템 코드를 통째 몇 번 재실행 조작하건 매번 한결같이 완전히 다 똑같은 단일 반환 도출 같은 결과 모조 세트를 조달 도출 산출합니다. 반환된 변수 객체 `rng` 는 구조 원리상 사실 근본적인 `np.random` 산하 조달 체제에서 획득 제공되는 모든 여하 시스템 종류의 난수 무작위 조작 생성 방식들을 일목요연 그 본체 내부에 전부 담아 고스란히 가지고 있습니다. 고로, 앞으로는 정규 조작 표본 데이터 모의를 산출 생성하기 단면 위해 우린 단순히 하위 속성 `rng.normal()` 을 통제 사용할 수 있습니다.

```python
In [32]: rng = np.random.default_rng(1303)
         print(rng.normal(scale=5, size=2))
         rng2 = np.random.default_rng(1303)
         print(rng2.normal(scale=5, size=2))
[ 4.09 -1.07]
[ 4.09 -1.07]
```

Throughout the labs in this book, we use `np.random.default_rng()` whenever we perform calculations involving random quantities within `numpy`. In principle, this should enable the reader to exactly reproduce the stated results. However, as new versions of `numpy` become available, it is possible that some small discrepancies may occur between the output in the labs and the output from `numpy`.

이 공식 교육 실습 책자에 수록 속한 모든 실험 단면에 거쳐 걸쳐서, 우리는 단편 체계 `numpy` 의 무작위 산점 난수 무리 요소 관련 계산이 조금이라도 산점 개입될 때마다 한결같이 언제나 일관 적용 `np.random.default_rng()` 를 사용하여 실험 통제합니다. 원칙적 기본으로 이 방식을 유지 전후 이용하면 책을 마주 보고 조작 익히는 각 독자들 또한 여기 교재 산출물에 적힌 모의 결괏값을 자신들 시스템 단면에 단 한 치도 빠짐없이 지독히도 명확 완벽 재생 복제 산출할 수 분명 있을 조달 가능할 겁니다. 그럴지라도 간혹 세월이 흘러 언젠가 파이썬 관련 `numpy` 라이브러리의 전혀 다른 상이 훨씬 새로운 파생 업데이트 버전이 조달 적용 사용할지 다가온다면, 우리 실습 책 본문에 모의 서술된 결괏값 도출 출력 수치 모델과 실제 사용자의 `numpy` 모델 출력 시스템 값들 사이 모델 내에서 몹시 약간의 소소한 편차 오류 징후가 조달 나타나 발생할 가능성 또한 여분 존재하긴 합니다.

The `np.mean()`, `np.var()`, and `np.std()` functions can be used to compute the mean, variance, and standard deviation of arrays. These functions are also available as methods on the arrays.

우리는 자주 통계 기표 구문으로써 `np.mean()`, `np.var()`, 및 `np.std()` 와 같은 산출 함수들을 사용하여 각 기표 배열 공간 척도 데이터들의 단면 평균치, 오차 분산, 척도 그리고 표준편차 수치들을 직접 측정 도출해 계산해 낼 수 있습니다. 사실 이 단면 수학 함수 구문들은 독립 투과 함수 시스템뿐만 아니라 배열 자체 속성의 모의 메서드 형식으로도 모두 기포 조작할 수 조달 있습니다.

> 3 `Python` also uses _positional_ arguments. Positional arguments do not need to use a keyword. To see an example, type in `np.sum?`. We see that `a` is a positional argument, i.e. this function assumes that the first unnamed argument that it receives is the array to be summed. By contrast, `axis` and `dtype` are keyword arguments: the position in which these arguments are entered into `np.sum()` does not matter. 
> 
> 3 `Python` 언어 구조는 _위치(positional)_ 기반 배열의 매개 인자 파악 구조 도식도 사용합니다. 이런 위치 표기 기반 인자들은 굳이 매개 지정 키워드 이름 명사에 목매 의지 묶일 전혀 필요가 없습니다. 명확한 조달 단편 예시를 직접 체감하려면 시스템 콘솔 모의 부분에 `np.sum?` 단어를 기표 실행하십시오. 열람 문서에서는 `a` 부분이 기표상 위치 인자라는 사실을 알려 주며, 즉 결론적으로 시스템 이 함수 시스템은 단면 자신이 이름 없는 명명 제약 부재 상태의 어떠한 무작위적 매개 변수 항목을 딱 한 개 가장 가장 우선 첫 번째 순서 자리에서 즉시 단박 전달 조달 넘겨받기만 하면 그것이 곧 덧셈 처분할 합계 대상의 본 배열이라 제멋 시스템 가정해 산식 처리한다는 것을 내포해 보여줍니다. 이와는 모순 정반대로서 단일 `axis` 나 파편 `dtype` 파라미터는 앞선 부류와는 달별로 _키워드(keyword)_ 시스템 인수에 등재 속합니다: 따라서 이 매개 조달 파편 항목 변수들을 굳이 함수 `np.sum()` 안에 선 투입 전개 삽입 전달 구동시킬 그 위치 순번 자리 따위는 산술 아무런 기표 제약 상관도 문제도 전혀 조달 발발시키지 단편 않게 영향을 조달 주지 결별 전혀 미치지 않습니다.

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

조달 산출 기본값 세팅 자체로써 저 `np.var()` 는 산술 분모 구조 항목을 변수 집단 $n - 1$ 대신 기표 $n$ 즉 실제 샘플 집계 표본 크기 데이터 규모 몫 수치 그 자체를 척도 대상으로 분모 나눠 버린다는 이면 사실 점을 분명 명시 깊이 유의하십시오; 더 속 내용의 깊은 척도 사항을 알고자 원하시면 명시 `np.var?` 실행을 통한 도움말의 `ddof` 분면 인수 항목 단편을 세심 열람하십시오.

```python
In [35]: np.sqrt(np.var(y)), np.std(y)
Out[35]: (1.65, 1.65)
```

The `np.mean()`, `np.var()`, and `np.std()` functions can also be applied to the rows and columns of a matrix. To see this, we construct a $10 \times 3$ matrix of $N(0, 1)$ random variables, and consider computing its row sums.

이 산점 `np.mean()`, `np.var()`, 와 기표 수단 `np.std()` 수학 조율 함수들은 통째 행렬 배열 무리의 수간 단일 열, 행 항목들에 시스템 각각 단독 조율 적용 사용할 수 조달 있습니다. 이런 산점을 직접 단편 모의 실행 체감하여 보려면, 기표 상 $N(0, 1)$ 난수를 척도로 하는 행 모의 10 열 기표 3 규모 치수인 형상 $10 \times 3$ 행렬 객체 척도 덩어리를 우선 먼저 단면 구축한 뒤 그것들의 각각 행 척도 부류 결합 덧셈 연산 결괏값을 수리로 도출 도달 고려해 봅니다.

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

Since arrays are row-major ordered, the first axis, i.e. `axis=0`, refers to its rows. We pass this argument into the `mean()` method for the object `X`.

앞선 이론에서 이미 우린 데이터 배열이 태생적으로 단면 행 우선 배열 지표 척방 정렬 속성 기표 방식을 취함 따름을 단면 분명히 전 수리 목도 체득 배웠으므로 알 수 있듯 조달 최우선 단절 방향 지수 첫 기준 축, 축 기준 즉 조달 `axis=0` 은 구조상 즉 기표 상 당 모델 배열의 무작위 행 방향 단편을 통렬해 뜻 의미 가리킵니다. 우리는 도출 산출될 인수를 기표 단면 객체 `X` 단위에 귀속 전제된 산술 조달 메서드 구문인 단편 `mean()` 덩어리의 인수로 제공 전격 패스 투입하여 사용합니다.

```python
In [37]: X.mean(axis=0)
Out[37]: array([ 0.15,  0.14, -0.34])
```

The following yields the same result.

이는 척도 아래 코드 도식과 똑같이 완벽히 단면 하나 동일한 결별 도출 동일 결괏값 수립을 조달 산출합니다.

```python
In [38]: X.mean(0)
Out[38]: array([ 0.15,  0.14, -0.34])
```

---

## Sub-Chapters (하위 목차)

현재 2.3.3 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)
