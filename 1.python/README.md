### Python 내용 요약, 오답정리 등

<hr/>

### git 만들기

```bash
$ git init

$ touch .gitignore    # gitignore.io 사이트 들어가서 (윈도우, 파이썬, vscode, 맥) 추가해서 생성 -> 복사해서 붙여넣기

$ touch README.md     # 관련 코드나 내용 끄적끄적 후기같은 코딩 일기

$ git status

$ git add .

$ git status

$ git commit -m "파일명 입력(상관없음)"

#깃랩에서 새로운 new projets 만든 후 아래에 있는거 복붙
$ git remote add origin https://new_projects 주소.git

$ git push origin master
 
```



### git 푸쉬

```bash
git bash에서..
$ git status #빨간색 파일색

$ git add .

$ git status #초록색 파일색

$ git commit -m "파일명 입력"

($ git status #nothing이 나와야함)

$ git push
```



### 이전 commit 수정

```bash
$ git commit --amend

> i 누르고 끼워넣기 상태로 수정
> esc 끼워넣기 모드 취소
> :wq 저장명령 주기
```



### pull request

```bash
# branch 삭제 후 변경사항 pull 받기
(브랜치 상관 없음)
$ git switch master

(master)
$ git pull origin master

(김해킹)
$ git add 김해킹.py  # 파일 단위로 add
$ git commit -m 'comment'
$ git switch -c <김해킹>
$ git push origin 김해킹


# pull request 이후 기존 branch 삭제
(김해킹)
$ git switch master

(master)
$ git pull origin master  
$ git branch -d 김해킹
```

