---
layout: default
title: "index"
---

# _12.2.4 More on PCA_ 

---

## Sub-Chapters (하위 목차)

### Scaling the Variables (모델 훈련 이전 변수들에 대한 단위 스케일링)
* [문서로 이동하기](./12_2_4_1_scaling_the_variables/)

수십 킬로그램 단위와 수백만 단위가 혼재할 때, 단순히 숫자 크기가 크다는 이유로 주성분 가중치가 쏠리는 것을 막는 표준화(Standardization) 당위성입니다.

### Uniqueness of the Principal Components (주성분의 유일성)
* [문서로 이동하기](./12_2_4_2_uniqueness_of_the_principal_components/)

계산된 주성분 방향의 정답은 사실상 부호(양수/음수)를 뒤집어도 공간에서 같은 축을 형성하기에 완전히 고유한 식이라는 보장은 없음을 이해합니다.

### Deciding How Many Principal Components to Use (몇 개의 주성분을 사용할 것인가?)
* [문서로 이동하기](./12_2_4_3_deciding_how_many_principal_components_to_use/)

정방향 정답이 없으므로 주로 스크리 도표에서 꺾이는 팔꿈치(Elbow) 지점을 찾거나, 후속 지도학습의 검증을 통해 최적 차원 갯수를 휴리스틱하게 정합니다.
