---
layout: default
title: "trans2"
---

[< 2.3 Lab Introduction To Python](../trans2.html) | [2.3.2 Basic Commands >](../2_3_2_basic_commands/trans2.html)

> 💡 **학습 팁:** 문법과 코드가 낯설고 어렵다면? 튜터와 함께 실습하듯 쉽게 풀어쓴 [📖 파이썬 랩(Lab) 해설판보기](./trans2.html)를 추천합니다! (직역본은 [📖 직역본 보기](./trans1.html) 메뉴를 활용하세요!)

# 2.3.1 Getting Started

# 2.3.1 시작하기 (파이썬 무기 장착!)

To run the labs in this book, you will need two things:
앞으로 이 책에 나오는 모든 실습 미션들을 성공적으로 완수하려면, 먼저 여러분 컴퓨터에 두 가지 필수 전투 장비(things)가 꼭 깔려 있어야 합니다:

1. An installation of `Python3`, which is the specific version of `Python` used in the labs.
**첫째!** 머신러닝의 표준 총알인 `Python3` 최신 버전 설치본입니다. 이 책의 모든 코드는 오직 이 `Python 3.x` 스펙 버전에서만 정상 작동하도록 설계되어 있습니다.

2. Access to `Jupyter`, a very popular `Python` interface that runs code through a file called a _notebook_.
**둘째!** 코딩용 고급 스케치북인 `주피터(Jupyter)` 접근 권한입니다. 이 녀석은 우리가 짠 파이썬 코드들을 흔히 _노트북(notebook)_ 이라 부르는 아름다운 파일 화면 위에서 실시간으로 팡팡 실행시켜 주는 요즘 가장 핫한 프로그래밍 인터페이스입니다.

You can download and install `Python3` by following the instructions available at `anaconda.com`.
어떻게 둘 다 까냐구요? 너무 쫄지 마세요. 그냥 인터넷 창을 켜고 `anaconda.com` 웹사이트에 들어가서 하라는 대로 '다음, 다음' 지시사항(instructions) 버튼만 신나게 누르며 다운로드 설치하다 보면, 알아서 여러분 컴퓨터에 `Python3` 뼈대가 통째로 박힙니다.

There are a number of ways to get access to `Jupyter`. Here are just a few:
게다가 이 '주피터 스케치북'에 접속하는 방법조차 요즘엔 세상이 좋아져서 여러 가지 지름길(a number of ways)이 뻥뻥 뚫려 있습니다. 대표적인 3대장 루트를 살짝 보여드릴게요:

1. Using Google’s `Colaboratory` service: `colab.research.google.com/`.
**루트 1.** 구글 형님이 공짜로 빌려주는 클라우드 대여 서비스 `Colaboratory(줄여서 코랩)` 활용하기! (`colab.research.google.com/` 접속) -> 그냥 구글 계정만 있으면 컴퓨터에 뭐 안 깔아도 인터넷 창에서 바로 파이썬 코딩이 팡팡 돌아갑니다!

2. Using `JupyterHub`, available at `jupyter.org/hub`.
**루트 2.** 대학이나 회사 서버에서 단체로 제공해 주는 `JupyterHub` 네트워크망 주소(`jupyter.org/hub`) 타고 꼽사리 끼어 사용하기.

3. Using your own `jupyter` installation. Installation instructions are available at `jupyter.org/install`.
**루트 3.** (가장 흔한 정석) 내 개인 컴퓨터 앞마당에 직접 `jupyter`를 통째로 설치해서 쓰기! 이 설치 비법들은 `jupyter.org/install` 문서에서 낱낱이 찾아볼 수 있습니다.

Please see the `Python` resources page on the book website `statlearning.com` for up-to-date information about getting `Python` and `Jupyter` working on your computer.
혹시 내 똥 컴퓨터에서 파이썬과 주피터를 어떻게 돌아가게 만들지 아직도 막막하시다면, 망설이지 말고 이 책 공식 웹사이트인 `statlearning.com` 안의 `Python` 정보 자료실을 클릭해 최신 꿀팁과 가이드 정보(up-to-date information)를 확인해 보십시오!

You will need to install the `ISLP` package, which provides access to the datasets and custom-built functions that we provide.
자, 스케치북을 깔았으니 이제 전용 물감(패키지)을 챙겨야죠? 당장 우리 책의 실습을 뛸 때 쓸 통계 데이터 세트들과 교수님들이 미리 마법처럼 잘 짜놓은 유용한 맞춤형 툴 함수(custom-built functions) 무기들을 마음껏 꺼내 쓰려면 반드시 **`ISLP`** 라는 기특한 외부 추가 패키지 꾸러미를 설치해야 합니다.

Inside a macOS or Linux terminal type `pip install ISLP`; this also installs most other packages needed in the labs.
설치는 아주 쉽습니다! 맥북(macOS)이나 리눅스는 그냥 시커먼 터미널 창을 켜서 마법의 주문 **`pip install ISLP`** 만 치고 기합을 넣으세요! (윈도우라면 아나콘다 프롬프트를 켜고요!) 이 주문 한 방이면 앞으로 책 전반에 걸쳐 필요할 온갖 잡다한 파이썬 패키지들까지 알아서 몽땅 덩달아 연쇄 설치(also installs)해 줍니다. 

The `Python` resources page has a link to the `ISLP` documentation website.
그 마법 물감 통 `ISLP`에 도대체 무슨 데이터가 들어있냐구요? 궁금하면 위에서 띄워둔 책 웹사이트 `Python` 자원 페이지 속 `ISLP 공식 설명서 링크`를 클릭해 구경해 보세요!

To run this lab, download the file `Ch2-statlearn-lab.ipynb` from the `Python` resources page.
자, 이제 모든 실탄 장전이 끝났습니다. 첫 코딩 실습을 뛰기 위해 저 `Python` 자료실에서 `Ch2-statlearn-lab.ipynb` (2장용 주피터 노트북 파일) 훈련장을 다운로드하여 문서 바탕화면에 모셔다 두세요.

Now run the following code at the command line: `jupyter lab Ch2-statlearn-lab.ipynb`.
그리고 터미널(혹은 프롬프트) 명령줄에서 엔터를 치며 웅장하게 아래 코드를 선포하십시오: `jupyter lab Ch2-statlearn-lab.ipynb`. 짠! 웹 브라우저가 열리며 훈련장이 멋지게 등장할 겁니다.

If you’re using Windows, you can use the `start menu` to access `anaconda`, and follow the links.
덧붙여, 여러분이 불우한 리눅스가 아닌 윈도우(Windows)를 편하게 쓴다면, 골치 아프게 검은 터미널 창 안 켜도 됩니다! 윈도우 화면 왼쪽 깃발 모양 `시작 메뉴(start menu)`를 눌러 초록색 `anaconda` 버튼을 찾고, 아이콘 링크들을 쥐 파먹듯 클릭클릭(follow the links)하다 보면 편하게 훈련장에 진입할 수 있습니다.

For example, to install `ISLP` and run this lab, you can run the same code above in an `anaconda` shell.
요컨대, 앞서 말한 저 마법 패키지 `ISLP`를 깔거나 오늘 실습 코드를 구동시킬 때, 윈도우 유저는 그저 편안하게 저 녹색 뱀 아이콘 셸(`anaconda` shell) 프롬프트 팝업 창 안에서 똑같은 구동 코드를 팍팍 실행(run)해 버리면 그만입니다! 자, 출격 준비 완료!

---

## Sub-Chapters

[< 2.3 Lab Introduction To Python](../trans2.html) | [2.3.2 Basic Commands >](../2_3_2_basic_commands/trans2.html)
