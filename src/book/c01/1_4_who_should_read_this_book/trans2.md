---
layout: default
title: "trans2"
---

[< 1.3 This Book](../1_3_this_book/trans2.html) | [1.5 Notation And Simple Matrix Algebra >](../1_5_notation_and_simple_matrix_algebra/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# Who Should Read This Book?
# 이 책은 누가 읽어야 하는가? (이 책을 냄비 받침으로 쓰지 않을 자들)

This book is intended for anyone who is interested in using modern statistical methods for modeling and prediction from data.
이 책은 그득그득 쌓여있는 쓰레기(데이터) 속에서 진주를 찾아내어 내일의 떡상을 찍어내는 마법(모델링 예측)을 부리고 싶어 환장하는 모든 분들을 안아주기 위해 만들어졌습니다.

This group includes scientists, engineers, data analysts, data scientists, and quants, but also less technical individuals with degrees in non-quantitative fields such as the social sciences or business.
이 축복받은 독자 클럽에는 당연히 허구한 날 엑셀과 싸우는 데이터 분석가, 퀀트(금융 천재), 엔지니어 같은 이과생들도 VIP로 모십니다. 하지만! 이 클럽의 진짜 알짜배기 손님은, 평생 숫자는 세어본 적도 없는 문과 감성의 끝판왕들(사회 과학이나 경영학 나오신 분들)까지 포함된다는 놀라운 사실을 잊지 마십시오! (덜 기술적인 비전공자 대환영!)

We expect that the reader will have had at least one elementary course in statistics.
아, 물론 우리가 보살은 아닙니다. 최소한의 양심으로, 여러분이 대학교 1학년 때 교양 필수로 듣다가 졸아버렸던 그 흔해 빠진 '기초 통계학' 과목 하나 정도는 수강신청해 봤을 거라고(기본 바탕) 믿어 의심치 않습니다.

Background in linear regression is also useful, though not required, since we review the key concepts behind linear regression in Chapter 3.
혹시 옛날에 '선형 회귀'를 배워본 기억이 머릿속 파편으로 남아있다면 베스트입니다! 하지만 걱정하지 마세요. 3장으로 넘어가면 우리가 기초부터 다시 밥상 차려 떠먹여 드릴 텐데, 모른다고 징징대도 필수는 아니니 쫓아내진 않겠습니다.

The mathematical level of this book is modest, and a detailed knowledge of matrix operations is not required.
당신이 가장 쫄아있는 이 책의 잔혹한 '수학적 맵기(수준)'? 오, 다행히도 진라면 순한 맛 수준(modest)입니다! 괜히 칠판 꽉 채우며 행렬 더하고 곱하는 그 끔찍한 대학수학 지식(상세한 행렬 연산) 따윈 눈을 씻고 찾아봐도 없으니 제발 도망가지 마십쇼!

This book provides an introduction to Python.
이 서적은 최근 제일 잘나간다는 '파이썬(Python)' 코딩을 다루는 입문 티켓을 끊어드립니다.

Previous exposure to a programming language, such as MATLAB or R, is useful but not required.
혹여나 당신이 과거에 꼰대들만 쓴다는 매트랩(MATLAB)이나 R 같은 걸 주워들어본 적이 있다면 완전 땡큐지만, 만약 처음 보는 생초보 컴맹이라 해도 안 잡아먹습니다(필수 아님).

The first edition of this textbook has been used to teach master's and PhD students in business, economics, computer science, biology, earth sciences, psychology, and many other areas of the physical and social sciences.
저희가 이 책 1판을 가지고 실제로 대학에서 팔아먹어(가르쳐) 본 결과, 문과, 이과, 예체능(?) 가릴 것 없이 경영, 컴퓨터, 심지어 심리학과나 돌멩이 캐는 지구 과학과 박사 과정 노예(학생)들까지 전부 불러다 앉혀놓고 재미를 톡톡히 봤다 이 말입니다.

It has also been used to teach advanced undergraduates who have already taken a course on linear regression.
물론 대학원생 말고도, 머리가 좀 굵어져서 선형 회귀 정도는 떼고 코를 파는 잘난 학부생(학사 짬바)들한테도 가르쳤을 때 아주 잘 먹혔습니다.

In the context of a more mathematically rigorous course in which ESL serves as the primary textbook, ISL could be used as a supplementary text for teaching computational aspects of the various approaches.
혹시나 교수님이 미쳐서 그 끔찍한 수학 마라맛 벽돌책(ESL)을 메인 교재로 지정한 그지 같은 전공 수업일지라도, 이 책 ISL을 "수식은 도저히 못 풀겠으니 컴퓨터 코드(전산화 실습)라도 외우자!"며 몰래 펴보는 꿀통 보조 교재로 스윽 끼워 넣기에도 아주 환상적입니다.

---

## Sub-Chapters (하위 목차)

[< 1.3 This Book](../1_3_this_book/trans2.html) | [1.5 Notation And Simple Matrix Algebra >](../1_5_notation_and_simple_matrix_algebra/trans2.html)
