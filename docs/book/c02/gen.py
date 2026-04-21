import os
import codecs

base_dir = r'd:\\site\\jinydev\\Statistical\\src\\book\\c02\\2_3_lab_introduction_to_python'
dirs = [
    '2_3_1_getting_started',
    '2_3_2_basic_commands',
    '2_3_3_introduction_to_numerical_python',
    '2_3_4_graphics',
    '2_3_5_sequences_and_slice_notation',
    '2_3_6_indexing_data',
    '2_3_7_loading_data',
    '2_3_8_for_loops',
    '2_3_9_additional_graphical_and_numerical_summaries'
]

titles = [
    '2.3.1 Getting Started (시작하기: 무기 장착)',
    '2.3.2 Basic Commands (기본 명령어: 방아쇠 당기기)',
    '2.3.3 Introduction to Numerical Python (NumPy: 숫자 마법사)',
    '2.3.4 Graphics (그래픽: 화려한 시각화 마법)',
    '2.3.5 Sequences and Slice Notation (시퀀스와 슬라이싱: 무 썰기)',
    '2.3.6 Indexing Data (데이터 인덱싱: 알짜배기만 골라내기)',
    '2.3.7 Loading Data (데이터 로딩: 거대한 식재료 가져오기)',
    '2.3.8 For Loops (for 반복문: 똑똑한 노가다 기계)',
    '2.3.9 Additional Graphical and Numerical Summaries (데이터 스캔하기)'
]

descriptions = [
    '파이썬을 처음 시작할 때 주피터(Jupyter)라는 훌륭한 도화지를 펴고, 필요한 외부 패키지(무기)들을 장착하는 영점 사격 훈련입니다.',
    '더하기, 빼기부터 시작해서 `print()`처럼 화면에 글씨를 띄워보는 가장 원시적이지만 위대한 파이썬의 첫걸음입니다.',
    '데이터 과학의 알파요 오메가인 `NumPy`입니다. 수백만 개의 엑셀 칸을 1초 만에 조작하는 다차원 배열과 난수(랜덤 주사위)를 굴리는 법을 배웁니다.',
    '`Matplotlib`을 활용해 숫자들을 그림으로 바꾸는 마법입니다. 산점도부터 윤곽선 지도까지 데이터를 한눈에 파악하는 기술입니다.',
    '긴 밧줄(데이터)에서 내가 딱 원하는 구간만 가위로 싹둑 잘라내는(Slicing) 아주 섬세하고 강력한 인덱싱 배열 조작법입니다.',
    '"30살 이상만 모여라!" 처럼 진릿값(True/False) 조건표를 이용해 방대한 데이터의 바다에서 내가 원하는 물고기만 그물로 건져 올리는 기술입니다.',
    '`Pandas`를 이용해 컴퓨터 하드에 잠들어 있는 거대한 CSV/엑셀 데이터 파일을 밥상 위로 끌어올리는 아주 중요한 첫 시작점입니다.',
    '수만 개의 파일이나 연산을 인간이 직접 할 순 없습니다. 파이썬에게 "이거 1만 번 반복해!" 라고 시키는 자동화의 핵심, 반복문입니다.',
    '`describe()` 명령어로 데이터의 평균과 최댓값을 1초 만에 훑어보고, 박스 플롯이나 히스토그램으로 정보의 맥락을 전체적으로 스캔하는 레이더 기술입니다.'
]

for i, d in enumerate(dirs):
    trans2_path = os.path.join(base_dir, d, 'trans2.md')
    
    prev_link = ''
    next_link = ''
    
    if i == 0:
        prev_link = '[< 2.3 Lab Introduction to Python](../trans2.html)'
    else:
        prev_link = f'[< {titles[i-1].split(" (")[0]}](../{dirs[i-1]}/trans2.html)'
        
    if i == len(dirs) - 1:
        next_link = '[2.4 Exercises >](../../2_4_exercises/trans2.html)'
    else:
        next_link = f'[{titles[i+1].split(" (")[0]} >](../{dirs[i+1]}/trans2.html)'

    content = f"""---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 직접 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

{prev_link} | {next_link}

# {titles[i].split(" (")[0]}
# {titles[i]}

{descriptions[i]}
(자세한 파이썬 실습 코드와 원문의 1:1 번역은 [직역본](./trans1.html)을 참조하세요.)

---

## Sub-Chapters (하위 목차)

{prev_link} | {next_link}
"""
    
    with codecs.open(trans2_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {trans2_path}")
