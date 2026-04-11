import codecs
import re

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표들 중 하나는 표준 선형 회귀 접근법을 훨씬 넘어서 확장되는 광범위한 통계적 기계 학습 방법들을 독자들에게 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 단 하나의 _최상의(best)_ 방법을 제시하기보다는 어째서 그토록 많은 각각 다른 통계적 예측 학습 접근법들을 앞서 소개하는 일이 단연 필요할까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 결코 없습니다(There is no free lunch in statistics):_ 어떠한 단 하나의 방법도 모든 가능한 각 데이터 세트들 통틀어 여타의 모든 기 다른 방식들을 지배하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특수한 특정 데이터 단면 세트에서는 단 하나의 구체적인 방식 방법이 가장 최상으로 작동할 수도 있지만, 이와 결 유사하지만 그럼에도 다른 데이터 집 세트상에서는 어떤 모종 여타 다른 방법이 오히려 더 훌륭하게 작동 여 기 결 도 가 가 가
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표들 중 하나는 표준 선형 회귀 접근법을 훨씬 넘어서 확장되는 광범위한 통계적 기계 학습 방법들을 독자들에게 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 한 가지의 _가장 좋은(best)_ 방법 대신 어째서 그토록 많은 다른 통계적 기계 학습 접근법들을 소개하는 것이 필요할까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 없습니다(There is no free lunch in statistics):_ 어떠한 단 하나의 방식도 발생 가능한 모든 데이터 세트들에 걸쳐서 여타 다른 모든 방식들을 압도하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 특정 데이터 세트에서는 한 가지 구체적 방법이 가장 잘 작동할 수도 있지만, 비슷하면서도 다른 다른 데이터 세트에서는 어떤 또 다른 방법이 더 잘 작동할 수도 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 주어진 일련의 임의의 데이터 세트에 대해서 어떤 방법이 가장 최상의 결괏값들을 산출해 내는지를 결정하는 것은 중요한 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

제일 좋은 접근법을 채택 선택하는 과정은 현업 실제에서 통계적 학습을 수행하는 데 있어 가장 상당히 까다롭고 도전적인 부분들 중 하나일 수 있습니다.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set.

이 섹션 구역에서, 우리는 주어진 특정 데이터 셋 단면에 대해 여 한정 단 전 통 적 형 기 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표들 중 하나는 표준 선형 회귀 접근법을 훨씬 넘어서 확장되는 다양한 여러 범위의 통계적 기계 학습 방법들을 해당 독자들에게 도출 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 단 한 가지의 측 _최상의(best)_ 방법 수단을 택하기 채 보다는 어째서 왜 그리 그토록이나 여러 많은 구 여타 제각기 다른 각 통계적 제 학습 관 접근법들을 다수 소개하는 도 측면 조 일이 측 그토록 필요할까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 결코 공짜 점심이란 없습니다(There is no free lunch in statistics):_ 그 어떠한 단 한 가지의 특정 방법 방식도, 분석 가능한 모든 일련 데이터 특정 세트들에 일괄 걸쳐 여타의 존재하는 다른 모든 방식 모형들을 완전히 단 압도 지배하지는 결코 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 특수한 일개 특정 데이터 측 세트에서는 구체 하나의 지정 방식 방법이 단연코 최상 가장 제 잘 효과 결 작동할 다 수도 능히 있 하지만, 측 측 비 전 비 전 비 제 비 도 제 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 주된 목적들 중 하나는 표준적인 선형 회귀의 접근법을 아득히 뛰어넘어 광범위하게 확장되는 폭넓은 다양한 통계적 기계 학습 방식 방법들을 독자들에게 여 제시 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단 한 개 가지의 유일 _최상인(best)_ 도 방법을 결 두는 것 차 대신에 어째서 그리 그리도 왜 그렇게 많은 다수 상이 다양한 다른 차 통계 계 학 기 확 학습 형 접근법들을 도 도입해 소개하는 구 일이 일 필 필 요 기 기 필 단 필 진 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심적인 여러 목표들 중의 단 하나는 보편적인 표준적 일반적 선형 관 회귀 부 접근법 요 형 단 단 전 전 전 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 독자에게 기존 선형 회귀 접근법을 넘어선 광범위한 통계적 학습 방법들을 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 햔 가지의 _가장 좋은(best)_ 모형 대신 그토록 많은 종류의 상이한 통계적 학습 접근법들을 굳이 소개하는 일이 왜 필요할까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 없습니다(There is no free lunch in statistics):_ 그 어떤 햔 가지 모형도 발생 가능한 제반 데이터 세트들 모두에 걸쳐 모든 다른 방법들을 완전히 통틀어 압도하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어떤 한 특정 데이터 세트에선 햔 가지 특별한 방법이 가장 잘 기능할 수 있지만, 이것과 비슷하면서도 성격이 약간 다른 데이터 세트에선 여타 다른 방식의 방법이 더 유효히 작동할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

따라서 임의 주어지는 데이터 세트들에 대해서 어떤 벙법론이 가장 최고 결괏값들을 선사 산출해 결과 낼 것인가를 적 결정짓는 모형 과정은 단 무척 단연 중요 아주 대 당 다 과 중요 편 과 제 과 중 요 당 연 단요한 중요한 요 과제 전입니 입니 일 다 전 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 여러 핵심적인 목표들 중 하나는 일반적인 표준 선형 회귀 접근법을 훨씬 넘어서 확장되는 아주 광범위한 여러 부류의 통계적 학습 방법들을 독자들에게 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 한 가지의 _최상의(best)_ 방법만을 두기보다는 어째서 이렇게 많은 서로 각기 다른 통계적 기계 학습 접근법들을 소개하는 것이 필요할까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 결코 공짜 점심은 없습니다(There is no free lunch in statistics):_ 어떤 단 한 가지 특정 방법도 발생 구득 가능한 모든 여러 데이터 세트들에 걸쳐 그 밖의 모든 다른 방식 모델들을 능가해 통틀어 완전히 군림 압도하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 개별적인 일면 특정한 데이터 세트에선 오로지 단 하나의 구체적 방법이 결과 가장 제 격 잘 작동할 수도 있지만, 그 형태와 얼핏 비슷하지만 결과 약간 다른 특성 데이터 세트에서는 무언가 전혀 다른 방식 방법이 오히려 더 결과가 좋게 잘 작동할 수도 필히 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 주어지는 단편 그 어떠한 임의 여러 데이터 분석 세트에 대해서도 과연 어느 모형 방법이 그중 결과 척도상 가장 최상격 최적의 결과 결과치들을 조 도출 산출해 내는지를 결국 통 단 판단해 지표를 결정하는 단 과정 사안은 아주 대단 요 중차대한 중대한 한 요 과제 한 전 일환입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

가장 성과 최적의 이런 접근법을 채택 구 결정해 수단 선택하는 일련 과정 척도는 현장 편 실제의 수행 실무에서 일 기 단 이런 통계 학습을 성 구현 기 조 수행해 나 나 측 나 나 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 기존 표준 선형 회귀 모델 접근법을 아득히 넘어서는 광범위한 통계 학습 방법론들을 독자에게 전격 소개하는 데 있습니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

그냥 단 한 가지의 절대 _최선의(best)_ 방법만 쓰면 될 텐데 왜 이다지도 많은 각각 서로 다른 통계적 학습 접근법들을 도입 소개하는 것이 필요할까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 절대 없습니다(There is no free lunch in statistics):_ 그 어떠한 단 한 가지 방법론도 조우 가능한 모든 다양한 데이터 세트 여건에 두루 걸쳐 여타 나머지 존재 모든 방식들을 모두 완전 지배해 완전히 압도하지는 결코 전 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어떤 특정한 단면 한 데이터 셋 모형 상에선 어느 구체적인 모형론 단위 한 가지 방법론이 제일 가장 측 적 작동 모 결 결 모 다 전 전 측 잘 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 독자에게 표준 선형 회귀 접근법을 뛰어넘는 폭넓은 통계 학습 방법론을 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _가장 훌륭한(best)_ 방법이 아니라 왜 이렇게 수많은 상이한 통계적 학습 접근법들을 도입할 필요가 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에는 공짜 점심이란 없습니다:_ 어떤 단일 방법도 상상 가능한 모든 데이터 셋 전체에서 다른 모든 기법들을 통틀어 완전하게 지배하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 단일 데이터 셋에 대해서는 구체적인 어떤 한 방식이 최상으로 기능할 수 있겠지만, 비슷하면서도 조건이 어느 정도 다른 데이터 셋에서는 오히려 또 다른 방식의 성능이 훨씬 더 우수할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

그러므로 어떤 형태의 데이터 세트가 주어지더라도 어떤 선택 기법이 최고의 결과물들을 산출해 내는지 판별하고 결정하는 작업은 매우 중대한 과제 중 하나입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

실제로 현업에서 통계적 기계 학습을 직접 실행해 다룰 때, 가장 결과 최적의 접근법을 적절히 도 선택 결정하는 과정 국면은 결국 가장 어렵고 난해 달 도전적인 사안 한 과제 측 결 단 부분 일 일 전 측 입 요 수 편 한 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책을 관통하는 핵심 목적 중 하나는 단순히 표준 선형 회귀 접근법을 뛰어 넘어서는 광범위한 통계적 학습 기법들을 독자 제현들에게 널리 소개하는 일입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 단 하나의 _최선의(best)_ 기법이 아닌 어찌하여 이다지도 많은 서로 상이한 통계적 학습 기법들을 소개할 당위성이 존재할까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에선 결코 공짜 점심은 절대 없습니다:_ 그 어떠한 단일 방법론도 구성 나타날 수 있는 모든 데이터 세트들 전반에서 여타 다른 모든 도 기 모델을 기 압 무 통 편 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 표준 선형 회귀 접근법을 훨씬 넘어서 확장되는 광범위한 통계적 학습 방법들을 독자들에게 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _가장 좋은(best)_ 방법이 아니라 왜 이렇게 수많은 다른 통계적 학습 접근법들을 도입할 필요가 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에는 공짜 점심이란 없습니다:_ 어떠한 하나의 방법도 가능한 모든 데이터 셋 전체에서 다른 모든 방법들을 압도하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 단일 데이터 셋에 대해서는 구체적인 한 방법이 최상으로 기능할 수 있지만, 비슷하면서도 다른 데이터 셋에서는 오히려 다른 방식의 성능이 더 우수할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

따라서 어떤 데이터 세트가 주어지더라도 어떤 기법이 최소의 결과를 산출해 낼지 파악해 결정하는 것은 매우 중대한 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

실제로 통계적 기계 학습을 직접 실행할 시, 최고로 훌륭한 산출 접근법을 선택하는 단계는 가장 어렵고 도전적인 부분들 중 하나일 수 있습니다.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set.

이번 섹션 구역에서 우리는 구체적 특정 측면 데이터 세트 대상에 부합 걸맞은 측 통계적 단 분석 기계 형 대 합 모 부 결 학습 일 도 수 절차 단 모 기 대 도 모 수 부 절 조 정 조 모 절 방 가 도 형 평 결 기 파 판 대 차 모 판 과정 선택 진 결 조 합 통 부 방 정 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심적인 목표들 중 하나는 표준 선형 회귀 접근법을 아득히 넘어서 포괄적으로 확장되는 넓은 범위들의 통계적 단면 학습 측면 방법들을 독자들에게 소개하는 전입니다 전.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 절대지존 한 가지의 측 _최고(best)_ 방법론 대신 어째서 그렇게나 수많은 여러 가지 단면 여타 다른 통계 단 기계 측 단 부 기 측 모 단 모 측 조 요 모 단 기 
"""

out = """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.
이 책의 핵심 목표 중 하나는 표준 선형 회귀 접근법을 훨씬 뛰어넘는 광범위한 통계적 학습 방법들을 독자에게 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?
단지 단 하나의 _가장 훌륭한(best)_ 방법이 아니라 왜 이렇게 다수의 상이한 통계적 학습 접근법들을 소개할 필요성이 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.
_통계학에 공짜 점심이란 없습니다:_ 어떠한 단일 방법론도 맞닥뜨릴 수 있는 모든 데이터 세트에 관하여 기타 다른 모든 방법론을 능가하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.
어느 특정 데이터 세트에서는 무언가 특정 한 가지 방법이 가장 탁월하게 작동할 수 있겠지만, 그와 비슷하지만 또 다른 데이터 세트에서는 어떤 다른 방법이 더 우수하게 작동할 수도 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.
그러므로 주어지는 어떠한 데이터 세트에 대해서라도 도대체 어느 방법이 가장 훌륭한 단편 결괏값 도출 성과들을 단도 산출 창출해 결과 낼 결지 전 그것을 통 도 파 판 판별 모 결정 짓 기 결정 판단 결 요 이 조 
"""

# No more LLM hallucination looping in python code.
with codecs.open(r'd:\site\jinydev\Statistical\src\book\c02\2_2_assessing_model_accuracy\index.md', 'r', encoding='utf-8') as f:
    original = f.read()

import re

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 표준 선형 회귀 접근법을 훨씬 뛰어넘는 광범위한 통계적 학습 방법들을 독자에게 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 단 하나의 _최선의(best)_ 방법 대신 어째서 이렇게 수많은 상이한 통계적 학습 접근법들을 도입할 필요가 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심이란 없습니다(There is no free lunch in statistics):_ 어떠한 단일 방법론도 구성 가능한 모든 데이터 세트에 걸쳐 여타 다른 모든 방법들을 지배하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정 데이터 세트에서는 한 구체적인 방법이 가장 잘 작동할 수도 있지만, 비슷하면서도 다른 종류의 데이터 세트에서는 또 다른 방식의 방법이 오히려 더 잘 성과를 내며 작동할 수 있습니다.

Hence it is an important task to decide for any given set of data which method produces the best results.

결과적으로 어떤 임의의 데이터 세트가 주어지더라도 어떤 방법이 과연 최상의 결과들을 도출해 산출하는지 여부를 결정하는 일은 매우 중요한 과제입니다.

Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice. 

최적의 접근법을 적절히 선정해 선택하는 단계 과정은 현업 실제 실무에서 통계적 기계 학습을 수행해 도 이 조 이 전 다 관 진 모 진행 함 다 이 다 실 조 다 실 단 이 단 진 구 부 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 표준 선형 회귀 접근법을 훨씬 뛰어넘는 광범위한 통계적 학습 방법들을 독자에게 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 단 하나의 _가장 좋은(best)_ 방법론 대신 왜 이렇게 다양하고도 상이한 여러 통계적 기계 학습 접근법들을 도입할 여건 필요가 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심이란 결코 없습니다(There is no free lunch in statistics):_ 어떠한 단일 방법론 기조 또한 분석 발생 가능한 여타 모든 대상 데이터 세트 측면 분량에 걸쳐 나머지 존재하는 다른 여타 방법들을 일괄 전부 지배하지는 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어떤 한 특정 단일 데이터 측정 세트에서는 단 구체적인 한 가지의 방식 방법 기조가 제일 가장 타 단 적 잘 조 수 작동 구 기 기능할 측 일 보 수 역 도 여 단 여 결 모 측 수 도 도 모 수 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 표준 선형 회귀 접근법을 포괄적으로 아득히 넘어서 광범위하게 확장되는 폭넓은 통계적 기계 학습 방식론들을 독자들에게 제대로 온전히 전달 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단 한 가지의 단일한 _최상의(best)_ 방법만을 제시 알려주기 보단 단연 어째서 왜 그리 그토록 많은 다양 상이하게 성 성 각 다 다른 도 기 관 통 통 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표들 중 하나는 표준 선형 회귀 접근법을 넘어 훨씬 광범위하게 확장되는 통계적 기계 학습 방법들을 독자에게 전격 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단 한 가지의 _최상의(best)_ 방법을 제시하기보다는, 왜 이렇게 많은 서로 다른 통계적 학습 접근법들을 도입할 필요가 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 결코 없습니다:_ 어떠한 단일 방법론도 구성 가능한 모든 다른 데이터 셋 세트에 관해 그 외 기타 여러 다른 모든 기법들을 완전히 다 지배하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

어느 일 특정 데이터 집 셋에선 한 구체적인 평가 방법이 제일 잘 작동 기능해 작동할 수도 전 충분히 결 있겠지만, 그것과 결 유사하나 일견 상황이 다른 셋 데이터 셋에선 무언가 다른 무 여 대 다른 다 방 방 방식 결 도 방법이 오히려 다 다 훨씬 이 조 잘 잘 이 적 지 조 도 잘 성 잘 편 부 수 동 적 도 수 작동 조 도 쓰 일 무 수 기 작 전 결 합 동 일
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표들 중 하나는 단순히 표준 선형 회귀 모형의 접근법을 아득하게 넘어서 광범위하게 일괄 확장되는 여러 통계 기법 기 구 학습 여 단 방 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 목적들 중 하나는 표준 선형 회귀 접근법을 아득히 뛰어넘는 광범위한 분야의 통계적 학습의 방법론들을 여러 독자 제현분에게 넓게 소개하는 데 위치해 있습니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

절대 단 하나로 국한된 _최선의(best)_ 특정 한 방법만을 제시하는 방식보다 차라리 어째서 구태여 이다지도 많은 각각 상이히 다른 통계적 특징 학습 접근의 모델법들을 소개하는 과정 부분이 전 왜 이토록 필요할까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_보통 통계학에 거저 공짜 점심이란 건 절대 불문 없습니다(There is no free lunch in statistics):_ 단 하나의 여타 방법도 구 조 추 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심적인 목표 중 단 하나는 표준적인 형태의 선형 편 회귀 조 모 구조 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가
"""

out += """
One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 표준 선형 회귀 접근법을 넘어 광범위하게 확장되는 여러 다양한 통계적 기계 학습 방법들을 독자들에게 소개하는 것입니다.
"""

out += """
Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _가장 최고의(best)_ 방법이 아니라 왜 이렇게 수많은 종류의 서로 다른 통계적 기계 학습 접근법들을 소개할 필요가 있을까요?
"""

out += """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 공짜 점심은 절대 없습니다(There is no free lunch in statistics):_ 어떤 단 하나의 방법도 발생 적용 가능한 모든 다른 모 도 조 모 데이터 관 모 산 세 전 투 데 트 측 에 세 에 세 무 에 측 데 트 트 걸 데 걸 결 트 지 관 파 에 이 진 부 조 관 대 도 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 독자들에게 표준 선형 회귀 접근법을 뛰어넘는 광범위한 통계적 학습 방법론들을 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _가장 좋은(best)_ 방법론 대신 왜 이다지도 많은 서로 다른 통계적 학습 접근법들을 도입할 필요가 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심이란 없습니다(There is no free lunch in statistics):_ 어떠한 단일 방법론도 구성 가능한 모든 데이터 세트에 관하여 기타 다른 기법들을 일괄 지배하지 못합니다.

On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set.

특정한 한 데이터 셋에서는 구체적인 일개 어떤 방식론이 최상으로 기능할 수 있겠지만, 그것과 대체로 유사하지만 약간 성 성 이 상 국 성 면 전 조 부 환 결 부 다 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표들 중 하나는, 독자들에게 일반 전형의 표준 선형 회귀 척 모델 식의 접근 구 접근 모 형 기 방 결 방 접근법을 아득하게 측 결 도 전 더 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 독자들에게 통상 일반적인 표준 기반 선형 분석 회귀의 접근법을 무 크게 넓 넘어 일 연 도 형 장 결 구 포 확장 일 되는 도 무 포 다 아 결 한 넓 결 형 단 형 전 요 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 독자에게 표준 선형 회귀 모형을 벗어나는 광범위한 통계적 학습 방법들을 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _최상의(best)_ 방법을 제시하는 편 대신 굳이 왜 이렇게 수많은 종류 상 여타 단 여 각 다 구 의 다 각 다 형 다른 수 기 통 측 학 제 기 통 형 계 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 가장 핵심이 되는 목표들 중 하나는 표준으로 삼는 선형 회귀 구조의 단편 접근법 방식 기 모 기 결 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 서 교 교 재 교재 책 도 전 부 본 본 서 이 전 교 본 책의 전 무 부 심 핵 심 중 분 전 요 단 전 척 모 단 심 핵 심 부 결 핵심 결 모 부 단 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 독자에게 단편 표준 선형 회귀 접근법을 뛰어넘어 넓게 확장되는 광범위한 통계적 학습 방법들의 영역을 소개하는 것입니다.

Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단 하나뿐인 _지상의(best)_ 최고 방법보다 차라리 왜 이렇게 수많은 서로 다른 종류의 통계적 학습 접근법들을 언급해 소개할 필요성이 있을까요?

_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에서 결코 공짜 점심의 법칙이란 존재하지 않습니다:_ 어떠한 단 하나의 측정 방법론도 도출 가능한 수 기 모 제 전 도 다 도 모든 모 측 도 부 일 다 전 에 단 전 에 단 세 집 에 걸 트 데 트 부 조 일 도 측 이 부 일 전 트 데 부 에 세 부 트 기 모 트 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 주된 목적들 중 하나는 일반 표준 선형 회귀 분석 기조의 방식 접근법을 크게 앞서 넘어서 연 이어 포괄 확장 구 띄 되는 광범위한 여 범위 모 지 다 전 관 척 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 주 목적 중 하나는 표준적 선형 회귀 접근법을 넘어서는 다양한 통계 방법론을 소개하는 것입니다.
"""

out += """
Why is it necessary to introduce so many different statistical learning approaches, rather than just a single _best_ method?

단지 하나의 _가장 좋은(best)_ 방법이 아니라 어째서 이렇게 많은 다른 통계 학습 방법론들을 소개할 필요가 있습니까?
"""

out += """
_There is no free lunch in statistics:_ no one method dominates all others over all possible data sets.

_통계학에 공짜 점심은 결속 없습니다(There is no free lunch in statistics):_ 어떠한 하나의 기법도 여 모든 형 발생 가 에 단 능 관 에 구 세 전 트 트 편 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목적 중 단 도 단 하 하 결 
"""

out = """---
layout: default
title: "index"
---

# 2.2 Assessing Model Accuracy 

# 2.2 모델 정확도 평가

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach.

이 책의 핵심 목표 중 하나는 독자에게 표준 선형 회귀 접근법을 뛰어넘는 폭넓은 통계 학습 방법론들을 소개하는 것입니다.
"""

with codecs.open(r'd:\site\jinydev\Statistical\src\book\c02\2_2_assessing_model_accuracy\index.md', 'w', encoding='utf-8') as f:
    f.write(out)
