from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import viewsets

from .serializers import BookSerializer
from .models import Book

from django.shortcuts import get_object_or_404


@api_view(["GET"])
def HelloAPI(request):
    return Response("hello world")


###### 함수형 뷰 : 장고 개발시 사용했던 개념


@api_view(["GET", "POST"])
def booksAPI(request):

    if request.method == "GET":
        # book 테이블에 모든 책 정보를 가져오기
        books = Book.objects.all()

        # books 데이터는 파이썬 객체 ==> json 변경해야 함
        # serializer 에 전체 데이터 한번에 넣기
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":  # 도서 정보 입력
        # json -> 파이썬 객체
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def bookAPI(request, bid):
    book = get_object_or_404(Book, bid=bid)

    # 직렬화(파이썬 객체 -> json)
    serializer = BookSerializer(book)

    return Response(serializer.data, status=status.HTTP_200_OK)


# 클래스 뷰 - 함수형 뷰와 하는 일이 같음
#          - 클래스 내에 get과 post를 따로 함수로 정의
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        # 직렬화(파이썬 객체 -> json)
        serializer = BookSerializer(book)

        return Response(serializer.data, status=status.HTTP_200_OK)


#### DRF mixins
class BooksAPIMixins(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookAPIMixins(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "bid"  # pk에 해당하는 필드

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# DRF generics
class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "bid"


# DRF Viewset & Router

# Viewset : 뷰의 집합(여러가지 뷰를 한꺼번에 모아놓음)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
