---
layout: default
title: "trans1"
---

[< 2.3.4 Graphics](../2_3_4_graphics/trans1.html) | [2.3.6 Indexing Data >](../2_3_6_indexing_data/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 2.3.5 Sequences and Slice Notation

# 2.3.5 시퀀스들과 슬라이스 표기법

As seen above, the function `np.linspace()` can be used to create a sequence of numbers.

위에서 보이듯, 함수 `np.linspace()` 는 숫자들의 시퀀스 하나를 생성하기 위해 사용될 수 있습니다.

```python
In [52]: seq1 = np.linspace(0, 10, 11)
         seq1
Out[52]: array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
```

The function `np.arange()` returns a sequence of numbers spaced out by `step`.

함수 `np.arange()` 는 `step` 간격으로 떨어진 숫자들의 시퀀스 하나를 반환합니다.

If `step` is not specified, then a default value of 1 is used.

만약 `step` 이 명시되지 않으면, 1이라는 기본값이 사용됩니다.

Let’s create a sequence that starts at 0 and ends at 10.

0에서 시작하고 10에서 끝나는 하나의 시퀀스를 생성해 봅시다.

```python
In [53]: seq2 = np.arange(0, 10)
         seq2
Out[53]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

Why isn’t 10 output above?

왜 위에서 10이 출력되지 않습니까?

This has to do with _slice_ notation in `Python`.

이것은 `Python` 안의 _슬라이스(slice)_ 표기법과 연관이 있습니다.

Slice notation is used to index sequences such as lists, tuples and arrays.

슬라이스 표기법은 리스트들, 튜플들, 그리고 배열들과 같은 시퀀스들을 인덱스하기 위해 사용됩니다.

Suppose we want to retrieve the fourth through sixth (inclusive) entries of a string.

우리가 한 문자열의 네 번째부터 여섯 번째까지의 (스스로를 포함하는) 항목들을 반환받기를 원한다고 가정해 봅시다.

We obtain a slice of the string using the indexing notation `[3:6]`.

우리는 인덱싱 표기 `[3:6]` 을 사용하여 해당 문자열의 한 슬라이스를 획득합니다.

```python
In [54]: "hello world"[3:6]
Out[54]: 'lo '
```

In the code block above, the notation `3:6` is shorthand for `slice(3, 6)` when used inside `[]`.

위 코드 블록 안에서, 표기 `3:6` 은 `[]` 안에서 사용될 때 `slice(3, 6)` 에 대한 축약형입니다.

```python
In [55]: "hello world"[slice(3, 6)]
Out[55]: 'lo '
```

You might have expected `slice(3, 6)` to output the fourth through seventh characters in the text string (recalling that `Python` begins its indexing at zero), but instead it output the fourth through sixth.

여러분은 `slice(3, 6)` 이 텍스트 문자열 내의 네 번째부터 일곱 번째 단면 문자들까지 내내 부단 출력하길 여과 없이 단연 예상했을 당면 수가 있습니다 (`Python` 이 숫자 0에서부터 그것의 그 인덱싱을 당면 시작함을 분명 일관 상기 관조하며), 그러나 역상 대신에 그것은 네 번째부터 무결 이내 오직 여섯 번째까지만을 지표 일체 출력 도출했습니다.

This also explains why the earlier `np.arange(0, 10)` command output only the integers from 0 to 9.

이것은 덧붙여 또한 어떻게 단연코 앞선 무단 `np.arange(0, 10)` 지표 명령 조작 단락이 오직 단위 0 에서 필경 종결 9 까지의 무결 정수들만을 전방 제한 일렬 출력 산출 도치했는지 지표 그 연유를 말끔 설명 부연합니다.

See the documentation `slice?` for useful options in creating slices.

다수 슬라이스들을 거듭 생성 축조함에 있어 다분 거론 유용한 당 옵션들을 단연 알기 위해 단초 `slice?` 매뉴얼 속 문서를 찾아 필시 확인 보십시오.

---

## Sub-Chapters (하위 목차)

[< 2.3.4 Graphics](../2_3_4_graphics/trans1.html) | [2.3.6 Indexing Data >](../2_3_6_indexing_data/trans1.html)
