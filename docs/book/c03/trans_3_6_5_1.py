import sys
import re

file_path = r"d:\site\jinydev\Statistical\src\book\c03\3_6_lab_linear_regression\3_6_5_interaction_terms\index.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"""```
Out[31]:           coef  std err       t  P>|t|
intercept 36.0885   1.470  24.553  0.000
lstat     -1.3921   0.167  -8.313  0.000
```

3.6 Lab: Linear Regression 

```
age-0.00070.020-0.0360.971
lstat:age0.00420.0022.2440.025
```""": 
    r"""```
Out[31]:           coef  std err       t  P>|t|
intercept 36.0885   1.470  24.553  0.000
lstat     -1.3921   0.167  -8.313  0.000
age       -0.0007   0.020  -0.036  0.971
lstat:age  0.0042   0.002   2.244  0.025
```"""
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
