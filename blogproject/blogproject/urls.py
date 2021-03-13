from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    # html form 이용한 블로그 객체
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form 이용한 블로그 객체생성
    path('djangocreate/', views.djangocreate, name='djangocreate'),

    # django modelform 이용한 블로그 객체생성
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # url/detail/id 로 나타나도록.
    # <int:blog_id>는 detail 함수에 넘길 값
    path('detail/<int:blog_id>', views.detail, name='detail'),

    
]

# media파일에 접근하는 url추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
