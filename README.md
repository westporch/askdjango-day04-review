# AskDjango Day4 오프라인 강의 복습

## 강의

날짜: 2017.07.16(일) 13:00 ~ 17:00

장소: [모임플러스](http://map.naver.com/?mapmode=0&lng=f27e089e43904d8797309ac76534197c&pinId=32514029&lat=25d147cf133d88881094ba67f6383ba8&dlevel=11&enc=b64&pinType=site)

## 수업 내용

### 장고 모델과 마이그레이션

더 이상 습관적으로 makemigrations/migrate 명령을 입력하지 마세요. 데이터는 방어적/보수적으로 관리해야합니다. 마이그레이션에 대해서 정확히 이해하고, 우리의 소중한 데이터를 안전하게 관리해봅시다.

### 장고 모델을 통한 추가/수정/삭제/조회 구현

장고의 핵심 기능인 모델을 잘 활용하신다면, 많게는 60~70% 이상의 코드를 절감하실 수 있습니다. 모델을 잘 이해하고, 데이터를 효율적으로 관리해봅시다.

## 테스트 환경

| 항목 | 내용 |
| :--: | :--: |
| Django | v1.11.3 |
| Python | v3.5 |
| Django-debug-toolbar | v1.8 |

### 사용 방법

```
# git clone https://github.com/westporch/askdjango-day04-review.git
# cd YOUR_PATH/askdjango-day04-review/myenv/bin
# source activate
(myenv) # pip3 install django==1.11.3
(myenv) # pip3 install django-debug-toolbar==1.8
```

## python3 manage.py shell 실행

```pycon
(myenv) root@django-review> python3 manage.py shell                                                                     ~/git/askdjango-day04-review/dev/askdjango
Python 3.5.3 (default, Jan 19 2017, 14:11:04)
[GCC 6.3.0 20170118] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

모든 포스트 가져오기

```pycon
>>> from blog.models import Post
>>> Post.objects.all()
<QuerySet [<Post: 볼트, 은퇴무대 마지막 리허설 9초95 우승>, <Post: [사설]남북 군사회담 무산됐지만 포기할 때 아니다>, <Post: [주말흥행기상도] '덩케르크'-'스파이더맨' 쌍끌이 흥행>, <Post: [할리웃POP]'원더우먼2'부터 '배트걸'..DC 신작 8편 전격 공개(공식)>, <Post: [클래식 프리뷰] 서울과 전북, 20일 만에 다시 만난 전설매치>, <Post: PC는 사라질 것인가>, <Post: "비 오면 공기 맑아진다고?" 장마철에도 미세먼지 '나쁨'>, <Post: [ICC 리뷰] '네이마르 멀티골' 바르사, 유벤투스에 2-1 승...2위 등극>, <Post: [날씨] 서울·경기 북부 호우경보...시간당 60mm 폭우>]>
```

for문으로 전체 포스트를 가져옴.

```pycon
>>> for post in Post.objects.all():
...     print(post.id, post.title, post.created_at)
...
9 볼트, 은퇴무대 마지막 리허설 9초95 우승 2017-07-23 01:19:28.879631+00:00
8 [사설]남북 군사회담 무산됐지만 포기할 때 아니다 2017-07-23 01:17:58.712018+00:00
7 [주말흥행기상도] '덩케르크'-'스파이더맨' 쌍끌이 흥행 2017-07-23 01:13:32.513975+00:00
6 [할리웃POP]'원더우먼2'부터 '배트걸'..DC 신작 8편 전격 공개(공식) 2017-07-23 01:10:49.588494+00:00
5 [클래식 프리뷰] 서울과 전북, 20일 만에 다시 만난 전설매치 2017-07-23 01:07:44.254394+00:00
4 PC는 사라질 것인가 2017-07-23 01:06:23.863275+00:00
3 "비 오면 공기 맑아진다고?" 장마철에도 미세먼지 '나쁨' 2017-07-23 01:04:35.607217+00:00
2 [ICC 리뷰] '네이마르 멀티골' 바르사, 유벤투스에 2-1 승...2위 등극 2017-07-23 01:03:21.039601+00:00
1 [날씨] 서울·경기 북부 호우경보...시간당 60mm 폭우 2017-07-23 01:01:02.545320+00:00
```

새로운 포스트 작성

```pycon
>>> Post.objects.create(author='YTN', title='[날씨] 수도권 강타한 장맛비...청주 폭우보다 강했다', content='이번 비는 시간당 96mm의 물 폭탄을 동반해 지난주 청주를강타했던 폭우보다 더 강했습니다.')
<Post: [날씨] 수도권 강타한 장맛비...청주 폭우보다 강했다>
```

DB에 엑세스하는 시기

```pycon
>>> qs = Post.objects.all() --> DB 엑세스가 이루어지지 않아서 데이터를 가져오지 않았음.
>>> qs --> 이때 DB 엑세스를 수행해서 데이터를 가져온다.
<QuerySet [<Post: [날씨] 수도권 강타한 장맛비...청주 폭우보다 강했다>, <Post: 볼트, 은퇴무대 마지막 리허설 9초95 우승>, <Post: [사설]남북 군사회담 무산됐지만 포기할 때 아니다>, <Post: [주말흥행기상도] '덩케르크'-'스파이더맨' 쌍끌이 흥행>, <Post: [할리웃POP]'원더우먼2'부터 '배트걸'..DC 신작 8편 전격 공개(공식)>, <Post: [클래식 프리뷰] 서울과 전북, 20일 만에 다시 만난 전설매치>, <Post: PC는 사라질 것인가>, <Post: "비 오면 공기 맑아진다고?" 장마철에도 미세먼지 '나쁨'>, <Post: [ICC 리뷰] '네이마르 멀티골' 바르사, 유벤투스에 2-1 승...2위 등극>, <Post: [날씨] 서울·경기 북부 호우경보...시간당 60mm 폭우>]>
```

포스트 3개를 가져오기

```pycon
>>> Post.objects.all()[:3]
<QuerySet [<Post: [날씨] 수도권 강타한 장맛비...청주 폭우보다 강했다>, <Post: 볼트, 은퇴무대 마지막 리허설 9초95 우승>, <Post: [사설]남북 군사회담 무산됐지만 포기할 때 아니다>]>
```

쿼리셋을 리스트 혹은 투플로 변환하는 것은 자제해야 함.
예를 들어 10만개를 리스트를 구성해서 메모리에 올린 후 거기서 3개의 포스트를 가져오면 부하가 크다.

```pycon
>>> list(Post.objects.all()[:3])
[<Post: [날씨] 수도권 강타한 장맛비...청주 폭우보다 강했다>, <Post: 볼트, 은퇴무대 마지막 리허설 9초95 우승>, <Post: [사설]남북 군사회담 무산됐지만 포기할 때 아니다>]
```
