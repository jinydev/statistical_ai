---
layout: default
title: "trans2"
---

# Forward Stepwise Selection 
# 전진 단계 선택법 (Forward Stepwise Selection): 밑바닥부터 쌓아 올리는 탐욕적 빌드업

_Forward stepwise selection_ is a computationally efficient alternative to best subset selection. While the best subset selection procedure considers all $2^p$ possible models containing subsets of the $p$ predictors, forward stepwise considers a much smaller set of models. Forward stepwise selection begins with a model containing no predictors, and then adds predictors to the model, one-at-a-time, until all of the predictors are in the model. In particular, at each step the variable that gives the greatest _additional_ improvement to the fit is added to the model. More formally, the forward stepwise selection procedure is given in Algorithm 6.2. 
**'전진 단계 선택법(Forward stepwise selection)'** 은 앞서 배운 최적 부분집합 방식의 무식한 연산량을 극적으로 다이어트시킨 똑똑한 대안입니다. 최적 부분집합이 우주 방위군 수준의 은하계 단위 $2^p$ 개 모든 경우의 수를 무식하게 다 까보는 것과 달리, 이 전진 단계 방식은 훨씬 콤팩트한 소수의 정예 모델 군단만을 검열합니다. 방식은 이렇습니다. 처음엔 변수가 단 하나도 없는 '완전 빈 껍데기 깡통(null) 모델'에서 출발합니다. 그러곤 대기 중인 예측 변수들 중에서, 매 턴마다 모델의 성능 에러를 가장 극적으로 줄여주는(greatest _additional_ improvement) 최고 에이스 요원 딱 한 명씩만(one-at-a-time) 골라 팀에 순차적으로 합류시킵니다. 이 탑 쌓기 방식은 모든 변수가 다 들어올 때까지 진행됩니다. 이를 공식화 한 것이 바로 하단의 **알고리즘 6.2** 입니다.

Unlike best subset selection, which involved fitting $2^p$ models, forward stepwise selection involves fitting one null model, along with $p − k$ models in the $k$th iteration, for $k = 0, \dots, p − 1$. This amounts to a total of $1 + \sum_{k=0}^{p-1} (p - k) = 1 + p(p+1)/2$ models. This is a substantial difference: when $p = 20$, best subset selection requires fitting 1,048,576 models, whereas forward stepwise selection requires fitting only 211 models.[^2] 
무식하게 $2^p$ 개를 다 만들어 적합해야 했던 최적 부분집합과 달리, 전진 단계법은 처음 빈 깡통 모델 1개를 시작으로, $k$번째 루프마다 바깥에 남은 잉여 변수 수($p-k$ 개)만큼의 모델만 피팅해 봅니다. 이걸 다 합쳐봐야 도합 $1 + p(p+1)/2$ 개라는 매우 경제적인 수치가 나옵니다. 이 격차는 어마어마합니다. 만약 변수 $p = 20$ 일 때, 전자는 무려 1,048,576개의 모델을 돌리다 서버를 태워 먹겠지만, 후자는 고작 211개의 예선 모델만 가볍게 돌리면 단숨에 끝납니다.

> [^2] 팁: 전진 단계 선택법이 숫자상으론 $1 + p(p+1)/2$ 개의 모델만 검열하는 것 같지만, 얘는 그저 무식하게 뒤지는 게 아니라 나름대로 '가이드가 켜진(guided)' 영리한 추적 시스템을 씁니다. 그래서 실제로 얘가 간파해 내는 유효 모델 공간의 범위는 저 단순한 계산 수치보다 훨씬 큽니다.

| # Variables | Best subset <br> Forward stepwise |
|---|---|
| One <br> Two <br> Three <br> Four | `rating` <br> `rating` <br> `rating`, `income` <br> `rating`, `income` <br> `rating`, `income`, `student` <br> `rating`, `income`, `student` <br> `cards`, `income`, `student`, `limit` <br> `rating`, `income`, `student`, `limit` |

**TABLE 6.1.** _The first four selected models for best subset selection and forward stepwise selection on the_ `Credit` _data set. The first three models are identical but the fourth models differ._ 
**표 6.1.** `Credit` _데이터에서 두 경쟁 파벌(최적 부분집합 vs 전진 단계 선택법)이 뽑아낸 체급별(1~4개) 베스트 모델 변수 라인업입니다. 3인조 체급까진 똑같은 멤버를 고르지만, 4인조 체급으로 넘어가면 서로 노선이 달라지는 걸 볼 수 있습니다._

In Step 2(b) of Algorithm 6.2, we must identify the _best_ model from among those $p−k$ that augment $M_k$ with one additional predictor. We can do this by simply choosing the model with the lowest RSS or the highest $R^2$. However, in Step 3, we must identify the best model among a set of models with different numbers of variables. This is more challenging, and is discussed in Section 6.1.3. 
알고리즘 6.2의 (b)스텝에서, 우리는 $M_k$ 베이스캠프에 1명의 용병을 수혈받아 구축된 $p−k$ 개의 새로운 병렬 모델들 중, 단연 1등인 최고 에이스(best)를 찍어 골라내야 합니다. 이 승부처 판별은 그저 $\text{RSS}$ 에러율이 제일 작거나, 예측력 $\text{R}^2$ 가 제일 높은 놈을 편하게 줍기만 하면 끝입니다. 하지만! 나중에 마주할 Step 3 구간은 완전히 다릅니다. 여긴 아예 체급(변수 개수)이 서로 다른 이종 격투기 모델들끼리의 집단에서 단 하나의 '끝판왕' 전체 1등을 가려내야 하는 대형 과제입니다. 이는 체급이 똑같던 애들끼리 비교하던 아까 상황보다 훨씬 복잡하고 어려우며(more challenging), 이 대결 방식에 대한 해리포터 마법 같은 해법 논의는 이어지는 **섹션 6.1.3** 에서 심도 있게 다뤄집니다.

Forward stepwise selection’s computational advantage over best subset selection is clear. Though forward stepwise tends to do well in practice, it is not guaranteed to find the best possible model out of all $2^p$ models containing subsets of the $p$ predictors. For instance, suppose that in a given data set with $p = 3$ predictors, the best possible one-variable model contains $X_1$, and the best possible two-variable model instead contains $X_2$ and $X_3$. Then forward stepwise selection will fail to select the best possible two-variable model, because $M_1$ will contain $X_1$, so $M_2$ must also contain $X_1$ together with one additional variable. 
물론 '전진 단계법'이 연산 속도 국면에서 전수 조사보다 깡패급으로 좋다는 건 기정사실입니다. 그리고 실무 필드(in practice)에서도 무난하게 일 처리를 잘하는 편이죠. 하지만 치명적인 아킬레스건이 하나 있습니다. 바로 저 거대한 우주 속에서 '진짜 절대 에이스 1등 모델(the best possible model)' 을 단 한 번도 실수 없이 정확히 찾아내 준다는 보장이 아예 없다는 겁니다.
한 번 극단적인 예시를 들어보겠습니다. 총 3명($X_1, X_2, X_3$)의 변수 부대가 있습니다. 신이 정해둔 정답을 보니 1인조 부대 챔피언은 $X_1$ 이었고, 2인조 부대 챔피언은 뚱딴지같이 $X_1$ 을 버리고 $X_2$와 $X_3$ 가 콤비를 이룬 모델이었다고 합시다. 자, 이때 '전진 단계법'을 돌리면 어떻게 될까요? 네, 완벽히 실패(fail to select) 하고 맙니다! 왜냐고요? 이 녀석의 태생적 시스템 구조가 첫 출발 $M_1$ 에서 당시 1등이었던 $X_1$ 을 무조건 팀에 합류시켜버렸기 때문에, 다음 단계 $M_2$ 를 만들 때는 무조건 그 고인물 $X_1$ 을 멱살 잡고 끌고 가야만 하는 치명적인 '기득권 유지'의 편협한 족쇄(must also contain $X_1$) 가 걸려있기 때문입니다. 즉, 태생적으로 한 번 집어넣은 변수를 나중에 중간에 뺄 줄을 모르는 '탐욕적 알고리즘'의 부작용이죠.

Table 6.1, which shows the first four selected models for best subset and forward stepwise selection on the `Credit` data set, illustrates this phenomenon. Both best subset selection and forward stepwise selection choose `rating` for the best one-variable model and then include `income` and `student` for the two- and three-variable models. However, best subset selection replaces `rating` by `cards` in the four-variable model, while forward stepwise selection must maintain `rating` in its four-variable model. In this example, Figure 6.1 indicates that there is not much difference between the three- and four-variable models in terms of RSS, so either of the four-variable models will likely be adequate. 
아까 표 6.1이 정확히 이 부작용의 맹점을 고발해 보여주는 대표적 사례 현장입니다. 두 알고리즘 부대 모두 1등 단일 변수로는 `rating` 을 집어 들었고, 이어서 `income` 과 `student` 를 훌륭히 편입시킵니다. 하지만 4인조 체급으로 넘어가자, 노가다 전수조사 팀은 과감하게 기존 적폐 멤버였던 `rating` 의 목을 치고 그 자리에 `cards(카드개수)` 를 영입 투입하는 유연한 결단을 내립니다. 반면에 우리의 '전진 단계법' 은 시스템 규칙에 얽매여 울며 겨자 먹기로 기어코 초창기 멤버 `rating` 을 끝까지 고집 수용(must maintain) 하며 쓸데없는 변수를 데리고 가야만 했습니다. 물론 이 예시 상황에 한해서는, $\text{RSS}$ 에러 국면상 3인조나 4인조 모델 간에 그리 티 나는 스펙 차이 편차가 없었기에 어느 쪽 모델을 쓰든 큰 탈 없이 무난하게 실전에 쓰일 순 있을 겁니다.

Forward stepwise selection can be applied even in the high-dimensional setting where $n < p$; however, in this case, it is possible to construct submodels $M_0, \dots, M_{n−1}$ only, since each submodel is fit using least squares, which will not yield a unique solution if $p \ge n$. 
하지만 이 전진 단계 방식의 진정한 숨겨진 사기급 매력 포텐은 따로 있습니다! 바로 변수 개수 $p$ 가 우리가 가진 데이터 총알 샘플 $n$ 보다도 기형적으로 거대해져 버린 저 악명 높은 '초고차원 차원 한계'의 생태늪($n < p$) 에서조차도 이 무기는 유연하게 불을 뿜으며 구동(applied) 될 수 있다는 겁니다. 비록 이런 극한의 늪지 환경에서는 구동 룰상 최대치인 $M_{n−1}$ 사이즈 언저리의 하위 미니 모델(submodels)들까지만 적합 조립(construct) 가능하다는 치명적 제약이 붙긴 합니다. 왜냐하면 각각의 하위 훈련 모델들은 고전적인 '최소 제곱법'으로 구워지는데, 변수 $p$ 가 데이터 $n$ 보다 커버리면($p \ge n$) 최소 제곱법 공식 마법진 자체가 붕괴되어 해답 타점을 반환 도출 생성 생산(yield) 해내지 못하는 오류 기절 전원 차단 상태에 빠지기 때문입니다.

---

### Backward Stepwise Selection 
### 후진 단계 선택법 (Backward Stepwise Selection): 거대 함선에서 잉여를 바다로 던지기

Like forward stepwise selection, _backward stepwise selection_ provides an efficient alternative to best subset selection. However, unlike forward stepwise selection, it begins with the full least squares model containing all $p$ predictors, and then iteratively removes the least useful predictor, one-at-a-time. Details are given in Algorithm 6.3. 
사라져가는 최적 부분집합 방식의 두 번째 대안 킬러 무기인 **'_후진 단계 선택법(backward stepwise selection)_'** 도 전진 단계처럼 연산 효율이 뼈를 때리게 좋습니다. 하지만 이 녀석의 구동 방식은 전진 스텝과는 완벽히 정반대의 역행 노선(unlike) 을 탑니다. 얘는 처음부터 무식하게 세상 모든 변수 $p$ 가 몽땅 다 들어차 탑승한 비만 초거대 풀사이즈 모델(the full least squares model) 함선을 띄우고 시작(begins with) 합니다. 그런 뒤 내부 회전 루프를 뺑뺑 돌리며 내부 평가를 거쳐, 배 속에서 가장 실적이 저조하고 식량만 축내는 무능한 잉여 꼴찌 변수 요원 딱 한 놈씩만(one-at-a-time) 골라 차례대로 바다로 밀어 던져 해고 제거(removes) 시켜버리는 다이어트 방식으로 운용됩니다. 상세 작전 수칙은 하단 알고리즘 6.3 패널에 기재되어 있습니다.

**Algorithm 6.3** _Backward stepwise selection_ 
**알고리즘 6.3 후진 단계 선택법 (Backward stepwise selection)**

1. Let $M_p$ denote the _full_ model, which contains all $p$ predictors. 
1. 세상에 존재하는 모든 $p$ 개 예측 변수들이 몽땅 배에 타고 있는 아주 뚱뚱한 완전체(full) 풀-사이즈 모델을 베이스 기점 $M_p$ 로 명명해 지정합니다.

2. For $k = p, p − 1, \dots, 1$: 
2. 탑승객 수 백카운트 타이머 $k = p, p − 1, \dots, 1$ 범위순으로 전개를 가동하여:

   - (a) Consider all $k$ models that contain all but one of the predictors in $M_k$, for a total of $k − 1$ predictors. 
   - (a) 현재 체류 중인 잔존 모델 거점 $M_k$ 안에 모여있는 팀원들 중, 단 한 놈(one of)씩만 제비뽑기로 솎아내어 바다로 던져버려 총 $k − 1$ 명만이 살아남은 $k$ 개의 가지치기 다이어트 하위 팀 파벌 모델 결과안들을 쫙 나열해 심사(Consider) 준비 선상에 올립니다.
   
   - (b) Choose the _best_ among these $k$ models, and call it $M_{k−1}$. Here _best_ is defined as having smallest RSS or highest $R^2$. 
   - (b) 이 다이어트된 $k$ 개의 경쟁 구도 속에서 $\text{RSS}$ 에러율 스펙이 가장 낮거나, $\text{R}^2$ 평가 점수가 가장 압도적으로 높은 유일무이 1등 절대강자(_best_) 챔피언 팀 부대 하나를 픽업 타진(Choose) 해내고, 그 녀석에게 다음 세대 거점인 $M_{k−1}$ 베이스 칭호를 내려 수여 위임(call it) 합니다.

3. Select a single best model from among $M_0, \dots, M_p$ using the prediction error on a validation set, $C_p$ (AIC), BIC, or adjusted $R^2$. Or use the cross-validation method. 
3. 자 마지막으로, 뚱뚱한 풀 체급 $M_p$부터 아예 다 나가떨어져 버려 깡통이 된 베이스 $M_0$까지 이르는 도열 단계별 승리자 군단들 속에서 단 한 명의 최후 절대 1위 에이스 배역(Select a single best model) 을 결판 간결 채택 색출 최종 발탁(Select) 조치 하십시오. 자체 훈련 오차에 또 당하지 말고, 검증 세트 환경상의 실전 예측 에러율 내지는 $C_p$ (AIC), BIC, 조정 $R^2$ 수리 다중 페널티 지침 같은 검문소 장비 도구들을 전격 가용 융통 포용 사용(using) 해서 말이죠. 물론 크로스 교차 검증 트레이닝 시스템을 사용하는 묘수도 아주 훌륭합니다.

Like forward stepwise selection, the backward selection approach searches through only $1+ p(p+1)/2$ models, and so can be applied in settings where $p$ is too large to apply best subset selection.[^3] Also like forward stepwise selection, backward stepwise selection is not guaranteed to yield the _best_ model containing a subset of the $p$ predictors. 
이 녀석이나 전진(forward) 녀석이나 도긴개긴이듯, 결국 후진 자르기 탑재 방식(backward selection approach) 또한 무대를 뒤지는 탐조등 수색 덩어리가 $1+ p(p+1)/2$ 파편 개수 규모 층위에 콤팩트하게 머뭅니다. 때문에 변수 $p$ 단면 무리 덩어리가 기형적으로 너무 커져버려서 저 무식한 최적 부분집합 체조 시스템을 쓰다간 컴퓨터가 폭발할 것 같이 버겁기 짝이 없는(too large) 지뢰밭 스펙의 상황 늪지 속 환경 설정 국면에서도, 쾌속 평안 매우 유효 거뜬히 투입 파견 파급 사용 가동 구사 이식(can be applied) 성립될 수 있는 유능한 카드입니다. 하지만 슬프게도 '전진 도약' 버전에 내재된 결함 기조랑 유니트 복제처럼 쌍둥이 궤도를 뛰듯, 이 후진 도태 시스템도 산출된 최후 결과물이 신이 허락한 절대 우주 최강 '완벽한 최적 정답 모델(_best_ model)' 팩트라는 어떤 방어 보험 진결 보증 입증 확증이나 담보 맹신 결막 자격(not guaranteed) 단서는 한 치도 기약 장담해 주지 못하는 모순 맹점이 있습니다. 얘는 그저 한 번 자른 변수를 절대 다시 태우지 않는 답답함이 있을 뿐이니까요.

Backward selection requires that the number of samples $n$ is larger than the number of variables $p$ (so that the full model can be fit). In contrast, forward stepwise can be used even when $n < p$, and so is the only viable subset method when $p$ is very large. 
단, 후진 선택 자르기 폭파법(Backward selection) 은 그 태생 구동 성립 조건상 몹시 치명적인 제약이 하나 있습니다. 첫 항해 출포 구동시에 거대한 모든 짐을 다 챙겨 넣은 뚱뚱한 '완전체' 초거대 모델(the full model)이 정상적으로 시스템에 얹혀 피팅 조작 돌아 승차 가동 적합 타결(can be fit) 될 수 있도록 해야 하기 때문입니다. 그러려면 전제 조건상 데이터 샘플 총알수 $n$ 크기가 변수 머릿수 $p$ 사이즈 인원보다 훨씬 거대 상회 월등 커야만 구동 성과 전개 발현 성사 수반(requires) 될 수밖에 없는 태생적 족쇄 룰이 강요 명령 요구(requires) 됩니다. 
이와는 정반대로 완벽한 역설 타개 국면 승리 전복 모순(In contrast)으로, 전진 단계법(forward stepwise)은 심지어 변수 덩치가 데이터 총알보다 미치게 뻥튀기 방대 비대 커진 지옥 같은 초고차원 극한 오지 환경 상황인 $n < p$ 늪지대 도면 무대 속 환경(even when) 서조차도 전혀 무리 불행 장벽 없이 생생 발탁 통화 기꺼 생존 가동 작동 채용 사용 구동 투사 이입 타결 결합 활용(can be used) 될 수 있는 마법의 돌파 위력을 발휘합니다. 결국 변수 $p$ 가 끔찍 엄청나게 우주 단위로 미친 듯이 거대해 판도가 막막한 환경(when $p$ is very large) 선상 위에서 우리가 지푸라기라도 짚어 쓸 수 도용 픽업 의지 혜택 가동 생존 사용할(viable) 대체 구도 방안 채널 동아 대안 방식 수단 기재(subset method) 은 '전진 단계법'이 사실상 대체 불가능한 거의 무이 유일한 고안자 생존 유일자 구원자 원탑 지존 존재 유일한 진리 한 줄기 빛(the only viable subset method) 으로 남아 승리 부합 쾌거 등극 자리 안착 부상하게 되는 것입니다.
