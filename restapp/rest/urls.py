from django.urls import path

from .views import *
from rest_framework import routers

routers = routers.SimpleRouter()
routers.register("books", BookViewSet)
urlpatterns = routers.urls


# urlpatterns = [
#     path("hello/", HelloAPI),
#     # 함수형 뷰
#     path("books/", booksAPI),
#     path("books/<int:bid>/", bookAPI),
#     # 클래스 뷰
#     path("cv/books/", booksAPI),
#     path("cv/books/<int:bid>/", bookAPI),
#     # mixin
#     path("mixin/books/", BooksAPIMixins.as_view()),
#     path("mixin/books/<int:bid>/", BookAPIMixins.as_view()),
#     # generics
#     path("gen/books/", BooksAPIMixins.as_view()),
#     path("gen/books/<int:bid>/", BookAPIMixins.as_view()),
# ]
