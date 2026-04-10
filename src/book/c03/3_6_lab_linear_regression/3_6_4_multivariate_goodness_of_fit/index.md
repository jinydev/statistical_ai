---
layout: default
title: "index"
---

# _3.6.4 Multivariate Goodness of Fit_ 

We can access the individual components of `results` by name ( `dir(results)` shows us what is available). Hence `results.rsquared` gives us the $R^2$ , and `np.sqrt(results.scale)` gives us the RSE. 

Variance inflation factors (section 3.3.3) are sometimes useful to assess the effect of collinearity in the model matrix of a regression model. We will compute the VIFs in our multiple regression fit, and use the opportunity to introduce the idea of _list comprehension_ . 

list comprehension 

---

## Sub-Chapters (하위 목차)

### List Comprehension (리스트 컴프리헨션)
* [문서로 이동하기](./3_6_4_1_list_comprehension/)

분석 과정에서 여러 변수 명칭을 동적으로 조작할 때 쓰이는 강력한 리스트 반복문(List Comprehension) 문법 팁을 배웁니다.
판다스 데이터프레임 내 칼럼들을 손쉽게 필터링할 때 사용합니다.
