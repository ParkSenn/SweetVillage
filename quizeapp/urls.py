from django.contrib import admin
from django.urls import path, include
from quizeapp import views
from .views import *

app_name = "quizeapp"
urlpatterns = [
    path('new', new, name='new'),#사용자가 퀴즈만들러 가는곳
    path('home', home, name='home'),         
    path('detail/<int:id>', detail, name='detail'),
    path('quiz_home', quiz_home, name='quiz_home'), # 만들어놓은 퀴즈가 없으면 뜨는 화면
    path('quiz/<int:pk>', quiz, name='quiz'), # 퀴즈 푸는 화면
    path('ranking/<int:pk>', ranking, name='ranking'), # 결과 화면
    # path('save_ans/', save_ans, name='saveans'), # 이용자가 입력한 정답 저장 함수
]