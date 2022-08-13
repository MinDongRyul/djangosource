from pydoc import describe
from django.db import models

# 제목, 상세설명, 생성날짜, 종료여부, 중요여부
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
