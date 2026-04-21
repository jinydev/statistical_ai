---
layout: default
title: "trans2"
---

[< 1.6 Organization Of This Book](../1_6_organization_of_this_book/trans2.html) | [1.8 Book Website >](../1_8_book_website/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# Data Sets Used in Labs and Exercises
# 랩 및 실습 문제에 사용된 데이터 세트 (우리의 영원한 장난감들)

In this textbook, we illustrate statistical learning methods using applications from marketing, finance, biology, and other areas.
이 피 말리는 교과서 내내, 저희는 통계 장난감 무기들이 어떻게 쓰이는지 보여드리려고 마케팅(물건 팔기)부터 금융(돈 놀이), 생물학(세포 뜯어보기) 등등 온 세상 모든 분야에서 온갖 오지랖(애플리케이션 실례)을 다 떨 예정입니다.

The `ISLP` package contains a number of data sets that are required in order to perform the labs and exercises associated with this book.
그리고 여러분이 빈손으로 싸우지 않게 하려고 저희가 쌈박한 `ISLP` 라는 책 전용 가방(패키지)을 만들었는데, 이 안에는 앞으로 여러분이 실습실(랩)과 연습 문제에서 질리도록 쥐어짜고 괴롭힐 수많은 공짜 장난감 데이터 세트들이 바글바글 들어있습니다.

One other data set is part of the base R distribution (the `USArrests` data), and we show how to access it from Python in Section 12.5.1.
아, 딱 하나 예외 장난감이 있습니다! `USArrests` 라는 데이터인데, 이건 옛날 호랑이 담배 피우던 시절 만들어진 R 언어의 화석(기본 배포판)에 짱박혀 있던 놈이거든요. 불쌍해서 우리가 나중에 12.5.1 섹션쯤 가면 그 화석을 어둠의 경로로 '파이썬(Python)'으로 어떻게 빼돌려오는지(액세스 방법) 친절하게 알려드릴 겁니다.

Table 1.1 contains a summary of the data sets required to perform the labs and exercises.
바로 아래 표 1.1 족보를 보시면, 앞으로 여러분의 피, 땀, 눈물을 쏙 뺄 실습 장난감(데이터 세트)들의 이름표와 간략한 스펙(요약)이 쫙 정리되어 있습니다.

A couple of these data sets are also available as text files on the book website, for use in Chapter 2.
이 장난감들 중에 한두 개는 당장 2장부터 급하게 써먹어야 해서, 친절하게 저희가 공식 웹사이트 자료실에다가 엑셀로 열리는 생짜 텍스트 파일(text files)로도 똑 떼서 올려뒀으니 마음껏 퍼가서 쓰십쇼!

| Name | Description | 이름 | 설명 |
|---|---|---|---|
| `Auto` | Gas mileage, horsepower, and other information for cars. | `Auto` | 붕붕이(자동차)들의 기름 먹는 하마 랭킹(연비), 발차기 힘(마력) 등 잡다한 찐 자동차 스펙 장부. |
| `Bikeshare` | Hourly usage of a bike sharing program in Washington, DC. | `Bikeshare` | 워싱턴 DC 동네 사람들이 자전거(따릉이 같은 거)를 시간대별로 얼마나 훔쳐 탔는지(이용량) 기록한 장부. |
| `Boston` | Housing values and other information about Boston census tracts. | `Boston` | 보스턴 동네 구석구석의 피 말리는 집값(주택 가치)과, 그 동네 팍팍한 삶의 수준을 호구 조사한 스펙 정보. |
| `BrainCancer` | Survival times for patients diagnosed with brain cancer. | `BrainCancer` | 뇌종양 암 선고를 받고 싸우신 병원 환자분들이 버텨내신 슬프고 숭고한 투병 생존 시계(시간) 기록 장부. |
| `Caravan` | Information about individuals offered caravan insurance. | `Caravan` | "고객님, 카라반 보험 하나 드시죠?" 하고 찔러봤던 동네 사람들의 약점 잡힌 신상 털이(상세) 정보. |
| `Carseats` | Information about car seat sales in 400 stores. | `Carseats` | 전국 팔도 400개 매장에서 애기들 카시트를 도대체 얼마나 미친 듯이 팔아 치웠는지(판매 실적) 탈탈 턴 정보. |
| `College` | Demographic characteristics, tuition, and more for USA colleges. | `College` | 미국 대학교들의 "우리 학교 짱임!" 자랑 스펙과, 피를 빨아먹는 극악무도한 대학 등록금(tuition) 정보 등등. |
| `Credit` | Information about credit card debt for 400 customers. | `Credit` | 카드 회사 호구 고객 400명의 피 눈물 나는 카드값 빚더미(신용 부채)와 한도 초과 상황을 까발린 정보. |
| `Default` | Customer default records for a credit card company. | `Default` | 결국 카드값 못 막고 장렬히 파산해서 신불자(결제 불이행) 낙인이 찍힌 무명 카드회사 불량 고객들의 흑역사 장부. |
| `Fund` | Returns of 2,000 hedge fund managers over 50 months. | `Fund` | 돈 냄새 기가 막히게 맡는 헤지 펀드 매니저 2,000명이 장장 50개월 동안 개미들 돈 굴려서 얼마나 빨아먹었나(수익률) 적은 기록. |
| `Hitters` | Records and salaries for baseball players. | `Hitters` | 야구 배트 깎는 장인(프로 선수)들의 타율 성적표와 그에 비례해 구단주 방에서 챙겨받는 두둑한 연봉(salaries) 족보. |
| `Khan` | Gene expression measurements for four cancer types. | `Khan` | 극악무도한 4대장 암세포들을 모아다가 유전자가 어떻게 발광(발현 측정)하는지 수치로 박제해버린 생물학 기록. |
| `NCI60` | Gene expression measurements for 64 cancer cell lines. | `NCI60` | 이건 스케일이 다릅니다! 무려 64가지 인간 암세포(고유주)들의 미친 유전자 발현 꼬라지를 전부 수치로 잡아낸 기괴한 기록. |
| `NYSE` | Returns, volatility, and volume for the New York Stock Exchange. | `NYSE` | 천조국의 삥뜯기 판, 뉴욕 증권 거래소에서 매일매일 거래량이 얼마고, 주가가 위아래로 얼마나 미친 듯이 널뛰는지(변동성, 수익률) 측정한 장부. |
| `OJ` | Sales information for Citrus Hill and Minute Maid orange juice. | `OJ` | 시트러스 힐 vs 미닛 메이드! 영원한 오렌지 주스 라이벌 두 브랜드가 마트에서 얼마나 피 튀기게 팔아재꼈는지(매출 실적) 쓴 영업부 장부. |
| `Portfolio` | Past values of financial assets, for use in portfolio allocation. | `Portfolio` | 주식쟁이들이 "계란을 한 바구니에 담지 마라!"며 투자 포트폴리오를 쪼갤 때(위험 배분) 썼던 옛날 금융 자산들의 역사적 가치 기록부. |
| `Publication` | Time to publication for 244 clinical trials. | `Publication` | 흰 가운 입은 교수님들이 244건의 임상 실험 빡세게 마치고 나서, 논문 통과돼서 세상에 나오기까지(공개 발표) 도대체 몇 날 며칠이 걸렸나(소요 시간) 센 기록. |
| `Smarket` | Daily percentage returns for S&P 500 over a 5-year period. | `Smarket` | 미국 주식의 영혼 S&P 500 지수가 5년이라는 아주 기나긴 세월 동안 매일매일 얼마나 올랐다 내렸다 요동쳤는지(일일 백분율 수익률) 찍은 기록. |
| `USArrests` | Crime statistics per 100,000 residents in 50 states of USA. | `USArrests` | 미국 넓은 50개 동네마다 "길거리 가다 사람 10만 명당 몇 명이 총에 맞거나 수갑 찼나?"를 파악한 끔찍하고 살벌한 강력 범죄 치안 도표 장부. |
| `Wage` | Income survey data for men in central Atlantic region of USA. | `Wage` | 미국 대서양 한가운데 동네 사는 아저씨들이 죽어라 일해서 대체 월급(Income) 통장에 얼마씩이나 꽂히나 영혼까지 털어본 소득 설문 족보. |
| `Weekly` | 1,089 weekly stock market returns for 21 years. | `Weekly` | 일일(Smarket) 장부가 쪼잔하다고? 이건 무려 21년이라는 영겁의 세월 동안 일주일(주간)마다 주식이 얼마나 올랐네 내렸네 총 1,089주를 꼬박 적은 광기의 주간 수익률 족보. |

**TABLE 1.1.** *A list of data sets needed to perform the labs and exercises in this textbook. All data sets are available in the ISLP package, with the exception of USArrests, which is part of the base R distribution, but accessible from Python.*

**표 1.1.** *이 살인적인 교과서 랩 실습들을 깰 때 무조건 파밍해야 하는 꿀템(장난감 데이터) 리스트입니다. 걱정 마세요! 이 템들은 전부 우리 갓 'ISLP 패키지' 인벤토리 안에 다 공짜로 들어있습니다. 아, (USArrests) 요 화석 템 하나만 빼고요! 얜 오리지널 R 시절 유물이지만 걱정 마세요, 파이썬으로 뽀려오는(액세스) 비전 머신을 나중에 다 알려드릴 테니까요!*

---

## Sub-Chapters (하위 목차)

[< 1.6 Organization Of This Book](../1_6_organization_of_this_book/trans2.html) | [1.8 Book Website >](../1_8_book_website/trans2.html)
