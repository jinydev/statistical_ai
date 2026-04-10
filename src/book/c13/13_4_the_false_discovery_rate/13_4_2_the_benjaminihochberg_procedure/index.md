---
layout: default
title: "index"
---

# _13.4.2 The Benjamini–Hochberg Procedure_ 

We now focus on the task of controlling the FDR: that is, deciding which null hypotheses to reject while guaranteeing that the FDR, E( _V/R_ ), is less than or equal to some pre-specified value _q_ . In order to do this, we need some way to connect the _p_ -values, _p_ 1 _, . . . , pm_ , from the _m_ null hypotheses to the desired FDR value, _q_ . It turns out that a very simple procedure, outlined in Algorithm 13.2, can be used to control the FDR. 

---

## Sub-Chapters (하위 목차)

### Algorithm 13.2 Benjamini–Hochberg Procedure to Control the FDR (B-H FDR 컨트롤 프로시저 구조)
* [문서로 이동하기](./13_4_2_1_algorithm_13.2_benjaminihochberg_procedure_to_control_the_fdr/)

* [FDR 수리식의 제어 한계 목표점(FDR <= q) 설정](./17_fdr_q./)
실질적으로 어느 정도의 B-H 역치(Threshold)에서 검정을 끊어야 평균 오발견율 기댓값(FDR)을 사용자가 원한 상한선 $q$ 이하로 묶을 수 있는지 스텝을 정의합니다.
