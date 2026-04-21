import codecs

content = r"""---
layout: default
title: "trans2"
---

# 6.5.1 부분집합 선택 기법 분석 (Subset Selection Methods)

Here we implement methods that reduce the number of parameters in a model by restricting the model to a subset of the input variables.
이번 세부 파트에서 우리들은 투입 변수들의 집단을 조그마한 일부 알짜배기 부분집합(subset)만 남도록 의도적으로 구속 강제 제한시켜버림으로써, 불필요하게 늘어난 전체 파라미터 묶음 계수 수치를 시원하게 다이어트 해 컷다운(cut down) 절감시켜버리는 실용적인 모델 튜닝법들을 직접 스크립트 상에서 구현해 보도록 하겠습니다.

---

## Sub-Chapters (하위 랩 코딩 실습 과정 요약)

### Forward Selection (전역 전진 선택법 알고리즘 파이썬 실습)
* [문서로 이동하기](./6_5_1_1_forward_selection/)

분석자들의 수고를 덜어주기 위해 변수 투입이 늘어날 때마다 자체 모델의 예측 보증 스코어를 루프문(loop)상에서 내부적으로 계속 관제 기록하며, 목표 타겟에 가장 엄청난 기여도를 뽐내는 변수만을 순차적으로 골라 선별해나가는 영리한 탐색 알고리즘의 파이썬 코드 작동 구조를 실전 포맷 궤도로 즐겁게 체험합니다.
"""

try:
    with open(r'd:\site\jinydev\Statistical\src\book\c06\6_5_lab_linear_models_and_regularization_methods\6_5_1_subset_selection_methods\trans2.md', 'w', encoding='utf-8') as f:
        f.write(content)
except Exception as e:
    print(e)
