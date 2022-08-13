from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from ..models import Comment, Question, Answer
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="common:login")
def comment_create_question(request, question_id):
    """
    질문 댓글
    """
    # 게시물 번호 가져오기
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # 추가작업(폼에서 안한 작업)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            # return redirect("board:detail", question_id=question_id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", question_id=question_id),
                    comment.id,
                ),
            )

    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_modify_question(request, comment_id):
    """
    질문 댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, "수정할 권한이 없습니다.")
        return redirect("board:detail", question_id=comment.question_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            # return redirect("board:detail", question_id=comment.question_id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", question_id=comment.question_id),
                    comment.id,
                ),
            )
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_delete_question(request, comment_id):
    """
    질문 댓글 삭제
    """

    # 삭제할 데이터 찾기
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, "삭제할 권한이 없습니다.")
        return redirect("board:detail", question_id=comment.question_id)

    comment.delete()

    return redirect("board:detail", question_id=comment.question_id)


# ----------------------- answer comment -------------------------------------------------


@login_required(login_url="common:login")
def comment_create_answer(request, answer_id):
    """
    답변 댓글
    """
    # 질문 댓글 번호 가져오기
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # 추가작업(폼에서 안한 작업)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            # return redirect("board:detail", question_id=answer.question_id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", question_id=answer.question_id),
                    comment.id,
                ),
            )
    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_modify_answer(request, comment_id):
    """
    답변 댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, "수정할 권한이 없습니다.")
        return redirect("board:detail", question_id=comment.answer.question_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            # return redirect("board:detail", question_id=comment.answer.question_id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", question_id=comment.answer.question_id),
                    comment.id,
                ),
            )
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_delete_answer(request, comment_id):
    """
    답변 댓글 삭제
    """

    # 삭제할 데이터 찾기
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, "삭제할 권한이 없습니다.")
        return redirect("board:detail", question_id=comment.answer.question_id)

    comment.delete()

    return redirect("board:detail", question_id=comment.answer.question_id)
