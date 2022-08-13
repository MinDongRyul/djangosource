# 시리얼라이저(직렬화, 역직렬화 담당)

from rest_framework import serializers
from .models import Todo

# 전체 조회
class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "complete", "important")


# 상세 조회
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "complete", "important")
