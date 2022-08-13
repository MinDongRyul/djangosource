from django.contrib import admin

from .models import Book

# 모델을 어드민에서 볼 때 보고 싶은 필드 지정
class BookAdmin(admin.ModelAdmin):
    list_display = ("bid", "title", "author")


admin.site.register(Book, BookAdmin)
