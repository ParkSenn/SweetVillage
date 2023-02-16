from django.contrib import admin
from django.urls import path
from sweetapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # runserver 테스트 용 path('', views.testapp, name='home'),
]
