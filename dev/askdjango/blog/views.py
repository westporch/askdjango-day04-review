from django.db.models import Q 
''' 예를 들어 OR 구문을 포함한 복잡한 쿼리를 실행하고자 할 때 Q object를 사용한다. 
참고: https://docs.djangoproject.com/en/1.11/topics/db/queries/#complex-lookups-with-q-objects
'''
import os
from .models import Post
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

''' from django.shortcuts import render에 대한 설명

render를 import하지 않고 3~4줄로 작성하는 것은 오래된 코드 방식이다.
간단히 from django.shortcuts import render 1줄로 작성한다.
'''

def post_list(request):
	#print(request.META['REMOTE_ADDR']) # 웹으로 django 접속시 remote host의 ip를 runserver 콘솔에 출력한다.
	qs = Post.objects.all()	# 아직 DB에서 데이터를 가져오지 않았음

	# request.GET['query'] # GET 인자의 query 항목을 가져온다.
	query = request.GET.get('query', '') # request.GET은 GET 인자(URL에서 물음표 뒤에 있는 부분)를 가져온다, query가 없으면 빈 문자열로 설정한다.
	if query:	# 만약 쿼리 값이 존재한다면
		#qs = qs.filter(title__icontains=query) # 제목에서 쿼리를 검색한다, __icontains는 대소문자를 구별하지 않는다.
		condition = Q(title__icontains=query) | Q(content__icontains=query)
		qs = qs.filter(condition)

	return render(request, 'blog/post_list.html', {'post_list': qs, 'query': query, }) # post_list를 qs에 저장함, 'post_list'는 템플릿 변수.

def post_list1(request):
	'FBV: 직접 문자열로 HTML형식 응답하기'

	name = '공유'
	return HttpResponse('''
		<h1>AskDjango</h1>
		<p> {name} </p>
		<p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>'''.format(name=name))

def post_list2(request):
	'FBV: 템플릿을 통해 HTML형식 응답하기'

	print(request.META['REMOTE_ADDR']) # 웹으로 django 접속시 remote host의 ip를 runserver 콘솔에 출력한다.

	name = '공유'
	response = render(request, 'blog/post_list.html', {'name': name})	# 좌 측의 name을 우측의 name으로 넘긴다.
	return response

def post_list3(request):
	'FBV: JSON 형식 응답하기'

	return JsonResponse({
		'message': '안녕, 파이썬&장고',
		'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
	}, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
	'FBV: 엑셀 다운로드 응답하기'
	
	filepath = '/home/westporch/test.xlsx'
	filename = os.path.basename(filepath)

	with open(filepath, 'rb') as f:
		response = HttpResponse(f, content_type='application/vnd.ms-excel')
		# 필요한 응답헤더 세팅
		response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
		return response

#def mysum(request, x):
#	''' 인자: 정수 1개
#    리턴값: URL에 입력한 값(정수 1개)을 리턴하여 웹페이지에 출력한다.
#	사용법(예): 웹브라우저의 주소 창에 아래 주소를 입력한다. (999가 출력된다.)
#				http://192.168.0.17:8080/blog/sum/999/
#	'''
#	return HttpResponse(int(x))

#def mysum(request, x, y):
#	''' 인자: 정수 2개
#    리턴값: URL에 입력한 값(정수 2개)을 더한 뒤 리턴하여 웹페이지에 출력한다.
#	사용법(예): 웹브라우저의 주소 창에 아래 주소를 입력한다. (1000이 출력된다.)
#				http://192.168.0.17:8080/blog/sum/999/1
#	'''
#	return HttpResponse(int(x) + int(y))

def mysum(request, x, y=0, z=0):
	''' 인자: 정수 3개
    리턴값: URL에 입력한 값(정수 3개)을 더한 뒤 리턴하여 웹페이지에 출력한다.
	사용법(예): 웹브라우저의 주소 창에 아래 주소를 입력한다. (1004가 출력된다.)
				http://192.168.0.17:8080/blog/sum/999/1/4
	'''
	return HttpResponse(int(x) + int(y) + int(z))

def greet_korean(request, korean_name, age):
	'''인자: 2개 (한글 이름, 나이)
	리턴값(예): 안녕하세요. 공유. 37살이시네요.
    사용법(예): http://192.168.0.17:8080/blog/hello/%EA%B3%B5%EC%9C%A0/37/
	'''
	return HttpResponse("안녕하세요. {korean_name}. {age}살이시네요.".format(korean_name=korean_name, age=int(age)))
