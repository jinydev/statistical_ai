---
layout: default
title: "trans1"
---

[< 1.6 Organization Of This Book](../1_6_organization_of_this_book/trans1.html) | [1.8 Book Website >](../1_8_book_website/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Data Sets Used in Labs and Exercises

# 랩 및 실습 문제에 사용된 데이터 세트

In this textbook, we illustrate statistical learning methods using applications from marketing, finance, biology, and other areas.

우리는 이 기본 지침 교과서의 전체 내용에 걸쳐 마케팅 시장 분야, 다각적 금융의 세계, 신비한 생물학적 영역, 기타 여러 분야에서의 다채로운 응용 애플리케이션의 실례를 사용하여 통계 도구와 학습 기법 및 적용 방식에 대해 다뤄 볼 것입니다.

The `ISLP` package contains a number of data sets that are required in order to perform the labs and exercises associated with this book.

그리고 우리가 자체적으로 심혈을 기울여 다같이 준비한 `ISLP` 고유 제공 패키지에는 이 기술 서적과 깊게 연관된 수많은 랩 연습과 및 각 장의 실습 문제들을 원만하게 제대로 수행하기 위해 반드시 요구되고 사용해야 하는 수의 무수한 양질의 다양한 종류의 실증 데이터 세트가 포진해 포함되어 있습니다.

One other data set is part of the base R distribution (the `USArrests` data), and we show how to access it from Python in Section 12.5.1.

또 다른 한 종류의 약간 독특한 유형의 하나의 특정 데이터 세트는 과거부터 사용된 기초 R 내장 배포판의 아주 유명한 한 구성 부분인 (정확히는 `USArrests` 데이터) 인데, 우리는 12.5.1 섹션에 위치한 내용 서술을 통하여 친절하게 Python 상에서 이를 원활하고 순조롭게 어떻게 파이썬 내부로 접속하여 불러들여 엑세스 할 수 있는지 방법을 세밀히 보여주고 일러 줍니다.

Table 1.1 contains a summary of the data sets required to perform the labs and exercises.

바로 아래 제시되는 테이블 표 1.1은 제공될 랩과 각종 연습의 실습을 수행하는 데 필요한 다채로운 데이터 세트의 간추린 핵심 요약 설명을 포함합니다.

A couple of these data sets are also available as text files on the book website, for use in Chapter 2.

여러분이 참고하실 수 있도록, 이러한 데이터 세트 중 가장 유용한 핵심적인 두어 개 정도는 추가적으로 특별히 따로 선별하여 2장에서 즉시 곧바로 활용하고 사용하실 수 있도록 지정 공식 서적용 지원 웹사이트를 통해서 텍스트 파일(text files) 다운로드 형태로도 제공될 수 있게끔 언제든 이용의 기능이 열려 있습니다.

| Name | Description | 이름 | 설명 |
|---|---|---|---|
| `Auto` | Gas mileage, horsepower, and other information for cars. | `Auto` | 자동차의 연비(가스 마일리지), 마력 및 기타 세부 특성 자동차 일반 정보. |
| `Bikeshare` | Hourly usage of a bike sharing program in Washington, DC. | `Bikeshare` | 워싱턴 DC의 자전거 공유 체계 프로그램 시간별 이용 및 사용 내역. |
| `Boston` | Housing values and other information about Boston census tracts. | `Boston` | 잘 알려진 보스턴(Boston) 인구 조사 구역 단위별 거주지 주택 가치 및 주택 지역 내 제반 기타 생활 수준 정보. |
| `BrainCancer` | Survival times for patients diagnosed with brain cancer. | `BrainCancer` | 심각한 뇌종양성 암 질환을 새롭게 진단받고 고통받는 투병하는 병원 환자들의 최종 집계 생존 허용 시간 정보. |
| `Caravan` | Information about individuals offered caravan insurance. | `Caravan` | 특정 보장 조건의 카라반형 보험(caravan insurance) 상품 체계 제공을 제안받았던 여러 개인들에 관한 다각도 관점 형태의 신상 상세 정보. |
| `Carseats` | Information about car seat sales in 400 stores. | `Carseats` | 약 400곳 이상의 전국 각지에 걸쳐 설립된 매장에서 이뤄진 총괄적인 종류별 카시트 판매 및 매출 활동 판매와 관련한 정보. |
| `College` | Demographic characteristics, tuition, and more for USA colleges. | `College` | 대다수 미국 대학의 학생 전체 모집 집단과 인구 통계학적 각종 특성 정보, 주요 학비 정보 비용(tuition) 및 기타 관련 세부 사항 정보 등등. |
| `Credit` | Information about credit card debt for 400 customers. | `Credit` | 어느 특정 은행 신용 카드 회사의 주요 거래 고객 400여 명의 빚, 개인 신용 부채와 신용 채무 상황과 관련한 여러 신용 한도 내역 정보. |
| `Default` | Customer default records for a credit card company. | `Default` | 어느 무명의 신용 카드 회사의 특정 우수 회원을 제외한, 불량 및 고위험 고객들의 채무 결제 불이행 및 채무액에 관련된 상세 파산 위기 기본 기록 정보. |
| `Fund` | Returns of 2,000 hedge fund managers over 50 months. | `Fund` | 약 50개월(50달)이 넘는 긴 운영 기간 동안 총 2,000명의 주요 거물 헤지 펀드의 전문 매니저들이 축적하고 운용하여 기록한 펀드 수익률과 연관 정보. |
| `Hitters` | Records and salaries for baseball players. | `Hitters` | 북미 지역 프로 야구(baseball) 현역 선수들의 타격 활약 및 운동 성적 기록 실적 정보, 그에 따른 차등 보수별 연봉(salaries) 관련 책정 집계 정보. |
| `Khan` | Gene expression measurements for four cancer types. | `Khan` | 각자 다르게 구별되는 총 특별한 네 가지(4) 개별 유형 범주의 생물학 질병 세포 조직 종류의 각종 암에 대한 종합 측정 관련 유전자 주요 측정 발현 기록 수치. |
| `NCI60` | Gene expression measurements for 64 cancer cell lines. | `NCI60` | 앞선 유형별 세포가 아닌 인간 인체에 대한 총 64개의 신체 기관의 매우 다양한 암세포를 발현하는 고유주(cell lines)들에 대한 종합 측정 유전자 수치 측정 집계 발현 기록 사항. |
| `NYSE` | Returns, volatility, and volume for the New York Stock Exchange. | `NYSE` | 악명 높은 큰 시장의 표방격인 뉴욕 지역 기반의 증권 거래소(New York Stock Exchange)에 관련된 매일의 주식 거래량 변동 수치 및 투자 수익률, 기초 변동성 관련 분석 상세 측정 내역 정보. |
| `OJ` | Sales information for Citrus Hill and Minute Maid orange juice. | `OJ` | Citrus Hill 이라는 식료품 상호 주스와 유명한 Minute Maid 시판 유명 가공 오렌지 주스 브랜드들의 각종 유통 및 판촉 상세 판매 및 매출 관련 종합 영업 수치 실적 요약 기술 기록 사항 정보. |
| `Portfolio` | Past values of financial assets, for use in portfolio allocation. | `Portfolio` | 각종 투자 전략을 위한 이상적인 다양한 방식의 위험 배분 및 전체적 포트폴리오를 분산, 세분하여 할당, 계산, 결정하여 배분하는 데 실용 목적으로 참고되어 사용되는 과거 금융성 자산들의 이전 과거 측정 가치 정보와 현황 파악 리스트 목록 내역서 기록. |
| `Publication` | Time to publication for 244 clinical trials. | `Publication` | 엄격하게 치러진 244종의 전 세계 의학 관련 전문 임상적 실험 연구와 학술 과학적 의학 평가 시도를 마친 뒤, 이것이 실제 사회의 대중적 공개 공시가 되는 시점까지 걸린 통계 발표 소요 시간 시간 관련 사항 정보 기록 내역. |
| `Smarket` | Daily percentage returns for S&P 500 over a 5-year period. | `Smarket` | 매우 넓은 시장의 측정 척도이고 경제 대표 지수 중 하나인 미국의 S&P 500 주식 주가 시장 지수 항목과 종목에 대하여 긴 장기간인 5년형 장기적 기간 전체를 포괄하여 통틀어 매일매일 측정된 평균적인 일일 1일 환산치 백분율 일일 수익률 상세 통계 지표 백분율 퍼센티지. |
| `USArrests` | Crime statistics per 100,000 residents in 50 states of USA. | `USArrests` | 매우 방대한 규모를 보이는 미국 50개주(states) 각 주별 통틀어 10만 명(100,000)당 측정 구역별 현지 거주민을 환산 기본 척도 단위로 하는 중범죄 강력 사건과 불법 폭력 체포 구속 범죄(Crime arrests) 등의 관련 전반적 사회 각계 기본 치안 현황 기초 범죄 통계 측정 수치 내용 요약 기록 사항 종합 도표 정보. |
| `Wage` | Income survey data for men in central Atlantic region of USA. | `Wage` | 북아메리카의 매우 핵심적이고 넓게 포함하는 중요한 중앙 대서양권 권역(central Atlantic region) 소속 미국 거주 지역에 살고 있는 근로 활동 남성 근로 직장인들(men)에 통상적으로 한정하고 측정한 노동 소득 및 관련 임금 개인 소득(Income) 파악 실태 종합 설문 조사 자료. |
| `Weekly` | 1,089 weekly stock market returns for 21 years. | `Weekly` | 수십 년이란 가장 오랜 장기간 범위인 전체 총합 무려 21년 범위에 길고 긴 다년 측정 기간을 온전히 내내 아우르는 총합 1,089주의 합계에 해당하는 한 개 주단위를 기준 단위 척도 삼은 미국 주식 금융 시장 내 매주(주간, weekly) 전체의 수집된 주간 단위 평균 시장 투자 환원 수익률(returns) 정보 분석 세부 요약. |

**TABLE 1.1.** *A list of data sets needed to perform the labs and exercises in this textbook. All data sets are available in the ISLP package, with the exception of USArrests, which is part of the base R distribution, but accessible from Python.*

**표 1.1.** *이 주요 학습 지침 교재에 편성된 방대한 각 챕터별 다양한 랩 과정의 모든 필수 실습과 여러 연습 문제들을 온전히 완전히 빠짐없이 수행하는 데 반드시 요구되는 갖가지 핵심 필수 제공 데이터 세트들에 관한 일목요연한 정리 요약 종합 도표 기본 요약 전체 목록 정보 표입니다.*  *단, 유일한 한 가지 예외로써 본문의 Python 기초 기반 기본 제공 액세스 접속 연결 환경의 수단이 추가로 포함 마련된 과거 태생적 출신의 기초 오리지널 base R 기초 기반 오리지널 과거 원본 배포 내장 배포판 중 주요한 핵심적 구성품 부속의 일원으로 제공되는 USArrests를 유일한 단 한 개의 예외 사례로 제외하고, 기타 나머지의 모든 다종다양한 학습을 위해 마련된 일체의 일괄된 데이터 세트 일체들은 모두 예외 없이 언제 어디서건 우리의 ISLP 고유 패키지 환경 내에서 전부 즉시 사용하고 꺼내 활용할 수 있는 가용성을 기본 보장 제공하고 있습니다.*

---

## Sub-Chapters (하위 목차)

[< 1.6 Organization Of This Book](../1_6_organization_of_this_book/trans1.html) | [1.8 Book Website >](../1_8_book_website/trans1.html)
