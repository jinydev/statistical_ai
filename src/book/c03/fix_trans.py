with open('trans_3_5.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Delete lines containing The KNN errors are well above the black dashed line, which is the test MSE for linear regression.
s_idx = text.find("The KNN errors are well above the black dashed line")

part1 = text[:s_idx]

part2 = r"""The KNN errors are well above the black dashed line, which is the test MSE for linear regression.":
    r'''The KNN errors are well above the black dashed line, which is the test MSE for linear regression.
KNN 의 오차는 선형 회귀의 테스트 세트 MSE 인 검은색 점선 위쪽에 높이 위치합니다.

When the value of _K_ is large, then KNN performs only a little worse than least squares regression in terms of MSE.
$K$ 값이 클 때는, KNN 이 최소 제곱 회귀보다 MSE 관점에서 약간 더 안 좋은 정도의 성능만 발휘합니다.

It performs far worse when _K_ is small.
하지만 $K$ 가 작을 때는 이보다 성능이 훨씬 형편없어집니다.'''
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
"""

with open('trans_3_5.py', 'w', encoding='utf-8') as f:
    f.write(part1 + part2)

