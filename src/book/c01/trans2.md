---
layout: default
title: "trans2"
---

[1.1 An Overview Of Statistical Learning >](1_1_an_overview_of_statistical_learning/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# 1. Introduction
# 1. 서론 (통계적 학습이라는 놀이공원에 오신 것을 환영합니다!)

This introduction introduces the overall background and purpose of the materials covered in this book. 
이 서론 파트에서는 앞으로 이 두꺼운 책에서 우리가 대체 뭘 배우려고 이 고생을 하는지, 그 은밀한 배경과 웅대한 목적을 살짝 맛보기로 핥아봅니다.

It examines the importance of statistical learning and major datasets, and guides you through the prerequisite knowledge necessary for learning.
왜 요즘 전 세계가 '통계적 학습(인공지능)'이라는 마법에 열광하고 목매달고 있는지 그 미친 중요성을 살펴보고, 우리가 책을 씹어 먹기 위해 장착해야 할 기본 필수 템(사전 지식)들을 친절하게 가이드해 드립니다.

## 1.1 An Overview of Statistical Learning (통계적 학습 개요: 기계가 공부하는 법)

This section provides an overview of what Statistical Learning is, exploring it through various examples and problems. 
이 고개에서는 도대체 그 잘난 '통계적 학습(Statistical Learning)'이 뭔 놈의 기술인지, 일상생활의 침 튀기는 재밌는 썰과 문제 상황들을 예시로 들어가며 큰 그림으로 구경해 봅니다.

It suggests the basic direction of how statistical methods are utilized in modern data analysis.
나아가 오늘날 쏟아지는 빅데이터 분석판에서 옛날 통계 기법들이 도대체 어떻게 딥러닝 못지않게 사골처럼 우려 먹히고(활용되는지) 있는지 그 뼈대 방향성을 확 잡아드립니다.

## 1.2 A Brief History of Statistical Learning (통계적 학습의 간략한 역사: 고인물들의 연대기)

It covers a brief history focusing on major milestones of how statistics and machine learning have evolved from the past to the present.
할아버지들이 주판알이나 튕기던 옛날 옛적 구석기 통계학 시절부터, 지금의 최첨단 머신러닝 로봇 시대까지 어떻게 이 학문이 진화하며 폭풍 성장했는지 그 피 튀기는 굵직한 역사 연대기를 빠르게 훑어봅니다.

You can understand the historical context in which the data science field was formed and the background behind the emergence of major methodologies.
이걸 알고 나면 "아! 이래서 현재 데이터 과학이라는 미친 짬뽕 학문이 탄생했구나!" 하는 역사적 맥락과, 여러분을 괴롭힐 수많은 수학 공식들이 대체 왜 세상에 기어 나와야만 했는지 그 짠한 사연(배경)을 이해할 수 있습니다.

## 1.3 This Book (이 책에 대하여: 왜 하필 이 책인가?)

It explains the purpose for which this book was written, and what distinctions and characteristics it has compared to other textbooks.
시중에 널리고 널린 게 데이터 과학 책인데, "도대체 저자들이 무슨 배짱으로 이 책을 또 썼는지" 그 불순한 목적(?)과, 다른 교과서들과 비교 불가능한 이 책만의 킹왕짱 매력 포인트(차별점과 특징)가 뭔지 자랑을 좀 늘어놓습니다.

It notes that the focus is on a practical approach and application using Python rather than deep theoretical depth.
자랑의 핵심은 이겁니다! "우리는 머리털 빠지는 수학 증명(침울한 이론적 깊이) 따윈 개나 주고, 당장 파이썬(Python) 키보드를 두들기며 실전에 바로 써먹을 수 있는(실용적 접근과 응용) 꿀팁에만 몰빵했다!"는 걸 강조합니다.

## 1.4 Who Should Read This Book? (이 책은 누가 읽어야 하는가?: 당신을 위한 맞춤 저격수)

It defines the target audience of this textbook with respect to academic backgrounds and interests.
이 교재를 냄비 받침으로 쓰지 않고 뼛속까지 씹어 먹을 수 있는 진정한 용사들(대상 독자)이, 도대체 어떤 스펙(학문적 배경)과 취향(관심사)을 가진 사람들인지 콕 집어 정의 내려 줍니다.

It explains that this book is suitable for industry practitioners and non-majors who want to apply data modeling to practice, even without advanced mathematical knowledge.
요약하자면 "당신이 비록 수학의 정석조차 다 못 뗀 수포자(문과생, 비전공자) 일지라도, 당장 회사 데이터를 쥐고 인공지능 모델을 빙의 시켜 돈을 벌어오고 싶은 실무자라면 이 책이 아주 찰떡같이 입에 맞을 거다!"라고 영업을 뜁니다.

## 1.5 Notation and Simple Matrix Algebra (표기법 및 간단한 행렬 대수: 수학 외계어 번역기 가이드)

It summarizes the statistical and mathematical notation and basic vector and matrix operation rules that will be used throughout the book.
앞으로 책장 넘길 때마다 튀어나올 알파벳과 그리스어의 참극! 그 지옥 같은 통계적 수학 기호(Notation)들과 엑셀 표 같은 벡터/행렬이 어떻게 더해지고 곱해지는지 그 최소한의 기본 룰만 살포시 요약해 드립니다.

It provides clear rules on how to mathematically represent data structures for readers who are not familiar with formulas.
수식만 보면 두드러기가 나는 수포자 독자 여러분을 위해, 우리가 모은 데이터 덩어리를 어떻게 수학 숫자 표기법으로 약속해서(명확한 룰) 부르기로 했는지 뇌에 주입시켜 줍니다.

## 1.6 Organization of This Book (책의 구성: 탐험 지도로 길 잃지 않기)

It summarizes the main topics of each chapter included in this book and their logical connections at an overview level.
앞으로 등장할 2장부터 13장까지 각 챕터 대빵들이 무슨 무기(주제)를 들고 기다리고 있는지, 그리고 걔네들이 서로 어떻게 꼬리에 꼬리를 무는 논리적 세계관을 갖는지 헬기에서 내려다보듯 쓱 요약해 줍니다.

You can view the learning roadmap and flow you will obtain as you read sequentially from beginning to end.
이 목차 지도를 머릿속에 박아두면, 1페이지부터 막장까지 순서대로 밀고 나갔을 때 여러분 뇌가 어떤 순서로 진화할지(학습 로드맵과 콤보 흐름) 한눈에 쫙 조망할 수 있습니다.

## 1.7 Data Sets Used in Labs and Exercises (랩 및 실습 문제에 사용된 데이터 세트: 우리의 마루타들)

It introduces the types and sources of major datasets that will be continuously utilized in Python labs and chapter exercises.
우리가 파이썬 코딩 실습(Labs) 할 때마다 불러와서 쥐어짜고 조리 돌림 할, 아주 귀하고 맛있는 마루타 데이터셋 장난감들이 어떤 놈들이고 대체 어디서 주워온 건지(출처) 썰을 풉니다.

You can confirm that data from various domains collected in the real world, such as healthcare, economics, and marketing, are being used.
병원 의사 선생님의 차트(의료), 월스트리트 주가(경제), 홈쇼핑 구매 내역(마케팅) 등등, 뻔한 장난감이 아니라 진짜 현실 세계 필드에서 발로 뛰어 수집된 피 튀기는 도메인 데이터들이 우리의 샌드백으로 활용된다는 걸 확인하실 수 있습니다.

## 1.8 Book Website (도서 웹사이트: 비밀 창고 좌표)

It guides you to the official website that provides dataset downloads and supplementary materials, as well as offline resources related to this textbook.
아까 말한 그 귀한 데이터셋 파일들 다운로드 링크나, 책에는 차마 다 못 적은 보따리(보충 자료)들이 숨겨져 있는 공식 인터넷 웹사이트 비밀 좌표를 친절하게 안내합니다.

It specifies the online channel where readers can check the latest Python code and learn additional lab content.
혹시나 오타가 났거나 더 삐까뻔쩍한 최신 파이썬 코드로 업데이트된 게 있으면 어디 가서 확인할 수 있는지, 그 피난처(온라인 채널)를 명확히 박아둡니다.

## 1.9 Acknowledgements (감사의 글: 엔딩 크레딧)

This is a word of gratitude to fellow researchers, reviewers, and contributors who provided academic and technical assistance until this textbook was published.
저자들이 이 미친 분량의 교재를 뽑아내면서 피를 토할 때 옆에서 같이 밤을 새우며 오타도 잡아주고 수식 오류도 까준 고마운 대학원생 노예들(동료 연구자, 리뷰어, 기여자)에게 눈물겨운 땡큐를 날리는 페이지입니다.

It honors the contributions of many eminent scholars and the community who have advanced statistical learning theory together.
그리고 혼자 잘나서 이 학문이 큰 게 아니라며, 지금까지 이 통계적 기계 학습 이론을 집대성하며 기초 공사를 다져준 과거의 수많은 천재 학자 할배들과 오픈소스 커뮤니티의 거룩한 공로에 빙긋이 숟가락을 얹으며 기광을 받칩니다.

---

## Sub-Chapters (하위 목차)

[1.1 An Overview Of Statistical Learning >](1_1_an_overview_of_statistical_learning/trans2.html)
