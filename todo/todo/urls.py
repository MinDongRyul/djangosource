# 장고는 config 안의 urls.py를 통해 request 처리
# 앱 별로 나누어서 request 관리

from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/todo 로 요청이 들어오면
    # 어느 view 를 보여줄 것인지 views.todo_list 가 처리
    # name : url 하드코딩 부분의 축소
    path("", views.todo_list, name="todo_list"),
    # http://127.0.0.1:8000/todo/1
    path("<int:pk>/", views.todo_detail, name="todo_detail"),
    # http://127.0.0.1:8000/todo/new
    path("new/", views.todo_register, name="todo_register"),
]
