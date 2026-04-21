---
layout: default
title: "trans2"
---

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/trans2.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 **[📖 Vibe Coding 해설본]** 모델입니다! (원문이 궁금하다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 4.7.3 Linear Discriminant Analysis
# 4.7.3 전투기 발진: 직선의 암살자 선형 판별 분석(LDA) 가동

We begin by performing LDA on the `Smarket` data, using the function `LinearDiscriminantAnalysis()`, which we have abbreviated `LDA()`.
자, 이번엔 스피드 깡패 로지스틱을 집어넣고, 좀 더 정교하고 각 잡힌 직선의 암살기계인 선형 판별 분석(LDA) 무기로 `Smarket` 주식 도박장을 박살 내 볼 차례입니다. 파이썬 `sklearn` 무기고에서 워낙 이름이 긴 `LinearDiscriminantAnalysis()` 지팡이를 꺼내 쓸 건데, 숨차니까 우리는 아까 `LDA()` 로 짧게 별명을 지어 압축 소환해 뒀었죠.

We fit the model using only the observations before 2005.
물론 훈련의 철칙! 아까처럼 똑같이 2005년 미래 시험 문제지는 꽁꽁 숨겨두고, 오직 2004년까지의 과거 훈련 데이터만 먹이로 주입해서 저 기계를 똑똑하게 먼저 스파링 학습 세팅(fit) 시켜야 합니다.

```python
In [22]: lda = LDA(store_covariance=True) # 공분산(covariance) 데이터까지 알뜰하게 뇌 속에 백업 저장(store)하라고 세팅 추가!
```

Since the `LDA` estimator automatically adds an intercept, we should remove the column corresponding to the intercept in both `X_train` and `X_test`.
여기서 코딩 주의보 삐용삐용! 이 잘난 `LDA` 기계 녀석은 지 혼자 훈련 연산 돌아갈 때, 똑똑하게도 기본 과녁 영점 조절나사인 **절편(intercept)** 스탯 단서를 몰래 자동으로 자체 장착하는 버릇이 있습니다. 따라서, 만약 우리가 아까 기계에 넣어줄 총알 탄창인 `X_train` 과 `X_test` 뭉치에 바보같이 수동으로 절편 기둥 열을 이미 끼워둔 채로 또 넣으면, 나사가 중복되어 기계가 체해버립니다! 그러니까 기계에 총알을 꽂기 전, 수동 절편 기둥 열은 시크하게 파내서 칼같이 다 폭파 폐기해 버리고 날렵하게 집어넣어야 합니다.

We can also directly use the labels rather than the Boolean vectors `y_train`.
그리고 또 하나, 목표 과녁인 정답지(Y)를 넣을 땐, 굳이 아까처럼 True/False 가 판치는 암호 숫자인 부울 벡터 `y_train` 뭉치 대신, 그냥 원시적이고 사람 눈에 직관적으로 보기 좋은 문자 정답지 `L_train` (예: "Up", "Down" 텍스트 그대로!)을 곧바로 던져 꽂아 넣어도, 똑똑한 LDA 기계는 투정 안 부리고 아주아주 찰떡같이 스무스하게 잘 씹어먹습니다. 편하죠?

```python
In [23]: X_train, X_test = [M.drop(columns=['intercept']) for M in [X_train, X_test]] # 리스트 압축 마법으로 훈련/테스트 양쪽에서 절편(intercept) 기둥만 칼같이 제거(drop)!
lda.fit(X_train, L_train) # 정답지(L_train) 딱 붙여서 훈련소 스파링 가동 발진!!!
```

```python
Out[23]: LinearDiscriminantAnalysis(store_covariance=True) # 오냐, 공분산 데이터 저장하며 무사히 모델 구축 완료했다 닝겐!
```

Here we have used the list comprehensions introduced in Section 3.6.4.
설명충 타임: 저기서 우리가 쓴 `[ ... for M in ... ]` 요상하게 괄호 친 기괴한 마법 배열 코드 조합은 파이썬만의 미친 전매특허 필살기, 일명 '리스트 내포(list comprehensions)' 공법입니다.

Looking at our first line above, we see that the right-hand side is a list of length two.
코드를 째려보면, 등호 `=` 우측 편에서 두 마리 타깃(`X_train`, `X_test`)이 묶인 길이 2짜리 작은 배열 리스트 안에서 반복문 톱니바퀴가 돌아가고 있죠.

This is because the code `for M in [X_train, X_test]` iterates over a list of length two.
즉 `for M ...` 명령을 통해 저 리스트 방에 갇힌 2마리 대상을 향해 무자비하게 차례차례 기계 지시봉 순찰 루프(loop) 순회 처리를 돌리겠다는 뜻입니다.

While here we loop over a list, the list comprehension method works when looping over any iterable object.
우리는 여기서 리스트에 루프를 걸었지만, 파이썬의 이 리스트 내포 문법은 배열, 튜플, 글자 등 순서대로 하나씩 쪼개 셀 수 있는 부류의 녀석들(iterable object) 위에서라면 언제 어디서든 무식하게 잘 먹히고 작동하는 미친 효율의 문법입니다.

We then apply the `drop()` method to each element in the iteration, collecting the result in a list.
돌아가는 루프 순회마다 `X_train` 그리고 `X_test` 개체 각각 단일 속성에다가 `drop()` 메서드라는 강제 칼날을 꽂아서 거추장스러운 절편 `intercept` 부품을 강제 썰어 파내고, 그 처리가 완료된 날렵한 가공 부산물을 다시 하나의 팩 리스트로 쭉 모아 담아 반환해 버리는 겁니다.

The left-hand side tells `Python` to unpack this list of length two, assigning its elements to the variables `X_train` and `X_test`.
그러자 등호 좌측이 나서서 수거합니다. "야 파이썬, 방금 우변에서 포장된 두 개짜리 결과물 상자 다시 까서(unpack), 순서대로 기존 이름표인 `X_train` 과 `X_test` 구멍에 다시 채워 치환해 넣어라!" 라고 지시하죠. 

Of course, this overwrites the previous values of `X_train` and `X_test`.
결국 기존에 뚱뚱하게 절편이 묻어있던 옛날 객체 변수 값들은 전산상 아예 날아가고, 칼같이 다이어트된 새로운 총알들로 전면 백지 기판 덮어쓰기(overwrites) 장전이 완료 세팅되는 구조입니다! 코딩 고수 꿀팁 참 쉽죠?

Having fit the model, we can extract the means in the two classes with the `means_` attribute.
사나운 LDA 암살 모델 기계 장비를 스파링 적합(fit) 훈련을 다 마쳤다면, 이제 우린 기계 뇌를 해킹해서 녀석의 비밀 무기 스탯인 `means_` 속성을 뽑아볼 수 있습니다. 이 버튼은 기계가 파악한 "상승 팀(Up)"과 "하락 팀(Down)", 두 싸움꾼 그룹 각각의 평균(means) 능력치 스탯 요약을 토해냅니다.

These are the average of each predictor within each class, and are used by LDA as estimates of $\mu_k$.
이게 뭐냐면 각 타깃 판별 클래스 집단 안에서 힌트(`Lag1`, `Lag2`)들이 어떻게 점수가 분포되었는지 보여주는 그룹 평균 산출값이며, LDA 기계는 이 스탯 정보들을 머릿속으로 파라미터 $\mu_k$ (그 가문 클래스의 본진 기지 좌표점 추정치)로 삼아서 암살 거리를 재는 핵심 전투 파편 지표로 삼아 사용합니다.

These suggest that there is a tendency for the previous 2 days’ returns to be negative on days when the market increases, and a tendency for the previous days’ returns to be positive on days when the market declines.
토해낸 저 뇌 해킹 데이터를 재밌게 분석해 보죠! 기계가 포착한 주식판의 기이한 경향성 징후가 보이십니까? 데이터상 주식이 미친 듯이 치솟아 오른 폭등 상승장 당일(increases)에는, 오히려 폭풍 전야처럼 **과거 이틀 전 힌트 성과 점수가 음수(negative, 하락세) 구덩이**를 기록하는 징후 성향이 강했습니다. 반면 당일 주가가 수직 떡락 나락 간(declines) 피 눈물 나는 날들엔, 오히려 그 **직전 과거 이틀의 예고 성적은 달콤한 양수(positive, 상승세)** 인 징후가 뚜렷했습니다. 이 주식 도박판, 어제 돈 땄다고 좋아하면 오늘 여지없이 머리 깨진다(Mean-Reversion, 평균 회귀)는 무서운 통계 팩트 폭력 경향을 말해주는 거죠!

```python
In [24]: lda.means_ # 기계야 네가 찾은 평균 좌표 좀 까봐!
```

```python
Out[24]: array([[ 0.0426,  0.0338], # [Lag1 결괏값, Lag2 결괏값] -> 하락(Down) 팀 본진 좌표는 둘 다 플러스!
                [-0.0395, -0.0313]]) # 상승(Up) 팀 본진 좌표는 둘 다 마이너스!
```

The estimated prior probabilities are stored in the `priors_` attribute.
또한 "아무 힌트 없이 그냥 눈 감고 찍었을 때" 도박판의 기본 밑밥 클래스 출현 비율 점유율 확률인 확률 파라미터 사전 확률들(prior probabilities) 도출 점수는 기계 해킹 속성 중 `.priors_` 버튼 안에 저장 보관되어 굴러나옵니다.

The package `sklearn` typically uses this trailing `_` to denote a quantity estimated when using the `fit()` method.
참고로 지식 꿀팁: 파이썬 기계 학습 도구 `sklearn` 공구함 부품들은 `fit()` 이라는 반복 스파링 훈련을 거치고 난 뒤에 기계가 스스로 학습해 도출 터득한 "추정치 산출물 결과" 수치들 뒤에는 항상 예의 바르게 꼬리표 밑줄 `_` 문자를 은밀히 부착해 주어 마킹해 놓는 특유의 변태적인 표기 관행을 지닙니다. "이거 내가 학습해서 계산한 거야~" 라는 증표죠.

We can be sure of which entry corresponds to which label by looking at the `classes_` attribute.
근데 방금 뽑은 사전 확률 수치 `[0.491..., 0.508...]` 두 개가 대체 각각 누구(Up? Down?)의 사전 몫 배당 확률표 점수인지 헷갈린다고요? 기계 뇌의 `.classes_` 출석부 분류 체계 속성을 열어 제껴 서류를 보면 그 서열 출석 순번 정체를 아주 확고히 추적 대조해 알아낼 수 있습니다.

```python
In [25]: lda.classes_ # 야 출석부 서열 번호 까봐!
```

```python
Out[25]: array(['Down', 'Up'], dtype='<U4') # 출석번호 1번은 떡락(Down)! 2번은 떡상(Up)!
```

The LDA output indicates that $\hat{\pi}_{Down} = 0.492$ and $\hat{\pi}_{Up} = 0.508$.
아하, 출석부 순서를 보니 해답이 명확해졌죠? 즉 기득권 도출 LDA 훈련 결과는 도박장 밑밥 확률로써 $\hat{\pi}_{Down}$ (떡락할 자체 사전 확률) 은 약 49.2%, 그리고 폭주 $\hat{\pi}_{Up}$ (떡상할 자체 사전 확률) 은 약 50.8% 라는 시장 생태계 기본 비율 수치 팩트를 시사하며 적나라하게 폭로합니다.

```python
In [26]: lda.priors_ # 기본 밑밥 점수 까봐!
```

```python
Out[26]: array([0.49198397, 0.50801603]) # 아하! Down이 49%, Up이 50.8% 구나!
```

The linear discriminant vectors can be found in the `scalings_` attribute:
이제 LDA 암살 기계의 가장 무서운 핵심 부품! 직선으로 적군을 썰어버리는 칼날인 '선형 판별 설계 벡터(linear discriminant vectors)' 무기 조각들은 기계 심장 `.scalings_` 속성을 해킹하면 은밀히 확보 발견할 수 있습니다:

```python
In [27]: lda.scalings_ # 칼날 설계도 까봐!
```

```python
Out[27]: array([[-0.64201906],
                [-0.51352928]]) # Lag1 곱셈 칼날, Lag2 곱셈 칼날 점수!
```

These values provide the linear combination of `Lag1` and `Lag2` that are used to form the LDA decision rule.
이 확보 수치 도출 결과 수치들은 기계가 판단 살육 규칙(decision rule) 이라는 궁극의 LDA 계산 공식을 완성 조립 전개하기 위해 단서 무기인 `Lag1` 그리고 `Lag2` 에다가 직빵 거는 곱셈 합산식, 즉 선형 결합(linear combination) 합체 부품 공식을 우리 눈앞에 적나라하게 도출 제공해 주는 원초적 소스입니다.

In other words, these are the multipliers of the elements of $X = x$ in (4.24).
단언컨대 찐 상남자의 언어로 요약 교체하자면, 이 험악한 숫자 쪼가리들은 이전 챕터 (4.24) 수식 도면에 박혀있던 정체불명의 암호 지표식 $X = x$ 부품들 자리에 욱여넣어 대치해 폭풍 곱셈 기폭을 가할 승수 기폭제 가중치 파라미터(multipliers)들 바로 그 자신 자체입니다!

If $-0.642 \times Lag1 - 0.513 \times Lag2$ is large, then the LDA classifier will predict a market increase, and if it is small, then the LDA classifier will predict a market decline.
자, 그래서 궁극의 깡패 룰 세팅 가동이 완성되었습니다. 만약 도박 단서 스코어를 갈아 넣어 산출 조립한 저 무자비한 $-0.642 \times Lag1 - 0.513 \times Lag2$ 수식 조합 공식 계산 결과 덩치가 통계적으로 아주 우월하게 압도적으로 거대하게 크게(large) 산출 폭주 판독되면, 즉시 가차 없이 똑똑한 LDA 분류 살육 장치는 주식판이 화려하게 떡상(market increase) 할 것이라고 판단 화살을 쏘아 맞출 것이요, 반대로 모의 계산 스코어가 쪼그라들고 초라하게 산술 작게(small) 바닥 결괏값 판별이 치달으면, 여지없이 역으로 놈은 주식 장이 처참히 무너져 내릴 나락 하락(decline) 곡선을 탈 것이라고 단언하여 정조준 킬각 타겟 저격 발동 예측 계산 확정 지시를 하달할 것입니다. 아주 단순 무식하지만 살벌하죠!

```python
In [28]: lda_pred = lda.predict(X_test) # 미래의 시험지(X_test)를 줘봤다. 맞춰봐! 빵!
```

As we observed in our comparison of classification methods (Section 4.5), the LDA and logistic regression predictions are almost identical.
우리가 예전 장대한 4.5 단원의 거대한 "판별 무기 성능 대전쟁" 리그 표에서 이미 스포일러 당하고 예측 예리하게 직관 관찰(observed) 했듯이, 여기서 발진시킨 각 잡힌 LDA 기계의 도출 예측 성적과, 아까 앞에서 굴렸던 조폭 스피드 깡패 로지스틱 회귀 기계의 무차별 예측 스코어 결과치 표본들은 정말 징그러울 정도로 거울을 보듯 완벽히 흡사한 쌍둥이 데칼코마니 처럼 판별 불가하게 똑같습니다(identical). 

```python
In [29]: confusion_table(lda_pred, L_test) # LDA 기계 성적표 폭로판 발동!
```

```python
Out[29]: Truth      Down   Up
Predicted            
Down         35   35
Up           76  106 # 아까 로지스틱 회귀 때 본 숫자랑 완전 판박이!?
```

We can also estimate the probability of each class for each point in a training set.
우리는 단순히 '올라간다/내려간다' 도장만 찍는 걸 넘어서, 훈련 관측 수비대 내부 촘촘한 각 단서 조건 표본 하나의 스코어 점(point) 하나하나 단서마다, 각각 타겟 분대 클래스(떡상? 혹은 떡락?)에 배당 속할 미세한 전격 확률 점수치(probability) 확률 자체만을 오롯이 따로 분리 파편 계산 측정(estimate) 해 볼 수도 있습니다.

Applying a 50% threshold to the posterior probabilities of being in class one allows us to recreate the predictions contained in `lda_pred`.
이때, 도출 기계가 특정하게 찝어낸 맹목적 후보 소속 점수인 '1번 구역 클래스(떡상 팀)에 들어갈 사후 확률 확률치(posterior probabilities) 전산 점수' 에다가, 무식하게 아까처럼 과부하 커트라인 제한 임계선(threshold) 마지노선 타격을 강제로 50% 확률 커트라인 부여 잣대로 내려쳐 찍어 대면, 그 결과는 신기하게도 이미 우리가 아까 `lda_pred` 결과 표기 보관 가방 안에 저장했던 '흑백 확정 결과물 점수 예측 라벨' 조각들을 소름 돋게 역추적 완벽 재창조(recreate) 하여 1:1 확률 복제 쌍둥이 짝꿍 기계 연산물 일치 도식을 찍어 내게 만들어 줍니다. 수학의 신비죠!

```python
In [30]: lda_prob = lda.predict_proba(X_test) # 아예 확률 수치만 싹 다 뽑아내자!
np.all( # 뒤에 나올 조건식이 '전부 다(all)' 무조건 팩트 100% 만족하는지 참 거짓 검사해 봐!
    np.where(lda_prob[:,1] >= 0.5, 'Up','Down') == lda_pred # 확률 0.5 넘으면 Up, 아니면 Down 찍은 거랑, 아까 기계가 통째로 정답 찍은 lda_pred 랑 똑같음?
)
```

```python
Out[30]: True # 응, 계산해 보니 소름 돋게 토씨 하나 안 틀리고 수치 퍼펙트하게 똑같음!
```

Above, we used the `np.where()` function that creates an array with value `'Up'` for indices where the second column of `lda_prob` (the estimated posterior probability of `'Up'`) is greater than 0.5.
바로 전 구동 마술 기교 블록에서 우리는 데이터 조작 특수 발동 함수 부품기기 인 파이썬 넘파이 `np.where()` (야 거기 어디냐 색출해내!) 조건을 발동 사용했습니다. 이 마술 조작 도구는 기계 산출 행렬인 `lda_prob` 데이터 덩어리에서 오직 특정 속성 지정 열 2번째 정보(`'Up'` 떡상 확증 전속 마킹 계산 사후 확률 데이터 기둥 지점) 점수 값이 강제 특정 요구 통계 제약 조건인 0.5 문턱 타점을 확실히 돌파 달성 초과 넘겨버린(greater) 표본 스코어 위치(indices) 좌표 방 부분들 구역에다가 만 살벌하게 강압 문자 낙인인 고정 정적 텍스트 라벨 `'Up'` 문자열 고지서를 덮어쓰기 창출 생성 발급 삽입하는 매우 사악한 데이터 강제 날조 재편 배열 배열체(array) 변환기 무기입니다.

For problems with more than two classes the labels are chosen as the class whose posterior probability is highest:
주의할 점! 우리가 지금 상대하는 건 올라가냐/내려가냐 동전 도박 수준의 얕은 이분법 도박판이라 저딴 단순 50% 꼼수 공식이 먹혔습니다. 하지만 만약 타겟 몬스터가 클래스 분류 소속 종속 파편이 오징어, 문어, 꼴뚜기 등등 2개를 훨씬 뛰어넘는 초거대 다중 복잡 혼동 실전 도박판 범주 분류 문제(problems with more than two classes)라면 얘기가 다르고 사양 판별이 까다로워집니다. 그럴 땐 50% 타점 기준 같은 애송이 잣대는 버리고, 오직 각 치열한 투기 후보 간의 사투 점수 산출 사후 스코어 확률 퍼센티지(posterior probability) 비교 격차전에서 피 터지게 싸워 1등 살아남은, 가장 독보적으로 최고 수경지 정점을 찍은 탑클래스(highest) 특정 최고 득점 집군 하나만을 무조건 절대 유일 지목 우승 분류 라벨(labels) 승자로 낙점 지시 확정 채결하는 무자비한 생존 게임 방식으로 로직이 변경 교체 세팅되어 구동 수렴 치환됩니다.

```python
In [31]: np.all( # 뒤에 나오는 검사가 100% 완벽 일치하는지 돌려봐!
    [lda.classes_[i] for i in np.argmax(lda_prob, 1)] == lda_pred # 확률 점수 중 제일 압도적으로 높은 놈(argmax)의 출석번호표 라벨 가져온 거랑, lda_pred 랑 똑같아?
)
# (참고: 아까 [30]번처럼 50% 타점이 아니라, 여러 클래스 중 argmax 1등 꽂아 넣기 방식의 로직 증명법!)
```

---

## Sub-Chapters

[< 4.7.2.1 In 8 Results.Params](../4_7_2_logistic_regression/4_7_2_1_in_8_results.params/trans2.html) | [4.7.3.1 Out31 True >](4_7_3_1_out31_true/trans2.html)
