from django.db import models

class Post(models.Model):
	'''
	실습 순서

	1. 모델 정의
    필드가 변경(i.e. title -> name)되면 마이그레이션을 해줘야 한다. 단순히 함수만 추가되는 것은 마이그레이션을 안해도 된다.

	2. python3 manage.py makemigrations blog 실행
	* python3 manage.py makemigrations <app-name>
	* makemigrations 명령은 마이그레이션 파일(초안, 작업지시서)을 생성한다.
	* 모델 파일을 '마이그레이션 파일(작업 지시서)'로 생성한다.
	* DB에 적용하지 않은 작업 지시서는 삭제해도 된다.
	* 하지만 DB에 적용된 작업 지시서는 절대로 삭제하면 안된다.
	* 모델의 내용을 어떻게 DB 적용할지 정의한 것이다.
	* 아직 DB가 생성된 상태는 아니다.
	* title 필드의 이름을 다른 이름(title -> name)으로 변경했다면, 날리고 다시 만들거나 작업지시서에서 이름을 다시 변경(title -> name)한다.
	* 작업지시서가 제대로 만들어졌는지 확인이 필요하다.


	3. blog/migrations/0001_initial.py 파일(작업 지시서) 확인 
	view blog/migrations/0001_initial.py
	* 0001_initial.py 파일이 작업 지시서이다. 이 파일을 열어보면 내역을 확인할 수 있다.

	4. python3 manage.py sqlmigrate blog 0001_initial 명령으로 sql 확인
	* python3 manage.py sqlmigrate <app-name> <migration-name>
	* sql 수행 내역을 확인할 수 있다.
	* blog는 앱 이름을 의미한다.
	* 출력된 sql을 DB에서 그대로 실행해도 작동한다.	

	5. python3 manage.py migrate blog 명령으로 DB에 적용
	* python3 manage.py migrate <app-name>
	* '마이그레이션 파일(작업 지시서)'을 데이터베이스로 생성한다.

	6. python3 manage.py showmigrations blog 명령으로 마이그레이션 현황 확인
	* python3 manage.py showmigrations <app-name>
	* 엑스표시는 마이그레이션이 적용되었다는 것이다.

	7. sqlite 브라우저를 통해 DB 테이블 확인
	* sqlite 브라우저 다운 -> http://sqlitebrowser.org/
	'''

	title = models.CharField(max_length=100)
	'''
	CharField는 길이 제한이 있는 문자열이다.
	DB는 길이 제한이 있는 문자열을 빠르게 잘 찾아낼 수 있다.
	'''
	content = models.TextField() # TextField는 길이 제한이 없는 문자열이다.
	created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True는 글을 포스팅할 때 '생성 시각'을 django가 자동으로 저장한다.
	updated_at = models.DateTimeField(auto_now=True) # auto_now=True는 글의 '갱신 시각'을 django가 자동으로 저장한다.
