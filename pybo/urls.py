from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'), # pybo/까지는 config/urls.py의 url 매핑 // name 속성 추가
    path('<int:question_id>/', views.detail, name='detail'), # name 속성 추가
    path('answer/create/<int:question_id>/',  views.answer_create, name='answer_create'), # answer_create 별명 추가
    path('question/create/', views.question_create,name='question_create'),
]