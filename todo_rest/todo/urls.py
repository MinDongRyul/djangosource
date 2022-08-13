from django.urls import path

from .views import TodosAPIView

urlpatterns = [
    # http://localhost:8000/todo
    path("", TodosAPIView.as_view()),
]
