from django.contrib import admin

from .models import Todo

# admin 페이지에서 Todo 모델 관리할 수 있도록 등록
admin.site.register(Todo)
