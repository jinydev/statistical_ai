---
layout: default
title: "trans2"
---

[< 2.3.4 Graphics](../2_3_4_graphics/trans2.html) | [2.3.6 Indexing Data >](../2_3_6_indexing_data/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.5 Sequences and Slice Notation
# 2.3.5 시퀀스 기차와 썰어 조각내기(Slice) 칼질 기법

As seen above, the function `np.linspace()` can be used to create a sequence of numbers.
윗동네 그래픽 단원에서도 이미 슬쩍 맛봤듯이, 우리가 애용하는 마법의 `np.linspace()` 칼잡이 함수는 시작과 끝을 정해주면 그사이를 일정하게 토막내 숫자들이 일렬종대로 쫙 도열한 **시퀀스(sequence, 기차 배열)** 하나를 군말 없이 생성해 줄 때 아주 기특하게 쓰입니다.

```python
In [52]: seq1 = np.linspace(0, 10, 11)
         seq1
Out[52]: array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
```

The function `np.arange()` returns a sequence of numbers spaced out by `step`.
근데 솔직히 등분 내기는 머리 아프잖아요? 그럴 땐 더 원초적인 동생 함수인 `np.arange()` 를 부르세요. 얘는 보폭 즉 `step` 간격 크기만을 주면 시작점부터 일정한 보폭으로 껑충껑충 띄어 넘어가는 숫자 시퀀스 기차 하나를 휙 반환해 주는 아주 직관적인 녀석입니다.

If `step` is not specified, then a default value of 1 is used.
만약 이 귀찮은 보폭 `step` 옵션 자체를 입에 올리지도 않고 생략하면? 알아서 착하게 "아, 1칸씩 가라는 거구나" 하고 기본값(default) 1로 알아들어 먹습니다.

Let’s create a sequence that starts at 0 and ends at 10.
백문이 불여일타! 당장 0번 역에서 출발하고 10번 역 언저리에서 과감히 끝나는 1보폭짜리 단출한 시퀀스 배열 기차를 생성해 봅시다.

```python
In [53]: seq2 = np.arange(0, 10)
         seq2
Out[53]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

Why isn’t 10 output above?
잠깐...! 내 눈이 잘못됐나요? 분명 10에서 끝나라고 0부터 10까지 줬는데, 왜 위 결과창 배열 끄트머리엔 10이라는 대문짝만 한 숫자가 결코 출력되지(output) 않은 걸까요? 파이썬이 사기 치는 걸까요?

This has to do with _slice_ notation in `Python`.
억울해 마십시오. 이것은 사기가 아니라 위대한 `Python` 세계관을 통치하는 고유의 **_슬라이스(slice)_ 표기 문법**의 지독한 배타성과 뼛속 깊이 연관이 있는 현상입니다.

Slice notation is used to index sequences such as lists, tuples and arrays.
이 슬라이스(조각칼 썰기) 표기법이란, 앞서 설명한 삼형제인 리스트들, 튜플들, 그리고 거대 배열들과 같은 제반 시퀀스 기차 무리에 접근조작(인덱싱, indexing)하기 위해 필수적으로 쓰이는 특수 요리칼 문법입니다.

Suppose we want to retrieve the fourth through sixth (inclusive) entries of a string.
가령 퀴즈 하나 볼까요? 일렬로 늘어선 어떤 글자 문자열 속에서 우리 입맛에 맞게 **네 번째부터 여섯 번째 단어까지의 (6번째 자신을 포함한) 항목들만을** 쏙 반환받아 끄집어내고 싶다고 단단히 가정해 봅시다.

We obtain a slice of the string using the indexing notation `[3:6]`.
놀라지 마십시오! 우리는 인덱싱 표기 기호로 `[4:6]` 이 아니라 기괴하게도 `[3:6]` 이라는 엽기적인 톱질 기호를 사용해야만 우리가 원했던 그 문자열 한 조각의 슬라이스를 온당 획득할 수 있습니다!

```python
In [54]: "hello world"[3:6]
Out[54]: 'lo '
```

In the code block above, the notation `3:6` is shorthand for `slice(3, 6)` when used inside `[]`.
위의 코드 블록 요리판 안에서, 대괄호 `[]` 사이에 낀 저 엽기적인 표기 `3:6` 이란 기호는 파이썬 전용 도마 위에서 엄밀히 말해 `slice(3, 6)` 이라는 본래 함수의 뼈대를 깎아 만든 단축 축약형 암호 기호일 뿐입니다.

```python
In [55]: "hello world"[slice(3, 6)]
Out[55]: 'lo '
```

You might have expected `slice(3, 6)` to output the fourth through seventh characters in the text string (recalling that `Python` begins its indexing at zero), but instead it output the fourth through sixth.
자, 아까 우리가 "파이썬 이놈은 1층이 아니라 0층(Zero-based indexing)부터 샌다!"라는 엽기 룰을 배웠지 않습니까? 그래서 그걸 감안해 독자 여러분은 짐짓 `slice(3, 6)` 이 들어오면 텍스트 문자열 내의 "네 번째 문자[3]부터 일곱 번째 문자[6]까지"를 내내 부단 출력하길 당당히 예상(expected)했을 겁니다. 그러나 잔혹하게도 이 슬라이스 룰은 마지막 절단면 [6]번 칸 자체는 도마 바깥으로 버려 포함하지 않고, 오직 "네 번째[3]부터 바로 전 칸인 여섯 번째[5]까지만"을 지표 출력 도출해 냅니다! (**시작점은 포함하되, 끝점은 배제한다!** 이것이 파이썬의 핵심 룰입니다!)

This also explains why the earlier `np.arange(0, 10)` command output only the integers from 0 to 9.
바로 이 "끝점은 배제하고 버린다"라는 끔찍한 슬라이싱 법칙이, 덧붙여 아까 윗단에서 우리가 `np.arange(0, 10)` 명령을 내렸을 때 파이썬이 왜 감히 10을 쏙 빼먹고 단지 0에서 필경 9까지의 정수들만을 전단 출력 배출했는지 그 속 깊은 기저 연유를 명쾌하게 부연 설명 지어줍니다.

See the documentation `slice?` for useful options in creating slices.
이 외에도 데이터를 요리조리 내 맘대로 썰고 깎는 슬라이스 조각 생성법엔 무수한 신기 옵션이 산재합니다! 단초 `slice?` 매뉴얼을 타건해 직접 찾아보며 그 유용한 칼질 옵션의 세계를 필시 구경해 보시길!

---

## Sub-Chapters

[< 2.3.4 Graphics](../2_3_4_graphics/trans2.html) | [2.3.6 Indexing Data >](../2_3_6_indexing_data/trans2.html)
