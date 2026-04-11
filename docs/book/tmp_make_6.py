import codecs

out = """
Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _가장 좋은(best)_ 방법이 아니라 어째서 이렇게 많은 다른 통계 학습 방법론들을 소개할 필요가 있습니까?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다(There is no free lunch in statistics):_ 어떠한 단일 기법도 발생 가능한 모든 데이터 세트에서 여타의 모든 기법을 압도하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 단일 데이터 셋에 대해서는 구체적인 한 방법론이 최상으로 작동할 수 있지만, 전반적으로 비슷하면서도 결이 약간 다른 데이터 셋에서는 오히려 또 다른 방식의 성능이 훨씬 더 우수히 작동할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 어떤 데이터 세트가 주어지더라도 과연 어떤 방식이 최고의 결과물들을 산출해 내는지 판별하고 결정하는 작업은 대단히 중대한 하나의 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

현업 실무에서 통계적 기계 학습을 수행해 작동시킬 시 가장 최상의 접근법을 선택하는 과정은 가장 매우 어렵고도 도전적인 난제 부분들 중 하나가 될 수 있습니다.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set.

이 섹션 구역에서, 우리는 주어진 특정 데이터 세트에 대하여 특정 통계적 역 학습 판 절차 모형 단면을 확 절 이 의 추 절 과 단 진 과 선택 기 선 기 확 확 측 모 확 기 진 조 진 다 도 수 확 결 측 진 단 
"""

out = """
Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _가장 좋은(best)_ 방법이 아니라 어째서 이렇게 많은 다른 통계 학습 방법론들을 소개할 필요가 있습니까?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다(There is no free lunch in statistics):_ 어떠한 방법론도 모든 모든 데이터 세트에서 압도하지 못합니다.
"""

out = """
Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 한 가지의 _최상의(best)_ 방법 대신 어째서 그렇게 많은 다양한 종류의 서로 다른 통계적 학습 접근법들을 도입해 소개하는 것이 필요할까요?
"""

with codecs.open(r'd:\site\jinydev\Statistical\src\book\c02\2_2_assessing_model_accuracy\index.md', 'a', encoding='utf-8') as f:
    f.write(out)
