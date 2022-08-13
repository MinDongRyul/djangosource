from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from ..models import Question, Answer
from ..forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 로그인 확인이 필요할 때
@login_required(login_url="common:login")
def answer_create(request, question_id):
    """
    답변 등록
    """
    # question_id 를 사용해 질문 가져오기
    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            # 작성자 추가(현재 로그인 사용자 : request.user)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # http://127.0.0.1:8000/board/305#answer_07
            # return redirect("board:detail", question_id=question_id)

            # detail에서 특정 영역 보여주기
            # resolve_url() : 실제 호출되는 URL을 문자열로 반환
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:detail", question_id=question_id), answer.id
                )
            )
    else:
        form = AnswerForm()

    context = {"question": question, "form": form}

    return render(request, "board/question_detail.html", context)

    # Answer 객체를 생성한 후 저장 - 모델 폼을 사용하지 않을 때
    # answer = Answer(
    #     question=question,
    #     content=request.POST.get("content"),
    #     create_date=timezone.now(),
    # )
    # answer.save()

    # 답변등록 후 상세 보기 페이지로 이동
    # board/2
    # return redirect("/board/{}".format(question_id), question_id=question_id)


@login_required(login_url="common:login")
def answer_modify(request, answer_id):
    """
    답변 수정 - 원본 내용 찾은 후 수정
    """

    # answer_id 값에 맞는 질문 찾아오기
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, "수정할 권한이 없습니다.")
        return redirect("board:detail", question_id=answer.question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        # 유효성 검증
        if form.is_valid():
            answer = form.save(commit=False)
            # 추가 정보 - 작성자, 수정 날짜
            answer.author = request.user
            answer.modify_date = timezone.now()
            # db 반영
            answer.save()
            # 이동
            # return redirect("board:detail", question_id=answer.question_id)
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:detail", question_id=answer.question_id),
                    answer.id,
                )
            )
    else:
        form = AnswerForm(instance=answer)

    return render(request, "board/answer_form.html", {"form": form})


@login_required(login_url="common:login")
def answer_delete(request, answer_id):
    """
    답변 삭제
    """
    # 삭제할 데이터 찾기
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, "삭제할 권한이 없습니다.")
        return redirect("board:detail", question_id=answer.question_id)

    answer.delete()

    return redirect("board:detail", question_id=answer.question_id)
