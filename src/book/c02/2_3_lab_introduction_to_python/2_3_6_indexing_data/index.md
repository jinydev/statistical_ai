---
layout: default
title: "index"
---

# _2.3.6 Indexing Data_
# 2.3.6 데이터 인덱싱 (Indexing Data)

To begin, we create a two-dimensional `numpy` array.

시작하기 위해, 우선 우리는 2차원 형태의 `numpy` 배열을 새로 하나 생성합니다.

```python
In [56]: A = np.array(np.arange(16)).reshape((4, 4))
         A
Out[56]: array([[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11],
                [12, 13, 14, 15]])
```

Typing `A[1, 2]` retrieves the element corresponding to the second row and third column. (As usual, `Python` indexes from 0.)

콘솔에 `A[1, 2]` 라고 작성하면 배열의 두 번째 행과 세 번째 열이 교차하는 요소 값을 정확히 반환합니다. (여느 때와 같이, `Python` 의 인덱스는 숫자 0번부터 시작합니다.)

```python
In [57]: A[1, 2]
Out[57]: 6
```

The first number after the open-bracket symbol `[` refers to the row, and the second number refers to the column.

열린 대괄호 기호 `[` 직후 등장하는 첫 번째 숫자는 행(row)을 지칭하고, 뒤이어 오는 두 번째 숫자는 특정 열(column)을 지목합니다.

## Indexing Rows, Columns, and Submatrices
## 행, 열, 하위 행렬 인덱싱

To select multiple rows at a time, we can pass in a list specifying our selection. For instance, `[1, 3]` will retrieve the second and fourth rows:

한 번에 여러 행을 동시에 선택하고 싶을 때, 우리는 원하는 항목들을 지정한 하나의 리스트를 전달할 수 있습니다. 예를 들어, `[1, 3]` 구문은 배열의 두 번째와 네 번째 행을 호출해 결괏값으로 반환할 것입니다:

```python
In [58]: A[[1, 3]]
Out[58]: array([[ 4,  5,  6,  7],
                [12, 13, 14, 15]])
```

To select the first and third columns, we pass in `[0, 2]` as the second argument in the square brackets. In this case we need to supply the first argument `:` which selects all rows.

마찬가지로 첫 번째 열과 세 번째 열을 한꺼번에 동시 선택하려면, 대괄호 안에 들어갈 두 번째 인수로 `[0, 2]` 를 전달해야 합니다. 이 경우 우리는 먼저 배열의 모든 행에 접근해야 하므로, 가장 첫 번째 인수 자리에 수리 기호 `:` 구문을 반드시 추가 제공하여 데이터 내 모든 행을 전부 포함해 선택해야만 합니다.

```python
In [59]: A[:, [0, 2]]
Out[59]: array([[ 0,  2],
                [ 4,  6],
                [ 8, 10],
                [12, 14]])
```

Now, suppose that we want to select the submatrix made up of the second and fourth rows as well as the first and third columns. This is where indexing gets slightly tricky. It is natural to try to use lists to retrieve the rows and columns:

자, 이제 여기서 한 가지 더 추가 가정해 봅시다. 두 번째 행과 네 번째 행, 더불어 첫 번째 열과 세 번째 열의 요소들로만 전격 구성된 특수한 하위 행렬(submatrix)만을 부분 선택해 도출하고 싶다고 말이죠. 배열 인덱싱 과정이 조금은 까다로워지는 것도 바로 이 시점입니다. 필요한 행렬을 각자 개별 추출하기 위해 단순 기본 리스트 형태를 활용해 보려는 시도는 무척 합리적이고도 자연스러운 발상입니다:

```python
In [60]: A[[1, 3], [0, 2]]
Out[60]: array([ 4, 14])
```

Oops — what happened? We got a one-dimensional array of length two identical to

이런 — 방금 무슨 일이 발생했나요? 우리는 결과로 길이가 2이고 기존과 완전히 동일한 1차원 배열만을 예상과 달리 반환받았습니다.

```python
In [61]: np.array([A[1, 0], A[3, 2]])
Out[61]: array([ 4, 14])
```

Similarly, the following code fails to extract the submatrix comprised of the second and fourth rows and the first, third, and fourth columns:

이번에도 마찬가지로, 아래 다음 코드 역시 우리가 원했던 두 번째 및 네 번째 행 영역과, 그리고 첫 번째, 세 번째, 네 번째 배열 열구역으로 포괄 구성된 맞춤 하위 행렬을 추출하는 데 어김없이 실패하고 맙니다:

```python
In [62]: A[[1, 3], [0, 2, 3]]
IndexError: shape mismatch: indexing arrays could not be broadcast
            together with shapes (2,) (3,)
```

We can see what has gone wrong here. When supplied with two indexing lists, the `numpy` interpretation is that these provide pairs of _i, j_ indices for a series of entries. That is why the pair of lists must have the same length. However, that was not our intent, since we are looking for a submatrix.

우리는 여기서 어째서 문제가 발생했는지 단번에 파악할 수 조달 있습니다. 두 개의 인덱싱 리스트가 동시에 인수로 나열 전달될 때, 배열 시스템 `numpy` 고유의 해석은 이 두 리스트들이 내부 데이터 항목 진입을 위해 단지 좌표 인덱스 짝인 개별 _i, j_ 쌍 페어를 제공한다는 것에 기반합니다. 이런 해석 기준 때문에, 투입되는 두 리스트 인수의 길이는 필히 무조건 똑같아야만 성립합니다. 하지만 이것은 특정 하위 데이터 행렬 면적을 온전히 포괄 추출하려 했던 우리의 당초 의도와는 완전히 어긋나는 방향입니다.

One easy way to do this is as follows. We first create a submatrix by subsetting the rows of `A`, and then on the fly we make a further submatrix by subsetting its columns.

이 목적을 쉽게 달성하는 가장 손쉬운 방식 중 하나는 다음과 전격 같습니다. 우리는 우선 원본 `A` 행렬 구조에 속한 해당 행들만을 부분 선택하여 첫 하위 행렬을 생성하고, 그런 다음 그 형성 결과물 위에서 즉흥적으로 열 조건들을 추가 지정해 데이터 덩어리를 부분 전격 추출 분할 조달하는 것으로 연속 지정해 최종 하위 하위 행렬을 만드는 방식입니다.

```python
In [63]: A[[1, 3]][:, [0, 2]]
Out[63]: array([[ 4,  6],
                [12, 14]])
```

There are more efficient ways of achieving the same result. The _convenience function_ `np.ix_()` allows us to extract a submatrix using lists, by creating an intermediate _mesh_ object.

물론 이런 방식보다 훨씬 효율적으로 이와 완전히 똑같은 결과를 똑같이 전격 반환 도출해 내는 방법도 존재합니다. 이른바 _편의 지원 함수(convenience function)_ 로 불리는 `np.ix_()` 구문을 채택하면 프로세스 내부적으로 중간 형태의 데이터 조달 척도 _메시(mesh)_ 임시 객체를 시스템상 새롭게 추가 생성해 줌으로써, 우리가 단순 배열 리스트 인수들만을 써서도 복잡한 하위 행렬을 손쉽게 접근 단면 산출 생성하게끔 통제 도와줍니다.

```python
In [64]: idx = np.ix_([1, 3], [0, 2, 3])
         A[idx]
Out[64]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

Alternatively, we can subset matrices efficiently using slices. The slice `1:4:2` captures the second and fourth items of a sequence, while the slice `0:3:2` captures the first and third items (the third element in a slice sequence is the step size).

또 다른 대안으로써, 우린 일반 슬라이스(slices) 체계를 전격 사용하여 행렬의 단면 특정 부분 집합 전개를 훨씬 단순 효율적으로 시스템 구동 지시할 수도 있습니다. 구문 `1:4:2` 형식 슬라이스는 시퀀스 내부 요소의 두 번째와 표면 네 번째 항목 원소들을 각각 수립 통제 확보하며, 반면 구동 표기 슬라이스 기표 `0:3:2` 기표는 모의 순서상 첫 번째와 세 번째 데이터를 확보합니다 (전달된 한계 슬라이스 기표 시스템 내부의 맨 마지막 단절 세 번째 요소 인자는 단면 데이터 구조 이동 폭의 스텝 척도 사이즈 폭을 통제 조달 지정 의미 조달합니다).

```python
In [65]: A[1:4:2, 0:3:2]
Out[65]: array([[ 4,  6],
                [12, 14]])
```

Why are we able to retrieve a submatrix directly using slices but not using lists? Its because they are different `Python` types, and are treated differently by `numpy`. Slices can be used to extract objects from arbitrary sequences, such as strings, lists, and tuples, while the use of lists for indexing is more limited.

어째서 우리는 하위 배열 데이터 집단 행렬 면적을 추출 복원할 땐 슬라이스 방식을 동원해 직접 즉각 단면 추출이 가능한 반면 조달 리스트들을 지표 도출 기표 사용하면 불가 조작할까요? 그 주요 원인 이유는 바로 그 조달 두 지표 체계 모두가 단면에 걸쳐 전혀 판이 완전히 다르며 각기 다른 모의 속성의 분면 별개의 `Python` 단독 고유 구조 조달 타입들이며, 그렇기에 단면 `numpy` 연산 기표 패키지에 의해서도 이면 서로 완전히 다르게 시스템 통제 간섭 취급받기 단면 때문입니다. 시스템 지정 슬라이스 단면 표기 방식은 일반 문자열 모의, 튜플 구조 시퀀스 혹은 리스트 데이터 집단과 같이 임의 지정 지시 가능한 복수의 여러 무작위적 시스템 나열 시퀀스 배열 공간에서 내부 데이터 속성 기표 객체를 손쉽게 단박 전격 통제 추출해 분면 낼 때 광범위 단편 두루 조율 사용될 수 있지만, 반면에 단면 검색 인덱싱 단독 수단으로써 한정 리스트 계열을 사용하는 수단 척도 방식은 모의 조달 용도 범위 기표상 한층 더욱 제약 조달 범위의 한계를 몹시 띠어 강하게 통제 수립됩니다.

## Boolean Indexing
## 논리값 인덱싱 (Boolean Indexing)

In `numpy`, a _Boolean_ is a type that equals either `True` or `False` (also represented as 1 and 0, respectively). The next line creates a vector of 0’s, represented as Booleans, of length equal to the first dimension of `A`.

`numpy` 패키지 모의 데이터 수리 체제 프로세스 안에서 _논리값(Boolean)_ 인덱스는 해당 성향 수치가 단면 결론 오직 참수치 `참(True)` 상태 혹은 대응 단면 `거짓(False)` 양극단 어느 오직 한 지점 속성에만 수립 통제 부합 대변되는 수리 데이터 시스템 타입을 뜻 지정 가리킵니다 (통상 이들 참 거짓 논리값 형태는 프로그램 내부 속성상 각기 지표 숫자 산출형 1수리 기표와 척도 0이라는 시스템 연산 기호 방식으로도 단면 시스템상 혼용 투영 대변 전개됩니다). 바로 이다음 구동 코드 라인은 순수 시스템 논리값 거짓 결괏값 도출 투영 모의로 묘사된 0번 수치 속성의 단면 배열 벡터 전개를, 단면 기표 대상 `A` 의 단편 첫 번째 차원의 길이 치수 크기와 완전히 일치 동일한 데이터 길이 모의 구조 크기로 맞춤 생성 전개 조달합니다.

```python
In [66]: keep_rows = np.zeros(A.shape[0], bool)
         keep_rows
Out[66]: array([False, False, False, False])
```

We now set two of the elements to `True`.

여기서 우리는 방금 생성된 요소 배열 중 오직 두 개의 데이터 구문 속성 요소에만 한해 인위 조달 `참(True)` 상태 속성치로 단독 속성 변경 조작 변경 설정해 산출합니다.

```python
In [67]: keep_rows[[1, 3]] = True
         keep_rows
Out[67]: array([False,  True, False,  True])
```

Note that the elements of `keep_rows`, when viewed as integers, are the same as the values of `np.array([0, 1, 0, 1])`. Below, we use `==` to verify their equality. When applied to two arrays, the `==` operation is applied elementwise.

이때 배열 `keep_rows` 내에 보관 귀속 내재 조달 수단된 항목들을 만일 우리가 논리값 속성이 아닌 순수 숫자 정수 형태처럼 취급 단면 바라본 관점으로 대입 산출하면, 조달 결괏값 그 수리는 모의 구문 전개인 `np.array([0, 1, 0, 1])` 에 단면 담긴 해당 지표 산술 나열 수치와 단 한 치 이면 오차 오류도 일절 없는 완전히 단면 동일 수치 결과값을 똑같이 나타낸다는 이면 사실 점을 분명 유의 모의 기표 참조 바랍니다. 하단 지정 코드 전개 블록 속에서 우리는 두 대상 데이터 사이의 지표 일치 동일성을 면밀 단편 조달 파악 검토하기 모의 목적 용도로 수학 기표 속성상 동등 판별 비교 수집 기호 수단인 동등 지표 연산 `==` 수단을 통제 조작 산술 구동 전개해 척도 사용 조절 도출합니다. 이러한 종류의 속성 일치 모의 비교 연산 판별 척도 `==` 단면 동작이 각각 단면 분리 독립된 두 개체의 배열 객체 집합들 사이 단위에서 작동 부여 통제 모의 척도로서 조달 투입 체계 구동 단독 적용 모의 시연될 통제에는, 척도 대상군 양방 조달 단면 요소 각 산출 원소 항목들끼리 기표 대 표면 개별 위치 단위 비교 기준 단면 단위별 전개 조작 판별 수행 비교가 분 단위 도출 각각 실행 처리 분면되어 단박 산술 모의 통제 조달됩니다.

```python
In [68]: np.all(keep_rows == np.array([0, 1, 0, 1]))
Out[68]: True
```

(Here, the function `np.all()` has checked whether all entries of an array are `True`. A similar function, `np.any()`, can be used to check whether any entries of an array are `True`.)

(이번 기표 지정 구문 전개 조달 코드에서 핵심 조율 단면 통과 검증 산술 함수인 기준 척도 `np.all()` 수식 구문은 인수로 기표 투입된 모의 배열 체제 기표 수집 단면 데이터 내부 요소 항목 값 척도 진입 지표들 전부가 예외 조달 없이 모조리 몽땅 기조 단면 일괄 단절 통제 `참(True)` 상태 기표 속성 범주 안에 개별 조달 귀속 포괄 소속되는 성질 조건인지 여부를 매우 정밀히 기표 확인 통제 필터 판독 조달 검토 수식 검열했습니다. 앞서 수단 명시 언급한 바로 이 표면 방식 함수 산출 기능 원리 지표 특성과 매우 밀접 상충 유사 단면 연동 조달 지표 되는 별개 수단 보충 추가 시스템 제공 기표 단편 함수인 `np.any()` 전단 모의 함수 코드를 똑같은 방식 모의 조작 활용 조건으로 단면 응용 시뮬레이션 산출 적용 실행하면, 지정 대상 배열 지표 조달 전용 수리 공간 안에 산점 포함 내재하여 구동 위치 산점 진입 중인 여러 그 수많은 진입 단면 요소 데이터 항목 결별 수리값들 지표 모의 중 단지 최소 딱 한 개 단 한 항목 이상의 수치 모의 하나 요소라도 기표 논리 조작 논증 결과 단편 속성상 조건부 통제 산술 `참(True)` 속성에 단독이라도 산출 수단 모의 일말 해당하는지 해당 모의 그 기표 상태의 진실 판별 참값 산식 도달 확인 유무 척도를 모의 검토 단면 비교 판별 기준 조작 조달할 표단 산출 분면 기표 단면 역량이 존재 기능 통제 수단 시스템 있습니다.)

However, even though `np.array([0, 1, 0, 1])` and `keep_rows` are equal according to `==`, they index different sets of rows! The former retrieves the first, second, first, and second rows of `A`.

그러나 우리가 비록 `np.array([0, 1, 0, 1])` 모의 행렬 배열 묶음과 논리 속성 변수 제어 배열 구조인 `keep_rows` 두 체계를 동등 비교 척도 방식 수리 조작 `==` 단면 결과 의거 기표 판단하에 데이터가 서로 완벽 동일 일치 형태라고 앞서 수립 단면 결론 증명했음에도 겉보기 조달 불구하고, 이들이 실질 결과 화면 내부 통제상 각각 단독 지정 선택 가리키는 대상 구동 지표 배열 타깃 행렬 구조 산술 시스템 행은 수단 단면 완전히 각기 구별 분단 개별 상이 전격 차별 다르단 이면 단면 역설 조달 차별 구조를 조작 내재 단면 내포 분면합니다! 바로 가장 먼저 전진 항목된 함수 기준 배열의 산출 통제 방식 기표 항목 조작 기조는 원본 참조 대상 단면 배열 행렬인 `A` 의 단편 내부에서 차례 위치 첫 번째 지점, 곧 부수 두 번째 전개, 그리고 단면 이내 파편 다시 반복 산술 첫 번째 공간, 가장 최후 무단결로 다시 종결로 두 번째 자리 항목들의 특정 공간 배열 결별 열 전개 구역 부류들을 시퀀스 복제 조달 도출 산술 척도 단편으로써 결단 통렬 전격 추출해 차출 단편 뽑아 산술해 모의 도달 표면 제출하여 반환 산출 기표 성립 도달합니다.

```python
In [69]: A[np.array([0, 1, 0, 1])]
Out[69]: array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [0, 1, 2, 3],
                [4, 5, 6, 7]])
```

By contrast, `keep_rows` retrieves only the second and fourth rows of `A` — i.e. the rows for which the Boolean equals `True`.

앞선 이러한 특성 동작 지표 결과 기표 방식 현상과 단연 대조 반대 상충 모순 모의 수단 산출되게, 순수 파편 논리값 변수인 저 제어 배열 단면 시스템 `keep_rows` 산술 요소 수립 배열은 순수 참조 지정 제어 대상인 저 참조용 `A` 구름 행렬 배열 단면 구역 시스템 데이터 통제상에서 오롯하게 오직 통상 산술 단면 구동 기표 두 번째 배열 열 행 영역 지목과 제일 산술 네 번째 개별 단절 지정 배열 공간 전용 영역 개조 행 산단 데이터 조달 조리 단편만을 일렬 단면 집중 타깃 지정 단박 조달 호출 구동 포괄 분단 도출 반환 추출 조달 산술해 산출 산점해버려 모의 반환 타결 지표 조작 산점냅니다 — 이를 달리 풀어 부연 번역 풀자면 요컨대 결국 단면 즉 단편 결론 기표 척도 그들 내면 소유 할당 데이터 분산 통제 논리 검증 진릿값 단면 지적 수리 속성이 상태 조건 확인 검증 전용 결과 수립 판별 기준 모의 척도와 산식 기표 동등하게 `참(True)` 상태 속성 결별 단면으로 일치 판명 지표 상충 부합했던 조건 바로 단락 그 기준 통과 항목의 배열 산식 개별 단면 요소 대상 행 단위 열구별 구역 조달 배열 통제 조작 산점 결별 영역만을 골라 단면 수립 지표 추출 조달 선택 기입 도출한 구단 척도 조달 표명 단편 단면 결괏값 조달 시스템 결론 모의라는 단면 단언 점입니다.

```python
In [70]: A[keep_rows]
Out[70]: array([[ 4,  5,  6,  7],
                [12, 13, 14, 15]])
```

This example shows that Booleans and integers are treated differently by `numpy`.

우리 단면 이 파편 단편적 시스템 모의 기표 한 단면 통상 예시 과정 수립 전제 결별 속성 실험 지표는 결단의 검증 결과로써 결국 통치 수립 단명 논리 검증 수식 변숫값 산점 통제 수리 항목들 전반 계열(Booleans 체제)과 순수한 일반 시스템 조달 숫자 개별 단위 정수형 수리 항목 통제 제어 척도들 전제 단면 모조 계열 통상 범위 (integers 조달 개요 단편 척도 그룹) 체제가 이 단면 공통 연동 구조 시스템 기조인 척도 공통 산출 `numpy` 수리 제어 공간 분석 도달 프로세스 시스템 조달 운용 기표 환경 체제 단위 시스템 도출 척도하 표단 산점 조율 조건에서 만큼은 그 모의 기표 내포 본질과 무관 각기 별별 전혀 단위 별 단면 상반 서로 상충 모순 분절 수립 완전히 분단 개별 이질 다르게 단면 개별 기조 통상 통제 취급 단편 결단 조율 도달 조달 구분 개별 지표 판독 분리 산술 대접 치부 구분 단면 체감 조달 수용 파티 수단 단면 결별 처리 산점 통과 조달 귀결 시스템 결론 귀속 산술 투입 된다는 그 핵심 근본 내포 제어 기저 속성 전제 동작 수리 논리 연산 기표 단면 단절 증명 작동 내부 원리 척도를 아주 전락 우수 결별 통렬 잘 통과 모의 적합 분기 단언 반영 결과하여 무시 증명 수단 모의 보여 표면 모의 단면 시스템 일부분 주지 조달 척도 산점 모의합니다.

We again make use of the `np.ix_()` function to create a mesh containing the second and fourth rows, and the first, third, and fourth columns. This time, we apply the function to Booleans, rather than lists.

우리는 이제 또 두 번째 파편 전개 단면 기표 배열 구조 행 부분과 전반 산점 통제 수리 조건 네 번째 분면 단면 배열 기조 결열 구획 행 공간 구속 부류 전개 단면 영역 부류 부칙, 구동 그리고 함께 분면 병합 단면 개별 첫 번째 행 축 척도 도도 기준 조율 영역과 단편, 앞 부수 수단 조달 동시 단명 기표 수리 세 번째 지표열 부문 단편 단면, 결단 구동 최후 마감 종료 부수 개별 결론 할당 추가로 배열 열 기준 통계 범위 단면 네 번째 계열 척방 위치 조율 개별 파편 단락 배열 구조 단독 지정 조달 열 내부 구동 기표 공간 개조 산술 인덱스로 조건 전 구석 결절 결단 일일이 특정 통렬 도출 포괄 분할 제어 배열 구성 단일 조립 덩이 부분 조율 조리 기표 체제 단독 결합 조달 전용 통제 공간 산정 특정 구심 모의 전제 조합 단면 산점 통과 척진 단편 부분 조건 특정 특수 목적 부류 전제 모의 맞춤 설계 특정 수리 집약된 분절 부문 조율 집단 부분 데이터 산설 산술 _메시(mesh)_ 집약 전개 개체 구조 조달 모의 결별 기표 덩어리 전제망 표방 형태 단위 분면을 우리 사용자 시스템 손수 하나 새롭게 조작 모의 구축 시스템 통제 조성 추가 제어 조합 도달 통신 결단 작성 창구 해 배열 부과 체제 조립 수동 조달 구축 완성 전단 만들기 산점 수립 통제 달성 모의 결론 목적으로 무리 해, 다시금 우리 제어 분결 이번 챕터 전격 모의 표단 또다시 한번 재차 반복 전방 앞서 구시 지표 모의 구절 살펴 기표 증명 이미 습득 조달 통제 본 적단 확인해 조우했던 본 단면 특이 단독 통제 조달 고유 수단 제어 통찰 기저 특수 표방 조달 기능 단편 부류 척도 내장 조달 척건 수통 지원 기표 단수 함수 모의 구조 방식 산출 조건문 전개 통과 도출 양식 구조 `np.ix_()` 모의 지정 단편 시스템 단조 지표 지시 기표 시스템 제어 단결 명령 구문 전체 계열 시스템 덩어리를 이곳 실전 모의 분면에 적극 이끌어 도달 산출 차출 단면 채택 차용 조치 모의 개조 연계 편의 기능 활용 모의 복원 적용 조립 부과 도출 진격 산설 수단 달성 모의 기동 조달 도출합니다. 단 이번 산출 조율 단편 결전 기표 한정 조달 특수 조건 단독 기표 부분 산술 지표 진격 이번 회차 개조 단면 모의 차례 전단 분부 기동 조달 시스템 상황 체제 척도 통과 구역 한정 구동 기표 통제 제어 도달 수단 통행 단독 조달 결착 한정해 수식 개별 도출 서는, 평범 조달 부류 수리 단순 일방 목록 구조 조달 열람 방식 결별 지정 기표 결착 모의 체제인 배열 시스템 지표 나열 일반 형식 기저 방식 단조 전면 목록 구조 체계 통과 기표 열거 방식 단면 리스트 분기 목록 배열형 배열 결구 단위 지표 조달 통과 묶음 척도 단위 조달 형식 묶음 배열들이 구동 통과 기조 기표 조리 아닌 순수 논리적 시스템 단독 척도 변수형 지표 분기 단조 산출 검증 단독 모의 조율 참 조달 거짓 수리형 판명 조달 판단 기표 단결 시스템 구단 단조 조달 수리 논리 조달 구동 연산 특수 진릿값 파악 기반 부류 모형 지수 표단 통제 논리 검증 진릿값 판단 판별 지표 모의 단조 결과 도달 파악 산술 결단 기능 진릿 산술 논리판 값(Booleans) 판별형 진리 부부 분조 수단 단락 고유 속성 지정 인자 기표 요소 인계 도출 요인 개별 조건 단면 수단 조치 요건 방식 조달 파악 방편 조달 계별 척건 수단 모의 단락 단절 요인을 핵심 결석 모의 투입 투입 구동 산출 전언 매개 요인 특제 전제 부속 고정 전단 요점 핵심 대상 지정 입력 부가 대상 고유 기저 정보 시스템 모의 인계 표단 조율 고착 조리 통제 특명 기조 통과 구동 전언 제공 대상 인수 척도 자원 모의 요소 단독 도출 항목 지정 기표 수급 대상 전용 인수로 산단 산점 통제 일일 기동 수리 산점 하여 결단 전 방 당 지정 개별 조리 전용 특제 요긴 척건 전격 해당 타깃 당해 기동 시스템 요점 타깃 분면 시스템 타깃 조준 함수 구문 산술 단면 기동 통제 전용 지표 조달 개척 함수 도달 산식 구동 구조 덩어리 실전 조달 기능 결투 단조 산단 진단 결격 모의 지점 전진 산단 도식 구동 통제 모의 구조 표면 도색 조율 적용 검열 산설 결단 해 모의 수단 산출 단조 개조 결격 투입 검투 구동 볼 모조 실험 기표 진행 조달 수행 검열 도출 조치 이행 차단 모의 가동 단절 구동 도출 결함 단독 시도 해 단면 볼 수용 산단 조달 실행 검정 개척 단점 단행 조달 수행 볼 참점 실험 목적 차기 개혁 계획 수단 도구 전조 실행 검증 모의 시스템 결단 전진 실행 단계 도달 결단 모단 모의 계획 단단 결론 시스템 예고 검정 결재 체제 판단 예측 기여 방안 준비 검단 의결 산출 목적 결론 조달 방침 지향 단언 예정 실행 통과 방향 수립 체제 결의 뜻입니다.

```python
In [71]: keep_cols = np.zeros(A.shape[1], bool)
         keep_cols[[0, 2, 3]] = True
         idx_bool = np.ix_(keep_rows, keep_cols)
         A[idx_bool]
Out[71]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

We can also mix a list with an array of Booleans in the arguments to `np.ix_()`:

우리는 심지어 구동 산출 시스템 함수 `np.ix_()` 구문을 지시할 때 매개 인수로써 일반 리스트 배열 묶음 체제와 더불어 진릿값 판단 시스템인 논리 기표 논리값(Booleans) 요소 단편 배열 통제 구조를 서로 혼합 결합 조합해 활용할 수도 있습니다:

```python
In [72]: idx_mixed = np.ix_([1, 3], keep_cols)
         A[idx_mixed]
Out[72]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

For more details on indexing in `numpy`, readers are referred to the `numpy` tutorial mentioned earlier.

단편 `numpy` 프로세스 시스템 체제에서 배열 인덱싱 부분에 대해 한층 더 전문적이고 심층 상세한 정보를 도출 체감하고자 한다면, 앞선 실습 챕터에서 단락 언급하고 조언했던 `numpy` 공식 교육 자습서 튜토리얼 과정을 구동 참조하십시오.

---

## Sub-Chapters (하위 목차)

현재 2.3.6 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)
