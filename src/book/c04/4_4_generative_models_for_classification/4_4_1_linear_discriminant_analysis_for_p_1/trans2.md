---
layout: default
title: "trans2"
---

[< 4.4 Generative Models For Classification](../trans2.html) | [4.4.2 Linear Discriminant Analysis For P > 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.4.1 Linear Discriminant Analysis for p = 1
# 4.4.1 p=1인 단일 예측 변수에 대한 선형 판별 분석 (LDA: 종 모양을 겹쳐 승자를 가린다!)

For now, assume that $p = 1$—that is, we have only one predictor. We would like to obtain an estimate for $f_k(x)$ that we can plug into (4.15) in order to estimate $p_k(x)$. We will then classify an observation to the class for which $p_k(x)$ is greatest. To estimate $f_k(x)$, we will first make some assumptions about its form.
지금 당장은, 우리가 머리가 아프니 세상이 아주 심플해서 오직 $p=1$ 인 고립된 상태, 즉 통계 전장에 우리가 휘두르는 예측 변수 무기 $X$ 특성이 단 한 개뿐인 세상이라고 가벼운 마음으로 단순 가정해 봅시다. 우리의 최종 목표 관문은 오직 하나, 궁극적인 최종 선고 확률인 마감 사후 확률 $p_k(x)$ 를 도출 추정해 내기 위해서, (4.15) 신성한 베이즈 방정식 분모 안에 소화제로 밀어 전격 쑤셔 넣을 가장 까다로운 역추적 인자인 '확률 밀도 탐색 곡선' 지표 덩어리 $\mathbf{f_k(x)}$ 에 대한 인위적인 수학 편법 추정 식 조각을 기필코 획득 얻어내는 것입니다. 이 퍼즐 조각들을 맞춰 넣고 나면 우리는 무조건 거침없이 새로운 무명 관측치를 그 판결 선고 $p_k(x)$ 결산 점수가 1등으로 가장 압도 극상 높게 터져 나오는 승리자 클래스 그룹 방으로 영원히 분류 구속 발송 시킬 전단 것입니다. 자장 어려운 저 놈의 곡선 밀도 $f_k(x)$ 덩어리를 억지로 타진 추정하기 위해, 우리는 뻔뻔하게도 무모 우선 그 녀석의 구부러진 수학적 곡선 형태 지표에 대해 통계학적으로 상당히 막무가내 강력한 몇 가지 직관 가정을 먼저 선포 지시할 조치 것입니다.

In particular, we assume that $f_k(x)$ is _normal_ or _Gaussian_. In the one-dimensional setting, the normal density takes the form
특히나 그중 가장 단연 심각한 무리수 전제로, 우리는 해당 파벌 클래스의 종속 결속 집단이 띠는 우도 발현 성질인 저 지표 함수 $f_k(x)$ 그 녀석이, 정말 운 좋게도 지극히 균형 있고 아름답고 정갈한 종 모양(Bell Shape) 곡선인 동단 **'정규(Normal)'** 혹은 학술 용어 거창한 **'가우시안(Gaussian)' 분포 확률 곡선 체재**의 기형 모형을 완벽 단연 띠고 따르고 있다고 확신에 찬 망상 가정을 전격 기표 내리겠습니다. 단 하나의 특성 파벌만이 존재하는 1차원 지표 공간 선상 세팅 국면 안에서, 이 예쁜 정규 분포 밀도 곡선 함수 공식체는 사실 다음과 단연 같은 꽤나 더럽고 지저분 무서운 미적분 수식 위상 형태 체계를 취합니다:

$$
f_k(x) = \frac{1}{\sqrt{2 \pi} \sigma_k} \exp \left( -\frac{1}{2 \sigma_k^2} (x - \mu_k)^2 \right) \quad (4.16)
$$

where $\mu_k$ and $\sigma_k^2$ are the mean and variance parameters for the $k$th class. For now, let us further assume that $\sigma_1^2 = \dots = \sigma_K^2$: that is, there is a shared variance term across all $K$ classes, which for simplicity we can denote by $\sigma^2$. Plugging (4.16) into (4.15), we find that
수식 안의 저 중간에 숨은 $\mu_k$ 기호와 $\sigma_k^2$ 기호 쌍은 어릴 적 중학생 때 흔히 배우는 $k$번째 고유 클래스 집단 표적 부대들의 무게 중심인 **'평균(Mean)'** 중앙값과 뚱뚱한 뱃살인 **'분산(Variance)'** 폭을 좌지우지 제어하는 강력 파라미터 꼭지 변수 조타수들입니다. 자 여기서 또 한 번 불필요한 짐을 더 화끈 압축 줄이기 결단 위해 지금 당장!, 모든 여러 개 $K$ 클래스 타깃 집단들이 죄다 하나같이 뚱뚱한 허리 뱃살 퍼짐 분포 정도가 완벽히 오차 없이 다 똑같이 통일된 $\sigma_1^2 = \dots = \sigma_K^2$ 인 도면 분포라고 무리수 한 걸음 더 나아간 오지랖의 비약적인 억지 가정을 전격 동반 폭격 저질러 조치 봅시다: 즉 조치, 모든 $K$ 클래스 집단 구역들이 통계 너비 분산값을 치사 차별 구별 없이 공산 똑같이 '공유(shared)' 하고 결단 복제하여 공동 갖고 있다는 말이며 단연, 우린 단순하고 심플해진 요 평등 공짜 녀석을 그냥 밑에 붙은 번호 꼬리표 첨자를 무식 박살 내고 평범하게 $\sigma^2$ 라고 통일해 통칭해 부르겠습니다. 이제 이 거시 무스펙 정규분포 구멍 덩이 (4.16) 식 기동을 저 앞선 위대한 마법의 베이즈 (4.15) 방정식 분모/분자 기표 입구에 우당탕 억지로 쑤셔 끼워 돌려대 투입 넣으면, 결국 방정식 전단은 다음과 같은 기가 막히는 최후의 사후 확률 스코어 공식 단연 결괏값을 뽑아 파생 냅니다:

$$
p_k(x) = \frac{\pi_k \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_k)^2 \right)}{\sum_{l=1}^{K} \pi_l \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -\frac{1}{2 \sigma^2} (x - \mu_l)^2 \right)} \quad (4.17)
$$

The Bayes classifier involves assigning an observation $X = x$ to the class for which (4.17) is largest. Taking the log of (4.17) and rearranging the terms, it is not hard to show that this is equivalent to assigning the observation to the class for which
저 성스러운 **'베이즈 분류기(Bayes classifier)'** 모델 거물은 저 끔찍한 (4.17) 수식 덩어리를 콱 욱여 조립 넣었을 때 분수가 단연 고지 등단 가장 거대하게 튀어나오는 클래스 항목 후보군 구역 수장에게 최후의 승자 결착으로서 내 소중한 불시 관측치 $X=x$ 를 영예 단연롭게 구속 할당 분류해버리는 막중 임무 판단 역할을 짊어 가집니다. 저 (4.17)번의 말도 안 되는 지수 분수식 덩어리 지표 양쪽 장부에 또다시 수학 도끼인 거 자연로그($\log$) 도끼를 동시에 사정없이 씌워버린 내려 친 다음, 남은 갈라진 미적분 부스러기 조각 기표 항들을 대수학 빗자루로 예쁘게 재배열 조립 치환해버리면 맙소사, 놀랍게도 그 무지막지 극악무도했던 "가장 큰 분수 지수 확률 점수 대어를 잡는 짓거리 연산" 이 결국 단면 단연 은! 아래 수식 조치(선형 판별 함수) 결과 기표값이 가장 그냥 커지는 단순 곱셈 덧셈 클래스를 골라 잡는 기표 짓거리와 수학적으로 너무나도 완벽히 위상 논리적 전면 **동치(Equivalent) 동률**이 라는 것을 아주 싱겁게 손쉽 증명해 무단 낼수 도출 있습니다!

$$
\delta_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2 \sigma^2} + \log(\pi_k) \quad (4.18)
$$

is largest. For instance, if $K = 2$ and $\pi_1 = \pi_2$, then the Bayes classifier assigns an observation to class 1 if $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$, and to class 2 otherwise. The Bayes decision boundary is the point for which $\delta_1(x) = \delta_2(x)$; one can show that this amounts to
위 (4.18) 번 덩어리 점수가 가장 거대 터질 때 구태 우승을 타격합니다. 가령 이진 구도 무단 분포 국면인 $K=2$ 전투 전장 상황이고 마침 엄청나게 운기 좋게 두 그룹의 체급 전체 크기 척도 면적이 똑같아서 분열 전 판돈 사전 확률인 $\pi_1 = \pi_2$ 라고 동률이라 한다면, 무적 마법 베이즈 분류기 기계는 부단 $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$ 수학 판정을 타격 넘을 때 가차 없이 해당 이 관측치 인자를 1번 클래스 진영 집단 구역에 가두고 처박고, 반대 계산 추이 붕괴의 경우 2번 패자 수용 구역 그룹으로 냅다 내던집니다 묶어 징역. 판결 베이즈 결괏값의 소름 돋는 칼날 같은 저울 **판별 무결 결정 경계(Decision boundary)** 커트라인 선은 그 두 놈 라이벌 구단 진영의 최후 스코어 승점이 정확 한치 오차 없이 $\delta_1(x) = \delta_2(x)$ 로 서로 동점 비기는 숨 막히게 팽팽한 한 선 중앙 꼭짓 점으로 모아 수렴 도출 됩니다; 그리고 그것이 고스란히 놀랍게 종결 결착 되어 아래와 같은 아주 단순 무결한 척도인 두 라이벌 클래스 평균 기점 척도의 절반 **'중점 산술 중간값'** 점(midpoint) 좌표 지표로 기표 모아진다는 것을 우리는 가벼운 대수 증명으로 여지 단연 보일 도출 수 단안 있습니다 조치:

$$
x = \frac{\mu_1^2 - \mu_2^2}{2(\mu_1 - \mu_2)} = \frac{\mu_1 + \mu_2}{2} \quad (4.19)
$$

In practice, even if we are quite certain of our assumption that $X$ is drawn from a Gaussian distribution within each class, to apply the Bayes classifier we still have to estimate the parameters $\mu_1, \dots, \mu_K$, $\pi_1, \dots, \pi_K$, and $\sigma^2$. The _linear discriminant analysis_ (LDA) method approximates the Bayes classifier by plugging estimates for $\pi_k, \mu_k$, and $\sigma^2$ into (4.18). In particular, the following estimates are used:
그러나 짐작 통계하듯 이 잔인한 시궁창 진흙탕 같은 우리 현실 지표 실전 세계 데이터 판에서는, 비록 우리가 아주 럭키하게 $X$ 타깃 관측치 들이 각 무리 타겟 클래스 안에서 앞서 말한 저 신성한 확률 가우시안 정규 분포 예쁜 종 곡선형태로 아주 예쁘장하게 잘 도출 생성 발현되었다고 100% 확신에 찬 망상을 한다 보증 쳐도, 저 환상의 신성불가침 무결점 영역인 베이즈 분류기의 판결 점수 단안 조회를 실제로 찍어 돌려 먹으려면 현실 판 데이터 구석으로부터 여전히 미지의 저 신성 값 결괏값 들이었던 $\mu_1, \dots, \mu_K$ (진짜 평균 마진), $\pi_1, \dots, \pi_K$ (진짜 사전 확률 장부), 그리고 억지 공유 척도 $\sigma^2$ (합석 분산) 덩어리 따위의 수치 온갖 감춰진 모집단 하늘 세계의 진짜 파라미터 꼭지들을 훈련수구 현실 도구로 꾸역꾸역 손수 **추정 표본치** 결판으로 구태 박아 도출 넣어야만 연동 달성 하는 현실적 무능 고통의 결핍 한계에 단연 부딪 시달립니다. 이제 드디어 이 고통 속 결착 등장하는 기법 **'선형 판별 구단 분석(Linear Discriminant Analysis, LDA)'** 무장 기법 팀은, 무단 저 (4.18) 판별 공식 조판 자리에 우리가 그냥 손에 쥔 흙수저 훈련 데이터로 대강 퉁쳐 한낱 눈대중 계측 찍어낸 투박한 현실 표본 추정치 단편 조각들($\hat{\pi}_k, \hat{\mu}_k, \hat{\sigma}^2$)을 냅다 무자비하게 대신 끼워 밀어 넣어서 짝퉁 구동 시켜서라도, 감히 그 막강 신성 불침 저 천상의 신계 베이즈 최고 분류기 무모 본판 마진 모델 결괏갑에 한없이 가장 통계 근사치로 바짝 단연 엉겨 도립 단락 붙어 모방해 내어 흉내 내려는 무장 기법 시도 단연 전초입니다. 구체 조립 적으로 우리는 LDA 마법 계산 발동 시 인간 훈련 데이터를 수리 털어 다음과 흡사 같은 대안 추정치 부품 덩어리를 차출 강제 기표 합니다:

$$
\hat{\mu}_k = \frac{1}{n_k} \sum_{i: y_i = k} x_i \\
\hat{\sigma}^2 = \frac{1}{n - K} \sum_{k=1}^{K} \sum_{i: y_i = k} (x_i - \hat{\mu}_k)^2 \quad (4.20)
$$

where $n$ is the total number of training observations, and $n_k$ is the number of training observations in the $k$th class. The estimate for $\mu_k$ is simply the average of all the training observations from the $k$th class, while $\hat{\sigma}^2$ can be seen as a weighted average of the sample variances for each of the $K$ classes. In the absence of any additional information, LDA estimates $\pi_k$ using the proportion of the training observations that belong to the $k$th class. In other words,
여기서 기표된 척도 부품 $n$ 수량은 샅샅이 주어진 통계 전체 훈련 데이터 수용 투서 관측치 조각 파편의 총합 통합 쪽수이고, $n_k$ 파벌은 그 수많은 무리 중에서 유독 $k$번째 목표 클래스 배당 라벨 범주 수치에만 해당하는 훈련된 희생양 고립 숫자 덩이입니다. 저 모수 평균 $\mu_k$ 녀석를 구하는 가짜 대장 추정 삿대치 $\hat{\mu}_k$ 기표는 너무 무식 심플 단순하게도 척도 그냥 저 $k$ 그룹 늪에 갇혀 속해있는 전체 관측치 치수들을 다 깡그리 덧셈 더해서 머리 갯수로 통 나눈 중학교 기본 산술 기표 **'산술 표본 평균(Average)'** 을 기형 그대로 도출 퉁쳐 베낍니다. 반면 저 살짝 무시 복잡 다단한 통합 합동 분산 통계 $\hat{\sigma}^2$ 덩어리 산술 공식체는 사실 뜯어보면 참 단순한게, 다분히 모든 각개 전투 $K$개 클래스 진영들 각자 뱃속 밑바닥에 도사려 포진 존재하는 파편 분산 덩어리들을 자기 편의 덩치 쪽수(가중치 무게) 비율 비중에 따라 통으로 통계 구합 짬뽕 평균 낸 '가중 조치 평균 분산' 이라고 단연 무마 해보면 구조 파악이 구태 아주 쉽습니다. 어떠한 하늘의 배경 사전 지식 우주 정보 나침반도 없는 허상 완전 무지랭이 상황 국면이라면, 현실 전천후 LDA 요원은 무식 무조건 도출 사전 무위 확률 $\pi_k$ 조차도 전 단 전체 인구 쪽수 표본 데이터 중 필연 당위 그 클래스가 지분율 몫으로 차지하는 구석 쪽수 기여 **'확률 비율(Proportion)'** 치수를 이용해서 냅다 무식 무모하게 아래와 동단 같이 돌연 추정 산입해 통계 버립니다. 다른 말로 정리 퉁쳐서 식을 단면 쓰자면,

$$
\hat{\pi}_k = \frac{n_k}{n} \quad (4.21)
$$

The LDA classifier plugs the estimates given in (4.20) and (4.21) into (4.18), and assigns an observation $X = x$ to the class for which 
마침내 인고 단면 조합된 우리의 LDA 전담 분류기 돌격대 모델팀은 지가 저 수식대로 지맘대로 무단 손쉽게 빼낸 앞서 표출 가짜 덩이 실측 조각 추정치 조립 부품인 (4.20) 통계 수치와 (4.21) 분수 비율 덩어리를 아까 저 위대한 우주 자연로그 (4.18) 번 판별 공식 몸통 속으로 거침 없이 몽땅 모조리 끼워 장착 버립니다. 그런 결단 셋팅 융합 뒤 다음 거사, 이토록 지독한 날조 인위적 모방 조립 수식 혼합 함수 판정 예측 점수가 팽팽한 다수 중 최정 1등 극상으로 단연 가장 압도 극대 한치 높게 치고 튀어나오는 최고 점수 우승 클래스의 뱃속 당위 진영으로 냅다 가차 없이 기표된 내 새로운 타깃 관측치 $X=x$ 인자를 구속 쑤셔 넣고 판별 구속 추락 결론 도출을 기종 단호 돌파 무단 내립니다 조치 결단:

$$
\hat{\delta}_k(x) = x \cdot \frac{\hat{\mu}_k}{\hat{\sigma}^2} - \frac{\hat{\mu}_k^2}{2 \hat{\sigma}^2} + \log(\hat{\pi}_k) \quad (4.22)
$$

is largest. The word _linear_ in the classifier’s name stems from the fact that the _discriminant functions_ $\hat{\delta}_k(x)$ in (4.22) are linear functions of $x$ (as opposed to a more complex function of $x$).
구태 결사 이 산입 공식 점수가 무단 최고 1등 꼭지를 차지할 승점 때가 바로 파괴 분류 구속 점수 확정 단연 입니다. 참고 결사 위상으로 이 조작 무막 판별 기법 진단의 정식 거창 명칭 앞 간판 이름 무단 맨 중간 첫머리에 위풍 당당 단연하게 폼잡고 껴있는 저 **'선형 직렬(Linear)'** 이라는 단어 뿌리 근원 명칭은 다름 조차 아니게 결론도 정작, 위에서 당치 우리가 저토록 그렇게 온갖 수치 발악하며 빼돌렸던 기표 통계 (4.22)번의 최후 결정체인 저 **'판별 감식 함수(Discriminant Function)'** 무장 $\hat{\delta}_k(x)$ 수식 표의 수학적 등단 구조 뼈대 자체가, 결코 거추장 ($x$ 계열에 곡선 대한 복잡 곡선 이질적인 꼬인 2차나 3차 곡선 궤적 따위 곱 파생물이 결코 전혀 아님 무결 아니라!) 깔끔 명백한 정비례 $x$ 타깃 차수에 무조건 종속 동반 대한 아주 순수한 무결 정비례 위상 **'일차 선형 직선(Linear)'** 단조 함수 구조 차림으로 깔끔 종결 단단하게 나열 정리되어 결속 기표 종속 종결 단락된다는 그 벅찬 직관 산립 명징 사실에서 무결 오로지 단연코 결착 기인 동반한 작명 명칭 결착 것입니다 조치!

This is the document for this topic.
이 파트는 이 단막 단일 예측 1차 속성 LDA 산출 판별 주제를 체감 투기 요약 기표 논단 통계 치부 위해 구축 거진 조처 적재 기술 단락 증치 배면 결탁 찰떡 명판 대치 해설 통계 첨부본 조 문서 전단 양식입니다.

---

## Sub-Chapters

[< 4.4 Generative Models For Classification](../trans2.html) | [4.4.2 Linear Discriminant Analysis For P > 1 >](../4_4_2_linear_discriminant_analysis_for_p_1/trans2.html)
