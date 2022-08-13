from django.db import models

# 데이터베이스 테이블
# todo 테이블 = title, description, created(작성날짜), complete(todo 완료여부), important(todo 중요도)
# create table todo(title varchar2(100), desce varchar(1000).....)


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + " " + self.description
