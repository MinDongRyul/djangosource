from .models import Question, Answer, Comment
from django import forms

# 모델 폼 - 모델과 연결될 폼
# class Meta 반드시 가져야 함


class QuestionForm(forms.ModelForm):  # forms.ModelForm이 자세히 뭘 의미 하는지 모르겠음
    class Meta:
        model = Question
        fields = ["subject", "content"]

        # 에러 메세지가 보여질 때 라벨명이 field명을 이용하기 때문에
        # 영어로 나오는 부분을 원하는 한글로 변경
        labels = {"subject": "제목", "content": "내용"}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]

        # 에러 메세지가 보여질 때 라벨명이 field명을 이용하기 때문에
        # 영어로 나오는 부분을 원하는 한글로 변경
        labels = {"content": "답변 내용"}


# comment 테이블과 연결된 폼 : form.save() -> db반영
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 사용자 한테 입력 받는거만 fields?
        fields = ["content"]
