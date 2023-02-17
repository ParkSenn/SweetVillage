from django.contrib import admin
from django.urls import include, path
from sweetapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    # runserver 테스트 용 path('', views.testapp, name='home'),
]
