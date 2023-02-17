from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
=======
from django.urls import path, include
>>>>>>> origin
from sweetapp import views
from quizeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('account/',include('account.urls')),
    # runserver 테스트 용 path('', views.testapp, name='home'),
=======
    # path('', home, name='home'), # 메인 화면 띄우기
    path('', include('sweetapp.urls')), # 분류를 해야 할 거 같아서 quize app을 만들긴 했는데... 우선 명확한 기능 분류가 안 됨
    path('', include('quizeapp.urls')), # 퀴즈 관련 화면들
>>>>>>> origin
]
