from django.db import models

# CharField : 문자열(길이제한 필요)
# TextField : 문자열(길이제한 필요없음)
# IntegerField : 정수
# DateField : 날짜
# DateTimeField : 날짜 + 시간
# FileField : 파일
# ImageField : 이미지 파일
# ForeignKey : 외래 키
# OneToOneField : 1:1 관계
# ManyToManyField : 다대다 관계


class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.title + " " + self.author
