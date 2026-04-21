---
layout: default
title: "trans2"
---

[< 1.2 A Brief History Of Statistical Learning](../1_2_a_brief_history_of_statistical_learning/trans2.html) | [1.4 Who Should Read This Book >](../1_4_who_should_read_this_book/trans2.html)

> 💡 **학습 팁:** 조금 더 쉽고 재미있게 공부하고 싶으신가요? 이 페이지는 중학생도 이해할 수 있는 친절한 '쉬운 해설판'입니다! 영어 원문을 문장 단위로 꼼꼼하게 번역한 느낌을 원하신다면 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!

# This Book
# 이 책에 대하여 (도대체 우리가 이걸 왜 썼을까?)

*The Elements of Statistical Learning* (ESL) by Hastie, Tibshirani, and Friedman was first published in 2001.
수포자들에겐 악몽 그 자체인 전설적인 바이블, Hastie, Tibshirani, Friedman 세 천재 할아버지들이 쓴 *'통계적 학습의 요소(ESL)'* 라는 끔찍하게 두꺼운 벽돌 책이 2001년에 찬란하게 세상에 강림했습니다.

Since that time, it has become an important reference on the fundamentals of statistical machine learning.
그때부터 이 벽돌(ESL)은 통계적 기계 학습의 파라오 같은 존재(기초를 다루는 가장 중요한 참고 문헌)로 군림해 왔습니다.

Its success derives from its comprehensive and detailed treatment of many important topics in statistical learning, as well as the fact that (relative to many upper-level statistics textbooks) it is accessible to a wide audience.
이 벽돌이 그렇게 대박을 친 이유는요, 통계판의 굵직한 주제들을 그야말로 영혼까지 탈탈 터는 백과사전 급(포괄적이고 상세하게 다룸)이었기 때문도 있지만, 사실 (그 당시 외계어로 쓰인 다른 꼰대 대학원 교재들에 비하면) 그나마 '인간의 언어'로 쓰여 있어서 꽤 많은 일반인(넓은 독자층)들이 범접할 수 있었기 때문입니다.

However, the greatest factor behind the success of ESL has been its topical nature.
하지만 입에 발린 소리 빼고, ESL 책이 진짜 전 세계를 휩쓴 가장 결정적인 대박 요인은 바로 그 책이 가졌던 '기가 막힌 타이밍과 화제성' 이었습니다.

At the time of its publication, interest in the field of statistical learning was starting to explode.
책을 똭! 출판하고 났더니, 때마침 전 세계적으로 "이게 바로 미래 기술이다!" 하면서 '통계적 학습' 분야에 대한 광기가 그야말로 미친 듯이 폭발(explode)하고 있던 시기였거든요. 

ESL provided one of the first accessible and comprehensive introductions to the topic.
타이밍 오지죠? 그 당시엔 이 미친 주제를 다루는 제대로 된 책이 없었는데, ESL이 최초로 총대 메고 "옛다! 여기 종합판(포괄적인 입문서) 있다!" 하고 던져준 겁니다.

Since ESL was first published, the field of statistical learning has continued to flourish.
그 벽돌책이 세상에 던져진 이후로, 이 통계적 기계 학습 바닥은 그야말로 잭과 콩나무마냥 미친 듯이 번창하며 떡상해왔습니다.

The field's expansion has taken two forms.
이 바닥이 몸집을 불리는 방식엔 뚜렷하게 두 가지 형태(투 트랙)가 있었습니다.

The most obvious growth has involved the development of new and improved statistical learning approaches aimed at answering a range of scientific questions across a number of fields.
가장 뻔하고 당연한 첫 번째 성장은 뭡니까? 천재 학자들이 맨날 골방에 틀어박혀서 수식 깎으면서, 세상 온갖 복잡한 과학 미스터리들을 풀어보겠답시고 새롭고 삐까뻔쩍하게 진보된 통계 기법들을 마구잡이로 찍어낸(개발한) 겁니다.

However, the field of statistical learning has also expanded its audience.
그런데 말입니다... 이 바닥의 진짜 무서운 확장은 따로 있었습니다. 바로 이 학문을 뜯어먹는 **'손님들(독자층)'** 의 머릿수와 족보가 엄청나게 넓어지고 다양해졌다는 겁니다!

In the 1990s, increases in computational power generated a surge of interest in the field from non-statisticians who were eager to use cutting-edge statistical tools to analyze their data.
1990년대, 드디어 우리들의 똥컴들이 탈태환골하며 연산 파워(CPU)가 미친 듯이 좋아지자마자, 평생 수학이랑은 담쌓고 살던 **'비통계학자'** 들(생물학자, 경제학자 등등)이 눈이 뒤집혀서 "야! 나도 저 최첨단 로봇(통계 도구) 가져와서 내 병원 데이터 한 번 분석해 볼래!!" 하고 광기의 러시가 시작된 거죠.

Unfortunately, the highly technical nature of these approaches meant that the user community remained primarily restricted to experts in statistics, computer science, and related fields with the training (and time) to understand and implement them.
하지만 안타깝게도 현실은 시궁창이었습니다. 저 최첨단 로봇들을 부리는 조종법(고도로 기술적인 특성)이 수포자들에게는 완전 토 나오는 외계어였거든요. 결국 이 꿀잼 도구들을 만지작거릴 수 있는 사람들은 고된 수학 훈련을 견디고 이걸 코딩으로 구현할 여유도 있는 찐 통계충, 컴공 변태(전문가들)들 그들만의 폐쇄된 클럽으로 남아있을 수밖에 없었습니다.

In recent years, new and improved software packages have significantly eased the implementation burden for many statistical learning methods.
그런데 요 몇 년 사이에 기적이 일어났죠! 딸깍 한 번이면 지 알아서 복잡한 수학을 다 씹어 먹고 결과를 뱉어내는 킹갓 친절한 소프트웨어 패키지들이 쏟아지면서, 그 토 나오던 코딩 노가다(구현의 부담)가 기적처럼 싹 다 날아가 버린 겁니다!

At the same time, there has been growing recognition across a number of fields, from business to health care to genetics to the social sciences and beyond, that statistical learning is a powerful tool with important practical applications.
게다가 동시에 장사꾼(비즈니스), 의사 쓰앵님(건강 관리), DNA 파는 학자(유전학), 심지어 사람 연구하는 문과생(사회 과학)들까지 온 동네방네서 "와! 통계적 학습 이거 엑셀 대신 쓰니까 돈도 벌고 실무에 갖다 붙이기에 완전 개쩌는 도구구나!" 하는 진리의 깨달음(인식)이 바이러스처럼 퍼지기 시작했습니다. 

As a result, the field has moved from one of primarily academic interest to a mainstream discipline, with an enormous potential audience.
그 결과, 옛날엔 대학 노교수님들 끼리 모여서 헛기침이나 하던 학문적 뒷방(관심사)에서, 이제는 지나가는 동네 꼬마도 딥러닝 딥러닝 거리는 어마무시한 스케일의 **'우주 대 주류 학문(메인스트림)'** 으로 군림하게 되었습니다.

This trend will surely continue with the increasing availability of enormous quantities of data and the software to analyze it.
하늘에서 끝도 없이 눈덩이처럼 쏟아지는 빅데이터 폭탄과, 그걸 딸깍질로 분석하게 해 주는 미친 소프트웨어들 덕분에 이 떡상 폭주 기관차 추세는 누구도 막을 수 없게 되었습니다.

The purpose of *An Introduction to Statistical Learning* (ISL) is to facilitate the transition of statistical learning from an academic to a mainstream field.
자, 그래서 드디어 본론입니다! 우리가 이 책 **_'통계적 학습 입문(ISL)'_** 을 쓴 진짜 흑심(목적)은 바로 이겁니다! 통계적 학습이라는 이 꿀잼 놀이공원을 저 대학 산꼭대기(학계)에서 질질 끌고 내려와서, 저잣거리 민간인들 누구나 즐길 수 있는 안방 주류 세계로 아주 스무스하게 연결해 주는 '다리(transition)' 역할을 하겠다는 겁니다!

ISL is not intended to replace ESL, which is a far more comprehensive text both in terms of the number of approaches considered and the depth to which they are explored.
오해는 하지 마세요. 우리가 쓴 이 착한 ISL 책은 절대 그 전설의 벽돌책 ESL을 쓰레기통에 처넣고 대체하려고 쓴 게 아닙니다. 사실 그 벽돌책은 우주에 존재하는 온갖 잡다한 공식들과 머리털 빠지는 깊이를 모두 다루는 넘사벽 그 자체(훨씬 포괄적인 텍스트)거든요. 

We consider ESL to be an important companion for professionals (with graduate degrees in statistics, machine learning, or related fields) who need to understand the technical details behind statistical learning approaches.
그러니까 그 벽돌책 ESL은 피 터지는 수학 공식(기술적 세부 사항) 하나하나를 다 씹어 먹고 논문 써서 졸업해야 하는 '찐 전문가들(통계/인공지능 대학원생 노예들)'을 위한 성경책(동반자)으로 고스란히 모셔두는 게 맞습니다.

However, the community of users of statistical learning techniques has expanded to include individuals with a wider range of interests and backgrounds.
하지만 시대가 바뀌었습니다! 이제 통계 무기를 쓰려는 손님들은 수포자 문과생부터 회사 팀장님들까지 그 취향과 배경 출신이 정말 동묘 벼룩시장판 급으로 스펙트럼이 넓어졌단 말입니다!

Therefore, there is a place for a less technical and more accessible version of ESL.
그러니 이제 이 바닥에서도 너무 수식에 집착하지 않고(기술적 내용 덜어내고) 마우스 딸깍질로도 꿀을 빨 수 있는 **'ESL의 순한 맛, 다이어트 치팅 버전'** 이 절실히 필요한 빈자리가 뚫려버린 겁니다!

In teaching these topics over the years, we have discovered that they are of interest to master's and PhD students in fields as disparate as business administration, biology, and computer science, as well as to quantitatively-oriented upper-division undergraduates.
우리가 교수 생활 수년간 칠판에다 분필 튀기며 이걸 가르치다 보니 깜짝 놀란 사실이 있습니다. 이 머리 아픈 주제를 통계과 애들만 듣는 게 아니라 경영학과 타자기부터, 개구리 배 가르는 생물학과 애들, 코딩 치는 컴공은 물론이고, 심지어 계산기 좀 두드린다는 핏덩이 학부 고학년 애들까지 눈을 반짝이며 침을 질질 흘리는(관심 있어 하는) 걸 발견했다는 거죠!

It is important for this diverse group to be able to understand the models, intuitions, and strengths and weaknesses of the various approaches.
네, 압니다! 완전 근본 없는 짬뽕 같은 다양한 출신들이지만, 이들도 온갖 로봇(접근 방식)들이 각각 무슨 철학(모델, 직관)으로 움직이고, 어디 가서 털리면 안 되는지(장단점) 그 맥락을 뼈저리게 이해하는 건 현생을 살기 위해 꼭 필요하고 중요한 일입니다!

But for this audience, many of the technical details behind statistical learning methods, such as optimization algorithms and theoretical properties, are not of primary interest.
다만 이 광활한 일반 청중들에게 솔직히 까놓고 물어보면, 그 로봇 안에 들어간 수백 줄짜리 미분 방정식 톱니바퀴(최적화 알고리즘)나 우주 진리 같은 '이론적 속성' 따위는 1도 안 궁금하고 하등 쓸모없는 쓰레기(기피 대상)라는 겁니다.

We believe that these students do not need a deep understanding of these aspects in order to become informed users of the various methodologies, and in order to contribute to their chosen fields through the use of statistical learning tools.
그래서 우리 저자들은 확신합니다! 이들이 각자 자기 회사나 병원에 가서 저 통계 무기들을 간지나게 휘두르면서(도구 사용) 에이스로 공헌하기 위해 굳이 저런 쓸데없는 수학 방어구 따위를 피 터지게 파고들며(깊이 이해) 시간 낭비할 필요는 "전혀, 1도 없다!"라고 말입니다.

ISL is based on the following four premises.
그래서 우리들의 갓띵작 ISL은 다음의 네 가지 피의 서약(전제) 위에서 탄생했습니다.

1. Many statistical learning methods are relevant and useful in a wide range of academic and non-academic disciplines, beyond just the statistical sciences.
서약 1. **"이 좋은 걸 통계쟁이들만 꿀 빨게 둘 순 없다!"** 통계 기법들은 책상머리 학계를 넘어서 시장 바닥 피 튀기는 온갖 잡다한 비학문적 실무 동네까지 약방의 감초처럼 미치도록 유용하게 쓰일 곳이 널렸습니다.

We believe that many contemporary statistical learning procedures should, and will, become as widely available and used as is currently the case for classical methods such as linear regression.
우리는 확언합니다! 요즘 나온 삐까뻔쩍한 현대 로봇(통계 학습 절차)들 역시, 옛날 고리타분한 선형 회귀 꼰대 엑셀 함수처럼 대한민국 국민 누구나 김치 썰듯 자유분방하게 썰어대는 '국민 필수 교양품'이 무조건 될 것이고, 반드시 그래야만 한다고요!

As a result, rather than attempting to consider every possible approach (an impossible task), we have concentrated on presenting the methods that we believe are most widely applicable.
결과적으로, 세상에 떠도는 수만 가지 로봇을 하나도 빠짐없이 백과사전으로 다 욱여넣으려는 미친 뻘짓(불가능한 과제)은 과감히 집어치웠습니다. 대신 우리가 픽한 "이거 하나는 실전에서 미치도록 써먹겠다!" 싶은 초특급 우량 갓성비 기법들만 액기스로 모아서 집중 폭격(제시) 하기로 결단했습니다.

2. Statistical learning should not be viewed as a series of black boxes.
서약 2. **"통계는 마법의 요술 상자(블랙박스)가 아니다!"** 제발 데이터만 쑤셔 넣으면 아브라카다브라 정답이 튀어나오는 요술 램프로 취급하며 환상에 빠지지 마세요. 

No single approach will perform well in all possible applications.
당신이 병에 걸렸을 때 먹는 만병통치약이 없듯, 이 세상의 우주 만물 모든 문제를 완벽하게 풀어재끼는 단 한 명의 절대 로봇(접근법)은 우주 어디에도 존재하지 않습니다!

Without understanding all of the cogs inside the box, or the interaction between those cogs, it is impossible to select the best box.
그러니까 그 요술 상자 안에 쥐새끼만 한 톱니바퀴들이 수식을 어떻게 갈아먹고 서로 치고 박는지(상호작용) 대충이라도 냄새(이해)를 못 맡으면, 당신의 데이터에 딱 맞는 운명의 짝꿍 상자(최적의 옵션)를 골라잡는 건 씹덕 망상(불가능)에 불과합니다.

Hence, we have attempted to carefully describe the model, intuition, assumptions, and trade-offs behind each of the methods that we consider.
뼈 때리는 충고를 받들어, 우리 저자들은 각 무기(기법)가 탄생한 철학, 로봇의 한계(가정), 그리고 "이걸 얻으면 저걸 버려라!" 하는 피도 눈물도 없는 등가교환의 법칙(트레이드오프)을 미치도록 친절하고 조심스럽게(수식 없이) 까발려 설명하려 발악했습니다.

3. While it is important to know what job is performed by each cog, it is not necessary to have the skills to construct the machine inside the box!
서약 3. **"시계는 볼 줄 알면 그만이지, 시계 부품을 깎아서 만들 필요는 없다!"** 로봇팔이 물건을 나르는 앨리스인 건 알고 써야 하지만, 당신이 직접 쇳물 녹여서 로봇을 조립해야 하는 엔지녀(현장 요원)가 될 필요는 절대(네버!) 없다는 겁니다! 

Thus, we have minimized discussion of technical details related to fitting procedures and theoretical properties.
그래서 이 친절한 저자들은 당신이 읽다가 찢어버리고 싶어 할 "파라미터 최적화 적합 과정" 따위의 고문 기구(기술적 세부 사항과 이론적 특징)들에 대한 입 털기(논의)를 가위질로 싹둑싹둑 최소화했습니다. 

We assume that the reader is comfortable with basic mathematical concepts, but we do not assume a graduate degree in the mathematical sciences.
물론 독자 여러분이 초등학교 덧셈 뺄셈이나 기초 팩트 폭행(기본 수학 개념) 정도는 코파며 넘길 수준이라 믿겠지만, 그렇다고 당신 코털에 "나 수학 대학원 졸업장 있소!" 하고 명찰이 박혀있다고 가정하는 미친 짓(무리수)은 두지 않습니다.

For instance, we have almost completely avoided the use of matrix algebra, and it is possible to understand the entire book without a detailed knowledge of matrices and vectors.
예를 하나 들어줄까요? 수포자들의 PTSD 발작 버튼인 그 망할 **'행렬과 백터 계산'** 을 우리는 이 책에서 거의 백신 맞은 사람처럼 소름 끼치게 완벽히 따돌렸습니다. 고로 당신은 엑셀 표(행렬) 나부랭이 디테일을 1도 몰라도 이 두꺼운 책의 끝판왕 마왕까지 거뜬히 이해하며 클리어할 수 있는 파티를 맵핑한 겁니다!

4. We presume that the reader is interested in applying statistical learning methods to real-world problems.
서약 4. **"어차피 당신의 최종 목적은 현실에서 이걸로 돈을 벌고 써먹는 것이다!"** 우리는 독자 여러분이 교양 쌓으려고 이 책을 읽는 게 아니라, 세상 밖의 진짜 자기 밥그릇(현실 문제)에 이 마법(방법론)을 당장 꽂아 넣고 싶어 환장해 있다고 강력히 가정(간주)합니다.

In order to facilitate this, as well as to motivate the techniques discussed, we have devoted a section within each chapter to computer labs.
우리의 뇌피셜을 현실로 만들어 드리고, 또 "아씨, 이거 배워서 어따 써?" 하는 불만(동기 부여 하락)을 막고자, 모든 챕터 끄트머리에 오아시스처럼 직접 키보드를 타닥타닥 두들길 수 있는 짜릿한 '컴퓨터 실습(Labs) 놀이터'를 통째로 헌납했습니다.

In each lab, we walk the reader through a realistic application of the methods considered in that chapter.
이 실습 놀이터에 입장하시면, 방금 전 침 흘리며 배운 이론 무기들을 가지고 현실판 마약 카르텔이나 주식 데이터 뺨치는 꿀잼 실전 문제(응용)에다 진짜 코드를 박아보며 당신의 손을 잡고 에스코트(설명)해 드립니다.

When we have taught this material in our courses, we have allocated roughly one-third of classroom time to working through the labs, and we have found them to be extremely useful.
라떼는 말입니다... 저자들이 실제 학교에서 애들을 가르칠 때도 아예 수업 시간의 한 33%(3분의 1)를 이 실습 코딩 놀이에 통째로 꼴아박았는데, 애들 눈망울이 돌아오는 걸 보며 "와, 이게 진짜 개꿀이구나!(극적인 유용성)"를 몸소 체감했습니다.

Many of the less computationally-oriented students who were initially intimidated by the labs got the hang of things over the course of the quarter or semester.
처음엔 검은 화면만 보면 멀미를 일으키며 덜덜 떨던 심약한 문과 감성 컴맹 학생들조차도, 한 학기를 굴려보니 막판엔 자기네가 콧노래 부르며 로봇을 돌리는 경지(숙달)에 오르는 기적을 보여주었거든요.

This book originally appeared (2013, second edition 2021) with computer labs written in the R language.
사실 이 갓띵작 ISL의 초판(2013년)과 두 번째 개정판(2021년) 실습 놀이터는 죄다 통계충들의 전유물 방언인 **'R 언어'** 로 떡칠이 되어있었습니다.

Since then, there has been increasing demand for Python implementations of the important techniques in statistical learning.
하지만 세상 참 빠르죠? 딥러닝 광풍이 불면서 온 세상이 "됐고, 이걸 범용 파이썬(Python)으로 당장 가져와라!"며 바야흐로 파이썬 구현 폭동(거대한 수요 증가)이 일어나기 시작했습니다.

Consequently, this version has labs in Python.
이런 민초들의 반란을 겸허히 수용하여, 짠! 지금 여러분이 쥐고 있는 이 최신 버전 책은 실습 놀이터를 싹 다 전면 **'파이썬(Python)'** 으로 갈아엎은 버전입니다! 

There are a rapidly growing number of Python packages available, and by examination of the imports at the beginning of each lab, readers will see that we have carefully selected and used the most appropriate.
파이썬 바닥엔 하루에도 수백 개씩 코드 패키지 쓰레기들이 양산되며 돌아다니고 있는데, 독자분들이 매번 실습장 문을 열 때마다(import 문 확인) 저희가 얼마나 뼈를 깎는 고민으로 가장 우량하고 세련된 패키지만(최적의 구현) 쏙쏙 뽑아 대령했는지 그 눈물겨운 정성을 눈치채게 될 겁니다. 

We have also supplied some additional code and functionality in our package `ISLP`.
심지어 기존 패키지로 안 돌아가는 꼬인 문제들은 저희 저자진이 밥도 굶어가며 손수 깎고 빚어낸 맞춤형 사제 패키지 모듈 **`ISLP`** 까지 얹어서 풀 서비스로 공양(공급)해 올립니다.

However, the labs in ISL are self-contained, and can be skipped if the reader wishes to use a different software package or does not wish to apply the methods discussed to real-world problems.
물론, 난 독고다이라 "다 필요 없고 내 맘대로 다른 프로그램(R이나 엑셀) 쓸 거다!" 하거나, 아님 "현실 적용 1도 관심 없고 난 이론만 먹을 거다!" 하는 별종 씹선비 독자가 있다면? 쿨하게 파이썬 실습(Labs) 부분은 죄다 스킵하고 페이지를 넘기셔도 됩니다. 어차피 이 녀석들은 독립 섬(self-contained) 같이 짜여있어서 책 뼈대는 유지되거든요! 안녕히 가세요! 

---

## Sub-Chapters (하위 목차)

[< 1.2 A Brief History Of Statistical Learning](../1_2_a_brief_history_of_statistical_learning/trans2.html) | [1.4 Who Should Read This Book >](../1_4_who_should_read_this_book/trans2.html)
