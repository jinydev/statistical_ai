---
layout: default
title: "trans1"
---

[< 2.3 Lab Introduction To Python](../trans1.html) | [2.3.2 Basic Commands >](../2_3_2_basic_commands/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 2.3.1 Getting Started_

# 2.3.1 시작하기_

To run the labs in this book, you will need two things:

이 책의 실습실(labs)들을 실행하기 위해, 여러분은 두 가지를 필요로 할 것입니다:

1. An installation of `Python3`, which is the specific version of `Python` used in the labs.

1. `Python3`의 설치본, 이것은 실습에서 사용되는 `Python`의 구체적인 버전입니다.

2. Access to `Jupyter`, a very popular `Python` interface that runs code through a file called a _notebook_.

2. `Jupyter`에의 접근 권한, 이것은 _노트북(notebook)_ 이라 불리는 파일을 통하여 코드를 실행하는 매우 대중적인 `Python` 인터페이스입니다.

You can download and install `Python3` by following the instructions available at `anaconda.com`.

당신은 `anaconda.com`에서 사용 가능한 지시사항들에 따름으로써 `Python3`를 다운로드하고 설치할 수 있습니다.

There are a number of ways to get access to `Jupyter`. Here are just a few:

`Jupyter`에 접근 권한을 얻는 데에는 많은 수의 방식들이 있습니다. 여기에 단지 몇 가지가 있습니다:

1. Using Google’s `Colaboratory` service: `colab.research.google.com/`.

1. 구글의 `Colaboratory` 서비스의 사용: `colab.research.google.com/`.

2. Using `JupyterHub`, available at `jupyter.org/hub`.

2. `jupyter.org/hub`에서 사용 가능한, `JupyterHub`의 사용.

3. Using your own `jupyter` installation. Installation instructions are available at `jupyter.org/install`.

3. 여러분 자신의 `jupyter` 설치본의 사용. 설치 지시사항들은 `jupyter.org/install`에서 사용 가능합니다.

Please see the `Python` resources page on the book website `statlearning.com` for up-to-date information about getting `Python` and `Jupyter` working on your computer.

여러분의 컴퓨터에서 `Python`과 `Jupyter`가 작동하도록 얻어내는 것에 관한 최신 정보를 위해 책 웹사이트 `statlearning.com`의 `Python` 자원들 페이지를 보십시오.

You will need to install the `ISLP` package, which provides access to the datasets and custom-built functions that we provide.

우리가 제공하는 데이터 세트들과 맞춤-구축된 함수들에 접근 권한을 제공하는 `ISLP` 패키지를 당신은 설치할 필요가 있을 것입니다.

Inside a macOS or Linux terminal type `pip install ISLP`; this also installs most other packages needed in the labs.

macOS 또는 리눅스 터미널 안에서 `pip install ISLP`를 타이핑하십시오; 이것은 또한 실습실들 내에서 필요로 되어지는 대부분의 기타 패키지들을 덩달아 설치합니다.

The `Python` resources page has a link to the `ISLP` documentation website.

`Python` 자원들 페이지는 `ISLP` 문서화 웹사이트에 링크를 가지고 있습니다.

To run this lab, download the file `Ch2-statlearn-lab.ipynb` from the `Python` resources page.

이 실습을 실행하기 위해서, `Python` 자원들 페이지로부터 파일 `Ch2-statlearn-lab.ipynb`를 다운로드 하십시오.

Now run the following code at the command line: `jupyter lab Ch2-statlearn-lab.ipynb`.

이제 명령줄 상에서 다음의 명령 코드를 실행하십시오: `jupyter lab Ch2-statlearn-lab.ipynb`.

If you’re using Windows, you can use the `start menu` to access `anaconda`, and follow the links.

만약 여러분이 윈도우즈를 사용하고 있다면, 여러분은 `anaconda`에 접근하기 위해 `시작 메뉴(start menu)`를 사용할 수 있으며 연결되는 링크들을 따라갈 수 있습니다.

For example, to install `ISLP` and run this lab, you can run the same code above in an `anaconda` shell.

예를 들어, `ISLP`를 설치하고 이 실습을 실행하기 위해, 여러본은 하나의 `anaconda` 쉘 내부에서 동일하게 위의 코드를 실행할 수 있습니다.

---

## Sub-Chapters (하위 목차)

[< 2.3 Lab Introduction To Python](../trans1.html) | [2.3.2 Basic Commands >](../2_3_2_basic_commands/trans1.html)
