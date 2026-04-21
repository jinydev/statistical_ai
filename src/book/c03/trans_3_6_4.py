import sys

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_6_lab_linear_regression\3_6_4_multivariate_goodness_of_fit\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# _3.6.4 Multivariate Goodness of Fit_": r"""# _3.6.4 Multivariate Goodness of Fit_
# 3.6.4 다변량 적합도 실습""",

    r"We can access the individual components of `results` by name ( `dir(results)` shows us what is available).":
    r"""We can access the individual components of `results` by name (`dir(results)` shows us what is available).
우리는 기 도출 반환된 이 `results` 산출 객체 단면 속에 내포된 자잘한 각 개별 하부 구성 요소(components) 파편들을 그들의 고유 지정 이름 규칙(by name)을 맞대어 곧장 개별 접근(access)해 빼내 차용해 올 수가 있습니다 (참고로 파이썬 구문 `dir(results)` 를 타건 실행해 보면 당장 어떤 이름표의 하위 가용 항목들이 도사리고 있는지 일목요연 그 목록들을 보여(shows us) 줍니다) .""",

    r"Hence `results.rsquared` gives us the $R^2$ , and `np.sqrt(results.scale)` gives us the RSE.":
    r"""Hence `results.rsquared` gives us the $R^2$, and `np.sqrt(results.scale)` gives us the RSE.
그런 까닭에 이 원리를 살려 `results.rsquared` 구문을 대입하면 목표하던 $R^2$ 지수를 단숨 획득 쥐여주며, 더불어 `np.sqrt(results.scale)` 수식을 기용하면 우리가 바란 RSE(잔차 표준 오차) 척도 결괏값 또한 척척 도출 제공(gives us)해 줍니다.""",

    r"Variance inflation factors (section 3.3.3) are sometimes useful to assess the effect of collinearity in the model matrix of a regression model.":
    r"""Variance inflation factors (section 3.3.3) are sometimes useful to assess the effect of collinearity in the model matrix of a regression model.
일명 분산 팽창 계수(Variance inflation factors, VIF, 앞선 본문 3.3.3절 참조) 지표는, 특정 일개 회귀 모델 기반 행렬 체제 내부에 똬리를 튼 다중 공선성(collinearity)의 여파와 기세(effect) 추이를 이리저리 감별 진단 타진 평가(assess)하고자 할 때 꽤나 매우 유용한(useful) 실무 도구 잣대로 애용됩니다.""",

    r"We will compute the VIFs in our multiple regression fit, and use the opportunity to introduce the idea of _list comprehension_ .":
    r"""We will compute the VIFs in our multiple regression fit, and use the opportunity to introduce the idea of _list comprehension_.
나아가 이 대목에서 우리는 방금 산출한 다중 회귀 적합(multiple regression fit) 국면 잣대를 토대로 이들 제반 VIF 점수들을 일괄 직접 연산 도출해(compute) 낼 터이며, 또한 이 과정 구현의 수행 기회를 십분 틈타 차용해 파이썬 고유의 강력한 문법 구도인 이른바 _리스트 컴프리헨션(list comprehension, 리스트 내포)_ 의 막강 개념 기조 역시 아주 덤으로 간략 친숙히 소개(introduce)해 드릴까 합니다.""",

    r"list comprehension": r""

}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
