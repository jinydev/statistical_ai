---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 직역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

[< 3.3 Other Considerations In The Regression Model](../trans2.html) | [3.3.1.1 Predictors With Only Two Levels >](3_3_1_1_predictors_with_only_two_levels/trans2.html)

# 3.3.1 Qualitative Predictors

# 3.3.1 정성적 예측 변수 (숫자가 아닌 골치 아픈 문자로 된 재료들)

In our discussion so far, we have assumed that all variables in our linear regression model are _quantitative_.
지금까지 우리가 다중 회귀라는 냄비에 넣고 지지고 볶았던 재료들(변수들)을 떠올려 보세요. '광고 예산 100만 원', '라디오 50회 방송'처럼 덧셈 뺄셈이 착착 맞아떨어지는 아주 얌전한 **_정량적(quantitative, 즉 수치형)_** 재료들뿐이었습니다. 그래서 수식에 넣고 끓이기가 참 편했죠.

But in practice, this is not necessarily the case; often some predictors are _qualitative_.
하지만 현실의 야생 장사판이 어디 그렇게 호락호락하던가요? 막상 가게 데이터 장부를 열어보면, 덧셈 뺄셈이 불가능한 골치 아픈 텍스트 쪼가리, 즉 **_정성적(qualitative, 즉 범주/카테고리형)_** 문자 재료들이 심심치 않게 튀어나와 우리를 괴롭힙니다. 마치 요리 수식에 '성별', '혈액형', '동네 이름' 같은 걸 숫자로 넣으라고 강요받는 셈이니까요.

For example, the `Credit` data set displayed in Figure 3.6 records variables for a number of credit card holders.
예를 한 번 들어봅시다. 그림 3.6에 등장하는 `Credit(신용)` 데이터 장부는 수많은 신용카드 고객들의 현황을 털어놓은 개인정보 기록 뭉치입니다.

The response is `balance` (average credit card debt for each individual) and there are several quantitative predictors: `age`, `cards` (number of credit cards), `education` (years of education), `income` (in thousands of dollars), `limit` (credit limit), and `rating` (credit rating).
여기서 우리가 맞히려는 최종 타겟(응답 변수)은 `balance(고객 1명당 짊어진 평균 카드 빚 액수)` 이며, 이 빚을 예측하기 위해 투입된 멀쩡한 '숫자형' 힌트 재료들은 `age(나이)`, `cards(지갑 속 카드 개수)`, `education(학교 다닌 짬바 연수)`, `income(통장에 찍히는 월급, 천 달러 단위)`, `limit(카드 긁기 한도)`, 그리고 `rating(은행이 매긴 신용 점수)` 등입니다. 이런 애들은 얌전한 숫자라 다루기 편하죠.

Each panel of Figure 3.6 is a scatterplot for a pair of variables whose identities are given by the corresponding row and column labels.
그림 3.6을 보면 네모난 표창장 타일(패널)들이 죽 늘어서 있는데, 이건 각 타일의 가로축 이름과 세로축 이름을 가진 두 변수가 서로 어떻게 싸우고 노는지(관계성) 점을 콕콕 찍어 보여주는 산점도(Scatterplot)라는 마법경입니다.

For example, the scatterplot directly to the right of the word "Balance" depicts `balance` versus `age`, while the plot directly to the right of "Age" corresponds to `age` versus `cards`.
가령, "Balance(카드 빚)"라는 글자 바로 오른쪽에 붙은 점박이 타일은 빚(Balance)과 나이(Age)가 비례하는지 반비례하는지 그 싸움 양상을 중계하고 있으며, "Age(나이)" 글자 바로 우측에 붙은 타일은 나이와 카드 개수(Cards)의 궁합을 까발려 줍니다.

In addition to these quantitative variables, we also have four qualitative variables: `own` (house ownership), `student` (student status), `status` (marital status), and `region` (East, West or South).
자, 문제는 지금부터입니다! 이 얌전한 숫자형 재료들 이외에도, 이 장부에는 계산기 자판에 입력조차 할 수 없는 사나운 '정성적(문자형) 변수' 4총사가 떡하니 자리 잡고 있습니다: 바로 `own(자기 집이 있냐 없냐)`, `student(학생이냐 직장인이냐)`, `status(결혼했냐 돌싱이냐)`, 그리고 `region(사는 곳이 동부, 서부, 남부 중 어디냐)` 같은 녀석들입니다. 얘네들을 도대체 어떻게 수학 공식 냄비에 집어넣어 끓여야 할까요? 

---

### Predictors with Only Two Levels (수준이 2개인 예측 변수: 둘 중 하나인 녀석들 요리법)
* [📖 쉬운 해설판으로 이동하기](./3_3_1_1_predictors_with_only_two_levels/trans2.html)

남성/여성, 예스/노 같이 선택지가 딱 두 개밖에 없는 심플한 '문자 변수'들을 속임수를 써서 0과 1이라는 숫자로 둔갑(더미 코딩, Dummy Coding)시켜 수학 방정식에 거부감 없이 밀어 넣는 사기적인 마술 기법을 살펴봅니다. 0과 1의 변신이 기울기(계수) 해석에 어떤 맛 차이를 가져오는지 낱낱이 파헤칩니다.

---

[< 3.3 Other Considerations In The Regression Model](../trans2.html) | [3.3.1.1 Predictors With Only Two Levels >](3_3_1_1_predictors_with_only_two_levels/trans2.html)
