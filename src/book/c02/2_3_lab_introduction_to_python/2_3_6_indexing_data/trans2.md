---
layout: default
title: "trans2"
---

[< 2.3.5 Sequences And Slice Notation](../2_3_5_sequences_and_slice_notation/trans2.html) | [2.3.7 Loading Data >](../2_3_7_loading_data/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.6 Indexing Data
# 2.3.6 데이터 인덱싱 (정보 낚아채기)

To begin, we create a two-dimensional `numpy` array.
인덱싱(원하는 데이터만 쏙쏙 뽑아내는 기술) 사냥을 시작하기 위해, 우리는 먹잇감이 될 듬직한 2-차원 `numpy` 배열 바둑판 하나를 생성해 줍니다.

```python
In [56]: A = np.array(np.arange(16)).reshape((4, 4))
         A
Out[56]: array([[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11],
                [12, 13, 14, 15]])
```

Typing `A[1, 2]` retrieves the element corresponding to the second row and third column. (As usual, `Python` indexes from 0.)
자, `A[1, 2]` 라고 주소를 쳐서 사냥개를 날려볼까요? 이 녀석은 배열 무리 속에서 '두 번째 행(1층)'과 '세 번째 열(2호)'의 교차점에 은신한 범인(원소)을 정확히 포위해 물어(retrieves) 옵니다. (늘 주의하세요, 파이썬 동네의 지번 체계는 항상 1이 아니라 0번부터 시작합니다!)

```python
In [57]: A[1, 2]
Out[57]: 6
```

The first number after the open-bracket symbol `[` refers to the row, and the second number refers to the column.
공식 하나 외우고 갑시다. 대괄호 `[` 가 열리고 나오는 첫 번째 숫자는 무조건 아파트의 **행(row, 층수)** 을 가리키며, 두 번째로 찍히는 녀석은 무조건 방 위치인 **열(column, 호수)** 을 가리키는 절대 규칙입니다.

## Indexing Rows, Columns, and Submatrices
## 행, 열, 그리고 서브-행렬(부분행렬) 동시에 덮치기

To select multiple rows at a time, we can pass in a list specifying our selection. For instance, `[1, 3]` will retrieve the second and fourth rows:
만약 내가 한 층만 터는 게 아니라 동시에 여러 행(층)을 한꺼번에 싹쓸이하고 싶다면? 간단합니다. 내가 털고 싶은 층수만 적은 `[1, 3]` 같은 살생부(리스트)를 주소창에 쑥 건네면 됩니다. 이 명단은 단숨에 빌딩의 두 번째 층과 네 번째 층 전체를 야무지게 강탈해 올 겁니다:

```python
In [58]: A[[1, 3]]
Out[58]: array([[ 4,  5,  6,  7],
                [12, 13, 14, 15]])
```

To select the first and third columns, we pass in `[0, 2]` as the second argument in the square brackets. In this case we need to supply the first argument `:` which selects all rows.
반대로 건물 전체 층을 놔두고 세로 기둥(열), 즉 "첫 번째 열과 세 번째 열 라인 전체만 압수수색해!" 라고 하고 싶다면? 대괄호의 두 번째 자리에 세로줄 살생부 `[0, 2]` 를 던져줍니다. 이때 주의할 점! 앞쪽 층수(행) 자리에는 텅 비운 채로 "전체 다 털어!"를 의미하는 무적의 프리패스 마크인 콜론 `:` 을 반드시 먼저 깔아(supply)줘야만 합니다.

```python
In [59]: A[:, [0, 2]]
Out[59]: array([[ 0,  2],
                [ 4,  6],
                [ 8, 10],
                [12, 14]])
```

Now, suppose that we want to select the submatrix made up of the second and fourth rows as well as the first and third columns. This is where indexing gets slightly tricky. It is natural to try to use lists to retrieve the rows and columns:
자, 이제 난이도를 높여서 대형 작전을 짜봅시다. "모든 층 다 말고 딱 두 번째 층과 네 번째 층만 고르면서, 각 층마다 첫 번째 방과 세 번째 방에 있는 놈들만 솎아내서 모아(부분행렬) 와!" 이 요구를 들어주려다 보니 파이썬의 인덱싱 문법에서 살짝 잔머리가 아찔해지는(tricky) 딜레마 구간이 찾아옵니다. 우리의 순진한 인간 두뇌로는 당연히 앞뒤로 리스트 명단을 두 개 나란히 꽂아놓고 자연스레 다음과 같이 코딩을 시도하겠죠:

```python
In [60]: A[[1, 3], [0, 2]]
Out[60]: array([ 4, 14])
```

Oops — what happened? We got a one-dimensional array of length two identical to
우웁스! (Oops —) 결과가 왜 이 모양이죠?! 원판 네모행렬이 아니라, 꼴랑 숫자 2개짜리에 심지어 바짝 쪼그라든 1차원 볼품없는 배열 막대기 하나만 던져졌습니다. 이 기괴한 막대기는 사실 아래 동작과 똑같은 겁니다.

```python
In [61]: np.array([A[1, 0], A[3, 2]])
Out[61]: array([ 4, 14])
```

Similarly, the following code fails to extract the submatrix comprised of the second and fourth rows and the first, third, and fourth columns:
이 멍청한 파이썬의 오해법칙(?)은 행과 열 개수를 다르게 주면 아예 에러를 내뿜습니다. 아래처럼 "2개 층에서 3개 호수를 뒤져라!"라고 리스트 짝짜꿍으로 넘겨버리면 미니 서브 행렬(submatrix) 추출 명령은 대차게 실패해 터져버리죠:

```python
In [62]: A[[1, 3], [0, 2, 3]]
IndexError: shape mismatch: indexing arrays could not be broadcast
            together with shapes (2,) (3,)
```

We can see what has gone wrong here. When supplied with two indexing lists, the `numpy` interpretation is that these provide pairs of _i, j_ indices for a series of entries. That is why the pair of lists must have the same length. However, that was not our intent, since we are looking for a submatrix.
도대체 왜 이런 대참사가 났는지 변명을 들어볼까요. `numpy` 놈의 뇌 회로는 이렇습니다. 리스트명단표 두 개를 던져주면 "아항! [1번층, 0호] 그리고 [3번층, 2호] 이렇게 '짝바위 쌍(pairs)'으로 1:1 매칭 핀셋 추적을 하라는 임무구나!" 라고 제멋대로 해석해 버립니다. 그래서 리스트 명부끼리 조 짝 숫자가 다르면 당황해서 에러를 뱉었던 거죠. 하지만 우리의 원래 의도는 '격자형 그물'을 던져 모든 교차점 놈들을 쓸어 담는 거창한 부분행렬 납치 작전이었으니 대화가 어긋난 셈입니다.

One easy way to do this is as follows. We first create a submatrix by subsetting the rows of `A`, and then on the fly we make a further submatrix by subsetting its columns.
이 그물망 작전을 해결하는 가장 쉽고 무식한 편법은 이거죠. 일단 먼저 `A`에서 그물 대상이 되는 '행(가로)'들만 통째로 발라내어 임시 부분 도마를 만들고, 그 잘린 도마들을 허공에 띄운 채 곧바로 이어서(on the fly) '열(세로)'들을 다시 한번 대각 토막 썰기(subsetting) 시전해 이중 절단하는 방식입니다.

```python
In [63]: A[[1, 3]][:, [0, 2]]
Out[63]: array([[ 4,  6],
                [12, 14]])
```

There are more efficient ways of achieving the same result. The _convenience function_ `np.ix_()` allows us to extract a submatrix using lists, by creating an intermediate _mesh_ object.
무식한 칼질 말고, 같은 결과를 달성하면서도 훨씬 뼈대 있고 효율적인 귀족형 방식이 있습니다. 바로 파이썬이 준비한 전용 효자손 함수, **편의 함수(convenience function) `np.ix_()`** 를 호출하는 겁니다. 이놈은 우리가 건네준 가로세로 명부 리스트들을 엮어서 보이지 않는 **거대한 중간 '그물망(mesh)' 투망**을 짠 뒤, 한 번에 배열에 덮어씌워 타깃들만 단숨에 건져 올려버립니다.

```python
In [64]: idx = np.ix_([1, 3], [0, 2, 3])
         A[idx]
Out[64]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

Alternatively, we can subset matrices efficiently using slices. The slice `1:4:2` captures the second and fourth items of a sequence, while the slice `0:3:2` captures the first and third items (the third element in a slice sequence is the step size).
대안으로 앞장 2.3.5에서 배운 그 전설의 절단검, **슬라이스(slices)** 마법을 끄집어내어 행렬들을 한 줄로 훅훅 효율적으로 썰어버릴 수도 있습니다. 마법 주문 `1:4:2` (1번부터 3번방까지, 2보폭으로 뛰어라!)는 순서의 2번째와 4번째 녀석만 포박해 채가고, 세로줄 주문 `0:3:2` 는 제일 앞놈과 세 번째 녀석 목줄만 사로잡는(captures) 화려한 이도류 칼춤을 보여줍니다 (마지막 3번째 칸 숫자는 당연히 보폭 징검다리 점프 크기인 건 안 까먹으셨죠?).

```python
In [65]: A[1:4:2, 0:3:2]
Out[65]: array([[ 4,  6],
                [12, 14]])
```

Why are we able to retrieve a submatrix directly using slices but not using lists? Its because they are different `Python` types, and are treated differently by `numpy`. Slices can be used to extract objects from arbitrary sequences, such as strings, lists, and tuples, while the use of lists for indexing is more limited.
여기서 질문! 아까 '리스트 명부'를 쌍으로 던졌을 땐 에러를 뿜으며 멍청한 짓을 하더니, 왜 이 '슬라이스 부호' 쌍을 넣을 땐 찰떡같이 그물망 방식으로 행렬 서브 셋을 직접 쫙쫙 아름답게 건져 올리는 걸까요? 간단합니다. 넘파이(`numpy`) 뇌 구조에선 이 두 개가 신분 계급 자체가 전혀 다른 파이썬 종족들(types)이어서, 완전히 급을 다르게 취급하기 때문입니다. 슬라이스(Slice) 칼은 글자, 리스트, 튜플 등 파이썬 세상 모든 시퀀스를 도륙낼 수 있는 마스터 소드지만, 반면 콤마 찍은 리스트(list) 따위를 명찰표 용도로 넘파이에 갖다 쓰는 짓은 그 허당 제약성(limited)이 무척 빡빡한 탓이죠.

## Boolean Indexing
## 불리언(Boolean) 인덱싱 (참치와 꽁치 걸러내는 진실의 그물)

In `numpy`, a _Boolean_ is a type that equals either `True` or `False` (also represented as 1 and 0, respectively).
파이썬 넘파이 세계에서 가장 살벌한 분류법, **_불리언(Boolean)_** 요원들의 존재감이 드러날 차례입니다. 불리언이란 "이것은 기필코 참(`True`)이다!" 아니면 "이것은 새빨간 거짓(`False`)이다!"라는 극단적 양자택일 상태만을 가진 데이터 혈통을 말합니다. (아, 심심하면 가끔 흑백 필터 씌워서 참은 `1`, 거짓은 `0` 숫자로 둔갑해서 나타나기도 합니다.)

The next line creates a vector of 0’s, represented as Booleans, of length equal to the first dimension of `A`.
이어질 무자비한 코드는 거대 배열 `A` 의 가로 세로 덩치 크기와 똑같은 길이의, 모두 새까만 거짓말인 `0(False)` 상태를 부여받은 빈 수건 돌리기용 불리언 군단 일렬 벡터 배열을 생성해 도열시킵니다.

We now set two of the elements to `True`.
그런 다음 우린 요원들 사이를 걸어가며 딱 두 명의 요원 머리통 스위치만 탁탁 눌러 빛의 요원(`True`)으로 무단 설정 조작 귀순을 시킵니다.

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
흥미로운 점! 방금 우리가 공작한 `keep_rows` 빛의 요원 배열표를 파이썬의 숫자 필터로 슥 훑어보면 무식하게 생긴 강박증 숫자 배열 `np.array([0, 1, 0, 1])` 과 영혼 쌍둥이처럼 똑같은 치수들을 품고 있다는 점에 주목하십시오.
아래에서, 우리는 진실의 거울인 `==` (똑같냐?) 기호를 등판시켜 그들의 유전자 단위 부합 동등성을 심판대에 검증시킵니다. 이 `==` 연산 심판봉은 두 집단을 통째로 재지 않고, 줄 세워놓고 각 위치 병사들끼리 한 명씩 원소별(elementwise)로 치밀하게 마스크를 벗겨 검문 처리하는 깡패 필터 방식입니다.

```python
In [68]: np.all(keep_rows == np.array([0, 1, 0, 1]))
Out[68]: True
```

(Here, the function `np.all()` has checked whether all entries of an array are `True`. A similar function, `np.any()`, can be used to check whether any entries of an array are `True`.)
(깨알 팁 하나 가슴에 품으세요. 여기서 등장한 형사 가제트 함수 `np.all()` 은 "수용소 안의 모든 죄수(출입 항목)가 단 한 명도 빠짐없이 `True` 병이 걸렸느냐?"를 철두철미하게 뒤지는 감식반입니다. 반면 그의 허술한 파트너 형사 `np.any()` 는 "야, 아무나 한 명이라도 `True` 걸린 놈 있냐?" 하고 한 명만 보여도 사건 종결 내버리는 빠른 서칭을 위해 쓰이곤 한답니다.)

However, even though `np.array([0, 1, 0, 1])` and `keep_rows` are equal according to `==`, they index different sets of rows!
하지만 대반전 호러 스펙터클! 설사 `np.array([0, 1, 0, 1])` 정수 군단과 `keep_rows` 불리언(True/False) 요원 군단이 거울 잣대 `==` 앞에서 DNA가 일치하는 한 핏줄이라고 떴을지언정, 막상 이 두 부대를 지휘봉(인덱싱 도구)으로 배열 사냥에 등판시키면 완전히 딴 세상의 다른 사냥감 행(rows)들 무리 세트를 낚아채 오는 대형 방송사고를 일으킵니다!

```python
In [69]: A[np.array([0, 1, 0, 1])]
Out[69]: array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [0, 1, 2, 3],
                [4, 5, 6, 7]])
```

The former retrieves the first, second, first, and second rows of `A`.
전자(정수 군단) 놈들은 너무 우직해서, 명령표에 적힌 0, 1, 0, 1 숫자를 보곤 앵무새처럼 "아하! 0층 한 번, 1층 한 번, 다시 0층 한 번, 다시 1층 한 번 가져오라는 거네?" 하면서 멍청하게 원본 아파트 `A` 의 첫 번째와 두 번째 층만 무한 반복해서 발췌 복사해 옵니다. 

By contrast, `keep_rows` retrieves only the second and fourth rows of `A` — i.e. the rows for which the Boolean equals `True`.
그에 반해, 후자의 똑똑한 암살 요원 군단 `keep_rows` 진실 그물망은 전혀 다르게 투척됩니다. 이 녀석들은 아파트 `A` 앞마당에 쭉 서서 "음~ 1층은 버리고 2층은 챙기고 3층은 버리고 4층은 챙기고!" 이런 식으로 자기 배지 상태표(`Boolean`)가 `True`(빛의 요원 조명)라고 번쩍번쩍 빛나는 위치 지점들에 상주하는 행들만 정갈하게 생포 압수해 냅니다! 놀라운 차이죠.

```python
In [70]: A[keep_rows]
Out[70]: array([[ 4,  5,  6,  7],
                [12, 13, 14, 15]])
```

This example shows that Booleans and integers are treated differently by `numpy`.
이 호러 반전 예제가 뼈저리게 가르쳐주는 교훈! 넘파이(`numpy`) 독재 체제 내부에선, 1/0 정수 군벌 나부랭이와 True/False 특수 불리언 혈통은 눈에 뻔히 같아 보여도 그 체급과 취급 방식 대우가 완전히 뼛속부터 다르다는 극명한 진실을 증명해 시사합니다.

We again make use of the `np.ix_()` function to create a mesh containing the second and fourth rows, and the first, third, and fourth columns.
충격은 거두고 다시 실전으로 돌아갑니다. 우리는 2, 4층을 장악하고 1, 3, 4호 구역을 쑥대밭으로 만들 전용 그물망(mesh)을 짜기 위해, 아까 그 훌륭한 요술 부채 마법 함수 `np.ix_()` 님을 다시 한번 더 등판 무대에 소환시킵니다.

This time, we apply the function to Booleans, rather than lists.
근데 이번 작전 구역에선 한 가지 변칙을 줍니다! 예전 멍청한 단순 정수 리스트 명부 따위를 던졌던 것 대신에 차라리 독기가 바짝 오른 **불리언(`True`/`False`) 지문 리스트 군단**을 해당 요술 부채 함수의 작동 엔진에 쑥 밀어 넣어 부과 타격시켜 봅니다.

```python
In [71]: keep_cols = np.zeros(A.shape[1], bool)
         keep_cols[[0, 2, 3]] = True
         idx_bool = np.ix_(keep_rows, keep_cols)
         A[idx_bool]
Out[71]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

We can also mix a list with an array of Booleans in the arguments to `np.ix_()`:
심지어! 우리 편의 만능 요술 부채 `np.ix_()` 의 입속(인자 구간 통로)에는 가로세로 줄을 던질 때 하나는 '멍청한 단순 정수 리스트'를 끼우고, 반대쪽은 '스마트 불리언 진릿값 배열'을 치밀하게 **혼합(mix) 짬짜면**해 투척해도 토하지 않고 소화해 낼 넉넉한 포용 공산을 갖추고 탑재했습니다:

```python
In [72]: idx_mixed = np.ix_([1, 3], keep_cols)
         A[idx_mixed]
Out[72]: array([[ 4,  6,  7],
                [12, 14, 15]])
```

For more details on indexing in `numpy`, readers are referred to the `numpy` tutorial mentioned earlier.
이 지옥불 같은 `numpy` 그물 던지기 인덱싱 편법 농간 기술들의 더 끝이 없는 심연 세부 옵션들이 내심 당기시나요? 코피 한 번 터져보길 바라는 용기 있는 제현 독자들께선, 이 글 앞단에서 아까 던져 줬던 그 전설의 절대경전 **공식 `numpy` 튜토리얼 성지 링크로 가셔서** 날밤을 새며 무림 비급을 단연코 더 파고 참조 정독하시길 눈물 어린 당부의 말씀을 전합니다!

---

## Sub-Chapters

[< 2.3.5 Sequences And Slice Notation](../2_3_5_sequences_and_slice_notation/trans2.html) | [2.3.7 Loading Data >](../2_3_7_loading_data/trans2.html)
