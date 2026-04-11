---
layout: default
title: "index"
---

# _2.3.6 Indexing Data_

# _2.3.6 데이터 인덱싱_

To begin, we create a two-dimensional `numpy` array.

시작하기 위해, 우리는 하나의 2-차원 `numpy` 배열을 생성합니다.

```python
In [56]: A = np.array(np.arange(16)).reshape((4, 4))
         A
Out[56]: array([[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11],
                [12, 13, 14, 15]])
```

Typing `A[1, 2]` retrieves the element corresponding to the second row and third column. (As usual, `Python` indexes from 0.)

`A[1, 2]` 를 타이핑하는 것은 두 번째 행과 세 번째 열에 해당하는 원소를 가져옵니다. (평소처럼, `Python` 은 0으로부터 인덱스합니다.)

```python
In [57]: A[1, 2]
Out[57]: 6
```

The first number after the open-bracket symbol `[` refers to the row, and the second number refers to the column.

대괄호 열기 기호 `[` 이후의 첫 번째 숫자는 행(row)을 지칭하며, 두 번째 숫자는 열(column)을 지칭합니다.

## Indexing Rows, Columns, and Submatrices

## 행들, 열들, 그리고 부분행렬들 인덱싱

To select multiple rows at a time, we can pass in a list specifying our selection. For instance, `[1, 3]` will retrieve the second and fourth rows:

한 번에 여러 행들을 선택하기 위해, 우리는 우리의 선택을 명시하는 리스트를 전달할 수 있습니다. 예를 들어, `[1, 3]` 은 두 번째 및 네 번째 행들을 가져올 것입니다:

```python
In [58]: A[[1, 3]]
Out[58]: array([[ 4,  5,  6,  7],
                [12, 13, 14, 15]])
```

To select the first and third columns, we pass in `[0, 2]` as the second argument in the square brackets. In this case we need to supply the first argument `:` which selects all rows.

첫 번째와 세 번째 열들을 선택하기 위해, 우리는 꺾쇠 괄호 안의 두 번째 인수로서 `[0, 2]` 를 전달합니다. 이 경우 우리는 모든 행들을 선택하는 첫 번째 인수 `:` 를 공급해야 할 필요가 있습니다.

```python
In [59]: A[:, [0, 2]]
Out[59]: array([[ 0,  2],
                [ 4,  6],
                [ 8, 10],
                [12, 14]])
```

Now, suppose that we want to select the submatrix made up of the second and fourth rows as well as the first and third columns. This is where indexing gets slightly tricky. It is natural to try to use lists to retrieve the rows and columns:

이제, 우리가 첫 번째와 세 번째 열들 뿐만 아니라 두 번째와 네 번째 행들로 구성된 부분행렬을 결합하여 선택하기를 원한다고 가정해 봅시다. 여기가 인덱싱이 약간 까다로워지는 곳입니다. 행들과 열들을 구하기 위해 리스트들을 사용하는 것을 시도하는 것이 자연스럽습니다:

```python
In [60]: A[[1, 3], [0, 2]]
Out[60]: array([ 4, 14])
```

Oops — what happened? We got a one-dimensional array of length two identical to

앗 — 무슨 일이 일어났습니까? 우리는 다음과 동일한 길이 2의 일-차원의 배열을 하나 얻었습니다.

```python
In [61]: np.array([A[1, 0], A[3, 2]])
Out[61]: array([ 4, 14])
```

Similarly, the following code fails to extract the submatrix comprised of the second and fourth rows and the first, third, and fourth columns:

유사하게, 다음 코드는 두 번째 및 네 번째 행들과 첫 번째, 세 번째, 그리고 네 번째 열들로 구성된 이 부분행렬을 추출하는 것에 실패합니다:

```python
In [62]: A[[1, 3], [0, 2, 3]]
IndexError: shape mismatch: indexing arrays could not be broadcast
            together with shapes (2,) (3,)
```

We can see what has gone wrong here. When supplied with two indexing lists, the `numpy` interpretation is that these provide pairs of _i, j_ indices for a series of entries. That is why the pair of lists must have the same length. However, that was not our intent, since we are looking for a submatrix.

우리는 여기에서 무엇이 잘못되었는지 관찰할 수 있습니다. 두 개의 인덱싱 리스트들이 주어졌을 때, `numpy` 의 해석은 이것들이 항목들의 시퀀스에 상응하는 _i, j_ 인덱스들의 쌍들을 제공한다는 것입니다. 그것이 그 리스트들의 짝이 반드시 동일한 길이를 보유해야만 하는 이유입니다. 하지만, 우리가 하나의 부분행렬을 찾고 있기 때문에, 그것은 우리의 의도가 아니었습니다.

One easy way to do this is as follows. We first create a submatrix by subsetting the rows of `A`, and then on the fly we make a further submatrix by subsetting its columns.

이것을 수행하는 쉬운 방식은 다음과 같습니다. 우리는 `A` 의 행들을 부분집합 함으로써 부분행렬을 우선 생성하며, 그러고 나면 진행 중에(on the fly) 그 열들을 다시 부분집합 함을 통해 나아간 하나의 더 나은 부분행렬을 이룹니다.

```python
In [63]: A[[1, 3]][:, [0, 2]]
Out[63]: array([[ 4,  6],
                [12, 14]])
```

There are more efficient ways of achieving the same result. The _convenience function_ `np.ix_()` allows us to extract a submatrix using lists, by creating an intermediate _mesh_ object.

동일한 결과값을 얻어 성취하는 더 효율적인 길들이 있습니다. 편의 함수(convenience function) 인 이 `np.ix_()` 는, 중간 과정의 메시(mesh) 객체 하나를 생성함으로써, 우리가 리스트들을 이용해 부분행렬을 분리해 추출하도록 허용합니다.

```python
In [64]: idx = np.ix_([1, 3], [0, 2, 3])
         A[idx]
Out[64]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

Alternatively, we can subset matrices efficiently using slices. The slice `1:4:2` captures the second and fourth items of a sequence, while the slice `0:3:2` captures the first and third items (the third element in a slice sequence is the step size).

대체로, 우리는 슬라이스들을 사용하여 효율적으로 행렬들을 부분집합 화 할 수 있습니다. 이 슬라이스 `1:4:2` 는 시퀀스의 두 번째와 네 번째 항목들을 잡는 한편, 슬라이스 `0:3:2` 는 첫 번째 및 세 번째 항목들을 포착합니다 (슬라이스 시퀀스 내의 그 세 번째 원소는 간격 크기(step size) 입니다).

```python
In [65]: A[1:4:2, 0:3:2]
Out[65]: array([[ 4,  6],
                [12, 14]])
```

Why are we able to retrieve a submatrix directly using slices but not using lists? Its because they are different `Python` types, and are treated differently by `numpy`. Slices can be used to extract objects from arbitrary sequences, such as strings, lists, and tuples, while the use of lists for indexing is more limited.

왜 우리는 리스트들을 사용해서가 아니라 슬라이스들을 사용하여 부분행렬 하나를 직접 가져올 수 있는 것입니까? 그것은 그들이 서로 다른 `Python` 의 타입들이고, 이어 `numpy` 에 의하여 다르게 취급되기 때문입니다. 인덱싱을 위한 리스트들의 사용이 더 한정적인 것에 반해, 슬라이스들은 문자열들, 리스트들, 그리고 튜플들과 같은 무작위 시퀀스들(arbitrary sequences)로부터 객체들을 추출하기 위해 사용될 수 있습니다.

## Boolean Indexing

## 불리언(Boolean) 인덱싱

In `numpy`, a _Boolean_ is a type that equals either `True` or `False` (also represented as 1 and 0, respectively).

`numpy` 에서, _불리언(Boolean)_ 은 참인 `True` 혹은 거짓 `False` 양자 중 하나와 동일한 타입입니다 (이것들은 또한 각각에 숫자 1 및 숫자 0 으로서도 표현됩니다).

The next line creates a vector of 0’s, represented as Booleans, of length equal to the first dimension of `A`.

다음 이 줄은 `A` 변수의 첫 번째 차원 단위의 크기와 길이가 같으며 불리언들로써 나타내어진, 0 단위 들의 벡터 배열 덩이 하나를 생성합니다.

We now set two of the elements to `True`.

우리는 이제 해당 원소들 중에서 두 개의 요소 수단들을 `True` 로 설정합니다.

```python
In [66]: keep_rows = np.zeros(A.shape[0], bool)
         keep_rows
Out[66]: array([False, False, False, False])
```

```python
In [67]: keep_rows[[1, 3]] = True
         keep_rows
Out[67]: array([False,  True, False,  True])
```

Note that the elements of `keep_rows`, when viewed as integers, are the same as the values of `np.array([0, 1, 0, 1])`. Below, we use `==` to verify their equality. When applied to two arrays, the `==` operation is applied elementwise.

이 `keep_rows` 의 대상 원소 요소들이 정수들로써 취급되어 보아질 때, 그들이 `np.array([0, 1, 0, 1])` 배열의 요소 값들과 동일하다는 전 도출 사실에 유의 하십시오.  
아래에서, 우리는 그들의 상호 동등성을 입증해 검증하기 양단으로 식 `==` 를 사용합니다. 단면 두 개 치 일치 배열 양상들 위로 가해 투영될 무렵에, 구조 `==` 연산식은 원소별(elementwise)로 처리됩니다.

```python
In [68]: np.all(keep_rows == np.array([0, 1, 0, 1]))
Out[68]: True
```

(Here, the function `np.all()` has checked whether all entries of an array are `True`. A similar function, `np.any()`, can be used to check whether any entries of an array are `True`.)

(여기서, 지정 함수인 이 `np.all()` 은 한 배열 안에 자리한 기재 출입 항목들 일체가 모두 다 이탈 없이 온전히 `True` 와 일치 되는지 여부를 점검했습니다. 유사한 다른 함수 기능인 `np.any()` 는 한 배열 안에서 어떠한 항목들 중에 속 그 중 다소 무엇 하나 라도 `True` 인가 여부를 확인해 조사하기 위해 사용될 수 있습니다.)

However, even though `np.array([0, 1, 0, 1])` and `keep_rows` are equal according to `==`, they index different sets of rows!

허나 대차 그러나, 설혹 `np.array([0, 1, 0, 1])` 과 이 `keep_rows` 쌍방이 연산 `==` 에 따라 순응하여 동일 똑같을 당면 지언정, 정작 그것들은 제 각기 다른 행들의 배열 세트 뭉치들을 가리켜 인덱스 냅니다!

```python
In [69]: A[np.array([0, 1, 0, 1])]
Out[69]: array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [0, 1, 2, 3],
                [4, 5, 6, 7]])
```

The former retrieves the first, second, first, and second rows of `A`.

전자는 배열 다발 `A` 조치 속에서 첫 번째, 두 번째, 다시 첫 번째, 아울러 마지막 두 번째 여벌인 행 축들을 각각 발췌해 반환 꺼내어 냅니다.

By contrast, `keep_rows` retrieves only the second and fourth rows of `A` — i.e. the rows for which the Boolean equals `True`.

그에 반해 역상으로, `keep_rows` 요소는 지극히 오로지 단연 지목 `A` 구역상의 두 번째 단위 축 구획과 및 네 번째 행 축 들 만을 추출 발췌해 꺼내어 반환 냅니다 — 오로지 즉 다시 말하여 당 해당 불리언(Boolean) 산출 치수가 참조 `True` 명목으로 동일 부합 되는 행 지점들을 수반합니다.

```python
In [70]: A[keep_rows]
Out[70]: array([[ 4,  5,  6,  7],
                [12, 13, 14, 15]])
```

This example shows that Booleans and integers are treated differently by `numpy`.

이 예제는 불리언들(Booleans)과 정수들(integers) 기반 배열 치수들이 `numpy` 시스템 단면 내부에 의하여 각각 다르게 처리된다는 사실을 보여 줍니다.

We again make use of the `np.ix_()` function to create a mesh containing the second and fourth rows, and the first, third, and fourth columns.

우리는 두 번째 및 네 번째 행들과 함께 더불어 첫 번째, 세 번째, 그리고 네 번째 열들을 담는 하나의 개체 메시(mesh)를 생성하기 위해 단연 다시 그 `np.ix_()` 함수를 거듭 사용합니다.

This time, we apply the function to Booleans, rather than lists.

이번 국면에서 시기에는, 우리는 이전 리스트들 형태들 대신에 외려 차라리 그 불리언들(Booleans) 측에 해당 구성 함수를 동반 인계 부과 시킵니다.

```python
In [71]: keep_cols = np.zeros(A.shape[1], bool)
         keep_cols[[0, 2, 3]] = True
         idx_bool = np.ix_(keep_rows, keep_cols)
         A[idx_bool]
Out[71]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

We can also mix a list with an array of Booleans in the arguments to `np.ix_()`:

우리는 또한 그 호출 `np.ix_()` 안으로 전달할 인자들 내에서 리스트 하나와 불리언들의 형태 배열 하나를 혼합해 사용할 공산 넉넉히 수 조차 갖습니다:

```python
In [72]: idx_mixed = np.ix_([1, 3], keep_cols)
         A[idx_mixed]
Out[72]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

For more details on indexing in `numpy`, readers are referred to the `numpy` tutorial mentioned earlier.

`numpy` 수단에서의 인덱싱 과정에 관한 더 많은 세부 상세 내용 부분에 대하여 깊이 당면 알기를 바라는 여러 독자 여러분 당면 제현께는, 위에서 거론 당면 시사 제시 언급되었던 해당 공식 참조 그 해당 `numpy` 교육 튜토리얼을 참관 지목해 참조 확인해 주시도록 줄곧 당부 드립니다.
