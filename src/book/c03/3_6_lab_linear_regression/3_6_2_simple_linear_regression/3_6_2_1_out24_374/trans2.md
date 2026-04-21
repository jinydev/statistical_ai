---
layout: default
title: "trans2"
---

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

[< 3.6.2 Simple Linear Regression](../trans2.html) | [3.6.3 Multiple Linear Regression >](../../3_6_3_multiple_linear_regression/trans2.html)

# **`Out[24]:`** `374`

The `np.argmax()` function identifies the index of the largest element of an `np.argmax()` array, optionally computed over an axis of the array. In this case, we maximized over the entire array to determine which observation has the largest leverage statistic.
우선 알아둘 점! 넘파이(numpy)의 **`np.argmax()`** 함수는, 주어진 거대한 숫자 배열 무더기(`np.argmax()` array) 안에서! 가장 덩치가 크고 뚱뚱한 **'최댓값 알맹이'가 과연 몇 번째 칸(인덱스 위치)에 처박혀 있는지** 그 자리 번호를 콕 집어 색출해 주는 기특한 위치 추적기 함수입니다. (필요하면 2차원 표의 가로나 세로 특정 축(axis)만 기준으로 검색할 수도 있죠.) 
이번 실습 케이스에선, 우리가 방금 계산해 낸 506개짜리 전체 관측치 레버리지(leverage) 통계량 배열 전체를 탈탈 뒤져서 극대화(maximized) 검색을 돌린 끝에! 그중 가장 악질적으로 **'제일 막대한 뻥튀기 레버리지 통계량(largest leverage statistic)'** 수치를 지문처럼 쥐고 있는 범인 데이터 관측치가 과연 몇 번째 녀석인지 추적(determine)해 떡 하니 '374번'이라는 번호표를 도출 색출해 낸 것입니다.

---

## Sub-Chapters (하위 목차)


[< 3.6.2 Simple Linear Regression](../trans2.html) | [3.6.3 Multiple Linear Regression >](../../3_6_3_multiple_linear_regression/trans2.html)
