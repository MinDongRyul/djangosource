from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from ..models import Question
from ..forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 로그인 확인이 필요할 때
@login_required(login_url="common:login")
def question_create(request):
    """
    질문등록
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            # 작성자 추가(현재 로그인 사용자 : request.user)
            question.author = request.user

            question.save()
            return redirect("board:index")
    else:
        form = QuestionForm()

    return render(request, "board/question_form.html", {"form": form})


# 로그인 확인이 필요할 때
@login_required(login_url="common:login")
def question_modify(request, question_id):
    """
    질문 수정(원본 내용 보여준 후 수정)
    """

    # question_id 값에 맞는 질문 찾아오기
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, "수정할 권한이 없습니다.")
        return redirect("board:detail", question_id=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        question = form.save(commit=False)
        question.author = request.user
        question.modify_date = timezone.now()
        question.save()
        return redirect("board:detail", question_id=question_id)
    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_form.html", {"form": form})


# 로그인 확인이 필요할 때
@login_required(login_url="common:login")
def question_delete(request, question_id):
    """
    질문 삭제
    """
    # question_id 질문 찾아오기
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, "삭제할 권한이 없습니다.")
        return redirect("board:detail", question_id=question_id)

    # 삭제
    question.delete()
    return redirect("index")
