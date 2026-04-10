---
layout: default
title: "index"
---

# 2.3.1 Getting Started
# 2.3.1 시작하기

To run the labs in this book, you will need two things:

이 책의 실습을 진행하려면 두 가지가 필요합니다:

1.  An installation of `Python3`, which is the specific version of `Python` used in the labs.
2.  Access to `Jupyter`, a very popular `Python` interface that runs code through a file called a _notebook_.

1. 실습에 사용되는 파이썬 특정 메인 버전인 `Python3` 의 구동 설치.
2. _노트북(notebook)_ 이라 불리는 구조 파일을 통해 분석 코드를 실행해 주는 가장 대중적인 파이썬 인터페이스 프로그램인 `Jupyter` 에 대한 접근.

You can download and install `Python3` by following the instructions available at `anaconda.com`.

안내 웹사이트 `anaconda.com` 의 지침을 따라 환경에 맞게 `Python3` 를 다운로드해 설치할 수 있습니다.

There are a number of ways to get access to `Jupyter`. Here are just a few:

`Jupyter` 환경에 접근하는 방법은 무척 다양합니다. 여기에 대표적인 몇 가지만 짚어봅니다:

1.  Using Google’s `Colaboratory` service: `colab.research.google.com/`.
2.  Using `JupyterHub`, available at `jupyter.org/hub`.
3.  Using your own `jupyter` installation. Installation instructions are available at `jupyter.org/install`.

1. 구글의 `Colaboratory` 서비스 주소 사용: `colab.research.google.com/` 접속.
2. 주소 웹 `jupyter.org/hub` 에서 제공되는 `JupyterHub` 네트워크 사용.
3. 개인 로컬 장비에 직접 `jupyter` 환경을 직접 설치해 기용. 설치 안내는 `jupyter.org/install` 문서에서 확인 가능.

Please see the `Python` resources page on the book website `statlearning.com` for up-to-date information about getting `Python` and `Jupyter` working on your computer.

사용자 개인 측정 컴퓨터에서 `Python` 과 `Jupyter` 환경이 작동하도록 구비하는 자세한 최신 정보는 본 도서의 공식 웹사이트 `statlearning.com` 도메인의 `Python` 리소스 페이지를 참고해 주십시오.

You will need to install the `ISLP` package, which provides access to the datasets and custom-built functions that we provide. 

우리가 이 책의 전 과정에 걸쳐 제공하는 고유 데이터 세트들과 사용자 정의 구축 함수들에 직접 전격 접근하도록 기능하는 필수 `ISLP` 패키지를 설치해야만 합니다.

Inside a macOS or Linux terminal type `pip install ISLP`; this also installs most other packages needed in the labs. 

운영체제 시스템인 macOS 혹은 시스템 Linux 터미널의 커맨드 내부에 명령어 `pip install ISLP` 만을 입력해 보십시오; 이 단순 명령어 동작은 훗날 측정 실습 전체에 요구되는 여타 대다수 필수 데이터 패키지들까지 모두 덤으로 알아서 한꺼번에 설치해 제공해 줍니다. 

The `Python` resources page has a link to the `ISLP` documentation website.

공식 도서의 `Python` 리소스 웹 페이지에는 구비된 `ISLP` 패키지 도큐먼트 설명 문서 웹사이트 주소로 곧장 이동하는 링크도 친절히 구비 정리되어 있습니다.

To run this lab, download the file `Ch2-statlearn-lab.ipynb` from the `Python` resources page. 

이번 챕터의 분석 실습 모의를 구동하려면, 먼저 `Python` 리소스 공식 도표 페이지에서 제공하는 이 챕터 실습 실행 전용 파일인 `Ch2-statlearn-lab.ipynb` 파일 본체를 다운로드 하여 마련하십시오.

Now run the following code at the command line: `jupyter lab Ch2-statlearn-lab.ipynb`.

그런 다음 시스템 외부 커맨드 명령행 조작 라인에서 터미널 접속해 바로 다이렉트로 아래 코드를 실행해 봅니다: 명령어 실행 `jupyter lab Ch2-statlearn-lab.ipynb`.

If you’re using Windows, you can use the `start menu` to access `anaconda`, and follow the links. 

만일 윈도우(Windows) 사용 시스템 체제에 있다면, 환경 시스템 기본의 `시작 메뉴(start menu)` 아이콘에 접근해 눌러 `anaconda` 폴더 단축을 열고 내장 제공되는 링크들을 직관적으로 따라 모의 사용할 수 있습니다.

For example, to install `ISLP` and run this lab, you can run the same code above in an `anaconda` shell.

예컨대 실습 사전 패키지 도출인 `ISLP` 설정 설치와 더불어 당장의 분석 실습 코드를 터미널로 구동하고자 할 시엔, 방금 살펴본 위쪽과 동일한 터미널 명령 코드를 그대로 윈도우 환경 구조용인 `아나콘다 셸(anaconda shell)` 내부에 직접 입력하여 동일하게 실행을 조작 도출하면 됩니다.

---

## Sub-Chapters (하위 목차)

현재 2.3.1 단원 소속 문서입니다.
[상위 경로(Lab: Introduction to Python)로 돌아가기](../)
