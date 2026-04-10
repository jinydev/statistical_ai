---
layout: default
title: "index"
---

# _2.3.5 Sequences and Slice Notation_
# 2.3.5 시퀀스와 슬라이스 표기법 (Sequences and Slice Notation)

As seen above, the function `np.linspace()` can be used to create a sequence of numbers.

위에서 본 것처럼, `np.linspace()` 함수는 숫자로 이루어진 연속된 단위 시퀀스를 생성하는 데 적용될 수 있습니다.

```python
In [52]: seq1 = np.linspace(0, 10, 11)
         seq1
Out[52]: array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
```

The function `np.arange()` returns a sequence of numbers spaced out by `step`. If `step` is not specified, then a default value of 1 is used. Let’s create a sequence that starts at 0 and ends at 10.

`np.arange()` 함수는 지정된 `step` 간격만큼 띄어져 나열된 숫자들의 연속 시퀀스를 돌려줍니다. 만약 이 `step` 파라미터가 명확히 지정되지 않는다면, 기본 설정 수치인 단위 1이 자동으로 적용됩니다. 그럼 이제 숫자 0에서 시작하여 10에서 마무리되는 시퀀스 배열을 새롭게 하나 생성해 봅시다.

```python
In [53]: seq2 = np.arange(0, 10)
         seq2
Out[53]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

Why isn’t 10 output above? This has to do with _slice_ notation in `Python`. Slice notation is used to index sequences such as lists, tuples and arrays. Suppose we want to retrieve the fourth through sixth (inclusive) entries of a string. We obtain a slice of the string using the indexing notation `[3:6]`.

결과 화면에서 어째서 도출된 마무리 숫자 10이 나타나지 않았을까요? 그 해답은 `Python` 체제 내부의 _슬라이스(slice)_ 인덱싱 표기법 구조와 깊게 연관되어 있습니다. 슬라이스 표기법 체계는 프로그램 배열(arrays), 튜플(tuples), 리스트(lists) 같은 반복 정보 시퀀스 항목들을 참조 인덱싱할 때 주로 활용됩니다. 예컨대 우리가 제공된 표면 문자열 기호 내용 중 네 번째 글자 위치부터 여섯 번째 요소 자리 범위(포함)까지만 뽑아 단편 추출하고 싶다고 상상해 봅시다. 우리는 이때 `[3:6]` 이라는 전용 구간 인덱싱 단축 표기법을 통해 문자열의 한정 범위인 특정 슬라이스를 전격 할당 얻을 수 있습니다.

```python
In [54]: "hello world"[3:6]
Out[54]: 'lo '
```

In the code block above, the notation `3:6` is shorthand for `slice(3, 6)` when used inside `[]`.

위의 예제 코드 구문 블록에서 작성 사용된 `3:6` 수식 표기법은 시스템 대괄호인 `[]` 안에서 활용 모의될 때, 사실상 `slice(3, 6)` 함수 속성 형태를 단순히 짧게 생략해 표기하는 조절 요약식 표현에 지나지 않습니다.

```python
In [55]: "hello world"[slice(3, 6)]
Out[55]: 'lo '
```

You might have expected `slice(3, 6)` to output the fourth through seventh characters in the text string (recalling that `Python` begins its indexing at zero), but instead it output the fourth through sixth. This also explains why the earlier `np.arange(0, 10)` command output only the integers from 0 to 9. See the documentation `slice?` for useful options in creating slices.

여러분 중에는 (`Python` 코딩 구조가 배열 인덱싱 카운트를 숫자 0부터 먼저 시작한다는 구조 원리를 되새기면서) 함수 모형 `slice(3, 6)` 이 곧 대상 문자열에서 네 번째부터 일곱 번째의 마지막 문자열 요소까지 포괄하여 추출해 결과 화면에 돌려보낼 것이라고 내심 예상했을지도 모릅니다. 하지만 기대와 달리 해당 프로세스는 실제로는 오로지 네 번째 문자부터 여섯 번째까지의 위치 단어만을 한정 결과로 도출 출력합니다. 바로 이러한 고유 단절 원리가, 우리가 앞서 조금 전 작성 구동했던 `np.arange(0, 10)` 구문 동작 코드가 어째서 수치 10까지 포함시키지 않고 0부터 9까지 한계 수치의 척도 정수만을 산출하여 돌려주었는지를 한눈에 매우 명확히 설명해 줍니다. 새로운 연속 부분 슬라이스를 설정 생산해 구성할 때 내부 필요한 더 세밀한 시스템 유용 옵션들을 알아보기 원한다면 콘솔 도움말 `slice?` 명령 문서를 전격 실행 호출해 참조해 주십시오.

---

## Sub-Chapters (하위 목차)

현재 2.3.5 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)
