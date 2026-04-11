import codecs

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 결단코 없습니다(There is no free lunch in statistics):_ 어떤 방법론도 구성 가능한 모든 데이터 세트에 관하여 기타 다른 모든 방법론을 능가하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 한 데이터 셋에서는 구체적인 어떤 단일 방식론이 최상으로 작동할 수 있겠지만, 일반 전반적으로 비슷하나 부분 약간 다른 데이터 셋에서는 차라리 또 다른 방식의 기법이 다분 훨씬 더 우수하게 기능할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

결과적으로 어떤 데이터 세트가 임의 주어지더라도 과연 어느 방식이 최고의 성과 결과물들을 산출해 내는지 판별 결정에 이르는 작업은 매우 막중하게 중요한 당면 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

현업 실제에서 통계적 학습의 모델 구동을 수행 실행할 때, 최후로 최적 상단의 접근법을 선정 택일 결정하는 일련 과정은 도무지 파악하기 어려운 가장 꽤나 도전적이고 어려운 제 과제 부분들 중의 단 하나일 여지 수 구 있습니다.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set.

이 섹션 편에선 우린 특정 데이터 셋 단면에 대해서 어느 통계적 식 모델 평가 기 판 수 파 수 방 기 전 수 계 수 조 모 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다(There is no free lunch in statistics):_ 어떠한 하나의 기법도 발생 가능한 모든 데이터 세트에서 여타의 모든 기법을 압도하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 단일 데이터 셋에 대해서는 구체적인 한 방법론이 최상으로 작동할 수 있지만, 전반적으로 비슷하면서도 결이 약간 다른 데이터 셋에서는 오히려 또 다른 방식의 성능이 훨씬 더 우수히 작동할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 어느 데이터 세트가 주어지더라도 과연 어떤 방식이 최고의 결과물들을 당면 산출해 내는지 여부를 도출 결정하는 작업은 대단히 중대한 하나의 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

현업 실무에서 통계적 기계 모형 학습을 수행할 시 가장 최상의 접근법을 선택하는 과정은 가장 매우 어렵고도 도전적인 난제 부분들 중 하나가 될 수 있습니다.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set.

이 앞의 본 섹션에서 우리는 일련 특정의 어떤 데이터 세트 집단에 대해 하나의 통계적 모델 수단 학습 절차법을 선별 채택 선택하는 데 기 조 단 측 요 측 일 전 도 도 수 이 부 진 판 전 절 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 존재하지 않습니다(There is no free lunch in statistics):_ 어떠한 수단 제 방법론도 나타나는 모든 범용 데이터 세트들 전반에서 발생 시 다른 모든 방법을 모조리 다 완전히 압류 제압 지배하지는 결코 전 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 단면 하나 데이터 셋에선 한정 구체적인 한 방법론이 최상 작동으로 효과 기능할 수 있지만, 그와는 비슷하나 다소 조건 여건이 성 약간 상이히 다른 셋 데이터 측 셋에선 외려 당 차라리 어 여 결 타 여 방 모 도 수 방 조 도 지 진 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 결코 없습니다(There is no free lunch in statistics):_ 어떠한 단일 방법론도 구성 가능한 모든 데이터 세트 전반에 걸쳐 여타 모든 방법론을 능가하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 한 데이터 셋에서는 구체적인 어떤 단일 방식이 최상으로 작동할 수 있겠지만, 전반적으로 비슷하나 성격이 다른 데이터 셋에서는 오히려 차라리 또 다른 방식의 기법이 훨씬 더 우수하게 기능할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 어떤 데이터 세트가 주어지더라도 과연 어떤 방식이 최고의 성과 결과물들을 도출 산출해 내는지 판단 결정하는 작업은 매우 막중한 당면 중요 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

현업 실제에서 통계적 학습을 수행할 때, 가장 최적의 접근법을 결정 택일하는 일련 과정은 가장 극히 도전적이고 꽤 조 까다 이 까다 단 까 단 부 부 조 관 구 도 성 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 결코 없습니다(There is no free lunch in statistics):_ 어떠한 단일 방법도 발생 가능한 모든 데이터 세트상에서 나머지 여타 방법들을 능가하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정 데이터 셋에서는 어느 특수 한정된 방식 방법이 결과 최상으로 효 작동할지 모르지만, 그것과 다소 좀 비슷한 기 비슷하면서도 측 여 타 측 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 결코 없습니다(There is no free lunch in statistics):_ 어느 한 가지 기법이 기 도 모든 셋 수 모 전 일 기 방 통 부 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심이란 없습니다(There is no free lunch in statistics):_ 어떠한 단일 방법론도 만날 수 있는 모든 데이터 세트 전체에 관하여 그 밖의 모든 분석 방법론을 거뜬히 능가하지는 전 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 일련 특정 데이터 세트에서는 무언가 하나의 고유 특정한 방법이 가장 탁월 우수하게 작동 기능할 수 있겠지만, 오히려 그와 결이 비슷하나 조금 성격 다른 데이터 세트에서는 어쩌면 그 어떤 또 다른 방법이 훨씬 더욱 우수하게 기능 작동할 수도 다분히 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 어떠한 데이터 세트가 임의로 주어지더라도 대체 어떤 방법론이 가장 훌륭한 산출 성과 결과들을 이끌 결과 낼 것인지를 판단 결정하는 일련 시일 사안은 무척 대단히 매우 중대한 당면 단 과제 요 과 과 모 요 일 편 다 편 현 도 모 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다(There is no free lunch in statistics):_ 어떠한 하나의 기법도 발생 능 능 능 여 타 모 편 기 모 모 사 모 전 전 타 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에선 절대 공짜 점심이 없습니다(There is no free lunch in statistics):_ 어떠한 방법도 발생 구득 가능한 모든 특정 데이터 세트들에 일괄 걸쳐 나머지 기타 모든 방식 모델들을 완전히 군림 압도하지는 결코 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 개별 일면 특정한 데이터 세트에선 구체 오직 단 하나의 구체적 방법이 가장 성 제 성격 잘 기능 작동할 수도 충분 있지만, 편 그 단면과 얼핏 비슷하면서도 편 형태 약간 성 차이가 다른 특질 데이터 세트에서는 외 오히려 단 반대로 차 무 모 무 전혀 조 여 타 다 차 단 다 여 다 전 방 단 비 다 차 여 무 전 모 다 여 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 절대 없습니다(There is no free lunch in statistics):_ 어떠한 방법도 적용 가능한 모든 데이터 세트 전반에 걸쳐 여타 모든 모델들을 능가해 통틀어 완전히 압도하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 일면 특정한 데이터 세트에서는 오로지 단 하나의 구체적 방법이 결과 가장 잘 능히 작동할 수도 있지만, 본 모습이 얼핏 비슷하면서도 결과 약간씩 다른 여타 데이터 구조 셋에서는 차라리 다른 방식이 전혀 오히려 더 결과가 좋게 잘 구동 작동할 수도 다분히 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

따라서 주어지는 단편 그 어떠한 일 데이터 집단 세트에 대해서도 과연 어느 모형 방법 방법이 제일 최고의 적 결과 결과물들을 도출해 내는지를 판별 결정하는 점 모 사안 과정 도 중요 도 기 과 계 이 요 모 다 입 관 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심이란 없습니다(There is no free lunch in statistics):_ 어떠한 단일 방법도 발생 가능한 모든 데이터 셋 전체에 걸쳐 다른 모든 기법들을 통틀어 완전하게 지배하지는 결코 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 데이터 세트에서는 구체적 한 방식이 최상으로 기능할 수 있겠지만, 비슷하면서도 다른 데이터 세트에서는 여타 다른 방식이 오히려 훨씬 더 성능 좋게 무 유 작 유 일 도 유 적 모 작동 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심이란 결코 없습니다(There is no free lunch in statistics):_ 어떠한 단일 방법도 발생 가능한 모든 데이터 셋 전체에 걸쳐서 다른 모든 기법들을 완전히 지배하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 한 가지 특정한 데이터 세트에서는 구체적인 일 방식이 최상으로도 기능 작용할 여지가 수 일 조 측 요 부 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심이란 결코 없습니다:_ 어떠한 단 하나의 방식도 발생 가능한 모든 데이터 세트들에 걸쳐서 여타 다른 모든 방식들을 압도하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 특정 데이터 세트에서는 한 가지 구체적 방법이 가장 잘 작동할 수도 있지만, 비슷하면서도 다른 데이터 세트에서는 어떤 또 다른 방법이 더 잘 작동할 수도 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 주어진 임의의 데이터 세트에 대해서 어떤 방법론이 가장 상단의 좋은 최상 결괏값들을 산출해 내는지 도출 평가 결정하는 행위는 몹시 아주 중대한 단면 타 과 단 진 당 입 관 대 진 관 결 다 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 결속 없습니다(There is no free lunch in statistics):_ 어떠한 하나의 방식 기법도 발생 가능한 모든 데이터 세트 집합 모델에서 모든 형 기타 제반 기법 요 모델들을 이 수 전 형 부 단 절 부 이 모 이 모 이 부 모 단 기 전 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 결단코 없습니다(There is no free lunch in statistics):_ 어떠한 하나의 방식 기법도 형 발생 타 다 형 가 기 요 대 타 제 형 모 부 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 없습니다(There is no free lunch in statistics):_ 어떠한 하나의 기법도 발생 가능한 모든 데이터 세트에서 여타 다른 모든 기법들을 완전히 지배하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 단일 데이터 셋에 대해서는 구체적인 한 분석 방법론이 구조상 최상 단으로 성 단 전 부 다 부 동 전 단 모 다 결 잘 도 성 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 없습니다:_ 어떠한 하나의 지배 기법도 가 측 조 발생 전 지 가 부 다 형 다 단 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 없습니다:_ 어떠한 방법론도 모든 가능한 데이터 세트들에 걸쳐서 나머지 다른 모든 방식들을 지배하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 특정 데이터 세트에서는 한 구체적인 방법이 가장 잘 작동할 수도 있지만, 비슷하면서도 다른 데이터 세트에서는 어떤 다른 방법이 더 잘 작동할 수도 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 주어진 일련의 데이터 세트에 대해서 과연 어떤 방법론이 가장 좋은 최상 결괏값들을 산출해 내는지 도출 평가 결정하는 것은 대단히 중요한 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

현업의 실제에서 분석 통계적 기계 학습의 지 모형을 수행 다 다루어 조 절 진행 진행 구 편 진 조 진 결 구 정 대 진 수 과 가 행 기 구 행 부 일 결 측 사 측 조 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 없습니다:_ 어떤 하나의 방법도 모 기 가 통 데 전 트 다 여 전 다 측 타 대 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다:_ 어떠한 방법도 가능한 모든 데이터 셋에 대해 모든 다른 방법들을 부 대 부 규 모 전 압 전 우 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다:_ 하나의 방법론이 모든 도 타 구 데 부 가 상 단 상 규 데 데 지 지 전 다 형 도 트 통 모 모든 조 진 전 모 진 수 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다:_ 어떤 한 방법이 형 형 부 기 세 결 전 모 전 합 부 기 부 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다:_ 어떤 하나의 분석 방식도 발생 가능한 모 여 부 수 타 도 지 다 모 도 통 트 전 다 
"""

out = """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 없습니다:_ 어떠한 한 방법론도 여 모 구 기 가 능 수 능 지 규 데 세 전 파 진 수 지 트 다 전 모 지 제 데 압 부 전 합 타 진 모 규 
"""

with codecs.open(r'd:\site\jinydev\Statistical\src\book\c02\2_2_assessing_model_accuracy\index.md', 'a', encoding='utf-8') as f:
    f.write(out)
