import sys
import re

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_6_lab_linear_regression\3_6_5_interaction_terms\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"# _3.6.5 Interaction Terms_": r"""# _3.6.5 Interaction Terms_
# 3.6.5 상호 작용 항 실습""",

    r"It is easy to include interaction terms in a linear model using `ModelSpec()` .":
    r"""It is easy to include interaction terms in a linear model using `ModelSpec()`.
이처럼 기본 `ModelSpec()` 도구를 차용하면 선형 모델 체제 속에 다변수 간의 상호 작용 항(interaction terms) 지표를 거뜬히 손쉽게(easy) 포함해 설계 삽입해 넣을 수 있습니다.""",

    r"""Including a tuple `("lstat","age")` tells the model matrix builder to include an interaction term between `lstat` and `age` .""":
    r"""Including a tuple `("lstat", "age")` tells the model matrix builder to include an interaction term between `lstat` and `age`.
예컨대 튜플 묶음 형태인 `("lstat", "age")` 조각을 연산식에 명시 귀속(Including)해 주면, 이는 행렬 조합기(builder) 측에게 두 변수 `lstat` 과 `age` 사이를 매개하는 실질적 상호 작용 항을 산입 포함하라는 명확한 지시(tells)로 작동합니다.""",

    r"""In [31]:X=MS(['lstat',
'age',
('lstat','age')]).fit_transform(Boston)
model2=sm.OLS(y,X)
summarize(model2.fit())""":
    r"""In [31]: X = MS(['lstat',
                'age',
                ('lstat', 'age')]).fit_transform(Boston)
model2 = sm.OLS(y, X)
summarize(model2.fit())""",

    r"""Out[31]:coefstderrtP>|t|
intercept36.08851.47024.5530.000
lstat-1.39210.167-8.3130.000""":
    r"""Out[31]:           coef  std err       t  P>|t|
intercept 36.0885   1.470  24.553  0.000
lstat     -1.3921   0.167  -8.313  0.000""",

    r"3.6 Lab: Linear Regression \n\n```\nage-0.00070.020-0.0360.971\nlstat:age0.00420.0022.2440.025\n```":
    r"""age       -0.0007   0.020  -0.036  0.971
lstat:age  0.0042   0.002   2.244  0.025"""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
