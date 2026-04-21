---
layout: default
title: "trans2"
---

# Hybrid Approaches 
# 혼합 접근법 (Hybrid Approaches): 전진과 후진 절묘한 콜라보

The best subset, forward stepwise, and backward stepwise selection approaches generally give similar but not identical models. As another alternative, hybrid versions of forward and backward stepwise selection are available, in which variables are added to the model sequentially, in analogy to forward selection. However, after adding each new variable, the method may also remove any variables that no longer provide an improvement in the model fit. Such an approach attempts to more closely mimic best subset selection while retaining the computational advantages of forward and backward stepwise selection. 
지금까지 우리가 다룬 최적 부분집합, 전진 단계, 후진 단계 선택법들은 결과적으로 서로 엇비슷한 우수 모델들을 뽑아내긴 하지만, 그렇다고 완전히 동일한 100% 싱크로율을 보여주진 못했습니다. 그래서 똑똑한 통계학자들은 "그럼 장점만 섞어보자!"라며 전진과 후진 양방향을 섞어버린 융합형 '하이브리드(Hybrid)' 전략을 개발했습니다. 
이 녀석의 구동 방식은 꽤 교묘합니다. 일단은 전진 단계법처럼 뼈대 모델에 새로운 변수를 하나씩 순차적으로 영입(added to) 합니다. 그런데 한 명을 영입하고 난 직후에, 기존 멤버들을 쓱 둘러보며 팀워크(model fit) 에 더 이상 1도 도움이 안 되는 식객 고인물 변수가 보인다면, 언제 그랬냐는 듯 가차 없이 바다로 던져 해고(remove) 시켜버리는 양방향 기동을 구사합니다. 즉, 넣고 빼고를 동시에 하는 거죠! 
이 혼합 전략은 왜 매력적일까요? 바로 '전/후진 단계법들'의 미친 연산 속도와 다이어트 효율성(computational advantages)은 쏙 빼먹어 그대로 유지하면서도, 앞서 배웠던 무식하지만 정확성은 가장 높았던 '최적 부분집합 방식'의 디테일한 결과물에 훨씬 더 가깝게 모방 도달(mimic) 하려는 아주 영리한 일거양득의 묘수이기 때문입니다.
