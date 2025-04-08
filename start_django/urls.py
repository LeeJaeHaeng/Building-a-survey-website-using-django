from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

# 루트 URL을 위한 간단한 뷰 함수
def home_view(request):
    return HttpResponse("Django 홈페이지에 오신 것을 환영합니다! <a href='/polls/'>설문조사 앱으로 이동</a>")

urlpatterns = [
    path('', home_view, name='home'),  # 루트 URL 패턴 추가
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]