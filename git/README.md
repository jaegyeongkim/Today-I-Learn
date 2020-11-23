# Git

[TOC]

## Why Git?

함께 일하는 사람들이 버전 관리를 쉽게하기 위해

## Git 구조

![1](assets/1.PNG)

## git 명령어

### git 초기 설정

git에 대한 모든 설정 확인할 수 있음

```bash
git config --list
```

git 설정을 파일로 확인하고 싶다.

```bash
git config --global -e
```

현재 디렉토리에서 visualcode를 열고 싶다.

```bash
code .
```

git config --global -e 명령어를 수행하는 방법 2가지

```bash
# VScode로 열겠다.
git config --global core.editor "code"
# VScode로 열고 끝날때까지 terminal을 기다리게 한다.
git config --global core.editor "code --wait"
```

git 설정에 이름, 이메일 설정

```bash
git config --global user.name "Jake"
git config --global user.email "tkwk1205@naver.com"
git config user.name
Jake
git config user.email
tkwk1205@naver.com
```

새로운 줄바꿈 설정

```bash
git config --global core.autocrlf true
```

git 시작

```bash
git init
```

git 삭제

```bash
rm -rf .git
```

git 상태 확인

```bash
git status
```

git 단축키 설정

```bash
git config --global alias.st status
git st
```

git 명령어, 속성값 확인

```bash
git config --h
```

### git add

디렉토리에 있는 모든 파일 추가

```bash
git add *
```

디렉토리에 있는 모든 파일들을 추가에서 git stagin area에 추가

```bash
git add .
```

git add 된 거 지우기

```bash
git rm --cahced -r .
```

특정 형식의 파일만 add

```bash
git add *.파일형식
```

### git ignore

git ignore 파일 생성

```bash
echo *.log > .gitignore
```

### git status

git status 에 대한 옵션을 더 확인 (help 옵션 추가)

```bash
git status -h
```

git status 를 단축어로 확인

```bash
git status -s
```

### 파일 비교 diff

정확하게 어떤 파일의 내용이 수정되었는지 확인

```bash
git diff
git diff --staged
git diif -h
```

VScode를 이용해서 수정된 내용 확인하기

```bash
[diff]
    tool = vscode
[difftool "vscode"]
    cmd = code --wait --diff #LOCAL $REMOTE
```

```basg
git difftool
```

staging Area 에 있는 수정된 내용 확인하기

```bash
git difftoole --staged
```

### git commit

commit 추가

```bash
git commit -m "커밋 메시지"
```

commit 내역 확인

```bash
git log
```

staging area와 working directory에 있는 모든 파일을 commit 메시지와 함께 commit

```bash
git commit -am "커밋 메시지"
```

### commit 팁

1. commit 1, 2, 3 이런식으로 작성 X

2. 현재형 동사형으로 commit 메시지 작성

3. commit 메시지에 맞는 것만 작성 

   ex) Fix면 Fix만 작성해서 올려야지 Add 등 작성해서 한꺼번에 올리는 거 X

## 그냥 명령어

디렉토리 만들기

```bash
mkdir 이름
```

폴더 이동

```bash
cd 폴더 이름
```

파일 확인

```bash
ls -al
```

`hello world!` 문장이 담긴`a.text` 파일 만들기

```bash
echo hello world! > a.text
```

파일 지우기

```bash
rm 파일 이름
```

파일 내용 확인

```bash
cat 파일 이름
```



